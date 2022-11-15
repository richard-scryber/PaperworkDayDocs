---
layout: default
title: Page Headers and Footers
parent: Template Content
nav_order: 1
---

# Template Content
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

## A Page header and footer.



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

        header, footer { 
          padding-bottom: 5px;
          border-bottom: solid 1px silver;
          border-top: solid 1px silver;
          margin-bottom: 5px;
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

<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='buttonGenerate' class='document-container' name='HeadersAndFooters' data-template='templates/headersAndFooters/pageHeadersAndFooters.html' data-pw-ui="Default, Code, Edit" ></div>


## Margins and Padding

Within the page, the margins will be applied to the body
