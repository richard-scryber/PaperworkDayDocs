---
layout: default
title: Configuration Structure
parent: Configuration & Extension
parent_url: /configuration/
has_children: false
has_toc: false
nav_order: 5
---

# Scryber Configuration File Structure


This comprehensive guide covers Scryber's configuration system. This documentation is aimed at developers who need to understand the internal architecture or extend Scryber's capabilities.

## Table of Contents

1. [Configuration Structure](#configuration-architecture)
6. [Image Factory System](#image-factory-configuration)
7. [Font Configuration](#font-configuration)
5. [Namespace Registration](#namespace-registration)
8. [Function Configuration](#function-configuration)
8. [Advanced Topics](#advanced-topics)

---

## Configuration Architecture

Scryber uses the .NET Core configuration system (`Microsoft.Extensions.Configuration`) with a hierarchical options pattern. Configuration is loaded from `scrybersettings.json` or `appsettings.json` and accessed through the `IScryberConfigurationService` available via dependency injection.

### Initializing the Configuration Service

To make sure that Scryber can access any custom configuration you must initialize it at application **start up**.


#### Console application

```csharp
// set up the configuraion as needed.
IConfigurationRoot config = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json")
    .Build();
    
//pass the configuration to the service provider class.
Scryber.ServiceProvider.Init(config);
```

#### ASP.NET MVC application

```csharp
//set up your app as wanted
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
var app = builder.Build();

//... pass it's configuration to Scryber.

Scryber.ServiceProvider.Init(app.Configuration);
```


### Accessing Configuration Service Bootstrap

```csharp
// Internal bootstrap in ServiceProvider
var config = ServiceProvider.GetService<IScryberConfigurationService>();
```

The configuration service exposes five primary option sections:
- `OutputOptions` - PDF output settings
- `ParsingOptions` - XML/HTML parsing behavior
- `FontOptions` - Font loading and registration
- `ImagingOptions` - Image factory registration
- `TracingOptions` - Logging configuration

### Configuration File Structure

```json

{
    /*
    Other configuration properties
    ...
    */

  "Scryber": {
    "Output": { /* PDF Output optins */    },
    "Parsing": { 
      "Namespaces": [ /* Custom namespace registrations */ ],
      "Bindings": [ /* Expression binding factories */ ]
    },
    "Fonts": {
      "Register": [ /* Custom font registrations */ ]
    },
    "Imaging": {
      "Factories": [ /* Custom image factories */ ]
    },
    "Tracing": { /* Logging configuration */ 
      "Loggers" : [
        /* Custom logging factories */
      ]
    }
  }
}
```

All properties are optional, and the default values are shown above.

---

## Image Factory Configuration

Image factories load image data from various sources (files, URLs, data URLs, streams) andl convert raw image data (png, jpeg, tiff, svg) into a format that can be written to a PDF file in the standard format. 


### Configuration Structure

```json
{
  "Scryber": {
    "Imaging": {
      "AllowMissingImages": true,
      "ImageCacheDuration": 60,
      "MinimumScaleReduction": 0.249,
      "Factories": [
        {
          "Name": "CustomImageLoader",
          "Match": ".*\\.custom",
          "FactoryType": "MyNamespace.CustomImageFactory",
          "FactoryAssembly": "MyAssembly, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
        }
      ]
    }
  }
}
```

### Configuration Properties

| Property | Type | Description |
|----------|------|-------------|
| `AllowMissingImages` | bool | If true, missing images log warning; if false, throw exception |
| `ImageCacheDuration` | int | Cache duration in minutes (-1 = no cache, 0 = session only, >0 = duration) |
| `MinimumScaleReduction` | double | Minimum scale factor before forcing a new layout container, e.g. a column, or a page. Default is 0.249 |
| `Factories[]` | array | Custom image factory registrations |

### Factory Registration Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Name` | string | Yes | Unique factory identifier |
| `Match` | string | Yes | Regex pattern for path matching |
| `FactoryType` | string | Yes | Fully qualified type name (namespace + class) |
| `FactoryAssembly` | string | Yes | Full assembly name with version and public key token |

### Factory Loading Mechanics

**Configuration loading** in `ImageOptionExtensions.GetConfiguredFactories()`:

```csharp
// Scryber.Imaging/Options/_Extensions.cs
public static ImageFactoryList GetConfiguredFactories(this ImagingOptions options)
{
    ImageDataFactoryOption[] configured = null;
    var standard = GetStandardFactories();
    var list = new ImageFactoryList();
    
    if (null != options && null != options.Factories && options.Factories.Length > 0)
    {
        configured = options.Factories;
        foreach (var configFactory in configured)
        {
            // Lazy-load and cache factory instance
            var instance = configFactory.GetInstance() as IPDFImageDataFactory;
            if (null == instance)
                throw new InvalidCastException(
                    "The configured image data factory entry '" + (configFactory.Name ?? "UNNAMED") +
                    "' does not implement the IImageDataFactory interface");

            // Wrap in custom factory with regex matcher
            var factory = new ImageFactoryCustom(
                new Regex(configFactory.Match), 
                configFactory.Name,
                instance.ShouldCache, 
                instance);

            list.Add(factory);
        }
    }
    
    // Add standard factories AFTER custom factories
    // This allows custom factories to override standard extensions
    list.AddRange(standard);
    
    return list;
}
```

**Standard factories** (always loaded):

```csharp
private static readonly ImageFactoryBase[] Standards = new ImageFactoryBase[]
{
    new ImageFactoryGif(),        // .*\.gif$
    new ImageFactoryPng(),        // .*\.png$
    new ImageFactoryTiff(),       // .*\.(tiff?|tif)$
    new ImageFactoryJpeg(),       // .*\.(jpe?g|jpg)$
    new ImageFactoryPngDataUrl(), // data:image/png
    new ImageFactoryJpegDataUrl(),// data:image/jpeg
    new ImageFactoryGifDataUrl()  // data:image/gif
};
```

All documents maintain a list of image factories available to them.

This can either be added to on an individual basis.

```csharp
doc.ImageFactories.Insert(0, new MyCustomImageType()); //always checked in order, so go first.
```

Or to evey document via the Imaging.Factories options.

### Implementing Custom Image Factories

{: .note }
> Needs to more to the separate file.

**Base class implementation pattern:**

```csharp
// Scryber.Imaging/Imaging/ImageFactoryBase.cs
public abstract class ImageFactoryBase : IPDFImageDataFactory
{
    public bool ShouldCache { get; }
    public Regex Match { get; }
    public MimeType ImageType { get; }
    public string Name { get; }
    
    public ImageFactoryBase(Regex match, MimeType type, string name, bool shouldCache)
    {
        this.Match = match ?? throw new ArgumentNullException(nameof(match));
        this.ImageType = type ?? MimeType.Empty;
        this.Name = name;
        this.ShouldCache = shouldCache;
    }

    public virtual bool IsMatch(string forPath)
    {
        return this.Match.IsMatch(forPath);
    }
    
    public virtual ImageData LoadImageData(IDocument document, IComponent owner, string path)
    {
        //override to add your own loading logic
    }

    public override async Task<ImageData> LoadImageDataAsync(IDocument document, IComponent owner, string path)
    {
        //Override to add your own async loading logic
    }
    
    protected virtual ImageData DoLoadRawImageData(IDocument document, IComponent owner, byte[] rawData, MimeType type)
    {
        //override to add your own image data conversion.
    }

    protected virtual Task<ImageData> DoLoadImageDataAsync(IDocument document, IComponent owner, string path)
    {
        //override to add your own async image data conversion.
    }
}
```

**Example custom factory:**

In this example we want to provide our own factory that will load some images that are stored in a database, rather than accessed from the file system.

We could implement a separate web handler to accept and return images from the DB over a http(s) request, to the template, but it is more performant to directly access via a connection so we can write a custom DatabaseImageFactory.

We can intercept requests for any 'db://' image path and handle independently. We can then call back to the document to actually convert the stored binary data to a known image data instance.



```csharp
public class DatabaseImageFactory : ImageFactoryBase
{
    public DatabaseImageFactory() 
        : base(new Regex(@"^db://"), MimeType.Empty, "DatabaseImages", shouldCache: true)
    {
    }
    
    protected override async Task<ImageData> DoLoadImageDataAsync(IDocument document, IComponent owner, string path)
    {
        // Extract ID from path: db://images/12345
        var id = path.Substring(path.LastIndexOf('/') + 1);
        
        // Load from database
        byte[] imageBytes = await LoadImageFromDatabase(id);
        MimeType type = DetectImageType(imageBytes);
        
        return DoLoadRawImageData(document, owner, imageBytes, type);
    }
    
    protected override ImageData DoLoadRawImageData(IDocument document, IComponent owner, byte[] rawData, MimeType type)
    {
        using (var stream = new MemoryStream(rawData))
        {
            return DoDecodeImageData(stream, document, owner, "db-image");
        }
    }
}
```

### Image Factory Selection Algorithm

**Path matching in `ImageFactoryList.TryGetMatch()`:**

```csharp
// Scryber.Imaging/Imaging/ImageFactoryList.cs
public bool TryGetMatch(string path, out ImageFactoryBase factory)
{
    // Skip data URLs - they're handled specially
    if (path.StartsWith("data:"))
    {
        // Continue to factory checks
    }
    else if (Uri.IsWellFormedUriString(path, UriKind.RelativeOrAbsolute))
    {
        // Extract local path from URI for matching
        path = new Uri(path).LocalPath;
    }

    // Iterate factories in registration order
    // Custom factories are checked BEFORE standard factories
    foreach (var match in this)
    {
        if (match.IsMatch(path))
        {
            factory = match;
            return true;
        }
    }

    factory = null;
    return false;
}
```

### Adding to a template

With the new image factory configured, any images with a source that starts with 'db://' will use the custom image factory to load the data.

```html
<img src='db://mypictureid' />
```

This can also be bound to model data

```html
{% raw %}<img id='{{concat("img_", model.recordid)}}' src='{{concat("db://", model.recordid)}}' />{% endraw %}
```

---

## Font Configuration System

Font configuration controls font loading from system fonts, custom directories, and explicit file registrations.

### Configuration Structure

```json
{
  "Scryber": {
    "Fonts": {
      "DefaultDirectory": "/path/to/fonts",
      "UseSystemFonts": true,
      "FontSubstitution": true,
      "DefaultFont": "Sans-Serif",
      "Register": [
        {
          "Family": "Custom Font",
          "Style": "Regular",
          "Weight": 400,
          "File": "/path/to/customfont.ttf"
        },
        {
          "Family": "Custom Font",
          "Style": "Bold",
          "Weight": 700,
          "File": "/path/to/customfont-bold.ttf"
        }
      ]
    }
  }
}
```

### Configuration Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `DefaultDirectory` | string | `""` | Directory to scan for font files |
| `UseSystemFonts` | bool | `true` | Load fonts from system font directories |
| `FontSubstitution` | bool | `true` | Allow font substitution when requested font unavailable |
| `DefaultFont` | string | `"Sans-Serif"` | Default font family name |
| `Register[]` | array | `[]` | Explicit font file registrations |

### Font Registration Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Family` | string | No | Override font family name (uses font's internal name if omitted) |
| `Style` | string | No | Font style: `Regular`, `Italic`, `Bold`, `BoldItalic` |
| `Weight` | int | No | Font weight: 100-900 (400=Regular, 700=Bold) |
| `File` | string | Yes | Absolute or relative path to `.ttf` font file |

### Font Loading Architecture

The `FontFactory` maintains **four separate font registries**:

```csharp
// Scryber.Drawing/Drawing/FontFactory.cs
private static FamilyReferenceBag _static;   // Embedded Standard Type 1 fonts (Helvetica, Times, Courier, etc.)
private static FamilyReferenceBag _system;   // System-installed fonts (platform-dependent)
private static FamilyReferenceBag _custom;   // User-registered fonts from configuration
private static FamilyReferenceBag _generic;  // Generic family mappings (Sans-Serif → Helvetica)
```

**Font lookup hierarchy:**

```csharp
public static FontDefinition GetFontDefinition(String family, FontStyle style, int weight, bool throwNotFound = true)
{
    FamilyReference fref;
    FontReference fontRef = null;

    // 1. Check custom fonts (user-registered)
    if (_custom.TryGetFamily(family, out fref))
    {
        fontRef = fref.GetFont(style, weight);
    }
    
    // 2. Check system fonts
    if (fontRef == null && _system.TryGetFamily(family, out fref))
    {
        fontRef = fref.GetFont(style, weight);
    }
    
    // 3. Check static fonts (embedded Type 1)
    if (fontRef == null && _static.TryGetFamily(family, out fref))
    {
        fontRef = fref.GetFont(style, weight);
    }
    
    // 4. Check generic family mappings
    if (fontRef == null && _generic.TryGetFamily(family, out fref))
    {
        fontRef = fref.GetFont(style, weight);
    }

    if (fontRef == null)
    {
        if (throwNotFound)
            throw new ArgumentException($"Font '{family}' not found");
        return null;
    }

    // Lazy-load font definition
    if (!fontRef.IsLoaded)
    {
        LoadFontDefinition(fontRef);
    }

    return fontRef.Definition;
}
```

### Custom Font Registration Implementation

**Font loading from configuration:**

```csharp
// Scryber.Drawing/Drawing/FontFactory.cs
private static FamilyReferenceBag UnsafeLoadCustomFonts(FontOptions options)
{
    FamilyReferenceBag custom = new FamilyReferenceBag();

    if (options.Register == null || options.Register.Length == 0) 
        return custom;

    using (var reader = new TypefaceReader())
    {
        foreach (var known in options.Register)
        {
            if (string.IsNullOrEmpty(known.File)) 
                continue;
            
            // Resolve file path (relative to application base)
            var file = new FileInfo(GetFullPath(known.File));
                
            if (!file.Exists) 
                continue;

            // Read OpenType/TrueType font file
            var info = reader.ReadTypeface(file);

            if (null != info && string.IsNullOrEmpty(info.ErrorMessage) && info.FontCount > 0)
            {
                foreach (var font in info.Fonts)
                {
                    // Use configured family name OR font's internal family name
                    var family = known.Family ?? font.FamilyName;
                    
                    // Register font with family, style, and weight
                    custom.AddFont(info, font, family);
                }
            }
        }

        // Scan default directory for additional fonts
        var defaultDir = options.DefaultDirectory;
        if (!string.IsNullOrEmpty(defaultDir))
        {
            UnsafeReadFontsFromDirectory(reader, defaultDir, custom);
        }
    }

    return custom;
}
```

**Font family structure:**

```csharp
// Internal font registry structure
private class FamilyReferenceBag : Dictionary<string, FamilyReference>
{
    public FontReference AddFont(ITypefaceInfo info, IFontInfo font, string familyName = null)
    {
        FamilyReference family;

        if (!_families.TryGetValue(familyName ?? font.FamilyName, out family))
        {
            family = new FamilyReference(familyName ?? font.FamilyName);
            _families.Add(familyName ?? family.FamilyName, family);
        }
        
        var reference = family.Add(font, info);
        return reference;
    }
}

private class FamilyReference
{
    public string FamilyName { get; }
    private Dictionary<FontStyleKey, FontReference> _fonts;
    
    public FontReference Add(IFontInfo font, ITypefaceInfo typeface)
    {
        var key = new FontStyleKey(font.FontStyle, font.Weight);
        var reference = new FontReference(font, typeface);
        _fonts[key] = reference;
        return reference;
    }
    
    public FontReference GetFont(FontStyle style, int weight)
    {
        var key = new FontStyleKey(style, weight);
        FontReference exact;
        
        // Try exact match
        if (_fonts.TryGetValue(key, out exact))
            return exact;
        
        // Try font substitution based on style and weight
        return FindClosestFont(style, weight);
    }
}
```

### Standard Type 1 Font Embedding

Scryber embeds **14 standard PDF Type 1 fonts** as assembly resources:

```csharp
private static FamilyReferenceBag UnsafeLoadStaticFamilies(FontOptions options)
{
    var bag = new FamilyReferenceBag();
    var assm = typeof(FontFactory).Assembly;
    
    using (var reader = new TypefaceReader())
    {
        // Courier family (4 variants)
        TryReadFontBinary(reader, assm, "Scryber.Text._FontResources.Courier.CourierNew.ttf", out var found);
        bag.AddFont(found, found.Fonts[0], "Courier").Definition = 
            PDFOpenTypeFontDefinition.InitStdType1WinAnsi("Fcour", "Courier", "Courier", "Courier New", 
                false, false, 1228, found.Fonts[0] as IOpenTypeFont);
        
        TryReadFontBinary(reader, assm, "Scryber.Text._FontResources.Courier.CourierNewBold.ttf", out found);
        bag.AddFont(found, found.Fonts[0], "Courier").Definition = 
            PDFOpenTypeFontDefinition.InitStdType1WinAnsi("FcourBo", "Courier-Bold", "Courier", "Courier New", 
                true, false, 1228, found.Fonts[0] as IOpenTypeFont);
        
        // ... Courier-Italic, Courier-BoldItalic
        
        // Helvetica family (4 variants)
        // Times family (4 variants)  
        // Symbol (1 font)
        // ZapfDingbats (1 font)
    }
    
    return bag;
}
```

Standard fonts are **always available** even if system fonts are disabled, ensuring baseline compatibility.

---

## Namespace Registration

Namespace registration maps **XML namespace URIs** to **.NET assembly namespaces**, enabling the parser to locate component types.

### Configuration Structure

```json
{
  "Scryber": {
    "Parsing": {
      "Namespaces": [
        {
          "Source": "http://www.mycompany.com/schemas/custom",
          "Namespace": "MyCompany.CustomComponents",
          "Assembly": "MyCompany.PDFComponents, Version=1.0.0.0, Culture=neutral, PublicKeyToken=1234567890abcdef"
        }
      ]
    }
  }
}
```

### Namespace Registration Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Source` | string | Yes | XML namespace URI (used in `xmlns` declarations) |
| `Namespace` | string | Yes | .NET namespace containing component classes |
| `Assembly` | string | Yes | Full assembly name with version and public key token |

### Built-in Namespace Registrations

```csharp
// Default registrations in ParsingOptions constructor
Namespaces.Add(new NamespaceMappingOption() 
{ 
    Source = "http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Components.xsd",
    Namespace = "Scryber.Components",
    Assembly = "Scryber.Components, Version=1.0.0.0, Culture=neutral, PublicKeyToken=872cbeb81db952fe"
});

Namespaces.Add(new NamespaceMappingOption() 
{ 
    Source = "http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Data.xsd",
    Namespace = "Scryber.Data",
    Assembly = "Scryber.Components, Version=1.0.0.0, Culture=neutral, PublicKeyToken=872cbeb81db952fe"
});

Namespaces.Add(new NamespaceMappingOption() 
{ 
    Source = "http://www.w3.org/1999/xhtml",
    Namespace = "Scryber.Html.Components",
    Assembly = "Scryber.Components, Version=1.0.0.0, Culture=neutral, PublicKeyToken=872cbeb81db952fe"
});

Namespaces.Add(new NamespaceMappingOption() 
{ 
    Source = "http://www.w3.org/2000/svg",
    Namespace = "Scryber.Svg.Components",
    Assembly = "Scryber.Components, Version=1.0.0.0, Culture=neutral, PublicKeyToken=872cbeb81db952fe"
});
```

### Namespace Lookup Mechanism

**XML namespace to assembly namespace mapping:**

```csharp
// Scryber.Generation/ParserDefintionFactory.cs
private static Dictionary<string, string> _namespaceMappings;

public static string LookupAssemblyForXmlNamespace(string xmlNamespace)
{
    string assm;
    if (!_namespaceMappings.TryGetValue(xmlNamespace, out assm))
        assm = xmlNamespace; // Fallback: treat XML namespace as assembly namespace
    return assm;
}

private static Dictionary<string, string> InitNamespaceMappings()
{
    var mappings = new Dictionary<string, string>();
    
    var config = ServiceProvider.GetService<IScryberConfigurationService>();
    var options = config.ParsingOptions;
    
    if (options.Namespaces != null)
    {
        foreach (var mapping in options.Namespaces)
        {
            // Format: "Namespace, Assembly"
            string value = mapping.Namespace + ", " + mapping.Assembly;
            mappings[mapping.Source] = value;
        }
    }
    
    return mappings;
}
```

### Type Resolution Process

**Full type resolution from XML element:**

```csharp
public static ParserClassDefinition GetClassDefinition(string elementname, string xmlNamespace, 
    bool throwOnNotFound, out bool isremote)
{
    Type found;
    lock (_applicationlock)
    {
        string assemblyQualifiedNamespace = string.Empty;

        if (!string.IsNullOrEmpty(xmlNamespace))
        {
            // Map XML namespace to assembly namespace
            assemblyQualifiedNamespace = LookupAssemblyForXmlNamespace(xmlNamespace);
        }
        else
        {
            // Check unqualified element whitelist
            string unqualNs;
            if (_unqualified.TryGetValue(elementname, out unqualNs))
                assemblyQualifiedNamespace = unqualNs;
        }

        found = UnsafeGetType(elementname, assemblyQualifiedNamespace, throwOnNotFound, out isremote);
    }

    if (null != found)
        return GetClassDefinition(found);
    else
        return null;
}
```

**Assembly and namespace extraction:**

```csharp
private static Type UnsafeGetType(string elementname, string assemblyQualifiedNamespace, 
    bool throwOnNotFound, out bool isremote)
{
    AssemblyDefn assmdefn;
    NamespaceDefn nsdefn;
    Type t;

    // Parse "Namespace, Assembly" format
    string assm;
    string ns;
    ExtractAssemblyAndNamespace(assemblyQualifiedNamespace, out assm, out ns);
    
    if (string.IsNullOrEmpty(assm))
    {
        if (throwOnNotFound)
            throw new PDFParserException($"Parser does not have assembly registered for namespace {assemblyQualifiedNamespace}");
        else
            return null;
    }

    // Get or load assembly definition
    if (!_application.TryGetValue(assm, out assmdefn))
    {
        assmdefn = new AssemblyDefn();
        Assembly found = GetAssemblyByName(assm);
        
        if (null == found)
        {
            if (throwOnNotFound)
                throw new PDFParserException($"Parser cannot find assembly with name {assm}");
            else
                return null;
        }
        
        assmdefn.InnerAssembly = found;
        _application[assm] = assmdefn;
    }

    // Get or populate namespace definition
    if (!assmdefn.TryGetValue(ns, out nsdefn))
    {
        nsdefn = new NamespaceDefn();
        PopulateNamespaceFromAssembly(ns, assmdefn, nsdefn);
        assmdefn[ns] = nsdefn;
    }

    // Look up type in namespace
    if (!nsdefn.TryGetValue(elementname, out t))
    {
        // Check remote types (components loaded from external sources)
        string actual;
        if (!nsdefn.RemoteTypes.TryGetValue(elementname, out actual) || 
            !nsdefn.TryGetValue(actual, out t))
        {
            if (throwOnNotFound)
                throw new PDFParserException($"No PDF component declared with name {elementname} in namespace {assemblyQualifiedNamespace}");
            else
                return null;
        }
        else
        {
            isremote = true;
        }
    }
    else
    {
        isremote = false;
    }

    return t;
}
```

**Namespace reflection and caching:**

```csharp
private static void PopulateNamespaceFromAssembly(string ns, AssemblyDefn assmdefn, NamespaceDefn nsdefn)
{
    Type[] all = assmdefn.InnerAssembly.GetTypes();
    
    foreach (Type t in all)
    {
        if (string.Equals(t.Namespace, ns))
        {
            // Check for PDFParsableComponent attribute
            object[] attrs = t.GetCustomAttributes(typeof(PDFParsableComponentAttribute), false);
            
            if (null != attrs && attrs.Length > 0)
            {
                PDFParsableComponentAttribute compattr = (PDFParsableComponentAttribute)attrs[0];
                string name = compattr.ElementName;
                
                if (string.IsNullOrEmpty(name))
                    name = t.Name;

                // Register concrete element
                nsdefn.Add(name, t);

                // Check for remote element variant
                attrs = t.GetCustomAttributes(typeof(PDFRemoteParsableComponentAttribute), false);
                if (null != attrs && attrs.Length > 0)
                {
                    PDFRemoteParsableComponentAttribute remattr = (PDFRemoteParsableComponentAttribute)attrs[0];
                    string remotename = remattr.ElementName;
                    
                    if (string.IsNullOrEmpty(remotename))
                        remotename = t.Name + "-Ref";
                    
                    // Map remote element name to concrete element name
                    nsdefn.RemoteTypes.Add(remotename, name);
                }
            }
        }
    }
}
```

### Creating Custom Components

**Component attribute decoration:**

```csharp
using Scryber.Generation;
using Scryber.Components;

namespace MyCompany.CustomComponents
{
    [PDFParsableComponent("CustomPanel")]
    [PDFJSConvertor("mycompany.convertors.custom_panel")]
    public class CustomPanel : Panel
    {
        [PDFAttribute("background-pattern")]
        public string BackgroundPattern { get; set; }
        
        [PDFElement("Header")]
        public Component Header { get; set; }
        
        [PDFArray(typeof(Component))]
        [PDFElement("Items")]
        public ComponentList Items { get; private set; }
        
        public CustomPanel()
        {
            Items = new ComponentList(this, ObjectTypes.Component);
        }
        
        protected override void DoBuildLayout(LayoutContext context, Rect bounds)
        {
            // Custom layout logic
        }
    }
}
```

**XML usage after registration:**

```xml
<?xml version="1.0" encoding="utf-8" ?>
<pdf:Document xmlns:pdf="http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Components.xsd"
              xmlns:custom="http://www.mycompany.com/schemas/custom">
    
    <Pages>
        <pdf:Page>
            <Content>
                <custom:CustomPanel background-pattern="dots">
                    <custom:Header>
                        <pdf:H1>Panel Header</pdf:H1>
                    </custom:Header>
                    <custom:Items>
                        <pdf:Label>Item 1</pdf:Label>
                        <pdf:Label>Item 2</pdf:Label>
                    </custom:Items>
                </custom:CustomPanel>
            </Content>
        </pdf:Page>
    </Pages>
    
</pdf:Document>
```

---

## Configuration File Location

Scryber searches for configuration in this order:

1. `scrybersettings.json` (Scryber-specific)
2. `appsettings.json` (standard .NET Core)
3. `appsettings.{Environment}.json` (environment-specific)

Configuration is loaded using `Microsoft.Extensions.Configuration.IConfiguration` and bound to strongly-typed options classes.

---

## Advanced Topics

### Thread Safety

All configuration lookups use **lazy initialization** with locking:

```csharp
private static object _applicationlock = new object();

public static ParserClassDefinition GetClassDefinition(...)
{
    lock (_applicationlock)
    {
        // Thread-safe type resolution
    }
}
```

Configuration is loaded **once at startup** and cached for the application lifetime.

### Performance Considerations

- **Type reflection is cached**: Once a type is resolved, its `ParserClassDefinition` is stored indefinitely
- **Assembly loading is lazy**: Assemblies are only loaded when a type from that assembly is first requested
- **Font definitions are lazy-loaded**: Font metrics are only read when the font is first used
- **Image factories use regex matching**: Keep regex patterns simple for optimal performance

### Configuration Validation

The configuration system performs minimal validation at load time. Invalid configurations typically throw exceptions during first use:

- **Invalid type names**: Throw `TypeLoadException` when attempting to instantiate
- **Missing assemblies**: Throw `FileNotFoundException` during assembly load
- **Invalid regex patterns**: Throw `ArgumentException` in `Regex` constructor
- **Missing font files**: Logged as warnings; fonts skipped

---

## Summary and Integration

Scryber's configuration and extension system provides a comprehensive framework for customization and extension:

### Extension Points Summary

| Extension Point | Mechanism | Use Case | Configuration |
|----------------|-----------|----------|----------------|
| **Processing Instructions** | XML processing instruction | Document-level parser settings | `<?scryber ... ?>` |
| **Controllers** | Code-behind classes with outlets/actions | Separation of logic from presentation | `controller='Type, Assembly'` |
| **Custom Components** | Subclass Component/Panel with attributes | Reusable widgets, domain-specific elements | Namespace registration |
| **Image Factories** | Implement `IPDFImageDataFactory` | Custom image sources (DB, API, etc.) | `Imaging:Factories[]` |
| **Font Registration** | TrueType/OpenType file paths | Custom fonts, branding | `Fonts:Register[]` |
| **Namespaces** | XML to .NET namespace mapping | Component discovery, modular architecture | `Parsing:Namespaces[]` |
| **Binding Factories** | Expression evaluators | Custom data binding syntaxes | `Parsing:Bindings[]` |

### Architecture Principles

1. **Dependency Injection**: Configuration loaded via `IScryberConfigurationService`
2. **Lazy Loading**: Types, assemblies, fonts loaded on-demand
3. **Caching**: Reflected definitions cached for performance
4. **Thread Safety**: Configuration access protected with locks
5. **Convention over Configuration**: Sensible defaults, explicit overrides
6. **Separation of Concerns**: Controllers separate logic from markup
7. **Type Safety**: Strongly-typed configuration options

### Complete Integration Example

This example demonstrates **all extension mechanisms working together**:

**1. Custom Components** (`MyCompany.PDFComponents.dll`):
```csharp
[PDFParsableComponent("DataTable")]
public class DataTable : Panel { /* ... */ }

[PDFParsableComponent("StatCard")]
public class StatCard : Panel { /* ... */ }
```

**2. Custom Image Factory** (`MyCompany.PDFExtensions.dll`):
```csharp
public class DatabaseImageFactory : ImageFactoryBase
{
    protected override async Task<ImageData> DoLoadImageDataAsync(...)
    {
        // Load from database
    }
}
```

**3. Configuration** (`scrybersettings.json`):
```json
{
  "Scryber": {
    "Parsing": {
      "Namespaces": [
        {
          "Source": "http://www.mycompany.com/schemas/components",
          "Namespace": "MyCompany.PDFComponents",
          "Assembly": "MyCompany.PDFComponents"
        }
      ]
    },
    "Imaging": {
      "Factories": [
        {
          "Name": "DatabaseImages",
          "Match": "^db://",
          "FactoryType": "MyCompany.PDFExtensions.DatabaseImageFactory",
          "FactoryAssembly": "MyCompany.PDFExtensions"
        }
      ]
    },
    "Fonts": {
      "Register": [
        {
          "Family": "Company Brand",
          "File": "Fonts/CompanyBrand-Regular.ttf"
        }
      ]
    }
  }
}
```

**4. Controller** (`MyCompany.Reports.dll`):
```csharp
namespace MyCompany.Reports
{
    public class MonthlyReportController
    {
        [PDFOutlet(Required = true)]
        public StatCard SalesCard { get; set; }
        
        [PDFOutlet]
        public DataTable DataTable { get; set; }
        
        [PDFOutlet]
        public Image CompanyLogo { get; set; }

        public void Init(InitContext context)
        {
            CompanyLogo.Source = "db://logos/company-logo";
        }

        public void LoadData(LoadContext context)
        {
            var data = FetchMonthlyData();
            DataTable.DataSource = data;
            SalesCard.Value = data.Sum(d => d.Amount).ToString("C");
        }

        private List<SalesData> FetchMonthlyData()
        {
            // Database query
            return new List<SalesData>();
        }
    }
}
```

**5. Template** (`MonthlyReport.pdfx`):
```xml
<?xml version='1.0' encoding='utf-8' ?>
<?scryber parser-mode='Strict' 
          log-level='Warnings'
          controller='MyCompany.Reports.MonthlyReportController, MyCompany.Reports' ?>

<pdf:Document xmlns:pdf='http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Components.xsd'
              xmlns:mc='http://www.mycompany.com/schemas/components'
              font-family='Company Brand'>
    
    <Pages>
        <pdf:Page on-init='Init' on-load='LoadData'>
            
            <Header>
                <!-- Image loaded from database via custom factory -->
                <pdf:Image id='CompanyLogo' />
                <pdf:H1>Monthly Sales Report</pdf:H1>
            </Header>
            
            <Content>
                
                <!-- Custom StatCard component -->
                <mc:StatCard id='SalesCard' 
                             icon='💰'
                             label='Total Sales' />
                
                <!-- Custom DataTable component -->
                <mc:DataTable id='DataTable'
                              show-header='true'
                              stripe-rows='true' />
                
            </Content>
            
        </pdf:Page>
    </Pages>
    
</pdf:Document>
```

**6. Usage**:
```csharp
using (var stream = File.OpenRead("MonthlyReport.pdfx"))
{
    var doc = Document.ParseDocument(stream, ParseSourceType.DynamicContent);
    doc.ProcessDocument("MonthlyReport.pdf");
}
```

This example demonstrates:
- ✅ Custom components in their own namespace
- ✅ Custom image factory for database images
- ✅ Custom font registration
- ✅ Controller with outlets and actions
- ✅ Processing instructions for document settings
- ✅ Full integration of all extension mechanisms

### Best Practices

#### Configuration
- Store configuration in `scrybersettings.json` for Scryber-specific settings
- Use environment-specific files: `scrybersettings.Development.json`
- Validate configuration at startup with unit tests
- Document custom configuration requirements in README

#### Controllers
- Keep controllers focused on coordination, not business logic
- Use dependency injection for services (pass via constructor if needed)
- Mark outlets as `Required` when template contract demands them
- Use descriptive action method names (`HandleDataBinding`, not `OnDB`)
- Test controllers independently of PDF generation

#### Custom Components
- Inherit from appropriate base (`Panel` for containers, `VisualComponent` for UI elements)
- Override `OnInit` to build internal structure
- Override `GetBaseStyle()` for default styling
- Document required attributes and elements
- Provide sensible defaults for all properties
- Test component lifecycle independently

#### Image Factories
- Use specific regex patterns to avoid false matches
- Return `ShouldCache = true` for expensive operations
- Handle errors gracefully (missing images, network failures)
- Log factory invocations for debugging
- Consider async operations for remote resources

#### Font Registration
- Verify font file paths during configuration validation
- Provide fallback fonts if custom fonts missing
- Document font licensing requirements
- Test font embedding in generated PDFs
- Consider file size implications of embedded fonts

#### Namespace Registration
- Use reverse-domain naming for XML namespaces (`http://company.com/schemas/...`)
- Group related components in same namespace
- Version namespaces for breaking changes
- Document namespace registrations in component library README
- Test namespace resolution in integration tests

### Troubleshooting

#### Common Issues

**"No PDF component declared with name X in namespace Y"**
- Verify namespace registration in configuration
- Check `[PDFParsableComponent]` attribute on class
- Ensure assembly is referenced and loaded
- Verify XML namespace in template matches registered namespace

**"Could not assign... to the outlet"**
- Check outlet type matches component type
- Verify component has correct `id` attribute
- Ensure outlet is public property or field
- Check for typos in ComponentID parameter

**"Controller type not found"**
- Verify assembly-qualified name is correct
- Ensure controller assembly is referenced
- Check for typos in processing instruction
- Verify controller class is public

**"Image factory not matching path"**
- Check regex pattern syntax
- Test regex against actual paths
- Verify factory is registered in configuration
- Check factory registration order (custom before standard)

**"Font not found"**
- Verify font file exists at specified path
- Check file permissions
- Ensure font file is valid TrueType/OpenType
- Verify family name matches registered name

### Performance Considerations

- **Type Reflection**: Cached indefinitely; first use slower, subsequent fast
- **Assembly Loading**: Lazy-loaded on first type request from assembly
- **Font Metrics**: Loaded on first font use, cached for document lifetime
- **Image Loading**: Cached based on `ShouldCache` and `ImageCacheDuration`
- **Configuration**: Loaded once at startup, immutable thereafter
- **Controller Reflection**: Definitions cached, instances per-document
- **Namespace Resolution**: Cached after first lookup per namespace

### Related Documentation

- **Expression Binding**: Covered separately in [Data Binding Documentation](../learning/binding/)
- **CSS Parsers**: See [Style System Deep Dive](style-system-deep-dive.md)
- **Layout Engine**: See [Layout Architecture](layout-architecture.md)
- **PDF Generation**: See [PDF Writing Pipeline](pdf-writing-pipeline.md)

---

## Appendix: Configuration Schema Reference

### ParsingOptions

```json
{
  "Parsing": {
    "MissingReferenceAction": "LogError|RaiseException|DoNothing",
    "DefaultCulture": "en-US",
    "Namespaces": [
      {
        "Source": "XML namespace URI",
        "Namespace": ".NET namespace",
        "Assembly": "Full assembly name"
      }
    ],
    "Bindings": [
      {
        "Prefix": "Binding prefix",
        "FactoryType": "Type name",
        "FactoryAssembly": "Assembly name"
      }
    ]
  }
}
```

### ImagingOptions

```json
{
  "Imaging": {
    "AllowMissingImages": true,
    "ImageCacheDuration": 60,
    "MinimumScaleReduction": 0.249,
    "Factories": [
      {
        "Name": "Factory name",
        "Match": "Regex pattern",
        "FactoryType": "Type name",
        "FactoryAssembly": "Assembly name"
      }
    ]
  }
}
```

### FontOptions

```json
{
  "Fonts": {
    "DefaultDirectory": "/path/to/fonts",
    "UseSystemFonts": true,
    "FontSubstitution": true,
    "DefaultFont": "Sans-Serif",
    "Register": [
      {
        "Family": "Font family name",
        "Style": "Regular|Italic|Bold|BoldItalic",
        "Weight": 400,
        "File": "path/to/font.ttf"
      }
    ]
  }
}
```

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**Target**: Scryber.Core 6.x / 7.x

For questions or issues with configuration and extension, please refer to:
- GitHub Issues: https://github.com/richard-scryber/scryber.core/issues
- Documentation: https://scrybercore.readthedocs.io
