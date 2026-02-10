#!/usr/bin/env python3
import re
import os

def fix_raw_escaping(filepath):
    """Fix all raw/endraw tag escaping issues in markdown files."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: {% raw %}\n```...\n{% raw %} → {% raw %}\n```...
    pattern1 = r'({% raw %}\n```[^\n]*)\n{% raw %}\n'
    content = re.sub(pattern1, r'\1\n', content)
    
    # Pattern 2: \n{% endraw %}\n```\n{% endraw %} → \n{% endraw %}\n```
    pattern2 = r'\n{% endraw %}\n```\n{% endraw %}\n'
    content = re.sub(pattern2, r'\n{% endraw %}\n```\n', content)
    
    # Pattern 3: ```\n{% endraw %}\n{% endraw %} → ```\n{% endraw %}
    pattern3 = r'```\n{% endraw %}\n{% endraw %}'
    content = re.sub(pattern3, r'```\n{% endraw %}', content)
    
    # Pattern 4: ```{% endraw %} (endraw immediately after backticks without newline)
    # This is malformed - remove the endraw
    pattern4 = r'```{% endraw %}'
    content = re.sub(pattern4, r'```', content)
    
    # Pattern 5: Fix lines that start with ``` and have {% raw %} at the end
    # Pattern: ```{% raw %}\n → ```\n{% raw %}\n
    pattern5 = r'```{% raw %}\n'
    content = re.sub(pattern5, r'```\n{% raw %}\n', content)
    
    # Pattern 6: Remove consecutive endraw tags
    # Pattern: {% endraw %}{% endraw %} → {% endraw %}
    pattern6 = r'{% endraw %}{% endraw %}'
    content = re.sub(pattern6, r'{% endraw %}', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process both learning and reference directories
for base_dir in ['/Users/richard/Projects/Paperwork/PaperworkDayDocs/learning',
                 '/Users/richard/Projects/Paperwork/PaperworkDayDocs/reference']:
    
    print(f"\nProcessing {base_dir}...")
    fixed_count = 0
    
    def process_directory(path):
        global fixed_count
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                process_directory(item_path)
            elif item.endswith('.md'):
                if fix_raw_escaping(item_path):
                    print(f"  Fixed: {item}")
                    fixed_count += 1
    
    process_directory(base_dir)
    print(f"Total files fixed in {base_dir}: {fixed_count}")
