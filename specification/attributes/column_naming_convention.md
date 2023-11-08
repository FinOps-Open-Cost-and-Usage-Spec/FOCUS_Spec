# Column Naming Convention

Column IDs provided in cost data follow a consistent naming convention to reduce friction for FinOps practitioners. Custom columns are prefixed with a vendor-specific string to indicate the source of the column, distinguish them from FOCUS columns, and avoid conflicts in future releases.

All columns included in a FOCUS dataset MUST follow the naming requirements listed below.

## Attribute ID

ColumnNamingConvention

## Attribute Name

Column Naming Convention

## Description

Naming convention for columns appearing in billing data.

## Requirements

- All columns defined by FOCUS MUST follow the following rules:
  - Column IDs MUST use [Pascal case](https://techterms.com/definition/pascalcase).
  - Column IDs MUST NOT use abbreviations.
  - Column IDs SHOULD NOT use acronyms.
  - Column IDs MUST be alphanumeric with no special characters.
  - Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID. Display Name for a Column MAY avoid the `Name` suffix if there are no other columns with the same name prefix.
- Custom columns SHOULD follow the same rules as FOCUS columns listed above.
- All custom column IDs MUST start with a vendor prefix string and an underscore (e.g., `abc_ColumnName`).
  - Vendor prefixes MUST be lowercase, alphanumeric strings and SHOULD NOT be longer than 10 characters in length.
  - Vendor prefixes MUST be representative of the company or brand that generated the column.

## Exceptions

- Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.

## Introduced (version)

0.5
