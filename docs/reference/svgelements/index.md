---
layout: default
title: SVG Elements
parent: Template reference
has_children: true
has_toc: true
nav_order: 6
---

# SVG Element Reference
{: .no_toc }

Drawing vector content within a document is supported using the well-known <code>svg</code> elements from the XML based markup. Although the library only supports part of the SVG specification, a significat proportion, of the static SVG capabilities are available, and most reference images and sources should work without modification as long as they do not rely on filters or animations.

The svg elements can be included inline or as an <a href='/reference/htmltags/tags/embed.html'>embedded</a> set of content. Or as a referenced <a href='/reference/htmltags/tags/img.html'>image</a> source. However, only inline or embedded content will get the full binding capability, so drawings can show dynamic values, or styles.

The SVG elements are grouped by function  

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Filters.

The filters defined in SVG are used to modify colors and blends of objects based on their raster data, as a vector description of document content, it is not possible to know the raster colour image of a drawing until the final rendition by the reading application.

---

## Animations

SVG supports a range of animation elements and attributes, however these are not supported in the library at this time, as the document output format is generically a static format.

## Unsupported Element Handling

If the library encounters an element it does not understand then, by default, it will skip over the element and all its inner content, moving down to the next sibling (or the end of the document).

If the <a href='/learning/templates/conformancemode.html'>conformance mode</a> is set to <code>strict</code>, then an error will be raised so that any offending content can be tracked if there is an issue.

---

## SVG Root Element

The root of a document is always the <code>&lt;html&gt;</code> element. Any known DTD and or processing instructions (<code>&lt;?&nbsp;&nbsp;?&gt;</code>) along with whitespace and comments are supported before the outermost html element

| Element  | Tag  | Description |
|---|---|---|
| <a href='tags/svg.html' >SVG Root /Container</a>   | <code>&lt;svg&gt;</code> | Marks the start of a complete svg drawing template, and encapsulates all references, metadata and content for that template.   |


---

## Document Elements

| Element  | Tag  | Description |
|---|---|---|
| <a href='tags/style.html' >Styles Declarations</a>   | <code>&lt;style&gt;</code> |  |
| <a href='tags/defs.html' >Shape Definitions</a>   | <code>&lt;defs&gt;</code> |  |


---

## Graphic Elements

The following basic shapes are supported

| Element  | Tag  | Description |
|---|---|---|
| <a href='tags/rect.html' >Rectangle</a>   | <code>&lt;rect&gt;</code> |  |
| <a href='tags/circle.html' >Circle</a>   | <code>&lt;circle&gt;</code> |  |
| <a href='tags/ellipse.html' >Ellipse</a>   | <code>&lt;ellipse&gt;</code> |  |
| <a href='tags/line.html' >Single Line</a>   | <code>&lt;line&gt;</code> |  |
| <a href='tags/polygon.html' >Mulitpoint Closed Shape</a>   | <code>&lt;polygon&gt;</code> |  |
| <a href='tags/polyline.html' >Multipoint Open Line</a>   | <code>&lt;polyline&gt;</code> |  |
| <a href='tags/path.html' >Graphics Path</a>   | <code>&lt;path&gt;</code> |  |
| <a href='tags/image.html' >Referenced Image</a>   | <code>&lt;image&gt;</code> |  |

---

## Structural Elements

All conversion functions

| Element  | Tag  | Description |
|---|---|---|
| <a href='tags/g.html' >Group</a>   | <code>&lt;g&gt;</code> |  |
| <a href='tags/use.html' >Graphic Use Reference</a>   | <code>&lt;use&gt;</code> |  |
| <a href='tags/symbol.html' >Symbol Definition</a>   | <code>&lt;symbol&gt;</code> |  |
| <a href='tags/a.html' >Anchor Link</a>   | <code>&lt;a&gt;</code> |  |


---

## Text Content Elements

| <a href='tags/text.html' >Text</a>   | <code>&lt;text&gt;</code> |  |
| <a href='tags/tspan.html' >Inner Text Span</a>   | <code>&lt;tspan&gt;</code> |  |

---

## Paint Elements

| Element  | Tag  | Description |
|---|---|---|
| <a href='tags/linearGradient.html' >Linear Gradient Definition</a>   | <code>&lt;linearGradient&gt;</code> |  |
| <a href='tags/radialGradient.html' >Radial Gradient Definition</a>   | <code>&lt;radialGradient&gt;</code> |  |
| <a href='tags/pattern.html' >Pattern Definition</a>   | <code>&lt;pattern&gt;</code> |  |
| <a href='tags/marker.html' >Marker Definition</a>   | <code>&lt;marker&gt;</code> |  |
| <a href='tags/stop.html' >Gradient Stop Definition</a>   | <code>&lt;stop&gt;</code> |  |





