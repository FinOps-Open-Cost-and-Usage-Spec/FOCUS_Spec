import pytest

@pytest.mark.order(4)
@pytest.mark.dependency(name="dataset_model_rules_exist", scope="session")
def test_dataset_model_rules_exist(cr_json):
    rules = cr_json.get("ModelRules") or {}
    defined_ids = set(rules.keys())
    datasets = cr_json.get("ModelDatasets") or {}

    missing = []

    for dataset_name, dataset in datasets.items():
        for rid in dataset.get("ModelRules") or []:
            if rid not in defined_ids:
                missing.append((dataset_name, rid))

    assert not missing, (
        "ModelDatasets reference rules not defined in top-level ModelRules:\n"
        + "\n".join(f"- Dataset {ds} references missing rule {rid}" for ds, rid in missing)
    )