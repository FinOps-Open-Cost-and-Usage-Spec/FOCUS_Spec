# tests/test_no_duplicate_dependencies.py

def _find_dups(strings):
    seen, dups = set(), set()
    for s in strings:
        if s in seen:
            dups.add(s)
        else:
            seen.add(s)
    return sorted(dups)

def test_no_duplicate_dependencies(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    violations = []  # (rule_id, duplicates)

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        deps = vc.get("Dependencies") or []
        if not isinstance(deps, list):
            continue  # ignore non-list shapes

        # Only consider string rule IDs
        ids = [d for d in deps if isinstance(d, str)]
        dups = _find_dups(ids)
        if dups:
            violations.append((rid, dups))

    assert not violations, (
        "Duplicate entries found in ValidationCriteria.Dependencies:\n"
        + "\n".join(f"- Rule {rid}: duplicates={dups}" for rid, dups in violations)
    )
