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
  * Otherwise, the absolute difference between the sum of BilledCost for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) and the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) MUST NOT exceed the count of [CostAndUsage](#datasets.costandusage) rows multiplied by 0.5 times the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency) (e.g., 0.01 for USD).
* When comparing BilledCost and [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername), BilledCost MUST adhere to the following requirements:
  * The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open".
  * Otherwise, the absolute difference between the sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) and the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) MUST NOT exceed the count of [CostAndUsage](#datasets.costandusage) rows multiplied by 0.5 times the smallest subunit of the [BillingCurrency](#datasets.invoicedetail.billingcurrency) (e.g., 0.01 for USD).

## Implementation Guidance

### Handling Rounding Discrepancies

When validating InvoiceDetail.BilledCost against [CostAndUsage.BilledCost](#datasets.costandusage.billedcost), exact matches are not expected due to precision differences (e.g., 6 decimals in CostAndUsage vs. 2 decimals in InvoiceDetail). The requirement allows for a maximum rounding error based on the number of CostAndUsage rows and the [BillingCurrency](#datasets.invoicedetail.billingcurrency) precision.

### Tolerance Formula

Tolerance = ([CostAndUsage](#datsets.costandusage) rows) x 0.5 x (Smallest Subunit of [BillingCurrency](#datasets.invoicedetail.billingcurrency))

### Examples

* Scenario 1: High Volume (Pass)
  * Data: 1,000 CostAndUsage rows sum to &dollar;150.492. InvoiceDetail sums to &dollar;152.00. Difference is &dollar;1.508.
  * Limit: 1,000 * 0.5 * &dollar;0.01 = &dollar;5.00.
  * Result: Pass (Difference $1.508 < Limit &dollar;5.00).

* Scenario 2: Missing Data (Fail)
  * Data: 50 CostAndUsage rows sum to &dollar;5,400.00. InvoiceDetail sums to &dollar;5,350.00. Difference is &dollar;50.00.
  * Limit: 50 * 0.5 * &dollar;0.01 = &dollar;0.25.
  * Result: Fail (Difference &dollar;50.00 > Limit &dollar;0.25).

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

Cost of a *charge* as invoiced by the *invoice issuer* in a given *billing period*.

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#attributes.numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.4
