#!/usr/bin/env python3
"""
Remove orphaned {% raw %} and {% endraw %} tags that appear in incorrect positions.
"""

import os
import re
from pathlib import Path

def remove_orphaned_tags(filepath):
    """Remove orphaned raw/endraw tags."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    modified = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for opening code fence followed by orphaned endraw
        if line.strip().startswith('```') and not line.strip().endswith('```'):
            # This is an opening code fence
            result_lines.append(line)
            i += 1

            # Check if next line is an orphaned raw/endraw tag
            if i < len(lines):
                next_line = lines[i].strip()
                if next_line in ['{% raw %}', '{%raw%}', '{% endraw %}', '{%endraw%}']:
                    # Skip this orphaned tag
                    modified = True
                    i += 1

            continue

        # Check for orphaned raw/endraw tag before opening code fence
        if line.strip() in ['{% raw %}', '{%raw%}', '{% endraw %}', '{%endraw%}']:
            # Look ahead to see if next non-empty line is an opening code fence
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1

            if j < len(lines):
                next_non_empty = lines[j].strip()
                # If this is an endraw followed by raw, or raw followed by opening fence, it might be orphaned
                if line.strip() in ['{% endraw %}', '{%endraw%}']:
                    if next_non_empty in ['{% raw %}', '{%raw%}']:
                        # Orphaned endraw before raw - skip it
                        modified = True
                        i += 1
                        continue

        result_lines.append(line)
        i += 1

    if modified:
        new_content = '\n'.join(result_lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    """Main function to process all markdown files."""
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    for md_file in md_files:
        if remove_orphaned_tags(md_file):
            print(f"Fixed: {md_file}")
            modified_count += 1

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
