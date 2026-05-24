# agent-skills

[mattpocock/skills](https://github.com/mattpocock/skills) 五个日常 skill 的**中文版**，彼此独立，按意图分别触发。

参考：[5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)

## 推荐顺序（非合并 skill，仅工作习惯）

```
grill-me-zh → to-prd-zh → to-issues-zh → tdd-zh
                    ↑
     improve-codebase-architecture-zh（周期性，或开发高峰后）
```

## Skill 列表

| 目录 | 对应上游 | 典型触发 |
|------|----------|----------|
| [grill-me-zh](./skills/grill-me-zh/SKILL.md) | `grill-me` | 拷问我、帮我想清楚方案 |
| [to-prd-zh](./skills/to-prd-zh/SKILL.md) | `to-prd` | 写成 PRD、整理需求文档 |
| [to-issues-zh](./skills/to-issues-zh/SKILL.md) | `to-issues` | 拆成 issue、纵向切片 |
| [tdd-zh](./skills/tdd-zh/SKILL.md) | `tdd` | TDD、红绿重构、先写测试 |
| [improve-codebase-architecture-zh](./skills/improve-codebase-architecture-zh/SKILL.md) | `improve-codebase-architecture` | 架构体检、加深模块 |

## 在 Cursor 中使用

将需要的 `skills/<name>-zh` 目录放入 Cursor 的 skills 路径（或在本仓库中引用），对话中说明要用的 skill 名称即可，例如：

- 「用 grill-me-zh 拷问我这个方案」
- 「用 to-prd-zh 把当前对话写成 PRD」

安装上游英文原版（可选）：

```bash
npx skills@latest add mattpocock/skills
```

## 目录结构

```
skills/
├── grill-me-zh/SKILL.md
├── to-prd-zh/
│   ├── SKILL.md
│   └── templates/prd-template.md
├── to-issues-zh/
│   ├── SKILL.md
│   └── templates/issue-slice-template.md
├── tdd-zh/SKILL.md
└── improve-codebase-architecture-zh/SKILL.md
```
