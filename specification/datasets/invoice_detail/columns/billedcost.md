# Billed Cost

Billed Cost represents the cost of a [*charge*](#glossary:charge) as invoiced by the [invoice issuer](#datasets.invoicedetail.invoiceissuername) in a given [*billing period*](#glossary:billing-period).

For all *charges*, Billed Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For purchase *charges*, Billed Cost includes any portion invoiced in the given *billing period*. For usage *charges*, Billed Cost excludes any portion covered by related purchase *charges* (e.g., *commitments*, pre-payments, or marketplace purchases), regardless of when those related charges are invoiced.

Billed Cost is denominated in the [Billing Currency](#datasets.invoicedetail.billingcurrency). Billed Cost is commonly used to support FinOps activities, including invoice reconciliation, [*cash-flow-based*](#glossary:cash-based-accounting) forecasting, budgeting, and cost allocation.

## Requirements

BilledCost adheres to the following requirements:

* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be 0 for *charges* where payments are received by a third party (e.g., marketplace transactions).
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MUST match the payable amount provided in the corresponding entries on the issued invoice when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Issued".
* When comparing BilledCost and [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername), BilledCost adheres to the following requirements:
  * The sum of BilledCost for a given [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) when [ChargeCategory](#datasets.invoicedetail.chargecategory) = "Tax" or [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open".
  * Otherwise, the sum of BilledCost for a given [InvoiceId](#datasets.invoicedetail.invoiceid) MUST match the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid).
* When comparing BilledCost and [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername), BilledCost adheres to the following requirements:
  * The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername) when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open".
  * Otherwise, the sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MUST match the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername).

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
