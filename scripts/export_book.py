"""Validate the built book and export an offline, single-file reading edition.

Run after: python -X utf8 -m mkdocs build --strict --site-dir build/site
"""
from __future__ import annotations
import argparse
import base64
from collections import Counter
from html import escape
import json
import mimetypes
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

def entries(items):
    for item in items:
        for title, value in item.items():
            if isinstance(value, list):
                yield from entries(value)
            else:
                yield title, value

def site_path(site, source):
    path = Path(source)
    if path.name == "index.md":
        return (site / path.parent / "index.html").resolve()
    return (site / path.with_suffix("") / "index.html").resolve()

def resolve_local(current, href):
    url = urlsplit(href)
    if url.scheme or url.netloc or not url.path:
        return None
    path = (current.parent / unquote(url.path)).resolve()
    if path.is_dir() or url.path.endswith("/"):
        path /= "index.html"
    return path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="build/site")
    parser.add_argument("--output", default="build/植物免疫学-完整书稿.html")
    args = parser.parse_args()
    site = (ROOT / args.site_dir).resolve()
    out = (ROOT / args.output).resolve()
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8-sig"), Loader=yaml.BaseLoader)
    pages = list(entries(config["nav"]))
    page_ids = {site_path(site, source): f"book-{i:02d}" for i, (_, source) in enumerate(pages)}
    errors, articles, stats = [], [], []
    for title, source in pages:
        path = site_path(site, source)
        if not path.exists():
            errors.append(f"Missing page: {source}")
            continue
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        article = soup.select_one("article.md-content__inner")
        if article is None:
            errors.append(f"Missing article: {source}")
            continue
        for node in article.select(".md-content__button, .headerlink"):
            node.decompose()
        # Give the new Markdown chapters the same answer controls as legacy chapters.
        if source.startswith(("learning/ch00", "part6-", "part7-", "part8-", "history/")):
            for heading in article.select("h2"):
                if "自测" not in heading.get_text():
                    continue
                active = None
                for node in list(heading.next_siblings):
                    if getattr(node, "name", None) in ("h1", "h2"):
                        break
                    is_question = (getattr(node, "name", None) == "p"
                                   and node.find("strong") is not None
                                   and re.match(r"^\d+[.．、]",node.get_text(strip=True)))
                    if is_question:
                        active = soup.new_tag("details")
                        summary = soup.new_tag("summary")
                        summary.string = node.get_text(" ",strip=True)
                        active.append(summary)
                        node.insert_before(active)
                        node.decompose()
                    elif active is not None:
                        active.append(node.extract())
        # Catalog controls need the website script; keep the full directories offline.
        for node in article.select(".history-tools"):
            node.decompose()
        for tag in article.select("a[href], img[src]"):
            attr = "href" if tag.name == "a" else "src"
            value = tag[attr]
            target = resolve_local(path, value)
            if value == "#":
                errors.append(f"Empty navigation: {source}")
            if target is not None and not target.exists():
                errors.append(f"Broken {attr}: {source} -> {value}")
            if attr == "src" and urlsplit(value).scheme in ("http", "https"):
                errors.append(f"Remote image prevents offline use: {source} -> {value}")
        for code in article.select("pre code"):
            if re.search(r"<(?:h[1-6]|div|section|p)[ >]", code.get_text()):
                errors.append(f"Escaped chapter HTML: {source}")
        if article.select(".mermaid"):
            errors.append(f"Diagram still needs online rendering: {source}")
        prefix = page_ids[path]
        for i, heading in enumerate(article.select("h2"), 1):
            if not heading.get("id"):
                heading["id"] = f"chapter-sec-{i}"
        old_ids = [node["id"] for node in article.select("[id]")]
        duplicates = [value for value, count in Counter(old_ids).items() if count > 1]
        if duplicates:
            errors.append(f"Duplicate IDs: {source}: {duplicates}")
        mapping = {value: f"{prefix}-{value}" for value in old_ids}
        for node in article.select("[id]"):
            node["id"] = mapping[node["id"]]
        for node in article.find_all(True):
            for key, value in list(node.attrs.items()):
                if isinstance(value, str):
                    node[key] = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{mapping.get(m[1],m[1])})", value)
            for attr in ("aria-labelledby", "aria-describedby"):
                if node.get(attr):
                    node[attr] = " ".join(mapping.get(x,x) for x in node[attr].split())
        for link in article.select("a[href]"):
            url = urlsplit(link["href"])
            if url.scheme or url.netloc:
                continue
            target = resolve_local(path, link["href"]) or path
            if target in page_ids:
                anchor = page_ids[target]
                if url.fragment:
                    anchor += "-" + unquote(url.fragment)
                link["href"] = "#" + anchor
        for img in article.select("img[src]"):
            target = resolve_local(path,img["src"])
            if target is not None and target.exists():
                mime = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
                img["src"] = f"data:{mime};base64," + base64.b64encode(target.read_bytes()).decode("ascii")
                img.attrs.pop("loading", None)
        # Keep explanations available offline and in print even without JavaScript.
        for detail in article.select("details"):
            detail["open"] = ""
        article.name = "section"
        article["class"] = ["book-section"]
        article["id"] = prefix
        for nav in article.select(".breadcrumb, .chapter-nav"):
            nav.decompose()
        text = article.get_text(" ",strip=True)
        stats.append({"title":title,"source":source,"han_characters":len(re.findall(r"[\u4e00-\u9fff]",text)),"tables":len(article.select("table")),"figures":len(article.select("svg, img")),"self_test_questions":len(article.select("details"))})
        articles.append(str(article))
    if errors:
        raise SystemExit("Book validation failed:\n" + "\n".join(errors))
    css = (ROOT/"docs/assets/stylesheets/book-chapter.v2.css").read_text(encoding="utf-8-sig")
    css = re.sub(r"@import[^;]+;", "", css)
    css += (ROOT/"docs/assets/stylesheets/textbook.css").read_text(encoding="utf-8")
    css += '''
html{scroll-behavior:auto;font-size:20px}*{box-sizing:border-box}[hidden]{display:none!important}body{margin:0;background:#faf9f6;color:#24382b}
a{color:#2d7a4f;text-underline-offset:.18em}aside{position:fixed;inset:0 auto 0 0;width:265px;background:#edf1e9;overflow:auto;padding:24px 20px;font:14px/1.7 "Microsoft YaHei",sans-serif;border-right:1px solid #d4dfd2}
aside a{display:block;padding:6px 0;text-decoration:none}aside h2{font-size:20px}main{margin-left:265px;padding:30px 5vw 90px;max-width:1240px}.cover{padding:48px 0 32px;border-bottom:3px solid #285338}.cover h1{font-size:2.5rem;line-height:1.2;margin:15px 0}.cover p{color:#54705d}.book-section{padding-top:40px;margin-bottom:55px;break-before:page}.book-section>.page-wrapper{padding:0;max-width:none;font-size:inherit}.md-typeset table{border-collapse:collapse;display:block;overflow-x:auto;width:100%;font-size:.72rem}.md-typeset td,.md-typeset th{border:1px solid #d8dfd4;padding:10px 12px;vertical-align:top}.md-typeset th{background:#1a472a;color:white}.md-typeset svg{width:100%;height:auto}button{padding:8px 12px;margin:4px 3px 4px 0;border:1px solid #617d61;background:white;color:#274f31;border-radius:5px;cursor:pointer}img{max-width:100%;height:auto}.md-typeset pre{overflow-x:auto}.book-section h1{font-size:1.65rem}input{width:100%;padding:8px;border:1px solid #acbca9;border-radius:4px;background:#fff} .printnote{font-size:14px}
.back-to-toc{position:fixed;right:20px;bottom:20px;padding:9px 15px;border-radius:20px;background:#214c30;color:white;font:14px "Microsoft YaHei",sans-serif;text-decoration:none;z-index:10}@media print{.back-to-toc{display:none!important}}
@media(max-width:1050px){aside{position:static;width:auto;max-height:350px;border-bottom:1px solid #c8d4c4}main{margin:0;padding:24px}.cover h1{font-size:2rem}}
@media print{@page{size:A4;margin:18mm}html{font-size:12pt}aside,.controls{display:none!important}main{margin:0;padding:0;max-width:none}.cover{min-height:190mm;padding-top:45mm}.cover h1{font-size:34pt}.book-section{margin:0;padding-top:0}.md-typeset{font-size:10.5pt;line-height:1.75}.md-typeset table{display:table;width:100%;font-size:9pt}.md-typeset img,.md-typeset svg{max-height:230mm;object-fit:contain}.md-typeset h2,.md-typeset h3{break-after:avoid}.md-typeset .figure,tr{break-inside:avoid}a{color:inherit;text-decoration:none}.page-wrapper .chapter-header{padding-top:10mm}}
'''
    toc = "\n".join(f'<a href="#{page_ids[site_path(site,source)]}">{escape(title)}</a>' for title,source in pages)
    chapter_count = sum(bool(re.match(r"ch\d", Path(source).stem)) for _, source in pages)
    gene_count = sum(source.startswith("history/genes/") and Path(source).name != "index.md" for _, source in pages)
    lab_count = sum(source.startswith("history/labs/") and Path(source).name != "index.md" for _, source in pages)
    revision = escape(config.get("extra", {}).get("book_revision", "持续修订版"))
    paper_viewer = (ROOT / "docs/assets/javascripts/paper-figures.js").read_text(encoding="utf-8")
    html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>植物免疫学 · 完整书稿</title><style>{css}</style></head><body>
<aside id="book-navigation" aria-label="全书目录"><h2>植物免疫学</h2><input id="filter" type="search" aria-label="筛选章节" placeholder="筛选章节"><nav id="toc">{toc}</nav></aside><a class="back-to-toc" href="#book-navigation" aria-label="返回全书目录">目录 ↑</a>
<main class="md-typeset"><header class="cover"><p>从基础概念到机制与证据</p><h1>植物免疫学</h1><p>{chapter_count} 章 · {gene_count} 篇基因研究史 · {lab_count} 篇课题组研究脉络</p><p>学习路线 · 机制图解 · 研究技术 · 自测讲解 · 文献研读</p><p>{revision}　教材扩充与科学校订稿</p><div class="controls"><button onclick="window.print()">打印 / 保存为 PDF</button><button id="answers">收起所有答案</button></div><p class="printnote">本文件内嵌正文与插图，可离线阅读；外部论文链接需联网。教学示意不代表实测结果，证据边界见版本说明。</p></header>{''.join(articles)}</main>
<script>document.getElementById('filter').addEventListener('input',function(){{let q=this.value.toLowerCase();document.querySelectorAll('#toc a').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(q))}});document.getElementById('answers').addEventListener('click',function(){{let open=this.textContent.includes('展开');document.querySelectorAll('details').forEach(d=>d.open=open);this.textContent=open?'收起所有答案':'展开所有答案'}});window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(d=>d.open=true));</script></body></html>'''
    html = html.replace("</body></html>", f"<script>{paper_viewer}</script></body></html>")
    final = BeautifulSoup(html,"html.parser")
    ids = Counter(x["id"] for x in final.select("[id]"))
    if any(n>1 for n in ids.values()):
        raise SystemExit("Duplicate IDs in assembled edition")
    broken = [a["href"] for a in final.select('a[href^="#"]') if unquote(a["href"][1:]) not in ids]
    if broken:
        raise SystemExit(f"Broken offline anchors: {broken}")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(html,encoding="utf-8")
    report={"pages":len(stats),"numbered_chapters":chapter_count,"gene_histories":gene_count,"lab_histories":lab_count,"han_characters":sum(s["han_characters"] for s in stats),"tables":sum(s["tables"] for s in stats),"figure_occurrences":sum(s["figures"] for s in stats),"self_test_questions":sum(s["self_test_questions"] for s in stats),"internal_links":"passed","offline_anchors":"passed","files":stats}
    (out.parent/"book-validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="files"},ensure_ascii=False))
    print(out)

if __name__ == "__main__":
    main()
