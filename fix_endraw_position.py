#!/usr/bin/env python3
"""
Fix {% endraw %} tags that appear in the wrong position (before the closing ``` or inside code blocks).
The correct structure should be:
{% raw %}
```
code
```
{% endraw %}
"""

import os
import re
from pathlib import Path

def fix_endraw_position(filepath):
    """Fix endraw tag positioning in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    modified = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Pattern 1: {% endraw %}``` (endraw before closing fence)
        if '{% endraw %}```' in line or '{%endraw%}```' in line:
            # Move endraw to after the fence
            line = line.replace('{% endraw %}```', '```')
            line = line.replace('{%endraw%}```', '```')
            result_lines.append(line)
            result_lines.append('{% endraw %}')
            modified = True
            i += 1
            continue

        # Pattern 2: content {% endraw %} (endraw at end of content line, before closing fence)
        if ('{% endraw %}' in line or '{%endraw%}' in line) and not line.strip().startswith('{% endraw %}'):
            # This is endraw after some content - check if next line is closing fence
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('```'):
                # Remove endraw from this line
                line = line.replace('{% endraw %}', '').replace('{%endraw%}', '')
                result_lines.append(line)
                i += 1
                # Add the closing fence
                result_lines.append(lines[i])
                # Add endraw after the fence
                result_lines.append('{% endraw %}')
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
        if fix_endraw_position(md_file):
            print(f"Fixed: {md_file}")
            modified_count += 1

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
