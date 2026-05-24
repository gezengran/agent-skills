# Skill 冒烟测试报告

测试时间：2026-05-24  
测试范围：`skills/` 下五个中文 skill + 交叉引用 + 流程抽样

## 1. 结构校验（自动化）

| 检查项 | 结果 |
|--------|------|
| 5 个目录均有 `SKILL.md` | 通过 |
| YAML `name` 与目录名一致 | 通过 |
| `description` 非空且足够长 | 通过 |
| README 链接可解析 | 通过 |
| 文内 `` `推敲方案` `` 等交叉引用 | 通过 |

命令：

```bash
python3 scripts/validate-skills.py
# 输出: 结构校验: 通过
```

## 2. 分 skill 行为抽样

### 推敲方案

**触发语**：「帮我把 skill 校验 CLI 想透」  
**规则抽检**：一次一问、附推荐、能读库先读库  

**抽样（第 1 问）**  
> 校验失败时你希望怎样反馈：仅退出码非零，还是打印每个 skill 的具体错误列表？  
> **推荐**：打印分 skill 的错误列表，便于 CI 日志定位。

（完整推敲需多轮；此处仅验证格式符合 skill。）

### 写需求文档

**规则抽检**：不重新访谈，综合已有上下文成文  

**产物**：[`tests/fixtures/smoke-feature-prd.md`](./fixtures/smoke-feature-prd.md)（含问题陈述、用户故事、实现/测试决策、不在范围）

### 拆分任务

**输入**：上述冒烟 PRD  
**规则抽检**：纵向切片、AFK/HITL、阻塞关系  

| # | 标题 | 类型 | 阻塞于 | 说明 |
|---|------|------|--------|------|
| 1 | validate-skills 脚本 + 退出码 0 | AFK | 无 | 核心 tracer bullet |
| 2 | README 增加校验命令说明 | AFK | #1 | 文档切片 |
| 3 | GitHub Actions 接入校验 | AFK | #1 | CI 切片 |

### 测试驱动

**规则抽检**：纵向红-绿，不测实现细节  

| 步骤 | 动作 | 结果 |
|------|------|------|
| 红 | `tests/test_validate_skills.py` 断言脚本退出 0 | 先写测试 |
| 绿 | 实现 `scripts/validate-skills.py` | 通过 |
| 测 | `pytest tests/test_validate_skills.py -v` | **1 passed** |

### 架构夯实

**规则抽检**：HTML 写临时目录、不提交仓库  

**产物**：`/tmp/architecture-review-agent-skills-smoke.html`（本机可 `xdg-open` 打开）  
**候选摘要**：建议保持「skill 管流程、脚本管结构校验」的分工。

## 3. 总结

| Skill | 结构 | 流程抽样 |
|-------|------|----------|
| 推敲方案 | 通过 | 通过（首问格式） |
| 写需求文档 | 通过 | 通过（PRD .fixture） |
| 拆分任务 | 通过 | 通过（3 条切片表） |
| 测试驱动 | 通过 | 通过（pytest 绿） |
| 架构夯实 | 通过 | 通过（HTML 已生成） |

**结论**：五个 skill 文件完整、可互相引用；已添加可重复运行的 `scripts/validate-skills.py` 与 pytest 用例，建议在 PR/CI 中执行：

```bash
python3 scripts/validate-skills.py && python3 -m pytest tests/ -q
```

## 4. 未覆盖项（需人在 Cursor 里验证）

- Cursor 是否按 `description` 正确**匹配并加载**各 skill（依赖 IDE 配置路径）
- 长对话下「推敲方案」是否坚持**一次一问**
- 「架构夯实」完整 HTML 报告（含 Mermaid 图）在浏览器中的渲染
