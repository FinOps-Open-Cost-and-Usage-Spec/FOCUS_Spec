# Purchase Payment Model

Purchase Payment Model defines the financial settlement structure of a purchase. It identifies whether the financial obligation is settled via a single upfront payment, distributed recurring charges, or a combination of both over the [Purchase Duration Type](#datamodel.skuprice.purchasedurationtype). When the purchase is a [*commitment discount*](#glossary:commitment-discount), this column represents the settlement structure of that *commitment discount*.

Purchase Payment Model has three possible values: "No Upfront", "Partial Upfront", and "All Upfront".

* "No Upfront" denotes that the obligation is settled entirely through recurring charges with no initial payment.
* "Partial Upfront" denotes that the obligation is settled through a combination of an initial payment and recurring charges.
* "All Upfront" denotes that the obligation is settled via a single payment at the start of the duration.

## Requirements

PurchasePaymentModel MUST adhere to the following requirements:

* PurchasePaymentModel MUST be of type String.
* PurchasePaymentModel MUST adhere to the following nullability requirements:
  * PurchasePaymentModel MUST be null when [ChargeCategory](#datamodel.skuprice.chargecategory) is "Usage".
  * PurchasePaymentModel MUST be null when ChargeCategory is "Credit".
  * PurchasePaymentModel MUST NOT be null when ChargeCategory is "Purchase".
* PurchasePaymentModel MUST be one of the allowed values when present.

## Allowed Values

| Value           | Sort Order | Description                                                                                  | Typical Use Case                                              |
| --------------- | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| No Upfront      | 10         | The obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment. | Pay-as-you-go Savings Plans or monthly-billed SaaS. |
| Partial Upfront | 20         | The obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges). | Hybrid RIs or EAs with a "Year 1" deposit plus installments. |
| All Upfront     | 30         | The total obligation is settled via a single payment at the start of the duration. | High-discount RIs or multi-year contracts paid in full Day 1. |

## Implementation Guidance

Within the SKU Price dataset, the Purchase Payment Model describes how the fee for a purchase is settled, across purchase constructs such as reservations, prepaid licenses, and commitment discounts:

* **All Upfront:** The full obligation is settled by a single fee at the start of the term.
* **No Upfront:** The obligation is settled through periodic fees over the term, with no initial payment.
* **Partial Upfront:** The obligation combines an initial fee and periodic fees, typically represented across multiple SKU Price records (e.g., one record for the upfront fee and a separate record for the recurring fee).

## Column ID

PurchasePaymentModel

## Display Name

Purchase Payment Model

## Description

Defines the financial settlement structure of a purchase.

## Content Constraints

| Constraint      | Value                                                                                      |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                                                            |
| Conditions      | [Includes Purchases](#conditions.includespurchases)                                        |
| Column type     | Dimension                                                                                  |
| Feature level   | Conditional                                                                                |
| Allows nulls    | True                                                                                       |
| Data type       | String                                                                                     |
| Value format    | Allowed values                                                                             |

## Version Introduced

1.5
