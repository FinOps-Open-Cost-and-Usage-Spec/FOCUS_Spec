# Corrections to Invoiced Billing Period

The following examples illustrate how corrections to previously issued billing periods may be represented in FOCUS Cost and Usage datasets, using delivery mechanisms and correction styles that preserve invoice integrity and auditability.

## Post-Invoice Correction Scenarios

### Scenario 1: Post-Invoice Correction - Partial Reallocation to Correct Resource

On July 12th, 2025, ACME Corp identified that a charge record previously invoiced for May 2025 was incorrectly attributed entirely to ResourceId `R-111`. In reality, only part of the cost and usage belonged to that resource, while the remainder pertained to ResourceId `R-222`.

To correct this misattribution, ACME Corp provisioned a reallocation correction using append-only mechanisms. The correction was realized either through a ledger-style adjustment, which redistributed the cost between resources using increment and decrement records, or through an accounting-style adjustment, which negated the original charge and introduced corrected records for each resource.

Correction records were assigned to the next open billing period to preserve invoice immutability and ensure completeness of cost reporting.

CSV Examples:

* [Original Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Ledger-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Accounting-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was invoiced and includes a charge record that was part of the finalized invoice for May 2025.
* The correction is modeled using append-only mechanisms, as the May billing period is closed and invoice immutability must be preserved.
* Correction records have ChargeClass set to "Correction", indicating they reallocate cost from a previously invoiced billing period.
* Original Dataset includes:
  * A charge record attributed entirely to ResourceId `R-111`.
* Ledger-style correction includes:
  * A decrement record for `R-111`, reducing the cost previously misattributed to that resource.
  * An increment record for `R-222`, assigning the corresponding portion of the cost to the correct resource.
* Accounting-style correction includes:
  * A negation record for the original charge.
  * A corrected record for `R-111`.
  * A corrected record for `R-222`.
* Replacement-style correction is not permitted, as modifying finalized records would violate audit and legal constraints.

### Scenario 2: Post-Invoice Correction - Late-arriving Usage

On July 12th, 2025, ACME Corp identified a cost that was incurred during May 2025 (ChargePeriodStart: `2025-05-01`) but was not included in the finalized invoice issued on June 12th, 2025. Since the May billing period was closed, the correction was delivered in the next open billing period (e.g., June or July).

To account for the previously omitted usage, ACME Corp provisioned a correction using append-only mechanisms. The correction was realized by introducing a single increment record in both ledger-style and accounting-style formats, representing the late-arriving cost and usage.

This record was assigned to the next open billing period to preserve invoice immutability and ensure completeness of cost reporting.

CSV Examples:

* [Ledger-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Accounting-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was invoiced.
* The late-arriving cost was incurred during May 2025 but was not captured in the original dataset and was therefore not reflected in the invoice for May 2025, issued on June 12th, 2025.
* The correction introduces a new charge record to account for this previously omitted cost.
* The correction is modeled using append-only mechanisms, as the original billing period is closed and invoice immutability must be preserved.
* The correction record is assigned to the next open billing period (e.g., June 2025).
* The correction record has ChargeClass set to "Correction", indicating it accounts for usage from a previously invoiced billing period.
* Both Ledger-style and Accounting-style corrections use a single increment record to represent the late-arriving usage and associated cost.
* Replacement-style correction is not permitted, as modifying finalized records would violate audit and legal constraints.

### Scenario 3: Post-Invoice Correction - Itemized Cost-only Correction

On July 12th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records related to a single SkuPriceId. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, ACME Corp provisioned a cost-only correction using append-only mechanisms. The correction was realized by introducing a single increment record in both ledger-style and accounting-style formats, representing the cost-only adjustment.

This record was assigned to the next open billing period to preserve invoice immutability and ensure completeness of cost reporting.

CSV Examples:

* [Ledger-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Accounting-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was invoiced.
* The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records related to a single SkuPriceId.
* The discrepancy was not captured in the original dataset and was therefore not reflected in the invoice for May 2025, issued on June 12th, 2025.
* The correction introduces a cost-only record to reconcile the total drift and ensure invoice accuracy.
* The correction is modeled using append-only mechanisms, as the original billing period is closed and invoice immutability must be preserved.
* The correction record is assigned to the next open billing period (e.g., July 2025).
* The correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously invoiced billing period.
* The correction is itemized and explicitly references the relevant SkuPriceId.
* Both Ledger-style and Accounting-style corrections use a single increment record to represent the cost-only adjustment.
* Replacement-style correction is not permitted, as modifying finalized records would violate audit and legal constraints.

### Scenario 4: Post-Invoice Correction - Bulk Cost-only Correction

On July 12th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records spanning several different SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, ACME Corp provisioned a bulk cost-only correction using append-only mechanisms. The correction was realized by introducing a single increment record in both ledger-style and accounting-style formats, representing the cost-only adjustment. Unlike itemized corrections, this bulk record did not specify a SkuPriceId, as the discrepancy spanned multiple SKU Price IDs.

This record was assigned to the next open billing period to preserve invoice immutability and ensure completeness of cost reporting.

CSV Examples:

* [Original Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Ledger-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)
* [Accounting-style Correction](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=620136225#gid=620136225)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was invoiced.
* The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records spanning several SkuPriceId values.
* The discrepancy was not captured in the original dataset and was therefore not reflected in the invoice for May 2025, issued on June 12th, 2025.
* The correction introduces a bulk cost-only record to reconcile the total drift and ensure invoice accuracy.
* The correction is modeled using append-only mechanisms, as the original billing period is closed and invoice immutability must be preserved.
* The correction record is assigned to the next open billing period (e.g., July 2025).
* The correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously invoiced billing period.
* The correction does not specify a SkuPriceId, as it spans multiple SKU Price IDs.
* Both Ledger-style and Accounting-style corrections use a single increment record to represent the cost-only adjustment.
* Replacement-style correction is not permitted, as modifying finalized records would violate audit and legal constraints.
