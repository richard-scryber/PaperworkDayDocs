#!/usr/bin/env python3
"""
Remove unnecessary calc() wrappers from binding expressions.
calc() should only be used for CSS calculations in style attributes.
"""
import re
import os

def remove_unnecessary_calc(filepath):
    """Remove calc() wrappers where they're not needed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: format(calc(...)) → format(...)
    # Match format(calc(expr), format) but preserve nested calc() in strings
    pattern1 = r'format\(calc\(([^)]+)\),\s*([\'"][^"\']+[\'"])\)'
    content = re.sub(pattern1, r'format(\1, \2)', content)
    
    # Pattern 2: data-value="{{calc(...)}}" → data-value="{{...}}"
    pattern2 = r'data-value="{{calc\(([^)]+)\)}}\"'
    content = re.sub(pattern2, r'data-value="{{\1}}"', content)
    
    # Pattern 3: {{calc(...)}} in non-CSS contexts (but not in style attributes)
    # This is trickier - we need to avoid removing calc() from style attributes
    # Match {{calc(...) }} when NOT preceded by style="
    # Look for patterns like: ${{{calc(...)}}} or plain {{calc(...)}}
    pattern3 = r'([^"])\{\{calc\(([^)]+)\)\}\}([^"=])'
    content = re.sub(pattern3, r'\1{{\2}}\3', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all markdown files
def process_directory(path):
    fixed_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if remove_unnecessary_calc(filepath):
                    relative_path = os.path.relpath(filepath, path)
                    fixed_files.append(relative_path)
    return fixed_files

# Fix learning and reference directories
for base_dir in ['/Users/richard/Projects/Paperwork/PaperworkDayDocs/learning',
                 '/Users/richard/Projects/Paperwork/PaperworkDayDocs/reference']:
    if os.path.exists(base_dir):
        print(f"\nProcessing {os.path.basename(base_dir)}...")
        fixed = process_directory(base_dir)
        if fixed:
            print(f"Fixed {len(fixed)} file(s):")
            for f in sorted(fixed):
                print(f"  ✅ {f}")
        else:
            print("No files needed fixing")
