# Corrections to Closed Billing Period

The following examples illustrate how corrections to previously closed billing periods may be represented in FOCUS Cost and Usage dataset artifacts, using delivery mechanisms and correction styles that preserve invoice integrity and auditability.

## Closed-Period Correction Scenarios

These scenarios address discrepancies related to charges from the May 2025 billing period after it was closed and invoiced by the issuer ACME Corp on June 8th, 2025. The discrepancies were identified on July 5th, 2025. At that time, the June 2025 billing period was still open.

### Billing Period Alignment

Corrections are applied to the open billing period rather than modifying the closed one. The ChargeClass is set to "Correction", and the BillingPeriodStart/End reflect the current open period (June). However, the ChargePeriodStart/End remain mapped to the original timeframe (May) to preserve the historical accuracy of when the cost was incurred.

### Correction Style

While the Overwrite mechanism is permissible when it doesn't impact issued invoices, ACME Corp defaults to the Append mechanism (Delta and Ledger styles) for all closed period corrections. This preference prioritizes auditability and traceability, ensuring that downstream consumers - particularly those managing chargeback - receive a clear, additive history of changes.

### Scenario 1: Closed-Period Correction - Partial Reallocation to Correct Resource

On July 5th, 2025, ACME Corp identified that a charge record previously invoiced for May 2025 was incorrectly attributed entirely to ResourceId `R-111`. In reality, only part of the cost and usage belonged to that resource, while the remainder pertained to ResourceId `R-222`.

To correct this misattribution, ACME Corp provisioned a reallocation correction using Append mechanisms. The correction was realized either through a Delta style correction, which redistributed the cost between resources using increment and decrement records, or through a Ledger style correction, which negated the original charge and introduced corrected records for each resource.

***Note:*** *Replacement (i.e., Overwrite delivery mechanism) could have been applied in this scenario because the reallocation would not affect invoice reconciliation and would not require additional invoices. However, ACME Corp chose Append to preserve traceability and auditability while ensuring that downstream processes, in particular chargeback, receive timely and accurate cost attribution.*

CSV Examples:

* [Original Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_1_partial_reallocation_original.csv)
* [Delta Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_1_partial_reallocation_delta.csv)
* [Ledger Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_1_partial_reallocation_ledger.csv)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was closed and includes a charge record that was part of the finalized invoice for May 2025.
* Correction records have ChargeClass set to "Correction", indicating they reallocate cost from a previously closed billing period.
* Original Dataset includes:
  * A charge record attributed entirely to ResourceId `R-111`.
* Delta style correction includes:
  * A decrement record for `R-111`, reducing the cost previously misattributed to that resource.
  * An increment record for `R-222`, assigning the corresponding portion of the cost to the correct resource.
* Ledger style correction includes:
  * A reversal record for the original charge.
  * A corrected record for `R-111`.
  * A corrected record for `R-222`.

### Scenario 2: Closed-Period Correction - Late-arriving Usage

On July 5th, 2025, ACME Corp identified a cost that was incurred during May 2025 (ChargePeriodStart: `2025-05-01`) but was not included in the finalized invoice issued on June 8th, 2025. Since the May billing period was closed, the correction was delivered in the next open billing period (e.g., June or July).

To account for the previously omitted usage, ACME Corp provisioned a correction using Append mechanisms. The correction was realized by introducing a single increment record in both Delta style correction and Ledger style correction formats, representing the late-arriving cost and usage.

CSV Examples:

* [Delta Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_2_late_arriving_usage_delta.csv)
* [Ledger Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_2_late_arriving_usage_ledger.csv)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was closed.
* The late-arriving cost was incurred during May 2025 but was not captured in the original dataset and was therefore not reflected in the invoice for May 2025, issued on June 8th, 2025.
* The correction introduces a new charge record to account for this previously omitted cost.
* The correction record is assigned to the next open billing period (e.g., June 2025).
* The correction record has ChargeClass set to "Correction", indicating it accounts for usage from a previously closed billing period.
* Both Delta style and Ledger style corrections use a single increment record to represent the late-arriving usage and associated cost.

### Scenario 3: Closed-Period Correction - Itemized Cost-only Correction

On July 5th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records spanning several different SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, ACME Corp provisioned a cost-only correction using Append mechanism. In both Delta style correction and Ledger style correction formats, the correction was realized by introducing two itemized increment records, each representing a cost-only adjustment for one of the affected SkuPriceId values. Unlike bulk corrections, which consolidate adjustments into a single record without specifying a SkuPriceId, this approach explicitly itemizes the correction per SkuPriceId. Compared to the bulk correction approach, this method ensures transparency and traceability and is preferred when itemized correction is feasible.

CSV Examples:

* [Original Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_3_itemized_cost_only_original.csv)
* [Delta Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_3_itemized_cost_only_delta.csv)
* [Ledger Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_3_itemized_cost_only_ledger.csv)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was closed.
* The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
* The discrepancies were not captured in the original dataset and therefore were not reflected in the invoice for May 2025, issued on June 8th, 2025.
* Both Delta style and Ledger style corrections introduce two itemized increment records representing cost-only adjustments.
* Each correction record is assigned to the next open billing period (e.g., July 2025).
* Each correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously closed billing period.
* Each correction record is itemized and explicitly references the relevant SkuPriceId.
* Each correction record has ChargeCategory set to "Adjustment". While in this case "Usage" might be more precise and is permitted (since ChargeClass is "Correction"), "Adjustment" was selected to denote a cost-only correction due to a rounding error.

### Scenario 4: Closed-Period Correction - Bulk Cost-only Correction

On July 5th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records spanning several different SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, ACME Corp provisioned a bulk cost-only correction using Append mechanism. The correction was realized by introducing a single increment record in both Delta style correction and Ledger style correction formats, representing the bulk cost-only adjustment. Unlike itemized corrections, this bulk record did not specify a SkuPriceId, as the discrepancy spanned multiple SKU Price IDs.

CSV Examples:

* [Original Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_4_bulk_cost_only_original.csv)
* [Delta Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_4_bulk_cost_only_delta.csv)
* [Ledger Dataset Artifact](/specification/data/correction-handling-examples/closed-billing-period/scenario_4_bulk_cost_only_ledger.csv)

Note the following details in the example datasets:

* The original dataset was delivered before the billing period was closed.
* The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
* The discrepancies were not captured in the original dataset and therefore were not reflected in the invoice for May 2025, issued on June 8th, 2025.
* Both Delta style and Ledger style corrections introduce a bulk cost-only record to reconcile the total drift and ensure invoice accuracy.
* The correction record is assigned to the next open billing period (e.g., July 2025).
* The correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously closed billing period.
* The correction record does not specify a SkuPriceId, as it spans multiple SKU Price IDs.
* The correction record has ChargeCategory set to "Adjustment". While in this case "Usage" might be more precise and is permitted (since ChargeClass is "Correction"), "Adjustment" was selected to denote a cost-only correction due to a rounding error.
