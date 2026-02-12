#!/usr/bin/env python3
"""
Fix inline handlebars notation that appears in backtick code expressions.
These are expressions like `{{#each}}` that need {% raw %} wrapping.
Only fixes expressions OUTSIDE of code blocks (not between ```).
"""

import re
from pathlib import Path

def is_in_code_block(lines, line_idx):
    """Check if a line is inside a code block (between ``` markers)."""
    in_code_block = False
    for i in range(line_idx):
        line = lines[i].strip()
        if line.startswith('```'):
            in_code_block = not in_code_block
    return in_code_block

def fix_inline_backtick_handlebars(filepath):
    """Fix inline handlebars in backtick expressions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    modified = False

    for i, line in enumerate(lines):
        # Skip if already in a code block
        if is_in_code_block(lines, i):
            continue

        # Skip if line has {% raw %} or {% endraw %} (already processed)
        if '{% raw %}' in line or '{% endraw %}' in line:
            continue

        # Pattern to find backticked expressions with handlebars
        # Matches `{{...}}` where the content can include nested braces
        pattern = r'`(\{\{[^`]*?\}\})`'

        matches = list(re.finditer(pattern, line))
        if not matches:
            continue

        # Replace each match with wrapped version
        new_line = line
        offset = 0

        for match in matches:
            # Get the full match including backticks: `{{...}}`
            original = match.group(0)
            # Get just the handlebars part: {{...}}
            handlebars = match.group(1)

            # Wrap with raw tags: `{% raw %}{{...}}{% endraw %}`
            wrapped = f'`{{% raw %}}{handlebars}{{% endraw %}}`'

            # Calculate position with offset
            start = match.start() + offset
            end = match.end() + offset
            new_line = new_line[:start] + wrapped + new_line[end:]

            # Update offset for next replacement
            offset += len(wrapped) - len(original)

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
            if fix_inline_backtick_handlebars(md_file):
                print(f"Fixed: {md_file}")
                modified_count += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
