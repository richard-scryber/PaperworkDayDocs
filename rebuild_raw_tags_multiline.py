#!/usr/bin/env python3
"""
Comprehensive fix: Remove ALL {% raw %} and {% endraw %} tags, then properly
add them back around code blocks that contain handlebars notation.
This version handles multiline handlebars expressions.
"""

import os
import re
from pathlib import Path

def has_handlebars(text):
    """Check if text contains handlebars notation, including multiline."""
    # Check for {{ followed by }} anywhere in the text
    return '{{' in text and '}}' in text

def rebuild_raw_tags(filepath):
    """Rebuild raw tags from scratch in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Step 1: Remove ALL existing raw/endraw tags
    content = re.sub(r'\{%\s*raw\s*%\}', '', content)
    content = re.sub(r'\{%\s*endraw\s*%\}', '', content)

    lines = content.split('\n')
    result_lines = []
    i = 0

    # Step 2: Process the file and add raw tags around code blocks with handlebars
    while i < len(lines):
        line = lines[i]

        # Check if this is the start of a code block
        if line.strip().startswith('```') and not line.strip().endswith('```'):
            # This is an opening code fence
            code_block_start = i
            code_block_lines = [line]
            i += 1

            # Collect all lines until the closing ```
            while i < len(lines):
                code_block_lines.append(lines[i])
                if lines[i].strip().startswith('```') and i > code_block_start:
                    # Found the closing fence
                    break
                i += 1
            else:
                # No closing fence found, just add what we have
                result_lines.extend(code_block_lines)
                continue

            i += 1  # Move past the closing fence

            # Check if the code block contains handlebars (multiline aware)
            code_block_content = '\n'.join(code_block_lines)
            if has_handlebars(code_block_content):
                # Wrap with raw tags
                result_lines.append('{% raw %}')
                result_lines.extend(code_block_lines)
                result_lines.append('{% endraw %}')
            else:
                # No handlebars, don't wrap
                result_lines.extend(code_block_lines)

        else:
            result_lines.append(line)
            i += 1

    # Write the result
    new_content = '\n'.join(result_lines)

    # Check if content changed
    if new_content != original_content:
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
        try:
            if rebuild_raw_tags(md_file):
                print(f"Rebuilt: {md_file}")
                modified_count += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
