# Sub Account ID

A sub account is an optional provider-supported construct for organizing resources and services connected to a billing account. Some common scenarios for using sub accounts include grouping based on organizational constructs and access management boundaries. Sub accounts must be associated with a billing account as they do not generate invoices. 

A sub account ID provider assigned identifier assigned to a sub account. It is commonly used for cost allocation, reporting, and chargeback purposes.

The SubAccountId column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values. Where a provider doesn't support a sub account construct (only has a billing account), use the BillingAccountId value.


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

* Where a provider doesn’t support a sub account construct, use the BillingAccountId value

## Introduced (version)

0.5

## Appendix

|                              | Billing Account             | Sub / Resource Account     |
|------------------------------|-----------------------------|----------------------------|
| Description                  | A provider-supported construct for isolating invoices *based on consumption (usage - e.g. resources, services and other charge types)*. <br>Billing Accounts may additionally be used for grouping consumption based on organizational constructs and needs. Where supported by the provider, accounts may be used as a boundary for access management.  | An optional provider-supported construct for organizing consumption inside of a Billing Account for reasons other than invoicing. Accounts are used for grouping consumption based on organizational constructs and needs. Where supported by the provider, accounts may be used as a boundary for access management. Accounts must be associated with a Billing Account as they do not generate invoices.                    |
| Generates an invoice?        | Yes                         | No                         |
| Invoiced level               | Self                        | Billing                    |
| Access separation supported? | Optional                    | Optional                   |
| Consumption at level         | Not recommended             | Yes                        |
| Child entities?              |                             |                            |
| Examples                     | AWS, GCP, Azure, Snowflake  | AWS, GCP, Azure, Snowflake |