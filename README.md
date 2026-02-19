# Plant Immunity Book

聚焦植物免疫的科学逻辑、研究思路和关键创新发现。

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
pip install "mkdocs<2" "mkdocs-material>=9,<10"
```

启动预览：

```powershell
mkdocs serve
```

构建静态网站：

```powershell
mkdocs build --strict
```

构建输出目录：`site/`

## 自动发布

推送到 `main` 或 `master` 分支后，GitHub Actions 会自动构建并发布。

如首次发布，请确认：

1. 仓库 `Settings -> Pages`
2. Source 设为 `GitHub Actions`

## 说明

仓库中原有 `book/`（Quarto）目录保留为历史沉淀，不再作为主发布路径。
