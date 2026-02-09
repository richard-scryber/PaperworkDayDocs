---
layout: default
title: Home
has_children: true
has_toc: false
nav_order: 0
---

# Welcome to the home of Scryber.Core library documentation
{: .no_toc}

If you are new here then jump straight into the <a href='./learning/01-getting-started/'>Getting Started</a> section.

### NOTE
The documentation is **IN REVIEW** phase. The reference section will be more accurate than the learing guides as it is rolled out. 

So if you do discover an inconsistency whilst trying to do something. Then check the reference section - if it's still incorrect then please do reach out via the [GitHub](https://github.com/richard-scryber/scryber.core) issue and discussion tabs.

<details class='top-toc' markdown="block">
  <summary>
    On this page
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

### Getting Around

This documentation is meant to support your use of the library. The navigation on the left (or top) will allow you to move around the docs without visiting every page in turn.

Most pages contain a table of contents for that page, istelf, and then further links so you can dive deeper of move to a related subject.

Finally if you know what you are looking for, then the search is available at the top.


### Learning the Scryber.Core library

The first section is for the Learing guides which covers the capabilities the library in general terms.

There are 8 individual modules

1. [Getting Started](learning/01_getting_started) - This comprehensive guide will take you from complete beginner to confident PDF document creator.
2. [Data Binding and Expressions](learning/02-data-bindng) - Transform static templates into dynamic, data-driven PDF documents with Scryber’s powerful data binding system.
3. [Styling and Appearance](learning/03-styling) - Master CSS styling to create beautiful, professional-looking PDF documents with Scryber.Core.
4. [Layout and Positioning](learning/04-layout) - Master page-based layout, positioning, and document structure to create professional multi-page PDF documents.
5. [Tyography and Fonts](learning/05-typography) - Use the advanced typography and font features, including font properties, custom fonts, using remote fonts sucha as Google fonts and FontAwesome text spacing, alignment, and advanced typographic techniques for professional PDF documents.
6. [Content Components](learning/06-content) - Start adding images, SVG graphics, lists, tables, and embedded content to create rich, data-driven PDF documents.
7. [Document Configuration](learning/07-configuration) - Configure logging, security, conformance, and optimization for production-ready PDF documents.
8. [Practical Applications](learning/08-poctical) - Learn through complete, real-world examples - from invoices to reports, certificates to catalogs. Highlighting specific features.


### Reference section

The reference section is split into 7 sections covering each of the major components with examples of usage, and samples.

1. [HTML Elements](reference/htmltags) - The HTML tags such as `<html>`, or `<div>` within a template or referernced source give the structure and content to your document
2. [HTML Attributes](reference/htmlattributes) - This section details all the attributes that the core library supports, along with the supported values for the attribute.
3. [CSS Selectors][cssselectors/index] - This sections details all the supported (and not supported) selectors in the library, along with the at rules such as @media that allow selectorss to be regulated on their application within the library.
4. [CSS Properties](reference/cssproperties/) - Styling properties such as font-style: italic; or background-image: var(model.logo); are defined within selectors to be applied to matching content tags, or drawing elements.
5. [Binding Operators and Functions](reference/binding) - Covers all data binding structures available in Scryber templates, including Handlebars helpers, operators, and expression functions.
6. [SVG Elements](reference/svgelements) - This section details all the SVG Drawing elements that the core library supports, along with the available (and unavailable attributes) that the tag supports.
7. [SVG Attributes](reference/svgattributes) - This section details all the attributes that the core library supports, along with the supported values for the attribute, and also elements it can be used on (and cannot).

