# Usage Unit

Usage Unit refers to a unit of measurement for consumption or usage of resources or services. Usage Unit may differ from published Pricing Unit when providers use different units,  unit increments, or dimensions for calculating cost.  This unit is commonly used when auditing or reconciling consumption or billing data.

The UsageUnit column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be composed of the list of recommended units if it is possible to be expressed in the set of possible units. Composite units made from combinations of recommended units is also allowed. E.g. GB/Month.Instead of "per" or "-" to denote a Composite Unit, slash ("/") SHOULD be used as a common convention.  Count based units like requests, instances, tokens SHOULD be expressed as count.  

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

A unit of measurement for consumption or usage of resources or services.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Recommended Unit Set

| TIME_UNIT        | DATA_UNIT | COUNT_UNIT   | PREFIXES        |
|------------------|-----------|--------------|-----------------|
| s: second        | bit: bit  | count: count | Ki: kibi (2^10) |
| min: minute      | B: byte   |              | Mi: mebi (2^20) |
| h: hour          |           |              | Gi: gibi (2^30) |
| d: day           |           |              | Ti: tebi (2^40) |
| wk: week         |           |              | Pi: pebi (2^50) |
| mo: month        |           |              | K: Kilo (10^3)  |
| yr: year         |           |              | M: Mega (10^6)  |
| ms: milli-second |           |              | G: Giga (10^9)  |
| us: micro-second |           |              | T: Tera (10^12) |
| ns: nano-second  |           |              | P: Peta (10^15) |

## Introduced (version)

1.0
