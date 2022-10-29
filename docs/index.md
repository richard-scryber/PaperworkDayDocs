# What is Paperwork?

Paperwork is a freely available tool, that allows you (as a designer, developer) to create beautiful and dymanic documents, quickly and easily on your site.

With templates based on `xhtml` and dynamic content from `json` data, generating and previewing the document directly on the page takes but moments.

It supports html tags, images, tables, cascading styles, custom fonts and repeating elements within the templates, along with complex json data, expressions, calculations and selecting.

## Creating a document with preview

We want to make it really easy to add paperwork to any site so you can create dynamic documents.

<div id='first-sample-container' class='document-container' data-pw-ui="Default, Code, Edit" data-pw-template="_samples/helloworld/helloworld.html" data-pw-json="_samples/helloworld/helloworld.json"></div>

<p>&nbsp;</p>

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

    //The content of the template as xhtml (or use a url)
    var html = "<html xmlns='http://www.w3.org/1999/xhtml' >" + 
            "<head><title>Hello world document</title>" +
            //Using the data in css styles with var (or calc)
            "<style> body { padding: 20px; } .title { background-color: var(theme.color);} </style>" + 
            "</head>" + 
            "<body>" +
            //Binding the data using {{}} (or calculating new values)
            "<h2 class='title' style='font-style: italic; padding: 30px' >{{greeting}}</h2>" + 
            "<p>{{concat('From all at ', author)}}</p></body>" + 
            "</html>";

    //The data to use in the template
    var values = { 
            greeting : "Hello World", 
            author : "the Paperwork Collective",
            theme: { color: "silver"} 
    };

    window.onload = function(evt){
        //Initialize the container
        paperwork.init({
            container: "#helloworld_doc",
            //Add some optional flags for user interface options
            ui: [Default, Code, Edit],
            loaded: (result) => {
                //And once loaded, then generate the document with the template and the current data
                paperwork.generate({
                    template: {content: html},
                    data: {content: values}
                });
            });
    }

```
{% endraw %}

See <a href='/docs/framemechanism' >how paperwork works</a> for a deeper dive into how Paperwork genersates your document.

If you want to avoid the inclusion of iframes in your own site take a look at <a href='https://www.paperworkday.net/preview?builder=true'>https://www.paperworkday.net/preview</a> 
that will allow you to build full links to the same capability outside of your site content, and even has a handy url builder.

{: .note-title }
> Remember
> All this is on the client browser. 
> There is no network file transfer involved or server side document creation. 
>
> **Paperwork does not know anything about your template data, it is just the tool**.


## Minimum browser versions.

Because of the way paperwork does it's thing, browsers **must** support the *messaging api*, and *browser web-assembly*, along with basic javascript and frames. 

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
4. White and black listing remote domains

Read more about the <a href='/docs/genconfig' >generate configuration</a>.

## Supported content

The core framework does **not** support all html tags or css style rules (and some may perform differently that you expect), so please see the following pages for more information.

- Html content
- Colors, sizes, columns and alignment
- Cascading styles
- Expressions and calculaions
- Images, types and inline support
- Remote content and imports
- Drawing shapes and svg
- Logging and output options.

## Want more?

We offer a subscription service that offers the following features.

- Document retrieval in your own code to do with the document anything you need.
- Custom css on the frame UI so it can be branded as your own site.
- Security options for restricting printing copying etc. And also password protecting your file.

## Samples

Or just refer to  <a href='/docs/genconfig' >here</a> for our list of samples and templates you can freely use for your own purposes.



