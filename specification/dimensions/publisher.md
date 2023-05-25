# Publisher

A Publisher is an entity that produced the resources and/or services that were purchased. It is commonly used for cost
analysis and reporting scenarios.

The Publisher column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null
values.

See [Appendix: Origination of cost data](#originationofcostdata) section for examples of Provider, Publisher and
Invoice Issuer values that can be used for various purchasing scenarios.

## Column ID

PublisherName

## Display Name

Publisher

## Description

The name of the entity that produced the resources and/or services that were purchased.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
