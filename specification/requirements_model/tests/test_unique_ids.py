import pytest

@pytest.mark.dependency(name="conformance_rule_ids_are_unique", scope="session")
def test_conformance_rule_ids_are_unique(cr_json):
    ids = [r for r in (cr_json.get("ModelRules")).keys()]
    assert len(ids) == len(set(ids)), "Duplicate ConformanceRule Ids detected"