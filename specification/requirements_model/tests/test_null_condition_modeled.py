"""
Verify that a rule whose MustSatisfy text conditions on a column being null or
not null carries a non-empty Condition in its ValidationCriteria.

Matched phrasings (case-insensitive):
    "when X is null"            "when X is not null"
    "unless X is null"          "unless X is not null"
    "except when X is null"     "except when X is not null"
    "when null" / "when not null" (no subject, refers to the rule's own column)

Only Column and Object rules are checked. Composite rules are skipped: their
conditions live in the child rules they reference. Attribute rules are skipped:
their subject is a generic dataset column, so there is no concrete column for a
Condition to reference.

This test complements test_null_polarity_matches_text, which compares the
polarity of null checks that exist against the text but cannot detect a
condition that was never modeled.

Applies to model version 1.5 and later.
"""
import re

import pytest

from conftest import requires_version

NULL_CONDITION = re.compile(
    r'\b(?:when|unless|except when)\s+(?:"?\w+(?:\.\w+)*"?\s+is\s+)?(?:not\s+)?null\b',
    flags=re.IGNORECASE,
)


def test_null_condition_is_modeled(cr_json, model_version):
    should_skip, reason = requires_version(model_version, min_version="1.5")
    if should_skip:
        pytest.skip(reason)

    rules = cr_json.get("ModelRules") or {}
    failures = []

    for rid, rule in rules.items():
        if rule.get("Function") == "Composite":
            continue
        if rule.get("EntityType") not in ("Column", "Object"):
            continue
        vc = rule.get("ValidationCriteria") or {}
        text = vc.get("MustSatisfy") or ""
        if not isinstance(text, str):
            continue
        match = NULL_CONDITION.search(text)
        if not match:
            continue
        if not vc.get("Condition"):
            failures.append(
                f"- {rid}: text conditions on \"{match.group(0)}\" "
                f"but Condition is empty\n"
                f"    MustSatisfy: {text}"
            )

    assert not failures, (
        "Rules whose text conditions on null / not null but whose Condition "
        "is not modeled:\n" + "\n".join(failures)
    )
