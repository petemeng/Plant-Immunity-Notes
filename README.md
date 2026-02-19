# Plant Immunity Notes

植物免疫学学习笔记，包含 PTI、ETI、实验技术等内容。

## 目录结构

```
├── 01-基础知识/          # 基础概念（PTI、ETI等）
├── 02-实验技术/         # 实验方法与技术
├── 03-文献笔记/         # 文献阅读笔记
├── 04-学习规划/         # 学习计划
├── 05-小知识点/         # 零散的知识点
└── images/              # 图片文件
```

## 内容

- **PTI**: PAMP-Triggered Immunity
- **ETI**: Effector-Triggered Immunity
- 植物免疫系统学习路线
- 实验技术笔记

## 更新日志

- 2025-02-19: 初始化仓库
- 2026-02-19: 新增 Quarto Book 原型（`book/`）与 GitHub Pages 自动发布流程

## Book 使用方式

### 同步 Obsidian 笔记到 Book（推荐先做）

```powershell
./scripts/sync-notes-to-book.ps1
```

这一步会自动生成 `book/knowledge/raw-notes.qmd`，并把 `images/` 同步到 `book/images/` 供网页展示。

### 本地预览

```powershell
quarto preview book
```

### 构建静态网页

```powershell
quarto render book
```

构建结果在 `book/_book/`。

### 自动发布到 GitHub Pages

已配置工作流：`.github/workflows/publish-book.yml`

首次启用建议：

1. 在 GitHub 仓库 `Settings > Pages` 中将 Source 设置为 `GitHub Actions`
2. 推送到 `main` 或 `master` 分支后自动发布

自动发布工作流会在以下内容变更时触发：

- `book/**`
- `01-基础知识/**` 到 `05-小知识点/**`
- `images/**`
- `scripts/sync-notes-to-book.ps1`
