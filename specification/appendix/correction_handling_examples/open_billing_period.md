# Corrections to Open Billing Period

The following examples illustrate how corrections to open billing periods, including both current and previous open periods, may be represented in FOCUS Cost and Usage datasets, using various delivery mechanisms and correction styles.

Note: Corrections in this section apply to billing periods that are still open, whether current (Current Open-Period Correction Scenarios) or previous (Previous Open-Period Correction Scenarios). In the examples that follow, the InvoiceId column contains a provisional or placeholder value, even though the invoice has not yet been issued.

## Current Open-Period Correction Scenarios

### Scenario 1: Current Open-Period Correction - Partial Reallocation to Correct Resource

On July 12th, 2025, ACME Corp identified that a charge record for the current billing period (July 2025) was incorrectly attributed entirely to ResourceId `R-111`. In reality, only part of the cost and usage belonged to that resource, while the remainder pertained to ResourceId `R-222`.

Since the billing period was still open and the invoice had not yet been finalized, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To correct the misattribution, ACME Corp had the option to use any of the following approaches:

* Replacement style correction, which replaced the original record attributed to R-111 with a corrected version, and introduced a new record for `R-222` to reflect the accurate resource attribution.
* Delta style correction, which used a decrement to reduce the cost from the incorrectly attributed resource (`R-111`), and an increment to assign the cost to the correct resource (`R-222`).
* Ledger style correction, which negated the original charge and introduced two new records (one for each resource) accurately reflecting the corrected cost and usage distribution.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)

Note the following details in the example dataset:

* The correction is modeled using either Overwrite or Append mechanisms, as the billing period is still open and invoice has not yet been issued.
* Original Dataset includes:
  * A charge record attributed entirely to ResourceId `R-111`.
* Replacement style correction includes:
  * A replacement of the original record to reflect the corrected portion for `R-111`.
  * An additional record for `R-222` to account for the remaining portion of the cost and usage.
* Delta style correction includes:
  * A decrement record for `R-111`, reducing the cost previously misattributed to that resource.
  * An increment record for `R-222`, assigning the corresponding portion of the cost to the correct resource.
* Ledger style correction includes:
  * A reversal record for the original charge.
  * A corrected record for `R-111`.
  * A corrected record for `R-222`.
* Each correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
* Each correction record is assigned to the current billing period (July 2025).

### Scenario 2: Current Open-Period Correction - Late-arriving Usage

On July 12th, 2025, ACME Corp identified a cost incurred during the current billing period (ChargePeriodStart: `2025-07-01`) that was not included in the initial dataset.

Since the billing period was still open and the invoice had not yet been finalized, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To account for the previously omitted usage, ACME Corp had the option to use either Overwrite or Append mechanisms, i.e.:

* Replacement style correction
* Delta style correction
* Ledger style correction

Regardless of the correction style used, the correction was realized by introducing a single increment record representing the late-arriving usage and associated cost.

CSV Examples:

* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)

Note the following details in the example datasets:

* The original dataset was incomplete and did not capture late-arriving usage and associated cost for July 2025.
* The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
* All three correction styles (Replacement, Delta, and Ledger) introduce a single increment record representing the previously omitted usage and associated cost.
* The correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
* The correction record is assigned to the current billing period (July 2025).

### Scenario 3: Current Open-Period Correction - Itemized Cost-only Corrections

On July 12th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple records spanning two distinct SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in small drifts.

Since the billing period was still open and the invoice had not yet been finalized, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To reconcile this discrepancy, ACME Corp had the option to use either Overwrite or Append mechanisms, i.e.:

* Replacement style correction
* Delta style correction
* Ledger style correction

Regardless of the correction style used, the correction was realized by introducing two itemized increment records, each representing a cost-only adjustment for one of the affected SkuPriceId values. Unlike bulk corrections, which consolidate adjustments into a single record without specifying a SkuPriceId, this approach explicitly itemizes the correction per SkuPriceId.

Compared to the bulk correction approach, this method ensures transparency and traceability and is preferred when itemized correction is feasible.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)

Note the following details in the example datasets:

* The original dataset was complete in terms of usage, but a minor cost discrepancy was identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
* The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
* All three correction styles (Replacement, Delta, and Ledger) introduce two itemized increment records representing cost-only adjustments.
* Each correction record explicitly references the affected SkuPriceId.
* Each correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
* Each correction record has ChargeCategory set to "Adjustment", which is the only valid value when both PricingQuantity and ChargeClass are null, due to the normative requirement that PricingQuantity must not be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
* Each correction record is assigned to the current billing period (July 2025).

### Scenario 4: Current Open-Period Correction - Bulk Cost-only Correction

On July 12th, 2025, ACME Corp detected a minor cost discrepancy caused by accumulated rounding differences across multiple records spanning two distinct SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in small drifts.

Since the billing period was still open and the invoice had not yet been finalized, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To reconcile this discrepancy, ACME Corp had the option to use either Overwrite or Append mechanisms, i.e.:

* Replacement style correction
* Delta style correction
* Ledger style correction

Regardless of the correction style used, the correction was realized by introducing a single increment record representing the bulk cost-only adjustment. Unlike itemized corrections, this record did not specify a SkuPriceId, as the discrepancy spanned multiple SKU Price IDs.

Compared to the itemized correction approach, this method sacrifices transparency and traceability, but is suitable when itemized correction is not feasible.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)

Note the following details in the example datasets:

* The original dataset was complete in terms of usage, but a minor cost discrepancy was identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
* The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
* All three correction styles (Replacement, Delta, and Ledger) introduce a single increment record representing the bulk cost-only adjustment to reconcile the total drift.
* The correction record does not specify a SkuPriceId, as it spans multiple SKU Price IDs.
* The correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
* The correction record has ChargeCategory set to "Adjustment", which is the only valid value when both PricingQuantity and ChargeClass are null, due to the normative requirement that PricingQuantity must not be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
* The correction record is assigned to the current billing period (July 2025).

## Previous Open-Period Correction Scenarios

### Scenario 1: Previous Open-Period Correction - Partial Reallocation to Correct Resource

This scenario is nearly identical to *Scenario 1: Current Open-Period Correction - Partial Reallocation to Correct Resource*. The only difference is that the original misattributed charge occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Replacement Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)

### Scenario 2: Previous Open-Period Correction - Late-arriving Usage

This scenario is nearly identical to *Scenario 2: Current Open-Period Correction - Late-arriving Usage*. The only difference is that the late-arriving usage pertains to the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)

### Scenario 3: Previous Open-Period Correction - Itemized Cost-only Corrections

This scenario is nearly identical to *Scenario 3: Current Open-Period Correction - Itemized Cost-only Adjustments*. The only difference is that the original cost discrepancy occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)

### Scenario 4: Previous Open-Period Correction - Bulk Cost-only Corrections

This scenario is nearly identical to *Scenario 4: Current Open-Period Correction - Bulk Cost-only Adjustments*. The only difference is that the original cost discrepancy occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

* [Original Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Replacement Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Delta Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
* [Ledger Dataset Artifact](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=957542531#gid=957542531)
