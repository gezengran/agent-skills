# Bases 示例与排错

## Schema 字段

```yaml
filters:          # 全局筛选，作用于所有视图
  and: []
  or: []
  not: []

formulas:
  name: 'expression'

properties:
  prop_name:
    displayName: "Display Name"
  formula.name:
    displayName: "Formula"

summaries:
  custom: 'values.mean().round(3)'

views:
  - type: table | cards | list | map
    name: "View Name"
    limit: 10
    groupBy:
      property: status
      direction: ASC | DESC
    filters:        # 视图级筛选
      and: []
    order:
      - file.name
      - formula.name
    summaries:
      price: Sum
```

## 常用 file 属性

| 属性 | 说明 |
|------|------|
| `file.name` / `file.basename` / `file.path` / `file.folder` / `file.ext` | 名称与路径 |
| `file.ctime` / `file.mtime` | 创建 / 修改时间 |
| `file.tags` / `file.links` / `file.backlinks` | 标签与链接 |
| `file.size` | 字节大小 |

`this`：主内容区指 base 文件本身；嵌入时指宿主笔记；侧栏指当前活动文件。

## 筛选示例

```yaml
filters: 'status == "done"'

filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

filters:
  or:
    - file.hasTag("book")
    - file.hasTag("article")

filters:
  not:
    - file.hasTag("archived")
```

## 公式示例

```yaml
formulas:
  total: "price * quantity"
  status_icon: 'if(done, "✅", "⏳")'
  created: 'file.ctime.format("YYYY-MM-DD")'
  days_old: '(now() - file.ctime).days'
  days_until_due: 'if(due_date, (date(due_date) - today()).days, "")'
```

日期运算单位：`y` `M` `d` `w` `h` `m` `s`。例：`"today() + \"7d\""`。

## 视图类型

**table** — `order` 列 + 可选 `summaries`（Average / Sum / Min / Max / Median / Earliest / Latest / Unique 等）

**cards** — 卡片画廊，适合封面图与描述

**list** — 简洁列表

**map** — 需经纬度属性及 Maps 社区插件

## 完整示例：任务追踪

```yaml
filters:
  and:
    - file.hasTag("task")
    - 'file.ext == "md"'

formulas:
  days_until_due: 'if(due, (date(due) - today()).days, "")'
  priority_label: 'if(priority == 1, "🔴 High", if(priority == 2, "🟡 Medium", "🟢 Low"))'

views:
  - type: table
    name: "Active Tasks"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.priority_label
      - due
      - formula.days_until_due
    groupBy:
      property: status
      direction: ASC
```

## 排错

**YAML 特殊字符未加引号**：含 `:` `{` `}` `[` `]` `,` `#` `|` `>` `=` 等的字符串须加引号。

**公式引号嵌套错误**：

```yaml
# 错
label: "if(done, "Yes", "No")"
# 对
label: 'if(done, "Yes", "No")'
```

**Duration 当数字用**：

```yaml
# 错
"(now() - file.ctime).round(0)"
# 对
"(now() - file.ctime).days.round(0)"
```

**引用未定义公式**：`order` 或 `properties` 中的 `formula.X` 必须在 `formulas` 里定义。
