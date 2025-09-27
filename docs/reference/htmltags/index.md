---
layout: default
title: HTML Elements
parent: Template reference
has_children: true
has_toc: false
nav_order: 5
---

# Supported HTML Element Reference
{: .no_toc }

The library supports the use of (x)html elements, also referred to a tags to structure content within a template. This can be extended by embedding external files, or dymamically binding elements.

The root level of a document should always be the <code>&lt;html&gt;</code> element, preferably using the xmlns attribute namespace to define the content as xhtml. Followed by the <code>&lt;head&gt;</code> element for document meta data (to describe the the document) and then a <code>&lt;body&gt;</code> to contain the content of the document. 

```
   {% raw %} &lt;html xmlns='http://www.w3.org/1999/xhtml'&gt;
    &lt;head&gt;

    &lt;/head&gt;
    &lt;body&gt;
   
      &lt;!-- add further content --&gt;

    &lt/body&gt;
   &lt;/html&gt; {% endraw %}
```

Or use the <code>&lt;frameset&gt;</code> if modifying an existing document.

More information on actual document creation can be found in <a href='/index.html'>Getting Started</a>

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

### Comments

Enclosing any content starting with a <code>&lt!-</code> and ending with <code>--&gt</code> will mark a comment within the document.

This content will not be processed, and be ignored. It can either be used to exclude content whilst creating a template, or adding context to the structure of a document.

### Modifying or updating existing documents.

Along with the creation of new documents, it is possible to modify a previously created document - adding new pages or removing existing pages.

This is done with the <code>&lt;frameset&gt;</code> element, replacing the body, and more information can be found <a href='/learning/templates/frameset.html' >here</a>

### Case sensitivity

By default **all** elements are case sensitive and are all lower case.

## Document Root

The root of a document is always the <code>&lt;html&gt;</code> element. A DTD and or processing instructions (<code>{% raw %}<?  ?>{% endraw %}</code>) along with whitespace and comments are allowed before the outermost html element

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/html.html' >Html Root</a>   | <code>&lt;html&gt;</code> | Marks the start of a complete document template, and encapsulates all references, metadata and content for that template.   |

## Sectioning Root

Within the document there should always be a <code>&lt;head&gt;</code> for the metadata and either a <code>&lt;body&gt;</code> or <code>&lt;frameset&gt;</code> for the actual content.

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/head.html' >Head Content</a>   | <code>&lt;head&gt;</code> | Will mark the beginning of the metadata for the document.   |
| <a href='tags/body.html' >Body Content</a>   | <code>&lt;body&gt;</code> | Will mark the beginning of the visual content within the document.   |
| <a href='tags/header.html' >Page Header</a>   | <code>&lt;header&gt;</code> | An optional element within <code>&lt;body&gt;</code> that begins a new content block for elements that will be shown at the top of every page of the document **including** the first page, *unless* a continuation header is defined.   |
| <a href='tags/footer.html' >Page Footer</a>   | <code>&lt;footer&gt;</code> | An optional element within <code>&lt;body&gt;</code> that begins a new content block for elements that will be shown at the bottom of every page of the document **including** the first page, *unless* a continuation header is defined.   |
| <a href='tags/contheader.html' >Continuation Header *</a>   | <code>&lt;continuation-header&gt;</code> | An optional element within <code>&lt;body&gt;</code> that begins a new content block for elements that will be shown at the top of every page of the document **except** the first page.   |
| <a href='tags/contfooter.html' >Continuation Footer *</a>   | <code>&lt;continuation-footer&gt;</code> | An optional element within <code>&lt;body&gt;</code> that begins a new content block for elements that will be shown at the bottom of every page of the document **except** the first page.   |
| <a href='tags/frameset.html' >Frameset Content</a>   | <code>&lt;frameset&gt;</code> | Will mark the beginning of a set of frames that a source document, or template and a set of pages from that document to include. Replaces the <code>&lt;body&gt;</code> element.   |
| <a href='tags/frame.html' >Frame</a>   | <code>&lt;frame&gt;</code> | An within a <code>&lt;frameset&gt;</code> that begins a new section of content from within an existing document, or from a referenced template.  |


---

## Document Metadata

The library supports the use of the following relational operators for comparing values.

| Operator  | Example  | Description |
|---|---|---|
| <a href='ops/equals.html' >Equals '==' </a>   | LHS == RHS | Will return true if the left and right side are the same value, otherwise false. If the types of values are different, then an attempt to convert to the same value will be made.   |


---

## Content Sectioning

The library supports the use of the following logical operators.

| Operator  | Example  | Description |
|---|---|---|


---

## Structural content

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/boolean.html' >Boolean Function</a>   | boolean(expr) | Will return true if the contained expression can be converted to a true value, otherwise false, or false if the contained expression results in false. The contained expression can be a constant or another expression, and an attempt to convert to boolean will be made.  |


## Dynamic Content

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/abs.html' >Abs Function</a>   | abs(expr) | Will return true if the contained expression can be converted to a true value, otherwise false, or false if the contained expression results in false. The contained expression can be a constant or another expression, and an attempt to convert to boolean will be made.  |




## Image and Multimedia

To manipulate string (character) values, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/concat.html' >Concatenate Function</a>   | concat(expr [, expr, expr, ...]) | Will take any length of parameters and concatenate them into a single string returning the result. If one of the parameters is a collection or array, then each of the entries in that array will be appended to the string in order. |



## Inline text semantics

The date functions work on (Gregorian) DateTime values, to convert strings, use one of the date() conversion function overloads.

**Note**" When working with the current date time value, it will increase as the document is processed unless it is stored in a <code>var</code> value.


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/adddays.html' >Add Days Function</a>   | adddays(expr , count) | Adds the specified number of days in the second parameter (either positive or negative), to the date value in the first parameter, returning the result |


---


## Forms Content

The library supports the use of the following logical functions.

| Operator  | Example  | Description |
|---|---|---|
| <a href='funcs/if.html' >If Function </a>   | if(expr, trueresult, falseresult) | Checks the first parameter and if the result is true, then returns the second parameter, otherwise the third parameter is evaluated and returned.   |

--

