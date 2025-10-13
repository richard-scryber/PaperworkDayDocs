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

CSS support within SVG is limited. The preferred approach for the library is to bind to and calculate from reference values in the data.

**NOTE**: CSS Support for properties will be added based on repeatable results from browsers.

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

### Standard Html Attributes.

The html global attributes are also available on the svg elements. 

| Element  | Tag  |  Description |
|---|---|---|
| <a href='attrs/id.html' >Element ID</a>   | <code>id</code> | The unique identifier for this element within the document. This can be used to reference the element from styles other elements inside and outside the svg for non-image content. |
| <a href='attrs/class.html' >Class name(s)</a>   | <code>class</code> | Zero or more names of css classes that will be used to match against for styling the element. |
| <a href='attrs/style.html' >Inline style values</a>   | <code>style</code> | The css style attribute for applying visual style to an element directly. See the <a href='/learning/styles/'>Styles</a> for more information.  |
| <a href='attrs/hidden.html' >Is Hidden</a>   | <code>hidden</code> | This mirrors the library implementation, as it is a fast and easy way to show and hide content dynamically.  |
| <a href='attrs/title.html' >Outline Title</a>   | <code>title</code> | This mirrors the library implementation of <a href='/reference/htmlattributes/title.html'>outline title attribute</a> and is also available as a <a href='/reference/svgelements/title.html'>title inner element</a>  |

---

## Scaling and View Attributes

The followning attributes alter the size., shape and aspect ratio of teh SVG canvas and elements within a canvas.

| Element  | Tag | Description |
|---|---|---|
| <a href='attrs/viewBox.html' >View Box</a> | <code>viewBox</code>  | Defines the rectangular position and size of a proportion of the inner drawing content that will be shown in the parent content, or of the canvas as a whole within the document. |
| <a href='attrs/preserveAspectRatio.html' >Preserve Aspect Ratio</a> | <code>preserveAspectRatio</code>  | Defines how the inner drawing content will be aligned and scaled to fit the parent content, or of the canvas as a whole within the document. |
| <a href='attrs/transform.html' >Element Transformation Operations</a> | <code>transform</code>  | Defines one or more transformation instrictions to be performed on the element for presentation within the canvas or as a whole within the document. |
| <a href='attrs/transform-origin.html' >Element Transformation Origin</a> | <code>transform-origin</code>  | Defines the origin point within the element that is being transformed - the point at which the transformations will be set from. |

---


## Position and Size Attributes

By default all the svg visual elements are absolutely positioned relative to their containing SVG canvas. Many have their own indivdual position and size properties, and should be confirmed with each of the elements.

| Element  | Tag | Description |
|---|---|---|
| <a href='attrs/cx.html' >Centre X Position</a>   | <code>cx</code> | The x coordinate position of the centre of a circle or ellipse within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings.   |
| <a href='attrs/cy.html' >Centre Y Position</a>   | <code>cy</code> | The y coordinate position of the centre of a circle or ellipse within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. |
| <a href='attrs/dx.html' >Delta (offset) X Position</a>   | <code>dx</code> | The x coordinate position of a text block or text span, relative to is parent. |
| <a href='attrs/dy.html' >Delta (offset) Y Position</a>   | <code>dy</code> | The y coordinate position of a text block or text span, relative to is parent. |
| <a href='attrs/x.html' >X Position</a>   | <code>x</code> | The x coordinate position of the element within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Used by the svg, rect, use, text, tspan, image and pattern.    |
| <a href='attrs/y.html' >Y Position</a>   | <code>y</code> | The y coordinate position of the element within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Used by the svg, rect, use, text, tspan, image and pattern. |
| <a href='attrs/x1.html' >First X Position</a>   | <code>x1</code> | The x coordinate position of the start of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the horizontal start point of the line a linear gradient will follow.  |
| <a href='attrs/y1.html' >First Y Position</a>   | <code>y1</code> | The y coordinate position of the start of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the vertical start point of the line a linear gradient will follow. |
| <a href='attrs/x2.html' >Second X Position</a>   | <code>x2</code> |  The x coordinate position of the end of line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the horizontal end point of the line a linear gradient will follow.  |
| <a href='attrs/y2.html' >Y Position</a>   | <code>y2</code> | The y coordinate position of the end of a line within the svg canvas. This is usually relative to the top left corner of the canvas, but can be altered by groups, transforms and viewbox settings. Also defines the vertical end point of the line a linear gradient will follow. |
| <a href='attrs/r.html' >Circle Radius</a>   | <code>r</code> | The radius of a circle element. |
| <a href='attrs/rx.html' >X Radius</a>   | <code>rx</code> |  The horizontal (x) radius of an ellipse element, and also the corner x radius of a rectangle elements. |
| <a href='attrs/ry.html' >Y Radius</a>   | <code>ry</code> | The vertical (y) radius of an ellipse element, and also the corner y radius of a rectangle elements.|
| <a href='attrs/refx.html' >X Reference Point</a>   | <code>refX</code> |  The horizontal (x) position of the referernce point for a marker. |
| <a href='attrs/refy.html' >Y Reference Point</a>   | <code>refY</code> | The vertical (y) position of the reference point for a marker.|
| <a href='attrs/width.html' >Element Width</a>   | <code>width</code> |  The horizontal size of an svg canvas, or elements within a canvas. |
| <a href='attrs/height.html' >Element Height</a>   | <code>height</code> | The vertical size of an svg canvas, or elements within a canvas. |

---

## Path Operation Attrbutes

The following attributes define the position of points, lines, arcs within complex shapes in the SVG canvas.

| Element  | Tag | Description |
|---|---|---|
| <a href='attrs/d.html' >Path Data</a>   | <code>d</code> |  The vector drawing instructions for a complex path. |
| <a href='attrs/points.html' >Poly Points</a>   | <code>points</code> | The set of points to draw for a poly-line or polygon. |

---


## Stroke and Fill Attributes

The following attributes control the visual appearance of elements around the edge and within the shape.

| Element  | Tag | Description |
|---|---|---|
| <a href='attrs/fill.html' >Element Fill</a>   | <code>fill</code> | A known color or a url reference to a defined pattern or gradient to use to flood fill the elements shape. |
| <a href='attrs/fill-opacity.html' >Element Fill Opacity</a>   | <code>fill-opacity</code> | Defines the visibility of content underneath the elements shape and how transparent the flood fill will be. |
| <a href='attrs/fill-rule.html' >Element Fill Rule</a>   | <code>fill-rule</code> | Defines how a point within the shape will be considered as 'inside' and hence whether it will be filled. |
| <a href='attrs/opacity.html' >Element Opacity</a>   | <code>opacity</code> | Specifies the transparency of an complete object or of a group of objects, that is, the degree to which the background behind the element is visible behind. |
| <a href='attrs/stroke.html' >Element Stroke</a>   | <code>stroke</code> | A known color or a url reference (TBC) to a defined pattern or gradient to use to render an edge around the elements shape or characters. |
| <a href='attrs/stroke-dasharray.html' >Element Stroke Dash Spacing</a> | <code>stroke-dasharray</code> | A series of numbers defining the repeating dashes and gaps used to render the border of a shape or character |
| <a href='attrs/stroke-opacity.html' >Element Stroke Opacity</a>   | <code>stroke-opacity</code> | Defines the visibility of the border around the elements shape or characters and how transparent the stroke will be. |
| <a href='attrs/stroke-width.html' >Element Stroke Width</a>   | <code>stroke-width</code> | Defines the width of the stroke around the elements shape or characters. |
| <a href='attrs/stroke-linecap.html' >Element Stroke Line Cap</a> | <code>stroke-linecap</code> | Defines the type of ending to be rendered for an open shape or character. |
| <a href='attrs/stroke-linejoin.html' >Element Stroke Line Join</a> | <code>stroke-linejoin</code> | Defines the type of join to be rendered at corners within a shape or character. |
| <a href='attrs/stroke-width.html' >Element Stroke Width</a> | <code>stroke-width</code> | Defines the thicknes of any stroke to be rendered around a shape or character. |

---

## Text Layout Attributes

All conversion functions

---

## Patterns and Gradient Attributes

All conversion functions

---
