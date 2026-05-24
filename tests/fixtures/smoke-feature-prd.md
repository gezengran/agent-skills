# PRD：skill 一键校验脚本（冒烟测试产物）

> 由 **写需求文档** skill 流程生成（测试用，非正式需求）

## 问题陈述

维护多个 SKILL.md 时，手改容易漏掉 frontmatter、目录名不一致或 README 死链。

## 解决方案

提供 `scripts/validate-skills.py`，在 CI 或本地一条命令校验五个 skill 的结构与引用。

## 用户故事

1. 作为维护者，我希望运行一条命令校验所有 skill，以便合并前发现结构问题。
2. 作为贡献者，我希望 README 中的 skill 链接有效，以便文档可点击导航。

## 实现决策

- 模块 `validate-skills`：扫描 `skills/*/SKILL.md`，解析 YAML，校验 `name` 与目录名一致。
- 校验 README 中 `./skills/<名>/SKILL.md` 链接存在。
- 已知 skill 集合与文内 `` `skill名` `` 交叉引用一致。

## 测试决策

- 用 pytest 子进程调用脚本，断言退出码 0 且输出含「结构校验: 通过」。
- 不测 YAML 库内部实现，只测对外行为（退出码与关键输出）。

## 不在范围内

- 不校验 SKILL 正文语义是否与上游 mattpocock/skills 一致。
- 不自动修复文件。

## 其他说明

本 PRD 仅用于 skill 冒烟测试。
