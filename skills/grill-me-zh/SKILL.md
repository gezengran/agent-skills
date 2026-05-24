---
name: grill-me-zh
description: |
  就计划或设计方案对用户持续追问，直到达成共同理解；沿设计树逐条分支消解决策依赖。
  在用户要压测方案、拷问设计、或说「拷问我」「grill me」时使用。
---

# 拷问设计（grill-me）

就这个方案的**每个方面**持续追问，直到我们达成**共同理解**。沿**设计树**的每条分支往下走，**一次只解决一个决策**及其依赖。每个问题附上你的**推荐答案**。

**一次只问一个问题。**

若某个问题可以通过探索代码库得到答案，**先去探索代码库**，不要向用户空问。

## 设计树

来自 Brooks《The Design of Design》：设计某功能时，要把决策树上的分支都走通。例如做搜索页：选「高级搜索」还是「简单搜索框」？若选高级搜索，再定筛选、排序……在写 PRD 或代码之前，把这些分叉对齐。

## 行为约束

- 不要过早输出完整计划文档；**对话优先**。
- 复杂功能可能需要很多轮问答，属正常情况。
- 探索代码库时关注：相关模块、现有 API、测试、ADR（若有）。

## 结束

用户表示可以写 PRD、拆任务或开始实现时，再进入后续 skill（如 `to-prd-zh`、`to-issues-zh`）。

## 参考

- [Grill Me 指南](https://www.aihero.dev/skills-grill-me)
- 上游：[mattpocock/skills — grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
