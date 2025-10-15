---
layout: default
title: continuation-footer Element
parent: HTML Elements
parent_url: /reference/htmlelements/
grand_parent: Template reference
grand_parent_url: /reference/
has_children: false
has_toc: false
---

# &lt;continuation-footer&gt; : The Continuation Footer Element
{: .no_toc }

---

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Summary

The `<continuation-footer>` element is used within `<body>` or `<section>` elements to provide a footer that displays on overflow pages. This is particularly useful for:
- Indicating "Continued on next page"
- Showing new footer content after a title page
- Adding disclaimers or notices on each page
- Displaying context information throughout multi-page content

The continuation footer appears on pages 2, 3, 4... but NOT on the first page. The first page shows the regular `<footer>` element (even if it is empty).
If the continuation footer is not present then any template `<footer>` will show on all pages.

---

## Usage

```html
<body>
    <div>
        Long content that spans multiple pages...
    </div>

    <continuation-footer>
        Continuation Footer - Appears on Pages 2, 3, 4...
        (but not the first page)
    </continuation-footer>

    <footer>
        Title Footer - First Page Only
    </footer>
</body>
```

---

## Supported Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | Unique identifier for the element |
| `class` | string | CSS class name(s) for styling |
| `style` | string | Inline CSS styles |
| `hidden` | string | If set to "hidden", the element is not visible |
| `data-bind` | expression | Data binding expression for dynamic content |

---

## Parent Elements

The `<continuation-footer>` element can be placed within:
- `<body>` - Applies to all pages in the document body
- `<section>` - Applies only to pages within that specific section

---

## Behavior

- **First Page**: Does NOT appear (use `<footer>` for first page)
- **Middle Pages**: Appears at the bottom of pages 2, 3, 4, etc.
- **Last Page**:  Appears at the bottom of the final page.
- **Styling**: Can be styled independently from the main `<footer>`
- **Data Binding**: Supports full data binding capabilities
- **Layout**: Automatically positioned at the bottom of each layout page
- **Overflow**: If the continuation footer itself is too tall, it will block the layout of any content.

---

## Notes

- The continuation footer is completely independent from the regular `<footer>` element
- Can contain any HTML content (text, images, tables, etc.)
- Useful for "Continued..." indicators, running totals, or interim summaries
- Margin, padding, and borders are respected
- Can be styled differently from the main footer
- Can include dynamic content through data binding

---

## Examples

### Example 1: Basic Continuation Footer

```html
<body>
    <div>
        <!-- Long content that spans multiple pages -->
    </div>

    <continuation-footer>
        <p style="text-align: right; font-style: italic; color: #666;">
            Article content
        </p>
    </continuation-footer>

    <footer>
        <p>Title Page</p>
    </footer>
</body>
```


### Example 4: Legal Disclaimer on Each following page

```html

<continuation-footer>
    <div style="font-size: 8pt; text-align: center; color: #666; padding: 5pt; border-top: 1pt solid #ccc;">
        CONFIDENTIAL - For Internal Use Only
    </div>
</continuation-footer>

```

### Example 5: Data-Bound Continuation Footer - No Title Footer spage

```html
<body>
    <div data-bind="{{report.sections}}">
        <h2>{{.title}}</h2>
        <p>{{.content}}</p>
    </div>

    <continuation-footer>
        <div style="background-color: #e9ecef; padding: 8pt;">
            <strong>{{report.title}}</strong> |
            Generated: {{report.date}} | page <page /> 
        </div>
    </continuation-footer>

    <footer>
    </footer>
</body>
```



### Example 8: Multi-Column Footer Layout

```html
{% raw %}<footer>
    <table style="width: 100%; border-collapse: collapse; border-top: 2pt solid #333;">
        <tr>
            <td style="width: 50%; font-size: 9pt; padding: 5pt;">
                Start of document
            </td>
            <td style="width: 50%; font-size: 9pt; padding: 5pt;">
                Title Page
            </td>
        </tr>
    </table>
</footer>
<continuation-footer>
    <table style="width: 100%; border-collapse: collapse; border-top: 2pt solid #333;">
        <tr>
            <td style="width: 50%; font-size: 9pt; padding: 5pt;">
                <span>{{string(date(), 'YYYY-MMM-DD')}}
            </td>
            <td style="width: 50%; text-align: right; font-size: 9pt; padding: 5pt;">
                Page <page /> of <page property='total' />
            </td>
        </tr>
    </table>
</continuation-footer>{% endraw%}
```

---

## See Also

- [continuation-header](/reference/htmlelements/html_continuation-header_element) - The header on continuation pages.
- [footer](/reference/htmlelements/html_footer_element) - Individual page footers
- [body](/reference/htmlelements/html_body_element) - The document body element
- [section](/reference/htmlelements/html_section_element) - Section Element
- [Page Management](/reference/learning/styles/pages) - Page sizing, numbering and sectioning.
- [Multi-page Documents](/guides/multi-page)

---
