---
layout: default
title: Configuration Guide
parent: Configuration & Extension
nav_order: 100
---

# Scryber Configuration
## Deep Technical Documentation

This comprehensive guide covers Scryber's configuration system, extension mechanisms, and the complete implementation details for creating custom components, controllers, and factories. This documentation is aimed at developers who need to understand the internal architecture or extend Scryber's capabilities.

## Table of Contents

1. [Configuration Architecture](#configuration-architecture)
2. [Processing Instructions](#processing-instructions)
3. [Document Controllers](#document-controllers)
4. [Custom Component Development](#custom-component-development)
5. [Namespace Registration](#namespace-registration)
6. [Image Factory System](#image-factory-system)
7. [Font Configuration](#font-configuration)
8. [Advanced Topics](#advanced-topics)

---

## Configuration Architecture

Scryber uses the .NET Core configuration system (`Microsoft.Extensions.Configuration`) with a hierarchical options pattern. Configuration is loaded from `scrybersettings.json` or `appsettings.json` and accessed through the `IScryberConfigurationService` available via dependency injection.

### Configuration Service Bootstrap

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
  "Scryber": {
    "Output": { /* PDF generation settings */ },
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
    "Tracing": { /* Logging configuration */ }
  }
}
```

---

## Processing Instructions

Processing instructions provide **document-level** parser configuration, overriding application configuration for a specific document.

### Syntax

```xml
<?scryber parser-mode='Strict' parser-log='false' append-log='false' 
         log-level='Warnings' controller='MyNamespace.MyController, MyAssembly' ?>
```

### Supported Attributes

| Attribute | Type | Values | Description |
|-----------|------|--------|-------------|
| `parser-mode` | enum | `Strict`, `Lax` | Strict throws on invalid elements; Lax ignores them |
| `parser-log` | bool | `true`, `false` | Enable parser trace output |
| `append-log` | bool | `true`, `false` | Append trace log to PDF document |
| `log-level` | enum | `Off`, `Errors`, `Warnings`, `Messages`, `Verbose`, `Diagnostic` | Minimum log level |
| `parser-culture` | string | Culture code | e.g., `en-GB`, `fr-FR` - affects number/date parsing |
| `controller` | string | Assembly-qualified type name | Document controller class |

### Implementation Details

**Processing instruction parsing** occurs in `XMLParser.ParseProcessingInstructions()`:

```csharp
// Scryber.Generation/XMLParser.cs
protected void ParseProcessingInstructions(XmlReader reader, string name)
{
    string value = reader.Value;
    this.Settings.ReadProcessingInstructions(value);
    
    LogAdd(reader, TraceLevel.Message, 
        "Parsed processing instructions. Controller = {5}, parser mode = {1}, logging = {2}, append-log = {3}, log-level = {4}", 
        value, this.Mode, this.Settings.LogParserOutput, 
        this.Settings.AppendLog, this.Settings.TraceLog.RecordLevel, 
        this.Settings.ControllerType == null ? "[NONE]" : this.Settings.ControllerType.ToString());
}
```

**Attribute extraction** uses simple string parsing in `ParserSettings.GetProcessingValue()`:

```csharp
// Scryber.Common/Generation/ParserSettings.cs
private string GetProcessingValue(string attributename, string full)
{
    int index = full.IndexOf(attributename + "=");
    
    if (index == 0 || (index > 0 && full[index - 1] == ' '))
    {
        index += attributename.Length + 1;
        char separator = full[index];
        int start, end;

        if (separator == '\'' || separator == '"')
        {
            start = index + 1;
            end = full.IndexOf(separator, start);
        }
        else
        {
            start = index;
            end = full.IndexOf(' ', start);
            if (end < start)
                end = full.Length;
        }

        return full.Substring(start, end - start);
    }
    return string.Empty;
}
```

---

## Document Controllers

Document controllers provide **code-behind** functionality for PDF templates, similar to ASP.NET MVC controllers or iOS ViewControllers. Controllers can:
- Access template components via **outlets** (properties/fields)
- Respond to document lifecycle events via **actions** (methods)
- Manipulate document content programmatically
- Implement business logic separate from presentation

### Controller Architecture

Controllers implement a **two-phase initialization pattern**:

1. **Parsing Phase**: Controller is instantiated, outlets are assigned as components are parsed
2. **Lifecycle Phase**: Actions are invoked during document Init, Load, DataBind, Layout, and Render

```
┌─────────────────────────────────────────────────────────────┐
│ Document Parsing                                             │
│  1. <?scryber controller='...' ?> → Instantiate controller  │
│  2. <Component id='myLabel' /> → Assign to outlet           │
│  3. All required outlets assigned? → Attach controller      │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Document Lifecycle                                           │
│  Init → Load → DataBind → PreLayout → Layout → PostLayout  │
│         ↓      ↓          ↓           ↓         ↓           │
│      Actions invoked on each event                          │
└─────────────────────────────────────────────────────────────┘
```

### Outlets

**Outlets** are properties or fields that receive references to components in the template, identified by `id` attribute.

#### PDFOutlet Attribute

```csharp
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property)]
public class PDFOutletAttribute : Attribute
{
    // Optional: Component ID to bind (defaults to member name)
    public string ComponentID { get; set; }
    
    // If true, parsing fails if component not found
    public bool Required { get; set; }
    
    // If false, member is ignored (allows selective disabling)
    public bool IsOutlet { get; set; }
}
```

#### Outlet Declaration Examples

```csharp
public class InvoiceController
{
    // Outlet named by property - looks for id='CustomerLabel'
    [PDFOutlet]
    public Label CustomerLabel { get; set; }
    
    // Explicit component ID - looks for id='invoice-total'
    [PDFOutlet(ComponentID = "invoice-total")]
    public Label TotalLabel { get; set; }
    
    // Required outlet - parser throws if not found
    [PDFOutlet(Required = true)]
    public TableGrid InvoiceItems { get; set; }
    
    // Field outlets work too
    [PDFOutlet]
    public Panel HeaderPanel;
    
    // Non-outlet property (no attribute)
    public decimal TotalAmount { get; set; }
}
```

#### Outlet Assignment Process

**Parser implementation in `XMLParser.TryAssignToControllerOutlet()`:**

```csharp
private void TryAssignToControllerOutlet(XmlReader reader, object instance, string outletName)
{
    ParserControllerOutlet outlet;
    if (this.HasController && this.ControllerDefinition.Outlets.TryGetOutlet(outletName, out outlet))
    {
        try
        {
            outlet.SetValue(this.Controller, instance);
            LogAdd(reader, TraceLevel.Verbose, 
                "Assigned the component with id '{0}' to the declared outlet '{1}' on controller '{2}'", 
                outletName, outlet.OutletMember.Name, this.Controller.ToString());
        }
        catch (Exception ex)
        {
            if (outlet.Required == true || this.Mode == ParserConformanceMode.Strict)
                throw BuildParserXMLException(ex, reader, 
                    "Could not assign the parsed component {0} with id '{1}' to the outlet '{2}' on the controller {3}", 
                    instance, outletName, outlet.OutletMember.Name, this.Controller);
            else
                LogAdd(reader, TraceLevel.Error, 
                    "Could not assign the parsed component {0} with id '{1}' to the outlet '{2}' on the controller {3} : {4}", 
                    instance, outletName, outlet.OutletMember.Name, this.Controller, ex);
        }

        // Remove from unassigned list
        this.UnassignedOutlets.Remove(outlet);
    }
}
```

**Outlet validation after parsing completes:**

```csharp
protected virtual void EnsureAllOutletsAreAssigned(XmlReader reader, IComponent parsed)
{
    if (parsed is IControlledComponent && this.HasController)
    {
        // Check all required outlets are assigned
        foreach (ParserControllerOutlet outlet in this.UnassignedOutlets)
        {
            if (outlet.Required)
                throw new PDFParserException(
                    $"The required outlet {outlet.OutletMember.Name} on the controller has not been assigned from the parsed source. " +
                    $"Make sure there is a component with id '{outlet.ID}' in the main content of source, or unmark the outlet as required");
        }

        LogAdd(reader, TraceLevel.Verbose, "All required outlets have been assigned on the controller.");

        // Attach controller to document
        ((IControlledComponent)parsed).Controller = this.Controller;
    }
}
```

### Actions

**Actions** are methods invoked during document lifecycle events. Action methods must:
- Be public instance methods
- Accept exactly one parameter (the context object for that lifecycle phase)
- Return `void`

#### Supported Lifecycle Events

| Event | Context Type | When Invoked | Use Case |
|-------|--------------|--------------|----------|
| `Init` | `InitContext` | After parsing, before data binding | Initialize state, set default values |
| `Load` | `LoadContext` | After Init, before data binding | Load data, prepare data sources |
| `DataBinding` | `DataBindContext` | Before databinding expressions evaluated | Modify data context |
| `DataBound` | `DataBindContext` | After databinding complete | Post-process bound data |
| `PreLayout` | `LayoutContext` | Before layout calculations | Modify structure before layout |
| `PostLayout` | `LayoutContext` | After layout complete | Access calculated positions/sizes |
| `PreRender` | `RenderContext` | Before PDF rendering | Final modifications |
| `PostRender` | `RenderContext` | After PDF rendering | Cleanup, logging |

#### Action Declaration

```csharp
public class ReportController
{
    [PDFOutlet(Required = true)]
    public Label ReportDateLabel { get; set; }
    
    [PDFOutlet(Required = true)]
    public ForEach DataRepeater { get; set; }

    // Init: Set up initial state
    public void Init(InitContext context)
    {
        context.TraceLog.Add(TraceLevel.Message, "Report Controller", "Initializing report");
        ReportDateLabel.Text = DateTime.Now.ToString("MMMM dd, yyyy");
    }

    // Load: Prepare data sources
    public void Load(LoadContext context)
    {
        var data = LoadReportData();
        DataRepeater.DataSource = data;
        
        context.Document.Params["RecordCount"] = data.Count;
    }

    // DataBinding: Modify binding context
    public void HandleDataBinding(DataBindContext context)
    {
        // Add computed values to data context
        if (context.DataStack.HasData)
        {
            var current = context.DataStack.Current;
            // Augment data object
        }
    }

    // DataBound: Post-process after binding
    public void HandleDataBound(DataBindContext context)
    {
        context.TraceLog.Add(TraceLevel.Verbose, "Report Controller", 
            $"Data binding complete for {DataRepeater.ChildCount} items");
    }

    // PreLayout: Modify before layout
    public void HandlePreLayout(LayoutContext context)
    {
        // Conditionally hide/show components based on data
        if (DataRepeater.ChildCount == 0)
        {
            // Show "no data" message
        }
    }

    // PostLayout: Access layout information
    public void HandlePostLayout(LayoutContext context)
    {
        // Log page count, dimensions
        context.TraceLog.Add(TraceLevel.Message, "Report Controller", 
            $"Layout complete: {context.DocumentLayout.AllPages.Count} pages");
    }

    private List<ReportData> LoadReportData()
    {
        // Database or API call
        return new List<ReportData>();
    }
}
```

#### Action Binding in Templates

Actions are bound via **event handler attributes** on components:

```xml
<pdf:Page on-init='Init' 
          on-load='Load' 
          on-databinding='HandleDataBinding'
          on-databound='HandleDataBound'
          on-prelayout='HandlePreLayout'
          on-postlayout='HandlePostLayout'>
    
    <Content>
        <pdf:Label id='ReportDateLabel' />
        <pdf:ForEach id='DataRepeater'>
            <!-- Template content -->
        </pdf:ForEach>
    </Content>
    
</pdf:Page>
```

### Controller Reflection and Definition

**Controller definition is created via reflection in `ParserDefintionFactory`:**

```csharp
private static ParserControllerDefinition LoadControllerDefinition(string name, Type type)
{
    ParserControllerDefinition defn = new ParserControllerDefinition(name, type);
    
    // Fill outlets (properties and fields)
    FillControllerOutlets(defn);
    
    // Fill actions (methods)
    FillControllerActions(defn);
    
    return defn;
}

private static void FillControllerOutlets(ParserControllerDefinition defn)
{
    // Reflect properties
    PropertyInfo[] allprops = defn.ControllerType.GetProperties(
        BindingFlags.Public | BindingFlags.Instance);
    
    foreach (PropertyInfo aprop in allprops)
    {
        Attribute found = System.Attribute.GetCustomAttribute(aprop, typeof(PDFOutletAttribute), true);
        if (found != null)
        {
            PDFOutletAttribute outletAttr = (PDFOutletAttribute)found;
            if (outletAttr.IsOutlet)
            {
                ParserControllerOutlet outlet = new ParserControllerOutlet(
                    aprop, 
                    outletAttr.ComponentID, 
                    outletAttr.Required);
                
                if (defn.Outlets.Contains(outlet.ID))
                    throw new PDFParserException(
                        $"Controller {defn.ControllerTypeName} already has outlet with ID {outlet.ID}");
                
                defn.Outlets.Add(outlet);
            }
        }
    }
    
    // Reflect fields
    FieldInfo[] allfields = defn.ControllerType.GetFields(
        BindingFlags.Public | BindingFlags.Instance);
    
    foreach (FieldInfo afield in allfields)
    {
        Attribute found = System.Attribute.GetCustomAttribute(afield, typeof(PDFOutletAttribute), true);
        if (found != null)
        {
            PDFOutletAttribute outletAttr = (PDFOutletAttribute)found;
            if (outletAttr.IsOutlet)
            {
                ParserControllerOutlet outlet = new ParserControllerOutlet(
                    afield, 
                    outletAttr.ComponentID, 
                    outletAttr.Required);
                
                defn.Outlets.Add(outlet);
            }
        }
    }
}
```

### Controller Specification

Controllers are specified in three ways:

#### 1. Processing Instruction (Document-level)

```xml
<?xml version='1.0' encoding='utf-8' ?>
<?scryber controller='MyNamespace.MyController, MyAssembly' ?>
<pdf:Document xmlns:pdf="...">
    <!-- Document content -->
</pdf:Document>
```

#### 2. Programmatic (Code-level)

```csharp
var settings = new ParserSettings(/* ... */);
settings.ControllerType = typeof(MyController);
// OR
settings.Controller = new MyController();

var doc = Document.ParseDocument(stream, ParseSourceType.DynamicContent, settings);
```

#### 3. Attribute (Component-level)

```csharp
[PDFController(typeof(MyController))]
public class CustomDocument : Document
{
    // ...
}
```

### Complete Controller Example

**Controller class:**

```csharp
using Scryber;
using Scryber.Components;
using Scryber.Data;

namespace MyCompany.Reports
{
    public class SalesReportController
    {
        // Outlets - assigned during parsing
        [PDFOutlet(Required = true)]
        public Label CompanyNameLabel { get; set; }
        
        [PDFOutlet(ComponentID = "report-title")]
        public Label TitleLabel { get; set; }
        
        [PDFOutlet(Required = true)]
        public ForEach SalesDataRepeater { get; set; }
        
        [PDFOutlet]
        public Label TotalSalesLabel { get; set; }
        
        [PDFOutlet]
        public Panel NoDataPanel { get; set; }
        
        // Controller state
        private List<SalesRecord> _salesData;
        private decimal _totalSales;

        // Action: Initialize report
        public void InitReport(InitContext context)
        {
            context.TraceLog.Add(TraceLevel.Message, "SalesReport", "Initializing sales report");
            
            CompanyNameLabel.Text = "Acme Corporation";
            TitleLabel.Text = "Monthly Sales Report";
            TitleLabel.StyleClass = "report-header";
        }

        // Action: Load data
        public void LoadReportData(LoadContext context)
        {
            context.TraceLog.Add(TraceLevel.Message, "SalesReport", "Loading sales data");
            
            // Load data from database/API
            _salesData = FetchSalesData();
            _totalSales = _salesData.Sum(s => s.Amount);
            
            // Bind to repeater
            SalesDataRepeater.DataSource = _salesData;
            SalesDataRepeater.Value = _salesData;
            
            // Set total
            TotalSalesLabel.Text = _totalSales.ToString("C");
            
            // Show/hide no-data message
            NoDataPanel.Visible = (_salesData.Count == 0);
        }

        // Action: Pre-layout modifications
        public void BeforeLayout(LayoutContext context)
        {
            if (_salesData.Count > 100)
            {
                context.TraceLog.Add(TraceLevel.Warning, "SalesReport", 
                    "Large dataset may cause performance issues");
            }
        }

        // Action: Post-layout inspection
        public void AfterLayout(LayoutContext context)
        {
            var pageCount = context.DocumentLayout.AllPages.Count;
            context.TraceLog.Add(TraceLevel.Message, "SalesReport", 
                $"Report generated: {pageCount} pages, {_salesData.Count} records, total ${_totalSales:N2}");
        }

        private List<SalesRecord> FetchSalesData()
        {
            // Database query
            return new List<SalesRecord>
            {
                new SalesRecord { Product = "Widget", Amount = 1250.00m },
                new SalesRecord { Product = "Gadget", Amount = 2100.50m },
                // ...
            };
        }
    }

    public class SalesRecord
    {
        public string Product { get; set; }
        public decimal Amount { get; set; }
        public DateTime Date { get; set; }
    }
}
```

**Template XML:**

```xml
<?xml version='1.0' encoding='utf-8' ?>
<?scryber controller='MyCompany.Reports.SalesReportController, MyCompany.Reports' ?>

<pdf:Document xmlns:pdf='http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Components.xsd'>
    
    <Pages>
        <pdf:Page on-init='InitReport' 
                  on-load='LoadReportData'
                  on-prelayout='BeforeLayout'
                  on-postlayout='AfterLayout'>
            
            <Header>
                <pdf:Label id='CompanyNameLabel' />
                <pdf:Label id='report-title' />
            </Header>
            
            <Content>
                
                <!-- Data display -->
                <pdf:TableGrid>
                    <pdf:TableHeaderRow>
                        <pdf:TableHeaderCell>Product</pdf:TableHeaderCell>
                        <pdf:TableHeaderCell>Amount</pdf:TableHeaderCell>
                    </pdf:TableHeaderRow>
                    
                    <pdf:TableRow>
                        <pdf:ForEach id='SalesDataRepeater' value='.'>
                            <pdf:TableCell>
                                <pdf:Label text='{@:Product}' />
                            </pdf:TableCell>
                            <pdf:TableCell>
                                <pdf:Label text='{@:Amount}' />
                            </pdf:TableCell>
                        </pdf:ForEach>
                    </pdf:TableRow>
                </pdf:TableGrid>
                
                <!-- Total -->
                <pdf:Div>
                    <pdf:Label text='Total Sales: ' />
                    <pdf:Label id='TotalSalesLabel' />
                </pdf:Div>
                
                <!-- No data message -->
                <pdf:Panel id='NoDataPanel' visible='false'>
                    <pdf:Label text='No sales data available for this period.' />
                </pdf:Panel>
                
            </Content>
            
        </pdf:Page>
    </Pages>
    
</pdf:Document>
```

**Usage:**

```csharp
using (var reader = new StreamReader("SalesReport.pdfx"))
{
    var doc = Document.ParseDocument(reader, ParseSourceType.DynamicContent);
    doc.ProcessDocument("SalesReport.pdf");
}
```

---

## Custom Component Development

Creating custom components allows extending Scryber with domain-specific functionality, reusable widgets, and specialized layout behaviors.

### Complete Custom Component Example

This example demonstrates creating a custom "StatCard" component with its own namespace, controller integration, and full lifecycle implementation.

#### Step 1: Create Component Class

```csharp
using System;
using Scryber;
using Scryber.Components;
using Scryber.Drawing;
using Scryber.Styles;
using Scryber.Generation;

namespace MyCompany.PDFComponents
{
    /// <summary>
    /// A statistic display card with icon, value, label, and trend indicator
    /// </summary>
    [PDFParsableComponent("StatCard")]
    [PDFJSConvertor("mycompany.convertors.stat_card")]
    public class StatCard : Panel
    {
        #region Properties

        [PDFAttribute("icon")]
        public string Icon { get; set; }

        [PDFAttribute("value")] 
        public string Value { get; set; }

        [PDFAttribute("label")]
        public string Label { get; set; }

        [PDFAttribute("trend")]
        public decimal? Trend { get; set; }

        [PDFAttribute("card-color")]
        public Color CardColor { get; set; }

        [PDFElement("Header")]
        public Component Header { get; set; }

        [PDFElement("Footer")]
        public Component Footer { get; set; }

        #endregion

        #region Constructor

        public StatCard()
            : base(ObjectTypes.Panel)
        {
            // Default styling
            CardColor = new Color(240, 240, 245);
        }

        #endregion

        #region Lifecycle

        protected override void OnInit(InitContext context)
        {
            base.OnInit(context);
            
            // Build internal structure
            BuildCardLayout();
        }

        protected override void OnDataBound(DataBindContext context)
        {
            base.OnDataBound(context);
            
            // Update values from data context
            if (context.DataStack.HasData)
            {
                var data = context.DataStack.Current;
                // Auto-bind if data object has matching properties
            }
        }

        #endregion

        #region Layout Construction

        private void BuildCardLayout()
        {
            // Clear existing content
            this.Contents.Clear();

            // Card container styling
            this.Style.Background.Color = CardColor;
            this.Style.Border.Width = 1;
            this.Style.Border.Color = new Color(220, 220, 220);
            this.Style.Border.CornerRadius = 4;
            this.Style.Padding.All = 12;

            // Header section (if provided)
            if (Header != null)
            {
                var headerContainer = new Div();
                headerContainer.Style.Margins.Bottom = 8;
                headerContainer.Contents.Add(Header);
                this.Contents.Add(headerContainer);
            }

            // Icon  section
            if (!string.IsNullOrEmpty(Icon))
            {
                var iconLabel = new Label();
                iconLabel.Text = Icon;
                iconLabel.Style.Font.Size = 24;
                iconLabel.Style.Fill.Color = StandardColors.Gray;
                this.Contents.Add(iconLabel);
            }

            // Value section
            if (!string.IsNullOrEmpty(Value))
            {
                var valueLabel = new Label();
                valueLabel.Text = Value;
                valueLabel.Style.Font.FontSize = 32;
                valueLabel.Style.Font.FontBold = true;
                valueLabel.Style.Fill.Color = StandardColors.Black;
                valueLabel.Style.Margins.Top = 4;
                this.Contents.Add(valueLabel);
            }

            // Label section
            if (!string.IsNullOrEmpty(Label))
            {
                var labelText = new Label();
                labelText.Text = Label;
                labelText.Style.Font.FontSize = 12;
                labelText.Style.Fill.Color = StandardColors.Gray;
                labelText.Style.Margins.Top = 4;
                this.Contents.Add(labelText);
            }

            // Trend indicator
            if (Trend.HasValue)
            {
                var trendLabel = new Label();
                var trendValue = Trend.Value;
                var trendText = (trendValue >= 0 ? "▲ +" : "▼ ") + trendValue.ToString("F1") + "%";
                
                trendLabel.Text = trendText;
                trendLabel.Style.Font.FontSize = 10;
                trendLabel.Style.Fill.Color = trendValue >= 0 
                    ? new Color(34, 139, 34)  // Green
                    : new Color(220, 20, 60);  // Red
                trendLabel.Style.Margins.Top = 4;
                this.Contents.Add(trendLabel);
            }

            // Footer section (if provided)
            if (Footer != null)
            {
                var footerContainer = new Div();
                footerContainer.Style.Margins.Top = 8;
                footerContainer.Style.Border.Sides = Sides.Top;
                footerContainer.Style.Border.Width = 1;
                footerContainer.Style.Border.Color = new Color(220, 220, 220);
                footerContainer.Style.Padding.Top = 8;
                footerContainer.Contents.Add(Footer);
                this.Contents.Add(footerContainer);
            }
        }

        #endregion
    }
}
```

#### Step 2: Register Namespace

**In `scrybersettings.json`:**

```json
{
  "Scryber": {
    "Parsing": {
      "Namespaces": [
        {
          "Source": "http://www.mycompany.com/schemas/pdf/components",
          "Namespace": "MyCompany.PDFComponents",
          "Assembly": "MyCompany.PDFComponents, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
        }
      ]
    }
  }
}
```

#### Step 3: Create Controller (Optional)

```csharp
using Scryber;
using Scryber.Components;
using MyCompany.PDFComponents;

namespace MyCompany.Reports
{
    public class DashboardController
    {
        [PDFOutlet(Required = true)]
        public StatCard SalesCard { get; set; }
        
        [PDFOutlet(ComponentID = "revenue-card")]
        public StatCard RevenueCard { get; set; }
        
        [PDFOutlet(Required = true)]
        public StatCard CustomersCard { get; set; }

        public void LoadDashboardData(LoadContext context)
        {
            // Fetch dashboard metrics
            var metrics = FetchMetrics();

            // Update cards
            SalesCard.Value = metrics.Sales.ToString("N0");
            SalesCard.Trend = metrics.SalesTrend;

            RevenueCard.Value = "$" + metrics.Revenue.ToString("N0");
            RevenueCard.Trend = metrics.RevenueTrend;

            CustomersCard.Value = metrics.Customers.ToString("N0");
            CustomersCard.Trend = metrics.CustomersTrend;
        }

        private DashboardMetrics FetchMetrics()
        {
            // Database or API call
            return new DashboardMetrics
            {
                Sales = 1234,
                SalesTrend = 12.5m,
                Revenue = 98765,
                RevenueTrend = -3.2m,
                Customers = 456,
                CustomersTrend = 8.1m
            };
        }
    }

    public class DashboardMetrics
    {
        public int Sales { get; set; }
        public decimal SalesTrend { get; set; }
        public decimal Revenue { get; set; }
        public decimal RevenueTrend { get; set; }
        public int Customers { get; set; }
        public decimal CustomersTrend { get; set; }
    }
}
```

#### Step 4: Use in Template

```xml
<?xml version='1.0' encoding='utf-8' ?>
<?scryber controller='MyCompany.Reports.DashboardController, MyCompany.Reports' ?>

<pdf:Document xmlns:pdf='http://www.scryber.co.uk/schemas/core/release/v1/Scryber.Components.xsd'
              xmlns:mc='http://www.mycompany.com/schemas/pdf/components'>
    
    <Pages>
        <pdf:Page on-load='LoadDashboardData'>
            <Content>
                
                <pdf:H1>Dashboard</pdf:H1>
                
                <!-- Using custom StatCard components -->
                <pdf:Div class='card-container'>
                    
                    <mc:StatCard id='SalesCard'
                                 icon='📈'
                                 value='0'
                                 label='Total Sales'
                                 card-color='#E3F2FD'>
                        <mc:Footer>
                            <pdf:Label text='Updated today' />
                        </mc:Footer>
                    </mc:StatCard>
                    
                    <mc:StatCard id='revenue-card'
                                 icon='💰'
                                 value='$0'
                                 label='Revenue'
                                 card-color='#F1F8E9'>
                        <mc:Footer>
                            <pdf:Label text='Last 30 days' />
                        </mc:Footer>
                    </mc:StatCard>
                    
                    <mc:StatCard id='CustomersCard'
                                 icon='👥'
                                 value='0'
                                 label='Active Customers'
                                 card-color='#FFF3E0'>
                        <mc:Footer>
                            <pdf:Label text='This month' />
                        </mc:Footer>
                    </mc:StatCard>
                    
                </pdf:Div>
                
            </Content>
        </pdf:Page>
    </Pages>
    
</pdf:Document>
```

#### Step 5: Generate PDF

```csharp
using System.IO;
using Scryber.Components;

namespace MyCompany.Reports
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var reader = new StreamReader("Dashboard.pdfx"))
            {
                var doc = Document.ParseDocument(reader, ParseSourceType.DynamicContent);
                doc.ProcessDocument("Dashboard.pdf");
            }
        }
    }
}
```

### Component Attribute Reference

#### Component-Level Attributes

| Attribute | Purpose | Required | Example |
|-----------|---------|----------|---------|
| `[PDFParsableComponent]` | Marks class as parsable, specifies XML element name | Yes | `[PDFParsableComponent("StatCard")]` |
| `[PDFRemoteParsableComponent]` | Specifies remote reference variant | No | `[PDFRemoteParsableComponent("StatCard-Ref")]` |
| `[PDFJSConvertor]` | JavaScript convertor for design tools | No | `[PDFJSConvertor("mycompany.convertors.stat_card")]` |

#### Property Attributes

| Attribute | Purpose | Applied To | Example |
|-----------|---------|------------|---------|
| `[PDFAttribute]` | Simple XML attribute property | Scalar properties | `[PDFAttribute("icon")]` |
| `[PDFElement]` | Complex/nested element | Component properties | `[PDFElement("Header")]` |
| `[PDFArray]` | Collection of components | Collection properties | `[PDFArray(typeof(Component))]` |
| `[PDFTextValue]` | Inner text content | String properties | `[PDFTextValue]` |

### Component Base Classes

| Base Class | Use Case | Key Features |
|------------|----------|--------------|
| `Component` | Any component | Lifecycle events, ID, styling |
| `VisualComponent` | Renderable components | Position, size, visibility |
| `Panel` | Containers | Child component management |
| `PagedContainerComponent` | Multi-page containers | Page breaking, overflow |
| `DataComponent` | Data-bound components | Data context, expressions |

### Lifecycle Override Methods

```csharp
public class CustomComponent : Panel
{
    protected override void OnPreInit(InitContext context)
    {
        // Before initialization
        base.OnPreInit(context);
    }

    protected override void OnInit(InitContext context)
    {
        base.OnInit(context);
        // Component initialization
    }

    protected override void OnLoad(LoadContext context)
    {
        base.OnLoad(context);
        // Load data, prepare state
    }

    protected override void OnDataBinding(DataBindContext context)
    {
        base.OnDataBinding(context);
        // Before databinding
    }

    protected override void OnDataBound(DataBindContext context)
    {
        base.OnDataBound(context);
        // After databinding complete
    }

    protected override Style GetBaseStyle()
    {
        // Default styling for component
        var style = base.GetBaseStyle();
        style.Background.Color = StandardColors.White;
        return style;
    }

    protected override void DoBuildLayout(LayoutContext context, Rect totalBounds)
    {
        // Custom layout logic
        base.DoBuildLayout(context, totalBounds);
    }

    protected override void DoRender(RenderContext context)
    {
        // Custom PDF rendering
        base.DoRender(context);
    }
}
```

---

## Image Factory Configuration

Image factories load image data from various sources (files, URLs, data URLs, streams). The factory pattern allows custom image loaders.

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
| `MinimumScaleReduction` | double | Minimum scale factor before image downsampling (default 0.249) |
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

### Implementing Custom Image Factories

**Interface contract:**

```csharp
// Scryber.Drawing/_Interfaces.cs
public interface IPDFImageDataFactory
{
    bool ShouldCache { get; }
    
    ImageData LoadImageData(IDocument document, IComponent owner, string path);
    ImageData LoadImageData(IDocument document, IComponent owner, byte[] data, MimeType type);
}
```

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
        if (null != document && document is IResourceRequester resourceRequester)
        {
            // Use proxy for async remote loading
            return GetProxyImageData(document, resourceRequester, owner, path);
        }
        else
        {
            var data = this.DoLoadImageDataAsync(document, owner, path).Result;
            return data;
        }
    }
    
    protected abstract ImageData DoLoadRawImageData(IDocument document, IComponent owner, byte[] rawData, MimeType type);
    protected abstract Task<ImageData> DoLoadImageDataAsync(IDocument document, IComponent owner, string path);
}
```

**Example custom factory:**

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
