---
layout: default
title: Document Head
parent: Template Content
has_children: false
nav_order: 0
---

# Document Head
{: .no_toc }

The head section within the root `html` element sets up the standard document properties, as well as supporting the addition of links to stylesheets and in-template styles.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Document Level Properties



{: .note}
> As the template is xml, then all elements MUST be properly closed. 
> Not closing an element will cause the parsing of the template to fail or be unpredictable.

{% raw %}
```html

    <?scryber append-log='false' log-level='Verbose' ?>
    <html xmlns="http://www.w3.org/1999/xhtml" >
    <head>
        <title>Hello world document</title>
        <style>
        body {
            padding : 20px;
        }

        </style>
    </head>
    <body>
        <h2>Hello World.</h2>
        <p>From everyone at Paperwork</p>
    </body>
    </html>

```
{% endraw %}

---

## Scryber processing instruction

Paperwork is built on our open source [Scryber Core Library](https://github.com/richard-scryber/scryber.core) library. As part of that it is possible to understand what is happening behind the scenes with the `scryber`
processing instruction.

The following are the supported options on the processing instruction.

* 'append-log' - Controls the tracing log output for a single document - 'true' or 'false' to add the log to the output document
* 'log-level' - This is an enumeration of the granularity of the logging performed on the pdf file. Values supported (from least to most) are 'None', 'Errors', 'Warnings', 'Messages', 'Verbose', 'Diagnostic'.
* 'parser-log' - Controls the logging from the xml parser when walking through the template, and any associated files.
* 'parser-culture' - specifies the global culture settings when parsing a file for interpreting dates and number formats in the content. e.g. 'en-GB', 'fr-FR'
* 'parser-mode' - Defines how errors will be recorded if unknown or invalid attributes values are encountered. 'Strict' will raise exceptions, 'Lax' will record the error but continue/

See :doc:`extending_logging` for a detailed explanation of the tracing and logging capabilities in the scryber library which is **really** useful when trying to hunt down issues.

{: .note }
> A log-level of Diagnostic will be extremely lengthy.
> And if appended can dramatically slow down any composition or rendering.
>
> Use with caution!

---

## Supported body elements

Whilst not a true html to document conversion engine. Paperwork uses the xhtml structure to reduce the learning curve and provide a framework to match to.

The following elements can be used within the body of a document template, and should match most expected behaviour. See each section individually to see what attributes and inner content are supported.

<dl>
    <dt>Page headers and footers</dt>
    <dd>The `header` and `footer` elements are supported on the body element for page headers and page footers (repeating on each page). 
    <br/>`continuation-header` and `continuation-footer` are also possible on the `body` if needed for subsequent pages.
    <br/>The main and section elements can be within a body and support their own headers and footers for new pages</dd>
    <dt>Heading elements</dt>
    <dd>`h1` to `h6` elements are fully supported with rich content.</dd>
    <dt>Block elements</dt>
    <dd>`div`, `p`, `main`, `article`, `section`, `nav`, `blockquote` are supported, and will, by default, be block elements starting and ending on a new line within the document. They can also be nested.</dd>
    <dt>Inline elements</dt>
    <dd>The simple inline elements: `span`, `b`, `i`, `u`, `strike`, `strong`, `emphasis` and `label` are supported with the usual textual adornments on specific </dd>
    <dt>Discreet inline elements</dt>
    <dd>The elements: `num`, `time` are supported with formatting for displaying numbers and dates.<br/>
        And a custom element `page` for displaying the current page or the page number of another element within the document.</dd>
    <dt>Table elements</dt>
    <dd>The standard `table` with inner `thead`, `tbody`, `tfoot` along with `tr` and `td` are supported (including column spans, but not currently row spans)</dd>
    <dt>Lists</dt>
    <dd>The lists are supported for unordered (`ul`) and ordered (`ol`) with the inner `li` elements. And definition lists (`dl`) with inner `dt` and `dd` content.</dd>
    <dt>Images</dt>
    <dd>All png, jpg, tiff, and bmp images should be supported based on their encoding.</dd>
    <dt>Code and pre-formatted content</dt>
    <dd>The `code` inline element along with the `pre` block element are supported.</dd>
    <dt>Links</dt>
    <dd>The anchor link to content either within the current document or external content is supported.</dd>
    <dt>Breaks</dt>
    <dd>The line break, `br` and horizontal rule, `hr` can be included within the body content - as xhtml e.g. &gt;br /&lt;  &gt;hr /&lt; </dd>
    <dt>Included content</dt>
    <dd>The `embed` and `iframe` elements will accept content from an external source to be included within the document using the `src` attribute.</dd>
    <dt>Template content</dt>
    <dd>The `template` element allows repeating data to be used as part of the normal flow of the document. This is the true power, and discussed in the [DataBinding](Binding) section.</dd>
</dl>

There are a few omissions from the full HTML5 set, but is a functional group of elements. More may be added in the future such as forms, fieldsets, cite and figure.

{: .note}
> Currently the form, input, select and button elements are not supported
> This may be something that will be supported in the future.
>
> Let us know if this is something important to you.

---

## Standard attributes

Paperwork supports the standard set of html attributes on all elements, along with specific attributes within that element, and somestimes a couple more to support the binding

<dl>
    <dt>id</dt>
    <dd>The `id` attribute on each element supports the use of links within documents and navigation.</dd>
    <dt>name</dt>
    <dd>A `name` attribute can also be used insted of an id for links, and is less prescriptive on format.</dd>
    <dt>hidden</dt>
    <dd>The hidden attribute is a string value that can dynamically show and hide content (inlcuding any child content).<br/>
        This is in addition to any style:display value as the visibility is more prominant and can be set with `hidden`. Any other value will be treated as not hidden.</dd>
    <dt>title</dt>
    <dd>The `title` is a human readable string attribute, as a description of the content, and forms the book mark hierarchy with inner titled content.</dd>
    <dt>class</dt>
    <dd>The `class` is a space separated list of class names to be applied to the element and styles from any css will be applied to the element when laid out and rendered based on these classes.</dd>
    <dt>style</dt>
    <dd>The `style` attribute creates a specific css descriptor applied directly to the element after all other styles have be applied</dd>
    
</dl>

---


