#!/usr/bin/env python3
"""
Unit test to validate that static model rules with simple check functions
have ColumnName matching the Reference field.

This test catches issues like EffectiveCost-C-004-M where the rule should
check EffectiveCost but incorrectly checks ConsumedQuantity.
"""

import json
import os
import glob
import unittest


class TestColumnNameValidation(unittest.TestCase):
    """Test that ColumnName matches Reference for simple static validation rules."""
    
    # Check functions that should validate the column they reference
    SIMPLE_CHECK_FUNCTIONS = {
        'CheckType',
        'CheckFormat', 
        'CheckValue',
        'CheckNotValue',
        'TypeDecimal',
        'FormatNumeric',
        'FormatString',
        'FormatDateTime',
        'FormatCurrency',
        'FormatUnit',
        'FormatKeyValue',
        'FormatJSON'
    }
    
    def get_model_rule_files(self):
        """Get all JSON files in the model_rules directory."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_rules_dir = os.path.join(current_dir, 'model_rules')
        
        if not os.path.exists(model_rules_dir):
            self.skipTest(f"Model rules directory not found: {model_rules_dir}")
        
        json_files = []
        for root, dirs, files in os.walk(model_rules_dir):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
        
        return json_files
    
    def load_json_file(self, filepath):
        """Load and parse a JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self.fail(f"Failed to load {filepath}: {e}")
    
    def extract_column_names_from_requirement(self, requirement):
        """Recursively extract ColumnName values from a requirement structure."""
        column_names = set()
        
        if isinstance(requirement, dict):
            if 'ColumnName' in requirement:
                column_names.add(requirement['ColumnName'])
            
            # Recurse into nested structures
            for key, value in requirement.items():
                if key != 'ColumnName':  # Avoid infinite recursion
                    column_names.update(self.extract_column_names_from_requirement(value))
        
        elif isinstance(requirement, list):
            for item in requirement:
                column_names.update(self.extract_column_names_from_requirement(item))
        
        return column_names
    
    def test_static_rules_column_name_matches_reference(self):
        """Test that static rules with simple check functions have matching ColumnName and Reference."""
        json_files = self.get_model_rule_files()
        self.assertGreater(len(json_files), 0, "No JSON files found in model_rules directory")
        
        violations = []
        
        for filepath in json_files:
            data = self.load_json_file(filepath)
            
            for rule_id, rule_data in data.items():
                # Only check Static type rules
                if rule_data.get('Type') != 'Static':
                    continue
                
                reference = rule_data.get('Reference', '')
                validation_criteria = rule_data.get('ValidationCriteria', {})
                requirement = validation_criteria.get('Requirement', {})
                
                # Check if this rule uses a simple check function
                check_function = requirement.get('CheckFunction', '')
                if check_function not in self.SIMPLE_CHECK_FUNCTIONS:
                    continue
                
                # Extract all ColumnName values from the requirement
                column_names = self.extract_column_names_from_requirement(requirement)
                
                # For simple check functions, expect exactly one ColumnName that matches Reference
                if len(column_names) == 1:
                    column_name = next(iter(column_names))
                    if column_name != reference:
                        violations.append({
                            'rule_id': rule_id,
                            'file': os.path.basename(filepath),
                            'reference': reference,
                            'column_name': column_name,
                            'check_function': check_function
                        })
                elif len(column_names) > 1:
                    # Multiple column names - check if Reference is among them
                    if reference not in column_names:
                        violations.append({
                            'rule_id': rule_id,
                            'file': os.path.basename(filepath),
                            'reference': reference,
                            'column_name': f"Multiple: {', '.join(sorted(column_names))}",
                            'check_function': check_function
                        })
        
        # Report violations
        if violations:
            violation_messages = []
            for v in violations:
                violation_messages.append(
                    f"  {v['rule_id']} in {v['file']}: "
                    f"Reference='{v['reference']}' but ColumnName='{v['column_name']}' "
                    f"(CheckFunction: {v['check_function']})"
                )
            
            self.fail(
                f"Found {len(violations)} static rules where ColumnName doesn't match Reference:\n" +
                "\n".join(violation_messages)
            )


if __name__ == '__main__':
    unittest.main()