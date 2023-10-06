# Product Categorization

Product Categorization is a set of dimensions used to categorize products into a hierarchy of categories, groups, families, classes, lines, and types.  The product categorization dimensions are used to identify the product being purchased or used and to group products together for analysis and reporting.

* The first two levels of product categorization dimensions, Product Category and Product Group, are both required and normalized across providers to ensure consistency and comparability across providers.  
* Product Family is a required field with a requirement for normalization across different providers.  
* Product Class and Product Line are optional fields that are not required with no requirement for normalization across providers.
* Product Type is a mandatory dimension identifying the specific item within a product line, class, or family that a particular line item references.  Product Type is a provider-defined value, with no requirements for normalization across providers.

The following table outlines the level and dimension names alongside normalization requirements and descriptions for each dimension.

| Level | Dimension | Normalized Values | Required | Description |
| ----- | --------- | ----------------- | -------- | ----------- |
| Category | ProductCategory | Yes | Yes | Product Category is the highest-level classification of a product that can be used or purchased. |
| Group | ProductGroup | Yes | Yes | Product Group is the second highest-level classification of a product that can be used or purchased within a Product Category. |
| Family | ProductFamily | No | Yes | A Product Family is the third level of classification of a product that can be used or purchased within a Product Category and Product Group. |
| Class | ProductClass | No | No | Product Class is the fourth level of classification of a product just below Product Family. |
| Line | ProductLine | No | No | A Product Line is a specific set of items within a Product Family or Product Class that have the same attributes and product details. |
| Type | ProductType | Yes | Yes | A Product Type is an item within a Product Line, Product Class, or Product Family that has the same attributes and product details. |
