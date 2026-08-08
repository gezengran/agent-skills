# agent-skills

Agent Skills 合集：日常开发工作流（[mattpocock/skills](https://github.com/mattpocock/skills) 中文版）与 Obsidian 笔记操作技能。

参考：[5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)

## 日常开发工作流

六个 skill 彼此独立，按意图分别触发。`极简实现` 挂在实现阶段，与 `测试驱动` 搭档；推敲 / PRD / 架构时不要默认开启。

### 推荐顺序（工作习惯，非合并 skill）

```
推敲方案 → 写需求文档 → 拆分任务 → 测试驱动 + 极简实现
              ↑
         架构夯实（周期性，或开发高峰后；与极简实现分开触发）
```

### Skill 列表

| 目录 / 名称 | 对应上游 | 典型触发 |
|-------------|----------|----------|
| [推敲方案](./skills/推敲方案/SKILL.md) | `grill-me` | 推敲方案、帮我把方案想透、grill me |
| [写需求文档](./skills/写需求文档/SKILL.md) | `to-prd` | 写成 PRD、整理需求文档 |
| [拆分任务](./skills/拆分任务/SKILL.md) | `to-issues` | 拆成 issue、纵向切片 |
| [测试驱动](./skills/测试驱动/SKILL.md) | `tdd` | TDD、红绿重构、先写测试 |
| [极简实现](./skills/极简实现/SKILL.md) | [ponytail](https://github.com/DietrichGebert/ponytail)（理念） | 极简实现、别过度设计、YAGNI、最简方案 |
| [架构夯实](./skills/架构夯实/SKILL.md) | `improve-codebase-architecture` | 架构夯实、梳理架构、让代码更好改 |

## Obsidian

三个 skill 覆盖 Obsidian vault 的 Markdown 语法、Bases 数据库视图与 CLI 操作。格式与日常开发 skill 一致：主文件精简，细节在 `references/`。

| 目录 / 名称 | 典型触发 |
|-------------|----------|
| [obsidian-markdown](./skills/obsidian-markdown/SKILL.md) | wikilinks、callout、frontmatter、嵌入、Obsidian 笔记 |
| [obsidian-bases](./skills/obsidian-bases/SKILL.md) | `.base` 文件、Bases、表格/卡片视图、筛选、公式 |
| [obsidian-cli](./skills/obsidian-cli/SKILL.md) | 命令行操作 vault、搜索笔记、插件/主题开发调试 |

## 在 Cursor 中使用

将需要的 `skills/<目录名>` 放入 Cursor 的 skills 路径（或在本仓库中引用），对话中说明 skill 名称即可，例如：

- 「用 **推敲方案** 帮我把这个导出功能想透」
- 「用 **极简实现** 写这个日期选择，别过度设计」
- 「用 **obsidian-markdown** 给这篇笔记加上 callout 和属性」

安装上游英文原版（日常开发 skill，可选）：

```bash
npx skills@latest add mattpocock/skills
```

## 目录结构

```
skills/
├── 推敲方案/SKILL.md
├── 写需求文档/
│   ├── SKILL.md
│   └── templates/prd-template.md
├── 拆分任务/
│   ├── SKILL.md
│   └── templates/issue-slice-template.md
├── 测试驱动/SKILL.md
├── 极简实现/SKILL.md
├── 架构夯实/SKILL.md
├── obsidian-markdown/
│   ├── SKILL.md
│   └── references/
├── obsidian-bases/
│   ├── SKILL.md
│   └── references/
└── obsidian-cli/SKILL.md
```

## 测试

```bash
python3 scripts/validate-skills.py
python3 -m pytest tests/ -q
```

详见 [tests/SKILL_SMOKE_TEST_REPORT.md](./tests/SKILL_SMOKE_TEST_REPORT.md)。
