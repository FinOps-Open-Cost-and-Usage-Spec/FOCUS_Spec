import pytest


def _iter_checkfunction_refs(node):
    """
    Yield every check-function name referenced under the given node.
    We consider:
      - "CheckFunction": "<name>"
      - "CheckFunctions": ["<name>", ...]
    and recurse through nested dicts/lists.
    """
    if node is None:
        return
    if isinstance(node, dict):
        v = node.get("CheckFunction")
        if isinstance(v, str):
            yield v
        v2 = node.get("CheckFunctions")
        if isinstance(v2, list):
            for s in v2:
                if isinstance(s, str):
                    yield s
        for child in node.values():
            yield from _iter_checkfunction_refs(child)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_checkfunction_refs(item)

@pytest.mark.dependency(name="no_unused_checkfunctions", scope="session")
def test_no_unused_checkfunctions(cr_json):
    rules = cr_json.get("ModelRules") or {}
    defined = set((cr_json.get("CheckFunctions") or {}).keys())

    # Collect all function names referenced anywhere under ModelRules
    used = set()
    for rule in rules.values():
        # If you want to limit to ValidationCriteria only, replace `rule` with:
        # (rule.get("ValidationCriteria") or {})
        for fn in _iter_checkfunction_refs(rule):
            used.add(fn)

    unused = sorted(defined - used)

    assert not unused, (
        "CheckFunctions defined but not referenced by any ConformanceRule:\n"
        + "\n".join(f"- {name}" for name in unused)
    )
