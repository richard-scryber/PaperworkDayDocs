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
| <a href='ops/multiply.html' >Multiply '*' </a>   | LHS * RHS | Will multiply the value of the expression on the left hand side by the value of the expression on right hand side and return the result   |
| <a href='ops/divide.html' >Divide '/' </a>   | LHS / RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the result  |
| <a href='ops/plus.html' >Plus '+' </a>   | LHS + RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the result, or concatenate 2 strings together |
| <a href='ops/minus.html' >Minus '-' </a>   | LHS - RHS | Will subtract the value of the expression on the left hand side with the value of the expression on right hand side and return the result  |
| <a href='ops/modulo.html' >Modulo '%' </a>   | LHS % RHS | Will divide the value of the expression on the left hand side by the value of the expression on right hand side and return the **remainder** as a result  |
| <a href='ops/Exponent.html' >Exponent '^' </a>   | LHS ^ RHS | Will raise the value of the expression on the left hand side to the power of the value of the expression on right hand side and return the result  |
| <a href='ops/nullcoalesce.html' >Null coalescing '??' </a>   | LHS ?? RHS | Will return the value of the expression on the left hand side if it is not null, otherwise it will retiurn the value of the expression on the right hand side  |
| <a href='ops/bitand.html' >Bitwise And '&' </a>   | LHS & RHS | Will perform a bit level comparison operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based on the AND truth table  |
| <a href='ops/bitor.html' >Bitwise Or '\|' </a>   | LHS \| RHS | Will perform a bit level comparison operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based on the OR truth table  |
| <a href='ops/bitleft.html' >Bitwise Shift Left '&lt;&lt;' </a>   | LHS &lt;&lt; RHS | Will perform a bit level operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based shifting the bits RHS number of places to the **right**.  |
| <a href='ops/bitright.html' >Bitwise Shift Right '&gt;&gt;' </a>   | LHS &gt;&gt; RHS | Will perform a bit level operation on the **integer** value of the expression on the left hand side with the **integer** value of the expression on right hand side and return the result based shifting the bits RHS number of places to the **right**.  |

---

## Relational operators

The library supports the use of the following relational operators for comparing values.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/equals.html' >Equals '==' </a>   | LHS == RHS | Will return true if the left and right side are the same value, otherwise false. If the types of values are different, then an attempt to convert to the same value will be made.   |
| <a href='ops/greater.html' >Greater Than '&gt;' </a>   | LHS &gt; RHS | Will return true if the left side is greater than the right side otherwise false. Again, if the types of values are different, then an attempt to convert to the same type will be made.  |
| <a href='ops/greaterequal.html' >Greater Than or Equal '&gt;=' </a>   | LHS &gt;= RHS | Will return true if the left side is more than or the same as the right side otherwise false. If the types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/less.html' >Less Than '&lt;' </a>   | LHS &lt; RHS | Will return true if the left side is considered less than the right side. Again, ifthe types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/lessequal.html' >Less Than or Equal '&lt;=' </a>   | LHS &lt;= RHS | Will return true if the left side is less than or the same as the right side otherwise false. If the types of values are different, then an attempt to convert to the same type will be made. |
| <a href='ops/notequal.html' >Not Equal '!=' </a>   | LHS != RHS | Will return true if the left and right side are *not* the same value, otherwise false. Again, if the types of values are different, then an attempt to convert to the same type will be made  |

---

## Logical operators

The library supports the use of the following logical operators.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/and.html' >And '&amp;&amp;' </a>   | LHS &amp;&amp; RHS | Will return true if the left and right side are both true, otherwise it will return false. Either side can be a constant or an expression, and if the types of values are different, then an attempt to convert to the same value will be made.   |
| <a href='ops/or.html' >Or '\|\|' </a>   | LHS \|\| RHS | Will return true if the left or right side are true, otherwise it will return false. Either side can be a constant or an expression, and if the types of values are different, then an attempt to convert to the same value will be made.  |
| <a href='ops/not.html' >Not '!' </a>   | !RHS | Will return true if the contained value results in false, or false if the contained value results in true. The contained value can be a constant or another expression, and if the type of value is not a boolean value, then an attempt to convert to boolean will be made. |

---

## Conversion functions

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/boolean.html' >Boolean Function</a>   | boolean(expr) | Will return true if the contained expression can be converted to a true value, otherwise false, or false if the contained expression results in false. The contained expression can be a constant or another expression, and an attempt to convert to boolean will be made.  |
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



## String functions

To manipulate string (character) values, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/concat.html' >Concatenate Function</a>   | concat(expr [, expr, expr, ...]) | Will take any length of parameters and concatenate them into a single string returning the result. If one of the parameters is a collection or array, then each of the entries in that array will be appended to the string in order. |
| <a href='funcs/contains.html' >Contains Function</a>   | contains(expr, comparison) | Will return true if the second string parameter appears at least once somewhere in the first string parameter. If not then the function returns false. The search is case-sensitive.  |
| <a href='funcs/endswith.html' >Ends With Function</a>   | endswith(expr, comparison) | Will return true if the second string parameter appears at the end of the first string parameter. If not then the function returns false. The search is by case-sensitive. |
| <a href='funcs/eval.html' >Evaluate Function</a>   | eval(expr) | Will accepts a single parameter and will try and evaluate and execute the result by converting the string to another expression. |
| <a href='funcs/indexof.html' >Index Of Function</a>   | indexof(expr, comparison) | Will return the starting (zero based) index of the first appearance of the second parameter within the first. If it is not found then the function returns -1. The search is case-sensitive|
| <a href='funcs/ismatch.html' >Is A Match Function</a>   | ismatch(expr, pattern) | Is a *Regular Expression* function, and will return true if the first string parameter matches the regular expression pattern string second parameter.|
| <a href='funcs/join.html' >Join Function</a>   | join(separator, expr [, expr, expr, ...]) | Will take any length of parameters and concatenate them into a single string inserting the first parameter after each of the following parameters except the last, returning the result. If one of the parameters is a collection or array, then each of the entries in that array will be appended to the string in order.  |
| <a href='funcs/length.html' >Length Function</a>   | length(expr) | Will return the total number of characters within the first string parameter.  |
| <a href='funcs/matches.html' >Matches Function</a>   | matches(expr, pattern) | Will return an *array* of all the strings in the first string parameter that match the regular expression string second parameter|
| <a href='funcs/padleft.html' >Pad Left Function</a>   | padleft(expr, length, paddingChar) | Will return the first string parameter padded at the left (start) of the string to the total length specified in the second parameter with the (first) character of the third parameter.|
| <a href='funcs/padright.html' >Pad Right Function</a>   | padright(expr, length, paddingChar) | Will return the first string parameter padded at the right (end) of the string to the total length specified in the second parameter with the (first) character of the third parameter.|
| <a href='funcs/replace.html' >Replace Function</a>   | replace(expr, searchString, replacement) | Will return the first string parameter where all occurances of the second string parameter are replaced with the third parameter. The search is case-sensitive.|
| <a href='funcs/split.html' >Split Function</a>   | split(expr, splitString) | Will return am array of strings that have been separated based on the index of the second parameter.  |
| <a href='funcs/startswith.html' >Starts With Function</a>   | startswith(expr, comparison) | Will return true if the second string parameter appears at the start of the first string parameter. If not then the function returns false. The search is case-sensitive.  |
| <a href='funcs/substring.html' >Sub-string Function</a>   | substring(expr, startIndex, [length]) | Will return a modified version of the first string parameter starting at the index of the second parameter and optionally limited in length to the third integer parameter.|
| <a href='funcs/swap.html' >Swap Function</a>   | swap(expr, pattern, replacement) | Will replace *all* of the values in the first string parameter that match the regular expression string second parameter, with the value passed in the third parameter. |
| <a href='funcs/tolower.html' >To Lowercase Function</a>   | tolower(expr) | Will return the string parameter converting all characters to lowercase characters.|
| <a href='funcs/toupper.html' >To Uppercase Function</a>   | toupper(expr) | Will return the string parameter converting all characters to uppercase (capital) characters.|
| <a href='funcs/trim.html' >Trim Function</a>   | trim(expr) | Will return the first string removing any white space characters from the start and end of the value when converted to a string. |
| <a href='funcs/trimend.html' >Trim End Function</a>   | trimend(expr) | Will return the first string parameter removing any white space characters from the right (end) of the string.  |
| <a href='funcs/trimstart.html' >Trim Start Function</a>   | trimstart(expr) | Will return the first string parameter removing any white space characters from the left (start) of the string. |


## Date functions

The date functions work on (Gregorian) DateTime values, to convert strings, use one of the date() conversion function overloads.

**Note**" When working with the current date time value, it will increase as the document is processed unless it is stored in a <code>var</code> value.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/adddays.html' >Add Days Function</a>   | adddays(expr , count) | Adds the specified number of days in the second parameter (either positive or negative), to the date value in the first parameter, returning the result |
| <a href='funcs/addhours.html' >Add Hours Function</a>   | addhours(expr, count) | Adds the specified number of hours in the second parameter (either positive or negative), to the date value in the first parameter, returning the result. If the expr or the count are null then null will be returned.  |
| <a href='funcs/addms.html' >Add Milliseconds Function</a>   | addmilliseconds(expr, count) | Adds the specified number of milli-seconds in the second parameter (either positive or negative) to the date value in the first parameter, returning the result |
| <a href='funcs/addmins.html' >Add Minutes Function</a>   | addminutes(expr, count) | Adds the specified number of minutes in the second parameter (either positive or negative) to the date value in the first parameter, returning the result. |
| <a href='funcs/addmonths.html' >Add Months Function</a>   | addmonths(expr, count) | Adds the specified number of months in the second parameter (either positive or negative), to the date value in the first parameter, returning the result.|
| <a href='funcs/addsecs.html' >Add Seconds Function</a>   | addseconds(expr, count) | Adds the specified number of seconds in the second parameter (either positive or negative) to the date value in the first parameter, returning the result.|
| <a href='funcs/addyears.html' >Add Years Function</a>   | addyears(expr, count) | Adds the specified discreet number of years in the second parameter (either positive or negative), to the date value in the first parameter, returning the result. |
| <a href='funcs/dayofmonth.html' >Day Of Month Function</a>   | dayofmonth(expr) | Will return the day of the month of the date expr parameter. The first day of the month is 1, not zero.  |
| <a href='funcs/dayofweek.html' >Day of Week Function</a>   | dayofweek(expr) | Will return the day of the week (0 - 6) of the date expr parameter. |
| <a href='funcs/dayofyear.html' >Day Of Year Function</a>   | dayofyear(expr) | Will return the total number of days that have passed in the current year for the date expr parameter.|
| <a href='funcs/daysbetween.html' >Days Between Function</a>   | daysbetween(start, end) | Will return the total number of days (inc partial days) that have passed between the two provided dates.|
| <a href='funcs/hourof.html' >Hour Of Function</a>   | hourof(expr) | discreet number of hours passed for the date expr parameter.|
| <a href='funcs/hoursbetween.html' >Hours Between Function</a>   | hoursbetween(start, end) | Will return the total number of hours (inc partial hours) that have passed between the two provided dates.  |
| <a href='funcs/msof.html' >Millisecond Of Function</a>   | millisecondof(expr) | Will return the discreet number of milliseconds passed *in the current second* for the date expr parameter.  |
| <a href='funcs/msbetween.html' >Milliseconds Between Function</a>   | millisecondsbetween(start, end) | Will return total number of milli-seconds (inc partial milli-seconds) that have passed between the two provided dates.|
| <a href='funcs/monthof.html' >Month Of Function</a>   | monthof(expr) | Will return the current month number passed for the date expr parameter - non-zero based |
| <a href='funcs/secsof.html' >Second Of Function</a>   | secondof(expr) | Will return the discreet number of seconds passed in the current minute for the date expr parameter.|
| <a href='funcs/secsbetween.html' >Seconds Between Function</a>   | secondsbetween(expr) | Will return the total number of seconds (inc partial seconds) that have passed between the two provided dates.|
| <a href='funcs/yearof.html' >Year Of Function</a>   | yearof(expr) | Will return the current year for the date expr parameter - non-zero based. |

---


## Logical Functions

The library supports the use of the following logical functions.

| Operator  | Example  | Description |
|---|---|---|
| <a href='funcs/if.html' >If Function </a>   | if(expr, trueresult, falseresult) | Checks the first parameter and if the result is true, then returns the second parameter, otherwise the third parameter is evaluated and returned.   |
| <a href='funcs/iferror.html' >If Error Function</a>   | iferror(expr, fallback) | Checks the first parameter and if the evaluated result does not cause an error, then it will be returned, otherwise the second parameter is evaluated and returned.  |
| <a href='funcs/in.html' >In Function</a>   | in(compare, expr1 [, expr2, expr3 ...]) | Takes the first parameter, and checks any following parameters to see if they are equal to the first. If so then it returns true, otherwise false. If one of the following parameters is a collection or array, then it will expand the contents and check each individual item. |

--

## Aggregate Functions

The library supports the use of the following aggregate functions to calculate individual values from collections or arrays.

| Operator  | Example  | Description |
|---|---|---|
| <a href='funcs/average.html' >Average Function</a>   | average(item1 [,item2,item3, ...]) | Will return the sum of the arguments passed to the function, divided by the number of arguments. If one of those arguments is a collection or array (or a function that returns an array), then each item in the array will be included in the calculation.   |
| <a href='funcs/averageof.html' >Average Of Function</a>   | averageof(collection, valueExpr) | Will return the mean average of evaluation of the second argument in the context of the current item from the first array or collection argument.  |
| <a href='funcs/count.html' >Count Function</a>   | count(item1 [,item2,item3, ...]) | Will return the number of non-null arguments passed to the function. If one of those arguments is a collection or array (or a function that returns an array), then it will add the non-null array length to the count. |
| <a href='funcs/max.html' >Max Function </a>   | max(item1 [,item2,item3, ...]) | Will return the largest value based on the non-null arguments passed to the function. If one of those arguments is a collection or array (or a function that returns an array), then it will check the non-null array values for the maximum.|
| <a href='funcs/maxof.html' >Max Of Function</a>   | maxof(collection, valueExpr) | Will return the the largest value based on the second parameter in the context of the current item from the array or collection in the first parameter|
| <a href='funcs/mean.html' >Mean Function</a>   | mean(item1 [,item2,item3, ...]) | Will return the sum of the arguments passed to the function, divided by the number of arguments. If one of those arguments is a collection or array (or a function that returns an array), then each item in the array will be included in the calculation. |
| <a href='funcs/median.html' >Median Function</a>   | median(item1 [,item2,item3, ...]) | Will return the middle value of all the arguments passed to the function. If one of those arguments is a collection or array (or a function that returns an array), then each item in the array will be included in the calculation. |
| <a href='funcs/min.html' >Min Function </a>   | min(item1 [,item2,item3, ...]) | Will return the smallest value based on the non-null arguments passed to the function. If one of those arguments is a collection or array (or an expression that returns an array), then it will check the non-null array values for the minimum.   |
| <a href='funcs/minof.html' >Min Of Function</a>   | minof(collection, valueExpr) | Will return the smallest value based on the second parameter in the context of the current item from the array of collection in the first parameter.  |
| <a href='funcs/mode.html' >Mode Function</a>   | mode(item1 [,item2,item3, ...]) | Will return the number value that occurs most often in all the arguments passed to the function. If one of those arguments is a collection or array (or a function that returns an array), then each item in the array will be included in the calculation. |
| <a href='funcs/sum.html' >Sum Function</a>   | sum(item1 [,item2,item3, ...]) | Will return the total accumulated value based on the non-null arguments passed to the function. If one of those arguments is a collection or array (or an expression that returns an array), then it will include the sum of the non-null array values.  |
| <a href='funcs/sumof.html' >Sum Of Function</a>   | sumof(collection, valueExpr) | will return the total value based on the second parameter in the context of the current item from the array of collection in the first parameter. |

---


## Collection Functions

The library supports the use of the following collection functions to bring together values into an array.

| Operator  | Example  | Description |
|---|---|---|
| <a href='funcs/collect.html' >Collect Function</a>   | collect(item1 [,item2,item3, ...]) | Will return all the arguments passed to the function as a single collection / array, in the order they are added. If one of those arguments is a collection or array (or a function that returns an array), then it will add the items in the array to the result.|
| <a href='funcs/eachof.html' >Each Of Function</a>   | eachof(collection, valueExpr) | Will return the an array of all the values based on the second parameter in the context of the current item from the array or collection in the first parameter.  |
| <a href='funcs/firstWhere.html' >First Where Function</a>   | firstwhere(collection, selectExpr) | Will return the first entry of the collection or array where the second expression results in a value considered to be true. |
| <a href='funcs/index.html' >Index Function </a>   | index() | Will return the current (zero based) value of the loop over a collection within the document processing.|
| <a href='funcs/lastWhere.html' ><del>Last Where Function</del></a>   | lastwhere(collection, selectExpr) | **TBC**: Will return the number of non-null arguments passed to the function. If one of those arguments is a collection or array (or a function that returns an array), then it will add the non-null array length to the count. |
| <a href='funcs/reverse.html' >Reverse Function</a>   | reverse(item1 [,item2,item3, ...]) | Will return all the arguments passed to the function as a single collection / array, inthe *reverse* order they are added. If one of those arguments is a collection or array (or a function that returns an array), then it will add the items in the array to the result (reversed)|
| <a href='funcs/sanitize.html' ><del>Sanitize Function</del></a>   | sanitize(item1 [,item2,item3, ...]) | **TBC**: Will return all the arguments passed to the function as a single collection / array, in the order they are added provided that value is not null or an empty string. If one of those arguments is a collection or array (or a function that returns an array), then it will include the items in the array to the result as long as they are again not null or an empty string. |
| <a href='funcs/selectwhere.html' >Select Where Function</a>   | selectwhere(collection, selectExpr) | Will return the an array of all the items from the array or collection in the first parameter that are matched against the second parameter in the context of the current item. |
| <a href='funcs/sortby.html' >Sort By Function</a>   | sortby(collection, sortExpr) | Will return the an array of all the items from the array or collection in the first parameter ordered by the compared value returned from the result of the second sort expression. |
