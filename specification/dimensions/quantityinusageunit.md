# Quantity In Usage Unit

Quantity In Usage Unit is the amount of resources or services consumed. The Quantity In Usage Unit is measured in units specified by the Usage Unit. Quantity In Usage Unit may differ from a Quantity In Pricing Unit when providers use a different unit of measure for calculating cost. Quantity In Usage Unit is often used when analyzing environments to gain understanding of usage or consumption of a given product/service in an environment.

Quantity In Usage Unit MUST exist in billing data. The column MUST be a numeric value and MUST NOT contain nulls.

## Column ID

quantity_in_usage_unit

## Display name

Quantity In Usage Unit

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
