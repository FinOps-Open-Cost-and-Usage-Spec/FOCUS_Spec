# Rounding Variance Tolerance

When performing invoice reconciliation between the [Cost and Usage](#datasets.costandusage) dataset and an invoice (either the payable invoice itself, or the [Invoice Detail](#datasets.invoicedetail) dataset), exact matches are not expected due to precision differences (e.g., 6 decimals in detailed cost data vs. 2 decimals in invoice data). The following tolerance formula allows for a maximum rounding error based on the statistical probability of rounding variance, which grows with the square root of the row count.

## Tolerance Formula

The tolerance used when comparing aggregated BilledCost values is defined as:

Tolerance = `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)`

Where:

* **Rows** — The number of [CostAndUsage](#datasets.costandusage) rows included in the aggregation for the relevant [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and (if applicable) [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid).
* **Subunit** — The numeric value of the smallest subunit of [CostAndUsage.BillingCurrency](#datasets.costandusage.billingcurrency) (for example, `0.01` for USD or `1` for JPY).

The tolerance is the **greater** of the following values:

* **100 × Subunit** — Establishes a fixed minimum tolerance equal to 100 units of the smallest currency subunit.
* **(SQRT(Rows) × 0.5) × Subunit** — Provides a tolerance that increases with the square root of the number of rows to account for rounding accumulation in larger datasets.

## Scenario 1: Small Invoice (Pass)

* Data: A small invoice with 5 line items.
* Values: CostAndUsage sums to &dollar;12.50. InvoiceDetail sums to &dollar;12.52. Difference is **&dollar;0.02**.
* Limit Calculation:
  * Statistical Limit: `SQRT(5) * 0.5 * 0.01` = &dollar;0.011.
  * Floor Limit: `100 * 0.01` = &dollar;1.00.
  * Effective Tolerance: **&dollar;1.00** (Greater of &dollar;0.011 and &dollar;1.00).
* Result: **Pass** (Difference &dollar;0.02 < Tolerance &dollar;1.00).

## Scenario 2: Small Invoice (Fail)

* Data: A small invoice with 5 line items where a &dollar;5.00 charge is missing from CostAndUsage.
* Values: CostAndUsage sums to &dollar;10.00. InvoiceDetail sums to &dollar;15.00. Difference is **&dollar;5.00**.
* Limit Calculation:
  * Effective Tolerance: **&dollar;1.00**.
* Result: **Fail** (Difference &dollar;5.00 > Tolerance &dollar;1.00).

## Scenario 3: Large Invoice (Pass)

* Data: An enterprise invoice with 1,000,000 line items.
* Values: CostAndUsage sums to &dollar;5,000,000.00. InvoiceDetail sums to &dollar;5,000,004.50. Difference is **&dollar;4.50**.
* Limit Calculation:
  * Statistical Limit: `SQRT(1,000,000) * 0.5 * 0.01` = &dollar;5.00.
  * Floor Limit: `100 * 0.01` = &dollar;1.00.
  * Effective Tolerance: **&dollar;5.00** (Greater of &dollar;5.00 and &dollar;1.00).
* Result: **Pass** (Difference &dollar;4.50 < Tolerance &dollar;5.00).

## Scenario 4: Large Invoice (Fail)

* Data: An enterprise invoice with 1,000,000 line items with a systematic rounding error (truncation bias).
* Values: CostAndUsage sums to &dollar;5,000,000.00. InvoiceDetail sums to &dollar;5,000,015.00. Difference is **&dollar;15.00**.
* Limit Calculation:
  * Effective Tolerance: **&dollar;5.00**.
* Result: **Fail** (Difference &dollar;15.00 > Tolerance &dollar;5.00).
