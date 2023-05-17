# Provider

A Provider is an entity that made the infrastructure and/or services available for purchase. It is commonly used for cost analysis and reporting scenarios.

The Provider column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Origination of the cost data](../appendix/origination_of_cost_data.md) section for context (Provider/Publisher/Invoicing Entity) in various purchasing scenarios.

## Column ID

Provider

## Display name

Provider

## Description

The entity that made the infrastructure and/or services available for purchase.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
