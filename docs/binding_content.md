---
layout: default
title: Binding Content
has_children: true
nav_order: 4
---

# Binding Content
{: .no_toc }

Paperwork uses handlebars syntax (by default), for dynamically binding values in any provided data to elements within the template, along with supporting repeating content and complex expresssions.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Basic Binding

The basic template is xhtml and has the **required** xml namespace (`xmlns`) attribute set to "http://www.w3.org/1999/xhtml", with an optional `scryber` processing instruction infront.

The head element supports the standard `title`, `base`, `style` and `link` inner elements.

The `body` defines the content of the page(s) within the document including most html elements, inline svg content and graphic images.

Css styles can either be referenced from `link` elements in the head or as inline `style` elements with css content.

{: .note}
> For linked content, the html head has a `base` element that can be used for referencing 
> files without having to provide the full path. 

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

## Repeating templates

With @rules Paperwork can be used to import content, specify page sizes and add specific print styles to existing stylesheets.

---

## Complex expressions and calculations

The paperwork binding implementation is flexible and pervasive. It is supported within the content of an element, on the attributes, or even within styles and referenced stylesheets.

---

## Calc and var within styles.
