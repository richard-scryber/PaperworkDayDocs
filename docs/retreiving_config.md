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
        retrieveAndDownloadBlob('ButtonDownload');
    }
  });

});

function retrieveAndDownloadBlob(frameName){
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
            },
            fail: function(message){
                alert("Could not download the data " + message);
            }
        });
    }

</script>

<!-- the frame will be initialzed by the code in the root default _layout -->
<div id='buttonDownload' class='document-container' name='ButtonDownload' data-pw-ui="Default, Code, Edit" ></div>

---

## Retrieval options

The options that can be provided to the `retreive` function are

<dl>
    <dt>name</dt>
    <dd>This is an optional value for the name of the frame to retreive the document for</dd>
    <dt>format</dt>
    <dd>This an optional enumeration for the way the document data is encoded in the call. Supported values are `blob`, 'array`, `base64`. If not provided then the default is `base64`</dd>
    <dt>success</dt>
    <dd>A function that will be called when the document has been successfully retreived with the data.</dd>
    <dt>fail</dt>
    <dd>A function that will be called when the document could not be retreived.</dd>
</dl>


{: .note }
> As the data is transfered across boundaries, the memory used is copied, 
> It is pure client side, but may cause bottleneck if the document is very large.

---

## When to retreive.

Retrieval can happen at any point once a document is created. 
An error will be raised (calling the fail function if defined), however, if there is a generation already happening or an existing retrieval in process.

This button will download any available document from the frame above without re-generating.


<button class="btn downloadDoc">Just Download</button>

<script>

var count = 0;

const downloadDoc = document.querySelector('.downloadDoc');

jtd.addEvent(downloadDoc, 'click', function(){
  retrieveAndDownloadBlob('ButtonDownload');
  });

</script>

---