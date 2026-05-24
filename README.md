# agent-skills

面向日常开发的 Agent Skill 探索与实践。

## 技能列表

| Skill | 说明 |
|-------|------|
| [daily-workflow-zh](./skills/daily-workflow-zh/SKILL.md) | 中文五段式工作流：拷问设计 → PRD → 拆 Issue → TDD → 架构加深 |

参考：[5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)（Matt Pocock / AI Hero）

## 在 Cursor 中使用

1. 将本仓库 clone 到本地，或把 `skills/daily-workflow-zh` 复制到你的项目的 `.cursor/skills/`（或 Cursor 设置里配置的 skills 目录）。
2. 在对话中说明意图，例如：
   - 「用日常工作流，先拷问我这个方案」
   - 「按 daily-workflow-zh 写 PRD」
   - 「把这份 PRD 拆成纵向切片的 issue」
3. Agent 会按 [SKILL.md](./skills/daily-workflow-zh/SKILL.md) 中的阶段规则执行。

## 目录结构

```
skills/daily-workflow-zh/
├── SKILL.md              # 主 skill（中文）
└── templates/
    ├── prd-template.md
    └── issue-slice-template.md
```
