---
layout: default
title: Quick Start
nav_order: 1
has_toc: false
---


# Scyber Quick Start

Follow along if you want to understand some of the key features and benefits of the Scryber.Core library. Here we add the package and build out a data template with dynamic styling and some repeating content. Based on your knowledge level you may then want to dive straight into your own use-cases to complete, or review the reference section to understand supported features.

---

## Adding Scryber.Core

Whilst Scryber is open source and the code can be downloaded and built locally, the easiest way is to add the nuget package to a new or existing project. Consult your own IDE documentation if you are not sure how to do this, or add the package from the command line in the project folder.

```
dotnet add package Scryber.Core
```

The package is located at [https://www.nuget.org/packages/Scryber.Core](https://www.nuget.org/packages/Scryber.Core)

If you are focussed on MVC or Web development, then you can use the Scryber.Code.Mvc package, the adds helpers and extra support for sending PDF's as responses to requests, and other capabilites. It also includes a reference to the matching Scryber.Core package.

```
dotnet add package Scryber.Core.Mvc
```

The package is located at [https://www.nuget.org/packages/Scryber.Core.Mvc](https://www.nuget.org/packages/Scryber.Core.Mvc)

---

## Create a template file

The first thing we can do is add a simple html template file (the ubiquitous Hello World) as a starter and call the file 'Hello.html'.

#### Hello.html
```handlebars
{% raw %}<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
    <!-- Give it a title -->
    <title>Hello {{user.firstName ?? "World"}}</title>
</head>
<!-- dynamic styling -->
<body>
    <!-- A heading title -->
    <h1>Hello, {{user.firstName ?? "World"}}</h1>

    <!-- custom style support -->
    <p class='intro'>
      This is {{(user.firstName + "'s") ?? "my"}} first dynamic PDF generated with Scryber.Core.
    </p>
</body>
</html>{% endraw %}
```

Save the file, and we can generate our first PDF.

{: .note }
> Scyber will accept streams, text readers and xml readers so you can load from many different sources (or resources), but for this example it  makes sense to use a file (it doesn't even need to have the '.html' extension, use '.config', and it will never be sent over a web server).

---


## Generate our first template


At an approprite location within your code, either responding to an event firing, or web request add the following

#### PDF Generation
```csharp
        //using Scryber.Components

        var input = "hello.html"; //Load the HTML template from a file (or open stream, or text reader)
        using var doc = Document.ParseDocument(input); //read the template

        using var output = new FileStream("hello.pdf", FileMode.Create); //create the stream to write to.
        doc.SaveAsPDF(stream); //write the pdf file.

```

---

## Viewing the result

The resultant file should now be able to be opened in any PDF Viewer application or browser, and should look like this.

![Hello World Preview](../assets/sampleImages/HelloWorld1.png)

---

## Making it dynamic

In the original template you may have noticed a few `{% raw %}{{handlebar}}{% endraw %}` expressions such as `{% raw %}{{user.firstName ?? "World"}}{% endraw %}` within the template. Scryber is using these to evaluate at runtime values provided to the document instance. The `??` is a [Null Coalescing](reference/binding/operators/nullcoalesce) operator that will provide the second value `"World"` if the first - the `user.firstName` object property reference - is null. 

With scryber we can now easily provide the dynamic data to the document using its `Params` property.


#### Add our user
```csharp
        var input = "hello.html";
        using var doc = Document.ParseDocument(input);

        //set the user to an instance (or JSON) value
        doc.Params["user"] = new { firstName = "John", lastName = "Smith" };

        using var output = new FileStream("hello.pdf", FileMode.Create);
        doc.SaveAsPDF(stream);

```

---

## Checking the result

If we generate again, our World should now be John, and I know he appreicates that!

![Hello John Preview](../assets/sampleImages/HelloWorld2.png)

---

## Getting into the power

This is a very simple example, as all Hello Worlds should be, but we can easily take it to a new level with the same template.

If our data model is expanded to include some personal information, and a collection of friends. And we want to 


```csharp
        //using Scryber.Components

        // Load the HTML template from a file, or stream, or text reader
        var doc = Document.ParseDocument("hello.html");

        // Add your data.
        doc.Params["user"] = new
        {
            firstName = "John", lastName = "Smith", 
            sightImpared = true,
            friends = new [] {
             new { firstName = "Bill", lastName = "Jones", stillFriends = true, },
             new { firstName = "Sarah", lastName = "Jones", stillFriends = true, },
             new { firstName = "James", lastName = "Long", stillFriends = true, },
             new { firstName = "Sam", lastName = "Elsewhere", stillFriends = false, }
             }
            
        };

        doc.Params["brand"] = new { color = "rgb(0, 168, 161)", 
                            lightColor = "rgb(144, 227, 223)",
                              logo = "https://www.paperworkday.info/assets/PaperworkTransparent.svg",
                              strapLine = "<span>We make documents <b><i>much</i> easier</b> for you</span>"
                              }

        // Generate the PDF to a file, a stream or a response.
        using (var stream = new FileStream("hello.pdf", FileMode.Create))
        {
            doc.SaveAsPDF(stream);
        }
```

#### hello.html
```handlebars
{% raw %}<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
    <!-- Bind some meta-data -->
    <title>Hello {{user.firstName ?? "World"}}</title>

    <!-- Add relative (or remote) CSS for styles -->
    <link rel="stylesheet" href="hello_styles.css" type="text/css" />

    <!-- Add some remote fonts from google -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&amp;display=swap" rel="stylesheet" />

    <!-- Some icons from font-awesome -->
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.5.0/css/all.css' />
    <style>

      /* use custom fonts */
      body { 
        font-family: 'Roboto', Helvetica, sans-serif;
        margins: 20pt 15pt 20pt 30pt;
      }
      /* dynamic styles */
      body > .logo { 
        color: var(--brand-color); 
        background-color: var(--brand-color-light); 
        padding: 2rem; 
        text-align: center;
      }
    </style>

</head>
<!-- dynamic styling -->
<body class='{{if(user.sightImpared,"accessible","normal")}}'>

    <div class='logo' >
        <!-- dynamic remote file loading -->
        <img src='{{brand.logoUrl}}'/>

        <!-- bound complex content with dynamic visibility -->
        <div class='strapline' data-content='{{brand.strapLine}}' data-type='text/html' hidden='{{if(length(brand.strapline) > 0, "", "hidden")}}'></div>
    </div>

    <!-- complex expression with function support -->
    <h1>Hello, {{concat(user.firstName, " ", user.lastName) ?? "World"}}!</h1>

    <!-- custom style support using a variable, but can also be a bound expression -->
    <p class='intro' style='border-top: solid 1px var(--brand-color);'>
      This is {{(user.firstName + "'s") ?? "my"}} first dynamic PDF generated with Scryber.Core.
    </p>


    <!--  dynamically store a calculated value of friends who are active -->
    <var data-id='activeFriends' data-value='{{selectWhere(user.friends, this.isActive == true)}}' />

    <!-- check if we have active friends -->
    {{#if count(activeFriends) > 0}}

        <!--  store the friends alphabetically last name and first name -->
        <var data-id='activeFriendsByName' data-value='{{sortBy(user.friends, this.lastName + " " + this.firstName)}}' />

        <!-- also going to keep a record of the first  -->
        <var data-id='rollingIndex' data-value='{{"0"}}' />

        <!-- aggregate functions on the collection of friends -->
        <h2>You have {{count(activeFriendsByName)}} friends:</h2>

        <!-- loop through each one, setting the current data -->
        {{#each activeFriendsByName}}

            <!-- check for the first letter. If it's not the same as the last, 
            then we can update the index and output content -->

            {{#if (rollingIndex != substring(this.lastName, 0, 1))}}
                <var data-id='rollingIndex' data-value='{{substring(this.lastName, 0, 1)}}' />
                <div class='friend-index-letter'>{{rollingIndex}}</div>
            {{/if}}

            <!-- Each friend has a card, with an icon, an index, and their name -->
            
            <div class='friend-card'>
                <div class='icon'><i class='far far-user'></i></div>
                <div class='details'>
                    <span class='index' >{{@index + 1}}</span>
                    <span class='name' >{{this.lastName + ", " + this.firstName}}</span>
                </div>
            </div>
        {{/each}}

    {{else}}
        <!-- finally a fallback if none -->
        <p class='muted'>You have no friends {{user.firstName}}, please try and get some!</p>
    {{/if}}

</body>
</html>{% endraw %}
```

#### hello_styles.css
```css

```

#### Updated parameters
```csharp

```

#### The result

---

## What's next


