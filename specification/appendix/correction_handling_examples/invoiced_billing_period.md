# Corrections to Invoiced Billing Period

The following examples illustrate how corrections to previously issued billing periods may be represented in FOCUS Cost and Usage datasets, using delivery mechanisms and correction styles that preserve invoice integrity and auditability.

## Scenario 1: Post-Invoice Correction - Partial Reallocation to Correct Resource

On July 12th, 2025, the Data Generator identifies that a charge record previously invoiced for May 2025 was incorrectly attributed entirely to ResourceId R-111. In reality, only part of the cost and usage belongs to that resource, while the remainder pertains to ResourceId R-222.

To correct this misattribution, the Data Generator provisions a reallocation correction using append-only mechanisms. The correction is realized either through a ledger-style adjustment, which redistributes the cost between resources using increment and decrement records, or through an accounting-style adjustment, which negates the original charge and introduces corrected records for each resource.

Correction records are assigned to the next open billing period to preserve invoice immutability and ensure completeness of cost reporting.

CSV Examples:

* [Original Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Ledger-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Accounting-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was invoiced and includes a charge record that was part of the finalized invoice for May 2025.
* The correction is modeled using append-only mechanisms, as the May billing period is closed and invoice immutability must be preserved.
* Original Dataset includes:
  * A charge record attributed entirely to ResourceId R-111
* Ledger-style correction includes:
  * A decrement record for R-111
  * An increment record for R-222
* Accounting-style correction includes:
  * A negation record for the original charge
  * A corrected record for R-111
  * A corrected record for R-222
* Replacement-style correction is not permitted, as modifying finalized records would violate audit and legal constraints.
