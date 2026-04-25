# Payment Currency Invoice Detail ID

Payment Currency Invoice Detail ID is a reference to the [Invoice Detail ID](#datasets.invoicedetail.invoicedetailid) of the record where the [Payment Currency Billed Cost](#datasets.invoicedetail.paymentcurrencybilledcost) for the current row is aggregated. This identifier enables practitioners to explicitly link granular usage records to their corresponding aggregate records stated in their chosen currency for settlement, ensuring accurate reconciliation across divergent grains.

## Requirements

PaymentCurrencyInvoiceDetailId MUST adhere to the following requirements:

* PaymentCurrencyInvoiceDetailId MUST be of type String.
* PaymentCurrencyInvoiceDetailId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PaymentCurrencyInvoiceDetailId MUST NOT be null.
* PaymentCurrencyInvoiceDetailId MUST match the [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid) of the record representing the [PaymentCurrencyBilledCost](#datasets.invoicedetail.paymentcurrencybilledcost) aggregation for the current row.
* PaymentCurrencyInvoiceDetailId MUST match [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid) of the current record when [PaymentCurrencyBilledCost](#datasets.invoicedetail.paymentcurrencybilledcost) is non-zero.

## Column ID

PaymentCurrencyInvoiceDetailId

## Display Name

Payment Currency Invoice Detail ID

## Description

The identifier linking a granular record to the specific [Invoice Detail](#datasets.invoicedetail) record where its [Payment Currency Billed Cost](#datasets.invoicedetail.paymentcurrencybilledcost) is represented or aggregated.

## Content Constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Dataset         | [Invoice Detail](#datasets.invoicedetail)             |
| Column type     | Dimension                       |
| Feature level   | Conditional                     |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | \<unspecified>                  |

## Introduced (version)

1.4
