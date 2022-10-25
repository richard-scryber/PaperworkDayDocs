---
layout: default
title: Home
nav_order: 1
description: "Paperwork is a free tool to create beautiful PDF documents from html templates and formatted data."
permalink: /
---

# What is Paperwork?

Paperwork is a freely available tool, that allows you (as a designer, developer) to create beautiful and dymanic documents, quickly and easily on your site.

With templates based on `xhtml` and dynamic content from `json` data, generating and previewing the document directly on the page takes but moments.

It supports html tags, images, cascading styles, custom fonts, expressions and calculations within the templates, and complex json data.

## Creating a document preview - (PoJS)

We wanted to make it really easy to add paperwork to any site.

### Add a reference to the javascript.

The easiset was to create a document with Paperwork is to firstly, add a reference to the script file in your html head.

```html

    <script src='https://www.paperworkday.net/paperwork.min.js'  ></script>

```

### Add a container for the preview.

And a div with a specific id (or unique selector) where you would like the document to be shown in the the body of the page.

```html

    <section class='document'>
        <div id='helloworld_doc' style='width: 400px; height: 600px' ></div>
    </section>

```

### Add the code that creates the document.

And then finally once the page is loaded, initialize and load a document from the javascript event (in this case the window.onload event, but it could be a button click, or any other event).

{% raw %}
```javascript

    window.onload = function(evt){

        var html = "<html xmlns='http://www.w3.org/1999/xhtml' >" + 
            "<head><title>Hello world document</title>" +
            "<style> body { padding: 20px; } .title { color: calc(theme.color);} </style>" + 
            "</head>" + 
            "<body>" +
            "<h2 class='title' style='font-style: italic;' >{{greeting}}</h2>" + 
            "<p>{{concat('From all at ', author)}}</p></body>" + 
            "</html>";
        
        var values = { 
            greeting : "Hello World", 
            author : "the Paperwork Collective",
            theme: { color: "aqua"} 
        };

        paperwork.init({
            container: "#helloworld_doc",
            loaded: (result) => {
                paperwork.generate({
                    template: {content: template},
                    data: {content: values}
                });
            });
    }

```
{% endraw %}

### Viewing the result

And the output on the page should be the same as below.

Yes, this is a **real** live preview!


<div id='first-sample-container' class='document-container' data-pw-ui="Default" data-pw-template="_samples/helloworld/helloworld.html" data-pw-json="_samples/helloworld/helloworld.json"></div>

<p>&nbsp;</p>

## How does it work?

The technical version of how this works can be found <a href='/docs/framemechanism' >here</a>, but as a simple starter.

The div `helloworld_doc` has an iframe injected into the page via the `init` function, with our static site at https://www.paperworkday.net that is hosted on the cloud-flare cdn.

Once the page has `loaded` then the call back allows our code to `generate` a document by passing the data to to the frame from the template and the data provided, and this is presented in the frame using our open-source <a href='https://github.com/richard-scryber/scryber.core' >Scryber.Core</a> framework.

The template has `handlebar` syntax for reading the values from the provided data in the template, and performing calculations on that data. And the `calc` (or `var`) function can be used within the document styles.

In fact, if we were to change the data, then calling the `generate` function again will re-create the document with the new data in the frame!

> NOTE: All this is on the client browser. 
> There is no file transfer involved or server side document creation. 
> **Paperwork does not know anything about your data, it is just the tool**.

## Other frameworks and platforms

We really want to add support for react, angual, wordpress, blazor and many other tools. Just beacuse we can and it is easy. Please, watch this space or get in-touch to suggest.

## Minimum browser versions.

Because of the way paperwork does it's thing, browsers **must** support the messaging api, and browser web-assembly, along with basic javascript and frames. 

All the latest versions of the main browsers do support this, even on mobiles and tablets.

## Initialization and Generation options

There are many more options available within initialization, including 

1. Changing the display theme,
2. Supporting multiple frame instances on a single page
3. Altering interface functions such as full screen and download
4. Allowing viewing and editing of the code
5. Frame sizing and resizing.
6. Callback functions and error handling.

Read more about the <a href='/docs/initconfig' >init configuration</a>.

In the same way there are more options for the document generation, including

1. Loading either or both template and data from a url.
2. Getting the final generated data.
3. Error handling and logging.

Read more about the <a href='/docs/genconfig' >generate configuration</a>.


## Avoid iframes

Sometimes an iframe is either not appropriate, or cannot be used. In this case we have added a simple wrapper to our frame at <a href='https://www.paperworkday.net/preview?builder=true'>https://www.paperworkday.net/preview</a> 
that will allow you to build full links to the same capability outside of your site content, and even has a handy url builder.

## Still interested

We are really glad to see that you are still interested.

Some links we thing you would like to read are...

 - <a href='/docs/framemechanism' >How paperwork works</a>
 - <a href='/docs/initconfig' >The initialization configuration</a>
 - <a href='/docs/genconfig' >The generation configuration</a>
