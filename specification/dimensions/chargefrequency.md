# Charge Frequency

Charge Frequency indicates how often a charge will occur. Charge Frequency is commonly used for scenarios like forecasting and differentiating between one-time and recurring fees for commitment-based discounts.

While Charge Frequency indicates whether a charge will reoccur, dimensions Charge Period Start and Charge Period End specify the period for which this charge applies. This can typically be used to also understand the recurrence period (e.g., monthly, yearly).

The ChargeFrequency column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeFrequency

## Display Name

Charge Frequency

## Description

Indicates the frequency with which a charge will occur - recurring (typically monthly), based on usage, or one-time

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | False                                    |
| Value format    | list-of-values                           |

Allowed values:

| Value       | Description                                                                                                                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recurring   | This charge type will occur on a periodic cadence which can be daily, hourly or monthly which indicate charges for the acquisition of a service or resource bought upfront or on a recurring basis. |
| Usage-Based | Charges based on the quantity and frequency of a service or resource that was consumed in a given period of time.                                                                                    |
| One-Time    | Charges that will occur only once and indicate a one-time purchase of a contract/commitment or pre-paid service. In other words, it can either be a pre-payment of usage charges or a truly one-time fee - such as a setup fee or a service fee.   
                                                                         

## Introduced (version)

1.0
