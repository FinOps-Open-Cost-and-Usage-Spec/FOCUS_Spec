# Amortization Category

Amortization Category represents the various classifications of a charge 
based on it's eligibility for coverage by a commitment discount, and 
whether or not a commitment discount was actually applied.

Amortization Category is used to identify and distinguish between types of charges 
that may require different handling, for example an upfront payment on 
a Savings Plan that is amortized over time into usage by other line items.

The AmortizationCategory column adheres to the following requirements:

* The AmortizationCategory column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.

## Column ID

AmortizationCategory

## Display Name

Amortization Category

## Description

Represents the various classifications of a charge 
based on it's eligibility for coverage by a commitment discount, and 
whether or not a commitment discount was actually applied.

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
| Commitment Purchase | Original charge that is amortized over time into usage by other line items. |
| Eligible - Covered | Usage that is discounted or covered by a commitment discount |
| Eligible - Not Covered | Usage that could be covered by some form of commitment discount, but is not |
| Not Applicable | Usage that is ineligible for commitment discounts of any kind. |
## Introduced (version)

1.2
