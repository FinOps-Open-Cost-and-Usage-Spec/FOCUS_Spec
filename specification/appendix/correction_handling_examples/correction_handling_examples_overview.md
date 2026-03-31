# Correction Handling Examples Overview

This section provides examples of how correction handling may be implemented in alignment with the FOCUS specification. The examples are limited to illustrating correction handling for the Cost and Usage FOCUS dataset, and cover scenarios involving corrections to open and closed billing periods, as well as the various delivery mechanisms and correction styles supported by FOCUS.

The examples that follow are sectioned by [Billing Period Status](#datasets.billingperiod.billingperiodstatus) (i.e., "Open" or "Closed") and Billing Period Category (i.e., current open period, or previous open period, or closed):

| Billing Period Status | Billing Period Category | Description |
| :--- | :--- | :--- |
| Open | Current Open | Examples of corrections to the current, open billing period. |
| Open | Previous Open | Examples of corrections to a previous billing period that has not yet been closed. |
| Closed | Closed | Examples of corrections to a closed billing period. |

Within each of the sections above, the following four correction scenarios are demonstrated:

| Correction Scenario | Description |
| :--- | :--- |
| **Partial Reallocation to Correct Resource** | Correcting misattributed costs between resources. |
| **Late-Arriving Usage** | Accounting for omitted costs and usage incurred in a prior timeframe. |
| **Itemized Cost-Only Corrections** | Reconciling minor cost drift with explicit adjustments per SKU. |
| **Bulk Cost-Only Corrections** | Reconciling minor cost drift using a single, consolidated adjustment. |

The example dataset artifacts provided in these scenarios demonstrate three distinct correction styles, each aligned with one of the supported delivery mechanisms:

| Correction Style | Delivery Mechanism | Description |
| :--- | :--- | :--- |
| **Replacement** | Overwrite | Corrections are modeled through updates, additions, or omissions relative to the previous snapshot. This style reflects the latest state of data and does not retain historical correction records unless externally preserved. |
| **Delta** | Append | Corrections are represented by additive records that increment or decrement selected cost and quantity values. Original records remain unchanged, and reversals are optional. This style offers limited audit transparency. |
| **Ledger** | Append | Corrections typically follow a two-step approach: reversal of the original record (if needed), and addition of a corrected record. Reversal is performed by creating a record with opposite cost and quantity values, while all other columns match the original. This style preserves full correction history and supports comprehensive auditability. |
