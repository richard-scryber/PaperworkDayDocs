---
layout: default
title: SVG Attributes
parent: Template reference
has_children: true
has_toc: true
nav_order: 7
---

# SVG Attribute Reference
{: .no_toc }

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

## Overview

The <a href='' >SVG elements</a> support a range of attributes to control their appearance and behaviour. Many of these attributes are shared with HTML elements, and some are specific to SVG.

### Unsupported Attributes

When re-using existing content, there are a lot of attributes that can be on an SVG file that are not supported, or relevant to the library. By default these attributes will be skipped over and ignored. However if running in <code>Strict</code> <a href='/learning/templates/conformancemode.html'>conformance mode</a> the library will raise an error each time it encounters an unknown attribute or attribute value.

---

### CSS vs Attributes

Within the attribute tables below, if a property supports being set from styles, then the name is showm. 

**NOTE**: Not all properties can support being set from styles, and some that are defined within the SVG specification, are pending implementation. A style property has a higher priority than an attribute value on the element.

---

### Case sensitivity

By default **All** attributes are *case sensitive*.

---


### Binding values to attributes

When included in the document either inline with the rest of the content or <a href='/reference/htmltags/embed.html' >embedded</a> into the content the attributes support binging to dynamic data. As an image the binding will be empty.

```html
   {{% raw %}}<html xmlns='http://www.w3.org/1999/xhtml'>
    <head>
      <title>SVG Attribute Binding</title>
    </head>
    <body>
       <!-- An inline SVG drawing --> 
       <svg xmlns='http://www.w3.org/2000/svg' viewport='0 0 30 30' 
          width='{{model.display.width ?? "100pt"}}' height='{{model.display.height ?? "100pt"}}'>
          <rect x='10' y='10' width='{{model.logo.width}}' height='{{model.logo.height}}' />
          <text fill='{{model.logo.color}}'>{{model.logo.title}}</rect>
        </svg>

        <!-- An embedded SVG drawing will also receive the binding with model.logo --> 
        <embed source='./mydrawing.svg' />

        <!-- An referenced SVG drawing as a static image will NOT be bound --> 
        <img src='./mydrawing.svg' />

    </body>
   </html>{{% endraw %}}
```

---

## Supported Attributes

The following attributes, spilt into functional groups, are supported by the library.

---

## Standard Html Attributes.

The html global attributes are also available on the svg elements. 

| Element  | Tag  |  Description |
|---|---|---|
| <a href='attrs/id.html' >Element ID</a>   | <code>&lt;id&gt;</code> | The unique identifier for this element within the document. This can be used to reference the element from styles other elements inside and outside the svg for non-image content. |
| <a href='attrs/class.html' >Class name(s)</a>   | <code>&lt;class&gt;</code> | Zero or more names of css classes that will be used to match against for styling the element. |
| <a href='attrs/style.html' >Inline style values</a>   | <code>&lt;style&gt;</code> | The css style attribute for applying visual style to an element directly. See the <a href='/learning/styles/'>Styles</a> for more information.  |
| <a href='attrs/hidden.html' >Is Hidden</a>   | <code>&lt;hidden&gt;</code> | This mirrors the library implementation, as it is a fast and easy way to show and hide content dynamically.  |
| <a href='attrs/title.html' >Outline Title</a>   | <code>&lt;title&gt;</code> | This mirrors the library implementation of <a href='/reference/htmlattributes/title.html'>outline title attribute</a> and is also available as a <a href='/reference/svgelements/title.html'>title inner element</a>  |

---

## Position and Size Attributes

By default all the svg visual elements are absolutely positioned relative to their containing SVG canvas. Many have their own indivdual position and size properties, and should be confirmed with each of the elements.

| Element  | Tag | Description |
|---|---|---|
| <a href='attrs/x.html' >X Position</a>   | <code>&lt;x&gt;</code> | The x coordinate position of the element within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Used by the svg, rect, use, text, tspan, image and pattern.    |
| <a href='attrs/y.html' >Y Position</a>   | <code>&lt;y&gt;</code> | The y coordinate position of the element within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Used by the svg, rect, use, text, tspan, image and pattern. |
| <a href='attrs/x1.html' >First X Position</a>   | <code>&lt;x1&gt;</code> | The x coordinate position of the start of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the horizontal start point of the line a linear gradient will follow.  |
| <a href='attrs/y1.html' >First Y Position</a>   | <code>&lt;y1&gt;</code> | The y coordinate position of the start of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the vertical start point of the line a linear gradient will follow. |
| <a href='attrs/x2.html' >Second X Position</a>   | <code>&lt;x2&gt;</code> |  The x coordinate position of the end of line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the horizontal end point of the line a linear gradient will follow.  |
| <a href='attrs/y2.html' >Y Position</a>   | <code>&lt;y2&gt;</code> | The y coordinate position of the end of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the vertical end point of the line a linear gradient will follow.

---

## Binding operators

All operators

---

## Binding conversion functions

All conversion functions
