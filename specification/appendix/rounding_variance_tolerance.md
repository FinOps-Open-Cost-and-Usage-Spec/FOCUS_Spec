---
dataset: CostAndUsage
---

# Rounding Variance Tolerance

When performing invoice reconciliation between the [Cost and Usage](#ds) dataset and an invoice (either the payable invoice itself, or the [Invoice Detail](#ds) dataset), the totals may not be perfectly equal due to precision differences (e.g., 6 decimals in detailed cost data vs. 2 decimals in invoice data). The following tolerance formula allows for a maximum rounding error based on the statistical probability of rounding variance, which grows with the square root of the row count.

## Tolerance Formula

The tolerance used when comparing aggregated [BilledCost](#col) values is defined as:

Tolerance = `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)`

Where:

* **Rows** — The number of [CostAndUsage](#ds) rows included in the aggregation for the relevant [CostAndUsage.InvoiceIssuerName](#col:CostAndUsage.InvoiceIssuerName), [CostAndUsage.InvoiceId](#col:CostAndUsage.InvoiceId), and (if applicable) [CostAndUsage.InvoiceDetailId](#col:CostAndUsage.InvoiceDetailId).
* **Subunit** — The numeric value of the smallest subunit of [CostAndUsage.BillingCurrency](#col:CostAndUsage.BillingCurrency) (for example, `0.01` for USD or `1` for JPY).

The tolerance is the **greater** of the following values:

* **100 × Subunit** — Establishes a fixed minimum tolerance equal to 100 units of the smallest currency subunit.
* **(SQRT(Rows) × 0.5) × Subunit** — Provides a tolerance that increases with the square root of the number of rows to account for rounding accumulation in larger datasets.

## Scenario 1: Small Invoice (Pass)

* Data: A small invoice with 5 underlying [CostAndUsage](#ds) rows.
* Values: [CostAndUsage](#ds) sums to $12.50. [InvoiceDetail](#ds) sums to $12.52. Difference is **$0.02**.
* Limit Calculation:
  * Statistical Limit: `SQRT(5) * 0.5 * 0.01` = $0.011.
  * Floor Limit: `100 * 0.01` = $1.00.
  * Effective Tolerance: **$1.00** (Greater of $0.011 and $1.00).
* Result: **Pass** (Difference $0.02 < Tolerance $1.00).

## Scenario 2: Small Invoice (Fail)

* Data: A small invoice with 5 underlying [CostAndUsage](#ds) rows where a $5.00 charge is missing from [CostAndUsage](#ds).
* Values: [CostAndUsage](#ds) sums to $10.00. [InvoiceDetail](#ds) sums to $15.00. Difference is **$5.00**.
* Limit Calculation:
  * Effective Tolerance: **$1.00**.
* Result: **Fail** (Difference $5.00 > Tolerance $1.00).

## Scenario 3: Large Invoice (Pass)

* Data: An enterprise invoice with 1,000,000 underlying [CostAndUsage](#ds) rows.
* Values: [CostAndUsage](#ds) sums to $5,000,000.00. [InvoiceDetail](#ds) sums to $5,000,004.50. Difference is **$4.50**.
* Limit Calculation:
  * Statistical Limit: `SQRT(1,000,000) * 0.5 * 0.01` = $5.00.
  * Floor Limit: `100 * 0.01` = $1.00.
  * Effective Tolerance: **$5.00** (Greater of $5.00 and $1.00).
* Result: **Pass** (Difference $4.50 < Tolerance $5.00).

## Scenario 4: Large Invoice (Fail)

* Data: An enterprise invoice with 1,000,000 underlying [CostAndUsage](#ds) rows with a systematic rounding error (truncation bias).
* Values: [CostAndUsage](#ds) sums to $5,000,000.00. [InvoiceDetail](#ds) sums to $5,000,015.00. Difference is **$15.00**.
* Limit Calculation:
  * Effective Tolerance: **$5.00**.
* Result: **Fail** (Difference $15.00 > Tolerance $5.00).
