# Publisher

A Publisher is an entity that produced the resources and/or services that were purchased. It is commonly used for cost analysis and reporting scenarios.

The Publisher column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Origination of cost data](#origination-of-cost-data) section for examples of Provider, Publisher and Invoice Issuer values that can be used for various purchasing scenarios.

## Column ID

Publisher

## Display name

Publisher

## Description

The entity that produced the resources and/or services that were purchased.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
