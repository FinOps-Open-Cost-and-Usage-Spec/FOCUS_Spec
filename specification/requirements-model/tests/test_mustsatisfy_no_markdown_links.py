import pytest
import re


@pytest.mark.dependency(name="mustsatisfy_no_markdown_links", scope="session")
def test_mustsatisfy_no_markdown_links(cr_json):
    """
    Test that MustSatisfy fields do not contain Markdown links.
    Markdown links should not appear in the MustSatisfy text as they are intended
    to be plain normative requirements without formatting.
    
    Markdown link patterns detected:
    - [text](url)
    - [text](#anchor)
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []
    
    # Regex pattern to match Markdown links: [text](url) or [text](#anchor)
    markdown_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for rule_id, rule in rules.items():
        validation_criteria = rule.get("ValidationCriteria", {})
        must_satisfy = validation_criteria.get("MustSatisfy")
        
        if not must_satisfy or not isinstance(must_satisfy, str):
            continue
        
        # Search for Markdown links in the MustSatisfy text
        matches = markdown_link_pattern.findall(must_satisfy)
        
        if matches:
            # Extract the matched links for reporting
            links = [f"[{text}]({url})" for text, url in matches]
            violations.append({
                "rule_id": rule_id,
                "must_satisfy": must_satisfy,
                "links": links
            })
    
    assert not violations, (
        "MustSatisfy fields must not contain Markdown links. "
        "Found Markdown links in the following rules:\n" +
        "\n".join(
            f"- Rule {v['rule_id']}: Found {len(v['links'])} link(s): {', '.join(v['links'])}"
            for v in violations
        )
    )
