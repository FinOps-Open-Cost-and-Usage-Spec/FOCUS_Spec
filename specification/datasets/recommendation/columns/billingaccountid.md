# Billing Account ID

A Billing Account ID is an invoice-issuer-assigned identifier for a [*billing account*](#glossary:billing-account). In the Recommendation dataset, Billing Account ID identifies the *billing account* under which the resource or service targeted by a recommendation is billed. This is the account associated with the [Service Provider Name](#datasets.recommendation.serviceprovidername), not the account of the [Recommendation Provider Name](#datasets.recommendation.recommendationprovidername). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

BillingAccountId MUST adhere to the following requirements:

* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* BillingAccountId MUST adhere to the following nullability requirements:
  * BillingAccountId MUST be null when a recommendation is not associated with a single *billing account*.
  * BillingAccountId SHOULD NOT be null when a recommendation is associated with a single *billing account*.
  * BillingAccountId MAY be null when the associated *billing account* is not known to the *data generator*.
* When BillingAccountId is not null, BillingAccountId MUST adhere to the following requirements:
  * BillingAccountId MUST be a unique identifier within an [*invoice issuer*](#glossary:invoice-issuer).
  * BillingAccountId SHOULD be a fully-qualified identifier.

## Column ID

BillingAccountId

## Display Name

Billing Account ID

## Description

The identifier assigned to a *billing account* by the invoice issuer.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
