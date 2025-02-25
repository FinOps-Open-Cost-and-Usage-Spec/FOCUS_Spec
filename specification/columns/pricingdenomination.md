# Pricing Denomination

[*Pricing denomination*](#glossary:pricing-denomination) is an identifier that represents the proprietary unit of measure (e.g. credits, tokens) in which a charge for [*resources*](#glossary:resource) or [*services*](#glossary:service) was priced. Pricing Denomination is commonly used in scenarios where costs need to be grouped or aggregated.

The PricingDenomination column adheres to the following requirements:

* PricingDenomination MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider presents prices in a proprietary, non-currency unit of measure (e.g. credits, tokens).
* PricingDenomination MUST be of type String.
* PricingDenomination MUST conform to [Pricing Denomination Format](#pricingdenominationformat) requirements.
* PricingDenomination MUST NOT be null when the provider presents prices in a proprietary, non-currency unit of measure (e.g. credits, tokens).

## Column ID

PricingDenomination

## Display Name

Pricing Denomination

## Description

Represents the proprietary unit of measure in which a charge was priced.

## Content Constraints

| Constraint      | Value                               |
|:----------------|:------------------------------------|
| Column type     | Dimension                           |
| Feature level   | Optional                            |
| Allows nulls    | True                                |
| Data type       | String                              |
| Value format    | [Pricing Denomination Format](#pricingdenominationformat) |

## Introduced (version)

1.2
