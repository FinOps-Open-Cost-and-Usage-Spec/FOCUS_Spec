# Correction Handling Examples

## Context

- **ChargePeriod and BillingPeriod:**
  - ChargePeriod denotes the effective period of the charge — i.e., when the underlying usage occurred.
  - BillingPeriod represents the invoicing window to which the charge is financially assigned, regardless of when the usage took place.

- **Export Date Time:**
  - The FOCUS specification does not define how to determine when a charge record was provisioned.
  - To address this gap in the context of this scenario, and solely for illustrative purposes, we introduce a custom helper column, `x_ExportDateTime`, to indicate when a charge record was delivered to the consumer.

- **Finalized Invoice and Closed Billing Period**
  - While the FOCUS specification mentions closed billing periods, it currently does not define the process for invoice issuance or billing period closure. It also does not define any explicit **“finalized”** status for invoices, nor a **“closed”** status for billing periods, nor the point at which an invoice is considered finalized or a billing period considered closed.
  - To address these gaps in this scenario, we assume the following:
    - Providers finalize invoices at some point, marking them as ready for invoice reconciliation.
    - A billing period is considered closed once all invoices for that period are finalized.
    - ***Note:** These information are assumed to be provided not within the cost and usage dataset itself, but in separate, adjacent datasets (e.g., invoice-related datasets).

## Use Case Scenarios

### Scenario 1: Handling Charges provisioned after Invoice Finalization and Billing Period Closure

#### Scenario Description

- During May and early June, the Data Generator (e.g., CSP) delivers cost and usage data for the **May 2025 billing period** (`BillingPeriodStart = 2025-05-01`, `BillingPeriodEnd = 2025-06-01`).
- All cost records include an `InvoiceId` (e.g., `INV-20250501-20250601`), assigned **prior to invoice issuance**, in accordance with the normative guidance for `InvoiceId`.

---

#### Timeline of Events

##### T0 – 2025-06-05

- The Provider has completed **initial provisioning** of all known cost records for the May 2025 billing period.  
  The working assumption at this point is that **all May costs have been delivered**.
- All charge records have `x_ExportDateTime` **earlier than T0**.
- The Provider performs internal **invoice reconciliation** and issues final invoices for the account for May 2025 (e.g., `INV-202505-202506`).
  - All Invoice related issues MUST be resoved at this point!
- All invoices for May are now finalized, and the Provider **closes** the May billing period, setting `BillingPeriodClosureDateTime = T0`.
- From the Provider’s (i.e., Data Generator's) **financial perspective**, May 2025 is now complete.
  - Any charge records **provisioned on or after T0** (i.e., with `x_ExportDateTime ≥ T0`) **must** be assigned to an **open billing period**.  
  Therefore, the earliest valid `BillingPeriodStart`/`BillingPeriodEnd` for such records is **June 2025**.

---

#### T1 – 2025-06-06

- Since the Provider has finalized the invoice and closed the billing period, the **Consumer** performs **final invoice reconciliation**.
- If the consumer is a **Managed Service Provider (MSP)**, they proceed to **generate downstream invoices** for their own customers based on the finalized May data.
- From the Consumer’s financial point of view, the **May 2025 billing period is now considered closed**.

---

#### T2 – 2025-07-12

##### Scenario 1.1 (S-1.1): Post Invoice Correction: Correction to ResourceId dimension

- The Provider identifies that a **previously provisioned charge record** (delivered before the billing period was closed) contains an **incorrect `ResourceId`**.
- This record was part of the **finalized invoice** issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.
- The correction requires **reallocating the cost and usage quantity** from the incorrect resource (`R-111`) to the correct one (`R-222`).
- At this point the May 2025 billing period is closed while the June 2025 billing period is still open.

- For corresponding **correction records**, the following applies:

  - **Provisioning perspective**: `x_ExportDateTime = T2` (i.e., the date it became available to the consumer)

  - **Operational perspective**: All Correction records (Increments and Decrements in case of the Ledger style, Negations and Corrected records in case of Accounting style) belong to **May**, so `ChargePeriodStart` and `ChargePeriodEnd` **must reflect the actual usage period** (e.g., `ChargePeriodStart = 2025-05-01`)

  - **Financial perspective**: The original invoice (`INV-20250501-20250601`) has already been finalized and sent (e.g., as PDF). The May billing period is **considered closed**.
    - **BillingPeriod constraint**: `BillingPeriodStart`/`BillingPeriodEnd` **must be equal to or later than** the first **open** billing period — i.e., **June 2025 or later**.

##### Scenario 1.2 (S-1.2): Post Invoice Correction: Late-arriving Usage

- The Provider identifies a **late-arriving cost** that was **incurred during May** (e.g., `ChargePeriodStart = 2025-05-01`).
- This cost was not included in the finalized invoice issued at T0.
- The **May billing period is already closed**, while the **June 2025 billing period is still open**.

- For such **late-arriving charge records**, the following applies:

  - **Provisioning perspective**: `x_ExportDateTime = T2` (i.e., the date it became available to the consumer)

  - **Operational perspective**: The cost belongs to **May**, so `ChargePeriodStart` and `ChargePeriodEnd` **must reflect the actual usage period** (e.g., `ChargePeriodStart = 2025-05-01`)

  - **Financial perspective**:  
    The original invoice (`INV-20250501-20250601`) has already been finalized and sent (e.g., as PDF). The May billing period is **considered closed**.
    - **BillingPeriod constraint**: `BillingPeriodStart`/`BillingPeriodEnd` **must be equal to or later than** the first **open** billing period — i.e., **June 2025 or later**.


## References

- **AWS**
  - https://docs.aws.amazon.com/cli/latest/reference/cur/describe-report-definitions.html

    > **RefreshClosedReports -> (boolean):** Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
    >
    > **ReportVersioning -> (string):** Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
