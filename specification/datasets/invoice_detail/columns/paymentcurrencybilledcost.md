# Payment Currency Billed Cost

[Payment Currency Billed Cost](#col) represents the [Billed Cost](#col) as expressed in [Payment Currency](#col). This metric is essential for organizations that need to reconcile their financial records in the currency used for actual settlement, especially when it differs from the currency used for initial billing.

## Requirements

[PaymentCurrencyBilledCost](#col) MUST adhere to the following requirements:

* [PaymentCurrencyBilledCost](#col) MUST be of type Decimal.
* [PaymentCurrencyBilledCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PaymentCurrencyBilledCost](#col) MUST NOT be null.
* [PaymentCurrencyBilledCost](#col) MUST be denominated in the [PaymentCurrency](#col).
* [PaymentCurrencyBilledCost](#col) MUST be the [PaymentCurrency](#col)-denominated equivalent of [BilledCost](#col).
* [PaymentCurrencyBilledCost](#col) MAY be non-zero while [BilledCost](#col) is 0 when [PaymentCurrencyBilledCost](#col) represents the aggregation of [BilledCost](#col) amounts (denominated in [PaymentCurrency](#col)) stated in other records.
* [PaymentCurrencyBilledCost](#col) MAY be 0 while [BilledCost](#col) is non-zero when [BilledCost](#col) (denominated in [PaymentCurrency](#col)) is represented in a separate aggregate record.

## Examples

### Example 1: Consistent Grain

In this scenario, the [invoice issuer](#term) performs currency conversion at the individual line-item level. The grain of the payment currency matches the grain of the billing currency exactly.

* **Billing Currency:** USD
* **[Payment Currency](#col):** EUR
* **Exchange Rate:** 1.00 USD = 0.92 EUR

| Column                         | Value  |
| :----------------------------- | :----- |
| InvoiceDetailId                | ID-001 |
| ChargeCategory                 | Usage  |
| BillingCurrency                | USD    |
| BilledCost                     | 100.00 |
| PaymentCurrency                | EUR    |
| PaymentCurrencyBilledCost      | 92.00  |
| PaymentCurrencyInvoiceDetailId | ID-001 |

> **Note:** Because the conversion is 1:1, the `PaymentCurrencyInvoiceDetailId` points to the record's own `InvoiceDetailId`.

### Example 2: Divergent Grain

In this scenario, the invoice issuer tracks usage in the billing currency at a granular level but represents that cost in the payment currency as a separate aggregate record.

* **Billing Currency:** USD
* **[Payment Currency](#col):** EUR
* **Effective Exchange Rate:** 1.00 USD = 0.92 EUR

| Column                         | A-101              | A-102              | Z-999                     |
| :----------------------------- | :----------------- | :----------------- | :------------------------ |
| InvoiceDetailId                | A-101              | A-102              | Z-999                     |
| InvoiceDetailDescription       | Compute Instance A | Compute Instance B | Usage in Payment Currency |
| BilledCost                     | 45.00              | 55.00              | 0.00                      |
| PaymentCurrencyBilledCost      | 0.00               | 0.00               | 92.00                     |
| PaymentCurrencyInvoiceDetailId | Z-999              | Z-999              | Z-999                     |

**Logic Breakdown:**

* **Rows A-101 & A-102:** These are "child" records. Their `PaymentCurrencyBilledCost` is 0, so they provide a pointer in `PaymentCurrencyInvoiceDetailId` to Row **Z-999**, where the financial settlement value is stored.
* **Row Z-999:** This is the "parent" record. It aggregates the costs of the children. To identify itself as the root of this conversion, its `PaymentCurrencyInvoiceDetailId` matches its own `InvoiceDetailId`.
* **Reconciliation:** A practitioner can now sum all `BilledCost` values where `PaymentCurrencyInvoiceDetailId` is **Z-999** to verify that the $100.00 total is equal to the 92.00 EUR settlement using the expected exchange rate.

## Column ID

PaymentCurrencyBilledCost

## Display Name

Payment Currency Billed Cost

## Description

The [Billed Cost](#col) as expressed in [Payment Currency](#col).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Invoice Detail](#ds)                       |
| Operating model conditions | [Includes Billing and Payment Currency Differences](#omc)                                                                   |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | False                                       |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.4
