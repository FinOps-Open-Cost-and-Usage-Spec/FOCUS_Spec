# Attributes

Attributes serve as reusable containers for requirements that enforce consistency across FOCUS specification entities (e.g., datasets, columns, objects). Functioning as a governance layer, Attributes define the constraints -- such as naming conventions, data types, granularity, or recency -- that an entity must satisfy. By grouping these requirements, Attributes ensure that data from any origin can be processed via standard instructions, which is essential for accurately supporting [FinOps capabilities][FODOFC].

## Attribute List<!--SkipTOC-->

| Attribute | Description |
| :--- | :--- |
| [Column Handling](#attributes.columnhandling) | Defines naming and ordering conventions for columns appearing in a FOCUS dataset. |
| [Currency Format](#attributes.currencyformat) | Specifies rules and formatting requirements for currency columns. |
| [Data Generator-Calculated Split Cost Allocation Handling](#attributes.datagenerator-calculatedsplitcostallocationhandling) | Allows data generators to provide granular cost information based on specific documented methods. |
| [Date/Time Format](#attributes.date/timeformat) | Outlines rules and ISO 8601 formatting requirements for date and time information. |
| [Discount Handling](#attributes.discounthandling) | Indicates how to include and apply various types of discounts to usage charges or rows. |
| [JSON Object Format](#attributes.jsonobjectformat) | Defines rules for columns that convey data as complex, hierarchical serialized JSON strings. |
| [Invoice Handling](#attributes.invoicehandling) | Ensures all monetary charges on an invoice are represented in the dataset for reconciliation. |
| [Key-Value Format](#attributes.key-valueformat) | Provides formatting requirements for columns conveying data as simple key-value pairs. |
| [Null Handling](#attributes.nullhandling) | Standardizes how to represent columns that do not have a value using NULL. |
| [Numeric Format](#attributes.numericformat) | Establishes rules for numeric values to ensure clarity, accuracy, and ease of interpretation. |
| [String Handling](#attributes.stringhandling) | Sets requirements for string-capturing columns to foster data integrity and interoperability. |
| [Unit Format](#attributes.unitformat) | Standardizes the expression of measurement units for data size, count, time, and other dimensions. |
