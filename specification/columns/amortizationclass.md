# Amortization Class

Amortization Class indicates how a row in a [*FOCUS dataset*](#glossary:FOCUS-dataset) relates to [*amortization*](#glossary:amortization). Amortization Class is used to identify and distinguish between the charges before and after *amortization* is applied. Amortization Class is commonly used to quantify cost savings accurately by excluding charges that can be double-counted when aggregating List Cost or Contracted Cost.

The AmortizationClass column adheres to the following requirements:

* AmortizationClass column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *amortization*.
* AmortizationClass MUST be of type String.
* AmortizationClass MUST be "Principal" when the row represents an original charge that is amortized across multiple other rows.
* AmortizationClass MUST be "Amortized Charge" when the row includes *amortization* from a previous charge.
* AmortizationClass MUST be null when it is not the original, principal charge or the effective, amortized charge after *amortization* is applied.

## Column ID

AmortizationClass

## Display Name

Amortization Class

## Description

Indicates how a row relates to amortization to identify and distinguish between the charges before and after amortization is applied.

## Content Constraints

| Constraint    | Value          |
| :------------ | :------------- |
| Column type   | Dimension      |
| Feature level | Conditional    |
| Allows nulls  | True           |
| Data type     | String         |
| Value format  | Allowed values |

Allowed values:

| Value            | Description                                                                                                                       |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| Principal        | Original charge that is amortized over time across multiple rows.                                                                 |
| Amortized Charge | Effective charge after the principal amount is amortized over time based on the associated ChargePeriodStart and ChargePeriodEnd. |

## Introduced (version)

1.2
