# Contract Applied Quantity

Contract Applied Quantity represents the quantity of the charge applied to the contract.  Contract Applied Quantity is applied to the contract via [Contract ID](#contractid).  Contract Applied Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as negotiated between a provider and a customer.

The ContractAppliedQuantity column adheres to the following requirements:

* ContractAppliedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *negotiated discounts*.
* ContractAppliedQuantity MUST be of type Decimal.
* ContractAppliedQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* ContractAppliedQuantity nullability is defined as follows:
  * ContractAppliedQuantity MUST be null when [Contract ID](#contractid) is null.
  * ContractAppliedQuantity MUST NOT be null when [Contract ID](#contractid) is not null.
* ContractAppliedQuantity MUST be a valid decimal value.

## Column ID

ContractAppliedQuantity

## Display Name

Contract Applied Quantity

## Description

The quantity of the *charge* applied to the contract.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Conditional             |
| Allows nulls    | True                    |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.3
