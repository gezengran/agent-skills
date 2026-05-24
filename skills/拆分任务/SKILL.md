---
name: 拆分任务
description: |
  将计划、规格或 PRD 拆成可独立领取的 Issue，采用 tracer bullet 纵向切片。
  在用户要把计划变成任务、创建实现工单、或拆分工作时使用。
---

# 拆分任务

把计划拆成**可独立领取**的 Issue，每条为**纵向切片（tracer bullet）**。

## 流程

### 1. 收集上下文

以对话中已有材料为主。若用户传入 Issue 引用（编号、URL 或路径），从跟踪器读取正文与评论。

### 2. 探索代码库（可选）

若尚未探索：了解代码现状。Issue 标题与描述使用项目**领域词汇**，遵守相关 **ADR**。

### 3. 起草纵向切片

每条切片是**细的纵向路径**，贯穿**所有集成层**（如 schema、API、UI、测试），**不是**只做某一层的横向任务。

切片类型：

- **HITL**：需人参与（架构决策、设计评审等）
- **AFK**：Agent 可独立完成并合并

**优先 AFK，减少 HITL。**

原则：

- 每条切片交付一条窄但**完整**的端到端路径
- 完成的切片应可演示或单独验证
- **宁细勿粗**

### 4. 与用户确认

以编号列表展示，每项包含：

- **标题**：简短描述
- **类型**：HITL / AFK
- **阻塞于**：须先完成的其他切片（若有）
- **覆盖的用户故事**：对应 PRD 中的编号（若有）

询问用户：

- 粒度是否合适（太粗 / 太细）？
- 依赖关系是否正确？
- 是否需要合并或再拆？
- HITL / AFK 标记是否准确？

**迭代直到用户批准。**

### 5. 发布到 Issue 跟踪器

对每条已批准的切片创建 Issue，使用下方模板。若项目有「可交给 Agent」类标签，按惯例加上。

按**依赖顺序**创建（先创建被依赖项），以便在「阻塞于」中引用真实 Issue 编号。

**不要**关闭或修改父级 PRD Issue。

## Issue 正文模板

```markdown
## 父级

（若来源是已有 Issue，填链接；否则删除本节）

## 要做什么

简明描述本纵向切片的端到端行为，不要按层罗列实现步骤。

避免具体文件路径或易过时片段。例外：原型片段规则同 PRD。

## 验收标准

- [ ] 条件 1
- [ ] 条件 2
- [ ] 条件 3

## 阻塞于

- #123（阻塞项）

或写：**无，可立即开始**
```

也可使用：[issue-slice-template.md](./templates/issue-slice-template.md)

## 参考

- [To Issues 指南](https://www.aihero.dev/skills-to-issues)
- [Tracer Bullets](https://www.aihero.dev/tracer-bullets)
- 上游：[mattpocock/skills — to-issues](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues)
