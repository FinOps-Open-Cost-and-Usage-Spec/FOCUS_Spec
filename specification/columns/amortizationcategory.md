# Amortization Category

Amortization Category represents the classification of a charge based on whether the charge discounts or is amortized into other line items. Amortization Category is used to identify and distinguish between types of charges that may require different handling, for example an upfront payment on a Savings Plan that is amortized over time into usage by other line items.

The AmortizationCategory column adheres to the following requirements:

* The AmortizationCategory column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.

## Column ID

AmortizationCategory

## Display Name

Amortization Category

## Description

Represents the classification of a charge based on whether it is amortized into or otherwise benefits other line items.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value            | Description                          |
| :--------------- | :------------------------------------|
| Principal        | Original charge that is amortized over time into usage by other line items. |
| Amortized Charge | Rows that receive the benefit of the original principal payment |

## Introduced (version)

1.2
