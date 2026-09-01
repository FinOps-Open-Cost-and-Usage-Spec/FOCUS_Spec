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

Within the SKU Price dataset, the Purchase Payment Model classifies how the total obligation of a purchase construct (e.g., reservation, prepaid license, or commitment discount) is represented:

* **All Upfront:** The full obligation is represented by a single [*SKU Price*](#glossary:sku-price) record for the one-time upfront payment.
* **No Upfront:** The obligation is represented by a single *SKU Price* record for the deferred payment, with no upfront record.
* **Partial Upfront:** The obligation is represented by two *SKU Price* records — one for the upfront payment and one for the deferred payment.

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
