# Date/Time Format

Columns that provide numeric values conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for both humans and systems.

All columns capturing a numeric value, defined in the FOCUS specification, MUST be a real number represented as an integer, a decimal value, or a value represented in scientific notation as defined in this section.

## Attribute ID

NumericFormat

## Attribute name

Numeric Format

## Description

Rules and formatting requirements for numeric columns appearing in billing data.

## Requirements

* Metrics with a Numeric format MUST contain a single value.
* The single value captured in metrics with a Numeric format MUST be a real, rational.
* Numeric values MUST be expressed as integer, decimal value, or scientific notation.
* Fractional notation or values expressed with an arithmetic operator (e.g. 1/2) are not permitted.
* Multiple values, arrays, or ranges are not permitted in the metrics using the Numeric format.
* Numerical values expressed with mathematical symbols, operators, or exponent values not required for scientific notation are not permitted.
* Numeric values MUST NOT contain qualifiers or additional characters (e.g. currency symbols, units of measure, etc.).
* Numeric values MUST NOT contain commas or punctuation marks except for a single decimal point if required to express a decimal value.
* Numeric values MUST NOT include a character to represent sign for a positive value.  The only sign permitted is a negative sign (-) to indicate a negative value.
* Numeric values MUST NOT be used to represent binary values (e.g. 0 or 1).

## Examples of Numeric Values Meeting Requirements

* Values Meeting Numeric Requirements:
  * "-100.2"
  * "0"
  * "1"
  * "1.234"
  * "1.23342 x 10^7"
  
* Values NOT Meeting Numeric Requirements
  * "1 1/2" - contains fractional notation
  * "[3,5,8]" - contains an array
  * "[4:5]" - contains a range
  * "5i + 4" - contains a non-real or complex number
  * "sqrt(2)" - contains a mathematical symbol or operations
  * "2.3^3" - contains an exponent not related to scientific notation
  * "32 GiB" - contains a unit of measure
  * "$32" - contains a currency symbol
  * "3,432,342" - contains a comma
  * "+333" - contains a positive sign

## Numeric Precision

The FOCUS specification does not require a specific level of precision for numeric values.  The level of precision required for a given metric is determined by the provider unless specified in the metric specification.  The level of precision required for a given metric SHOULD be documented in the metric definition.  The following table outlines the options for specifying the level of precision for a given metric.

| Precision      | Qualifier            | Definition          | Range / Significant Digits          |
| :--------------| :------------------- | :------------------ | :-------------------- |
| (unspecified)  | (unspecified)        | 64-bit binary format IEEE 754-2008 floating-point |
| Integer        | (unspecified)        | 32-bit signed two's complement integer | -2,147,483,647 to +2,147,483,647 |
| Integer        | Short                | 16-bit signed two's complement integer | -32,767 to +32,767 |
| Integer        | Long                 | 32-bit signed two's complement integer | -2,147,483,647 to +2,147,483,647 |
| Integer        | Extended             | 64-bit signed two's complement integer *or higher* | extended |
| Float          | (unspecified)        | 64-bit binary format IEEE 754-2008 floating-point | 16 |
| Float          | Single               | 32-bit binary format IEEE 754-2008 floating-point | 9 |
| Float          | Double               | 64-bit binary format IEEE 754-2008 floating-point | 16 |
| Float          | Extended             | 128-bit binary format IEEE 754-2008 floating-point *or higher* | extended |

## Numeric Format Definitions

Numeric data types are defined in each metric specification.  The following table outlines the numeric data types defined in the FOCUS specification.

| Numeric Type    |                 |
| :-------------- | :-------------- |
| Numeric         | General Numeric Type  | Specifies any numeric value compliant with this attribute definition.  This type is used when the metric definition does not specify a more specific numeric type. |
| Integer         | Integer               | Specifies a numeric value represented by a whole number or by zero. |
| Decimal         | Decimal               | Specified a numeric value represented by a decimal number with or without scientific notation |

The numeric Data type is specified in the metric definition as the "Data type" constraint as shown in the following example table.

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Allows nulls    | False           |
| Value format    | Numeric value   |

The constraint table in a metric definition may also provide an optional "Data precision" constraint to specify the level of precision required for the metric.  If the "Data precision" constraint is not specified, the level of precision required for the metric is determined by the default precision for either Integer or Float precision as defined in the previous section.

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Data precision  | Extended Float  |
| Allows nulls    | False           |
| Value format    | Numeric value   |

## Exceptions

None

## Introduced (version)

1.0
