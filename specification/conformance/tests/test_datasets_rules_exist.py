def test_dataset_conformance_rules_exist(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    defined_ids = set(rules.keys())
    datasets = cr_json.get("ConformanceDatasets") or {}

    missing = []

    for dataset_name, dataset in datasets.items():
        for rid in dataset.get("ConformanceRules") or []:
            if rid not in defined_ids:
                missing.append((dataset_name, rid))

    assert not missing, (
        "ConformanceDatasets reference rules not defined in top-level ConformanceRules:\n"
        + "\n".join(f"- Dataset {ds} references missing rule {rid}" for ds, rid in missing)
    )