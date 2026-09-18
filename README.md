# 植物免疫学：从基础概念到机制与证据

面向初学者的中文植物免疫学习书稿。当前为**第0章基础导论＋7篇23章，共24章**，覆盖细胞基础、识别与信号、NLR、激素、进化、微生物组、屏障与化学防御、系统免疫、根部免疫、育种、证据阅读及常用研究技术。

公网阅读：[GitHub Pages 植物免疫学](https://petemeng.github.io/Plant-Immunity-Notes/)。新增技术篇从 Co-IP、Y2H 讲到表达定位、转录调控、遗传证据与免疫读数，侧重原理、对照和结果解读。

从 [全书导览](docs/index.md) 或 [学习路线](docs/learning/学习路线与知识地图.md) 开始。每章提供导读与带解析的自测；[版本说明](docs/appendix/版本说明与证据边界.md)记录科学校订与尚未完成的出版级审核范围。

## 当前结构

- `docs/`: 成书内容（MkDocs 网站）
- `素材库/`: 概念卡、文献笔记、实验方法、领域动态
- `Templates/`: 统一模板（概念卡片、文献笔记）
- `CLAUDE.md`: 写作与整理规则
- `mkdocs.yml`: 网站导航与配置
- `.github/workflows/deploy.yml`: 自动发布到 GitHub Pages

## 本地预览

先安装依赖：

```powershell
python -m pip install -r requirements-book.txt
```

启动预览：

```powershell
python -X utf8 -m mkdocs serve
```

构建静态网站：

```powershell
python -X utf8 -m mkdocs build --strict --site-dir build/site
```

本地构建输出目录：`build/site/`。使用 `-X utf8` 避免 Windows 控制台编码问题；依赖限定为 MkDocs 1.x，不需要为此迁移站点框架。

## 离线整书阅读版

先运行上面的严格构建，再导出：

```powershell
python -X utf8 scripts/export_book.py
```

输出为 `build/植物免疫学-完整书稿.html`。该文件内嵌正文、样式和插图，双击即可离线阅读，支持目录筛选、答案展开/收起及浏览器打印。外部论文链接仍需联网。`build/book-validation.json` 记录目录页数、编号章节数、可见文本汉字数、图表出现次数及链接检查结果；统计不等于学术准确性认证。

第0、19、20章的原创插图可用 `scripts/render_learning_figures.py` 重新生成（可选依赖 `matplotlib`）；第17、18章保留 SVG 与 Mermaid 源码。所有构建产物位于已忽略的 `build/`，正文源文件仍在 `docs/`。

## 自动发布

推送到 `main` 或 `master` 分支后，GitHub Actions 会自动构建并发布。

如首次发布，请确认：

1. 仓库 `Settings -> Pages`
2. Source 设为 `GitHub Actions`

## 说明

主发布链路保持 MkDocs，GitHub Actions 默认输出 `site/`。本地修改和构建不会自动提交或推送。正文以机制理解和证据阅读为主；学术引用时请回到原始文献，并留意版本说明中的未核验项与图片许可边界。
