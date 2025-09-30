---
layout: default
title: How Paperwork works
parent: With the viewer
parent_url: /viewer/
nav_order: 5
has_children: true
---

# How Paperwork works
{: .no_toc }

When generating a document in a frame, there are a number of actions the framework performs.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Process Flow

![](https://www.paperworkday.info/assets/ProcessSlide.png)


{: .note }
> All generation and rendering are performed on the client.
> Only remote requests are made for files within the template across the network e.g images, fonts, stylesheets.

---
## Loading the frame

The first stage of initialization will set up the library, and then inject a wrapping div and an iFrame into the current document, within the container specified, and an iframe source of 'https://www.paperworkday.net/(version)/generate'. 
The init options will be passed on the url parameters so the library can initialize the content of the frame as required.

A reference to this frame, along with it's name and whether it is 'running' is stored in the library.

{% raw %}
```html

    <div id='doc-container'>
        <!-- This content is injected by the library given the container #doc-container -->
        <div id='provided name or default' >
            <iframe src='https://www.paperworkday.net/v1_0/generate?....' style='width and height etc.' ></iframe>
        </div>
    </div>

```
{% endraw %}

---

## WASM and Blazor

The paperworkday.net site is a single page application that loads a number of Blazor .net (6.0) web assemblies into the browser context. This allows the frame to dynamically load and generate documents with fonts, images and graphics on the site without needing a server to generate.

Once the page is fully loaded then a message is sent back to the calling frame content via the window messaging API.

*By using this api the frame does not have to come from the same domain as the hosting frame, and messages are secure and client side only*

---

## Generating content 

With the frame fully loaded, the paperwork script can `generate` a document by passing the content again via the messaging api, to the waiting Blazor application. 
This application will decode the message, and interpret the generate request, loading any remote files as needed.

403 redirects are generally ignored, but content can be obtained from any service the current user has direct access to. If they are already authenticated onto a site, then the content can be retrieved.

{: .note }
> Paperwork must be the in the root of the page, for security reasons we do not support the library being within a frame.
> So nested frames within frames cannot be used to pull content.

Once generated then the preview will be rendered using the pdf.js library into a canvas on the frame at the requested page.

---

## Retrieving content

Once the document has been generated, the Blazor application holds a reference the the binary data for the generated document.

To retrieve this again the messaging api is used and the data encoded and transferred across the boundary. If the document is very large, or has large images or fonts within it, then it may fail or cause poor performance.

---

## Multiple instances

Each container will have an iframe attached to it. That iframe will have an instance of the blazor application. The generated document is presented with a PDF worker process building the representation.

If there are a lot of frames on the page, or many re-generations of a document within a single frame, then memory performance may become an issue. We have not experienced any problems with hundreds of generations, but be aware!
