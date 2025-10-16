---
layout: default
title: embed
parent: HTML Elements
parent_url: /reference/htmltags/
grand_parent: Template reference
grand_parent_url: /reference/
has_children: false
has_toc: false
---

# &lt;embed&gt; : The Embedded Content Element
{: .no_toc }

---

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{: toc}
</details>

---

## Summary

The `<embed>` element includes the content of an external local or remote file directly into the PDF document. The external file is loaded, parsed, and rendered as part of the current document, enabling modular document composition and content reuse.

---

## Usage

The `<embed>` element loads and includes external HTML or XML content into your PDF document. The content is fetched during document generation and becomes part of the document structure. This allows you to create reusable content fragments and build complex documents from multiple sources.

```html
<embed src="./templates/header.html" />
```

Remote content is also supported:

```html
<embed src="https://example.com/templates/footer.html" />
```

---

## Supported Attributes

- **src** - **Required**. The path or URL to the external content file to load and include
- **id** - Unique identifier for the element
- **class** - CSS class name(s) for styling
- **style** - Inline CSS styles
- **title** - Sets the outline/bookmark title for the embedded content
- **hidden** - Controls visibility. Set to `"hidden"` to hide the element

Standard CSS properties are supported: `width`, `height`, `margin`, `padding`, `border`, `background-color`, `display`, `position`, `float`, `opacity`.

---

## Data Binding

The embed element fully supports data binding for dynamic content sources and conditional inclusion.

### Basic Data Binding

Bind the source path dynamically:

```html
{% raw %}<embed src="{{model.templatePath}}" />{% endraw %}

```
### Complex Data Binding

As the content loaded by the embed element becomes a direct graph within the document tree, any data binding expressions within the loaded content will get full access to the current data context and can use this to add dynamic content within if.

**Main Document**

```html
{% raw %}<body>
    <template data-bind="{{report.sections}}">
        <div>
            <h2>{{.title}}</h2>
            <p>{{.content}}</p>
        </div>
    </template>

    <footer>
        <embed src='./footer.html'>
    </footer>
</body>{% endraw %}
```

**footer.html**
```html
{% raw %}<div>
    <!-- These values will be resolved dynamically base on the parent documents data -->
    <div class="{{report.theme ?? 'default'}}">
        <strong>{{report.title}}</strong> |
        Generated: {{report.date}} | page <page /> 
    </div>
</div>{% endraw %}
```


### Conditional Visibility

Show or hide embedded content based on data:

```html
{% raw %}<embed src="./sections/disclaimer.html"
       hidden="{{if(model.includeDisclaimer, '', 'hidden')}}" />{% endraw %}
```

### Dynamic Path Construction

Build paths dynamically from multiple data values:

```html
{% raw %}<embed src="{{'templates/' + model.language + '/' + model.section + '.html'}}" />{% raw %}
```

---

## Notes

- The embedded content is loaded and parsed at document generation time, not at viewing time
- Embedded content becomes part of the parent document's content tree
- External content can be HTML fragments or complete HTML documents
- Both local file paths and remote URLs (HTTP/HTTPS) are supported
- File paths are resolved relative to the current document or as absolute paths
- The `<embed>` element always inherits styles from the parent document
- For style isolation, use `<iframe>` instead with `data-passthrough="false"`
- If the external content fails to load in Strict mode, an error is thrown
- In Lax conformance mode, loading errors are logged but generation continues
- Embedded content can contain data binding expressions that are evaluated in the parent document's data context
- Multiple `<embed>` elements can reference the same external file
- Embedded content can itself contain additional `<embed>` elements (nesting is supported)
- The element is self-closing in HTML syntax: `<embed src="..." />`

---

## Examples

### Simple Content Inclusion

Include a header template in your document:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Document</title>
</head>
<body>
    <embed src="./partials/header.html" />

    <div class="content">
        <h1>Main Content</h1>
        <p>This is the main document content.</p>
    </div>

    <embed src="./partials/footer.html" />
</body>
</html>
```

### Dynamic Template Loading

Load templates based on data values:

```html
{% raw %}<embed src="{{model.headerTemplate}}" />

<div>
    <h1>{{model.title}}</h1>
    <p>{{model.description}}</p>
</div>

<embed src="{{model.footerTemplate}}" />{% endraw %}
```

With data:
```json
{
    "model": {
        "headerTemplate": "./headers/corporate-header.html",
        "footerTemplate": "./footers/standard-footer.html",
        "title": "Annual Report",
        "description": "Financial results for 2025"
    }
}
```

### Multi-Language Support

Load language-specific content:

```html
{% raw %}<embed src="{{'i18n/' + model.language + '/header.html'}}" />

<div class="content">
    <embed src="{{'i18n/' + model.language + '/welcome.html'}}" />
</div>

<embed src="{{'i18n/' + model.language + '/footer.html'}}" />{% endraw %}
```

With data:
```json
{
    "model": {
        "language": "es"
    }
}
```

### Conditional Content Inclusion

Include content only when conditions are met:

```html
{% raw %}<div class="document">
    <h1>{{model.reportTitle}}</h1>

    <embed src="./sections/summary.html" />

    <embed src="./sections/detailed-analysis.html"
           hidden="{{if(model.includeDetails, '', 'hidden')}}" />

    <embed src="./sections/appendix.html"
           hidden="{{if(model.includeAppendix, '', 'hidden')}}" />
</div>{% endraw %}
```

With data:
```json
{
    "model": {
        "reportTitle": "Quarterly Report",
        "includeDetails": true,
        "includeAppendix": false
    }
}
```

### Reusable Table Components

Include reusable table structures:

```html
{% raw %}<h2>Sales Data</h2>
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <embed src="./components/sales-table-header.html" />
    </thead>
    <tbody>
        <template data-bind="{{salesData}}">
        <tr>
            <td>{{this.region}}</td>
            <td>{{this.amount}}</td>
            <td>{{this.growth}}</td>
        </tr>
        </template>
    </tbody>
    <tfoot>
        <embed src="./components/table-footer.html" />
    </tfoot>
</table>{% endraw %}
```

### Remote Content Loading

Load content from remote URLs:

```html
<div class="document">
    <!-- Load company header from CDN -->
    <embed src="https://cdn.company.com/templates/header.html" />

    <div class="content">
        <p>Document content here...</p>
    </div>

    <!-- Load disclaimer from remote server -->
    <embed src="https://legal.company.com/disclaimers/standard.html" />
</div>
```


### Modular Document Assembly

Build complex documents from multiple parts:

```html
{% raw %}<!DOCTYPE html>
<html>
<head>
    <title>{{model.documentTitle}}</title>
</head>
<body>
    <!-- Cover page -->
    <div style="page-break-after: always;">
        <embed src="sections/cover.html" />
    </div>

    <!-- Table of contents -->
    <div style="page-break-after: always;">
        <embed src="sections/toc.html" />
    </div>

    <!-- Chapters -->
    <div style="page-break-after: always;">
        <embed src="chapters/chapter1.html" />
    </div>

    <div style="page-break-after: always;">
        <embed src="chapters/chapter2.html" />
    </div>

    <div>
        <embed src="chapters/chapter3.html" />
    </div>
</body>
</html>{% endraw %}
```

### Example 9: API-Driven Content

Load content from API endpoints:

```html
{% raw %}<div class="report">
    <embed src="{{model.apiUrl + '/reports/' + model.reportId + '/header.html'}}" />

    <div class="report-body">
        <embed src="{{model.apiUrl + '/reports/' + model.reportId + '/body.html'}}" />
    </div>

    <embed src="{{model.apiUrl + '/reports/' + model.reportId + '/footer.html'}}" />
</div>{% endraw %}
```

With data:
```json
{
    "model": {
        "apiUrl": "https://api.example.com",
        "reportId": "12345"
    }
}
```


### Template Versioning

Load different template versions:

```html
{% raw %}<embed src="{{'templates/v' + model.templateVersion + '/header.html'}}" />

<div class="content">
    <h1>{{model.title}}</h1>
    <embed src="{{'templates/v' + model.templateVersion + '/body.html'}}" />
</div>

<embed src="{{'templates/v' + model.templateVersion + '/footer.html'}}" />{% endraw %}
```

With data:
```json
{
    "model": {
        "templateVersion": "2",
        "title": "Updated Document Format"
    }
}
```


### Nested Embeds with Parameters

Store parameters and use in embedded content:

```html
{% raw %}<var data-id="companyName" data-value="{{model.company}}" />
<var data-id="reportDate" data-value="{{date(model.date)}}" />

<div class="annual-report">
    <embed src="./sections/cover.html" />
    <!-- cover.html can access and perform calculations on {{companyName}} and {{reportDate}} -->

    <embed src="./sections/letter-to-shareholders.html" />

    <embed src="./sections/financial-highlights.html" />
</div>{% endraw %}
```

With data:
```json
{
    "model": {
        "company": "Acme Corporation",
        "date": "2025-04-30"
    }
}
```

### Context-Aware Content

Include content based on multiple conditions:

```html
{% raw %}<var data-id="documentType" data-value="{{model.type}}" />
<var data-id="securityLevel" data-value="{{model.security}}" />

<div class="secure-document">
    <!-- Header varies by security level -->
    <embed src="{{'headers/' + model.security + '-security-header.html}}" />

    <!-- Main content -->
    <div class="content">
        <h1>{{model.title}}</h1>
        <embed src="{{'content/' + model.type + '/main.html'}}" />
    </div>

    <!-- Conditional watermark -->
    <if data-test="{{model.security == 'high'}}" >
        <div style="position: absolute; top: 50%; left: 50%; transform: rotate(-45deg);
                    opacity: 0.1; font-size: 72pt; color: red;">
            <embed src="watermarks/confidential.html" />
        </div>
    </if>

    <!-- Footer varies by document type and security -->
    <embed src="{{'footers/' + model.security + '-security-header.html}}" />

    <!-- Audit trail for classified documents -->
    <if data-test="{{model.requiresAudit}}" >
        <div style="page-break-before: always; font-size: 8pt;">
            <embed src="audit/audit-trail.html" />
        </div>
    </if>
</div>{% endraw %}
```

With data:
```json
{
    "model": {
        "type": "financial",
        "security": "high",
        "title": "Q4 Financial Projections",
        "requiresAudit": true
    }
}
```

---

## See Also

- [span](html_span_elelemts.html) - Generic inline container element
- [cite, defn, q](html_output_slot_num_elements.html) - Other inline semantic text elements
- [var](html_var_element.html) - For storing or outputting document parameters.
- [Text Formatting](/library/templates/text.html) - Text formatting
- [Data Binding](/library/binding/) - Data binding expressions
- [CSS Styling](/library/styles/) - CSS styling reference

---
