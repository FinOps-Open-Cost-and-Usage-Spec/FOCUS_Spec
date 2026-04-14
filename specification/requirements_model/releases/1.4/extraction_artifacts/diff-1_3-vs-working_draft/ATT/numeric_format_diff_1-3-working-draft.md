## Diff

@@ -1,52 +1,35 @@
## Requirements

[-* Columns with a Numeric value format MUST contain a single numeric value.-]
[-* Numeric values MUST be expressed as an integer value, a decimal value, or a value expressed in scientific notation. Fractional notation MUST NOT be used.-]
[-* Numeric values expressed using scientific notation MUST be expressed using E notation "mEn" with a real number m and an integer n indicating a value of "m x 10^n".   The sign of the exponent MUST only be expressed as part of the exponent value if n is negative.-]
[-* Numeric values MUST NOT be expressed with mathematical symbols, functions, or operators.-]
[-* Numeric values MUST NOT contain qualifiers or additional characters (e.g., currency symbols, units of measure, etc.).-]
[-* Numeric values MUST NOT contain commas or punctuation marks except for a single decimal point (".") if required-]{+Column conforming+} to [-express a decimal value.-]
[-* Numeric values-]{+NumericFormat attribute+} MUST [-NOT include a character-]{+adhere+} to[-represent a sign for a positive value. A negative sign (-) MUST indicate a negative value.-]
[-* Columns with a Numeric value format MUST present one of-] the following [-values as the "Data type" in the column definition.-]
[-  * Allowed values:-]{+requirements:+}

[-| Data Type | Type Description |-]
[-    |:----------|:-----------------|-]
[-    | Integer   | Specifies-]{+* *FOCUS dataset column* MUST contain+} a {+single+} numeric [-value represented by a whole number-]{+value.+}
{+* *FOCUS dataset column* MUST have values of type integer, decimal,+} or [-by zero. Integer number formats correspond-]{+scientific notation.+}
{+* *FOCUS dataset column* MUST contain values that, when not null, conform+} to [-standard data types-]{+one of the allowed Data Types+} defined [-by ISO/IEC 9899:2018 |-]
[-    | Decimal   | Specifies-]{+in the table below.+}
{+* *FOCUS dataset column* MUST contain values that, when not null, conform to one of the allowed precision levels (and scale, where applicable) defined in the table below.+}
{+* *FOCUS dataset column* MUST NOT use mathematical symbols, functions, or operators, except for+} a [-numeric-]{+negative sign (-) to indicate a negative+} value [-represented by-]{+or+} a {+negative exponent in scientific notation.+}
{+* *FOCUS dataset column* MUST NOT include additional characters or qualifiers (e.g., currency symbols, units of measure).+}
{+* *FOCUS dataset column* MUST NOT contain commas or punctuation marks, except for a single+} decimal [-number. Decimal formats correspond-]{+point when required for a decimal value.+}
{+* *FOCUS dataset column* MUST use a negative sign (-)+} to [-ISO/IEC/IEEE 60559:2011 and IEEE 754-2008 definitions. |-]{+indicate a negative value.+}
* [-Providers SHOULD define precision and scale-]{+*FOCUS dataset column* MUST NOT include a positive sign (+)+} for [-Numeric Format columns using one of the following precision-]{+a positive value.+}
{+* When *FOCUS dataset column* contains numeric+} values {+expressed+} in {+scientific notation, it MUST adhere to the following requirements:+}
{+  * *FOCUS dataset column* MUST use E notation "mEn", where m is+} a [-data definition document that providers publish.-]{+real number and n is an integer exponent.+}
  * [-Allowed values:-]{+*FOCUS dataset column* MUST use a negative sign (-) to indicate a negative exponent.+}
{+  * *FOCUS dataset column* MUST NOT include a positive sign (+) for a positive exponent.+}

[-|-]{+### Allowed+} Data [-Type | Precision | Definition                                                                | Range / Significant Digits       |-]
[-    |:----------|:----------|:--------------------------------------------------------------------------|:---------------------------------|-]
[-    | Integer   | Short     | 16-bit signed short int ISO/IEC 9899:2018                                 | -32,767 to +32,767               |-]
[-    | Integer   | Long      | 32-bit signed long int ISO/IEC 9899:2018                                  | -2,147,483,647 to +2,147,483,647 |-]
[-    | Integer   | Extended  | 64-bit signed two's complement integer *or higher*                        | -(2^63 - 1) to (2^63 - 1)        |-]
[-    | Decimal   | Single    | 32-bit binary format IEEE 754-2008 floating-point (decimal32)             | 9                                |-]
[-    | Decimal   | Double    | 64-bit binary format IEEE 754-2008 floating-point (decimal64)             | 16                               |-]
[-    | Decimal   | Extended  | 128-bit binary format IEEE 754-2008 floating-point (decimal128) or higher | 36+                              |-]{+Types+}

[-### Examples-]{+| Data Type | Type Description |+}
{+|:----------|:-----------------|+}
{+| Integer   | Specifies a numeric value represented by a whole number or by zero. Integer number formats correspond to standard data types defined by ISO/IEC 9899:2018 |+}
{+| Decimal   | Specifies a numeric value represented by a decimal number. Decimal formats correspond to ISO/IEC/IEEE 60559:2011 and IEEE 754-2008 definitions. |+}

[-This format requires that single numeric values be represented using an integer or decimal format without additional characters or qualifiers. The following lists provide examples of values that meet the requirements and those that do not.-]{+### Allowed Precisions+}

[-* Values Meeting Numeric Requirements:-]
[-  * -100.2-]
[-  * -3-]
[-  * 4-]
[-  * 35.2E-7-]
[-  * 1.234-]
[-  -]
[-* Values NOT Meeting Numeric Requirements-]
[-  * 1 1/2-]{+| Data Type | Precision | Definition                                                                | Range / Significant Digits       |+}
{+|:----------|:----------|:--------------------------------------------------------------------------|:---------------------------------|+}
{+| Integer   | Short     | 16-bit signed short int ISO/IEC 9899:2018                                 | -32,767 to +32,767               |+}
{+| Integer   | Long      | 32-bit signed long int ISO/IEC 9899:2018                                  | -2,147,483,647 to +2,147,483,647 |+}
{+| Integer   | Extended  | 64-bit signed two's complement integer *or higher*                        | -(2^63+} - [-contains fractional notation-]
[-  * 35.2E+7-]{+1) to (2^63+} - [-contains a positive exponent with a sign-]
[-  * 35.24 x 10^7 - contains an invalid-]{+1)        |+}
{+| Decimal   | Single    | 32-bit binary+} format [-for scientific notation-]
[-  * [3,5,8] - contains an array-]
[-  * [4:5] - contains a range-]
[-  * 5i + 4 - contains a complex number-]
[-  * sqrt(2) - contains a mathematical symbol-]{+IEEE 754-2008 floating-point (decimal32)             | 9                                |+}
{+| Decimal   | Double    | 64-bit binary format IEEE 754-2008 floating-point (decimal64)             | 16                               |+}
{+| Decimal   | Extended  | 128-bit binary format IEEE 754-2008 floating-point (decimal128)+} or [-operation-]
[-  * 2.3^3 - contains an exponent-]
[-  * 32 GiB - contains a unit of measure-]
[-  * $32 - contains a currency symbol-]
[-  * 3,432,342 - contains a comma-]
[-  * +333 - contains a positive sign-]{+higher | 36+                              |+}
