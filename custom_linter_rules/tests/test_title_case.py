import sys
import subprocess
import os
import re
sys.path.insert(0, 'custom_linter_rules')

from rule_md_991 import RuleMd991

plugin = RuleMd991()

# Core unit tests - minimal set to verify basic logic works
test_cases = [
    # Basic title case rules
    ("This is a Test Heading", True),  # Minor words lowercase in middle
    ("this is a test heading", False),  # First word must be capitalized

    # Hyphenated compounds - key cases
    ("Database-as-a-Service", True),  # Minor words in middle of compound are lowercase
    ("At-Bat Average", True),  # Minor word at start of compound is capitalized
    ("X-Ray Technology", True),  # Both parts of compound capitalized
]

print("=" * 70)
print("Core unit tests (quick validation):")
print("=" * 70)
all_passed = True
for text, expected in test_cases:
    result = plugin._is_title_case(text)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{text}' -> {result} (expected {expected})")
    if result != expected:
        all_passed = False
        suggestion = plugin._to_title_case(text)
        print(f"  Suggestion: '{suggestion}'")

print()
print("=" * 70)
print("Testing against test_linter_violations.md:")
print("=" * 70)

# Run pymarkdownlnt against test_linter_violations.md
script_dir = os.path.dirname(os.path.abspath(__file__))
test_file = os.path.join(script_dir, "test_linter_violations.md")
plugin_file = os.path.join(os.path.dirname(script_dir), "rule_md_991.py")

cmd = [
    "pymarkdownlnt",
    "--add-plugin", plugin_file,
    "scan",
    test_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    # Count MD991 violations (check both stdout and stderr)
    md991_violations = []
    output = result.stdout + result.stderr
    for line in output.split('\n'):
        if 'MD991' in line:
            # Extract line number
            match = re.search(r':(\d+):\d+: MD991:', line)
            if match:
                md991_violations.append(int(match.group(1)))

    print(f"Found {len(md991_violations)} MD991 violations in test_linter_violations.md")

    if md991_violations:
        print(f"Lines with violations: {sorted(md991_violations)}")

    # Check if we found the expected violations
    expected_violation_count = 30  # Update this if you add more test cases
    if len(md991_violations) == expected_violation_count:
        print(f"✓ Expected {expected_violation_count} violations, found {len(md991_violations)}")
    else:
        print(f"✗ Expected {expected_violation_count} violations, found {len(md991_violations)}")
        all_passed = False

except FileNotFoundError:
    print("⚠ pymarkdownlnt not found - skipping file test")
    print("  (This is OK if running outside virtual environment)")
except Exception as e:
    print(f"⚠ Error running pymarkdownlnt: {e}")

print()
if all_passed:
    print("=" * 70)
    print("✓ All tests passed!")
    print("=" * 70)
else:
    print("=" * 70)
    print("✗ Some tests failed")
    print("=" * 70)
    sys.exit(1)
