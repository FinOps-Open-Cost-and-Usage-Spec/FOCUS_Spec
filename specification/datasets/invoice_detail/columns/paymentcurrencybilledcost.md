# Payment Currency Billed Cost

A Payment Currency Billed Cost represents the [Billed Cost](#datasets.invoicedetail.billedcost) as expressed in [Payment Currency](#datasets.invoicedetail.paymentcurrency). This metric is essential for organizations that need to reconcile their financial records in the currency used for actual settlement, especially when it differs from the currency used for initial billing.

## Requirements

PaymentCurrencyBilledCost adheres to the following requirements:

* PaymentCurrencyBilledCost MUST be of type Decimal.
* PaymentCurrencyBilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PaymentCurrencyBilledCost MUST NOT be null.
* PaymentCurrencyBilledCost MUST be a valid decimal value.
* PaymentCurrencyBilledCost MUST be 0 for *charges* where payments are received by a third party (e.g., marketplace transactions).
* PaymentCurrencyBilledCost MAY be non-zero while [BilledCost](#datasets.invoicedetail.billedcost) is 0 when PaymentCurrencyBilledCost represents the aggregation of BilledCost amounts (denominated in [PaymentCurrency](#datasets.invoicedetail.paymentcurrency)) stated in other records.
* PaymentCurrencyBilledCost MAY be 0 while [BilledCost](#datasets.invoicedetail.billedcost) is non-zero when BilledCost (denominated in [PaymentCurrency](#datasets.invoicedetail.paymentcurrency)) is represented in a separate aggregate record.

## Examples

### Example 1: Consistent Grain
In this scenario, the invoice issuer performs currency conversion at the individual line-item level. The grain of the payment currency matches the grain of the billing currency exactly.

* **Billing Currency:** USD
* **Payment Currency:** EUR
* **Exchange Rate:** 1.00 USD = 0.92 EUR

| ChargeCategory | ChargeDescription | BillingCurrency | BilledCost | PaymentCurrency | PaymentCurrencyBilledCost |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Usage | Compute Instance A | USD | 100.00 | EUR | 92.00 |

### Example 2: Divergent Grain
In this scenario, the invoice issuer tracks usage in the billing currency at a granular level but represents that cost in the payment currency as a separate aggregate record. This is often done to maintain precision and avoid rounding discrepancies.

* **Billing Currency:** USD
* **Payment Currency:** EUR
* **Effective Exchange Rate:** 1.00 USD = 0.92 EUR

| ChargeCategory | ChargeDescription | BillingCurrency | BilledCost | PaymentCurrency | PaymentCurrencyBilledCost |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Usage | Compute Instance A | USD | 45.00 | EUR | 0.00 |
| Usage | Compute Instance B | USD | 55.00 | EUR | 0.00 |
| Usage | Usage in Payment Currency | USD | 0.00 | EUR | 92.00 |

**Logic Breakdown:**
* **Rows 1 & 2:** `PaymentCurrencyBilledCost` is 0 because the `BilledCost` (denominated in `PaymentCurrency`) is represented in a separate aggregate record (Row 3).
* **Row 3:** `BilledCost` is 0 because the `PaymentCurrencyBilledCost` represents the aggregation of `BilledCost` amounts (denominated in `PaymentCurrency`) stated in other records (Rows 1 & 2).
* **Total Reconciliation:** Summing `BilledCost` (100.00) and `PaymentCurrencyBilledCost` (92.00) at the invoice level allows for the calculation of the effective exchange rate.

## Column ID

PaymentCurrencyBilledCost

## Display Name

Payment Currency Billed Cost

## Description

The [Billed Cost](#datasets.invoicedetail.billedcost) as expressed in [Payment Currency](#datasets.invoicedetail.paymentcurrency).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Conditional             |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#attributes.numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.4