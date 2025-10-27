# tests/test_rule_number_sequences.py
import re
import pytest


# Regex to capture: prefix (up to and incl. -A- / -C- / -D-) and the numeric segment
ID_RE = re.compile(r'^(?P<prefix>.+-(?:A|C|D)-)(?P<num>\d+)-')

@pytest.mark.dependency(name="rule_numbers_start_at_000_and_are_consecutive", scope="session")
def test_rule_numbers_start_at_000_and_are_consecutive(cr_json):
    rules = cr_json.get("ModelRules") or {}
    by_prefix = {}
    invalid_ids = []

    for rid in rules.keys():
        m = ID_RE.match(rid)
        if not m:
            invalid_ids.append(rid)
            continue
        prefix = m.group("prefix")
        num = int(m.group("num"))
        by_prefix.setdefault(prefix, []).append(num)

    # If you want to fail on unparseable IDs, uncomment this:
    # assert not invalid_ids, "Rule IDs not matching expected pattern:\n" + "\n".join(f"- {r}" for r in sorted(invalid_ids))

    problems = []  # (prefix, present_sorted, expected_range)

    for prefix, nums in by_prefix.items():
        nums_sorted = sorted(set(nums))
        expected = list(range(0, len(nums_sorted)))  # 0..N-1
        # compare against expected values
        if nums_sorted != expected:
            problems.append((prefix, nums_sorted, expected))

    assert not problems, (
        "ConformanceRule IDs must start at -000- and be consecutive without gaps:\n"
        + "\n".join(
            f"- Prefix '{prefix}': present={present} expected={expected}"
            for prefix, present, expected in problems
        )
    )
