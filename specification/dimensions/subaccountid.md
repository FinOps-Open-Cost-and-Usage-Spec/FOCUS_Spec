# Sub Account ID

A sub account is an optional provider-supported construct for organizing resources and services connected to a billing account. Some common scenarios for using sub accounts include grouping based on organizational constructs and access management boundaries. Sub accounts must be associated with a billing account as they do not generate invoices. 

A sub account ID provider assigned identifier assigned to a sub account. It is commonly used for cost allocation, reporting, and chargeback purposes.

The SubAccountId column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values. Where a provider doesn't support a sub account construct (only has a billing account), use the BillingAccountId value.

[Link to Appendix]()

## Column ID

SubAccountId

## Display name

Sub Account ID

## Description

An ID assigned to a grouping of resources, often used to manage access and/or cost.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False*          |
| Value format    | \<not specified> |

* Where a provider doesn't support a sub account construct, use the BillingAccountId value

## Introduced (version)

0.5