#!/usr/bin/env python3
"""
Fix inline handlebars notation that appears outside of code blocks and backticks.
These appear in headings, plain text, and need to be wrapped in {% raw %} {% endraw %}.
"""

import re
from pathlib import Path

def is_in_code_block(lines, line_idx):
    """Check if a line is inside a code block."""
    in_code_block = False
    for i in range(line_idx):
        if lines[i].strip().startswith('```'):
            in_code_block = not in_code_block
    return in_code_block

def is_in_backticks(line, match_start):
    """Check if a position is inside backticks."""
    # Count backticks before the match
    before = line[:match_start]
    backtick_count = before.count('`')
    # If odd number of backticks before, we're inside backticks
    return backtick_count % 2 == 1

def fix_inline_handlebars(filepath):
    """Fix inline handlebars in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    modified = False

    # Pattern to match handlebars expressions
    # Matches {{ ... }} including nested braces
    pattern = r'\{\{[^}]*\}\}'

    for i, line in enumerate(lines):
        # Skip lines in code blocks
        if is_in_code_block(lines, i):
            continue

        # Skip if line already has {% raw %} or {% endraw %}
        if '{% raw %}' in line or '{% endraw %}' in line:
            continue

        # Find all handlebars matches in the line
        matches = list(re.finditer(pattern, line))
        if not matches:
            continue

        # Check each match to see if it needs wrapping
        needs_fix = False
        for match in matches:
            if not is_in_backticks(line, match.start()):
                needs_fix = True
                break

        if needs_fix:
            # Wrap each handlebars expression not in backticks with {% raw %}{% endraw %}
            new_line = line
            offset = 0
            for match in matches:
                if not is_in_backticks(line, match.start()):
                    handlebars = match.group()
                    wrapped = f'{{% raw %}}{handlebars}{{% endraw %}}'
                    # Calculate position with offset
                    start = match.start() + offset
                    end = match.end() + offset
                    new_line = new_line[:start] + wrapped + new_line[end:]
                    # Update offset for next replacement
                    offset += len(wrapped) - len(handlebars)

            if new_line != line:
                lines[i] = new_line
                modified = True

    if modified:
        new_content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    """Process all markdown files."""
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    for md_file in md_files:
        try:
            if fix_inline_handlebars(md_file):
                print(f"Fixed: {md_file}")
                modified_count += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
