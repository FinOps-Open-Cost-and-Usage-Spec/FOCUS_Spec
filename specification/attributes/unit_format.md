# Unit Format

Billing data frequently captures data measured in units related to data size, count, time, and other [*dimensions*](#glossary:dimension). The Unit Format attribute provides a standard for expressing units of measure in columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

Key concepts used in Unit Format:

* Measurement Unit: a standardized expression that describes how quantities in a *FOCUS dataset* are denominated (e.g., `GB`, `Seconds`, `GB-Hours`, `10 GB/Hour`, `Units/3 Months`).
* Base Unit: an atomic unit of measurement that serves as a building block for all measurement units; can be a data size unit, time-based unit, or count-based unit (e.g., `GB`, `Hour`, `Token`).
* Simple Unit: a measurement unit that contains exactly one base unit, optionally preceded by a unit quantity (e.g., `GB`, `Seconds`, `1000 Tokens`).
* Compound Unit: a measurement unit that combines two base units using a hyphen (`-`) to express a quantity sustained over a period, optionally preceded by a unit quantity (e.g., `GB-Hours`, `MB-Days`).
* Ratio Unit: a measurement unit that expresses one base unit per another using a slash (`/`), optionally including a denominator quantity (e.g., `GB/Hour`, `Units/3 Months`).
* Unit Quantity: a positive integer included in a measurement unit, indicating the granularity of measurement (e.g., `1000` in `1000 Tokens`).
* Denominator Quantity: a positive integer included in the denominator of a ratio unit, indicating the granularity of the denominator (e.g., `3` in `Units/3 Months`).

## Attribute ID

UnitFormat

## Attribute Name

Unit Format

## Description

Indicates standards for expressing measurement units in columns appearing in a *FOCUS dataset*.

## Requirements

Column conforming to UnitFormat attribute MUST adhere to the following requirements:

* *FOCUS dataset* column MUST adhere to the following base unit requirements:
  * *FOCUS dataset* column MUST include at least one base unit.
  * *FOCUS dataset* column MUST use one of the allowed data size unit abbreviations listed below for data size base units.
  * *FOCUS dataset* column MUST use the allowed data size unit abbreviations in the same form for both singular and plural units.
  * *FOCUS dataset* column MUST use the allowed abbreviation for exabit, exabyte, exbibit, or exbibyte when representing values exceeding 10^18.
  * *FOCUS dataset* column MUST use the allowed abbreviation for bit or byte when representing values smaller than one byte.
  * *FOCUS dataset* column MUST use one of the allowed time-based unit names listed below for time-based base units.
  * *FOCUS dataset* column SHOULD use one of the recommended count-based unit names listed below for count-based base units.
  * *FOCUS dataset* column MAY include a count-based base unit that is not listed as one of the allowed values.
  * *FOCUS dataset* column SHOULD use capitalized nouns for base units that do not correspond to any of the allowed base unit names listed below.
* *FOCUS dataset* column MUST use a hyphen ("-") to separate base units when expressing a compound unit (e.g., "GB-Hours").
* *FOCUS dataset* column MUST use a slash ("/") to separate the numerator and denominator when expressing a ratio unit (e.g., "GB/Hour" to signify gigabytes per hour).
* *FOCUS dataset* column SHOULD use the `<plural-units>` format when expressing a simple unit (e.g., "GB", "Seconds").
* *FOCUS dataset* column SHOULD use the `<singular-unit>-<plural-time-units>` format when expressing a compound unit (e.g., "GB-Hours", "MB-Days").
* *FOCUS dataset* column SHOULD use the `<plural-units>/<singular-time-unit>` format when expressing a ratio unit with a time denominator (e.g., "GB/Hour", "PB/Day").
* *FOCUS dataset* column MAY include a unit quantity expressed as a positive integer.
* *FOCUS dataset* column SHOULD use the `<unit-quantity> <plural-units>` format when a unit quantity is included (e.g., "1000 Tokens", "1000 Characters").
* *FOCUS dataset* column MAY include a denominator quantity expressed as a positive integer when the *FOCUS dataset* column represents a ratio unit.
* *FOCUS dataset* column SHOULD use the `<plural-units>/<denominator-quantity> <plural-time-units>` format when the *FOCUS dataset* column represents a ratio unit and a denominator quantity is included (e.g., "Units/3 Months").

## Base Unit Names

### Allowed Data Size Unit Abbreviations

Data size units are nouns representing data size measured in bits or bytes, expressed using standard abbreviations. Each abbreviation can be used for both the singular and plural form of the unit.

For example:

* "GB" represents both the singular and plural form of a gigabyte.
* "TB" is a valid base unit name, while "TBs" and "terabyte" are considered invalid.

Values larger than 10^18 must use the abbreviation for exabit, exabyte, exbibit, or exbibyte. Values smaller than a byte must use the abbreviation for bit or byte.

The table below lists the valid abbreviations for data size units from a single bit or byte to 10^18 bits or bytes.

| Data size in bits    | Data size in bytes    |
| :------------------- | :-------------------- |
| b (bit) = 10^1       | B (byte = 10^1)       |
| Kb (kilobit = 10^3)  | KB (kilobyte = 10^3)  |
| Mb (megabit = 10^6)  | MB (megabyte = 10^6)  |
| Gb (gigabit = 10^9)  | GB (gigabyte = 10^9)  |
| Tb (terabit = 10^12) | TB (terabyte = 10^12) |
| Pb (petabit = 10^15) | PB (petabyte = 10^15) |
| Eb (exabit = 10^18)  | EB (exabyte = 10^18)  |
| Kib (kibibit = 2^10) | KiB (kibibyte = 2^10) |
| Mib (mebibit = 2^20) | MiB (mebibyte = 2^20) |
| Gib (gibibit = 2^30) | GiB (gibibyte = 2^30) |
| Tib (tebibit = 2^40) | TiB (tebibyte = 2^40) |
| Pib (pebibit = 2^50) | PiB (pebibyte = 2^50) |
| Eib (exbibit = 2^60) | EiB (exbibyte = 2^60) |

### Allowed Time-based Unit Names

Time-based units are nouns representing a discrete time period. They can be used alone to indicate duration, combined with another unit to form a compound unit (e.g., "GB-Hours"), or a per-time ratio unit (e.g., "GB/Hour").

The table below lists allowed time-based base units.

| Time-based Unit (Singular) | Time-based Unit (Plural) |
|:---------------------------|:-------------------------|
| Year                       | Years                    |
| Month                      | Months                   |
| Day                        | Days                     |
| Hour                       | Hours                    |
| Minute                     | Minutes                  |
| Second                     | Seconds                  |

### Recommended Count-based Unit Names

A count-based unit is a noun representing a discrete number of items, events, or actions. For example, a count-based unit can represent the number of requests, instances, tokens, or connections.

The table below lists recommended names for count-based base units.

| Count-based Unit (Singular) | Count-based Unit (Plural) |
|:----------------------------|:--------------------------|
| Count                       | Counts                    |
| Unit                        | Units                     |
| Request                     | Requests                  |
| Token                       | Tokens                    |
| Connection                  | Connections               |
| Certificate                 | Certificates              |
| Domain                      | Domains                   |
| Core                        | Cores                     |

*Note: If a count-based base unit is not covered by the recommended values, a new value may be used as long as it is capitalized.*

## Introduced (version)

1.0-preview
