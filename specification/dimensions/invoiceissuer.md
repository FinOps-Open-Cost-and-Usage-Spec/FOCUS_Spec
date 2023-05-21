# Invoice Issuer

An Invoice Issuer is an entity responsible for invoicing for the resources and/or services consumed. It is commonly used for cost analysis and reporting scenarios.

The InvoiceIssuer column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Origination of cost data](#origination-of-cost-data) section for examples of Provider, Publisher and Invoice Issuer values that can be used for various purchasing scenarios.

## Column ID

InvoiceIssuer

## Display name

Invoice Issuer

## Description

The entity responsible for invoicing for the resources and/or services consumed.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
