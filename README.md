# agent-skills

[mattpocock/skills](https://github.com/mattpocock/skills) 五个日常 skill 的**中文版**，彼此独立，按意图分别触发。

参考：[5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)

## 推荐顺序（工作习惯，非合并 skill）

```
拷问设计 → 写需求文档 → 拆分任务 → 测试驱动
              ↑
         加深架构（周期性，或开发高峰后）
```

## Skill 列表

| 目录 / 名称 | 对应上游 | 典型触发 |
|-------------|----------|----------|
| [拷问设计](./skills/拷问设计/SKILL.md) | `grill-me` | 拷问我、帮我想清楚方案 |
| [写需求文档](./skills/写需求文档/SKILL.md) | `to-prd` | 写成 PRD、整理需求文档 |
| [拆分任务](./skills/拆分任务/SKILL.md) | `to-issues` | 拆成 issue、纵向切片 |
| [测试驱动](./skills/测试驱动/SKILL.md) | `tdd` | TDD、红绿重构、先写测试 |
| [加深架构](./skills/加深架构/SKILL.md) | `improve-codebase-architecture` | 架构体检、加深模块 |

## 在 Cursor 中使用

将需要的 `skills/<中文目录名>` 放入 Cursor 的 skills 路径（或在本仓库中引用），对话中说明 skill 名称即可，例如：

- 「用 **拷问设计** 拷问我这个方案」
- 「用 **写需求文档** 把当前对话写成 PRD」

安装上游英文原版（可选）：

```bash
npx skills@latest add mattpocock/skills
```

## 目录结构

```
skills/
├── 拷问设计/SKILL.md
├── 写需求文档/
│   ├── SKILL.md
│   └── templates/prd-template.md
├── 拆分任务/
│   ├── SKILL.md
│   └── templates/issue-slice-template.md
├── 测试驱动/SKILL.md
└── 加深架构/SKILL.md
```
