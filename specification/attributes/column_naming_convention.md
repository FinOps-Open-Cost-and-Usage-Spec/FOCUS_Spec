# Column Naming Convention

Column IDs provided in cost data following a consistent naming convention reduces friction for FinOps practitioners
that consume the data for analysis, reporting, and other use cases.

All columns defined in the FOCUS specification MUST follow the naming requirements listed below. Provider generated columns SHOULD adopt these same naming requirements over time.

## Attribute ID

ColumnNamingConvention

## Attribute Name

Column Naming Convention

## Description

Naming convention for columns appearing in billing data.

## Requirements

* Column IDs MUST use [Pascal case](https://techterms.com/definition/pascalcase).
* Column IDs MUST NOT use abbreviations.
* Column IDs SHOULD NOT use acronyms.
* Column IDs MUST be alphanumeric with no special characters.
* Columns that have an ID and a Name MUST have the Id or Name suffix in the Column ID. Display Name for a Column MAY
  avoid the Name suffix if it is considered superfluous

## Exceptions

* Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.

## Introduced (version)

0.5
