# Pricing Currency Category

[Pricing Currency Category](#col) categorizes the nature of the [Pricing Currency](#col) as either a financial instrument the customer can pay in or a proprietary [consumption currency](#term) issued by the [service provider](#term). This column defines whether multiplying a usage amount by the unit price results in a base financial cost (["Payable"](#val:PricingCurrencyCategory)) or a virtual cost balance (["Consumable"](#val:PricingCurrencyCategory)). For a ["Consumable"](#val:PricingCurrencyCategory) rate, a mandatory secondary lookup is required to determine the actual financial cost. For a ["Payable"](#val:PricingCurrencyCategory) rate, a secondary currency conversion is only required if the customer's billed currency differs from the pricing currency.

## Requirements

[PricingCurrencyCategory](#col) MUST adhere to the following requirements:

* [PricingCurrencyCategory](#col) MUST be of type String.
* [PricingCurrencyCategory](#col) MUST NOT be null.
* [PricingCurrencyCategory](#col) MUST be one of the allowed values.
* [PricingCurrencyCategory](#col) MUST be ["Payable"](#val:PricingCurrencyCategory) when [PricingCurrency](#col) represents a [national currency](#term).
* [PricingCurrencyCategory](#col) MUST be ["Consumable"](#val:PricingCurrencyCategory) when [PricingCurrency](#col) represents a [consumption currency](#term).

## Allowed Values

| Value      | Description                                                                                                                                                             |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payable    | The pricing currency represents a financial medium of exchange the customer can pay in: a *national currency* (e.g., USD, EUR, JPY). Math resulting from this rate yields a base financial cost, though a currency conversion step may still be required if the customer's actual billed currency differs. |
| Consumable | The pricing currency represents a service-provider-specific *consumption currency* (e.g., platform credits, normalized billing units). Math resulting from this rate yields a virtual cost balance within the provider's ecosystem, requiring a mandatory secondary conversion to determine the financial cost. |

## Column ID

PricingCurrencyCategory

## Display Name

Pricing Currency Category

## Description

Categorizes the nature of the [Pricing Currency](#col) as either a financial instrument the customer can pay in (["Payable"](#val:PricingCurrencyCategory)) or a proprietary consumption currency issued by the [service provider](#term) (["Consumable"](#val:PricingCurrencyCategory)).

## Content Constraints

| Constraint                 | Value                           |
| :------------------------- | :------------------------------ |
| Dataset                    | [SKU Price](#ds)                 |
| Operating Model Conditions | Not applicable                  |
| Column type                | Dimension                       |
| Feature level              | Mandatory                       |
| Allows nulls               | False                           |
| Data type                  | String                          |
| Value format               | Allowed values                  |

## Version Introduced

Preview: 1.5
