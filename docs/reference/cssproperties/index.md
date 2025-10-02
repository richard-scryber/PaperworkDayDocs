---
layout: default
title: CSS Style Properties
parent: Template reference
has_children: true
has_toc: false
nav_order: 4
---

# CSS Style Property Reference
{: .no_toc }

Within the style attribute of a visual element, or a selector in a stylesheet or group, properties alter the actual visual apperance of the element they are on, or matched to. Each property has a name and one or more values, depending on what is being set.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Property Value Keywords

Initial, Inherit, etc.

## Element Fills.

The following properties are supported to alter the basic color of elements.


| Property  | Description |
|---|---|
| <a href='properties/color.html' >color</a>   |  Defines the fill color of any character content, and any decoration applied. |
| <a href='properties/opacity.html' >opacity</a>   | Defines the opacity of the element itself. |

---

## Element Backgrounds.

The following properties are supported to alter the background appearance of 'boxed'* elements **NOTE**: The background area is a rectangular shape including any padding are that is applied to the elelemt (and chaildren).


| Property  | Description |
|---|---|
| <a href='properties/background.html' >background</a>   | A shorthand pproperty for setting the background properties of an element. |
| <a href='properties/background-color.html' >background-color</a>   | Specifies the colour that will fill the entire background. |
| <a href='properties/background-image.html' >background-image</a>   | Specifies an image, or gradient, that will fill the entire background. |
| <a href='properties/background-repeat.html' >background-repeat</a>   | Specifies how that image, if it is smaller than the element size will repeat.  |
| <a href='properties/background-size.html' >background-size</a>   | Specifies the horizontal and vertical size of the image to repeat |
| <a href='properties/background-position.html' >background-position</a>   | Specifies both the horizontal and vertical starting postion of the image (including the repeat). |
| <a href='properties/background-position-x.html' >background-position-x</a>   | Specifies just the horizontal starting postion of the image (including the repeat). |
| <a href='properties/background-position-y.html' >background-psition-y</a>   | Specifies Just the vertical starting postion of the image (including the repeat). |

---

## Element Borders

The following properties alter the border appearance on 'boxed'* elements. **NOTE**: By default borders do not affect the spacing around an element. Thick borders will impinge on outer and inner content, if no margins or padding are applied.

| Property  | Description |
|---|---|
| <a href='properties/border.html' >border</a>   | A shorthand property of setting the style, width and color of all the borders |
| <a href='properties/border-width.html' >border-width</a>   | Sets the width of all the borders around an element. |
| <a href='properties/borde-color.html' >border-color</a>   | Sets the color of all the borders around an element.  |
| <a href='properties/border-style.html' >border-style</a>   | Sets the style (solid, dash, none) of all the borders around an element. |
| <a href='properties/border-radius.html' >border-radius</a>   | Sets the corner radius, of a border when switching between sides. Only one value is (currently) supported. |
| <a href='properties/border-top.html' >border-top</a>   | A shorthand property of setting the style, width and color of the top borders.  |
| <a href='properties/border-top-color.html' >border-top-color</a>   | Sets the color of the top border of an element. |
| <a href='properties/border-top-width.html' >border-top-width</a>   | Sets the width of the top border of an element. |
| <a href='properties/border-top-style.html' >border-top-style</a>   | Sets the style of the top border of an element. |
| <a href='properties/border-left.html' >border-left</a>   | A shorthand property of setting the style, width and color of the left borders. |
| <a href='properties/border-left-color.html' >border-left-color</a>   | Sets the color of the left border of an element. |
| <a href='properties/border-left-width.html' >border-left-width</a>   | Sets the width of the left border of an element. |
| <a href='properties/border-left-style.html' >border-left-style</a>   | Sets the style of the left border of an element. |
| <a href='properties/border-bottom.html' >border-bottom</a>   | A shorthand property of setting the style, width and color of the bottom borders. |
| <a href='properties/border-bottom-color.html' >border-bottom-color</a>   | Sets the color of the bottom border of an element. |
| <a href='properties/border-bottom-width.html' >border-bottom-width</a>   | Sets the width of the bottom border of an element. |
| <a href='properties/border-bottom-style.html' >border-bottom-style</a>   | Sets the style of the bottom border of an element. |
| <a href='properties/border-right.html' >border-top</a>   | A shorthand property of setting the style, width and color of the right borders. |
| <a href='properties/border-right-color.html' >border-right-color</a>   | Sets the color of the right border of an element. |
| <a href='properties/border-right-width.html' >border-right-width</a>   | Sets the width of the right border of an element. |
| <a href='properties/border-right-style.html' >border-right-style</a>   | Sets the style of the right border of an element. |

---

## Element Position and Size.

The following properties are supported to alter the position and size appearance of 'boxed'* elements.

| Property  | Description |
|---|---|
| <a href='properties/position.html' >position</a> |    |
| <a href='properties/display.html' >display</a> | |
| <a href='properties/float.html' >float</a> |  |
| <a href='properties/top.html' >top</a> |  |
| <a href='properties/left.html' >left</a> |  |
| <a href='properties/bottom.html' >bottom</a> |  |
| <a href='properties/right.html' >right</a> |  |
| <a href='properties/width.html' >width</a>  |  |
| <a href='properties/height.html' >height</a> |    |
| <a href='properties/min-width.html' >min-width</a>   |    |
| <a href='properties/min-height.html' >min-height</a>   | |
| <a href='properties/max-width.html' >max-width</a>   |  |
| <a href='properties/max-height.html' >max-height</a>   |  |
| <a href='properties/transform.html' >transform</a>   |  |
| <a href='properties/overflow.html' >overflow</a>   |  |

---

## Element Spacing

The following properties manage the spacing in and around 'boxed'* elements.

| Property  | Description |
|---|---|
| <a href='properties/padding.html' >padding</a>   |  |
| <a href='properties/padding-top.html' >padding-top</a>   |  |
| <a href='properties/padding-left.html' >padding-left</a>   |  |
| <a href='properties/padding-bottom.html' >padding-bottom</a>   |  |
| <a href='properties/padding-right.html' >padding-right</a>   |  |
| <a href='properties/padding-inline.html' >padding-inline</a>   |  |
| <a href='properties/padding-inline-start.html' >padding-inline-start</a>   |  |
| <a href='properties/padding-inline-end.html' >padding-inline-end</a>   |  |
| <a href='properties/margin.html' >margin</a>   |  |
| <a href='properties/margin-top.html' >margin-top</a>   |  |
| <a href='properties/margin-left.html' >margin-left</a>   |  |
| <a href='properties/margin-bottom.html' >margin-bottom</a>   |  |
| <a href='properties/margin-right.html' >margin-right</a>   |  |
| <a href='properties/margin-inline.html' >margin-inline</a>   |  |
| <a href='properties/margin-inline-start.html' >margin-inline-start</a>   |  |
| <a href='properties/margin-inline-end.html' >margin-inline-end</a>   |  |

---

## Pages and Columns

The following properties control the page sizes, columns and breaks within.

| Property  | Description |
|---|---|
| <a href='properties/column-count.html' >column-count</a>   |  |
| <a href='properties/column-gap.html' >column-gap</a>   |  |
| <a href='properties/column-width.html' >column-width</a>   |  |
| <a href='properties/break-inside.html' >break-inside</a>   |  |
| <a href='properties/break-after.html' >break-after</a>   |  |
| <a href='properties/break-before.html' >break-before</a>   |  |
| <a href='properties/page-break-inside.html' >page-break-inside</a>   |  |
| <a href='properties/page-break-after.html' >page-break-after</a>   |  |
| <a href='properties/page-break-before.html' >page-break-before</a>   |  |
| <a href='properties/margin-top.html' >margin-top</a>   |  |
| <a href='properties/margin-left.html' >margin-left</a>   |  |
| <a href='properties/margin-bottom.html' >margin-bottom</a>   |  |
| <a href='properties/margin-right.html' >margin-right</a>   |  |
| <a href='properties/margin-inline.html' >margin-inline</a>   |  |
| <a href='properties/margin-inline-start.html' >margin-inline-start</a>   |  |
| <a href='properties/margin-inline-end.html' >margin-inline-end</a>   |  |

---

## Fonts and Type Faces

The following properties control the font that any text will use, including families and styles, and remote font registration.

| Property  | Description |
|---|---|
| <a href='properties/font.html' >font</a>   |  |
| <a href='properties/font-style.html' >font-style</a>   |  |
| <a href='properties/font-family.html' >font-family</a>   |  |
| <a href='properties/font-weight.html' >font-weight</a>   |  |
| <a href='properties/font-size.html' >font-size</a>   |  |
| <a href='properties/font-display.html' >font-display</a>   |  |
| <a href='properties/font-stretch.html' >font-stretch</a>   |  |
| <a href='properties/src.html' >src</a>   |  |

--- 

## Text and Character Adjustment

The following properties control the way any text within the element will be output.

| Property  | Description |
|---|---|
| <a href='properties/text-align.html' >text-align</a>   |  |
| <a href='properties/vertical-align.html' >vertical-align</a>   |  |
| <a href='properties/line-height.html' >line-height</a>   |  |
| <a href='properties/text-decoration.html' >text-decoration</a>   |  |
| <a href='properties/text-decoration-line.html' >text-decoration-line</a>   |  |
| <a href='properties/letter-spacing.html' >letter-spacing</a>   |  |
| <a href='properties/hyphens.html' >hyphens</a>   |  |
| <a href='properties/hyphenate-limit-chars.html' >hyphenate-limit-chars</a>   |  |
| <a href='properties/hyphenate-character.html' >hyphenate-character</a>   |  |
| <a href='properties/word-spacing.html' >word-spacing</a>   |  |
| <a href='properties/white-space.html' >white-space</a>   |  |


---

## Counters and Content

The following properties manage counter values, updating and displaying dynamic content.

| Property  | Description |
|---|---|
| <a href='properties/content.html' >content</a>   |  |
| <a href='properties/counter-reset.html' >counter-reset</a>   |  |
| <a href='properties/counter-increment.html' >counter-increment</a>   |  |

---

## Lists and List Items

The following properties are specific to lists and the items within them. Some are unique to the library as the functionality is not available (or difficult to replicate) in CSS < 3, but used significantly in many forms of documentation.

| Property  | Description |
|---|---|
| <a href='properties/list-style.html' >list-style</a>   |  |
| <a href='properties/list-style-type.html' >list-style-tyle</a>   |  |
| <a href='properties/pdf-li-group.html' >-pdf-li-group</a>   |  |
| <a href='properties/pdf-li-concat.html' >-pdf-li-concat</a>   |  |
| <a href='properties/pdf-li-align.html' >-pdf-li-align</a>   |  |
| <a href='properties/pdf-li-inset.html' >-pdf-li-inset</a>   |  |
| <a href='properties/pdf-li-prefix.html' >-pdf-li-prefix</a>   |  |
| <a href='properties/pdf-li-postfix.html' >-pdf-li-postfix</a>   |  |


---

* 'boxed' elements have a non pure inline display, so they encapsulate all their content within a rectangular 'box', e.g. block, or inline-block.