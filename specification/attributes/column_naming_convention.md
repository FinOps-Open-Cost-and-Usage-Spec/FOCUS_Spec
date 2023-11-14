# Column Naming Convention

Column IDs provided in cost data following a consistent naming convention reduces friction for FinOps practitioners that consume the data for analysis, reporting, and other use cases.

All columns defined in the FOCUS specification MUST follow the naming requirements listed below.

## Attribute ID

ColumnNamingConvention

## Attribute Name

Column Naming Convention

## Description

Naming convention for columns appearing in billing data.

## Requirements

* All columns defined by FOCUS MUST follow the following rules:
  * Column IDs MUST use [Pascal case](https://techterms.com/definition/pascalcase).
  * Column IDs MUST NOT use abbreviations.
  * Column IDs SHOULD NOT use acronyms.
  * Column IDs MUST be alphanumeric with no special characters.
  * Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID. Display Name for a Column MAY avoid the Name suffix if there are no other columns with the same name prefix.
* Custom (e.g., provider-defined) columns SHOULD follow the same rules as FOCUS columns listed above.
* Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID. Display Name for a Column MAY avoid the `Name` suffix if it is considered superfluous.
* Columns with the `Category` suffix must be normalized.
* All custom columns MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
* All FOCUS columns SHOULD be first in the provided dataset.
  * Custom columns SHOULD be listed after all FOCUS columns and SHOULD NOT be intermixed.
  * Columns MAY be sorted alphabetically but custom columns SHOULD be after all FOCUS columns.

## Exceptions

* Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.
* Product offerings that incur charges will use the "Sku" abbreviation because it is a well-understood term both within and outside the industry.

## Introduced (version)

0.5
