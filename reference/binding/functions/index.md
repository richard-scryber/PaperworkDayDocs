---
layout: default
title: Expression Functions
parent: Data Binding
parent_url: /reference/binding/
grand_parent: Template reference
grand_parent_url: /reference/
has_children: true
has_toc: false
---

# Expression Functions Reference
{: .no_toc }

Built-in functions for data manipulation and formatting in Scryber binding expressions.

---

<details open class='top-toc' markdown="block">
  <summary>
    On this page
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Overview

Expression functions transform and manipulate data within binding expressions. Over 90 built-in functions are available across multiple categories.

**Usage:**


{% raw %}
```handlebars
{{functionName(param1, param2, ...)}}
```
{% endraw %}



---

## Conversion Functions

Convert values between different types.

| Function | Description | Example |
|----------|-------------|---------|
| [int](./int) | Convert to integer | `{{int(model.value)}}` |
| [long](./long) | Convert to long integer | `{{long(model.bigNumber)}}` |
| [double](./double) | Convert to double precision float | `{{double(model.value)}}` |
| [decimal](./decimal) | Convert to decimal | `{{decimal(model.price)}}` |
| [bool](./bool) | Convert to boolean | `{{bool(model.flag)}}` |
| [date](./date) | Convert to DateTime | `{{date(model.dateString)}}` |
| [typeof](./typeof) | Get type name | `{{typeof(model.value)}}` |

---

## String Functions

Manipulate and format text.

| Function | Description | Example |
|----------|-------------|---------|
| [format](./format) / [string](./string.md) | Format values as strings | `{{format(model.price, 'C2')}}` |
| [concat](./concat) | Concatenate strings | `{{concat(model.first, ' ', model.last)}}` |
| [join](./join) | Join array with separator | `{{join(model.items, ', ')}}` |
| [substring](./substring) | Extract substring | `{{substring(model.text, 0, 10)}}` |
| [replace](./replace) | Replace text | `{{replace(model.text, 'old', 'new')}}` |
| [toLower](./toLower) | Convert to lowercase | `{{toLower(model.text)}}` |
| [toUpper](./toUpper) | Convert to UPPERCASE | `{{toUpper(model.code)}}` |
| [trim](./trim) | Remove leading/trailing whitespace | `{{trim(model.text)}}` |
| [trimEnd](./trimEnd) | Remove trailing whitespace | `{{trimEnd(model.text)}}` |
| [length](./length) | Get string length | `{{length(model.text)}}` |
| [contains](./contains) | Check if contains substring | `{{contains(model.text, 'search')}}` |
| [startsWith](./startsWith) | Check if starts with substring | `{{startsWith(model.text, 'prefix')}}` |
| [endsWith](./endsWith) | Check if ends with substring | `{{endsWith(model.text, 'suffix')}}` |
| [indexOf](./indexOf) | Find substring position | `{{indexOf(model.text, 'search')}}` |
| [padLeft](./padLeft) | Pad left with characters | `{{padLeft(model.num, 5, '0')}}` |
| [padRight](./padRight) | Pad right with characters | `{{padRight(model.text, 10, ' ')}}` |
| [split](./split) | Split string into array | `{{split(model.text, ',')}}` |
| [regexIsMatch](./regexIsMatch) | Test regex pattern | `{{regexIsMatch(model.email, '^.+@.+$')}}` |
| [regexMatches](./regexMatches) | Find all regex matches | `{{regexMatches(model.text, '\\d+')}}` |
| [regexSwap](./regexSwap) | Replace using regex | `{{regexSwap(model.text, '\\d+', 'X')}}` |

---

## Mathematical Functions

Perform calculations and mathematical operations.

| Function | Description | Example |
|----------|-------------|---------|
| [abs](./abs) | Absolute value | `{{abs(model.value)}}` |
| [ceiling](./ceiling) | Round up to integer | `{{ceiling(model.value)}}` |
| [floor](./floor) | Round down to integer | `{{floor(model.value)}}` |
| [round](./round) | Round to nearest | `{{round(model.value, 2)}}` |
| [truncate](./truncate) | Truncate decimal | `{{truncate(model.value)}}` |
| [sqrt](./sqrt) | Square root | `{{sqrt(model.value)}}` |
| [pow](./pow) | Raise to power | `{{pow(model.base, model.exp)}}` |
| [exp](./exp) | Exponential (e^x) | `{{exp(model.value)}}` |
| [log](./log) | Natural logarithm | `{{log(model.value)}}` |
| [log10](./log10) | Base-10 logarithm | `{{log10(model.value)}}` |
| [sign](./sign) | Sign of number (-1, 0, 1) | `{{sign(model.value)}}` |
| [sin](./sin) | Sine | `{{sin(model.radians)}}` |
| [cos](./cos) | Cosine | `{{cos(model.radians)}}` |
| [tan](./tan) | Tangent | `{{tan(model.radians)}}` |
| [asin](./asin) | Arcsine | `{{asin(model.value)}}` |
| [acos](./acos) | Arccosine | `{{acos(model.value)}}` |
| [atan](./atan) | Arctangent | `{{atan(model.value)}}` |
| [degrees](./degrees) | Convert radians to degrees | `{{degrees(model.radians)}}` |
| [radians](./radians) | Convert degrees to radians | `{{radians(model.degrees)}}` |
| [pi](./pi) | Pi constant (3.14159...) | `{{pi()}}` |
| [e](./e) | Euler's number (2.71828...) | `{{e()}}` |
| [random](./random) | Random number | `{{random()}}` |

---

## Date & Time Functions

Work with dates and timestamps.

| Function | Description | Example |
|----------|-------------|---------|
| [addDays](./addDays) | Add days to date | `{{addDays(model.date, 7)}}` |
| [addMonths](./addMonths) | Add months to date | `{{addMonths(model.date, 1)}}` |
| [addYears](./addYears) | Add years to date | `{{addYears(model.date, 1)}}` |
| [addHours](./addHours) | Add hours to date | `{{addHours(model.date, 2)}}` |
| [addMinutes](./addMinutes) | Add minutes to date | `{{addMinutes(model.date, 30)}}` |
| [addSeconds](./addSeconds) | Add seconds to date | `{{addSeconds(model.date, 45)}}` |
| [addMilliseconds](./addMilliseconds) | Add milliseconds to date | `{{addMilliseconds(model.date, 500)}}` |
| [daysBetween](./daysBetween) | Days between two dates | `{{daysBetween(model.start, model.end)}}` |
| [hoursBetween](./hoursBetween) | Hours between two dates | `{{hoursBetween(model.start, model.end)}}` |
| [minutesBetween](./minutesBetween) | Minutes between two dates | `{{minutesBetween(model.start, model.end)}}` |
| [secondsBetween](./secondsBetween) | Seconds between two dates | `{{secondsBetween(model.start, model.end)}}` |
| [yearOf](./yearOf) | Extract year | `{{yearOf(model.date)}}` |
| [monthOfYear](./monthOfYear) | Extract month (1-12) | `{{monthOfYear(model.date)}}` |
| [dayOfMonth](./dayOfMonth) | Extract day (1-31) | `{{dayOfMonth(model.date)}}` |
| [dayOfWeek](./dayOfWeek) | Extract day of week (0-6) | `{{dayOfWeek(model.date)}}` |
| [dayOfYear](./dayOfYear) | Extract day of year (1-366) | `{{dayOfYear(model.date)}}` |
| [hourOf](./hourOf) | Extract hour (0-23) | `{{hourOf(model.date)}}` |
| [minuteOf](./minuteOf) | Extract minute (0-59) | `{{minuteOf(model.date)}}` |
| [secondOf](./secondOf) | Extract second (0-59) | `{{secondOf(model.date)}}` |
| [millisecondOf](./millisecondOf) | Extract millisecond (0-999) | `{{millisecondOf(model.date)}}` |

---

## Logical Functions

Control flow and conditional logic within expressions.

| Function | Description | Example |
|----------|-------------|---------|
| [if](./if) | Ternary conditional | `{{if(model.active, 'Yes', 'No')}}` |
| [ifError](./ifError) | Fallback on error | `{{ifError(model.value, 'default')}}` |
| [in](./in) | Check if value in list | `{{in(model.status, 'active', 'pending')}}` |

---

## Collection Functions

Aggregate and manipulate collections.

| Function | Description | Example |
|----------|-------------|---------|
| [count](./count) | Count items in collection | `{{count(model.items)}}` |
| [countOf](./countOf) | Count with condition | `{{countOf(model.items, 'isActive')}}` |
| [sum](./sum) | Sum numeric values | `{{sum(model.numbers)}}` |
| [sumOf](./sumOf) | Sum property values | `{{sumOf(model.items, 'price')}}` |
| [min](./min) | Minimum value | `{{min(model.numbers)}}` |
| [minOf](./minOf) | Minimum property value | `{{minOf(model.items, 'price')}}` |
| [max](./max) | Maximum value | `{{max(model.numbers)}}` |
| [maxOf](./maxOf) | Maximum property value | `{{maxOf(model.items, 'price')}}` |
| [collect](./collect) | Extract property values | `{{collect(model.items, 'name')}}` |
| [each](./each) | Iterate with function | `{{each(model.items, 'transform')}}` |
| [eachOf](./eachOf) | Iterate property with function | `{{eachOf(model.items, 'prop', 'fn')}}` |
| [firstWhere](./firstWhere) | Find first matching item | `{{firstWhere(model.items, 'isActive')}}` |
| [selectWhere](./selectWhere) | Filter collection | `{{selectWhere(model.items, 'isActive')}}` |
| [sortBy](./sortBy) | Sort by property | `{{sortBy(model.items, 'name')}}` |
| [reverse](./reverse) | Reverse order | `{{reverse(model.items)}}` |

---

## Statistical Functions

Calculate statistics on collections.

| Function | Description | Example |
|----------|-------------|---------|
| [average](./average) | Average of values | `{{average(model.numbers)}}` |
| [averageOf](./averageOf) | Average of property | `{{averageOf(model.items, 'price')}}` |
| [mean](./mean) | Mean value | `{{mean(model.numbers)}}` |
| [median](./median) | Median value | `{{median(model.numbers)}}` |
| [mode](./mode) | Mode (most frequent) | `{{mode(model.numbers)}}` |

---

## CSS Functions

Dynamic CSS calculations.

| Function | Description | Example |
|----------|-------------|---------|
| [calc](./calc.md) | CSS calc expression | `{{calc('100% - 20pt')}}` |
| [var](./var.md) | CSS variable reference | `{{var('primary-color')}}` |

---

## Common Patterns

### Formatting Currency



{% raw %}
```handlebars
<p>Total: {{format(model.total, 'C2')}}</p>
<!-- Output: Total: $1,234.56 -->
```
{% endraw %}



### Date Calculations



{% raw %}
```handlebars
<p>Due: {{format(addDays(model.orderDate, 30), 'MMMM dd, yyyy')}}</p>
<!-- Output: Due: April 14, 2024 -->
```
{% endraw %}



### Conditional Values



{% raw %}
```handlebars
<span class="{{if(model.score >= 70, 'pass', 'fail')}}">
  Score: {{model.score}}
</span>
<!-- Output: <span class="pass">Score: 85</span> -->
```
{% endraw %}



### Collection Aggregation



{% raw %}
```handlebars
<p>Total Items: {{count(model.items)}}</p>
<p>Total Price: {{format(sumOf(model.items, 'price'), 'C2')}}</p>
<p>Average: {{format(averageOf(model.items, 'price'), 'C2')}}</p>
```
{% endraw %}



### String Manipulation



{% raw %}
```handlebars
<h2>{{toUpper(substring(model.title, 0, 1))}}{{substring(model.title, 1)}}</h2>
<!-- Output: Capitalize first letter -->
```
{% endraw %}



---

## See Also

- [Handlebars Helpers](../helpers/) - Control flow and context management
- [Binding Operators](../operators/) - Mathematical, comparison, and logical operators
- [Expressions Guide](../../learning/02-data-binding/02_expression_functions.html) - Complete guide to expressions

---
