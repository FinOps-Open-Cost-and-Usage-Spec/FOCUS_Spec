import pytest


def _iter_strings_under_arrays(node):
    """
    Yield all string values that appear inside any list under `node`.
    Handles nested dict/list structures.
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

@pytest.mark.dependency(name="formatattributes_rule_ids_exist", scope="session")
def test_formatattributes_rule_ids_exist(cr_json):
    rules = cr_json.get("ModelRules") or {}
    defined_rule_ids = set(rules.keys())

    check_funcs = cr_json.get("CheckFunctions") or {}
    violations = []  # (function_name, missing_ids)

    for fname, fdef in check_funcs.items():
        fmt = fdef.get("FormatAttributes")
        if fmt is None:
            continue  # nothing to check for this function

        # Collect all string IDs found in arrays under FormatAttributes
        refs = set(_iter_strings_under_arrays(fmt))
        missing = sorted(r for r in refs if r not in defined_rule_ids)
        if missing:
            violations.append((fname, missing))

    assert not violations, (
        "FormatAttributes contains rule IDs not found in top-level ModelRules:\n"
        + "\n".join(f"- CheckFunction {fname}: {missing}" for fname, missing in violations)
    )