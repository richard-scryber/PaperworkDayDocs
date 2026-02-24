---
layout: default
title: column-fill
parent: CSS Properties
parent_url: /reference/cssproperties/
grand_parent: Template reference
grand_parent_url: /reference/
has_children: false
has_toc: false
---

# column-fill : Column Fill Property
{: .no_toc }

The `column-fill` property controls how content is distributed across columns in a multi-column container.

---

<details class='top-toc' markdown="block">
  <summary>
    On this page
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Usage

```css
selector {
    column-fill: balance | auto;
}
```

---

## Supported Values

- `balance` - Distributes content to keep column heights as even as possible (default)
- `auto` - Fills columns sequentially, producing fuller earlier columns before continuing

---

## Supported Elements

The `column-fill` property can be applied to:
- Block containers with active multi-column layout
- Page/body content regions using `columns`, `column-count`, or `column-width`
- Nested content sections where fill behavior needs tuning

---

## Notes

- Has effect only when multi-column layout is enabled
- Use `balance` for magazine/newsletter appearance
- Use `auto` when preserving source-order fill behavior is preferred
- Pair with `column-gap` and `column-rule` for production-ready columns

---

## Examples

### Example 1: Balanced columns

```css
.article {
    columns: 2;
    column-gap: 20pt;
    column-fill: balance;
}
```

### Example 2: Sequential fill

```css
.appendix {
    column-count: 3;
    column-gap: 16pt;
    column-fill: auto;
}
```

### Example 3: Data-bound fill mode

{% raw %}
```html
<div style="column-count: {{layout.columns}};
            column-gap: {{layout.gap}}pt;
            column-fill: {{layout.fillMode}};">
    <p>{{content}}</p>
</div>
```
{% endraw %}
