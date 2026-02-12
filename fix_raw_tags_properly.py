#!/usr/bin/env python3
"""
Properly fix {% raw %} and {% endraw %} tags by:
1. Removing any raw/endraw tags that appear INSIDE code blocks
2. Ensuring code blocks with handlebars are wrapped OUTSIDE the code fences
"""

import os
import re
from pathlib import Path

def has_handlebars(text):
    """Check if text contains handlebars notation."""
    return bool(re.search(r'\{\{.*?\}\}', text))

def fix_raw_tags_in_file(filepath):
    """Fix raw tag placement in a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    modified = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a {% raw %} tag before a code block
        if (line.strip() in ['{% raw %}', '{%raw%}'] and
            i + 1 < len(lines) and
            lines[i + 1].strip().startswith('```')):

            # This is a raw tag before a code block - keep it
            result_lines.append(line)
            i += 1

            # Now process the code block
            code_block_start = i
            result_lines.append(lines[i])  # Add the opening ```
            i += 1

            # Collect all lines until the closing ```
            while i < len(lines):
                if lines[i].strip().startswith('```'):
                    # Found closing ```
                    # Check if there are any raw/endraw tags inside the code block
                    # Those should be removed
                    result_lines.append(lines[i])  # Add the closing ```
                    i += 1

                    # Check for {% endraw %} tag after the code block
                    if (i < len(lines) and
                        lines[i].strip() in ['{% endraw %}', '{%endraw%}']):
                        result_lines.append(lines[i])
                        i += 1
                    break
                elif lines[i].strip() in ['{% raw %}', '{%raw%}', '{% endraw %}', '{%endraw%}']:
                    # Raw/endraw tag inside code block - skip it
                    modified = True
                    i += 1
                else:
                    result_lines.append(lines[i])
                    i += 1

        # Check if this is the start of a code block without a preceding raw tag
        elif line.strip().startswith('```'):
            code_block_start = i
            code_block_lines = [line]
            i += 1

            # Collect the code block
            while i < len(lines):
                code_block_lines.append(lines[i])
                if lines[i].strip().startswith('```'):
                    break
                i += 1
            else:
                # No closing ```, just add what we have
                result_lines.extend(code_block_lines)
                continue

            i += 1  # Move past the closing ```

            # Check if code block contains handlebars
            code_block_content = '\n'.join(code_block_lines)
            needs_raw = has_handlebars(code_block_content)

            # Check if it's followed by {% endraw %} (orphaned endraw)
            has_endraw_after = (i < len(lines) and
                               lines[i].strip() in ['{% endraw %}', '{%endraw%}'])

            if needs_raw and not has_endraw_after:
                # Add raw tags around the code block
                result_lines.append('{% raw %}')
                result_lines.extend(code_block_lines)
                result_lines.append('{% endraw %}')
                modified = True
            elif has_endraw_after:
                # There's an orphaned endraw - remove it
                result_lines.extend(code_block_lines)
                i += 1  # Skip the endraw
                modified = True
            else:
                # No handlebars or already wrapped, keep as is
                result_lines.extend(code_block_lines)

        else:
            result_lines.append(line)
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
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    for md_file in md_files:
        if fix_raw_tags_in_file(md_file):
            print(f"Fixed: {md_file}")
            modified_count += 1

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
