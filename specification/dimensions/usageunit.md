# Usage Unit

Usage Unit refers to a unit of measurement for the purchase or consumption of resources or services. The Usage Unit for a particular line item may differ from the published Pricing Unit when providers use different units, unit increments, or dimensions for calculating cost.  This unit is commonly used when auditing or reconciling consumption or billing data.

The UsageUnit column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values when the ChargeType is 'Usage'. UsageUnit should be expressed as a single unit of measure adhering to the values and format requirements specified in the Allowed Values section below.

If the UsageUnit value is a composite value made from combinations of one or more units, each component MUST also align with the set of allowed values.

UsageUnit MUST be composed of the list of recommended units listed in "Allowed Values" below unless the UsageUnit value covers a dimension not listed in the recommended unit set or if the unit covers a count-based unit distinct from allowed values in the count dimension listed in "Allowed Values."  

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

A unit of measurement for the consumption of resources or services

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | list-of-values |

## Allowed Values

Usage units MUST be expressed as a single unit of measure adhering one of the following three formats.

* &lt;plural-units&gt; - "GB", "Seconds"
* &lt;singular-unit&gt; &lt;plural-time-units&gt; - "GB Hours", "MB Days"
* &lt;plural-units&gt;/&lt;singular-time-unit&gt; - "GB/Hour", "PB/Day"

Unit names are listed in this section with the appropriate capitalization.  If the unit is not listed in the table, it is to be used over a functional equivalent with similar meaning or incompatible capitalization.  

The following tables list the valid singular units for 3 dimensions of measurement: time, data, and count.  

| Time         | Count        |
|--------------|--------------|
| Day          | Count        |
| Hour         | Unit         |
| Minute       | Request      |
| Second       | Token        |
|              | Connection   |
|              | Certificate  |
|              | Domain       |
|              | Core         |

### Data Size Units

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

### Count-based Units

A count-based unit is a noun that represents a discrete number of items, events, or services.  For example, a count-based unit can be used to represent the number of requests, instances, tokens, or connections.  If the list of allow values does not cover a count-based unit, a provider may introduce a new noun representing a count-based unit.  All nouns appearing in UsageUnit that are not listed in the allowed values table will be considered count-based units.  

Any new count-based units introduced MUST use a capitalization scheme that is consistent with the capitalization scheme used in the allowed values table.  For example, if a provider introduces a new count-based unit "Thing", the capitalization scheme MUST be "Thing" and not "thing" or "THING".

### Composite Units

Instead of "per" or "-" to denote a Composite Unit, slash ("/") must be used as a common convention.  Count based units like requests, instances, tokens SHOULD be expressed using a value listed in the count dimension.  For example, if a usage unit is measured as a rate of requests or instances over a period of time, the unit should be listed as "count/day" to signify the number of requests per day.

## Introduced (version)

1.0
