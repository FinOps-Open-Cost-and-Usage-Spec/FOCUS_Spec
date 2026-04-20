# Custom Linter Rules Tests

This directory contains tests for the custom markdown linter rules used in the FOCUS specification.

## Test Files

### test_linter_violations.md

A comprehensive test file containing intentional markdown linting violations of various types. Use this to verify that both built-in and custom linter rules are working correctly.

**Violations included:**
- MD991: Title case violations (custom rule)
- MD012: Multiple consecutive blank lines
- MD022: Headings not properly surrounded by blank lines
- Various edge cases and combinations

### test_title_case.py

Python unit test for testing the title case logic in `rule_md_991.py`. Tests the `_is_title_case()` method with various heading formats.

## Running the Tests

### Prerequisites

Ensure Python dependencies are installed:

```bash
pip3 install -r requirements.txt
```

### Test the Enhanced Markdown Linter

From the `specification/` directory, run:

```bash
# Test with the enhanced linter wrapper (shows detailed error context)
python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan ../custom_linter_rules/tests/test_linter_violations.md
```

**Expected output:** 9 violations with enhanced error messages showing:
- Actual vs Expected values for title case violations
- Heading text for MD022 violations
- Consecutive blank line counts for MD012 violations

### Test with Standard pymarkdownlnt

From the `specification/` directory, run:

```bash
# Test with standard pymarkdownlnt (without enhancements)
pymarkdownlnt --config markdownlnt.cfg scan ../custom_linter_rules/tests/test_linter_violations.md
```

**Expected output:** Same 9 violations but with standard pymarkdownlnt error format.

### Test Title Case Logic

From the `custom_linter_rules/tests/` directory, run:

```bash
python3 test_title_case.py
```

**Expected output:** Test results showing which title case examples pass or fail, with suggestions for corrections.

## Understanding the Output

### Enhanced Linter Format

```
file.md:line:col: RULE_ID: Message [Actual: 'found text', Expected: 'expected text']
```

Example:
```
test_linter_violations.md:13:4: MD991: Heading should use title case [Actual: 'column id', Expected: 'Column Id']
```

### Key Components

- **file.md:line:col** - Location of the violation
- **RULE_ID** - The markdown rule being violated (e.g., MD991, MD012, MD022)
- **Message** - Description of the violation
- **[Actual: ..., Expected: ...]** - Shows what was found vs what should be there

## Adding New Tests

To add new test cases to `test_linter_violations.md`:

1. Add the intentional violation to the file
2. Run the linter to verify it's detected
3. Document the expected behavior in this README

## Troubleshooting

**Issue:** "pymarkdownlnt not found"
- **Solution:** Install Python dependencies: `pip3 install -r requirements.txt`

**Issue:** "enhanced_markdown_lint.py not found"
- **Solution:** Make sure you're running from the `specification/` directory

**Issue:** Custom rule MD991 not triggering
- **Solution:** Verify `markdownlnt.cfg` has `"additional_paths": "../custom_linter_rules/"`

## Related Files

- `../rule_md_991.py` - Custom title case linter rule
- `../../specification/enhanced_markdown_lint.py` - Enhanced linter wrapper
- `../../specification/markdownlnt.cfg` - Linter configuration
