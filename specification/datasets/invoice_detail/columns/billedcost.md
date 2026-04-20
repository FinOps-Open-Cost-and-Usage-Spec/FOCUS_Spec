# Billed Cost

Billed Cost represents the cost of a [*charge*](#glossary:charge) as invoiced by the [invoice issuer](#datasets.invoicedetail.invoiceissuername) in a given [*billing period*](#glossary:billing-period).

For all *charges*, Billed Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For purchase *charges*, Billed Cost includes any portion invoiced in the given *billing period*. For usage *charges*, Billed Cost excludes any portion [*covered*](#glossary:covered-charge) by related purchase *charges* (e.g., [*covering charges*](#glossary:covering-charge) such as *commitments*, prepayments, or marketplace purchases), regardless of when those related *charges* are invoiced.

Billed Cost is denominated in the [Billing Currency](#datasets.invoicedetail.billingcurrency). Billed Cost is commonly used to support FinOps activities, including invoice reconciliation, [*cash-based*](#glossary:cash-based-accounting) forecasting, budgeting, and cost allocation.

## Requirements

BilledCost MUST adhere to the following requirements:

* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be denominated in the BillingCurrency.
* BilledCost MUST reflect all applicable pricing adjustments, including but not limited to *negotiated discounts*, *commitment discounts*, and other applicable discount programs.
* BilledCost MUST NOT include any portion of a [*covered charge*](#glossary:covered-charge) that is offset by a [*covering charge*](#glossary:covering-charge).
* BilledCost MUST be 0 for *charges* that are fully *covered* by one or more *covering charges*.
* The sum of BilledCost for a given [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) MUST match the payable amount provided in the corresponding entries on the issued invoice when [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Issued".
* When comparing BilledCost aggregated by [InvoiceId](#datasets.invoicedetail.invoiceid) and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) with [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) aggregated by [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername), BilledCost MUST adhere to the following requirements:
  * When [ChargeCategory](#datasets.invoicedetail.chargecategory) is not "Tax" and [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is not "Open", the sum of BilledCost MUST NOT differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) by more than `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)` as defined in [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).
  * When [ChargeCategory](#datasets.invoicedetail.chargecategory) is "Tax" or [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open", the sum of BilledCost MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost).
* When comparing BilledCost aggregated by [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid), [InvoiceId](#datasets.invoicedetail.invoiceid), and [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) with [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) aggregated by [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid), [CostAndUsage.InvoiceId](#datasets.costandusage.invoiceid), and [CostAndUsage.InvoiceIssuerName](#datasets.costandusage.invoiceissuername), BilledCost MUST adhere to the following requirements:
  * When [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is not "Open", the sum of BilledCost MUST NOT differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost) by more than `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)` as defined in [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).
  * When [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus) is "Open", the sum of BilledCost MAY differ from the sum of [CostAndUsage.BilledCost](#datasets.costandusage.billedcost).

## Implementation Guidance

### Handling Rounding Discrepancies

When validating InvoiceDetail.BilledCost against [CostAndUsage.BilledCost](#datasets.costandusage.billedcost), exact matches are not expected due to precision differences (e.g., 6 decimals in CostAndUsage vs. 2 decimals in InvoiceDetail). The requirement allows for a maximum rounding error based on the statistical probability of rounding variance, which grows with the square root of the row count. For more information, see the [Rounding Variance Tolerance](#appendix.roundingvariancetolerance) appendix entry.

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

Cost of a *charge* as invoiced by the [*invoice issuer*](#glossary:invoice-issuer) in a given *billing period*.

## Content Constraints

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
