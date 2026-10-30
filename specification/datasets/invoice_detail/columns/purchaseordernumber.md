# Purchase Order Number

[Purchase Order Number](#col) is the unique customer-issued identifier for tracking the lifecycle of a purchase. This identifier is typically provided by the customer to the [invoice issuer](#term) to ensure that charges are mapped to specific internal procurement records or purchase orders.

## Requirements

[PurchaseOrderNumber](#col) MUST adhere to the following requirements:

* [PurchaseOrderNumber](#col) MUST be of type String.
* [PurchaseOrderNumber](#col) MUST conform to [StringHandling](#attr) requirements.
* [PurchaseOrderNumber](#col) MAY be null.
* [PurchaseOrderNumber](#col) MUST represent the identifier used by the customer to uniquely identify the purchase order responsible for the charge.

## Column ID

PurchaseOrderNumber

## Display Name

Purchase Order Number

## Description

The unique customer-issued identifier for tracking the lifecycle of a purchase.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | [Includes Purchase Order Numbers](#omc)                                                   |
| Column type                | Dimension                                  |
| Feature level              | Conditional                                |
| Allows nulls               | True                                       |
| Data type                  | String                                     |
| Value format               | \<not specified>                           |

## Version Introduced

1.4
