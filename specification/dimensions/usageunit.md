# Usage Unit

Usage Unit is the unit of measure for the usage or consumption of a resource or service. Usage Unit is used in conjunction with Quantity In Usage Unit to gain understanding of usage or consumption of a given product or service in an environment.

The UsageUnit column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values when the ChargeType is 'Usage'. UsageUnit should be expressed as a single unit of measure.  Units of measure used in UsageUnit SHOULD adhere to the values and format requirements specified in the Recommended Values section below.  The UsageUnit column MUST not be used as the basis for determining values related to any pricing or cost metric.

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

The Usage Unit for a particular line item may differ from PricingUnit when providers use different units, unit increments, or columns to determine cost. The values in UsageUnit and QuantityInUsageUnit are often listed at a finer granularity or over a different time interval than the PricingUnit and QuantityInPricingUnit. While UsageUnit may appear to relate to pricing and cost, UsageUnit is focused on resource or service consumption.  It is essential not to confuse UsageUnit with PricingUnit which is the basis for determining cost. 

The unit of measure for the usage or consumption of a resource or service

### Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

### Recommended Values

Usage units SHOULD be expressed as a single unit of measure adhering to one of the following three formats.

* `<plural-units>` - "GB", "Seconds"
* `<singular-unit> <plural-time-units>` - "GB Hours", "MB Days"
* `<plural-units>/<singular-time-unit>` - "GB/Hour", "PB/Day"

Usage units MAY be expressed with a unit quantity or time interval.  If a unit quantity or time interval is used, the unit quantity or time interval MUST be expressed as a whole number.  The following formats are valid.

* `<quantity> <plural-units>` - "1000 Tokens", "1000 Characters"
* `<plural-units>/<interval> <plural-time-units>` - "Units/3 Months"

### Recommended Usage Unit Values

Unit values and components of the UnitName column MUST use a capitalization scheme that is consistent with the capitalization scheme used in this section if that term is listed in this section. For example, a value of "gigabyte seconds" would not be compliant with this specification as the terms "gigabyte" and "second" are listed in this section with the appropriate capitalization.  If the unit is not listed in the table, it is to be used over a functional equivalent with similar meaning.

UsageUnit SHOULD be composed of the list of recommended units listed in this section unless the UsageUnit value covers a dimension not listed in the recommended unit set or if the unit covers a count-based unit distinct from recommended values in the count dimension listed in this section.  

#### Data Size Unit Names

Data size MUST be abbreviated using the following standard abbreviations.  Each data size abbreviation can be considered both the singular and plural form of the unit.  For example, "GB" is both the singular and plural form of the unit "GB".  The following table lists the valid data size units.

| Data size in bits    | Data size in bytes    |
| -------------------- | --------------------- |
| Kib (kibibit = 2^10) | KiB (kibibyte = 2^10) |
| Mib (mebibit = 2^20) | MiB (mebibyte = 2^20) |
| Gib (gibibit = 2^30) | GiB (gibibyte = 2^30) |
| Tib (tebibit = 2^40) | TiB (tebibyte = 2^40) |
| Pib (pebibit = 2^50) | PiB (pebibyte = 2^50) |
| Eib (exbibit = 2^60) | EiB (exbibyte = 2^60) |
| Kb (kilobit = 10^3)  | KB (kilobyte = 10^3)  |
| Mb (megabit = 10^6)  | MB (megabyte = 10^6)  |
| Gb (gigabit = 10^9)  | GB (gigabyte = 10^9)  |
| Tb (terabit = 10^12) | TB (terabyte = 10^12) |
| Pb (petabit = 10^15) | PB (petabyte = 10^15) |
| Eb (exabit = 10^15)  | EB (exabyte = 10^15)  |

#### Count-based Unit Names

A count-based unit is a noun that represents a discrete number of items, events, or services.  For example, a count-based unit can be used to represent the number of requests, instances, tokens, or connections.  

If the list of recommended values does not cover a count-based unit, a provider may introduce a new noun representing a count-based unit.  All nouns appearing in UsageUnit that are not listed in the recommended values table will be considered count-based units.  A new count-based unit value MUST be capitalized.

| Count        |
|--------------|
| Count        |
| Unit         |
| Request      |
| Token        |
| Connection   |
| Certificate  |
| Domain       |
| Core         |


#### Time-based Unit Names

A time-based unit is a noun that represents a time interval.  Time-based units can be used to measure consumption over a time interval or in combination with another unit to capture a rate of consumption.

| Time         |
|--------------|
| Year         |
| Month        |
| Day          |
| Hour         |
| Minute       |
| Second       |

### Composite Units

If the UsageUnit value is a composite value made from combinations of one or more units, each component MUST also align with the set of recommended values.

Instead of "per" or "-" to denote a Composite Unit, slash ("/") and space(" ") must be used as a common convention.  Count-based units like requests, instances, and tokens SHOULD be expressed using a value listed in the count dimension.  For example, if a usage unit is measured as a rate of requests or instances over a period of time, the unit should be listed as "count/day" to signify the number of requests per day.

## Introduced (version)

1.0
