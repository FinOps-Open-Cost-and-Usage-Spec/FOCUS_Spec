# Billed Cost

Billed Cost represents the cost of a [*charge*](#glossary:charge) as invoiced by the [invoice issuer](#datasets.costandusage.invoiceissuername) in a given [*billing period*](#glossary:billing-period). Billed Cost differs from [Effective Cost](#datasets.costandusage.effectivecost) when *charges* (both pre-paid and post-paid) are invoiced separately from usage.

For all *charges*, Billed Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For purchase *charges*, Billed Cost includes any portion invoiced in the given *billing period*. For usage *charges*, Billed Cost excludes any portion covered by related purchase *charges* (e.g., *commitments*, pre-payments, or marketplace purchases), regardless of when those related charges are invoiced.

Billed Cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Billed Cost is commonly used to support FinOps activities, including invoice reconciliation, [*cash-flow-based*](#glossary:cash-based-accounting) forecasting, budgeting, and cost allocation.

## Requirements

BilledCost MUST adhere to the following requirements:

* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* BilledCost MUST reflect all applicable pricing adjustments, including but not limited to *negotiated discounts*, *commitment discounts*, and other applicable discount programs.
* BilledCost MUST NOT include any portion covered by related purchase *charges*.
* BilledCost MUST reflect amounts as invoiced by the [InvoiceIssuerName](#datasets.costandusage.invoiceissuername), not estimated or inferred values.
* Entities that are not responsible or authorized for invoicing this *charge* MUST NOT generate *charges* with non-zero BilledCost to avoid double-counting when merging multiple datasets.
* The sum of BilledCost for a given [InvoiceId](#datasets.costandusage.invoiceid) and [InvoiceIssuerName](#datasets.costandusage.invoiceissuername) MUST match the payable amount provided on the corresponding issued invoice.

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

Cost of a *charge* as invoiced by the *invoice issuer* in a given *billing period*.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

0.5
