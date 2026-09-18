"""Generate the two history directories and navigation from the reviewed catalog.

Run with --check to detect stale directory/navigation output and missing profiles.
The checks cover publishing structure, not scientific accuracy.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "  # BEGIN HISTORY CATALOG\n"
END = "  # END HISTORY CATALOG\n"


def directory(kind, records):
    genes = kind == "genes"
    title = "经典基因研究史" if genes else "课题组研究脉络"
    intro = (
        "这里以基因、家族或协作模块为单位，追踪从表型、身份鉴定到功能与模型修订的过程。"
        "每篇包含关键年表、研究阶段、代表证据、开放问题、原始文献和两道带讲解自测。"
        "多个基因合并讨论时，目录会明确显示模块名称。"
        if genes else
        "这里按研究方向介绍国际与中国研究者的代表性工作。每篇围绕持续问题与关键转折组织，"
        "包含原始论文年表、证据推理、合作归属和两道带讲解自测。负责人姓名是检索入口；"
        "历史成果按论文作者和当时单位归属，本文的研究思路是依据公开成果的编辑归纳。"
    )
    parts = [f"# {title}：{len(records)}篇专题\n\n{intro}\n",
             "[研究史导览](../index.md) · [跨主题年表](../timeline.md) · [资料与署名规则](../sources-and-attribution.md)\n"]
    if genes:
        parts.append("第一次阅读可从[FLS2](FLS2.md)、[RIN4](RIN4.md)、[ZAR1](ZAR1.md)与[NPR1](NPR1.md)开始。想练习判断模型修订，读[Pi-ta](Pi-ta.md)、[XA21](XA21.md)和[MPK3/MPK6](MPK3-MPK6.md)。\n")
    else:
        parts.append("希望理解领域起点，可读[Boller](Boller.md)、[Baker](Baker.md)、[Dangl](Dangl.md)和[Staskawicz](Staskawicz.md)；希望追踪研究对象的持续深化，可读[董欣年](Dong-Xinnian.md)、[Parker](Parker.md)、[周俭民](Zhou-Jianmin.md)和[柴继杰](Chai-Jijie.md)。分类仅用于导航，不表示团队只研究该方向。\n")
    parts.append('<div class="history-tools" hidden>\n<label for="history-filter">筛选本系列目录</label>\n<input id="history-filter" type="search" placeholder="输入名称、基因或研究方向" autocomplete="off">\n<p id="history-filter-status" role="status" aria-live="polite"></p>\n</div>\n')
    groups = defaultdict(list)
    for record in records:
        groups[record[2]].append(record)
    for category, group in groups.items():
        table = f"## {category}\n\n| {'基因或模块' if genes else '研究脉络'} | 阅读焦点 |\n|---|---|\n"
        table += "".join(f"| [{name}]({slug}.md) | {focus} |\n" for slug, name, _, focus in group)
        parts.append(table)
    other = "[课题组系列](../labs/index.md)" if genes else "[经典基因系列](../genes/index.md)"
    parts.append(f"## 怎样继续阅读\n\n读完一篇后，用“问题—证据—认识变化—适用范围”写四句话，再沿文末主题链接进入{other}。"
                 "不同篇章可能引用同一篇合作论文，不能将这些重复引用计作独立验证。"
                 "本批次为代表性教学选编，未覆盖所有基因或所有团队；未收录不表示科学贡献较少。\n")
    return "\n".join(parts)


def navblock(data):
    lines = [START.rstrip("\n")]
    for kind, label in (("genes", "经典基因研究史"), ("labs", "课题组研究脉络")):
        lines += [f"  - {label}:", f"      - 系列目录: history/{kind}/index.md"]
        groups = defaultdict(list)
        for record in data[kind]:
            groups[record[2]].append(record)
        for category, records in groups.items():
            lines.append(f"      - {category}:")
            for slug, name, _, _ in records:
                lines.append(f"          - {name}: history/{kind}/{slug}.md")
    lines.append(END.rstrip("\n"))
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/history-catalog.json").read_text(encoding="utf-8"))
    errors = []
    for kind in ("genes", "labs"):
        records = data[kind]
        if len({r[0] for r in records}) != len(records):
            errors.append(f"Duplicate slug: {kind}")
        output = directory(kind, records)
        path = ROOT / "docs/history" / kind / "index.md"
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != output:
                errors.append(f"Stale directory: {path}")
            actual = {p.name for p in path.parent.glob("*.md")}
            for slug, *_ in records:
                if slug + ".md" not in actual:
                    errors.append(f"Missing or wrong-case profile: {kind}/{slug}.md")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(output, encoding="utf-8")
    config = ROOT / "mkdocs.yml"
    old = config.read_text(encoding="utf-8-sig")
    if START in old:
        before, rest = old.split(START, 1)
        _, after = rest.split(END, 1)
        new = before + navblock(data) + after
    else:
        marker = "  - 附录与复习:\n"
        if marker not in old:
            raise SystemExit("Missing navigation insertion point")
        new = old.replace(marker, navblock(data) + marker, 1)
    if args.check:
        if old != new:
            errors.append("Stale history navigation")
    else:
        config.write_text(new, encoding="utf-8")
    if errors:
        raise SystemExit("\n".join(errors))
    print(json.dumps({"genes": len(data["genes"]), "labs": len(data["labs"]), "mode": "checked" if args.check else "generated"}))


if __name__ == "__main__":
    main()
