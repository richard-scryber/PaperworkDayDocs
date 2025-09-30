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

The library is strongly typed and expects specific types to be set on a value of an attribute. These can be explicity set within a template content, or created dynamically at generation time. Some attributes however are explicitly static only, or explicitly binding only - as the required type is not convertable. These are marked in tables below, with one of **Any** or **Binding Only** or **Static Only**.


## Global Attributes

The following attributes are supported on all visual elements - the elements that are within the body element, including the body element itself.

| Attribute  | Use | Bindable  | Description |
|---|---|---|--|
| <a href='global/id.html' >id</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/title.html' >title</a>   | *All* | Any | By default adds an entry into the document outline structure with the attribute text value to support navigation to the element. **NOTE**: See the data extension attributes below as some elements override this default behaviour.   |
| <a href='global/style.html' >style</a>   | *All* | Any | Allows a full definition of the visual appearance of the element. Styles and classes are discussed in their own sections as part of <a href='/styling_content.html'>Styling Content</a> and a full reference section on <a href='/reference/cssproperties/'>CSS properties</a>    |
| <a href='global/class.html' >class</a>   | *All* | Any | Specifies a set of style class names as <a href='/reference/cssselectors/'>CSS selectors</a> to apply to the element.   |
| <a href='global/hidden.html' >hidden</a>   | *All* | Any | Indicates if this content should be displayed or not. As an xhtml template the value of the attribute should also be 'hidden' e.g. hidden='hidden'.  |
| <a href='global/name.html' >name</a>   | *All* | Any | Defines an explicit name for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-content.html' >data-content</a>   | *All* | *Binding Only* | Allows the dynamic binding of more visual content into the template at generation time from the documents data. More infomation on data binding can be found in the <a href='/learning/' >Learning section</a>   |
| <a href='global/data-content-action.html' >data-content-action</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-content-type.html' >data-content-type</a>   | *All* | Any | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |
| <a href='global/data-style-identifier.html' >data-style-identifier</a>   | *All* | *Static Only* | Defines an identifier for the element it is contained in, that can be used to refer to elsewhere in the template.   |

---

## Global Event Attributes


The following event attributes are supported on all visual elements. For more information on document controllers and event handling see the <a href='/learning/binding/codebehind.html'>code behind</a> learning article

| Attribute  | Use | Bindable  | Description |
|---|---|---|---|
| <a href='events/init.html' >on-init</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller when the element is initialized.   |
| <a href='events/loaded.html' >on-loaded</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller when the element is loaded.   |
| <a href='events/binding.html' >on-databinding</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller before the element is data bound.   |
| <a href='events/bound.html' >on-databound</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller after the element is databound.   |
| <a href='events/prelayout.html' >on-prelayout</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller before the element is laid out.   |
| <a href='events/postlayout.html' >on-postlayout</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller after the element is laid out.   |
| <a href='events/prerender.html' >on-prerender</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller before the element is rendered.   |
| <a href='event/postrender.html' >on-postrender</a>   | *All* | Static Only | An event that is raised to a declared method on the defined controller after the element is rendered.   |

---

## Supported Standard Attributes


The library supports the use of the following standard attributes that match existing attributes on html elements.

| Attribute  | Use | Bindable  | Description |
|---|---|---|---|
| <a href='standard/align.html' >align</a>   | <code>img</code> | Any | Defines the alignment on a line for an image when it is laid out.   |
| <a href='standard/alt.html' >alt</a>   | <code>img</code>, <code>object</code> | Any | An alternative name for the element. *Not currently used, but defined*  |
| <a href='standard/charset.html' >charset</a>   | <code>&lt;meta&gt;</code> | Any | The character set for the meta data information. *Not currently used, but defined*  |
| <a href='standard/cite.html' >cite</a>   | <code>&lt;ins&gt;</code>, <code>&lt;del&gt;</code> | Any | The citation information for the inserter or deleter of the section. *Not currently used, but defined*  |
| <a href='standard/colspan.html' >colspan</a>   | <code>&lt;td&gt;</code> | Any |  Defines the number of columns across, a cell occupies including the current column.  |
| <a href='standard/content.html' >content</a>   | <code>&lt;meta&gt;</code> | Any | Set the actual content value of a named meta-data element so that it can be used in document processing.  |\
| <a href='standard/data.html' >data</a>   | <code>&lt;object&gt;</code> | Any | Sets the source file path to a specific location (using any document base path) so the attachment can be loaded and included.  |
| <a href='standard/datetime.html' >datetime</a>   | <code>&lt;ins&gt;</code>, <code>&lt;del&gt;</code>, <code>&lt;time&gt;</code> | Any | In the case of ins and del, specifies the timestamp for the modification. For a time element, specifies the date and/or time that should be displayed by the element.  |
| <a href='standard/for.html' >for</a>   | <code>&lt;label&gt;</code>, <code>&lt;output&gt;</code>, <code>&lt;page&gt;</code> | Any | Identifies the id of the referenced element this element is referring to. For a page element, this with then be the page number of that referenced element.  |
| <a href='standard/height.html' >height</a>   | <code>&lt;img&gt;</code> | Any | A legacy support attribute for the image element to explicitly set the pixel height for rendering. Use the CSS properties instead  |
| <a href='standard/high.html' >high</a>   | <code>&lt;meter&gt;</code> | Any | Defines the recommended high value for a graphical meter bar.  |
| <a href='standard/href.html' >href</a>   | <code>&lt;a&gt;</code>, <code>&lt;link&gt;</code> | Any | Sets the source file path to a specific location (using any document base path) so an image or external resource can be loaded and included.  |
| <a href='standard/http-equiv.html' >http-equiv</a>   | <code>&lt;meta&gt;</code> | Any | Defines a pragme directive for the template. *Not currently used, but defined*  |
| <a href='standard/lang.html' >lang</a>   | <code>&lt;html&gt;</code> | Any | Specifies the default output culture (e.g. en-US or fr-FR) for the resultant document. This impacts features such as number conversion and date conversion to rendered strings.  |
| <a href='standard/low.html' >low</a>   | <code>&lt;meter&gt;</code> | Any | Defines the recommended low value for a graphical meter bar.  |
| <a href='standard/max.html' >max</a>   | <code>&lt;meter&gt;</code>, <code>&lt;progress&gt;</code>  | Any | Defines the maximum value for a graphical meter or progress bar - based on this value the offset of the bar will be calculated.  |
| <a href='standard/media.html' >media</a>   | <code>&lt;source&gt;</code>, <code>&lt;style&gt;</code>  | Any | Specifies the mime type of the picture source or a media query the style is appropriate to be used for.  |
| <a href='standard/min.html' >min</a>   | <code>&lt;meter&gt;</code>  | Any | Defines the minimum value for a graphical meter - based on this value the offset of the bar will be calculated.  |
| <a href='standard/open.html' >open</a>   | <code>&lt;details&gt;</code> | Any | Used to define if a details section will show all content, or just the summary.  |
| <a href='standard/optimum.html' >min</a>   | <code>&lt;meter&gt;</code>  | Any | Defines the optimum value for a graphical meter.  |
| <a href='standard/property.html' >property</a>   | <code>&lt;page&gt;</code>  | Any | Specifies the type of page number that should be looked up and used, e.g. 'total', or 'section' page number or 'sectiontotal' number.  |
| <a href='standard/rel.html' >rel</a>   | <code>&lt;link&gt;</code>  | Any | Specifies the relationship of the linked source to the current source. **NOTE** anything other than 'stylesheet' will currently be ignored.  |
| <a href='standard/rowspan.html' >rowspan</a>   | <code>&lt;td&gt;</code>  | Any | Defines the number of rows down, a cell occupies including the current row.  |
| <a href='standard/scope.html' >scope</a>   | <code>&lt;th&gt;</code>  | Any | Defines whether a header cell is a header for a column, row, or group of columns or rows. Has no effect on output.  |
| <a href='standard/src.html' >src</a>   | <code>&lt;embed&gt;</code>, <code>&lt;frame&gt;</code>,<code>&lt;source&gt;</code>, <code>&lt;img&gt;</code>  | Any | Defines the external location of a resource (taking into account the document base path) that the element will use.  |
| <a href='standard/srcset.html' >srcset</a>   | <code>&lt;source&gt;</code>  | Any | Defines the external location of a range of resource (taking into account the document base path) that the element *can* use.  |
| <a href='standard/target.html' >target</a>   | <code>&lt;a&gt;</code>  | Any | Sets the location within the consuming application where the linked content should be shown. *Support is based on the reader applications implementation*  |
| <a href='standard/type.html' >type</a>   | <code>&lt;frame&gt;</code>, <code>&lt;source&gt;</code>, <code>&lt;style&gt;</code> <code>&lt;object&gt;</code>  | Any | Identifies the content mime type of a resource at an external location (taking into account the document base path).  |
| <a href='standard/value.html' >value</a>   | <code>&lt;progress&gt;</code>  | Any | Defines the actual value for a graphical progress bar - based on this value the offset of the bar will be calculated using max  |
| <a href='standard/width.html' >width</a>   | <code>&lt;img&gt;</code> | Any | A legacy support attribute for the image element to explicitly set the pixel width for rendering. Use the CSS properties instead  |

---

## Extension Attributes


The library uses the <code>data-*</code> attributes to extend the use of existing elements to preserve validity of a html template and provide support for the library features.

| Attribute  | Use | Bindable  | Description |
|---|---|---|---|
| <a href='tags/data-bind.html' >data-bind</a>   | <code>&lt;template&gt;</code> | *Bindable Only* | Allows the dynamic binding of more visual content, **multiple times**, from within the template into the documents' layout, based on the data received from the data-bind value. More infomation on data binding can be found in the <a href='/learning/' >Learning section</a>  |
| <a href='tags/data-bind-max.html' >data-bind-max</a>   | <code>&lt;template&gt;</code> | Any | Limits the dynamic binding of visual content, to a **maximum** number of items. More infomation on data binding can be found in the <a href='/learning/' >Learning section</a>  |
| <a href='tags/data-bind-start.html' >data-bind-start</a>   | <code>&lt;template&gt;</code> | Any | Sets the start of the dynamic binding of more visual content, from within the template into the documents' layout, with zero being the first itteration. More infomation on data binding can be found in the <a href='/learning/' >Learning section</a>  |
| <a href='tags/data-bind-start.html' >data-bind-step</a>   | <code>&lt;template&gt;</code> | Any | Sets the loop over count of the dynamic binding data before any entry is added to the document's layout. More infomation on data binding can be found in the <a href='/learning/' >Learning section</a>  |


