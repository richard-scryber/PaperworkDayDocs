---
layout: default
title: Body, Headers & Footers
parent: Template Content
nav_order: 1
---

# The body, headers and footers
{: .no_toc }

Paperwork supports the use of page headers and footers within the body element of the template. These will repeat across multiple pages when content overflows.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## A header and footer.


{% raw %}
```html

    <?scryber append-log='false' log-level='Verbose' ?>
    <html xmlns="http://www.w3.org/1999/xhtml" >
    <head>
        <title>Hello world document</title>
        <style>
        body {
        padding : 10px;
        font-size: 14pt;
      }
      header, footer {
        padding-bottom: 5px;
        border-bottom: solid 1px silver;
        border-top: solid 1px silver;
        margin-bottom: 5px;
        font-size: 12pt
      }
        </style>
    </head>
    <body>
        <header>
          This is the page header.
        </header>
        <h2>Main Page content.</h2>
        <p>Lorem Ipsum.....

          <!-- Content truncated for brevity -->

          ....tristique tempor sapien.
        </p>
        <footer>
            This is the footer on page <page />, and any content can be added to the header and footer to make it flow across multiple lines and reduce the inner content space of the page.
        </footer>
    </body>
    </html>

```
{% endraw %}

---

## Repeating Headers and footers example

The following example shows a simple repeating header and footer on each of the page, as the content flows along.


<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='buttonGenerate' class='document-container' name='HeadersAndFooters' data-pw-template='_samples/templates/headersAndFooters/pageHeadersAndFooters.html' data-pw-ui="Default, Code, Edit" ></div>


## Margins, Padding and spacing.

Within the page, the margins and padding will be applied to **both** the body content and the headers and footers. And the default body padding is 20pt so it is evenly spaced on a page without any effort. Sometimes, though, this can lead to excessive spacing around all elements, and it is easier to remove the margins, and only apply to inner content

{% raw %}
```html

  <?scryber append-log='false' log-level='Verbose' ?>
  <html xmlns="http://www.w3.org/1999/xhtml" >
  <head>
      <title>Hello world document</title>
      <style>
  body {
      margin: 0px;
      padding : 0px;
      font-size: 14pt;
      background-color: #aaa;
    }
    header, footer {
      margin: 0px;
      padding: 10px;
      font-size: 12pt;
      background-color: #999;
    }

    p{
      margin: 10px;
      padding: 10px;
      background-color: #ddd;
    }
      </style>
  </head>
  <body>
      <header>
        <div>This is the page header.</div>
      </header>
      <p>Lorem Ipsum.....
        ....tristique tempor sapien.
      </p>
      <footer>
          <div>This is the footer on page <page />.</div>
      </footer>
  </body>
  </html>

```
{% endraw %}


<div id='paddingExample' class='document-container' name='HeadersAndFootersWithPadding' data-pw-template='_samples/templates/headersAndFooters/pageHeadersAndFootersPadding.html' data-pw-ui="Default, Code, Edit" ></div>


---

## Further reading

<dl>
  <dt>Page Numbers</dt>
  <dd>Paperwork supports the display of page numbers, both current and total within the footer and main content using the custom inline `page` element.<br/>
      The default (no attributes) will simply show the current page number but a `data-format` attribute can be applied (See <a href='11_page_numbers.html' >Page Numbering</a> for more details).</dd>

  <dt>Page Breaks</dt>
  <dd>Explictly splitting content at a particular place within the content can be done with the `page-break-before` and `page-break-after` styles. <br/>
      These are covered in more details in the <a href='2_main_section.html' >Next</a> section.</dd>

  <dt>Page Sizes</dt>
  <dd>Page sizes are fixed for the content within an element, except when a new page is applied. They can be changed globally and for that specific element that begins a new page.<br/>
      This is covered in the <a href='../styles/13_pages.html' >Page styles</a> section.</dd>
</dl>

---