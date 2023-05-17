# Provider

An Invoicing Entity is an entity responsible for invoicing for the infrastructure and/or services consumed. It is commonly used for cost analysis and reporting scenarios.

The InvoicingEntity column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Origination of the cost data](../appendix/origination_of_cost_data.md) section for context (Provider/Publisher/Invoicing Entity) in various purchasing scenarios.

## Column ID

InvoicingEntity

## Display name

Invoicing Entity

## Description

The entity responsible for invoicing for the infrastructure and/or services consumed.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
