# Usage Unit

Usage Unit is the unit of measure for the usage or consumption of a resource or service. Usage Unit is used in conjunction with Usage Quantity to gain understanding of usage or consumption of a given product or service in an environment.

UsageUnit for a particular line item may differ from units, unit increments, or columns to determine cost. The values in UsageUnit and UsageQuantity are often listed at a finer granularity or over a different time interval than columns used to determine cost. While UsageUnit may appear to relate to pricing and cost, UsageUnit is focused on resource or service consumption.  UsageUnit must not be used as the basis for determining values related to any pricing or cost metric.

The UsageUnit column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values when the ChargeType is 'Usage'. UsageUnit should be expressed as a single unit of measure.  Units of measure used in UsageUnit SHOULD adhere to the values and format requirements specified in the Unit Format attribute.  The UsageUnit column MUST not be used as the basis for determining values related to any pricing or cost metric.

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

Unit of measure for the usage or consumption of a resource or service

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | Unit Format     |

## Introduced (version)

1.0
