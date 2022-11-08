---
layout: default
title: No Frame Options
parent: Getting Started
nav_order: 3
---

# No Frame Options
{: .no_toc }

It may be that, as a designer or configurator, there is no ability to support frames within your platform of choice. As a convenience Paperwork offers a preview option that can be invoked from a link.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## As a minimum

The minimum the link requires a template

{% raw %}
```html

    <a href='https://www.paperworkday.net/preview?template=https%3A%2F%2Fraw.githubusercontent.com%2Frichard-scryber%2FPaperworkDayDocs%2Fmain%2Fdocs%2F_samples%2Fnodata%2Fhelloworld.html' target='paperwork_preview' >Preview Sample</a>

```
{% endraw %}

This will open a new window or tab with the contents of the template 'https:www.paperworkday.info/samples/nodata/helloworld.html' within a full pane.

<a href='https://www.paperworkday.net/preview?template=https%3A%2F%2Fraw.githubusercontent.com%2Frichard-scryber%2FPaperworkDayDocs%2Fmain%2Fdocs%2F_samples%2Fnodata%2Fhelloworld.html' target='paperwork_preview' >Preview Sample</a>

---

## Builder and option

Within the preview pane, there is an optional builder. Simple append the `&builder=true` parameter and you can create your own url's to copy and paste into your pages.

{% raw %}
```html

    <a href='https://www.paperworkday.net/preview?template=https%3A%2F%2Fraw.githubusercontent.com%2Frichard-scryber%2FPaperworkDayDocs%2Fmain%2Fdocs%2F_samples%2Fnodata%2Fhelloworld.html&builder=true' target='paperwork_preview' >Preview Sample</a>

```
{% endraw %}


<a href='https://www.paperworkday.net/preview?template=https%3A%2F%2Fraw.githubusercontent.com%2Frichard-scryber%2FPaperworkDayDocs%2Fmain%2Fdocs%2F_samples%2Fnodata%2Fhelloworld.html%0A&builder=true' target='paperwork_preview' >Preview Sample</a>


{: .note }
> Although, we can make no assurance that anyone cannot access this link, it is always loaded as the current user, 
> if they cannot access the data or template, then they cannot see the preview.

---

## The builder options

![](https://www.paperworkday.info/assets/builderOptions.png)

---

## The Options

The options match directly to the configuration available on the init and generate options, except that the template and data can only be an absolute url link, so they are specified directly.

<dl>
    <dt>Template Path</dt>
    <dd>This is the <strong>required</strong> absolute url to the xhtml template to generate a file from</dd>
    <dt>Data Path</dt>
    <dd>This is the <emphasis>optional</emphasis> absolute url to the json dynamic data to generate a file with.</dd>
    <dt>User Interface options</dt>
    <dd>This optional set of flags define the functional user interface elements that will be shown on the client when initialized, and or a document is generated. </dd>
    <dt>theme</dt>
    <dd>There are currently 2 themes available. 'dark' and 'light' with the default being dark. Or for subscribers there are also `custom-dark` and `custom-light` themes from your own stylesheets.</dd>
    <dt>width</dt>
    <dd>This optional css unit of size string, will set the starting width of the frame (and or wrapper)</dd>
    <dt>height</dt>
    <dd>This optional css unit of size string, will set the starting height of the frame (and or wrapper)</dd>
    <dt>scale</dt>
    <dd>This optional numeric value will set the initial percentage scale of the preview when a document is first generated.</dd>
    <dt>page</dt>
    <dd>This optional numeric value, will set the starting page number within the document. The first page is 1</dd>
    <dt>loaded:</dt>
    <dd>This optional function will be called once the frame has been created and is ready with a reference to the frame.</dd>
</dl>

If, for some reason, none of the above interface elements are wanted, then the `None` option can be explicitly provided.

---

## Build, or build and go

With the build action, the Preview Url will be updated based on the selections, with the Build and Go, 
the page will be refreshed with the requested options and the builder available. 

When happy, the link can be coppied and used in any pages as is.

{% raw %}
```html

    <a href='https://www.paperworkday.net/preview.html?ui=None&template=https%3A%2F%2Fraw.githubusercontent.com%2Frichard-scryber%2FPaperworkDayDocs%2Fmain%2Fdocs%2F_samples%2Fnodata%2Fhelloworld.html' target='_blank' >Open my document</a>
    
```
{% endraw %}

---
