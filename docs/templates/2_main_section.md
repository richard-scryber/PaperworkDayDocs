---
layout: default
title: Main and Sections
parent: Template Content
nav_order: 2
---

# Section element, plus Main and Article elements
{: .no_toc }

Paperwork supports the use of the section, main and article element of the template to give structure to content along with different page size / proportions.

By default the section element will force a new page (adding the document headers and footers as appropriate). Main and article will not be on a new page unless explicitly set.

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

## A section within a main content flow.


<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='mainElement' class='document-container' name='mainElement' data-pw-template='_samples/templates/headersAndFooters/mainElement.html' data-pw-ui="Default, Code, Edit" ></div>

Here there is a main content within the body, and a section that will break onto a new page, with the main content following after any body headers and footers.


