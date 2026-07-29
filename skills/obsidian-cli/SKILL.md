---
name: obsidian-cli
description: |
  通过 Obsidian CLI 读写 vault、搜索笔记、管理任务与属性；支持插件/主题开发与调试。
  在用户要从命令行操作 Obsidian vault、管理笔记、搜索内容，或开发调试插件/主题时使用。
---

# Obsidian CLI

用 `obsidian` 命令与**正在运行的 Obsidian 实例**交互。Obsidian 须已打开。

完整命令列表以 `obsidian help` 为准（始终最新）。文档：[CLI 帮助](https://help.obsidian.md/cli)

## 语法

- **参数**带值：`name="My Note"`（含空格须引号）
- **标志**无值：`silent` `overwrite`
- 多行内容：`\n` 换行、`\t` 制表

## 目标定位

| 参数 | 作用 |
|------|------|
| `file=` | 按 wikilink 解析（无需路径/扩展名） |
| `path=` | vault 根目录起的精确路径，如 `folder/note.md` |
| `vault=` | 指定 vault（放首位），默认最近聚焦的 vault |

未指定 `file` / `path` 时，操作当前活动文件。

## 常用命令

```bash
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

`--copy` 复制输出到剪贴板；`silent` 不打开文件；列表命令加 `total` 只返回计数。

## 插件开发循环

改代码后按此顺序验证：

1. `obsidian plugin:reload id=my-plugin`
2. `obsidian dev:errors` — 有错误则修复后回到 1
3. `obsidian dev:screenshot path=screenshot.png` 或 `obsidian dev:dom selector=".workspace-leaf" text`
4. `obsidian dev:console level=error`

其他：`obsidian eval code="app.vault.getFiles().length"` · `obsidian dev:css selector=".workspace-leaf" prop=background-color` · `obsidian dev:mobile on`

## 参考

- [Obsidian CLI](https://help.obsidian.md/cli)
