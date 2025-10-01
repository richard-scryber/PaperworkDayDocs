---
layout: default
title: CSS Selectors
parent: Template reference
parent_url: /reference/
has_children: true
has_toc: true
nav_order: 3
---

# CSS Style Selector Reference
{: .no_toc }

A style selector contains one or more style properties and defines a set of conditions that an element must match in order to have any properties applied to it.
A rule contains one or more selectors and defines a condition that the current environment must meet to have the selectors considered.

The library supports the use of a sub-set of all the current CSS selectors and at-rules. These are detailed below.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

### Unsupported Rules

If the library encounters a css rule it cannot understand the entire content of that rule will be skipped

```css

@color-profile --swop5c {
  /* Nothing after this will be checked.
  src: url("https://example.org/SWOP2006_Coated5v2.icc");
  */
}

.next{
  /* This will be included */
  color: red;
}

```

---

### Unsupported Selectors

If the library encounters a css selector it cannot understand, then it will be skipped. But any valid selectors will be maintained.

```css

.myclass[lang="pt"] {
  /* Nothing after this will be checked.
  src: url("https://example.org/SWOP2006_Coated5v2.icc");
  */
}

.next{
  /* This will be included */
  color: red;
}

```

### Combining Selectors

If the library encounters an individual css selector within the declaration that it cannot understand, then it will be skipped. But any valid selectors will be maintained.

```css

.myclass[lang="pt"], .next {
  /* This will be included for .next */
  color: red;
}


```

---

## Style Selectors Reference

How to bind

---

## Style Rules Reference

Adding data

---


