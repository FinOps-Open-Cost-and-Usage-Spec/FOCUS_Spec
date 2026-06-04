# tests/test_orphan_attributes.py

def _iter_rule_ids_in_requirement(node):
    """Yield ModelRuleId strings from Requirement/Condition structures."""
    if node is None:
        return
    if isinstance(node, dict):
        rid = node.get("ModelRuleId")
        if isinstance(rid, str):
            yield rid
        for v in node.values():
            yield from _iter_rule_ids_in_requirement(v)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_rule_ids_in_requirement(item)


def test_no_orphan_attributes_excluding_formatattributes_and_deprecated(cr_json):
    """
    Attribute-type rules are considered 'referenced' if they appear:
      • in any rule's ValidationCriteria.Dependencies, OR
      • in any Requirement/Condition tree via ModelRuleId, OR
      • in any CheckFunctions.*.FormatAttributes array.

    Attributes with Status='Deprecated' are ignored (allowed to be orphaned).
    """
    rules = cr_json.get("ModelRules") or {}
    checkfuncs = cr_json.get("CheckFunctions") or {}

    # 1) Collect references from other rules (Dependencies + Requirement/Condition)
    referenced = set()
    for _, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}

        # Dependencies
        deps = vc.get("Dependencies") or []
        if isinstance(deps, list):
            for dep in deps:
                if isinstance(dep, str):
                    referenced.add(dep)

        # Requirement / Condition trees
        for ref in _iter_rule_ids_in_requirement(vc.get("Requirement")):
            referenced.add(ref)
        for ref in _iter_rule_ids_in_requirement(vc.get("Condition")):
            referenced.add(ref)

    # 2) Collect references from CheckFunctions.*.FormatAttributes
    if isinstance(checkfuncs, dict):
        for cfg in checkfuncs.values():
            if not isinstance(cfg, dict):
                continue
            fmt_attrs = cfg.get("FormatAttributes") or []
            if isinstance(fmt_attrs, list):
                for rid in fmt_attrs:
                    if isinstance(rid, str):
                        referenced.add(rid)

    # 3) Find orphaned Attributes (excluding Deprecated)
    orphaned = []
    for rid, rule in rules.items():
        if (rule.get("EntityType") or "").strip() != "Attribute":
            continue
        if (rule.get("Status") or "").strip() == "Deprecated":
            continue  # deprecated attributes are allowed to be orphaned
        if rid not in referenced:
            orphaned.append(rid)

    assert not orphaned, (
        "Active Attribute rules are orphaned (not referenced by Dependencies, "
        "Requirement/Condition, or CheckFunctions.*.FormatAttributes):\n"
        + "\n".join(f"- {rid}" for rid in sorted(orphaned))
    )
