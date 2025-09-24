---
layout: default
title: Binding Expressions
parent: Template reference
has_children: true
has_toc: false
nav_order: 5
---

# Binding Expression Reference
{: .no_toc }

The library supports the use of data binding to dynamic content within a template (including refrenced files and stylesheets) so that textual or visual elements and styles can be updated when a document is created.

Binding is supported by wrapping expressions within 'handlebars' either in content, or for attribute or style values.

```
   {% raw %} <span id='{{model.blockId}}' style='color: {{model.theme.color}};' >{{model.name}}</span> {% endraw %}
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

The library fully supports the use of parenthese '()' to encapsulate operations into discreet sets, and also to encapsulate values passed to function calls - 'parameters'. Nesting parentheses is supported to N number of levels.

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
| <a href='ops/And.html' >And '&amp;&amp;' </a>   | LHS &amp;&amp; RHS | Wiill return true if the left and right side are both true, otherwise it will return false. Either side can be a constant or an expression, and if the types of values are different, then an attempt to convert to the same value will be made.   |
| <a href='ops/Or.html' >Or '\|\|' </a>   | LHS \|\| RHS | Will return true if the left or right side are true, otherwise it will return false. Either side can be a constant or an expression, and if the types of values are different, then an attempt to convert to the same value will be made.  |
| <a href='ops/Not.html' >Not '!' </a>   | !RHS | Will return true if the contained value results in false, or false if the contained value results in true. The contained value can be a constant or another expression, and if the type of value is not a boolean value, then an attempt to convert to boolean will be made. |

---

## Conversion functions

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/Boolean.html' >Boolean Function</a>   | boolean(expr) | Will return true if the contained expression can be converted to a true value, otherwise false, or false if the contained expression results in false. The contained expression can be a constant or another expression, and an attempt to convert to boolean will be made.  |
| <a href='funcs/date.html' >Date Function</a>   | date([expr], [format]) | Will return the value, of the contained expression, as a date. If no contained expression is provided, then it will return the current date and time. The contained expression can be aconstant or another expression, and an attempt to convert to date will be made. If a second *format* parameter is provided, then the expr will be parsed according to that format.  |
| <a href='funcs/decimal.html' >Decimal Function</a>   | decimal(expr) | Will return the value as a decimal of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to decmial will be made|
| <a href='funcs/double.html' >Double Function</a>   | double(expr) | Will return the value as a double of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to double will be made|
| <a href='funcs/integer.html' >Integer Function</a>   | integer(expr) | Will return the value as a integer of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to integer will be made|
| <a href='funcs/string.html' >String Function</a>   | string(expr, [format]) | Will return the value of the contained expression as a string. Complex (object and array values will be expanded). A formatting parameter can also be specifified to alter how the value is encoded|



## Mathematical functions

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/abs.html' >Abs Function</a>   | abs(expr) | Will return true if the contained expression can be converted to a true value, otherwise false, or false if the contained expression results in false. The contained expression can be a constant or another expression, and an attempt to convert to boolean will be made.  |
| <a href='funcs/acos.html' >Arc Cos Function</a>   | acos(expr) | Will return the value, of the contained expression, as a date. If no contained expression is provided, then it will return the current date and time. The contained expression can be aconstant or another expression, and an attempt to convert to date will be made. If a second *format* parameter is provided, then the expr will be parsed according to that format.  |
| <a href='funcs/asin.html' >Arc Sine Function</a>   | asin(expr) | Will return the value as a decimal of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to decmial will be made|
| <a href='funcs/atan.html' >Arc Tangent Function</a>   | atan(expr) | Will return the value as a double of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to double will be made|
| <a href='funcs/ceiling.html' >Ceiling Function</a>   | ceiling(expr) | Will return the value as a integer of the contained expression. The contained expression can be a constant or another expression, and an attempt to convert to integer will be made|
| <a href='funcs/cos.html' >Cosine Function</a>   | cos(expr) | Will return the value of the contained expression as a string. Complex (object and array values will be expanded). A formatting parameter can also be specifified to alter how the value is encoded|
| <a href='funcs/deg.html' >Degrees Function</a>   | deg(expr) | Will convert any numeric value (expected to be in radians), to its equivalent degree value based on the rotation around half a circle circumference.  |
| <a href='funcs/e.html' >Eulers Constant Function</a>   | e[()] | Will return the value of Eulers number (to 10 decimal places). It can also be used as a constant without the parenthese. e.g. e and E() are equivalent.|
| <a href='funcs/floor.html' >Floor Function</a>   | floor(expr) | Will return the highest possible integer value below the provided value. |
| <a href='funcs/log.html' >Logarithm Function</a>   | log(expr, newbase) | Will return the logarithm of the first argument in the base of the second argument. |
| <a href='funcs/log10.html' >Logarithm Base 10 Function</a>   | log10(expr) | Is a standard shorthand for the log(n,10) function, and will return the base 10 logarithm of a number. |
| <a href='funcs/pi.html' >PI Constant Function</a>   | pi[()] | Will return the value of Pi (to 10 decimal places). It can also be used as a constant without the parenthese. e.g. pi and PI() are equivalent.|
| <a href='funcs/pow.html' >Power Exponent Function</a>   | pow(expr, exponent) | Will return the first argument, raised to the exponent of the second argument e.g. pow(3,2) is equivalent to 3^2|
| <a href='funcs/rad.html' >Radient Function</a>   | rad(expr) | Will convert a value in degrees to it's radian equivalent.|
| <a href='funcs/round.html' >Round Function</a>   | round(expr, [precision]) | Will return the value of a provided number to the nearest integer, or rounded to any provided precision.  |
| <a href='funcs/sign.html' >Sign Function</a>   | sign(expr) | Will return 1 if the value of a provided number is positive. If the value is negative it will return -1, and zero will return 0.|
| <a href='funcs/sine.html' >Sine Function</a>   | sin(expr) | Will return the sine of the provided angle (in radians). |
| <a href='funcs/sqrt.html' >Square Root Function</a>   | sqrt(expr) | Will return the square root of a number. |
| <a href='funcs/tan.html' >Tangent Function</a>   | tan(expr) | Will return the tangent of the provided angle (in radians). |
| <a href='funcs/truncate.html' >Truncate Function</a>   | truncate(expr) | Will remove any floating point value from expr. This means negative values are equivalent to ceiling(expr) and positive values are equivalent to floor(expr).|