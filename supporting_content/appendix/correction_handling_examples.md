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

### Enforce Nullability When `SkuPriceId` Is Null

> **NOTE:** This applies beyond Correction Handling scenarios and may require a separate FR. It MUST be resolved comprehensively — addressing it solely within correction scenarios is not sufficient.  
> **TODO:** Address this in the respective Column Definitions (Normative Requirements sections), assuming consensus is reached.

***Note:*** *See S-3: Bulk and Bulk Correction Scenarios with Cost Calculation Integrity Exceptions Allowed - S-3.2 and S-3.3 in particular*

In cases where `SkuPriceId` is null, we should prevent setting non-null values in the following SKU/SKU Price-dependent columns:

- `SKU`
- `Pricing Quantity`
- `Pricing Category`
- `Contracted Unit Price`
- `List Unit Price`
- `Pricing Currency Contracted Unit Price`
- `Pricing Currency List Unit Price`
- `Consumed Quantity`
- `Commitment Discount Quantity`

The values in the above columns lack business meaning unless the associated `SkuPriceId` (or `SkuId`) is known. We propose making these columns **strictly null** when the SKU context is missing, to ensure consistency and data integrity.

To achieve this, we suggest updating the **nullability** section of each relevant column as follows:

> - `<ColumnId>` nullability is defined as follows:  
>   - `<ColumnId>` **MUST be null** when `SkuPriceId` is null.  
>   - ...

#### Current Nullability Behavior for SKU/SKU Price-dependent columns

Based on the analysis of current nullability requirements, all listed columns (except `Consumed Quantity` and `Commitment Discount Quantity`) currently follow this pattern:

> - `<ColumnId>` nullability is defined as follows:  
>   - `<ColumnId>` MUST be null when [`ChargeCategory`](#chargecategory) is `"Tax"`.  
>   - `<ColumnId>` MUST NOT be null when `ChargeCategory` is `"Usage"` or `"Purchase"` and [`ChargeClass`](#chargeclass) is not `"Correction"`.  
>   - `<ColumnId>` MAY be null in all other cases.

As a result, under the current rules, these columns can be populated even when the corresponding `SkuPriceId` (or `SkuId`) is not known, specifically in the following cases:

- `ChargeCategory: Adjustment` or `Credit`
- `ChargeCategory: Usage` or `Purchase` with `ChargeClass: Correction`

***Note:*** *Although `Consumed Quantity` and `Commitment Discount Quantity` follow a slightly different nullability pattern, they are also currently allowed to hold values even when `SkuPriceId` is not provided.*

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

#### T1: 2025-06-13 - Invoice finalization (and Billing Period closure) on Consumen's side

- Since the Data Generator (Provider) has finalized the invoice and closed the billing period, the **Consumer** performs **final invoice reconciliation**.
- If the consumer is a **Managed Service Provider (MSP)**, they proceed to **generate downstream invoices** for their own customers based on the finalized May data.
- From the Consumer’s financial point of view, the **May 2025 billing period is now considered closed**.

---

#### T2: 2025-07-12 - Corrections After Invoice Finalization

##### Normative Requirements for Post-Invoice Finalization Corrections

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

##### S-1: Itemized Correction Scenarios with Cost Calculation Integrity Respected

###### REPLACED Scenario 1.1 (S-1.1): Post Invoice Correction - Correction to ResourceId dimension

- The Data Generator identifies that a **previously provisioned charge record** (delivered before the billing period was closed) contains an **incorrect `ResourceId`**.
- This record was part of the **finalized invoice** issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires **reallocating the cost and usage quantity** from the incorrect resource (`R-111`) to the correct one (`R-222`).

###### Scenario 1.1 (S-1.1): Post Invoice Correction – Partial Reallocation to Correct ResourceId

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

###### Scenario 1.2 (S-1.2): Post Invoice Correction - Late-arriving Usage

- The Data Generator identifies a **late-arriving cost** that was **incurred during May** (e.g., `ChargePeriodStart = 2025-05-01`).
- This cost was not included in the finalized invoice issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires provisioning **additional charge record** to represent the late-arriving cost
  - **Ledger Style:**  
    The Data Generator sends a single Increment record representing the late-arriving usage and associated cost.
  - **Accounting Style:**  
    The Data Generator sends a single Corrected record representing the late-arriving usage and associated cost.
  - **Restatement Style**
    Restatement style, which involves overwriting or replacing previously delivered charge records within the original billing period, is not suitable for this scenario. Since the invoice is already finalized and the corresponding billing period is closed, modifying or replacing original records is prohibited due to legal and procedural requirements. Therefore, the Data Generator sends corrections using one of the two non-restatement styles.

##### S-2: Itemized Correction Scenarios with Cost Calculation Integrity Exceptions Allowed

###### Scenario 2.1 (S-2.1): Post-Invoice Correction – Cost-only correction

**TODO:**

###### Scenario 2.2 (S-2.2): Post-Invoice Correction – PricingQuantity-only correction

**TODO:**

###### Scenario 2.3 (S-2.3): Post-Invoice Correction – Misaligned Cost and PricingQuantity correction without UnitPrice

**TODO:**

###### Scenario 2.4 (S-2.4): Post-Invoice Correction – Misaligned Cost and PricingQuantity correction with UnitPrice

**TODO:**

##### S-3: Bulk and Bulk Correction Scenarios with Cost Calculation Integrity Exceptions Allowed

**Note:** In the context of this PR, Bulk refers to charge records where SkuPriceId (and SkuId) is null.

###### Scenario 3.1 (S-3.1): Post-Invoice Correction – Cost-only Bulk Usage Correction

**TODO:**

###### Scenario 3.2 (S-3.2): Post-Invoice Correction – PricingQuantity-only Bulk Usage Correction

PricingQuantity and several other SKU/SKU Price-dependent columns lack business meaning in such cases, as they cannot be interpreted without a known SkuPriceId.

Therefore, Bulk corrections to `PricingQuantity` (or any other SKU Price-dependent column) **are not (or should not be) allowed** regardless of the timing of the correction timing. This rule applies equally to Adjustments (e.g., rounding errors) occurring in the current or any still open past billing period. 

If a PricingQuantity correction is needed, the associated SkuPriceId **must** be provided to ensure accurate attribution and interpretation.

###### Scenario 3.3 (S-3.3): Post-Invoice Correction – Cost and PricingQuantity Bulk Usage Correction

Bulk corrections to `PricingQuantity` (or any other SKU Price-dependent column) **are not (or should not be) allowed** regardless of the timing of the correction timing. (*See Scenario 3.2 for more details.*)

## References

- **AWS**
  - https://docs.aws.amazon.com/cli/latest/reference/cur/describe-report-definitions.html

    > **RefreshClosedReports -> (boolean):** Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
    >
    > **ReportVersioning -> (string):** Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
