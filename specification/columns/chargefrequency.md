# Charge Frequency

Charge Frequency indicates how often a [*charge*](#glossary:charge) will occur. Along with the [charge period](#glossary:chargeperiod) related columns, the Charge Frequency is commonly used to understand recurrence periods (e.g., monthly, yearly), forecast upcoming *charges*, and differentiate between one-time and recurring fees for purchases.

The ChargeFrequency column adheres to the following requirements:

* ChargeFrequency is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeFrequency MUST be of type String.
* ChargeFrequency MUST NOT be null.
* ChargeFrequency MUST be one of the allowed values.
* ChargeFrequency MUST NOT be "Usage-Based" when [ChargeCategory](#chargecategory) is "Purchase".

## Column ID

ChargeFrequency

## Display Name

Charge Frequency

## Description

Indicates how often a *charge* will occur.

## Content Constraints

| Constraint      | Value          |
|:----------------|:---------------|
| Column type     | Dimension      |
| Feature level   | Recommended    |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value       | Description                   |
|:------------|:------------------------------|
| One-Time    | *Charges* that only happen once and will not repeat. One-time *charges* are typically recorded on the hour or day when the cost was incurred.  |
| Recurring   | *Charges* that repeat on a periodic cadence (e.g., weekly, monthly) regardless of whether the product or [*service*](#glossary:service) was used. Recurring *charges* typically happen on the same day or point within every period. The charge date does not change based on how or when the *service* is used. |
| Usage-Based | *Charges* that repeat every time the *service* is used. Usage-based *charges* are typically recorded hourly or daily, based on the granularity of the cost data for the period when the *service* was used (referred to as *charge period*). Usage-based *charges* are not recorded when the *service* is not used.                    |

## Introduced (version)

1.0-preview
