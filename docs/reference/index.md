---
layout: default
title: Template Reference
has_children: true
nav_order: 4
has_toc: false
---

# Template content refererence
{: .no_toc }

All the elements, attributes, style selectors and properties that paperwork and the core library support

---

### <a href='htmltags/index.html'>HTML element refererence</a>

The HTML tags such as <c>&lt;html&gt;</c>, or <c>&lt;div&gt;</c> within a template or referernced source give the structure and content to your document. This section details all the HTML tags that the core library supports, along with the available (and unavailable attributes) that the tag supports - including those that are specific to the library.

### <a href='htmlattributes/index.html'>HTML attribute refererence</a>

The HTML attributes alter the behaviour of their containing tag such as <c>&lt;div id='idAttrValue' &gt;</c>. This section details all the attributes that the core library supports, along with the supported values for the attribute, and also elements it can be used on (and cannot) - including those that are specific to the library.


### <a href='cssselectors/index.html'>CSS selector and at rule reference</a>

Separating the visual design from the actual content of a template is done using the standard css notation within a <c>&lt;style&gt;</c> element or including references to css style sheets. The selectors such as <c>.className</c> and / or <c>#refId</c> .  This sections details all the supported (and not supported) selectors in the library, along with the at rules such as <c>@media</c> that allow selectorss to be regulated on their application within the library.

### <a href='cssproperties/index.html'>CSS style properties reference</a>

Styling properties such as <c>font-style: italic;</c> or <c>background-image: var(model.logo);</c> are defined within selectors to be applied to matching content tags, or drawing elements. This section details the available properties, what values can be assigned to them, and which tags/elements support them.


### <a href='binding/index.html'>Binding Expressions reference</a>

Binding content within templates to external or calculated data is key to creating dynamic documents and can be within the <c>{{ handle bars notation }}</c> or within style properties with the <c>width: calc(model.size + 10pt)</c>. This sections details all the available expressions and functions that can be used within a template (or passed content) to dynamically alter the output, or layout, or design of the resultant document.

### <a href='svgelements/index.html'>SVG drawing element refererence</a>

Drawing within a template is based around inline or databound svg elements in the content, and must be qualified with the svg namespace (e.g. <c>&lt;svg xmlns='http://www.w3.org/2000/svg' &gt;...&lt;svg&gt;</c>) or referenced via the <c>&lt;img src='mydrawing.svg' /&gt;</c> element. This section details all the SVG Drawing elements that the core library supports, along with the available (and unavailable attributes) that the tag supports.

### <a href='svgattributes/index.html'>SVG drawing attribute refererence</a>

The SVG attributes such as <c>@width</c> or <c>@fill</c> alter the appearance and behaviour of their containing element, e.g. <c>&lt;rect width="20pt" height="40pt" fill="aqua" /&gt;</c>. This section details all the attributes that the core library supports, along with the supported values for the attribute, and also elements it can be used on (and cannot).

