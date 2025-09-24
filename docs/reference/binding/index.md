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

Binding is supported by wrapping expressions within 'handlebars' either in content, or for attribute or style values.

```
    <span id='\{\{model.blockId\}\}' style='color: \{\{model.theme.color\}\}; font-weight: strong;' >\{\{model.username\}\}</span>
```

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

### Parentheses

The library fully supports the use of parenthese '()' to encapsulate operations into discreet sets, and also to encapsulate values passed to function calls - 'parameters'.

### Storing results

Sometimes it is appropriate to capture the results of a function or calculation to be re-used or output elsewhere. The library allows for the use of the <code>&lt;var &gt;</code> element within a template to capture calculated values during processing. See the <a href='../learning/templates/variables.html' >Variables article</a> for more information

## Binary operators

The library supports the use of the standard mathematical binary operators, using standard operator precedence.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/Multiply.html' >Multiply '*' </a>   | LHS * RHS | Will multiply the value of the expression on the left hand side by the value of the expression on right hand side and return the result   |
| <a href='ops/Divide.html' >Divide '/' </a>   | LHS / RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the result  |
| <a href='ops/Plus.html' >Plus '+' </a>   | LHS + RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the result, or concatenate 2 strings together |
| <a href='ops/Minus.html' >Minus '-' </a>   | LHS - RHS | Will subtract the value of the expression on the left hand side with the value of the expression on right hand side and return the result  |
| <a href='ops/Modulo.html' >Modulo '%' </a>   | LHS % RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the **remainder** as a result  |
| <a href='ops/Exponent.html' >Exponent '^' </a>   | LHS ^ RHS | Will raise the value of the expression on the left hand side to the power of the value of the expression on right hand side and return the result  |
| <a href='ops/nullCoalesce.html' >Null coalescing '??' </a>   | LHS ?? RHS | Will return the value of the expression on the left hand side if it is not null, otherwise it will retiurn the value of the expression on the right hand side  |
| <a href='ops/BitAnd.html' >Bitwise And '&' </a>   | LHS & RHS | Will perform a bit level comparison operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based on the AND truth table  |
| <a href='ops/BitOr.html' >Bitwise Or '\|' </a>   | LHS \| RHS | Will perform a bit level comparison operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based on the OR truth table  |
| <a href='ops/BitLeft.html' >Bitwise Shift Left '&lt;&lt;' </a>   | LHS &lt;&lt; RHS | Will perform a bit level operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based shifting the bits RHS number of places to the **right**.  |
| <a href='ops/BitRight.html' >Bitwise Shift Right '&gt;&gt;' </a>   | LHS &gt;&gt; RHS | Will perform a bit level operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based shifting the bits RHS number of places to the **right**.  |

---

## Relational operators

The library supports the use of the following relational operators for comparing values.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/equals.html' >Equals '==' </a>   | LHS == RHS | Will return true if the left and right side are the same value, otherwise false. If the types of values are different, then an attempt to convert to the same value will be made.   |
| <a href='ops/Greater.html' >Greater Than '&gt;' </a>   | LHS &gt; RHS | Will return true if the left side is greater than the right side otherwise false. Again, if the types of values are different, then an attempt to convert to the same type will be made.  |
| <a href='ops/GreaterEqual.html' >Greater Than or Equal '&gt;=' </a>   | LHS &gt;= RHS | Will return true if the left side is more than or the same as the right side otherwise false. If the types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/Less.html' >Less Than '&lt;' </a>   | LHS &lt; RHS | Will return true if the left side is considered less than the right side. Again, ifthe types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/LessEqual.html' >Less Than or Equal '&lt;=' </a>   | LHS &lt;= RHS | Will return true if the left side is less than or the same as the right side otherwise false. If the types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/NotEqual.html' >Not Equal '!=' </a>   | LHS != RHS | Will return true if the left and right side are *not* the same value, otherwise false. Again, if the types of values are different, then an attempt to convert to the same type will be made  |

---

## Logical operators

The library supports the use of the following logical operators.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/And.html' >And '&amp;&amp;' </a>   | LHS &amp;&amp; RHS | Will return true if the left and right side are the same value, otherwise false. If the types of values are different, then an attempt to convert to the same value will be made.   |
| <a href='ops/Or.html' >Or '\|\|' </a>   | LHS \|\| RHS | Will return true if the left side is greater than the right side otherwise false. Again, if the types of values are different, then an attempt to convert to the same type will be made.  |
| <a href='ops/Not.html' >Not '!' </a>   | !RHS | Will return true if the left side is more than or the same as the right side otherwise false. If the types of values are different, then an attempt to convert to the same type will be made. |

---

## Binding conversion functions

All conversion functions
