"""测试驱动示例：校验 scripts/validate-skills.py 行为。"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-skills.py"


def test_validate_skills_exits_zero_on_current_repo():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "结构校验: 通过" in result.stdout
    assert "极简实现" in result.stdout
