"""
Verify that null checks in a rule's Requirement and Condition agree with the
null / not-null wording of its MustSatisfy text.

Checked leaves are CheckValue / CheckNotValue / JSONCheckPathValue /
JSONCheckPathNotValue with "Value": null, whether they sit at the top level
or inside an AND / OR composite.

Requirement side
    "X MUST be null"       -> CheckValue / JSONCheckPathValue (null)
    "X MUST NOT be null"   -> CheckNotValue / JSONCheckPathNotValue (null)
    (SHOULD and MAY are treated the same way as MUST)

Condition side
    "when X is null"       -> CheckValue / JSONCheckPathValue (null)
    "when X is not null"   -> CheckNotValue / JSONCheckPathNotValue (null)
    "unless X is null" and "except when X is null" invert the polarity.
    "when not null" / "when null" with no subject refers to the rule's own
    column (the condition column must equal the rule EntityId).

For JSON path checks the subject in the text is the last path segment,
usually written in double quotes (e.g. "ContractCommitmentAppliedQuantity").

Leaves whose column is never described as null / not null in the text are
skipped: the text does not make a claim the model can contradict.

Applies to model version 1.5 and later. Earlier releases carry known
mismatches that are to be corrected separately.
"""
import re

import pytest

from conftest import requires_version

NULL_CHECKS = {
    "CheckValue": False,
    "JSONCheckPathValue": False,
    "CheckNotValue": True,
    "JSONCheckPathNotValue": True,
}

NEGATING_CONNECTIVES = ("unless", "except when")


def _null_leaves(node, path):
    """Yield (path, leaf) for every null-valued simple check under node."""
    if not isinstance(node, dict):
        return
    fn = node.get("CheckFunction")
    if fn in NULL_CHECKS and "Value" in node and node["Value"] is None:
        yield path, node
    for op in ("AND", "OR"):
        for i, child in enumerate(node.get(op) or []):
            yield from _null_leaves(child, f"{path}.{op}[{i}]")


def _subject(leaf):
    """Name of the thing the text should call null / not null."""
    path = leaf.get("Path")
    if isinstance(path, str) and path:
        seg = path.split(".")[-1]
        return re.sub(r"\[.*?\]$", "", seg)
    return leaf.get("ColumnName") or ""


def _requirement_polarity(text, subject):
    """Return True (not null), False (null) or None (no claim found)."""
    kw = r"(?:MUST|SHOULD|MAY)"
    subj = re.escape(subject)
    pat = rf'"?\b{subj}\b"?\s+{kw}(\s+NOT)?\s+be\s+null\b'
    hits = re.findall(pat, text)
    if not hits:
        pat = rf'\b{kw}(\s+NOT)?\s+be\s+null\b'
        hits = re.findall(pat, text)
        if len(hits) != 1:
            return None
    polarities = {bool(h.strip()) for h in hits}
    return polarities.pop() if len(polarities) == 1 else None


def _condition_polarity(text, subject, is_own_column):
    """Return True (not null), False (null) or None (no claim found)."""
    subj = re.escape(subject)
    pat = (
        rf'(?:\b(unless|except when)\s+)?'
        rf'"?\b{subj}\b"?\s+is\s+(not\s+)?null\b'
    )
    polarities = set()
    for connective, neg in re.findall(pat, text, flags=re.IGNORECASE):
        polarity = bool(neg)
        if connective:
            polarity = not polarity
        polarities.add(polarity)
    if not polarities and is_own_column:
        for connective, neg in re.findall(
            r'\b(when|unless|except when)\s+(not\s+)?null\b', text, flags=re.IGNORECASE
        ):
            polarity = bool(neg)
            if connective.lower() in NEGATING_CONNECTIVES:
                polarity = not polarity
            polarities.add(polarity)
    return polarities.pop() if len(polarities) == 1 else None


def _describe(expected_not_null):
    return "not null" if expected_not_null else "null"


def test_null_polarity_matches_text(cr_json, model_version):
    should_skip, reason = requires_version(model_version, min_version="1.5")
    if should_skip:
        pytest.skip(reason)

    rules = cr_json.get("ModelRules") or {}
    failures = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        text = vc.get("MustSatisfy") or ""
        if not isinstance(text, str) or "null" not in text.lower():
            continue
        entity_id = rule.get("EntityId")

        for path, leaf in _null_leaves(vc.get("Requirement"), "Requirement"):
            expected = _requirement_polarity(text, _subject(leaf))
            if expected is None:
                continue
            actual = NULL_CHECKS[leaf["CheckFunction"]]
            if actual != expected:
                failures.append(
                    f"- {rid} [{path}]: text says {_subject(leaf)} "
                    f"{'MUST NOT' if expected else 'MUST'} be null, "
                    f"but {leaf['CheckFunction']} checks for {_describe(actual)}\n"
                    f"    MustSatisfy: {text}"
                )

        for path, leaf in _null_leaves(vc.get("Condition"), "Condition"):
            subject = _subject(leaf)
            expected = _condition_polarity(
                text, subject, leaf.get("ColumnName") == entity_id
            )
            if expected is None:
                continue
            actual = NULL_CHECKS[leaf["CheckFunction"]]
            if actual != expected:
                failures.append(
                    f"- {rid} [{path}]: text conditions on {subject} being "
                    f"{_describe(expected)}, but {leaf['CheckFunction']} "
                    f"checks for {_describe(actual)}\n"
                    f"    MustSatisfy: {text}"
                )

    assert not failures, (
        "Null checks that contradict the null / not-null wording of MustSatisfy:\n"
        + "\n".join(failures)
    )
