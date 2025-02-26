# Pricing Denomination

[*Pricing Denomination*](#glossary:pricing-denomination) is a value that represents the unit of measure in which a charge for [*resources*](#glossary:resource) or [*services*](#glossary:service) was priced. Pricing Denomination is commonly used in scenarios where costs need to be grouped or aggregated by proprietary units of measure.

The unit of measure may be one of the following types: 

 * Currency (e.g. USD, EUR).
 * Non-currency consumable unit (e.g. tokens, credits).

The PricingDenomination column adheres to the following requirements:

* PricingDenomination presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingDenomination MUST be present in a FOCUS dataset when the provider presents prices in a non-currency consumable unit of measure (e.g. credits, tokens).
  * PricingDenomination MUST be present in a FOCUS dataset when the provider presents prices and bills in different currencies (e.g. prices are presented in USD and billed in EUR).
  * PricingDenomination MAY be present in a FOCUS dataset in all other cases.
* PricingDenomination MUST be of type String.
* PricingDenomination MUST conform to [Pricing Denomination Format](#pricingdenominationformat) requirements.
* PricingDenomination nullability is defined as follows:
  * PricingDenomination MUST NOT be null when the provider presents prices in a presents prices in a non-currency consumable unit of measure (e.g. credits, tokens).
  * PricingDenomination MUST NOT be null when the provider presents prices and bills in different currencies (e.g. prices are presented in USD and billed in EUR).
  * PricingDenomination MAY be null in all other cases.

## Column ID

PricingDenomination

## Display Name

Pricing Denomination

## Description

Represents the unit of measure in which a charge was priced.

## Content Constraints

| Constraint      | Value                               |
|:----------------|:------------------------------------|
| Column type     | Dimension                           |
| Feature level   | Conditional                         |
| Allows nulls    | True                                |
| Data type       | String                              |
| Value format    | [Pricing Denomination Format](#pricingdenominationformat) |

## Introduced (version)

1.2
