import pytest

@pytest.mark.dependency(name="all_applicability_criteria_refs_exist", scope="session")
def test_all_applicability_criteria_refs_exist(cr_json):
    rules = cr_json.get("ModelRules") or {}
    criteria_defs = set((cr_json.get("ApplicabilityCriteria") or {}).keys())
    missing = []

    for rid, rule in rules.items():
        for crit in rule.get("ApplicabilityCriteria") or []:
            if crit not in criteria_defs:
                missing.append((rid, crit))

    assert not missing, (
        "ApplicabilityCriteria references not found in top-level ApplicabilityCriteria:\n"
        + "\n".join(f"- Rule {rid} references {crit}" for rid, crit in missing)
    )