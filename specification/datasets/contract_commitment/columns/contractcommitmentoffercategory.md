# Contract Commitment Offer Category

Contract Commitment Offer Category indicates whether the pricing and terms of a [*contract commitment*](#glossary:contract-commitment) are based on a standard, publicly accessible offering or have been specifically brokered through private negotiation.

Contract Commitment Offer Category has two possible values: **Public** and **Negotiated**. _Public_ denotes terms and pricing that are generally available to all customers via a service provider's standard rate card or portal. _Negotiated_ denotes terms and pricing that have been specifically modified through an agreement between the customer and the service provider.

## Requirements

ContractCommitmentOfferCategory MUST adhere to the following requirements:

* ContractCommitmentOfferCategory MUST be of type String.
* ContractCommitmentOfferCategory MUST NOT be null.
* ContractCommitmentOfferCategory MUST be one of the allowed values.

## Allowed Values

| Value      | Description                                                                                                        | Typical Use Case                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Public     | Terms that are generally available to all customers via a service provider's standard rate card or portal. | Standard Savings Plans or Reserved Instances purchased via the cloud console without a custom discount. |
| Negotiated | Terms and pricing that have been specifically modified through an agreement between the customer and the service provider. | Enterprise Agreements (EA), private marketplace offers, or custom SaaS contracts with volume-based discounting. |

## Implementation Context

* Use Public as your baseline for market comparison.
* Use Negotiated to track the efficacy of your procurement team's discount efforts.

Sensitivity Note: Records marked as Negotiated often fall under non-disclosure agreements (NDAs). This field can serve as a metadata tag for data masking or access control when sharing reports with third parties.

## Column ID

ContractCommitmentOfferCategory

## Display Name

Contract Commitment Offer Category

## Description

Indicates whether the pricing and terms of a [*contract commitment*](#glossary:contract-commitment) are based on a standard, publicly accessible offering or have been specifically brokered through private negotiation.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

## Introduced (version)

1.4
