# Contract Applied Cost

Contract Applied Cost represents the cost of the charge applied to the contract.  Contract Applied Cost is applied to the contract via [Contract ID](#contractid).  Contract Applied Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as negotiated between a provider and a customer.

The ContractAppliedCost column adheres to the following requirements:

* ContractAppliedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *negotiated discounts*.
* ContractAppliedCost MUST be of type Decimal.
* ContractAppliedCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractAppliedCost nullability is defined as follows:
  * ContractAppliedCost MUST be null when [Contract ID](#contractid) is null.
  * ContractAppliedCost MUST NOT be null when [Contract ID](#contractid) is not null.
* ContractAppliedCost MUST be a valid decimal value.
* ContractAppliedCost MUST be denominated in the BillingCurrency.

## Column ID

ContractAppliedCost

## Display Name

Contract Applied Cost

## Description

The cost of the *charge* applied to the contract.

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
