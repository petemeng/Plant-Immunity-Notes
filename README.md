# 植物免疫学：从基础概念到机制与证据

面向初学者的中文植物免疫学习书稿。当前为**第0章基础导论＋8篇27章，共28章**，覆盖细胞基础、识别与信号、NLR、激素、进化、微生物组、屏障与化学防御、系统免疫、根部免疫、育种、证据阅读及常用研究技术。

公网阅读：[GitHub Pages 植物免疫学](https://petemeng.github.io/Plant-Immunity-Notes/)。新增技术篇从 Co-IP、Y2H 讲到表达定位、转录调控、遗传证据与免疫读数，侧重原理、对照和结果解读。

研究史双系列深化版：[32篇经典基因或模块](https://petemeng.github.io/Plant-Immunity-Notes/history/genes/)与[28篇课题组研究脉络](https://petemeng.github.io/Plant-Immunity-Notes/history/labs/)。全部60篇展开关键年表、至少两项代表研究的具体证据与接续问题、模型演进表、原始文献及四道讲解自测，共240题；另有[研究史导览](docs/history/index.md)、跨主题年表和资料署名说明。这60篇专题与28章教材并行，单独统计。

从 [全书导览](docs/index.md) 或 [学习路线](docs/learning/学习路线与知识地图.md) 开始。每章提供导读与带解析的自测；[版本说明](docs/appendix/版本说明与证据边界.md)记录科学校订与尚未完成的出版级审核范围。

新增[免疫与微生物专题](https://petemeng.github.io/Plant-Immunity-Notes/part8-免疫与微生物/)：第24—27章系统讲解群落稳态、根瘤与丛枝菌根、有益微生物与诱导抗性、微生物组测量与因果。四章配12幅原创示意图、24道带解析自测及原始论文研读。

## 当前结构

研究技术篇提供[真实论文原图研读](https://petemeng.github.io/Plant-Immunity-Notes/part7-研究技术与实验逻辑/)，12个案例按问题、原图面板、观察、对照与结论展开。直接展示经核对许可的出版原图，可点击放大；每张附作者、年份、原图号、论文入口和转载许可。第21—23章保留原有方法讲解和25道自测。

- `docs/`: 成书内容（MkDocs 网站）
- `素材库/`: 概念卡、文献笔记、实验方法、领域动态
- `Templates/`: 统一模板（概念卡片、文献笔记）
- `CLAUDE.md`: 写作与整理规则
- `mkdocs.yml`: 网站导航与配置
- `data/history-catalog.json`: 研究史目录及主题分类
- `scripts/build_history_catalog.py`: 从目录数据生成两份索引与导航，`--check` 检查同步及文件名大小写
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

研究史目录调整后运行 `python -X utf8 scripts/build_history_catalog.py`，提交前用 `python -X utf8 scripts/build_history_catalog.py --check` 验证目录与导航一致。网页两份目录支持即时筛选；离线整书保留完整目录，并沿用全书目录搜索。

第0、19、20章的原创插图可用 `scripts/render_learning_figures.py` 重新生成（可选依赖 `matplotlib`）；第17、18章保留 SVG 与 Mermaid 源码。所有构建产物位于已忽略的 `build/`，正文源文件仍在 `docs/`。

研究史中的FLS2、ZAR1、EDS1、NPR1四幅原创教学图可用 `python -X utf8 scripts/render_history_figures.py` 重新生成，无需额外依赖。图示表达概念与证据层次，不是实验数据或原子结构。

第24—27章的12幅原创教学图可用 `python -X utf8 scripts/render_microbiome_figures.py` 重新生成，无需额外依赖。丰度算例为明确标注的虚拟数据。

技术篇的论文原图及来源清单位于 `docs/assets/images/papers/`；运行 `python -X utf8 scripts/check_paper_figures.py` 核验文件与来源记录。图片保留下载时的原始文件，不经绘图脚本生成。网页与离线版均支持点击放大。旧版虚拟案例的生成脚本 `scripts/render_method_cases.py` 留作历史资料，当前原图案例不使用其图片。

## 自动发布

推送到 `main` 或 `master` 分支后，GitHub Actions 会自动构建并发布。

如首次发布，请确认：

1. 仓库 `Settings -> Pages`
2. Source 设为 `GitHub Actions`

## 说明

主发布链路保持 MkDocs，GitHub Actions 默认输出 `site/`。本地修改和构建不会自动提交或推送。正文以机制理解和证据阅读为主；学术引用时请回到原始文献，并留意版本说明中的未核验项与图片许可边界。
