# Examples: Invoice Detail

## Overview

The **Invoice Detail** dataset provides a transactional representation of the financial obligations between a customer and an invoice issuer. While the [Cost and Usage](#datasets.costandusage) dataset tracks granular consumption, the Invoice Detail dataset tracks the legal and financial record of charges as they appear on a physical or electronic billing document.

### Core Logical Pillars

To ensure interoperability across different billing systems, the dataset relies on three core logical pillars:

1. **Reconciliation & Lineage:** The dataset links every charge back to a specific document (`InvoiceId`) and allows for auditable corrections. If a charge is refunded or adjusted, the `ReferenceInvoiceId` connects the adjustment back to the original invoice, preserving the financial narrative.
2. **Granularity Definition:** Unlike standard datasets with fixed schemas, invoice line items vary wildly in detail (e.g., a single line for "Enterprise Support" vs. millions of lines for "Storage"). The `InvoiceDetailGrain` column uses a flexible JSON structure to capture the specific dimensions (SKU, Region, Project) relevant to that specific line item without breaking the schema.
3. **Currency Duality:** The dataset explicitly separates the currency of measurement (`BillingCurrency`) from the currency of settlement (`PaymentCurrency`). This allows organizations to validate usage costs in the original currency (e.g., USD) while reconciling the final cash outflow in their local currency (e.g., EUR, AUD).

### Expected Value Taxonomy

The following table defines the high-level expectations for key categorical columns in this dataset:

| Attribute | Expected Value Logic | Example Values |
| :--- | :--- | :--- |
| **Charge Category** | The high-level classification of the line item. | `Usage`, `Purchase`, `Tax`, `Credit`, `Adjustment` |
| **Invoice Issue Status** | The publication state of the document. | `Open`, `Issued`, `Voided` |
| **Payment Terms** | The agreed-upon timeframe for settlement. | `Net 30`, `Due on Receipt`, `Net 60` |
| **Billing Currency** | The currency used to measure the value of the service. | `USD`, `EUR`, `CNY` |
| **Payment Currency** | The currency required for the actual financial transfer. | `USD`, `GBP`, `AUD` |

## Examples

The following examples demonstrate some common patterns for issuing invoices from a major provider, **Acme Co**.

### Scenario 1: Typical Monthly Cloud Invoice

This example includes a mix of standard consumption, a one-time purchase of a reserved instance, and taxes, all billed and paid in the same currency (USD).

* **Currencies:** Since Billing and Payment currencies are identical, `PaymentCurrencyBilledCost` matches `BilledCost`.
* **Aggregate Payment Currency**: Since no aggregate rows are present, `PaymentCurrencyInvoiceDetailId` is different for all rows.
* **Invoice Lineage:** Since this is an original invoice, `ReferenceInvoiceId` matches `InvoiceId`.

#### Data Example: INV-2025-001

| Column | Line 1: Compute Usage | Line 2: RI Purchase | Line 3: NY State Tax |
| :--- | :--- | :--- | :--- |
| **Billed Cost** | `450.00` | `1000.00` | `128.63` |
| **Billing Account ID** | `123456789` | `123456789` | `123456789` |
| **Billing Currency** | `USD` | `USD` | `USD` |
| **Billing Period End** | `2025-02-01T00:00:00Z` | `2025-02-01T00:00:00Z` | `2025-02-01T00:00:00Z` |
| **Billing Period Start** | `2025-01-01T00:00:00Z` | `2025-01-01T00:00:00Z` | `2025-01-01T00:00:00Z` |
| **Charge Category** | `Usage` | `Purchase` | `Tax` |
| **Invoice Detail Created** | `2025-02-02T10:00:00Z` | `2025-02-02T10:00:00Z` | `2025-02-02T10:00:00Z` |
| **Invoice Detail Description** | `Use of m5.large in us-east-1` | `Upfront fee for RI #998877` | `Sales Tax for NY Jurisdiction` |
| **Invoice Detail Grain** | `{"ServiceName": "Compute"}` | `{"ServiceName": "Compute"}` | `{}` |
| **Invoice Detail ID** | `LINE-001` | `LINE-002` | `LINE-003` |
| **Invoice Detail Last Updated** | `2025-02-02T10:00:00Z` | `2025-02-02T10:00:00Z` | `2025-02-02T10:00:00Z` |
| **Invoice ID** | `INV-2025-001` | `INV-2025-001` | `INV-2025-001` |
| **Invoice Issue Date** | `2025-02-03T00:00:00Z` | `2025-02-03T00:00:00Z` | `2025-02-03T00:00:00Z` |
| **Invoice Issue Status** | `Issued` | `Issued` | `Issued` |
| **Invoice Issuer Name** | `Acme Co` | `Acme Co` | `Acme Co` |
| **Payment Currency** | `USD` | `USD` | `USD` |
| **Payment Currency Billed Cost** | `450.00` | `1000.00` | `128.63` |
| **Payment Currency Invoice Detail ID** | `LINE-001` | `LINE-002` | `LINE-003` |
| **Payment Due Date** | `2025-03-05T00:00:00Z` | `2025-03-05T00:00:00Z` | `2025-03-05T00:00:00Z` |
| **Payment Terms** | `Net 30` | `Net 30` | `Net 30` |
| **Purchase Order Number** | `PO-998877` | `PO-998877` | `PO-998877` |
| **Reference Invoice ID** | `INV-2025-001` | `INV-2025-001` | `INV-2025-001` |

### Scenario 2: Multi-Currency Settlement

This example demonstrates the "Divergent Grain" model, where usage is tracked in a global currency (USD), but the legal financial obligation is settled in a local currency (AUD).

* **Row 1 & 2 (Usage):** The detail lines, denominated in USD. `PaymentCurrencyBilledCost` is `0.00` because the detail does not have an exchange rate applied.
* **Row 3 (Settlement):** The aggregate payable line, denominated in AUD. `BilledCost` is `0.00` (USD) to avoid double-counting consumption. `PaymentCurrencyBilledCost` holds the 5.17 AUD obligation.
* **Aggregate Payment Currency**: Because aggregate Payment Currency rows are present, the same `PaymentCurrencyInvoiceDetailId` value of `LINE-AGG` associates these rows with each other.
* **Invoice Lineage:** Since this is an original invoice, `ReferenceInvoiceId` matches `InvoiceId`.

#### Data Example: AUIN25-1286479

| Column | Line 1: Storage Usage | Line 2: Storage Tax | Line 3: AUD Settlement |
| :--- | :--- | :--- | :--- |
| **Billed Cost** | `3.03` | `0.30` | `0.00` |
| **Billing Account ID** | `615703680694` | `615703680694` | `615703680694` |
| **Billing Currency** | `USD` | `USD` | `USD` |
| **Billing Period End** | `2025-07-01T00:00:00Z` | `2025-07-01T00:00:00Z` | `2025-07-01T00:00:00Z` |
| **Billing Period Start** | `2025-06-01T00:00:00Z` | `2025-06-01T00:00:00Z` | `2025-06-01T00:00:00Z` |
| **Charge Category** | `Usage` | `Tax` | `Adjustment` |
| **Invoice Detail Created** | `2025-07-01T12:00:00Z` | `2025-07-01T12:00:00Z` | `2025-07-01T12:00:00Z` |
| **Invoice Detail Description** | `AcmeStore Standard Storage` | `Tax for AcmeStore` | `Currency Conversion Settlement` |
| **Invoice Detail Grain** | `{"ServiceName": "AcmeStore"}` | `{"ServiceName": "AcmeStore"}` | `{}` |
| **Invoice Detail ID** | `LINE-001` | `LINE-002` | `LINE-AGG` |
| **Invoice Detail Last Updated** | `2025-07-01T12:00:00Z` | `2025-07-01T12:00:00Z` | `2025-07-01T12:00:00Z` |
| **Invoice ID** | `AUIN25-1286479` | `AUIN25-1286479` | `AUIN25-1286479` |
| **Invoice Issue Date** | `2025-07-01T00:00:00Z` | `2025-07-01T00:00:00Z` | `2025-07-01T00:00:00Z` |
| **Invoice Issue Status** | `Issued` | `Issued` | `Issued` |
| **Invoice Issuer Name** | `Acme Co` | `Acme Co` | `Acme Co` |
| **Payment Currency** | `AUD` | `AUD` | `AUD` |
| **Payment Currency Billed Cost** | `0.00` | `0.00` | `5.17` |
| **Payment Currency Invoice Detail ID** | `LINE-AGG` | `LINE-AGG` | `LINE-AGG` |
| **Payment Due Date** | `2025-08-01T00:00:00Z` | `2025-08-01T00:00:00Z` | `2025-08-01T00:00:00Z` |
| **Payment Terms** | `Net 30` | `Net 30` | `Net 30` |
| **Purchase Order Number** | `null` | `null` | `null` |
| **Reference Invoice ID** | `AUIN25-1286479` | `AUIN25-1286479` | `AUIN25-1286479` |

### Scenario 3: Billing Error Correction

This example demonstrates the lineage of a billing error correction.

* **Line 1 (The Error):** The original charge appears on the January invoice (`INV-JAN`) with an overstated cost of 150.00.
* **Line 2 (The Correction):** In February (`INV-FEB`), the error is identified. A correction line is issued for -50.00. Crucially, the `ReferenceInvoiceId` points back to `INV-JAN`, linking the refund to the original transaction.

#### Data Example: INV-JAN and INV-FEB

| Column | Line 1: Jan Usage (Overstated) | Line 2: Feb Correction (Adjustment) |
| :--- | :--- | :--- |
| **Billed Cost** | `150.00` | `-50.00` |
| **Billing Account ID** | `987654321` | `987654321` |
| **Billing Currency** | `USD` | `USD` |
| **Billing Period End** | `2025-02-01T00:00:00Z` | `2025-03-01T00:00:00Z` |
| **Billing Period Start** | `2025-01-01T00:00:00Z` | `2025-02-01T00:00:00Z` |
| **Charge Category** | `Usage` | `Adjustment` |
| **Invoice Detail Created** | `2025-02-02T10:00:00Z` | `2025-03-02T10:00:00Z` |
| **Invoice Detail Description** | `Database Usage (Overstated)` | `Correction for Line-100` |
| **Invoice Detail Grain** | `{"ServiceName": "Database"}` | `{}` |
| **Invoice Detail ID** | `Line-100` | `ADJ-001` |
| **Invoice Detail Last Updated** | `2025-02-02T10:00:00Z` | `2025-03-02T10:00:00Z` |
| **Invoice ID** | `INV-JAN` | `INV-FEB` |
| **Invoice Issue Date** | `2025-02-03T00:00:00Z` | `2025-03-03T00:00:00Z` |
| **Invoice Issue Status** | `Issued` | `Issued` |
| **Invoice Issuer Name** | `Acme Co` | `Acme Co` |
| **Payment Currency** | `USD` | `USD` |
| **Payment Currency Billed Cost** | `150.00` | `-50.00` |
| **Payment Currency Invoice Detail ID** | `Line-100` | `ADJ-001` |
| **Payment Due Date** | `2025-03-05T00:00:00Z` | `2025-04-05T00:00:00Z` |
| **Payment Terms** | `Net 30` | `Net 30` |
| **Purchase Order Number** | `PO-554433` | `PO-554433` |
| **Reference Invoice ID** | `INV-JAN` | `INV-JAN` |
