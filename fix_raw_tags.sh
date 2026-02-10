#!/bin/bash

# Process all markdown files with HTML code blocks containing {{
find reference learning -name "*.md" -type f | while read file; do
    # Check if file has html code block with {{ but no {% raw %}
    if grep -q '```html' "$file" && grep -q '{{' "$file"; then
        # Use perl for in-place editing with multiline support
        perl -i -0777 -pe 's/```html\n((?:(?!```).)*?\{\{.*?\n```)/```html\n{% raw %}\n$1{% endraw %}\n```/gs unless /{% raw %}/; s/```html\n```/```html\n```/g' "$file"
        echo "Fixed: $file"
    fi
done
