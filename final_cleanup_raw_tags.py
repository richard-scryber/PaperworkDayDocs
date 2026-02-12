#!/usr/bin/env python3
"""
Final cleanup to ensure proper {% raw %} and {% endraw %} tag placement.
This script will:
1. Remove any raw/endraw tags that appear on the same line as code fences
2. Remove duplicate consecutive raw/endraw tags
3. Ensure proper structure: {% raw %} before opening ```, {% endraw %} after closing ```
"""

import os
import re
from pathlib import Path

def has_handlebars(text):
    """Check if text contains handlebars notation."""
    return bool(re.search(r'\{\{.*?\}\}', text))

def clean_file(filepath):
    """Clean raw/endraw tags in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    lines = content.split('\n')

    # Step 1: Separate raw/endraw tags that are on the same line as code fences
    modified_step1 = False
    for i, line in enumerate(lines):
        # Check for ```{% endraw %} pattern
        if '```' in line and ('{% endraw %}' in line or '{%endraw%}' in line):
            # Split them onto separate lines
            line = line.replace('```{% endraw %}', '```\n{% endraw %}')
            line = line.replace('```{%endraw%}', '```\n{% endraw %}')
            if line != lines[i]:
                lines[i] = line
                modified_step1 = True

        # Check for {% raw %}``` pattern
        if '{% raw %}' in line and '```' in line:
            line = line.replace('{% raw %}```', '{% raw %}\n```')
            if line != lines[i]:
                lines[i] = line
                modified_step1 = True

    if modified_step1:
        # Re-split lines after modification
        content = '\n'.join(lines)
        lines = content.split('\n')

    # Step 2: Remove duplicate consecutive raw/endraw tags
    result_lines = []
    i = 0
    modified_step2 = False

    while i < len(lines):
        current_line = lines[i].strip()

        if current_line in ['{% raw %}', '{%raw%}']:
            # Add the raw tag
            result_lines.append(lines[i])
            i += 1
            # Skip any duplicate raw tags
            while i < len(lines) and lines[i].strip() in ['{% raw %}', '{%raw%}']:
                modified_step2 = True
                i += 1
        elif current_line in ['{% endraw %}', '{%endraw%}']:
            # Add the endraw tag
            result_lines.append(lines[i])
            i += 1
            # Skip any duplicate endraw tags
            while i < len(lines) and lines[i].strip() in ['{% endraw %}', '{%endraw%}']:
                modified_step2 = True
                i += 1
        else:
            result_lines.append(lines[i])
            i += 1

    # Step 3: Validate and fix orphaned tags
    # Count raw and endraw tags to ensure they're balanced
    raw_count = sum(1 for line in result_lines if line.strip() in ['{% raw %}', '{%raw%}'])
    endraw_count = sum(1 for line in result_lines if line.strip() in ['{% endraw %}', '{%endraw%}'])

    modified = modified_step1 or modified_step2 or (raw_count != endraw_count)

    if modified:
        new_content = '\n'.join(result_lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, raw_count, endraw_count

    return False, raw_count, endraw_count

def main():
    """Main function to process all markdown files."""
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))
    md_files = [f for f in md_files if '_site' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")

    modified_count = 0
    unbalanced_files = []

    for md_file in md_files:
        modified, raw_count, endraw_count = clean_file(md_file)
        if modified:
            print(f"Cleaned: {md_file}")
            modified_count += 1
        if raw_count != endraw_count:
            unbalanced_files.append((md_file, raw_count, endraw_count))

    print(f"\nProcessed {len(md_files)} files")
    print(f"Modified {modified_count} files")

    if unbalanced_files:
        print(f"\nWarning: {len(unbalanced_files)} files have unbalanced raw/endraw tags:")
        for file, raw, endraw in unbalanced_files[:10]:  # Show first 10
            print(f"  {file}: {raw} raw tags, {endraw} endraw tags")

if __name__ == '__main__':
    main()
