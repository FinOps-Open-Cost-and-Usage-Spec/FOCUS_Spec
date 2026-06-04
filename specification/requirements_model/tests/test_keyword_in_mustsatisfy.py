import re
import pytest


_SKIP_SUFFIXES = (
    "nullability is defined as follows:",
    "adheres to the following requirements:",
    "adheres to the following additional requirements:",
    "adhere to the following additional requirements:",
    "is defined as follows:",
)

def _keyword_matches_text(keyword: str, text: str) -> bool:
    """
    Return True iff `keyword` (always uppercase) is present in `text` with correct semantics:
      - MUST         -> 'MUST' but not 'MUST NOT'
      - SHOULD       -> 'SHOULD' but not 'SHOULD NOT'
      - RECOMMENDED  -> 'RECOMMENDED' but not 'NOT RECOMMENDED'
      - MUST NOT / SHOULD NOT / NOT RECOMMENDED -> exact phrase
    """
    k = keyword  # expected to already be uppercase
    t = text     # check case-sensitively

    if k == "MUST":
        return re.search(r"\bMUST\b(?!\s+NOT)", t) is not None
    if k == "SHOULD":
        return re.search(r"\bSHOULD\b(?!\s+NOT)", t) is not None
    if k == "RECOMMENDED":
        return re.search(r"(?<!\bNOT\s)RECOMMENDED\b", t) is not None
    if k in {"MUST NOT", "SHOULD NOT", "NOT RECOMMENDED"}:
        return re.search(rf"\b{k}\b", t) is not None

    # Fallback: strict substring check
    return k in t

@pytest.mark.dependency(name="keyword_present_in_mustsatisfy", scope="session")
def test_keyword_present_in_mustsatisfy(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        keyword = vc.get("Keyword")
        mustsatisfy = vc.get("MustSatisfy")

        if isinstance(keyword, str) and isinstance(mustsatisfy, str):
            ms_stripped = mustsatisfy.rstrip()
            if any(ms_stripped.endswith(suf) for suf in _SKIP_SUFFIXES):
                continue
            if not _keyword_matches_text(keyword, mustsatisfy):
                violations.append((rid, keyword, mustsatisfy))

    assert not violations, (
        "ValidationCriteria.Keyword must appear in ValidationCriteria.MustSatisfy (uppercase, correct semantics):\n"
        + "\n".join(
            f"- Rule {rid}: keyword '{kw}' not found (or only as its negation) in MustSatisfy='{ms}'"
            for rid, kw, ms in violations
        )
    )