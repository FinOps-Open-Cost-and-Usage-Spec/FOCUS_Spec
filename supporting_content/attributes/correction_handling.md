# Correction handling

## Prevent Replacement After Invoice Finalization (and Billing Period Closure)

***Note:*** *See S-1: Itemized Correction Scenarios with Cost Calculation Integrity Respected - S-1.1 and S-1.2 in particular*

We should prevent the use of the Replacement provisioning style once an invoice has been finalized and the corresponding billing period closed.

Since Replacement relies on overwriting or replacing previously delivered charge records within the original billing period, it inherently conflicts with the Normative Requirements for Post-Invoice Finalization Corrections - and in particular the Legal and Procedural Perspective, which states that once an invoice has been finalized and the corresponding billing period closed:

- A finalized invoice is considered legally issued and immutable.
- The associated billing period is closed, prohibiting any modifications or overwriting of previously delivered records.

Therefore, only append-only provisioning styles (such as ledger-style increments/decrements or accounting-style reversals followed by corrected entries) should be permitted for handling Post-Invoice Finalization Corrections.

**Exceptions:**

- Contributors are encouraged to document any exception to the general rule.

- Should we allow restating in cases where corrections apply to dimensions that were not included in the original invoice?
  *Note: Personally, I would prefer not to allow this.*
- Technical issues mentioned by Riley.
- Explicitly specified by the end-user.

### Normative Requirements for Post-Invoice Finalization Corrections

> Shawn has added numbers to the statements that would become normative requirements in the attribute

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

## Cost and Usage data Provisioning Styles

Data Generators typically use two main provisioning styles/mechanisms when delivering cost and usage data:

- **Replacement:** Overwrites previously delivered records with updated ones. This approach ensures data accuracy by reflecting corrections directly in place.

- **Append-only:** Delivers only new records without modifying previously sent data. This approach can be further divided into two subtypes:
  - **Ledger-style:** Adds incremental (or decremental) records over time. Corrections are reflected as additional entries where the cost or quantity metrics are adjusted (+/-), while all other dimensions remain identical to the original record. This supports an append-only model but offers limited auditability, as there is typically no explicit reversal.
  - **Accounting-style:** Tracks changes explicitly via negative (reversal) entries followed by corrected records. This ensures full auditability and provides a clear historical trail of adjustments.

## Finalized Invoice and Closed Billing Period

> See [FR #Add invoice-level correction handling rules](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1013)

While the FOCUS specification mentions closed billing periods, it currently does not define the process for invoice issuance or billing period closure. It also does not define any explicit **“finalized”** status for invoices, nor a **"closed"** status for billing periods, nor the point at which an invoice is considered finalized or a billing period considered closed.

To address these **gaps** in this scenario, we assume the following:

- Data Generator (Providers) finalize invoices at some point, marking them as ready for invoice reconciliation.
- A billing period is considered closed once all invoices for that period are finalized.

***Note:** These information are assumed to be provided not within the cost and usage dataset itself, but in separate, adjacent datasets (e.g., invoice-related datasets).
