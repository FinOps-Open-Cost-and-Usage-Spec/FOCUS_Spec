import pytest


def _iter_rule_ids_in_requirement(node):
    if node is None:
        return
    if isinstance(node, dict):
            rid = node.get("ModelRuleId")
            if isinstance(rid, str):
                yield rid
            for v in node.values():
                yield from _iter_rule_ids_in_requirement(v)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_rule_ids_in_requirement(item)

def _text_has_keywords(text, keywords=None) -> bool:
    if not isinstance(text, str):
        return False
    if keywords is None:
        keywords = ["when", "unless"]
    s = text.lower()
    return any(kw in s for kw in keywords)

def _rule_has_scope(rule: dict) -> bool:
    vc = rule.get("ValidationCriteria") or {}
    app = rule.get("ApplicabilityCriteria")
    cond = vc.get("Condition")
    ms = vc.get("MustSatisfy")
    has_app = isinstance(app, list) and len(app) > 0
    has_cond = isinstance(cond, dict) and len(cond) > 0
    has_ms_scope = _text_has_keywords(ms)
    return has_app or has_cond or has_ms_scope

def _all_requirement_refs_have_scope(rule: dict, rules: dict) -> bool:
    vc = rule.get("ValidationCriteria") or {}
    req_refs = set(_iter_rule_ids_in_requirement(vc.get("Requirement")))
    if not req_refs:
        return False
    for ref_id in req_refs:
        linked = (rules.get(ref_id) or {})
        if not _rule_has_scope(linked):
            return False
    return True

def _deps_presence_keywords(rule: dict, rules: dict):
    """
    Return two booleans:
      has_presence_must_or_should: any dep is Presence with Keyword in {'MUST','SHOULD'}
      has_presence_other:          any dep is Presence with other keyword
    (Dependencies only.)
    """
    vc = rule.get("ValidationCriteria") or {}
    deps = vc.get("Dependencies") or []
    if not isinstance(deps, list):
        return (False, False)

    has_must_should = False
    has_other = False

    for dep_id in deps:
        if not isinstance(dep_id, str):
            continue
        linked = (rules.get(dep_id) or {})
        if linked.get("Function") != "Presence":
            continue
        kw = ((linked.get("ValidationCriteria") or {}).get("Keyword") or "").strip().upper()
        if kw in {"MUST", "SHOULD"}:
            has_must_should = True
        else:
            has_other = True

    return has_must_should, has_other




@pytest.mark.order(6)
@pytest.mark.dependency(
    name="suffixes_by_keyword_and_scope",
    depends=["provider_supports_requires_applicabilitycriteria"],
    scope="session",
)
def test_suffixes_unified(cr_json):
    """
    Scope = non-empty ApplicabilityCriteria OR non-empty Condition OR 'when'/'unless' in MustSatisfy
    • If scope: require '-C' (skip '-M'/'-O').

    Otherwise (no scope):
      Composite rules:
        1) If ALL Requirement-linked rules have scope -> require '-C'
        2) Else Presence deps priority:
             - If ANY Presence dep has Keyword in {MUST, SHOULD} -> require '-M'
             - Else if ANY Presence dep has other Keyword        -> require '-O'
      Base keywords if none of the above fired:
        - MUST / MUST NOT -> require '-M'
        - MAY / MAY NOT / RECOMMENDED / NOT RECOMMENDED -> require '-O'
    """
    rules = cr_json.get("ModelRules") or {}

    need_c, need_m, need_o = [], [], []
    O_KEYWORDS = {"MAY", "MAY NOT", "RECOMMENDED", "NOT RECOMMENDED"}

    for rid, rule in rules.items():
        if (rule.get("Status") or "").strip() != "Active":
            continue
        
        if (rule.get("EntityType") or "") == "Dataset" and '-000-' in rid:
            continue

        vc = rule.get("ValidationCriteria") or {}
        keyword = (vc.get("Keyword") or "").strip().upper()

        # 1) Scope precedence
        if _rule_has_scope(rule):
            if not (isinstance(rid, str) and rid.endswith("-C")):
                need_c.append(rid)
            continue

        # 2) No scope on the rule
        func = rule.get("Function")
        if func == "Composite":
            # 2.1) Requirement-linked scope forces -C
            if _all_requirement_refs_have_scope(rule, rules):
                if not (isinstance(rid, str) and rid.endswith("-C")):
                    need_c.append(rid)
                continue

            # 2.2) Presence deps priority: prefer -M if any MUST/SHOULD, else -O if any other
            has_ms, has_other = _deps_presence_keywords(rule, rules)
            if has_ms:
                if not (isinstance(rid, str) and rid.endswith("-M")):
                    need_m.append(rid)
                continue
            if has_other:
                if not (isinstance(rid, str) and rid.endswith("-O")):
                    need_o.append(rid)
                continue
            # else fall through to base keyword handling

        # 3) Base keyword handling
        if keyword in {"MUST", "MUST NOT"}:
            if not (isinstance(rid, str) and rid.endswith("-M")):
                need_m.append(rid)
        elif keyword in O_KEYWORDS:
            if not (isinstance(rid, str) and rid.endswith("-O")):
                need_o.append(rid)

    assert not need_c, (
        "Rules with scope OR Composite whose Requirement-linked rules all have scope must end with '-C':\n"
        + "\n".join(f"- {r}" for r in need_c)
    )
    assert not need_m, (
        "Rules that require '-M' (MUST/MUST NOT without scope, or Composite with Presence deps MUST/SHOULD) "
        "do not end with '-M':\n" + "\n".join(f"- {r}" for r in need_m)
    )
    assert not need_o, (
        "Rules that require '-O' (MAY/MAY NOT/RECOMMENDED/NOT RECOMMENDED without scope, "
        "or Composite with non-MUST/SHOULD Presence deps) do not end with '-O':\n"
        + "\n".join(f"- {r}" for r in need_o)
    )
