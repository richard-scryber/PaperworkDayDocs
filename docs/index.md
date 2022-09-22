# What is Paperwork?

Paperwork is a freely available tool, that allows you (as a designer, developer) to create beautiful and dymanic documents, quickly and easily on your site.

The templates are based on xhtml and you can add dynamic content from json data, generating and previewing the document directly on the page.

It supports html tags, images, cascading styles, expressions and calculations within the templates and complex json data.

## Creating a document preview - with Plain old Javascript


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
            "<h2 class='title' style='font-style: italic;' >{{content.greeting}}</h2>" + 
            "<p>{{concat('From all at ', content.author)}}</p></body>" + 
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


<div id='first-sample-container' class='document-container' data-pw-ui="Default" data-pw-template="_samples/helloworld/helloworld.html" data-pw-json="_samples/helloworld/helloworld.json"></div>
