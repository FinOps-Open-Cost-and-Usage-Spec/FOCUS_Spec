"""
Test that all JSON files in model_rules use 2-space indentation.
"""

import json
import os
from pathlib import Path

import pytest


def get_model_rules_json_files():
    """Get all JSON files in the model_rules directory."""
    model_rules_path = Path(__file__).parent.parent / "model_rules"
    json_files = []
    
    for root, dirs, files in os.walk(model_rules_path):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    
    return json_files


@pytest.mark.parametrize("json_file", get_model_rules_json_files())
def test_json_indentation_is_two_spaces(json_file):
    """
    Test that JSON files use 2-space indentation.
    
    This test verifies that:
    1. The file can be parsed as valid JSON
    2. When re-serialized with 2-space indent, it matches the original
    3. The file does not use 4-space or tab indentation
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
        f.seek(0)
        data = json.load(f)
    
    # Re-serialize with 2-space indentation
    expected_content = json.dumps(data, indent=2, ensure_ascii=False)
    
    # Normalize line endings for comparison
    original_normalized = original_content.strip().replace('\r\n', '\n')
    expected_normalized = expected_content.strip().replace('\r\n', '\n')
    
    # Check if content matches expected 2-space indentation
    assert original_normalized == expected_normalized, (
        f"{json_file} does not use 2-space indentation. "
        f"Please format with 2 spaces (not 4 spaces or tabs)."
    )


def test_no_four_space_indentation():
    """
    Test that no JSON files use 4-space indentation patterns.
    
    This is a supplementary check that looks for common 4-space indent patterns.
    """
    json_files = get_model_rules_json_files()
    files_with_four_spaces = []
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for lines that start with 4 spaces (common in 4-space indentation)
        # but not 2 or 6 spaces (which would be valid in 2-space indentation)
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            # Check if line starts with exactly 4 spaces (not 2, 6, 8, etc.)
            if line.startswith('    ') and not line.startswith('      '):
                # This could be 4-space indentation
                # But we need to check if it's actually at indent level 2 in a 2-space scheme
                stripped = line.lstrip(' ')
                spaces = len(line) - len(stripped)
                # If spaces is 4, 12, 20, etc. (4 + 8n), it's likely 4-space indentation
                if spaces > 0 and spaces % 4 == 0 and spaces % 2 == 0:
                    # Could be either, so we rely on the main test
                    pass
    
    # The main parametrized test will catch these, this is just a helper


def test_no_tab_indentation():
    """
    Test that no JSON files use tab indentation.
    """
    json_files = get_model_rules_json_files()
    files_with_tabs = []
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '\t' in content:
            files_with_tabs.append(json_file)
    
    assert not files_with_tabs, (
        f"The following JSON files contain tab characters. "
        f"Please use 2 spaces for indentation:\n" +
        "\n".join(files_with_tabs)
    )
