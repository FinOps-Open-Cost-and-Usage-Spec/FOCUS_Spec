# tests/test_no_duplicate_checkconformancerule_items.py
import pytest

def _find_dups(strings):
    seen, dups = set(), set()
    for s in strings:
        if s in seen:
            dups.add(s)
        else:
            seen.add(s)
    return sorted(dups)

def _scan_and_or_items_for_dups(node, rule_id, path_prefix, violations):
    """
    Recursively scan for nodes like:
      {"CheckFunction": "AND"|"OR", "Items": [ ... ]}
    and ensure within Items there are no duplicate:
      {"CheckFunction": "CheckModelRule", "ModelRuleId": "..."}
    """
    if node is None:
        return

    if isinstance(node, dict):
        cf = node.get("CheckFunction")
        items = node.get("Items")
        if cf in {"AND", "OR"} and isinstance(items, list):
            ids = []
            for idx, item in enumerate(items):
                if isinstance(item, dict) and item.get("CheckFunction") == "CheckModelRule":
                    rid = item.get("ModelRuleId")
                    if isinstance(rid, str):
                        ids.append(rid)
            dups = _find_dups(ids)
            if dups:
                violations.append(
                    (rule_id, ".".join(path_prefix + ["Items"]), dups)
                )

        # Recurse into all children
        for k, v in node.items():
            _scan_and_or_items_for_dups(v, rule_id, path_prefix + [k], violations)

    elif isinstance(node, list):
        for i, item in enumerate(node):
            _scan_and_or_items_for_dups(item, rule_id, path_prefix + [str(i)], violations)

@pytest.mark.dependency(name="no_duplicate_checkmodelrule_in_and_or_items", scope="session")
def test_no_duplicate_checkmodelrule_in_and_or_items(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        # Check both Requirement and Condition trees if present
        for root_key in ("Requirement", "Condition"):
            root = vc.get(root_key)
            if root is not None:
                _scan_and_or_items_for_dups(root, rid, [f"ValidationCriteria.{root_key}"], violations)

    assert not violations, (
        "Duplicate CheckModelRule entries found within AND/OR Items:\n" +
        "\n".join(f"- Rule {rid} at {jpath}: duplicates={dups}" for rid, jpath, dups in violations)
    )
