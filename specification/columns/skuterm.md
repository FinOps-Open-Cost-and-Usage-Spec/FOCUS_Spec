# SKU Term

A SKU Term refers to the predetermined length of time under which a commitment-based discount applies. This term is agreed upon contractually and can vary depending on the pricing models, payment options, and specific requirements of the user and provider. During this term, the user commits to use a certain amount of a specific type of usage, such as virtual machines or databases, in exchange for a discounted unit price. The SKU Term is an essential part of a commitment-based discount, dictating the duration of the contractual agreement. The duration of the term can be diverse, ranging from months to multiple years.

The SkuTerm column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values for charges related to a commitment-based discount. The SkuTerm column MUST conform to the following format: Numerical value followed by a space and a time unit. The time unit MUST be one of the following allowed values: hour, day, week, month, year. The numerical value MUST be an integer. The SkuTerm column MUST NOT contain any other values than the ones specified above.

## Column ID

SkuTerm

## Display Name

SKU Term

## Description

The length of the commitment-based discount.

## Content constraints

| Constraint      | Value                       |
| :-------------- | :-------------------------- |
| Column required | True                        |
| Data type       | String                      |
| Allows nulls    | False                       |
| Value format    | Integer + Space + Time Unit |

Allowed values:

### Time Unit

| Value |
| :---- |
| hour  |
| day   |
| week  |
| month |
| year  |

## Introduced (version)

1.0
