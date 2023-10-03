# Usage Unit

Usage Unit refers to a unit of measurement for the consumption or usage of resources or services. The Usage Unit for a particular line item may differ from the published Pricing Unit when providers use different units, unit increments, or dimensions for calculating cost.  This unit is commonly used when auditing or reconciling consumption or billing data.

The UsageUnit column MUST be present and MUST NOT be null or empty. UsageUnit is of type String, and UsageUnit MUST be composed of the list of recommended units or unit abbreviations if it is possible to be expressed with the units listed in "Recommended Unit Set" below. If the UsageUnit value is a composite value made from combinations of one or more units, each component MUST also align with the set of recommended units if possible.  For example, a composite unit of "GB/Month" is allowed.

Instead of "per" or "-" to denote a Composite Unit, slash ("/") SHOULD be used as a common convention.  Count based units like requests, instances, tokens SHOULD be expressed as "count".  For example, if a usage unit is measured as a rate of requests or instances over a period of time, the unit should be listed as "count/day" to signify the number of requests per day.

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

Units listed in the following table are presented in the following format: "abbreviation: unit (numeric prefix unit)".  Unit names are all listed with the appropriate capitalization, and abbreviations are all listed in lowercase.  The numeric prefix unit is optional, and if present, the numeric prefix unit MUST be used in conjunction with a unit.  For example, "KiB" is allowed, but "Ki" is not allowed.  

If the unit is not listed in the table, it is to be used over a functional equivalent with similar meaning or incompatible capitalization.  An example of unit now allowed is a unit such as "calls" or "number" to signify the number of times an event occurred in this case, the unit "count" MUST be used to maintain compatibility with this specification.

| TIME_UNIT        | DATA_UNIT | COUNT_UNIT   | NUMERIC PREFIXES        |
|------------------|-----------|--------------|-------------------------|
| yr: year         | bit: bit  | cnt: count   | Ki: kibi (2^10)         |
| mo: month        | B: byte   |              | Mi: mebi (2^20)         |
| wk: week         |           |              | Gi: gibi (2^30)         |
| d: day           |           |              | Ti: tebi (2^40)         |
| h: hour          |           |              | Pi: pebi (2^50)         |
| min: minute      |           |              | K: kilo (10^3)          |
| s: second        |           |              | M: mega (10^6)          |
| ms: millisecond  |           |              | G: giga (10^9)          |
| us: microsecond  |           |              | T: tera (10^12)         |
| ns: nanosecond   |           |              | P: peta (10^15)         |

## Introduced (version)

1.0
