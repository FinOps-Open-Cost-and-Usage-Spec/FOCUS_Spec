# Usage Quantity

Usage Quantity is the amount of resources or services consumed. The Usage Quantity is measured in units specified by the Usage Unit. Usage Quantity may differ from a Pricing Quantity when providers use a different unit of measure for calculating cost. Usage Quantity is often used when analyzing environments to gain understanding of usage or consumption of a given product/service in an environment.


Usage Quantity MUST exist in billing data. The column MUST be a numeric value and MUST NOT contain nulls.

## Column ID

usage_quantity

## Display name

Usage Quantity

## Description

## Content constraints

| Constraint      | Value        |
|-----------------|--------------|
| Column required | True         |
| Data type       | Numeric      |
| Allows nulls    | False        |
| Value format    | number-range |
| Number range    | [8,16]       |
| String format   |              |

## Introduced (version)

1.0
