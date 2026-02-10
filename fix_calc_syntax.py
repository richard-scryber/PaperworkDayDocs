#!/usr/bin/env python3
"""
Fix all calc() syntax from comma-separated arguments to standard math expression format.
Converts: calc(a, '+', b) → calc(a + b)
"""
import re
import os

def fix_calc_syntax(filepath):
    """Convert calc() from comma-separated to expression syntax."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Strategy: Find all calc() calls and replace the comma-operator-comma pattern
    # We need to handle nested calc() calls, so we use a different approach
    
    # Replace patterns like: calc(expr, '+', expr) → calc(expr + expr)
    # This pattern looks for: , 'operator' , where operator is +, -, *, or /
    pattern = r",\s*'([+\-*/])'\s*,"
    content = re.sub(pattern, r" \1 ", content)
    
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
                if fix_calc_syntax(filepath):
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
