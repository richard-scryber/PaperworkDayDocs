---
layout: default
title: Main and Sections
parent: Template Content
nav_order: 2
---

# Section element, plus Main and Article elements
{: .no_toc }

Paperwork supports the use of the section, main and article element of the template to give structure to content along with different page size / proportions.


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

## A section element.

By default, a section element will force a new page (adding the document page headers and footers as appropriate). 

The section header shows at the start of the section and the footer at the end (irrespective of the order in the content, or overflowing onto new pages), and can be styled either globally or explicitly

The content after the section will flow as normal.

{% raw %}
```html

  <?scryber append-log='false' log-level='Verbose' ?>
  <html xmlns="http://www.w3.org/1999/xhtml" >
  <head>
      <title>Main with nested section</title>
      <style>
      body {
          padding : 10px;
          font-size: 14pt;
      }
      /* appied to any headers inclding body and section  */
      header, footer {
          border-bottom: solid 1px silver;
          border-top: solid 1px silver;
          margin: 5px 0px;
          font-size: 12pt
      }
      
      section{
          color: red;
      }

      /* Applies just to section headers */
      section > header{
          border-bottom-color: red;
          border-top-color: red;
      }
      
      </style>
  </head>
  <body>
      <header>
          This is the body header.
      </header>
      <h2>Initial body content.</h2>
      <p>Lorem ipsum ...... aliquet.
      </p>
      <section>
          <header style="color:blue">Section Header on a new page</header>
          <h2>Section inner content.</h2>
          <p>Nullam scelerisque .... vestibulum dui.</p>
          <p>Nulla quis purus .... pretium.</p>
          <footer>Section Footer on page <page /></footer>
      </section>
      <section>
          <header>Second section forcing another new page</header>
          <footer>Section Footer on page <page /></footer>
          <h2>Section inner content.</h2>
          <p>Nullam scelerisque .... vestibulum dui.</p>
          <p>Nulla quis purus .... pretium.
          </p>
        
      </section>
      <h2>Continuation of the main content after a section</h2>
      <p>Suspendisse pellentesque .... ante.</p>
      <footer>
          This is the footer on page <page />.
      </footer>
  </body>
  </html>

```
{% endraw %}


<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='mainElement' class='document-container' name='mainElement' data-pw-template='_samples/templates/headersAndFooters/sectionElement.html' data-pw-ui="Default, Code, Edit" ></div>



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
  <dt>Page styles</dt>
  <dd>See <a href='../styles/13_pages' >Pages</a> for more information the use of page breaks, along with changing the page size.</dd>
  <dt>Page headers and footers</dt>
  <dd>See <a href='../templates/1_header_footer' >Body, Headers & Footers</a> for more information the repeating page headers and footers</dd>
</dl>
