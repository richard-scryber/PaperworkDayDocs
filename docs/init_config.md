---
layout: default
title: Init Options
parent: Getting Started
nav_order: 1
---

# Initialization Options
{: .no_toc }

When initializing the container to show documents, there are a number of options that can be provided, and events that may be raised.

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

The minimum configuration options for initializing paperwork is the name of the container where the paperwork tool will be shown.

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork"});

```
{% endraw %}

This will create an initialize a new iframe, add it to a wrapping div and then append it to the container with id 'paperwork'.

If the container is not provided, or cannot be found then an error will be raised in the console and false returned from the `init` function.

---

## All options

More options can be provided to change the appearance and behaviour as below.

<dl>
    <dt>container</dt>
    <dd>This is the <strong>required</strong> selector for an existing element within the page that the frame should be shown in</dd>
    <dt>name</dt>
    <dd>This optional string is the identifying name of the wrapper and frame. It allows multiple paperwork frame instances on a single page.</dd>
    <dt>vers</dt>
    <dd>This version string, is <strong>recommended</strong> for production environments, but not required.</dd>
    <dt>ui</dt>
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

---

## Full Example

A complete set of options for the initialization would be as follows...

{% raw %}
```javascript

    //Initialize the container
    paperwork.init({
        container: "#helloworld_doc",
        name: "fullInit",
        vers: "latest",
        width: "400px",
        height: "600px",
        theme: "light",
        ui: "FullScreen, Paging, Zoom", //no download, resizing or editing
        scale: 2.0,
        page: 3,
        loaded: (result) => {

            //Once loaded, then do anything you want, including
            //generate the document with a template and any current data
            //using the name of the frame.

            paperwork.generate({
                name: "fullInit",
                template: {source: url}
            });
        }
    });

```
{% endraw %}

---

## The name identifier

By providing names, then more than one frame instance is supported by Paperwork on the current page. Each named frame must still be initialized, and can then be referred to individually for other actions.

If a name is not provided then it will be given a default name. And any secondary initialization will fail if a name is not provided.


{% raw %}
```javascript


    paperwork.init({ container: "#paperwork1", name : "first"});
    paperwork.init({ container: "#paperwork1", name : "second"});

    .
    .
    .

    paperwork.gen({name: "second", template:{content: html}, data: {content: values} });

    .
    .
    .

    paperwork.retrieve({name: "second"});


```
{% endraw %}

---

## The UI flags

The UI options can either be provided as an array or as a comma separated string of values. Each value will show a particular user interface (ui) component as follows.

<dl>
    <dt>FullScreen</dt>
    <dd>If included in the set of flags, then the full screen toggle icon will be shown to allow the user to enter full screen mode with the frame content. By pressing escape, the end user will return the frame back to the last size. Normally this icon will be on the top far right corner.</dd>
    <dt>Download</dt>
    <dd>If included in the set of flags then the download document icon will be shown (disabled unless a document has been generated), to allow the user to easily download a single full copy of the current document. </dd>
    <dt>Paging</dt>
    <dd>If included in the set of flags then the next, previous icons and current page will be shown, (disabled unless a document has been generated), to allow the user to easily move between pages in the current document.</dd>
    <dt>Zoom</dt>
    <dd>If included in the set of flags then the zoom-in, zoom-out icons and current zoom percentate will be shown, (disabled unless a document has been generated), to allow the user to easily increases the displayed size of the documents' current page frame.</dd>
    <dt>Resize</dt>
    <dd>If included in the set of flags then the initialized frame will be identified as resizable to the browser. Provided this is supported based upon parent elements and browser version, then the current user should be able to change the size and or aspect ration of the previewing frame.</dd>
    <dt>Code</dt>
    <dd>If included in the set of flags then the code (template and data) that was used to generate any document and preview can be viewed, even if it was loaded from a url rather than directly provided. This does not affect the original source, but can be very useful in checking template and data sources.</dd>
    <dt>Edit</dt>
    <dd>If included in the set of flags then the code (template and data) that was used to generate any document and preview can be <strong>EDITED</strong></dd>
</dl>

If, for some reason, none of the above interface elements are wanted, then the `None` option can be explicitly provided.

### Default components and the Default flag.

Along with the flags above another value of `Default` is supported. This is also the value that is used if the `ui` option is not specified on the initialization options.

Default will currently show `FullScreen, Download, Paging, Zoom` ui options.

If another flag is added to the ui set, and is deemed a standard interface element, the it will be included in `Default`. As a designer / developer it is realy up to you, to be explicit or implicit in the specfication of the UI elements. 

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork1", name : "simple", ui : "Default, Resize"});
    paperwork.init({ container: "#paperwork2", name : "editable", ui : "Default, Resize"});
    paperwork.init({ container: "#paperwork3", name : "none", ui : "None"});
    
```
{% endraw %}

Currently it is not possible to update / change the UI elements after initialization. An instance can only be `release`d by name, and then re-initialized.
Releasing will remove the frame from the page.

{% raw %}
```javascript

    paperwork.release({name : "simple"});
    paperwork.init({ container: "#paperwork1", name : "simple2", ui : "Default, Resize, Code, Edit", theme: "light"});
    
```
{% endraw %}

_Passing '*' to release will remove **ALL** instances_

---

### Code viewing and editing

By specifying the `Code` flag on the `ui` it is possible to view the data and template that was used to generate any document.

By also specifying the `Edit`flag, then it is possible to not only view the code, but also change it. Any changes will not be saved back to the original source, but it is useful to test and validate.

---

## Width and Height of the frame.

If width and height are not specified on the initialization options, then both the wrapper and the frame will be set to 100% size. This allows you as the designer or developer to control the height via the specified container.

If more control is needed, then simply specifying an explicit size will be applied to the frame.

{% raw %}
```javascript


    paperwork.init({ container: "#paperwork1", name : "fixed", ui : "Default", width: "100%", height: "600px" });
    paperwork.init({ container: "#paperwork1", name : "stretch", ui : "Default, Resize", width: "400px", height: "600px"});
    
```
{% endraw %}

---

## Zoom (Scale) of the document page.

During the initialization of the frame a first percentage scale for the displayed page can be specified. THis allows the standard value to be set, based upon the explict or expected viewport size vs the expected document page size. Ultimately the consuming end user has full control of the zoom level.

The following values are supported

- 0.25, equivalent to 25%
- 0.5,
- 0.75,
- 1.0, the default 100% value if not provided,
- 1.5,
- 2.0,
- 4.0,
- 8.0, equivalent to 800%

Currently, if a value outside of these numbers is provided for scale it will be ignored.

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork1", name : "small", ui : "Default", scale: "0.5" });
    
```
{% endraw %}

---

## Starting page index.

During the initialization of the frame the one-based first page index for the displayed page can be specified. This allows the standard values to be set of the page the consuming end user will see, but they will have full control of the current page (if the UI controls allow paging).

The first page in the document is alway 1, and if a value is provided e.g. 10 that falls beyond the range of the documents number of pages, then the last (or first) page in the document will be shown.

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork1", name : "second-page", ui : "Default", page: "2" });
    
```
{% endraw %}

---

## Versioning of the generation.

The 'vers' number used to intialize the frame will specifiy the Paperwork framework version to use for generation. 

Currently there are only 2 values supported: '1.0' or 'latest'. It is expected that in future further values will be supported, and these versions may not support your template - hence it is recommended to use it in all production environments.

By specifying `latest` then a client will always be using the most recent **released** version of the framework. 

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork1", name : "explicit-version", ui : "Default", vers: "1.0" });
    
```
{% endraw %}

---

## Loaded Event

There is only 1 event raised from the init method and that is the loaded event. A provided function will be called once the inner content is ready in the browser. 

Because the init method will set the source of a frame to remote content, the secondary generation method cannot be called as soon as init returns, so loaded is a good convenience method to use to explicity generate content, or enable any client interface to interact with the frame.

The loaded option method will be called with the same object as the init method returns. A single object instance with the name given to the frame, and whether it is currently running or not.

{% raw %}
```javascript

    //Initialize the container
    paperwork.init({
        container: "#helloworld_doc",
        loaded: (result) => {
            //Once loaded, then generate the document with a template and any current data
            paperwork.generate({
                template: {content: html},
                data: {content: values}
            });
        }
    });

```
{% endraw %}

---

Once all the init options are set correctly, it makes sense to move onto the <a href='gen_config' >generation options</a>