# Billed Cost

Billed Cost represents the cost of a [*charge*](#glossary:charge) as invoiced by the [invoice issuer](#datasets.invoicedetail.invoiceissuername) in a given [*billing period*](#glossary:billing-period).

For all *charges*, Billed Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For purchase *charges*, Billed Cost includes any portion invoiced in the given *billing period*. For usage *charges*, Billed Cost excludes any portion covered by related purchase *charges* (e.g., *commitments*, pre-payments, or marketplace purchases), regardless of when those related charges are invoiced.

Billed Cost is denominated in the [Billing Currency](#datasets.invoicedetail.billingcurrency). Billed Cost is commonly used to support FinOps activities, including invoice reconciliation, [*cash-flow-based*](#glossary:cash-based-accounting) forecasting, budgeting, and cost allocation.

## Requirements

BilledCost MUST adhere to the following requirements:

* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be 0 for *charges* where payments are received by a third party (e.g., marketplace transactions).
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MUST match the payable amount provided in the corresponding entries on the issued invoice when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Issued".
* When comparing BilledCost and [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername), BilledCost MUST adhere to the following requirements:
  * The sum of BilledCost for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) when [ChargeCategory](#datasets.invoicedetail.chargecategory) = "Tax" or [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open".
  * Otherwise, the absolute difference between the sum of BilledCost for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) and the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) MUST NOT exceed the **greater** of:
    * 100 units of the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency) (e.g., 1.00 for USD, 100 for JPY).
    * The square root of the count of [CostAndUsage](#datasets.costandusage) rows multiplied by 0.5 times the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency).
* When comparing BilledCost and [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername), BilledCost MUST adhere to the following requirements:
  * The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open".
  * Otherwise, the absolute difference between the sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) and the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) MUST NOT exceed the **greater** of:
    * 100 units of the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency) (e.g., 1.00 for USD, 100 for JPY).
    * The square root of the count of [CostAndUsage](#datasets.costandusage) rows multiplied by 0.5 times the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency).

## Implementation Guidance

### Handling Rounding Discrepancies

When validating InvoiceDetail.BilledCost against [CostAndUsage.BilledCost](#datasets.costandusage.billedcost), exact matches are not expected due to precision differences (e.g., 6 decimals in CostAndUsage vs. 2 decimals in InvoiceDetail). The requirement allows for a maximum rounding error based on the statistical probability of rounding variance, which grows with the square root of the row count.

### Tolerance Formula

Tolerance = `MAX(100 * Subunit, SQRT(Rows) * 0.5 * Subunit)`

* Rows: The count of related [CostAndUsage](#datsets.costandusage) rows.
* Subunit: The smallest subunit of [BillingCurrency](#datasets.invoicedetail.billingcurrency) (e.g., 0.01 for USD, 1 for JPY).
* 100 * Subunit: Represents a universal floor of 100 "ticks" of precision to prevent false positives on small files, regardless of currency scale.

### Scenario 1: Small Invoice (Pass)

* Data: A small invoice with 5 line items.
* Values: CostAndUsage sums to &dollar;12.50. InvoiceDetail sums to &dollar;12.52. Difference is **&dollar;0.02**.
* Limit Calculation:
  * Statistical Limit: `SQRT(5) * 0.5 * 0.01` = &dollar;0.011.
  * Floor Limit: `100 * 0.01` = &dollar;1.00.
  * Effective Tolerance: **&dollar;1.00** (Greater of &dollar;0.011 and &dollar;1.00).
* Result: **Pass** (Difference &dollar;0.02 < Tolerance &dollar;1.00).

### Scenario 2: Small Invoice (Fail)

* Data: A small invoice with 5 line items where a &dollar;5.00 charge is missing from CostAndUsage.
* Values: CostAndUsage sums to &dollar;10.00. InvoiceDetail sums to &dollar;15.00. Difference is **&dollar;5.00**.
* Limit Calculation:
  * Effective Tolerance: **&dollar;1.00**.
* Result: **Fail** (Difference &dollar;5.00 > Tolerance &dollar;1.00).

### Scenario 3: Large Invoice (Pass)

* Data: An enterprise invoice with 1,000,000 line items.
* Values: CostAndUsage sums to &dollar;5,000,000.00. InvoiceDetail sums to &dollar;5,000,004.50. Difference is **&dollar;4.50**.
* Limit Calculation:
  * Statistical Limit: `SQRT(1,000,000) * 0.5 * 0.01` = &dollar;5.00.
  * Floor Limit: `100 * 0.01` = &dollar;1.00.
  * Effective Tolerance: **&dollar;5.00** (Greater of &dollar;5.00 and &dollar;1.00).
* Result: **Pass** (Difference &dollar;4.50 < Tolerance &dollar;5.00).

### Scenario 4: Large Invoice (Fail)

* Data: An enterprise invoice with 1,000,000 line items with a systematic rounding error (truncation bias).
* Values: CostAndUsage sums to &dollar;5,000,000.00. InvoiceDetail sums to &dollar;5,000,015.00. Difference is **&dollar;15.00**.
* Limit Calculation:
  * Effective Tolerance: **&dollar;5.00**.
* Result: **Fail** (Difference &dollar;15.00 > Tolerance &dollar;5.00).

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

Cost of a *charge* as invoiced by the *invoice issuer* in a given *billing period*.

## Content constraints

| Constraint | Value |
| :--- | :--- |
| Column type | Metric |
| Feature level | Mandatory |
| Allows nulls | False |
| Data type | Decimal |
| Value format | [Numeric Format](#attributes.numericformat) |
| Number range | Any valid decimal value |

## Introduced (version)

1.4
