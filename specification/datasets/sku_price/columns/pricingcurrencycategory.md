# Pricing Currency Category

Pricing Currency Category categorizes the nature of the [Pricing Currency](#datasets.skuprice.pricingcurrency) as either a financial instrument paid by the customer or a proprietary [*consumption currency*](#glossary:consumption-currency) issued by the [*service provider*](#glossary:service-provider). This column defines whether multiplying a usage amount by the unit price results in a final financial cost ("Payable") or a virtual cost balance that requires a secondary lookup to determine the actual financial cost ("Consumable").

## Requirements

PricingCurrencyCategory MUST adhere to the following requirements:

* PricingCurrencyCategory MUST be of type String.
* PricingCurrencyCategory MUST NOT be null.
* PricingCurrencyCategory MUST be one of the allowed values.

## Allowed Values

| Value      | Description                                                                                                                                                             |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payable    | The pricing currency represents the financial medium of exchange the customer uses to pay for the offering; typically a [*national currency*](#glossary:national-currency) (e.g., USD, EUR, JPY). Math resulting from this rate yields a final financial cost. |
| Consumable | The pricing currency represents a service-provider-specific consumption currency (e.g., platform credits, normalized billing units). Math resulting from this rate yields a virtual cost balance within that provider's ecosystem, not a final financial cost. |

## Column ID

PricingCurrencyCategory

## Display Name

Pricing Currency Category

## Description

Categorizes the nature of the Pricing Currency as either a financial instrument paid by the customer (`Payable`) or a proprietary consumption currency issued by the *service provider* (`Consumable`).

## Content Constraints

| Constraint      | Value                           |
| :-------------- | :------------------------------ |
| Dataset         | [SKU Price](#datasets.skuprice) |
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | Allowed values                  |

## Version Introduced

1.5
