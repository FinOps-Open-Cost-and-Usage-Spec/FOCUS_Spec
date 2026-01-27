# Purchase Order Number

A Purchase Order Number is the unique customer-issued identifier for tracking the lifecycle of a purchase. This identifier is typically provided by the customer to the invoice issuer to ensure that charges are mapped to specific internal procurement records or purchase orders.

## Requirements

PurchaseOrderNumber adheres to the following requirements:

* PurchaseOrderNumber MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset) if the provider supports customer input of purchase order numbers.
* PurchaseOrderNumber MUST be of type String.
* PurchaseOrderNumber MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PurchaseOrderNumber MUST represent the identifier used by the customer to unique identify the purchase order responsible for the charge.

## Column ID

PurchaseOrderNumber

## Display Name

Purchase Order Number

## Description

The unique customer-issued identifier for tracking the lifecycle of a purchase.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Conditional                     |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | <unspecified>                   |

## Introduced (version)

1.4