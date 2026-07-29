---
name: obsidian-bases
description: |
  创建与编辑 Obsidian Bases（.base 文件），含视图、筛选、公式与汇总。
  在用户处理 .base 文件、做笔记数据库视图，或提到 Bases、表格/卡片视图、筛选、公式时使用。
---

# Obsidian Bases

`.base` 文件用 YAML 定义**全局筛选**、**公式属性**、**汇总**与多种**视图**（table / cards / list / map）。先保证 YAML 合法，再在 Obsidian 中打开验证渲染。

## 流程

1. 在 vault 中创建 `.base` 文件
2. 用 `filters` 限定笔记范围（标签、文件夹、属性、日期）
3. 可选：在 `formulas` 中定义计算属性
4. 在 `views` 中配置视图类型与 `order` 列
5. 校验：YAML 无语法错误；`formula.X` 均在 `formulas` 中有定义
6. 在 Obsidian 中打开，确认视图正确

## 最小结构

```yaml
filters:
  and:
    - 'file.hasTag("task")'

formulas:
  days_left: 'if(due, (date(due) - today()).days, "")'

properties:
  formula.days_left:
    displayName: "Days Left"

views:
  - type: table
    name: "Active"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.days_left
```

## 关键规则

- **属性类型**：`note.x`（frontmatter）、`file.x`（文件元数据）、`formula.x`（公式）
- **筛选**：单条字符串，或 `and` / `or` / `not` 嵌套；运算符 `==` `!=` `>` `<` `>=` `<=` `&&` `||` `!`
- **公式引号**：含双引号的表达式用单引号包裹：`'if(done, "Yes", "No")'`
- **日期差**：两日期相减得 **Duration**，须先取 `.days` / `.hours` 等再运算；Duration 不支持直接 `.round()`
- **空值**：属性可能缺失，用 `if(prop, ..., "")` 兜底
- **嵌入**：`![[MyBase.base]]` 或 `![[MyBase.base#View Name]]`

## 参考

- 完整示例与排错：[references/EXAMPLES.md](references/EXAMPLES.md)
- 函数全集：[references/FUNCTIONS_REFERENCE.md](references/FUNCTIONS_REFERENCE.md)
- [Bases Syntax](https://help.obsidian.md/bases/syntax) · [Functions](https://help.obsidian.md/bases/functions) · [Views](https://help.obsidian.md/bases/views)
