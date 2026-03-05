import pytest
from conftest import requires_version

@pytest.mark.dependency(name="no_duplicate_child_dependencies", scope="session")
def test_no_duplicate_child_dependencies(cr_json, model_version):
    # This test only applies to model version 1.3 and above
    should_skip, reason = requires_version(model_version, min_version="1.3")
    if should_skip:
        pytest.skip(reason)
    
    """
    Test that composite rules don't list dependencies that are already dependencies of their child rules.
    
    For example, if rule A lists rules B and C as dependencies, and rule B also lists C as a dependency,
    then rule A shouldn't need to list C since it's already covered by B.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rule_id, rule in rules.items():
        # Only check composite rules
        if rule.get("Function") != "Composite":
            continue
        
        entity_type = rule.get("EntityType")
        entity_id = rule.get("EntityId")
        
        vc = rule.get("ValidationCriteria") or {}
        direct_deps = vc.get("Dependencies", [])
        
        if not direct_deps:
            continue
        
        # Collect all transitive dependencies from direct child rules
        # Only consider children with the same EntityType and EntityId
        transitive_deps = set()
        for dep_id in direct_deps:
            if dep_id in rules:
                dep_rule = rules[dep_id]
                # Only check if dependency has same EntityType and EntityId
                if (dep_rule.get("EntityType") == entity_type and 
                    dep_rule.get("EntityId") == entity_id):
                    dep_vc = dep_rule.get("ValidationCriteria") or {}
                    dep_deps = dep_vc.get("Dependencies", [])
                    # Only add transitive deps that also match EntityType and EntityId
                    for trans_dep_id in dep_deps:
                        if trans_dep_id in rules:
                            trans_dep_rule = rules[trans_dep_id]
                            if (trans_dep_rule.get("EntityType") == entity_type and 
                                trans_dep_rule.get("EntityId") == entity_id):
                                transitive_deps.add(trans_dep_id)
        
        # Find dependencies that are both direct and transitive (duplicates)
        duplicate_deps = []
        for dep_id in direct_deps:
            if dep_id in transitive_deps:
                duplicate_deps.append(dep_id)
        
        if duplicate_deps:
            violations.append((rule_id, duplicate_deps))

    assert not violations, (
        "Composite rules should not list dependencies that are already dependencies of their child rules:\n"
        + "\n".join(
            f"- Rule {rule_id}: Duplicate dependencies {deps} (already covered by child rules)"
            for rule_id, deps in violations
        )
    )
