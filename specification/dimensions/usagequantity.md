# Usage Quantity

Usage Quantity is the amount of resources or services consumed. The Usage Quantity is measured in units specified by the Usage Unit. Usage Quantity may differ from a Pricing Quantity when providers use a different unit of measure for calculating cost. Usage Quantity is often used when analyzing environments to gain understanding of usage or consumption of a given product/service in an environment.

Usage Quantity MUST exist in billing data. The column MUST be a numeric value and MUST NOT contain nulls.

The value of UsageQuantity MUST be a non-negative, real number with a single value greater than or equal to zero. The single numeric value in this column can be expressed as integer, decimal value, or scientific notation. Fractional notation or a value expressed with an arithmetic operator (e.g. 1/2) is not permitted.  Multiple values, arrays, or ranges are not permitted in the UsageUnit dimension. Numerical values expressed with mathematical symbol, operators, or exponent values not required for scientific notation are not permitted.

* Examples of valid values for Usage Quantity are "0", "1", "1.5", "1.234", "1.23342 x 10^7"
* Examples of invalid values for Usage Quantity are "-100", "1 1/2", "[3,5,8]", "[4:5]", "5i + 4", "sqrt(2)", "2.3^3"

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
