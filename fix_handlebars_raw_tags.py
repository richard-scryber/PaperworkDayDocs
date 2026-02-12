#!/usr/bin/env python3
"""
Fix Jekyll handlebars notation issues by wrapping code blocks containing
{{ }} in {% raw %} and {% endraw %} tags if not already wrapped.
"""

import os
import re
from pathlib import Path

def has_handlebars(text):
    """Check if text contains handlebars notation."""
    return bool(re.search(r'\{\{.*?\}\}', text))

def is_already_wrapped_in_raw(lines, start_idx, end_idx):
    """Check if a code block is already wrapped in {% raw %} tags."""
    # Look backwards from start_idx to find {% raw %}
    for i in range(start_idx - 1, max(-1, start_idx - 10), -1):
        if i < 0 or i >= len(lines):
            continue
        line = lines[i].strip()
        if '{% raw %}' in line or '{%raw%}' in line:
            # Found raw tag, now look for endraw after the code block
            for j in range(end_idx + 1, min(len(lines), end_idx + 10)):
                if '{% endraw %}' in lines[j] or '{%endraw%}' in lines[j]:
                    return True
            return False
        # If we hit another code block or frontmatter, stop looking
        if line.startswith('```') or line == '---':
            break
    return False

def process_markdown_file(filepath):
    """Process a single markdown file to add raw tags where needed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    modified = False
    i = 0
    result_lines = []

    while i < len(lines):
        line = lines[i]

        # Check if this is the start of a code block
        if line.strip().startswith('```'):
            # Find the end of the code block
            code_block_start = i
            code_block_lines = [line]
            i += 1

            while i < len(lines):
                code_block_lines.append(lines[i])
                if lines[i].strip().startswith('```'):
                    # Found the end
                    code_block_end = i
                    break
                i += 1
            else:
                # No closing ```, just add what we have
                result_lines.extend(code_block_lines)
                continue

            # Check if the code block contains handlebars
            code_block_content = '\n'.join(code_block_lines)
            if has_handlebars(code_block_content):
                # Check if it's already wrapped
                if not is_already_wrapped_in_raw(lines, code_block_start, code_block_end):
                    # Add {% raw %} before and {% endraw %} after
                    result_lines.append('{% raw %}')
                    result_lines.extend(code_block_lines)
                    result_lines.append('{% endraw %}')
                    modified = True
                else:
                    # Already wrapped, keep as is
                    result_lines.extend(code_block_lines)
            else:
                # No handlebars, keep as is
                result_lines.extend(code_block_lines)

            i += 1
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
    # Get all .md files recursively
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))

    # Exclude files in _site directory (generated)
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    for md_file in md_files:
        if process_markdown_file(md_file):
            print(f"Modified: {md_file}")
            modified_count += 1

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
