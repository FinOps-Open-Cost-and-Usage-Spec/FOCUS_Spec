# Payment Currency Invoice Detail ID

[Payment Currency Invoice Detail ID](#col) is a reference to the [Invoice Detail ID](#col) of the record where the [Payment Currency Billed Cost](#col) for the current row is aggregated. This identifier enables practitioners to explicitly link granular usage records to their corresponding aggregate records stated in their chosen currency for settlement, ensuring accurate reconciliation across divergent grains.

## Requirements

[PaymentCurrencyInvoiceDetailId](#col) MUST adhere to the following requirements:

* [PaymentCurrencyInvoiceDetailId](#col) MUST be of type String.
* [PaymentCurrencyInvoiceDetailId](#col) MUST conform to [StringHandling](#attr) requirements.
* [PaymentCurrencyInvoiceDetailId](#col) MUST NOT be null.
* [PaymentCurrencyInvoiceDetailId](#col) MUST match the [InvoiceDetailId](#col) of the record representing the [PaymentCurrencyBilledCost](#col) aggregation for the current row.
* [PaymentCurrencyInvoiceDetailId](#col) MUST match [InvoiceDetailId](#col) of the current record when [PaymentCurrencyBilledCost](#col) is non-zero.

## Column ID

PaymentCurrencyInvoiceDetailId

## Display Name

Payment Currency Invoice Detail ID

## Description

The identifier linking a granular record to the specific [Invoice Detail](#ds) record where its [Payment Currency Billed Cost](#col) is represented or aggregated.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | [Includes Aggregation Level Currency Differences](#omc)                                                                  |
| Column type                | Dimension                                  |
| Feature level              | Conditional                                |
| Allows nulls               | False                                      |
| Data type                  | String                                     |
| Value format               | \<not specified>                           |

## Version Introduced

1.4
