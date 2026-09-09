import pytest
from conftest import get_conditions, get_conditions_catalog, conditions_key

@pytest.mark.dependency(name="all_applicability_criteria_refs_exist", scope="session")
def test_all_applicability_criteria_refs_exist(cr_json, model_version):
    rules = cr_json.get("ModelRules") or {}
    criteria_defs = set(get_conditions_catalog(cr_json, model_version).keys())
    missing = []

    for rid, rule in rules.items():
        for crit in get_conditions(rule, model_version):
            if crit not in criteria_defs:
                missing.append((rid, crit))

    key = conditions_key(model_version)
    assert not missing, (
        f"{key} references not found in top-level {key}:\n"
        + "\n".join(f"- Rule {rid} references {crit}" for rid, crit in missing)
    )