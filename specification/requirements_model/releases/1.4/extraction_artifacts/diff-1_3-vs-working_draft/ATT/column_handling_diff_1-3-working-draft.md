## Diff

@@ -1,22 +1,17 @@
## Requirements

### Column Names

* All columns defined by FOCUS MUST follow the following rules:
  * Column IDs MUST use Pascal case.
  * Column IDs MUST NOT use abbreviations.
  * Column IDs MUST be alphanumeric with no special characters.
  * Column IDs SHOULD NOT use acronyms.
  * Column IDs SHOULD NOT exceed 50 characters to accommodate column length restrictions of various data repositories.
  * Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID.
  * Column display names MUST be consistent with their Column IDs, with spaces inserted between words (e.g., Column ID "BillingAccountName" and display name "Billing Account Name").
  * Columns with the `Category` suffix MUST be normalized.
* <a name="column_handling:custom-column"></a>Custom (e.g., service-provider-defined) columns that are not defined by FOCUS but included in a *FOCUS dataset* MUST follow the following rules:
  * Custom columns MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
  * Custom columns SHOULD follow the same rules listed above for FOCUS columns.
[-### Column Order-]

[-* All FOCUS columns SHOULD be first in the provided dataset.-]  * Custom columns [-SHOULD-]{+MUST+} be [-listed after all FOCUS columns-]{+detailed in publicly-available documentation, including description, purpose,+} and [-SHOULD NOT be intermixed.-]
[-* Columns MAY be sorted alphabetically, but custom columns SHOULD be after all FOCUS-]{+relationship to *native dataset*+} columns.
