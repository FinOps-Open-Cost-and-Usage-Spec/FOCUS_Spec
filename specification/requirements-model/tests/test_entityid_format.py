# tests/test_entityid_format.py
import re
import pytest


# Map EntityType -> expected marker
_EXPECTED_MARKER = {
    "Attribute": "A",
    "Column": "C",
    "Dataset": "D",
    "Object": "O",
}

def _marker_ok(entity_id: str, expected_letter: str) -> bool:
    """
    Check that entity_id contains '-<letter>-' immediately before the numeric segment,
    e.g., ...-C-000-..., ...-A-012-..., ...-D-3-...
    """
    # Require -<LETTER>-<digits>- somewhere in the ID
    pat = re.compile(rf"-{re.escape(expected_letter)}-\d+-")
    return bool(pat.search(entity_id))

@pytest.mark.dependency(name="entityid_marker_matches_entitytype", scope="session")
def test_entityid_marker_matches_entitytype(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        et = rule.get("EntityType")
        if et not in _EXPECTED_MARKER:
            # Ignore other entity types (or collect as separate violations if you prefer)
            continue

        # Validate the rule key (rid) itself
        expected = _EXPECTED_MARKER[et]
        if not _marker_ok(rid, expected):
            violations.append((rid, et, rid))

    assert not violations, (
        "EntityId must include the correct marker before the numeric segment "
        "(Attribute -> -A-, Column -> -C-, Object -> -O-, Dataset -> -D-):\n" +
        "\n".join(f"- Rule {rid} (EntityType={et}): EntityId='{eid}'" for rid, et, eid in violations)
    )
