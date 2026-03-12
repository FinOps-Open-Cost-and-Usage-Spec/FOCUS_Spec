# Numeric Format

Columns that provide numeric values conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for humans and systems. The FOCUS specification does not require a specific level of precision for numeric values. The level of precision required for a given column is determined by the provider and should be part of a data definition published by the provider.

## Attribute ID

NumericFormat

## Attribute Name

Numeric Format

## Description

Rules and formatting requirements for numeric columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

NumericFormat MUST adhere to the following requirements:

* FOCUS column containing numeric values MUST adhere to the following requirements:
  * FOCUS column containing numeric values MUST contain a single numeric value.
  * FOCUS column containing numeric values MUST have values of type integer, decimal, or scientific notation.
  * FOCUS column containing numeric values expressed in scientific notation MUST use E notation "mEn", where m is a real number and n is an integer exponent.
  * FOCUS column containing numeric values expressed in scientific notation MUST use a negative sign (-) to indicate a negative exponent.
  * FOCUS column containing numeric values expressed in scientific notation MUST NOT include a positive sign (+) for a positive exponent.
  * FOCUS column containing numeric values MUST NOT use mathematical symbols, functions, or operators.
  * FOCUS column containing numeric values MUST NOT include additional characters or qualifiers (e.g., currency symbols, units of measure).
  * FOCUS column containing numeric values MUST NOT contain commas or punctuation marks, except for a single decimal point when required for a decimal value.
  * FOCUS column containing numeric values MUST use a negative sign (-) to indicate a negative value.
  * FOCUS column containing numeric values MUST NOT include a positive sign (+) for a positive value.
  * FOCUS column containing numeric values MUST contain values that, when not null, conform to one of the allowed Data Types defined in the table below.
  * FOCUS column containing numeric values MUST contain values that, when not null, conform to one of the allowed precision levels (and scale, where applicable) defined in the table below.
* Custom column containing numeric values MUST adhere to the following requirements:
  * Custom column containing numeric values SHOULD contain a single numeric value.
  * Custom column containing numeric values SHOULD have values of type integer, decimal, or scientific notation.
  * Custom column containing numeric values expressed in scientific notation SHOULD use E notation "mEn", where m is a real number and n is an integer exponent.
  * Custom column containing numeric values expressed in scientific notation SHOULD use a negative sign (-) to indicate a negative exponent.
  * Custom column containing numeric values expressed in scientific notation SHOULD NOT include a positive sign (+) for a positive exponent.
  * Custom column containing numeric values SHOULD NOT use mathematical symbols, functions, or operators.
  * Custom column containing numeric values SHOULD NOT include additional characters or qualifiers (e.g., currency symbols, units of measure).
  * Custom column containing numeric values SHOULD NOT contain commas or punctuation marks, except for a single decimal point when required for a decimal value.
  * Custom column containing numeric values SHOULD use a negative sign (-) to indicate a negative value.
  * Custom column containing numeric values SHOULD NOT include a positive sign (+) for a positive value.
  * Custom column containing numeric values SHOULD contain values that, when not null, conform to one of the allowed Data Types defined in the table below.
  * Custom column containing numeric values SHOULD contain values that, when not null, conform to one of the allowed precisions (and scale, where applicable) defined in the table below.

### Allowed Data Types

| Data Type | Type Description |
|:----------|:-----------------|
| Integer   | Specifies a numeric value represented by a whole number or by zero. Integer number formats correspond to standard data types defined by ISO/IEC 9899:2018 |
| Decimal   | Specifies a numeric value represented by a decimal number. Decimal formats correspond to ISO/IEC/IEEE 60559:2011 and IEEE 754-2008 definitions. |

### Allowed Precisions

| Data Type | Precision | Definition                                                                | Range / Significant Digits       |
|:----------|:----------|:--------------------------------------------------------------------------|:---------------------------------|
| Integer   | Short     | 16-bit signed short int ISO/IEC 9899:2018                                 | -32,767 to +32,767               |
| Integer   | Long      | 32-bit signed long int ISO/IEC 9899:2018                                  | -2,147,483,647 to +2,147,483,647 |
| Integer   | Extended  | 64-bit signed two's complement integer *or higher*                        | -(2^63 - 1) to (2^63 - 1)        |
| Decimal   | Single    | 32-bit binary format IEEE 754-2008 floating-point (decimal32)             | 9                                |
| Decimal   | Double    | 64-bit binary format IEEE 754-2008 floating-point (decimal64)             | 16                               |
| Decimal   | Extended  | 128-bit binary format IEEE 754-2008 floating-point (decimal128) or higher | 36+                              |

## Examples

This format requires that single numeric values be represented using an integer or decimal format without additional characters or qualifiers. The following lists provide examples of values that meet the requirements and those that do not.

* Values Meeting Numeric Requirements:
  * -100.2
  * -3
  * 4
  * 35.2E-7
  * 1.234
  
* Values NOT Meeting Numeric Requirements
  * 1 1/2 - contains fractional notation
  * 35.2E+7 - contains a positive exponent with a sign
  * 35.24 x 10^7 - contains an invalid format for scientific notation
  * [3,5,8] - contains an array
  * [4:5] - contains a range
  * 5i + 4 - contains a complex number
  * sqrt(2) - contains a mathematical symbol or operation
  * 2.3^3 - contains an exponent
  * 32 GiB - contains a unit of measure
  * $32 - contains a currency symbol
  * 3,432,342 - contains a comma
  * +333 - contains a positive sign

## Exceptions

None

## Introduced (version)

1.0-preview
