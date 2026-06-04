# tests/test_orphan_rules_same_type_deps_c000_exception.py
import re
import pytest


_C000_RE = re.compile(r"-C-000-")
_D000_RE = re.compile(r"-D-000-")

_ALLOWED_TYPES = {"Column", "Dataset"}  # Attributes not included at this stage

@pytest.mark.dependency(name="no_orphans_deps_only_same_type_with_c000_dataset_exception", scope="session")
def test_no_orphans_deps_only_same_type_with_c000_dataset_exception(cr_json):
    rules = cr_json.get("ModelRules") or {}

    # Build rule -> type map (normalized strings)
    rtype = {rid: (rule.get("EntityType") or "").strip() for rid, rule in rules.items()}

    # ACTIVE rules to check (exclude Deprecated, Attributes, and *-D-000-)
    active = {
        rid for rid, rule in rules.items()
        if (rule.get("Status") or "").strip() != "Deprecated"
        and rtype.get(rid) in _ALLOWED_TYPES
        and not _D000_RE.search(rid)
    }

    # Collect references via Dependencies only
    referenced_same_type = set()
    c000_referenced_by_dataset = set()

    for src_id, src_rule in rules.items():
        src_type = rtype.get(src_id)
        if src_type not in _ALLOWED_TYPES:
            continue  # ignore Attributes and anything else as referrers

        deps = (src_rule.get("ValidationCriteria") or {}).get("Dependencies") or []
        if not isinstance(deps, list):
            continue

        for dep in deps:
            if not isinstance(dep, str) or dep not in rules or dep == src_id:
                continue
            dep_type = rtype.get(dep)

            # same-EntityType de-orphaning
            if dep_type == src_type:
                referenced_same_type.add(dep)

            # exception: if a Dataset depends on a *-C-000-* rule, de-orphan that column
            if src_type == "Dataset" and _C000_RE.search(dep):
                c000_referenced_by_dataset.add(dep)

    referenced = referenced_same_type | c000_referenced_by_dataset
    orphans = sorted(active - referenced)

    assert not orphans, (
        "Active ModelRules must be referenced via Dependencies by another rule of the SAME EntityType "
        "(Attributes ignored; *-D-000-* excluded; exception: *-C-000-* may be referenced by a Dataset):\n"
        + "\n".join(f"- {rid} (EntityType={rtype.get(rid)})" for rid in orphans)
    )
