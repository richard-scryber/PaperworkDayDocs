#!/usr/bin/env python3
"""Fix unescaped handlebars syntax in HTML code blocks"""

import os
import re
from pathlib import Path

def fix_markdown_file(filepath):
    """Fix HTML code blocks with unescaped handlebars syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None
    
    original_content = content
    changes_made = False
    
    # Split by code blocks to process them separately
    parts = content.split('```html\n')
    
    if len(parts) == 1:
        # No HTML code blocks
        return None
    
    result = [parts[0]]  # Keep content before first code block
    
    for i in range(1, len(parts)):
        # Find the end of this code block
        if '```' in parts[i]:
            code_block, after_block = parts[i].split('```', 1)
            
            # Check if this code block has handlebars AND is not already wrapped
            if '{{' in code_block and '{% raw %}' not in code_block:
                # Wrap the code block with raw tags
                code_block = '{% raw %}\n' + code_block + '{% endraw %}\n'
                changes_made = True
            
            result.append('```html\n' + code_block + '```' + after_block)
        else:
            result.append('```html\n' + parts[i])
    
    new_content = ''.join(result)
    
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return None


# Main execution
count = 0
fixed_files = []

print("Processing reference directory...")
for md_file in Path('reference').rglob('*.md'):
    result = fix_markdown_file(str(md_file))
    if result:
        count += 1
        fixed_files.append(str(md_file))
        print(f"  Fixed: {md_file}")

print("\nProcessing learning directory...")
for md_file in Path('learning').rglob('*.md'):
    result = fix_markdown_file(str(md_file))
    if result:
        count += 1
        fixed_files.append(str(md_file))
        print(f"  Fixed: {md_file}")

print(f"\n✓ Total files fixed: {count}")
