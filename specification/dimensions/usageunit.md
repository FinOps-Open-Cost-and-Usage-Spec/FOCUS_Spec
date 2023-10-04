# Usage Unit

Usage Unit refers to a unit of measurement for the consumption or usage of resources or services. The Usage Unit for a particular line item may differ from the published Pricing Unit when providers use different units, unit increments, or dimensions for calculating cost.  This unit is commonly used when auditing or reconciling consumption or billing data.

The UsageUnit column MUST be present and MUST NOT be null or empty. UsageUnit is of type String.

Instead of "per" or "-" to denote a Composite Unit, slash ("/") SHOULD be used as a common convention.  Count based units like requests, instances, tokens SHOULD be expressed as "count".  For example, if a usage unit is measured as a rate of requests or instances over a period of time, the unit should be listed as "count/day" to signify the number of requests per day.

## Mandatory Alignment with Recommended Unit Set

UsageUnit MUST be composed of the list of recommended units or unit abbreviations listed in "Recommended Unit Set" below unless the UsageUnit value covers a dimension not listed in the recommended unit set.  If the UsageUnit value is a composite value made from combinations of one or more units, each component MUST also align with the set of recommended units or unit abbreviations.

This specification requires alignment with recommended units or unit abbreviations to ensure consistency and compatibility across providers, but it allows providers to adapt to emerging units or dimensions as they are introduced.

For example, if a UsageUnit value is "requests/day", the unit "count/day" MUST be used instead as "requests" is not a recommended unit.  In another example, if a UsageUnit must cover distance or length, a new unit term may be introduced as the recommended unit set listed in this specification does not cover a distance of the length dimension.  

Another example of a non-compliant value illustrates that count-based units must align with the recommended unit set.  If a UsageUnit captures "tokens/sec", the unit "count/sec" MUST be used instead as "tokens" is not a recommended unit.  Any unit that consists of a number of events, occurrences, or instances MUST be expressed as "count" to maintain compatibility with this specification.

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

The following table lists the valid units for 3 dimensions of measurement: time, data, and count.  

| Time             | Data      | Count        |
|------------------|-----------|--------------|
| yr: year         | bit: bit  | cnt: count   |
| mo: month        | B: byte   |              |
| wk: week         |           |              |
| d: day           |           |              |
| h: hour          |           |              |
| min: minute      |           |              |
| s: second        |           |              |
| ms: millisecond  |           |              |
| us: microsecond  |           |              |
| ns: nanosecond   |           |              |

Each unit can be associated with a numeric prefix to multiply the value by a defined power of ten.  The following table lists the valid numeric prefixes.

| NUMERIC PREFIXES        |
|-------------------------|
| Ki: kibi (2^10)         |
| Mi: mebi (2^20)         |
| Gi: gibi (2^30)         |
| Ti: tebi (2^40)         |
| Pi: pebi (2^50)         |
| Ei: exbi (2^60)         |
| K: kilo (10^3)          |
| M: mega (10^6)          |
| G: giga (10^9)          |
| T: tera (10^12)         |
| P: peta (10^15)         |
| E: exa (10^15)          |

## Introduced (version)

1.0
