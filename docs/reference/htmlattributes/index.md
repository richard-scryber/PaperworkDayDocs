---
layout: default
title: HTML Attributes
parent: Template reference
has_children: true
has_toc: false
nav_order: 2
---

# Supported HTML Attribute Reference
{: .no_toc }

An attribute supports the element in which it is enclosed by adding further information in a formal and discreet manner. The library supports the use of the many standard element attributes on various <a href='../htmltags/' >Html Elements</a>. Where possible the library tries to match expected behaviour to the final output based on existing meaning.

The library also extended the behaviour of the element with a number of custom elements

```
    <body id='bId' class='main-content other-class' >
   
      <!--  custom binding repeater on a list -->

      <ol class='model-list'>
        <template id='listing' data-bind='{{model.items}}' data-bind-max='200' >
          <li id='{{"item" + index()}}' class='model-item' >{{.name}}</li>
        </template>
      </ol>

      <!-- more content -->

    </body>
```


More information on actual document creation can be found in <a href='/index.html'>Getting Started</a>. And all <a href='/reference/htmltags/' >elements</a> have a list of the specific attributes they individually support.

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

### Unsupported attributes

When re-using existing content, there are a lot of attributes that can be on an html file that are not supported, or relevant to the library. By default these attributes will be skipped over and ignored. However if running in <code>Strict</code> <a href='/learning/templates/conformancemode.html'>conformance mode</a> the library will raise an error each time it encounters an unknown attribute or attribute value.

---

### Case sensitivity

By default **all** attributes are *case sensitive* and are all lower case.

---

### Binding values to attributes

The library is strongly typed and expects specific types to be set on a value of an attribute. These can be explicity set within a template content, or created dynamically at generation time. Some attributes however are explicitly static only, or explicitly binding only - as the required type is not convertable. These are marked in tables below, with one of **Any | Binding Only | Static Only**.


## Global Attributes

The following attributes are supported on all visual elements - the elements that are within the body element, including the body element itself.

| Attribute  | Use | Bindable  | Description |
|---|---|---|--|
| <a href='global/id.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/title.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/style.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/hidden.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/class.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/name.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
|--|--|--|--|
| <a href='global/data-content.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-content-action.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-content-type.html' >data-content-type</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-content-type.html' >data-content-type</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |

---

## Global Event Attributes


The following event attributes are supported on all visual elements. For more information on document controllers and event handling see the <a href='/learning/binding/codebehind.html'>code behind</a> learning article

| Attribute  | Use  | Description |
|---|---|---|
| <a href='tags/head.html' >Head Content</a>   | <code>&lt;head&gt;</code> | Will mark the beginning of the metadata section for the document.   |


---

## Supported Standard Attributes


The library supports the use of the following standard attributes that match existing attributes on html elements.

| Attribute  | Use  | Description |
|---|---|---|
| <a href='tags/title.html' >Document Title</a>   | <code>&lt;title&gt;</code> | A purely textual value that will set the display title for the output document.   |
| <a href='tags/base.html' >Document Base Path</a>   | <code>&lt;base&gt;</code> | A folder or uri reference to to a path where any relative files specified in the content of the document (images etc.) can be located.  |
| <a href='tags/meta.html' >Meta data</a>   | <code>&lt;meta&gt;</code> | A generalized informational tag that can define information about the final document production, its owners or security settings for use.  |
| <a href='tags/link.html' >Linked files</a>   | <code>&lt;link&gt;</code> | References an external file that contains resources (specifically styles) that the document should use when generating the output.  |
| <a href='tags/styles.html' >Style content</a>   | <code>&lt;style&gt;</code> | Marks the document specific visual styles for the content that the document should use. Has a higher priority than any linked stylesheets.  |


---

## Extension Attributes


The library uses the <code>data-*</code> attributes to extend the use of existing elements to preserve validity of a html template and provide support for the library features.

| Attribute  | Use  | Description |
|---|---|---|
| <a href='tags/contfooter.html' >Continuation Footer *</a>   | <code>&lt;continuation&#8209;footer&gt;</code> | Begins a new content block for elements that will be shown at the bottom of every page of the document, within a <code>&lt;body&gt;</code> element **<u>except</u>** the first page.   |


