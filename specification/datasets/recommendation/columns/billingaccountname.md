# Billing Account Name

A Billing Account Name is a display name assigned to a [*billing account*](#glossary:billing-account). In the Recommendation dataset, the Billing Account Name is used to make billing-account-scoped recommendations readable without resolving the [Billing Account ID](#datasets.recommendation.billingaccountid). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

BillingAccountName MUST adhere to the following requirements:

* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* BillingAccountName MUST adhere to the following nullability requirements:
  * BillingAccountName MUST NOT be null when the *billing account* has a display name that is assigned by the [*invoice issuer*](#glossary:invoice-issuer) and available to the [data generator](#metadata.datagenerator).
  * BillingAccountName MAY be null when the *billing account* has no display name assigned by the *invoice issuer*, or when the display name is not available to the data generator.

## Column ID

BillingAccountName

## Display Name

Billing Account Name

## Description

The display name assigned to a *billing account*.

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
