# Charge Frequency

Charge Frequency indicates how often a [*charge*](#glossary:charge) will occur. Along with the [*charge period*](#glossary:chargeperiod) related columns, the Charge Frequency is commonly used to understand recurrence periods (e.g., monthly, yearly); forecast upcoming *charges*; and differentiate between one-time and recurring fees for purchases.

## Requirements

ChargeFrequency MUST adhere to the following requirements:

* ChargeFrequency MUST be of type String.
* ChargeFrequency MUST NOT be null.
* ChargeFrequency MUST be one of the allowed values.
* ChargeFrequency MUST be "Usage-Based" when [ChargeCategory](#datasets.skuprice.chargecategory) is "Usage".
* ChargeFrequency MUST NOT be "Usage-Based" when ChargeCategory is "Purchase".

## Allowed Values

| Value       | Description                   |
|:------------|:------------------------------|
| One-Time    | *Charges* that only happen once and will not repeat. One-time *charges* are typically recorded on the hour or day when the cost was incurred.  |
| Recurring   | *Charges* that repeat on a periodic cadence (e.g., weekly, monthly) regardless of whether the product or [*service*](#glossary:service) was used. Recurring *charges* typically happen on the same day or point within every period. The charge date does not change based on how or when the *service* is used. |
| Usage-Based | *Charges* that repeat every time the *service* is used. Usage-based *charges* are typically recorded hourly or daily, based on the granularity of the cost data for the period when the *service* was used (referred to as *charge period*). Usage-based *charges* are not recorded when the *service* is not used.                    |

## Implementation Guidance

While the Charge Frequency column and its allowed values are shared between the [Cost and Usage](#datasets.costandusage) dataset and the [SKU Price](#datasets.skuprice) dataset, the cross-column requirements against Charge Category differ by design.

The Cost and Usage dataset records realized *charges*, and the frequency of a realized *charge* reflects the underlying billing arrangement rather than the nature of the published rate. A *charge* with a Charge Category of "Usage" can therefore carry any frequency (e.g., professional services billed by the hour appear as "One-Time" for a single engagement or as "Recurring" under an ongoing contract). For this reason, the Cost and Usage dataset excludes only the "Usage-Based" frequency for "Purchase" charges.

Conversely, the SKU Price dataset describes published pricing constructs. A [*SKU Price*](#glossary:sku-price) with a Charge Category of "Usage" is a per-unit consumption rate, which is inherently "Usage-Based", while a *SKU Price* with a Charge Category of "Purchase" is acquired either upfront ("One-Time") or on a periodic cadence ("Recurring"). Both datasets exclude the same combination of a "Usage-Based" frequency with a "Purchase" charge; the SKU Price dataset additionally constrains "Usage" prices to the "Usage-Based" frequency.

Because the Cost and Usage dataset records ledger events that can reference a SKU Price ID without mirroring its classification (e.g., a refund recorded with a Charge Category of "Credit" and a Charge Frequency of "One-Time"), Charge Category and Charge Frequency values are not expected to match across the two datasets for a given SKU Price ID.

## Column ID

ChargeFrequency

## Display Name

Charge Frequency

## Description

Indicates how often a *charge* will occur.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Condition       | [Includes multiple charge frequencies](#conditions.includesmultiplechargefrequencies) |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
