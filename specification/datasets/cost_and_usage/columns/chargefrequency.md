# Charge Frequency

[Charge Frequency](#col) indicates how often a [charge](#term) will occur. Along with the [charge period](#term) related columns, the [Charge Frequency](#col) is commonly used to understand recurrence periods (e.g., monthly, yearly); forecast upcoming [charges](#term); and differentiate between one-time and recurring fees for purchases.

## Requirements

[ChargeFrequency](#col) MUST adhere to the following requirements:

* [ChargeFrequency](#col) MUST be of type String.
* [ChargeFrequency](#col) MUST NOT be null.
* [ChargeFrequency](#col) MUST be one of the allowed values.
* [ChargeFrequency](#col) MUST NOT be ["Usage-Based"](#val:ChargeFrequency) when [ChargeCategory](#col) is ["Purchase"](#val:CostAndUsage.ChargeCategory).

## Allowed Values

| Value       | Description                   |
|:------------|:------------------------------|
| One-Time    | *Charges* that only happen once and will not repeat. One-time *charges* are typically recorded on the hour or day when the cost was incurred.  |
| Recurring   | *Charges* that repeat on a periodic cadence (e.g., weekly, monthly) regardless of whether the product or [*service*](#glossary:service) was used. Recurring *charges* typically happen on the same day or point within every period. The charge date does not change based on how or when the *service* is used. |
| Usage-Based | *Charges* that repeat every time the *service* is used. Usage-based *charges* are typically recorded hourly or daily, based on the granularity of the cost data for the period when the *service* was used (referred to as *charge period*). Usage-based *charges* are not recorded when the *service* is not used.                    |

## Column ID

ChargeFrequency

## Display Name

Charge Frequency

## Description

Indicates how often a [charge](#term) will occur.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Recommended                               |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

1.0-preview
