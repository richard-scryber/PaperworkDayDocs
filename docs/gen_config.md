---
layout: default
title: Generate Options
parent: Getting Started
nav_order: 2
---

# Generation Options
{: .no_toc }

When generating a document in a frame, there are a number of options that can be provided, and events that may be raised.

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

The minimum configuration options for generating a document in paperwork is the template with either html, or a source where the html can be located.

{% raw %}
```javascript

    paperwork.generate({ template: { source: "https://mylocation.com/templates/first.html"}});

```
{% endraw %}

This will attempt to generate a new document from the source path, add render in the previously <a href='init_config' >initialized frame</a> with the default name. 

If the frame is not initialized, or cannot be found then an error will be raised in the console and false returned from the `generate` function.

A `data` object can also be provided to reference any dynamic content.

---

## Template and Data Objects

Within the template and data objects, there are 3 properties that can be set.

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

<input type='text' class='generateName' style='width: 400px' placeholder='Your Name' ></input>

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