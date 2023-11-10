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
  - Vendor prefixes MUST much match an entry in the Vendor Prefix List as defined in this appendix when an vendor organization is present therein.
  - Columns making use of a vendor prefix MUST be generated and managed by the Management Organization in the Vendor Prefix List.
  - Providers and managing organzition names SHOULD be listed in the Vendor Prefix List as defined in this appendix.
  - Managing organizations SHOULD public a specification document for custom columns including the vendor prefix, column name, and the version of the FOCUS specification each column is compatible with.

### Vendor Prefix List

The following table lists the vendor prefixes that are currently registered in the Vendor Prefix List as part of the FOCUS specification.

| Vendor Prefix | Provider Name         | Managing Organziation |
|:--------------|:----------------------|:----------------------|
| aws           | Amazon Web Services   | Amazon.com, Inc.      |
| azure         | Azure                 | Microsoft Corporation |
| gcp           | Google Cloud Platform | Google LLC            |
| ibm           | IBM Cloud             | IBM                   |
| oci           | Oracle Cloud          | Oracle Corporation    |

If a provider or organization is not listed in the Vendor Prefix List and a provider or organization is present in the billing data, the provider or organization SHOULD be added to the Vendor Prefix List as part of the FOCUS specification.  Vendors and organizations can public preliminary specifications for custom columns prior to being added to the Vendor Prefix List.  The Vendor Prefix List will be updated as part of the FOCUS specification release process.

Vendors and managing organizations can request a vendor prefix by submitting a pull request to the Vendor Prefix List in the FOCUS specification repository.  The pull request MUST include the following information:

- Vendor prefix
- Provider name
- Managing organization name
- Managing organization website URL
- Managing organization contact name
- Managing organization contact email address

## Exceptions

- Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.

## Introduced (version)

0.5
