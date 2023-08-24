# List Unit Price

The List Unit Price represents the suggested provider published price for a single pricing measurement unit, which incorporates volume/tier-based reductions while excluding any negotiated or commitment based discounts. This price is denominated in the pricing currency. It is used to calculate List Cost and savings based on rate optimization activities.

The ListUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal, within the range of valid positive decimal values and MUST NOT contain null values in case of usage-based charges.

## Column ID

ListUnitPrice

## Display name

List Unit Price

## Description

Represents the suggested provider published price for a single pricing measurement unit, which incorporates volume/tier-based reductions while excluding any negotiated or commitment based discounts.

## Content Constraints

| Constraint      | Value                            |
|:----------------|:---------------------------------|
| Column required | True                             |
| Data type       | Decimal                          |
| Allows nulls    | True                             |
| Value format    | Numeric value                    |
| Number range    | Any valid positive decimal value |

## Introduced (version)

1.0
