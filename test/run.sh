#!/bin/bash
set -euo pipefail
PASS=0; FAIL=0
assert() { if [ $? -eq 0 ]; then PASS=$((PASS+1)); echo "  ✅ $1"; else FAIL=$((FAIL+1)); echo "  ❌ $1"; fi; }
echo "=== Content Creator Tests ==="
[ -f SKILL.md ]; assert "SKILL.md"
grep -q "^---" SKILL.md; assert "frontmatter"
[ -x scripts/hotspot.py ]; assert "hotspot.py"
[ -x scripts/copywriter.py ]; assert "copywriter.py"
[ -x scripts/schedule.py ]; assert "schedule.py"
! grep -r "ghp_" scripts/ 2>/dev/null; assert "no secrets"
python3 scripts/copywriter.py 小红书 AI赚钱 5 2>/dev/null; assert "copywriter.py runs"
python3 scripts/schedule.py 抖音 2>/dev/null; assert "schedule.py runs"
echo "=== $PASS passed, $FAIL failed ==="
exit $FAIL
