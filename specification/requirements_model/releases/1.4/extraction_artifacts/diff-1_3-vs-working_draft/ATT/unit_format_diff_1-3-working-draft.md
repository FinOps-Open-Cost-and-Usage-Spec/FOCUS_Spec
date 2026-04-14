## Diff

@@ -1,69 +1,24 @@
## Requirements

[-* Units SHOULD be expressed as a single unit of measure adhering-]{+Column conforming to UnitFormat attribute MUST adhere+} to[-one of-] the following [-three formats.-]{+requirements:+}

* [-`<plural-units>` - "GB", "Seconds"-]
[-  * `<singular-unit>-<plural-time-units>` - "GB-Hours", "MB-Days"-]
[-  * `<plural-units>/<singular-time-unit>` - "GB/Hour", "PB/Day"-]
[-* Units MAY be expressed with a unit quantity or time interval.  If a unit quantity or time interval is used, the unit quantity or time interval-]{+*FOCUS dataset column*+} MUST [-be expressed as a whole number.  The-]{+adhere to the+} following [-formats are valid:-]
[-  * `<quantity> <plural-units>` - "1000 Tokens", "1000 Characters"-]{+base unit requirements:+}
  * [-`<plural-units>/<interval> <plural-time-units>` - "Units/3 Months"-]{+*FOCUS dataset column* MUST include at least one base unit.+}
  * [-Unit values and components of columns using the Unit Format-]{+*FOCUS dataset column*+} MUST use [-a capitalization scheme that is consistent with the capitalization scheme used in this attribute if that term is listed in this section. For example, a value-]{+one+} of[-"gigabyte-seconds" would not be compliant with this specification as the terms "gigabyte" and "second" are listed in this section with the appropriate capitalization.  If-] the {+allowed data size+} unit [-is not-]{+abbreviations+} listed [-in the table, it is to be used over a functional equivalent with a similar meaning with the same capitalization scheme.-]{+below for data size base units.+}
  * [-Units SHOULD be composed of the list of recommended units listed in this section unless the unit value covers a *dimension* not listed in the recommended unit set, or if the unit covers a count-based unit distinct from recommended values in-]{+*FOCUS dataset column* MUST use+} the [-count *dimension* listed in this section.  -]

[-### Data Size Unit Names-]

[-Data-]{+allowed data+} size unit[-names MUST be abbreviated using one of the-] abbreviations in the [-following table.  For example, a unit name of "TB" is a valid unit name, and a unit name of "terabyte" is an invalid unit name. Data size abbreviations can be considered both the singular and plural-]{+same+} form [-of the unit.  For example, "GB" is-]{+for+} both[-the-] singular and plural [-form of the unit "gigabyte", and "GBs" would be an invalid unit name.  Values that exceed 10^18-]{+units.+}
{+  * *FOCUS dataset column*+} MUST use the {+allowed+} abbreviation for exabit, exabyte, exbibit, [-and exbibyte, and-]{+or exbibyte when representing+} values [-smaller than a byte-]{+exceeding 10^18.+}
{+  * *FOCUS dataset column*+} MUST use the {+allowed+} abbreviation for bit or {+byte when representing values smaller than one+} byte.
  [-For example,-]{+* *FOCUS dataset column* MUST use one of+} the [-abbreviation "YB" for "yottabyte" is not a valid data size-]{+allowed time-based+} unit [-name as it represents a value larger than what is-]{+names+} listed [-in the following table.-]

[-The following table lists the valid abbreviations-]{+below+} for [-data size units from a single bit or byte to 10^18 bits or bytes.-]

[-| Data size in bits    | Data size in bytes    |-]
[-| :------------------- | :-------------------- |-]
[-| b (bit) = 10^1       | B (byte = 10^1)       |-]
[-| Kb (kilobit = 10^3)  | KB (kilobyte = 10^3)  |-]
[-| Mb (megabit = 10^6)  | MB (megabyte = 10^6)  |-]
[-| Gb (gigabit = 10^9)  | GB (gigabyte = 10^9)  |-]
[-| Tb (terabit = 10^12) | TB (terabyte = 10^12) |-]
[-| Pb (petabit = 10^15) | PB (petabyte = 10^15) |-]
[-| Eb (exabit = 10^18)  | EB (exabyte = 10^18)  |-]
[-| Kib (kibibit = 2^10) | KiB (kibibyte = 2^10) |-]
[-| Mib (mebibit = 2^20) | MiB (mebibyte = 2^20) |-]
[-| Gib (gibibit = 2^30) | GiB (gibibyte = 2^30) |-]
[-| Tib (tebibit = 2^40) | TiB (tebibyte = 2^40) |-]
[-| Pib (pebibit = 2^50) | PiB (pebibyte = 2^50) |-]
[-| Eib (exbibit = 2^60) | EiB (exbibyte = 2^60) |-]

[-### Count-based Unit Names-]

[-A count-based unit is a noun that represents a discrete number of items, events, or actions.  For example, a count-based unit can be used to represent the number-]{+time-based base units.+}
{+  * *FOCUS dataset column* SHOULD use one+} of[-requests, instances, tokens, or connections.  -]

[-If-] the[-following list of-] recommended[-values does not cover a-] count-based [-unit, a service provider/data generator MAY introduce a new noun representing a-]{+unit names listed below for+} count-based [-unit.  All-]{+base units.+}
{+  * *FOCUS dataset column* SHOULD use capitalized+} nouns [-appearing in-]{+for base+} units that [-are-]{+do+} not [-listed in-]{+correspond to any of+} the [-recommended values table will be considered count-based units.  A new count-based-]{+allowed base+} unit [-value MUST be capitalized.-]

[-| Count        |-]
[-|:-------------|-]
[-| Count        |-]
[-| Unit         |-]
[-| Request      |-]
[-| Token        |-]
[-| Connection   |-]
[-| Certificate  |-]
[-| Domain       |-]
[-| Core         |-]

[-### Time-based Unit Names-]

[-A time-based-]{+names listed below.+}
{+  * *FOCUS dataset column* MAY include a count-based base+} unit {+that+} is {+not listed as one of the allowed values.+}
{+* *FOCUS dataset column* MAY include+} a [-noun that represents-]{+unit quantity expressed as+} a [-time interval.  Time-based units can be used to measure consumption over-]{+positive integer.+}
{+* *FOCUS dataset column* expressing+} a [-time interval or in combination with another-]{+compound+} unit [-to capture-]{+MUST use+} a [-rate of consumption.  Time-based-]{+hyphen (`-`) to separate base+} units [-MUST match one of the values listed in the following table.-]

[-| Time         |-]
[-|:-------------|-]
[-| Year         |-]
[-| Month        |-]
[-| Day          |-]
[-| Hour         |-]
[-| Minute       |-]
[-| Second       |-]

[-### Composite Units-]

[-If the-]{+(e.g., `GB-Hours`).+}
{+* *FOCUS dataset column* expressing a compound+} unit [-value is-]{+SHOULD use the `<singular-base-unit>-<plural-base-unit>` format (e.g., `GB-Hours`, `MB-Days`, `Request-Tokens`).+}
{+* *FOCUS dataset column* expressing+} a [-composite value made from combinations of one or more units, each component-]{+ratio unit+} MUST [-also align with the set of recommended values.-]

[-Instead of "per" or "-" to denote-]{+use+} a[-Composite Unit,-] slash [-("/")-]{+(`/`) to separate the numerator+} and [-space(" ") MUST be used-]{+denominator (e.g., `GB/Hour` to signify gigabytes per hour).+}
{+* *FOCUS dataset column* expressing a ratio unit MAY include a denominator quantity expressed+} as a [-common convention.  Count-based units like requests, instances,-]{+positive integer.+}
{+* *FOCUS dataset column* expressing a ratio unit+} and [-tokens-]{+including a denominator quantity+} SHOULD [-be expressed using-]{+use the `<plural-units>/<denominator-quantity> <plural-time-units>` format (e.g., `Units/3 Months`).+}
{+* *FOCUS dataset column* expressing+} a [-value listed in-]{+ratio unit with a compound unit numerator SHOULD use+} the [-count *dimension*.  For example, if-]{+`<compound-unit>/<singular-time-unit>` format (e.g., `Core-Hours/Day`).+}
{+* *FOCUS dataset column* expressing+} a [-usage-]{+ratio+} unit [-is measured as-]{+with+} a [-rate of requests or instances over-]{+time denominator SHOULD use the `<plural-units>/<singular-time-unit>` format (e.g., `GB/Hour`, `PB/Day`).+}
{+* *FOCUS dataset column* expressing+} a [-period of time,-]{+simple unit SHOULD use+} the {+`<plural-units>` format (e.g., `GB`, `Seconds`).+}
{+* *FOCUS dataset column* including a+} unit {+quantity+} SHOULD [-be listed as "Requests/Day" to signify-]{+use+} the [-number of requests per day.-]{+`<unit-quantity> <plural-units>` format (e.g., `1000 Tokens`, `1000 Characters`).+}
