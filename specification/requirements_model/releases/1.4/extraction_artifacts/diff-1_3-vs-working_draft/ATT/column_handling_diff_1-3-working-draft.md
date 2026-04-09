## Diff

* <a name="column_handling:custom-column"></a>Custom (e.g., service-provider-defined) columns that are not defined by FOCUS but included in a *FOCUS dataset* MUST follow the following rules:
  * Custom columns MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
  * Custom columns SHOULD follow the same rules listed above for FOCUS columns.
[-### Column Order-]

[-* All FOCUS columns SHOULD be first in the provided dataset.-]  * Custom columns [-SHOULD-]{+MUST+} be [-listed after all FOCUS columns-]{+detailed in publicly-available documentation, including description, purpose,+} and [-SHOULD NOT be intermixed.-]
[-* Columns MAY be sorted alphabetically, but custom columns SHOULD be after all FOCUS-]{+relationship to *native dataset*+} columns.
