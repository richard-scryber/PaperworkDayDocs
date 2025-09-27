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

The root level of a document should always be the <code>&lt;html&gt;</code> element, (preferably) using the xmlns attribute namespace to define the content as xhtml. Followed by the <code>&lt;head&gt;</code> element for document meta data (to describe the the document) and then a <code>&lt;body&gt;</code> to contain the content of the document. 

```
   <html xmlns='http://www.w3.org/1999/xhtml'>
    <head>

    </head>
    <body>
   
      <!-- add further content -->

    </body>
   </html>
```


More information on actual document creation can be found in <a href='/index.html'>Getting Started</a>

---

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

---

### Modifying or updating existing documents.

Along with the creation of new documents, it is possible to modify a previously created document - adding new pages or removing existing pages.

This is done with the <code>&lt;frameset&gt;</code> element, replacing the body, and more information can be found <a href='/learning/templates/frameset.html' >here</a>

---

### Case sensitivity

By default **all** elements are *case sensitive* and are all lower case.

---

## Document Root Elements

The root of a document is always the <code>&lt;html&gt;</code> element. Known DTD and or processing instructions (<code>&lt;?  ?&gt;</code>) along with whitespace and comments are supported before the outermost html element

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/html.html' >Html Root</a>   | <code>&lt;html&gt;</code> | Marks the start of a complete document template, and encapsulates all references, metadata and content for that template.   |

---

## Sectioning Root Elements

Within the document there should be a <code>&lt;head&gt;</code> for the metadata and either a <code>&lt;body&gt;</code> or <code>&lt;frameset&gt;</code> for the actual content.

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/head.html' >Head Content</a>   | <code>&lt;head&gt;</code> | Will mark the beginning of the metadata section for the document.   |
| <a href='tags/body.html' >Body Content</a>   | <code>&lt;body&gt;</code> | Will mark the beginning of the visible content within the document.   |
| <a href='tags/header.html' >Page Header</a>   | <code>&lt;header&gt;</code> | Begins a new block for content that will be shown at the top of the first page of the document, and all subsequent pages within a <code>&lt;body&gt;</code> element, <u>**unless**</u> a continuation header is defined.   |
| <a href='tags/footer.html' >Page Footer</a>   | <code>&lt;footer&gt;</code> | Begins a new content block for elements that will be shown at the bottom of the first page of the document, and all subsequent pages within a <code>&lt;body&gt;</code> element, <u>**unless**</u> a continuation header is defined.   |
| <a href='tags/contheader.html' >Continuation Header *</a>   | <code>&lt;continuation&#8209;header&gt;</code> | Begins a new content block for elements that will be shown at the top of every page of the document, within a <code>&lt;body&gt;</code> element <u>**except**</u> the first page.   |
| <a href='tags/contfooter.html' >Continuation Footer *</a>   | <code>&lt;continuation&#8209;footer&gt;</code> | Begins a new content block for elements that will be shown at the bottom of every page of the document, within a <code>&lt;body&gt;</code> element <u>**except**</u> the first page.   |
| <a href='tags/frameset.html' >Frameset Content</a>   | <code>&lt;frameset&gt;</code> | Will mark the beginning of a set of <code>&lt;frame&gt;</code> elements that a source document, or template and a set of pages from that document to include. Replaces the <code>&lt;body&gt;</code> element.   |
| <a href='tags/frame.html' >Frame</a>   | <code>&lt;frame&gt;</code> | An element within a <code>&lt;frameset&gt;</code> that begins a new section of content from within an existing document, or from a referenced template.  |


---

## Document Metadata Elements

The library supports the use of the following elements within the meta-data <code>&lt;head&gt;</code> of the document.

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/title.html' >Document Title</a>   | <code>&lt;title&gt;</code> | A purely textual value that will set the display title for the output document.   |
| <a href='tags/base.html' >Document Base Path</a>   | <code>&lt;base&gt;</code> | A folder or uri reference to to a path where any relative files specified in the content of the document (images etc.) can be located.  |
| <a href='tags/meta.html' >Meta data</a>   | <code>&lt;meta&gt;</code> | A generalized informational tag that can define information about the final document production, its owners or security settings for use.  |
| <a href='tags/link.html' >Linked files</a>   | <code>&lt;link&gt;</code> | References an external file that contains resources (specifically styles) that the document should use when generating the output.  |
| <a href='tags/styles.html' >Style content</a>   | <code>&lt;style&gt;</code> | Marks the document specific visual styles for the content that the document should use. Has a higher priority than any linked stylesheets.  |



---

## Content Sectioning Elements

The library supports the use of the following sectioning elements used to divide up the main content of the template into significant blocks.

| Operator  | Example  | Description |
|---|---|---|
| <a href='tags/address.html' >Address</a>   | <code>&lt;address&gt;</code> | Denotes a single block of content that is a physical address.   |
| <a href='tags/article.html' >Article</a>   | <code>&lt;article&gt;</code> | Denotes a continuous block of content that is on a specific subject.  |
| <a href='tags/aside.html' >Aside</a>   | <code>&lt;aside&gt;</code> | Denotes a block of content that is not part of the current main content but relevant to place at the location.  |
| <a href='tags/headings.html' >Headings 1-6</a>   | <code>&lt;h1&gt; - &lt;h6&gt;</code> | Denotes a heading within the content. Levels vary in importance from level 1 down to 6.  |
| <a href='tags/main.html' >Main</a>   | <code>&lt;main&gt;</code> | Marks the content within the template that contains the majority of the document content.  |
| <a href='tags/nav.html' >Nav</a>   | <code>&lt;nav&gt;</code> | Marks the content within the template that performs navigation functions.  |
| <a href='tags/section.html' >Section</a>   | <code>&lt;section&gt;</code> | Denotes a block of content within the template that is in discreet. **NOTE:** By default each section in a template will start on a new page in the output document. |

---

## Structural Content Elements

To convert values of one type to another, the following functions are available.


| Function  | Example  | Description |
|---|---|---|
| <a href='tags/blockquote.html' >Block Quote</a>   | <code>&lt;blockquote&gt;</code> | Denotes a quote within the context of the temlate that is separate from the primary content |
| <a href='tags/details.html' >Details</a>   | <code>&lt;details&gt;</code> | Denotes a block of content that has a summery (below) and then further information available to provide greater clarity.|
| <a href='tags/summary.html' >Details Summary</a>   | <code>&lt;summary&gt;</code> | Denotes the shorter information of a details block before the main information |
| <a href='tags/dl.html' >Definition List</a>   | <code>&lt;dl&gt;</code> |  |
| <a href='tags/dt.html' >Definition List Term</a>   | <code>&lt;dt&gt;</code> |  |
| <a href='tags/dd.html' >Definition List Item</a>   | <code>&lt;dd&gt;</code> |  |
| <a href='tags/div.html' >Div</a>   | <code>&lt;div&gt;</code> | Denotes a discrete block of content, without specific meaining |
| <a href='tags/figure.html' >Figure</a>   | <code>&lt;figure&gt;</code> |  |
| <a href='tags/figcaption.html' >Figure Caption</a>   | <code>&lt;figcaption&gt;</code> |  |
| <a href='tags/hr.html' >Horizontal Rule</a>   | <code>&lt;hr&gt;</code> |  |
| <a href='tags/ol.html' >List Ordered</a>   | <code>&lt;ol&gt;</code> |  |
| <a href='tags/ul.html' >List Unordered</a>   | <code>&lt;ul&gt;</code> |  |
| <a href='tags/li.html' >List Item</a>   | <code>&lt;li&gt;</code> |  |
| <a href='tags/menu.html' >Menu List</a>   | <code>&lt;li&gt;</code> |  |
| <a href='tags/p.html' >Paragraph</a>   | <code>&lt;p&gt;</code> |  |
| <a href='tags/pre.html' >Pre-formatted</a>   | <code>&lt;pre&gt;</code> |  |
| <a href='tags/span.html' >Span</a>   | <code>&lt;span&gt;</code> |  |

---

## Table Content Elements

Description

| <a href='tags/table.html' >Table</a>   | <code>&lt;table&gt;</code> |  |
| <a href='tags/tbody.html' >Table Body</a>   | <code>&lt;tbody&gt;</code> |  |
| <a href='tags/thead.html' >Table Header</a>   | <code>&lt;thead&gt;</code> |  |
| <a href='tags/tfoot.html' >Table Footer</a>   | <code>&lt;tfoot&gt;</code> |  |
| <a href='tags/tr.html' >Table Row</a>   | <code>&lt;tr&gt;</code> |  |
| <a href='tags/td.html' >Table Cell</a>   | <code>&lt;td&gt;</code> |  |
| <a href='tags/th.html' >Table Header Cell</a>   | <code>&lt;th&gt;</code> |  |

---

## Dynamic Content Elements

To


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/a.html' >Anchor Link</a>   | <code>&lt;a&gt;</code> |   |
| <a href='funcs/embed.html' >Anchor Link</a>   | <code>&lt;embed&gt;</code> |   |
| <a href='funcs/fragment.html' >Fragment</a>   | <code>&lt;fragment&gt;</code> |   |
| <a href='funcs/if.html' >If *</a>   | <code>&lt;if&gt;</code> |   |
| <a href='funcs/iframe.html' >i-Frame</a>   | <code>&lt;iframe&gt;</code> |   |
| <a href='funcs/object.html' >Object</a>   | <code>&lt;object&gt;</code> |   |
| <a href='funcs/page.html' >Page Number</a>   | <code>&lt;page&gt;</code> |   |
| <a href='funcs/template.html' >Template Content</a>   | <code>&lt;template&gt;</code> |   |
| <a href='funcs/var.html' >Variable Store and Display</a>   | <code>&lt;var&gt;</code> |  |

---

## Image and Multimedia Elements

To 


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/img.html' >Image Content</a>   | <code>&lt;img&gt;</code>|  |
| <a href='funcs/picture.html' >Picture Content</a>   | <code>&lt;picture&gt;</code> |  |
| <a href='funcs/meter.html' >Meters</a>   | <code>&lt;meter&gt;</code> |  |
| <a href='funcs/progress.html' >Progress</a>   | <code>&lt;progress&gt;</code> |  |

---

## Inline Text Semantic Elements

The 


| Function  | Example  | Description |
|---|---|---|
| <a href='funcs/abbr.html' >Abbreviation</a>   | <code>&lt;abbr&gt;</code> |  |
| <a href='funcs/big.html' >Big</a>   | <code>&lt;big&gt;</code> |  |
| <a href='funcs/b.html' >Bold</a>   | <code>&lt;b&gt;</code> |  |
| <a href='funcs/cite.html' >Citation</a>   | <code>&lt;cite&gt;</code> |  |
| <a href='funcs/code.html' >Code</a>   | <code>&lt;code&gt;</code> |  |
| <a href='funcs/defn.html' >Definition</a>   | <code>&lt;defn&gt;</code> |  |
| <a href='funcs/del.html' >Mark Deleted</a>   | <code>&lt;del&gt;</code> |  |
| <a href='funcs/em.html' >Emphasised</a>   | <code>&lt;em&gt;</code> |  |
| <a href='funcs/font.html' >Font style</a>   | <code>&lt;font&gt;</code> |  |
| <a href='funcs/ins.html' >Mark Inserted</a>   | <code>&lt;ins&gt;</code> |  |
| <a href='funcs/i.html' >Italic</a>   | <code>&lt;i&gt;</code> |  |
| <a href='funcs/kbd.html' >Keyboard</a>   | <code>&lt;kbd&gt;</code> |  |
| <a href='funcs/br.html' >Line Break</a>   | <code>&lt;br&gt;</code> |  |
| <a href='funcs/mark.html' >Marked span</a>   | <code>&lt;mark&gt;</code> |  |
| <a href='funcs/num.html' >Number</a>   | <code>&lt;num&gt;</code> |  |
| <a href='funcs/output.html' >Output</a>   | <code>&lt;output&gt;</code> |  |
| <a href='funcs/q.html' >Quoted Span</a>   | <code>&lt;q&gt;</code> |  |
| <a href='funcs/em.html' >Sample Span</a>   | <code>&lt;samp&gt;</code> |  |
| <a href='funcs/small.html' >Small</a>   | <code>&lt;small&gt;</code> |  |
| <a href='funcs/strike.html' >Strikethrough</a>   | <code>&lt;strike&gt;</code> |  |
| <a href='funcs/strong.html' >Strong style</a>   | <code>&lt;strong&gt;</code> |  |
| <a href='funcs/sub.html' >Subscript</a>   | <code>&lt;sub&gt;</code> |  |
| <a href='funcs/sup.html' >Superscript</a>   | <code>&lt;sup&gt;</code> |  |
| <a href='funcs/time.html' >Time Span</a>   | <code>&lt;time&gt;</code> |  |
| <a href='funcs/u.html' >Underlined</a>   | <code>&lt;u&gt;</code> |  |

---


## Forms Content Elements <span class='label label-yellow'>alpha</span>

The library supports the use of the following logical functions.

| Operator  | Example  | Description |
|---|---|---|
| <a href='funcs/if.html' >If Function </a>   | if(expr, trueresult, falseresult) | Checks the first parameter and if the result is true, then returns the second parameter, otherwise the third parameter is evaluated and returned.   |

---

