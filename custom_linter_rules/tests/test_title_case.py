import sys
sys.path.insert(0, 'custom_linter_rules')

from rule_md_991 import RuleMd991

plugin = RuleMd991()

# Test the _is_title_case method
test_cases = [
    ("This Is a Test Heading", False), # 'is' should be lowercase now
    ("this is a test heading", False),
    ("This is a Test Heading", True),  # 'is' and 'a' should be lowercase
    ("Another heading with bad case", False),  # 'heading' should be capitalized
    ("Another Heading with Bad Case", True),
]

print("Testing title case logic:")
for text, expected in test_cases:
    result = plugin._is_title_case(text)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{text}' -> {result} (expected {expected})")
    if result != expected:
        suggestion = plugin._to_title_case(text)
        print(f"  Suggestion: '{suggestion}'")
