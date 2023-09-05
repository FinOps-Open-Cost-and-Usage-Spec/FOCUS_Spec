# Charge Frequency

Charge Frequency indicates how often a charge would occur. 

The ChargeFrequency column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the
allowed values.

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
| Usage Based | Charges based on the quantity and frequency of a service or resource that was consumed in a given period of time.                                                                                    |
| One-time    | Charges that will occur only and indicate a one-time purchase of a contract/commitment or pre-paid service.     
                                                                         

## Introduced (version)

1.0
