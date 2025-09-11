# tests/test_orphan_rules.py

def _iter_values_for_key(node, target_key):
    """Yield all string values for a given key found anywhere under node."""
    if node is None:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k == target_key and isinstance(v, str):
                yield v
            yield from _iter_values_for_key(v, target_key)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_values_for_key(item, target_key)


def _iter_strings_under_arrays(node):
    """
    Yield all string values that appear inside any list under `node`.
    Used to collect rule IDs from CheckFunctions.FormatAttributes.
    """
    if node is None:
        return
    if isinstance(node, list):
        for item in node:
            if isinstance(item, str):
                yield item
            else:
                yield from _iter_strings_under_arrays(item)
    elif isinstance(node, dict):
        for v in node.values():
            yield from _iter_strings_under_arrays(v)


def test_no_orphan_conformance_rules_except_deprecated(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    all_rule_ids = set(rules.keys())

    # Only ACTIVE rules must not be orphaned
    active_rule_ids = {
        rid for rid, rule in rules.items()
        if (rule.get("Status") or "").strip() != "Deprecated"
    }

    # References from other rules (Dependencies + nested ConformanceRuleId)
    referenced_by_rules = set()
    for _, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        referenced_by_rules.update(vc.get("Dependencies") or [])
        for root_key in ("Requirement", "Condition"):
            referenced_by_rules.update(_iter_values_for_key(vc.get(root_key), "ConformanceRuleId"))
    referenced_by_rules = {r for r in referenced_by_rules if r in all_rule_ids}

    # References from datasets
    datasets = cr_json.get("ConformanceDatasets") or {}
    referenced_by_datasets = set()
    for ds in datasets.values():
        for rid in ds.get("ConformanceRules") or []:
            if isinstance(rid, str):
                referenced_by_datasets.add(rid)
    referenced_by_datasets &= all_rule_ids

    # References from CheckFunctions.FormatAttributes (strings inside arrays)
    check_funcs = cr_json.get("CheckFunctions") or {}
    referenced_by_checkfuncs = set()
    for fdef in check_funcs.values():
        fmt = fdef.get("FormatAttributes")
        if fmt is None:
            continue
        for s in _iter_strings_under_arrays(fmt):
            if s in all_rule_ids:
                referenced_by_checkfuncs.add(s)

    # Rules are considered referenced if they appear in any of the above
    referenced = referenced_by_rules | referenced_by_datasets | referenced_by_checkfuncs

    # Orphans are ACTIVE rules not referenced anywhere
    orphans = sorted(active_rule_ids - referenced)

    assert not orphans, (
        "Active ConformanceRules (Status != 'Deprecated') not referenced by any rule, dataset, "
        "or CheckFunctions.FormatAttributes:\n"
        + "\n".join(f"- {rid}" for rid in orphans)
    )
