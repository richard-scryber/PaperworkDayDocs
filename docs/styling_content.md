---
layout: default
title: Styling Content
has_children: true
nav_order: 3
---

# Styling Content
{: .no_toc }

Paperwork uses css for the styling of template content, this can either be in linked files from the template, in a style element of the template head, or directly on the element itself.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Basic Style


Css styles can either be referenced from `link` elements in the head or as `style` elements with css content, again in the head, or declared on the element itself.

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

## Supported style selectors


---

## Units and measurements

---

## Built in and remote fonts

---



## At rule styles

With @rules Paperwork can be used to import content, specify page sizes and add specific print styles to existing stylesheets.

---

## Binding data and expressions

The paperwork binding implementation is flexible and pervasive. It is supported within the content of an element, on the attributes, or even within styles and referenced stylesheets.
