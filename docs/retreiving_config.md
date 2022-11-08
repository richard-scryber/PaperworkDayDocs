---
layout: default
title: Retrieving the document
parent: Getting Started
nav_order: 4
---

# Retreiving a generated document
{: .no_toc }

Once a document has been generated in a frame, then the actual document data can be retrieved in code to be stored or other action taken.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Loading the frame

The first stage of initialization will set up the library, and then inject a wrapping div and an iFrame into the current document, within the container specified, and an iframe source of 'https://www.paperworkday.net/generate'. 
The init options will be passed on the url parameters so the library can initialize the content of the frame as required.

A reference to this frame, along with it's name and whether it is 'running' is stored in the library.

{% raw %}
```html

    <div id='doc-container'>
        <!-- This content is injected by the library given the container #doc-container -->
        <div id='provided name or default' >
            <iframe src='https://www.paperworday.net/generate?....' style='width and height' ></iframe>
        </div>
    </div>

```
{% endraw %}

---

## WASM and BLazor

The paperworkday.net site is a single page application that loads a number of Blazor .net web assemblies into the browser. This allows the frame to dynamically load and generate documents with fonts, images and graphics
dynamically on the site without needing a server to generate.

<dl>
    <dt>content</dt>
    <dd>This is a <strong>raw</strong> object or string of the actual values (JSON or XHTML)</dd>
    <dt>source</dt>
    <dd>This is a full URL to the content that should be loaded and used.</dd>
    <dt>type</dt>
    <dd>This is by default <code>Auto</code>, but supports also <code>Content</code> or <code>Location</code>. So if both properties are set, then the one to use can be specified.</dd>
</dl>

{% raw %}
```javascript

    function getTemplateObject(raw, link){

        var obj = {
            content = raw,
            source = link,
            type = (link ? "Location" : "Content")
        };

        return obj;
    }
    
```
{% endraw %}

{: .note }
> If both properties content and source are set, and the type is Auto (or not specified), 
> then the `content` will be used as a preference.

---

## Providing content 


{% raw %}
```javascript

    function generateMyDocument(){

        var html = getTemplateObject(null, "https://localhost/path/totemplate.html");

        var data = getTemplateObject({
            greeting: "Hello World", 
            when: Date.name().toLocaleString(),
        }, null);

        paperwork.generate({
            name: "myContainer", 
            template: html
            data: data
            });
    }
```
{% endraw %}

---

## When to generate.

Because the  <a href='init_config' >initialized frame</a> is loaded asyncronously, the generate method cannot be called immediately after the init function.

If you want to create a preview as soon as the frame is available, then the `loaded` event is available on the init configuration.

Alternatively the `generate` function can be called with a button click, or other user interface interaction on your page. 
This can be called multiple times on the same frame instance with different options.


{% raw %}
```html

    <div class='button-wrapper' >
        <button id='GenerateButton' onclick='generateMyDocument()'>Update Document</button>
    <div>
    
```
{% endraw %}

<input type='text' class='generateName' style='width: 400px' placeholder='Your Name' />

<button class="btn generateDoc">Create document on click</button>

<script>

var count = 0;

const generateDoc = document.querySelector('.generateDoc');
const generateName = document.querySelector('.generateName');

jtd.addEvent(generateDoc, 'click', function(){
  count++;
  var inputName = generateName.value;
  var source = "https://raw.githubusercontent.com/richard-scryber/PaperworkDayDocs/main/docs/_samples/nodata/buttonCounterIncrement.html"
  var data = { count: count, name: inputName ?? "None" };

  paperwork.generate({
    name: 'ButtonGenerate',
    template: {source: source},
    data: {content: data}
  });

});
</script>

<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='buttonGenerate' class='document-container' name='ButtonGenerate' data-pw-ui="Default, Code, Edit" ></div>

---