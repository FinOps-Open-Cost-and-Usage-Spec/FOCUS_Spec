# Contract Commitment Availability

Contract Commitment Availiability indicates whether the pricing and terms of a [*contract commitment*](#glossary:contract-commitment) are based on a standard, publicly accessible offering or have been specifically brokered through private negotiation.

Contract Commitment Availiability has two possible values: **Public** and **Negotiated**.  Public availability denotes terms and pricing that are generally available to all customers via a provider’s standard rate card or portal.  Negotiated availability denotes terms and pricing that have been specifically modified through an agreement between the customer and the service provider.

## Implementation Context

* Use Public as your baseline for market comparison. 
* Use Negotiated to track the efficacy of your procurement team's discount efforts.

Sensitivity Note: Records marked as Negotiated often fall under non-disclosure agreements (NDAs). This field can serve as a metadata tag for data masking or access control when sharing reports with third parties.

## Requirements

ContractCommitmentAvailability adheres to the following requirements:

* ContractCommitmentAvailability MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentAvailability MUST be of type String.
* ContractCommitmentAvailability MUST NOT be null.
* ContractCommitmentAvailability MUST be one of the allowed values.

## Column ID

ContractCommitmentAvailability

## Display Name

Contract Commitment Availability

## Description

Indicates whether the pricing and terms of a [*contract commitment*](#glossary:contract-commitment) are based on a standard, publicly accessible offering or have been specifically brokered through private negotiation.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                                                                                                        | Typical Use Case                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Public     | Terms that are generally available to all customers via a provider’s standard rate card or portal.                 | Standard Savings Plans or Reserved Instances purchased via the cloud console without a custom discount.         |
| Negotiated | Terms and pricing that have been specifically modified through an agreement between the customer and the provider. | Enterprise Agreements (EA), private marketplace offers, or custom SaaS contracts with volume-based discounting. |

## Introduced (version)

1.4
