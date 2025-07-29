# Correction Handling Examples

## Proposals

### Prevent Restatement After Invoice Finalization (and Billing Period Closure)

> **TODO:** Mention/address in upcoming Correction Handling attribute

***Note:*** *See S-1: Itemized Correction Scenarios with Cost Calculation Integrity Respected - S-1.1 and S-1.2 in particular*

We should prevent the use of the Restatement provisioning style once an invoice has been finalized and the corresponding billing period closed.

Since Restatement relies on overwriting or replacing previously delivered charge records within the original billing period, it inherently conflicts with the Normative Requirements for Post-Invoice Finalization Corrections — and in particular the Legal and Procedural Perspective, which states that once an invoice has been finalized and the corresponding billing period closed:

- A finalized invoice is considered legally issued and immutable.
- The associated billing period is closed, prohibiting any modifications or overwriting of previously delivered records.

Therefore, only non-restating provisioning styles (such as ledger-style increments/decrements or accounting-style reversals followed by corrected entries) should be permitted for handling Post-Invoice Finalization Corrections.

**Exceptions:**

- Contributors are encouraged to document any exception to the general rule.

- Should we allow restating in cases where corrections apply to dimensions that were not included in the original invoice?
Personally, I would prefer not to allow this — but this is currently the only scenario where I can see a possible justification.

#### Normative Requirements for Post-Invoice Finalization Corrections

> **TODO:** Mention/address in upcoming Correction Handling attribute
> (Shawn has added numbers to the statements that would become normative requirements in the attribute)

The following applies to all corrections to a previously closed billing period, i.e., correction charge records provisioned after invoice finalization and billing period closure, but which pertain to activity that occurred during that already invoiced and closed period:

- **Legal and Procedural Perspective:**
  - <<1>> The invoice is considered legally issued and immutable.
  - The billing period is considered closed, thereby prohibiting any modifications to or overwriting of the originally invoiced records.

- **Provisioning perspective**: `x_ExportDateTime = T2` (i.e., the date it became available to the consumer)

- **Operational Perspective**: All Correction records (Increments and Decrements in case of the Ledger style, Negations and Corrected records in case of Accounting style) pertain to activity that occurred in **May**, so in case of Usage records <<2>> `ChargePeriodStart`/`ChargePeriodEnd` **must reflect the actual usage period** (e.g., `ChargePeriodStart = 2025-05-01`)

- **Financial Perspective**: The original invoice (e.g., `INV-20250501-20250601`) has already been finalized (issued and sent e.g., as PDF). The May billing period is **considered closed** therefore
  - <<3>> `BillingPeriodStart`/`BillingPeriodEnd` **must be equal to or later than** the first **open** billing period (i.e., June 2025 or later)
  - <<4>> `InvoiceId` must not match the original invoice (e.g., `INV-20250501-20250601`).

- **Charge Class:** <<5>> ChargeClass must be set to "Correction".

### Enforce Nullability When `SkuPriceId` Is Null

> **TODO:** Address this in the respective Column Definitions (Normative Requirements sections), assuming consensus is reached.

#### Current Nullability Behavior for SKU/SKU Price-dependent columns

The following columns are considered SKU Price-dependent in FOCUS version 1.2:

- `SKU ID`
- `Pricing Quantity`
- `Pricing Category`
- `Contracted Unit Price`
- `List Unit Price`
- `Pricing Currency Contracted Unit Price`
- `Pricing Currency List Unit Price`
- `Consumed Quantity`
- `Commitment Discount Quantity`

Based on the analysis of current nullability requirements, all listed SKU Price-dependent columns (except `Consumed Quantity` and `Commitment Discount Quantity`) currently follow this pattern:

> - `<ColumnId>` nullability is defined as follows:  
>   - `<ColumnId>` MUST be null when [`ChargeCategory`](#chargecategory) is `"Tax"`.  
>   - `<ColumnId>` MUST NOT be null when `ChargeCategory` is `"Usage"` or `"Purchase"` and [`ChargeClass`](#chargeclass) is not `"Correction"`.  
>   - `<ColumnId>` MAY be null in all other cases.

As a result, under the current rules, these columns can be populated even when the corresponding `SkuPriceId` (or `SkuId`) is not known, specifically in the following cases:

- `ChargeCategory: Adjustment` or `Credit`
- `ChargeCategory: Usage` or `Purchase` with `ChargeClass: Correction`

***Note:*** *Although `Consumed Quantity` and `Commitment Discount Quantity` follow a slightly different nullability pattern, they are also currently allowed to hold values even when `SkuPriceId` is not provided.*

#### Proposal: Enforce Nulls in Price-Dependent Columns When SkuPriceId Is Null

Values in SKU Price-dependent columns **lack business meaning unless the associated `SkuPriceId` (or `SkuId`) is known**.
We propose making these columns **strictly null when the SKU, i.e., SKU Price context is missing**, to ensure consistency and data integrity.

To achieve this, we suggest updating the **nullability** section of each relevant column as follows:

> - `<ColumnId>` nullability is defined as follows:  
>   - `<ColumnId>` **MUST be null** when `SkuPriceId` is null.  
>   - ...

***Warning:*** *This applies beyond Correction Handling scenarios and may require a separate FR. It MUST be resolved comprehensively — addressing it solely within correction scenarios is not sufficient.*

### Refine Cost Calculation Integrity Norms and Permissible Discrepancies for Correction

In FOCUS 1.2, **Cost Calculation Integrity** and associated **discrepancy allowances for correction records** are addressed through specific normative requirements defined at the column level. While the exact phrasing may vary slightly across columns, the underlying logic is generally captured by the following two formulations:

- **Cost Calculation Integrity Requirement**  
  *The product of PricingQuantity and a unit price (e.g., ListUnitPrice) MUST match the corresponding cost metric (e.g., ListCost) when PricingQuantity is not null, the unit price is not null, and ChargeClass is not "Correction".*

  Currently specified for the following columns:

  - List Cost  
  - Contracted Cost  
  - List Unit Price  
  - Contracted Unit Price  
  - Pricing Quantity

- **Permissible Cost Calculation Integrity Discrepancy**  
  *Discrepancies in PricingQuantity, unit prices (e.g., ListUnitPrice), or costs (e.g., ListCost) MAY exist (and be handled independently) when ChargeClass is "Correction".*

  Currently specified for the following columns:

  - List Cost  
  - Contracted Cost  
  - List Unit Price  
  - Contracted Unit Price  
  - Pricing Quantity  
  - Pricing Currency List Unit Price  
  - Pricing Currency Contracted Unit Price

#### Proposal: Enforce Cost Calculation Integrity When All Three Metrics Are Provided (regardless of ChargeClass)

Revise the existing normative requirement to enforce Cost Calculation Integrity on all charge records (regardless of ChargeClass) if all three metrics are non-null.

***Current:***

> *The product of PricingQuantity and a unit price (e.g., ListUnitPrice) MUST match the corresponding cost metric (e.g., ListCost) when PricingQuantity is not null, the unit price is not null, and ChargeClass is not "Correction".*

**Recommended:**

> *The product of PricingQuantity and a unit price (e.g., ListUnitPrice) MUST match the corresponding cost metric (e.g., ListCost) when PricingQuantity is not null, the unit price is not null.*

**Exceptions?**

- At the time of writing, no valid use case has been identified where adjusting PricingQuantity without also adjusting Cost would be appropriate.
- If such a case exists or emerges, contributors are encouraged to document it explicitly here as an exception to the general rule. 

#### Proposal: Require Unit Prices When SkuPriceId Is Provided

Introduce new normative requirements specifying that Unit prices (e.g., ListUnitPrice, ContractedUnitPrice) MUST NOT be null be non-null If SkuPriceId is not null

**Rationale:** A non-null SkuPriceId implies a known pricing context, so the relevant unit prices should always be explicitly provided.

**Note:** Introducing this requirement will also help elegantly prevent unsupported PricingQuantity-only corrections, since such corrections would violate cost calculation integrity (i.e., Cost = UnitPrice × PricingQuantity) when all three values are present.

**Exceptions?**

- At the time of writing, no valid use case has been identified where adjusting PricingQuantity without also adjusting Cost would be appropriate.
- If such a case exists or emerges, contributors are encouraged to document it explicitly here as an exception to the general rule.

#### Proposal: Prevent PricingQuantity-only corrections

**Question:** Is it really necessary to allow corrections to Pricing Quantity only, without affecting Cost (ListCost and ContractedCost)?

**Note:** This applies specifically to `PricingQuantity` corrections, not to `ConsumedQuantity` or `CommitmentDiscountQuantity`.

**Explanation:**  
Given the formula `Cost = UnitPrice × PricingQuantity`, in the case of itemized corrections — where `SkuPriceId` is not null and `UnitPrice` is (or should be) known — adjusting `PricingQuantity` will inherently impact the corresponding `Cost`, since it is a derived value.

Therefore, when corrections are needed, they should be made either to both `PricingQuantity` and `Cost` together, or solely to `Cost`, depending on the use case — in accordance with Cost Calculation Integrity, which requires consistency with the formula `Cost = UnitPrice × PricingQuantity` when all three metrics are provided (i.e., non-null).

**Note:** If we adopt the two previous proposals — (1) Require Unit Prices when SkuPriceId is provided, and (2) Enforce Cost Calculation Integrity when all three metrics are present (regardless of ChargeClass) — the prevention of PricingQuantity-only correction scenarios will follow as a direct consequence.

**Exceptions?**

- At the time of writing, no valid use case has been identified where adjusting PricingQuantity without also adjusting Cost would be appropriate.
- If such a case exists or emerges, contributors are encouraged to document it explicitly here as an exception to the general rule. 

## Context

### ChargePeriod and BillingPeriod

> See [FR #1192: Refine Billing and Charge Period definitions](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1192)

- ChargePeriod denotes the effective period of the charge — i.e., when the underlying usage occurred.
- BillingPeriod represents the invoicing window to which the charge is financially assigned, regardless of when the usage took place.

### Export Date Time

> **TODO:** Add corresponding FR to backlog.

The FOCUS specification does not define how to determine when a charge record was provisioned.

To address this **gap** in the context of this scenarios, and solely for illustrative purposes, we introduce a custom helper column, `x_ExportDateTime`, to indicate when a charge record was delivered to the consumer.

### Incurred Date Time

> See [FR #1210: Provide ability to Identify the actual date/time when a charge was incurred](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1210)

The FOCUS specification does not include a column that explicitly captures when a charge was incurred.
Since the ChargePeriod is defined as "the time window for which a charge is effective", it does not necessarily reflect the actual time the charge was incurred.

In some cases — such as Usage records — ChargePeriodStart can serve as a proxy for the incurred date.
However, in other cases — such as Burn-Down Commitment Purchase records under a No Upfront Payment model — all installment records share the same ChargePeriodStart and ChargePeriodEnd. In such scenarios, only the first installment’s ChargePeriodStart typically reflects the actual time the charge was incurred, while the others do not.

To address this **gap** in the context of this scenarios, and solely for illustrative purposes, we introduce a custom helper column, `x_IncurredDateTime`, to indicate when a charge was incurred.

### Cost and Usage data Provisioning Styles

> **TODO:** Mention/address in upcoming Correction Handling attribute

Data Generators typically use two main provisioning styles/mechanisms when delivering cost and usage data:

- **Restatement:** Overwrites previously delivered records with updated ones. This approach ensures data accuracy by reflecting corrections directly in place.

- **Non-restating:** Delivers only new records without modifying previously sent data. This approach can be further divided into two subtypes:
  - **Ledger-style:** Adds incremental (or decremental) records over time. Corrections are reflected as additional entries where the cost or quantity metrics are adjusted (+/-), while all other dimensions remain identical to the original record. This supports an append-only model but offers limited auditability, as there is typically no explicit reversal.
  - **Accounting-style:** Tracks changes explicitly via negative (reversal) entries followed by corrected records. This ensures full auditability and provides a clear historical trail of adjustments.

### Finalized Invoice and Closed Billing Period

> **TODO:** Mention/address in upcoming Correction Handling attribute
> See [FR #Add invoice-level correction handling rules](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1013)

While the FOCUS specification mentions closed billing periods, it currently does not define the process for invoice issuance or billing period closure. It also does not define any explicit **“finalized”** status for invoices, nor a **“closed”** status for billing periods, nor the point at which an invoice is considered finalized or a billing period considered closed.

To address these **gaps** in this scenario, we assume the following:

- Data Generator (Providers) finalize invoices at some point, marking them as ready for invoice reconciliation.
- A billing period is considered closed once all invoices for that period are finalized.

***Note:** These information are assumed to be provided not within the cost and usage dataset itself, but in separate, adjacent datasets (e.g., invoice-related datasets).

## Use Case Scenarios

### Intro

- During May and early June, the Data Generator (e.g., CSP) delivers cost and usage data for the **May 2025 billing period** (`BillingPeriodStart = 2025-05-01`, `BillingPeriodEnd = 2025-06-01`).
- All cost records include an `InvoiceId` (e.g., `INV-20250501-20250601`), assigned **prior to invoice issuance**, in accordance with the normative guidance for `InvoiceId`.

---

### Timeline of Events

#### T0: 2025-06-12 - Invoice finalization (and Billing Period closure) on Data Generator's (Provider's) side

- The Data Generator has completed **initial provisioning** of all known cost and usage records that were incurred in May 2025 (`x_IncurredDateTime`), i.e., the working assumption at this point is that **all May costs have been delivered**.
- All charge records have `x_ExportDateTime` **earlier than T0**.
- The Data Generator performs internal **invoice reconciliation** and issues final invoices for the account for May 2025 (e.g., `INV-202505-202506`).
  - All Invoice related issues MUST be resoved at this point!
- All invoices for May are now finalized, and the Data Generator **closes** the May 2025 billing period.
- From the Data Generator's (Provider's) **financial perspective**, May 2025 is now complete.
  - Any charge records **provisioned on or after T0** (i.e., with `x_ExportDateTime ≥ T0`) **must** be assigned to an **open billing period** and therefore the earliest valid `BillingPeriodStart`/`BillingPeriodEnd` for such records is **June 2025**.

---

#### T1: 2025-06-13 - Invoice finalization (and Billing Period closure) on Consumer's side

- Since the Data Generator (Provider) has finalized the invoice and closed the billing period, the **Consumer** performs **final invoice reconciliation**.
- If the consumer is a **Managed Service Provider (MSP)**, they proceed to **generate downstream invoices** for their own customers based on the finalized May data.
- From the Consumer’s financial point of view, the **May 2025 billing period is now considered closed**.

---

#### T2: 2025-07-12 - Corrections After Invoice Finalization

> **Note:** Detailed correction scenarios related to post-invoice finalization are available in Chapter Post-Invoice Finalization Scenarios.

---

### Post-Invoice Finalization Scenarios

#### S-1: Itemized Correction Scenarios with Cost Calculation Integrity Respected

##### REPLACED Scenario 1.1 (S-1.1): Post Invoice Correction - Correction to ResourceId dimension

- The Data Generator identifies that a **previously provisioned charge record** (delivered before the billing period was closed) contains an **incorrect `ResourceId`**.
- This record was part of the **finalized invoice** issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires **reallocating the cost and usage quantity** from the incorrect resource (`R-111`) to the correct one (`R-222`).

##### Scenario 1.1 (S-1.1): Post Invoice Correction – Partial Reallocation to Correct ResourceId

- The Data Generator identifies that a **previously provisioned charge record** (delivered before the billing period was closed) was **incorrectly attributed entirely to `ResourceId R-111`**, even though only part of the cost and usage belongs to that resource, with the remainder pertaining to another resource (`ResourceId R-222`).
- This record was part of the **finalized invoice** issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires **reallocating part of the cost and usage quantity** from the incorrect resource (`R-111`) to the correct resource (`R-222`), while the remainder stays attributed to the original resource.
  - **Ledger Style:**  
    The Data Generator sends two correction records to adjust the original charge:  
    - A **decrement** record to reduce cost and usage attributed to the `ResourceId R-111`.  
    - An **increment** record to increase cost and usage attributed to the `ResourceId R-222`.
  - **Accounting Style:**  
    The Data Generator sends three correction records:  
    - One Negation record to fully negate the original incorrect charge attributed to `ResourceId R-111`.  
    - One Corrected record with the remaining cost and usage still attributed to the original resource (`R-111`).
    - One Corrected record with the adjusted cost and usage attributed to the correct resource (`R-222`).
  - **Restatement Style**
    Restatement style, which involves overwriting or replacing previously delivered charge records within the original billing period, is not suitable for this scenario. Since the invoice is already finalized and the corresponding billing period is closed, modifying or replacing original records is prohibited due to legal and procedural requirements. Therefore, the Data Generator sends corrections using one of the two non-restatement styles.

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Problematic Scenarios Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=1846137666#gid=1846137666)*.

##### Scenario 1.2 (S-1.2): Post Invoice Correction - Late-arriving Usage

- The Data Generator identifies a **late-arriving cost** that was **incurred during May** (e.g., `ChargePeriodStart = 2025-05-01`).
- This cost was not included in the finalized invoice issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires provisioning **additional charge record** to represent the late-arriving cost
  - **Ledger Style:**  
    The Data Generator sends a single Increment record representing the late-arriving usage and associated cost.
  - **Accounting Style:**  
    The Data Generator sends a single Increment record representing the late-arriving usage and associated cost.
  - **Restatement Style**
    Restatement style is not suitable for this scenario. (*See Scenario 1.1 for more details.*)

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Problematic Scenarios Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=1846137666#gid=1846137666)*.

#### S-2: Itemized Correction Scenarios with Cost Calculation Integrity Exceptions Allowed

##### Scenario 2.1 (S-2.1): Post-Invoice Correction – Cost-only correction

- The Data Generator detects a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records **related to a single `SkuPriceId`**. Although each individual record was correctly rounded, the aggregated cost differs slightly from the precise total, resulting in a small drift.
- Original records were part of the finalized invoice issued at T0.
- The original billing period is already closed, while the subsequent billing period (e.g., July 2025) is still open.
- The correction requires provisioning a cost-only correction record to reconcile the total cost drift and ensure invoice accuracy.
- The correction requires provisioning an **itemized cost-only correction record** with the relevant `SkuPriceId` to reconcile the total cost drift and ensure invoice accuracy.
  - **Ledger Style:**  
    The Data Generator sends a single Increment record representing the cost-only correction required to reconcile the total cost drift, with the relevant `SkuPriceId` specified.
  - **Accounting Style:**  
    The Data Generator sends a single Increment record representing the cost-only correction required to reconcile the total cost drift.
  - **Restatement Style**
    Restatement style is not suitable for this scenario. (*See Scenario 1.1 for more details.*)

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Cost Calculation Integrity Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=669333874#gid=669333874)*.

##### Scenario 2.2 (S-2.2): Post-Invoice Correction – PricingQuantity-only correction

**Recommendation:** This use case should be prevented by design. (See **Proposal: Prevent PricingQuantity-only corrections** chapter for more details)

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Cost Calculation Integrity Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=669333874#gid=669333874)*.

##### Scenario 2.3 (S-2.3): Post-Invoice Correction – Misaligned Cost and PricingQuantity correction without UnitPrice

This is not considered a valid use case.
Refer to the proposals in **Refine Cost Calculation Integrity Norms and Permissible Discrepancies for Correction** for reasonng.

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Cost Calculation Integrity Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=669333874#gid=669333874)*.

##### Scenario 2.4 (S-2.4): Post-Invoice Correction – Misaligned Cost and PricingQuantity correction with UnitPrice

This is not considered a valid use case.
Refer to the proposals in **Refine Cost Calculation Integrity Norms and Permissible Discrepancies for Correction** for reasonng.

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Cost Calculation Integrity Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=669333874#gid=669333874)*.

#### S-3: Bulk and Bulk Correction Scenarios with Cost Calculation Integrity Exceptions Allowed

***Note:** In the context of this PR, Bulk refers to charge records where SkuPriceId (and SkuId) is null.*

##### Scenario 3.1 (S-3.1): Post-Invoice Correction – Cost-only Bulk Usage Correction

- The Data Generator detects a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records **spanning several different `SkuPriceId` values**. Although each individual record was correctly rounded, the aggregated cost differs slightly from the precise total, resulting in a small drift.
- Original records were part of the finalized invoice issued at T0.
- The original billing period is already closed, while the subsequent billing period (e.g., July 2025) is still open.
- The correction requires provisioning a **bulk cost-only correction record** (without specifying `SkuPriceId`) to reconcile the total cost drift across multiple items and ensure invoice accuracy.
  - **Ledger Style:**  
    The Data Generator sends a single Increment record representing the cost-only correction required to reconcile the total cost drift, without specifying a `SkuPriceId`, as the correction spans multiple SKU Price IDs.
  - **Accounting Style:**  
    The Data Generator sends a single Increment record representing the cost-only correction required to reconcile the total cost drift.
  - **Restatement Style**
    Restatement style is not suitable for this scenario. (*See Scenario 1.1 for more details.*)

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Problematic Scenarios Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=1846137666#gid=1846137666)*.

##### Scenario 3.2 (S-3.2): Post-Invoice Correction – Cost and PricingQuantity Bulk Usage Correction

Bulk corrections to `PricingQuantity` (or any other SKU Price-dependent column) **are not (or should not be) allowed** regardless of the timing of the correction timing. This rule applies equally to Adjustments (e.g., rounding errors) occurring in the current or any still open past billing period.

If a PricingQuantity correction is needed, the associated SkuPriceId **must** be provided to ensure accurate attribution and interpretation.

**Reasoning:** PricingQuantity and several other SKU/SKU Price-dependent columns lack business meaning SkuPriceId (and SkuId) is null, as they cannot be interpreted without a known SkuPriceId.

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Problematic Scenarios Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=1846137666#gid=1846137666)*.

##### Scenario 3.3 (S-3.3): Post-Invoice Correction – PricingQuantity-only Bulk Usage Correction

Bulk corrections to `PricingQuantity` (or any other SKU Price-dependent column) **are not (or should not be) allowed** regardless of the timing of the correction timing. (*See Scenario 3.2 for more details.*)

- *For sample data, see the [30.06.25 Correction Handling Use Cases spreadsheet, sheet Problematic Scenarios Examples](https://docs.google.com/spreadsheets/d/1RV2Pb4bSo86L2wOFZm5dK0lYxiac6BfkQK81ivOvhsU/edit?gid=1846137666#gid=1846137666)*.

## References

- **AWS**
  - https://docs.aws.amazon.com/cli/latest/reference/cur/describe-report-definitions.html

    > **RefreshClosedReports -> (boolean):** Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
    >
    > **ReportVersioning -> (string):** Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
