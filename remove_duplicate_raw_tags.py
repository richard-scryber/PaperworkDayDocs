#!/usr/bin/env python3
"""
Remove duplicate {% raw %} and {% endraw %} tags that may have been
added by the previous script when files already had raw tags.
"""

import os
import re
from pathlib import Path

def remove_duplicate_raw_tags(filepath):
    """Remove consecutive duplicate raw/endraw tags."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    modified = False
    i = 0

    while i < len(lines):
        current_line = lines[i].strip()

        # Check if this is a {% raw %} tag
        if current_line == '{% raw %}' or current_line == '{%raw%}':
            # Look ahead for duplicate {% raw %} tags
            j = i + 1
            raw_count = 1
            while j < len(lines) and (lines[j].strip() == '{% raw %}' or lines[j].strip() == '{%raw%}'):
                raw_count += 1
                j += 1

            # Only keep one {% raw %} tag
            result_lines.append(lines[i])
            if raw_count > 1:
                modified = True
                # Skip the duplicates
                i = j
            else:
                i += 1

        # Check if this is a {% endraw %} tag
        elif current_line == '{% endraw %}' or current_line == '{%endraw%}':
            # Look ahead for duplicate {% endraw %} tags
            j = i + 1
            endraw_count = 1
            while j < len(lines) and (lines[j].strip() == '{% endraw %}' or lines[j].strip() == '{%endraw%}'):
                endraw_count += 1
                j += 1

            # Only keep one {% endraw %} tag
            result_lines.append(lines[i])
            if endraw_count > 1:
                modified = True
                # Skip the duplicates
                i = j
            else:
                i += 1

        else:
            result_lines.append(lines[i])
            i += 1

    if modified:
        # Write the modified content back
        new_content = '\n'.join(result_lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    """Main function to process all markdown files."""
    # Get all .md files recursively
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))

    # Exclude files in _site directory (generated)
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    for md_file in md_files:
        if remove_duplicate_raw_tags(md_file):
            print(f"Removed duplicates in: {md_file}")
            modified_count += 1

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
