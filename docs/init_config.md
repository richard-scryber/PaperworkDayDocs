# Initialization Options

When initializing the container to show documents, there are a number of options that can be provided, and events that may be raised.

## As a minimum

The minimum configuration options for initializing paperwork is the name of the container where the paperwork tool will be shown.

{% raw %}
```javascript

    paperwork.init({ container: "#paperwork"});

```
{% endraw %}

This will create an initialize a new iframe, add it to a wrapping div and then append it to the container with id 'paperwork'.

If the container is not provided, or cannot be found then an error will be raised in the console and false returned from the `init` function.

## More options

More options can be provided to change the appearance and behaviour as below.

<dl>
  <dt>container</dt>
  <dd>This is the required selector for an existing element within the page that the frame sho</dd>
  <dt>name</dt>
  <dd>This optional <code>string</code> is the identifying name of the wrapper and frame. It allows multiple paperwork frame instances on a single page, and supports the mechanism for calling each individually from within your code at any point.</dd>
  <dt>ui</dt>
  <dd>This optional set of flags define the functional user interface elements that will be shown on the client when initialized, and or a document is generated. </dd>
  <dt>width</dt>
  <dd>This optional css unit of size string, will set the starting <i>width</i> of the frame (and or wrapper)</dd>
  <dt>height</dt>
  <dd>This optional css unit of size string, will set the starting <i>height</i> of the frame (and or wrapper)</dd>
  <dt>scale</dt>
  <dd>This optional numeric value will set the <u>initial</u> percentage scale of the preview when a document is first generated. If the end user alters the scale, then this be honoured, and will not be reset by paperwork, on subsequent generations.<br/> Supported values are 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0</dd>
  <dt>page</dt>
  <dd>This optional numeric value, will set the starting page number within the document. The first page is 1. If the page does not exist then the closest page to that number will be shown.</dd>
  <dt>vers</dt>
  <dd>This version string, is recommended for production environments, but not required. It will specifiy the framework version to use for generation. Currently there are only 2 values supported: '1.0' or 'latest'. It is expected that in future further values will be supported, and these versions may not support your template - hence the recommentation.</dd>
</dl>

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

## The UI flags

FullScreen=1,
Download = 2,
Paging = 4,
Code = 8,
Zoom = 16,
Resize = 64,
Edit = 128,

Default is equivalent FullScreen + Download + Paging + Zoom
