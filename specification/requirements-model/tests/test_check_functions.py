import pytest


def _walk_checkfunctions(node, path=None):
    """
    Yield (json_path, value) for every key == 'CheckFunction' found anywhere
    under the provided node. Handles dicts/lists at arbitrary depth.
    """
    if path is None:
        path = []

    if isinstance(node, dict):
        for k, v in node.items():
            new_path = path + [k]
            if k == "CheckFunction":
                yield (".".join(new_path), v)
            # Recurse into children
            yield from _walk_checkfunctions(v, new_path)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from _walk_checkfunctions(item, path + [str(i)])

@pytest.mark.dependency(name="all_checkfunction_refs_exist", scope="session")
def test_all_checkfunction_refs_exist(cr_json):
    # All defined function names
    defined = set((cr_json.get("CheckFunctions")).keys())

    missing = []   # (rule_id, json_path, func_name)
    badtype = []   # (rule_id, json_path, actual_value_type)

    rules = (cr_json.get("ModelRules") or {})
    for rule_id, rule in rules.items():
        for jpath, value in _walk_checkfunctions(rule):
            if isinstance(value, str):
                if value not in defined:
                    missing.append((rule_id, jpath, value))
            else:
                badtype.append((rule_id, jpath, type(value).__name__))

    assert not badtype, "Non-string CheckFunction values found:\n" + "\n".join(
        f"- {rid}: {jpath} -> {typ}" for rid, jpath, typ in badtype
    )
    assert not missing, "Missing CheckFunctions (not defined in top-level CheckFunctions):\n" + "\n".join(
        f"- {rid}: {jpath} -> '{name}'" for rid, jpath, name in missing
    )