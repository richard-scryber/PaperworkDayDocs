#!/usr/bin/env python3
import re
import os

def fix_double_escaping(filepath):
    """Fix double-escaped raw tags in markdown files."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern: {% raw %}\n```...\n{% raw %} should become {% raw %}\n```...
    # We need to remove the second {% raw %} that comes right after a code fence
    pattern1 = r'({% raw %}\n```[^\n]*)\n{% raw %}\n'
    content = re.sub(pattern1, r'\1\n', content)
    
    # Pattern: \n{% endraw %}\n```\n{% endraw %} should become \n{% endraw %}\n```
    # We need to remove the second {% endraw %} after code fence
    pattern2 = r'\n{% endraw %}\n```\n{% endraw %}\n'
    content = re.sub(pattern2, r'\n{% endraw %}\n```\n', content)
    
    # Pattern: ```\n{% endraw %}\n{% endraw %} should become ```\n{% endraw %}
    # Remove consecutive endraw tags
    pattern3 = r'```\n{% endraw %}\n{% endraw %}'
    content = re.sub(pattern3, r'```\n{% endraw %}', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Fix all markdown files in learning and reference directories
for base_dir in ['/Users/richard/Projects/Paperwork/PaperworkDayDocs/learning',
                 '/Users/richard/Projects/Paperwork/PaperworkDayDocs/reference']:
    fixed_count = 0
    
    def process_directory(path):
        global fixed_count
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                process_directory(item_path)
            elif item.endswith('.md'):
                if fix_double_escaping(item_path):
                    print(f"Fixed: {item_path}")
                    fixed_count += 1
    
    process_directory(base_dir)

print(f"\nTotal files fixed: {fixed_count}")
