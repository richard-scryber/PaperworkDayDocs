---
layout: default
title: Retrieving the document
parent: Getting Started
nav_order: 4
---

# Retreiving a generated document
{: .no_toc }

Once a document has been generated in a frame, then the actual data can be retrieved in code to be stored or another action taken.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Post execution retrieval

With the <a href='gen_config.html' >Generate Options</a> a function can be provided that will be called on successful execution. Within that function it is possible to retrieve the data and process.

{% raw %}
```javascript

    function doGenerate(initilazedFrameName, dynamicData){

        paperwork.generate({
            name: initilazedFrameName,
            template: { source: 'link_to_template'},
            data: { content: dynamicData},
            success: function(result){
                retreiveAndDownloadBlob(initilazedFrameName);
            }
        });
    }

    function retreiveAndDownloadBlob(frameName){
        //This will download the file by creating  a blob url
        //and automatically clicking a link referencing the blob.

        paperwork.retreive({
            name: fameName, 
            format: 'blob',
            success: function (data) {
                //we have our blob
                const blobUrl = URL.createObjectURL(data);
                var link = document.createElement("a");
                link.href = blobUrl;
                link.download = (name || "PaperworkForms") + ".pdf";

                document.body.appendChild(link);
                link.dispatchEvent(
                    new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    })
                );
                document.body.removeChild(link);
            }
        });
    }

```
{% endraw %}

---

<button class="btn generateDoc">Create and Download</button>

<script>

var count = 0;

const generateDoc = document.querySelector('.generateDoc');


jtd.addEvent(generateDoc, 'click', function(){
  count++;
  var source = "https://raw.githubusercontent.com/richard-scryber/PaperworkDayDocs/main/docs/_samples/nodata/buttonDownload.html"
  var data = { count: count, name: "Just for download" };

  paperwork.generate({
    name: 'ButtonDownload',
    template: {source: source},
    data: {content: data},
    success: function(result) {
        retreiveAndDownloadBlob('ButtonDownload');
    }
  });

});

function retreiveAndDownloadBlob(frameName){
        //This will download the file by creating  a blob url
        //and automatically clicking a link referencing the blob.

        paperwork.retrieve({
            name: frameName, 
            format: 'blob',
            success: function (data) {
                //we have our blob
                const blobUrl = URL.createObjectURL(data);
                var link = document.createElement("a");
                link.href = blobUrl;
                link.download = (frameName || "PaperworkForms") + ".pdf";

                document.body.appendChild(link);
                link.dispatchEvent(
                    new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    })
                );
                document.body.removeChild(link);
            }
        });
    }

</script>

<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='buttonDownload' class='document-container' name='ButtonDownload' data-pw-ui="Default, Code, Edit" ></div>

---

## Retrieval options

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

## Available formats


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

## When to retreive.

---