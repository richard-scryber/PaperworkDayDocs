---
layout: default
title: Binding Expressions
parent: Template reference
has_children: true
has_toc: true
nav_order: 5
---

# Binding Expression Reference
{: .no_toc }

The library supports the use of data binding to dynamic content within a template (including refrenced files and stylesheets) so that textual or visual elements and styles can be updated when a document is created.

More information on the binding syntax can be found in <a href='../binding_content.html'>Binding Content</a>

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Parentheses

The library fully supports the use of parenthese '()' to encapsulate operations into discreet sets, and also to encapsulate values passed to function calls - 'partameters'.

## Storing results

Sometimes it is appropriate to capture the results of a function or calculation to be re-used or output elsewhere. The library allows for the use of the <code>&lt;var &gt;</code> element within a template. See the <a href='../learning/templates/variables.html' >Variables article</a> for more information

## Binary operators

The library supports the use of the standard mathematical binary operators, using standard operator precedence.

<dl>
  <dt><a href='ops/Parenthese.html' >Parenthese () </a></dt>
  <dd>.</dd>
  <dt><a href='ops/Multiply.html' >Multiply * </a></dt>
  <dd>Will multiply the result of the left hand side by the right hand  and return the result.</dd>
</dl>

---

## Relational operators

The library supports the use of the standard mathematical operators, and standard operator precedence.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/Multiply.html' >Multiply * </a>   | a * b | Will multiply the expression on the left hand side by the expression on right hand side and return the result   |
| <a href='ops/Divide.html' >Divide / </a>   | a / b | Will divide the expression on the left hand side by the expression on the right hand side and return the result  |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |

---

## Binding conversion functions

All conversion functions
