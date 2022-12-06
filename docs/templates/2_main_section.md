---
layout: default
title: Main and Sections
parent: Template Content
nav_order: 2
---

# Section element, plus Main and Article elements
{: .no_toc }

Paperwork supports the use of the section, main and article element of the template to give structure to content along with different page size / proportions.

By default the section element will force a new page (adding the document headers and footers as appropriate). Main and article will not be on a new page unless explicitly set.

All 3 elements support having their own header and footer content within the flow of the document.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## A section within a main content flow.


<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='mainElement' class='document-container' name='mainElement' data-pw-template='_samples/templates/headersAndFooters/mainElement.html' data-pw-ui="Default, Code, Edit" ></div>
(Edit the content to view the source)


Here there is a main content within the body, and a section that will break onto a new page, with the main content following again after the section. Body headers and footers are repeated.

{: .note }
> When forcing a new page with the nested section any padding, margins and border are preserved on the
> parent element as the inner section is built.


## An Article with explicit new page.

An article is by default the same as the main element, supporting headers and footers. To force an article onto a new page, then a style attribute can be applied to ensure that an article is always on a new page using the `page-break-before` equal to `always` in this case (`page-break-after` is also supported).

<div id='articleElement' class='document-container' name='articleElement' data-pw-template='_samples/templates/headersAndFooters/breakingArticleElement.html' data-pw-ui="Default, Code, Edit" ></div>

{: .note }
> Any element can have the the page break style applied to it, but deeply nesting may cause layout 
> issues.

## Further reading

<dl>
  <dt>Page break styles</dt>
  <dd>See <a href='../styles/13_pages' >Pages</a> for more information the use of page breaks, along with changing the page size.</dd>
  <dt>Page headers and footers</dt>
  <dd>See <a href='../templates/1_header_footer' >Body, Headers & Footers</a> for more information the repeating page headers and footers</dd>
</dl>
