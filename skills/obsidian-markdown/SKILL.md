---
name: obsidian-markdown
description: |
  创建与编辑 Obsidian Flavored Markdown：wikilinks、嵌入、callout、属性等。
  在用户处理 vault 中的 .md 文件，或提到 wikilinks、callout、frontmatter、标签、嵌入、Obsidian 笔记时使用。
---

# Obsidian Markdown

在标准 Markdown 之上使用 Obsidian 扩展语法。vault 内链用 **wikilinks**，外链用 `[text](url)`。

## 流程

1. 顶部加 **frontmatter** 属性（title、tags、aliases）→ [PROPERTIES.md](references/PROPERTIES.md)
2. 正文用标准 Markdown + 下方 Obsidian 语法
3. 用 `[[Note]]` 链 vault 内笔记
4. 用 `![[embed]]` 嵌入笔记、图片、PDF → [EMBEDS.md](references/EMBEDS.md)
5. 用 `> [!type]` 写 callout → [CALLOUTS.md](references/CALLOUTS.md)
6. 在 Obsidian 阅读视图中确认渲染

## 速查

**Wikilinks**

```markdown
[[Note]]                    [[Note|显示名]]
[[Note#标题]]               [[Note#^block-id]]
[[#同页标题]]
```

段落末尾加 `^block-id` 可定义块引用；列表/引用块的 ID 放在块后单独一行。

**嵌入**

```markdown
![[Note]]                   ![[Note#标题]]
![[image.png|300]]          ![[doc.pdf#page=3]]
```

**Callout**

```markdown
> [!note]
> 内容

> [!warning] 自定义标题
> 内容

> [!faq]- 默认折叠
```

常用类型：`note` `tip` `warning` `info` `example` `quote` `bug` `danger` `success` `failure` `question` `abstract` `todo`

**属性**

```yaml
---
title: My Note
tags: [project, active]
aliases: [别名]
---
```

**其他**

```markdown
#tag / #nested/tag          标签
%%隐藏注释%%                阅读视图不可见
==高亮==                    高亮语法
$e^{i\pi}+1=0$              行内公式；块级用 $$
```

Mermaid 图中节点链到笔记：`class NodeName internal-link;`

## 参考

- [PROPERTIES.md](references/PROPERTIES.md) · [EMBEDS.md](references/EMBEDS.md) · [CALLOUTS.md](references/CALLOUTS.md)
- [Obsidian Flavored Markdown](https://help.obsidian.md/obsidian-flavored-markdown) · [Links](https://help.obsidian.md/links) · [Embeds](https://help.obsidian.md/embeds) · [Callouts](https://help.obsidian.md/callouts) · [Properties](https://help.obsidian.md/properties)
