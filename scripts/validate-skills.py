#!/usr/bin/env python3
"""校验 skills/ 下各 SKILL.md 的结构与交叉引用。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("需要 PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
KNOWN_SKILLS = frozenset({"推敲方案", "写需求文档", "拆分任务", "测试驱动", "架构夯实"})


def parse_skill(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: 缺少 YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: frontmatter 格式错误")
    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return meta, body


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    found: dict[str, Path] = {}

    if not SKILLS_ROOT.is_dir():
        errors.append(f"目录不存在: {SKILLS_ROOT}")
        return report(errors, warnings)

    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"缺少 SKILL.md: {skill_dir.name}")
            continue
        try:
            meta, body = parse_skill(skill_md)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        name = meta.get("name")
        desc = meta.get("description")
        if not name:
            errors.append(f"{skill_dir.name}: 缺少 name")
        elif name != skill_dir.name:
            warnings.append(
                f"目录名与 name 不一致: 目录={skill_dir.name}, name={name}"
            )
        if not desc or len(str(desc).strip()) < 20:
            warnings.append(f"{name or skill_dir.name}: description 过短")
        if name:
            found[name] = skill_md

        for ref in re.findall(r"`([^`]+)`", body):
            if ref in KNOWN_SKILLS and ref not in found and ref != name:
                pass  # 其他 skill 可能尚未遍历
            if ref in KNOWN_SKILLS and ref not in KNOWN_SKILLS:
                errors.append(f"{skill_dir.name}: 未知引用 `{ref}`")

    for name in KNOWN_SKILLS:
        if name not in found:
            errors.append(f"缺少 skill: {name}")

    readme = ROOT / "README.md"
    if readme.is_file():
        for link_dir in re.findall(
            r"\]\(\./skills/([^/)]+)/SKILL\.md\)", readme.read_text(encoding="utf-8")
        ):
            if not (SKILLS_ROOT / link_dir / "SKILL.md").is_file():
                errors.append(f"README 死链: skills/{link_dir}/SKILL.md")

    # 交叉引用：引用了已知 skill 但文件不存在
    for skill_dir in SKILLS_ROOT.iterdir():
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        _, body = parse_skill(skill_md)
        for ref in re.findall(r"`([^`]+)`", body):
            if ref in KNOWN_SKILLS and ref not in found:
                errors.append(f"{skill_dir.name}: 引用未找到的 skill `{ref}`")

    return report(errors, warnings, found)


def report(
    errors: list[str],
    warnings: list[str],
    found: dict[str, Path] | None = None,
) -> int:
    if found:
        print(f"已校验 {len(found)} 个 skill:")
        for name in sorted(found):
            print(f"  ✓ {name}")
    if warnings:
        print("\n警告:")
        for w in warnings:
            print(f"  ⚠ {w}")
    if errors:
        print("\n错误:")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print("\n结构校验: 通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
