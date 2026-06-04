"""
Enhanced markdown linter wrapper that adds context to pymarkdownlnt error messages.
Shows the actual violating content for better debugging.
"""

import sys
import subprocess
import re
from pathlib import Path


def read_file_lines(file_path):
    """Read file and return lines as a list."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        return None


def get_line_context(file_path, line_num, col_num=None):
    """Get the content of the specified line."""
    lines = read_file_lines(file_path)
    if not lines or line_num < 1 or line_num > len(lines):
        return None

    # Return the line content (strip trailing newline for display)
    line_content = lines[line_num - 1].rstrip('\n')
    return line_content


def enhance_md012_error(file_path, line_num, error_msg):
    """Enhance MD012 (multiple consecutive blank lines) error."""
    lines = read_file_lines(file_path)
    if not lines:
        return error_msg

    # Count consecutive blank lines around the error line
    blank_count = 0

    # Count backwards from error line
    idx = line_num - 1
    while idx >= 0 and lines[idx].strip() == '':
        blank_count += 1
        idx -= 1

    # Count forwards from error line
    idx = line_num
    while idx < len(lines) and lines[idx].strip() == '':
        blank_count += 1
        idx += 1

    return f"{error_msg} [Actual: {blank_count} consecutive blank lines starting around line {line_num}]"


def enhance_md022_error(file_path, line_num, error_msg):
    """Enhance MD022 (headings should be surrounded by blank lines) error."""
    line_content = get_line_context(file_path, line_num)
    if not line_content:
        return error_msg

    # Extract heading if it's a heading line
    if line_content.strip().startswith('#'):
        heading = line_content.strip()
        return f"{error_msg} [Heading: '{heading}']"

    return error_msg


def enhance_md047_error(file_path, line_num, error_msg):
    """Enhance MD047 (single trailing newline) error."""
    lines = read_file_lines(file_path)
    if not lines:
        return error_msg

    # Count trailing newlines
    trailing_newlines = 0
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == '':
            trailing_newlines += 1
        else:
            break

    if trailing_newlines == 0:
        return f"{error_msg} [Actual: No trailing newline]"
    elif trailing_newlines > 1:
        return f"{error_msg} [Actual: {trailing_newlines} trailing newlines, Expected: 1]"

    return error_msg


def enhance_generic_error(file_path, line_num, col_num, error_msg):
    """Add line context to generic errors."""
    line_content = get_line_context(file_path, line_num, col_num)
    if not line_content:
        return error_msg

    # Truncate very long lines for readability
    max_length = 80
    if len(line_content) > max_length:
        line_content = line_content[:max_length] + '...'

    # Show the line content
    return f"{error_msg} [Line: '{line_content}']"


def enhance_error_message(file_path, line_num, col_num, rule_id, error_msg):
    """Enhance error message based on rule type."""

    try:
        # MD991 already has custom enhancement in the rule itself
        if 'MD991' in rule_id:
            return error_msg

        # Specific enhancements for common rules
        if 'MD012' in rule_id:
            return enhance_md012_error(file_path, line_num, error_msg)
        elif 'MD022' in rule_id:
            return enhance_md022_error(file_path, line_num, error_msg)
        elif 'MD047' in rule_id:
            return enhance_md047_error(file_path, line_num, error_msg)
        else:
            # For other rules, add generic line context
            return enhance_generic_error(file_path, line_num, col_num, error_msg)
    except Exception as e:
        # If enhancement fails, return original message
        return error_msg


def parse_and_enhance_output(output):
    """Parse pymarkdownlnt output and enhance error messages."""
    # Pattern: file_path:line:col: RULE_ID: message
    pattern = r'^(.+?):(\d+):(\d+):\s+(MD\d+):\s+(.+)$'

    enhanced_lines = []
    for line in output.split('\n'):
        if not line.strip():
            continue

        match = re.match(pattern, line)
        if match:
            file_path = match.group(1)
            line_num = int(match.group(2))
            col_num = int(match.group(3))
            rule_id = match.group(4)
            error_msg = match.group(5)

            # Enhance the error message
            enhanced_msg = enhance_error_message(file_path, line_num, col_num, rule_id, error_msg)

            # Reconstruct the error line
            enhanced_line = f"{file_path}:{line_num}:{col_num}: {rule_id}: {enhanced_msg}"
            enhanced_lines.append(enhanced_line)
        else:
            # Non-error line, pass through
            enhanced_lines.append(line)

    return '\n'.join(enhanced_lines)


def main():
    """Run pymarkdownlnt with the same arguments and enhance output."""
    # Build the pymarkdownlnt command with all passed arguments
    cmd = ['pymarkdownlnt'] + sys.argv[1:]

    try:
        # Run pymarkdownlnt and capture output
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Enhance the output
        enhanced_stdout = parse_and_enhance_output(result.stdout)
        enhanced_stderr = parse_and_enhance_output(result.stderr)

        # Print enhanced output
        if enhanced_stdout:
            print(enhanced_stdout)
        if enhanced_stderr:
            print(enhanced_stderr, file=sys.stderr)

        # Exit with the same code as pymarkdownlnt
        sys.exit(result.returncode)

    except FileNotFoundError:
        print("Error: pymarkdownlnt not found. Make sure it's installed and in PATH.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error running enhanced linter: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
