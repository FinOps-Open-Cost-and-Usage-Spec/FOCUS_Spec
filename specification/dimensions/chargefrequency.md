# Charge Frequency

Charge Frequency indicates how often a charge would occur - periodically, usage-based, or one-time charge. When the charge frequency is periodic (typically monthly), it can be inferred that this type of charge can be seen in past and future bill periods (within constraints like charge type or possible expiry). Such records indicate charges for the acquisition of a service or resource bought upfront or on a recurring basis.
When charge frequency is one-time, this can be an indicator of a prepaid purchase which cannot be directly tied to usage in that billing period. Usage-based charges will occur as frequently as that type of usage exists. 

The ChargeFrequency column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the
allowed values.

See [Appendix: Charge Frequency](#chargefrequency-1) for details about allowed values and governance criteria for this dimension.

## Column ID

ChargeFrequency

## Display Name

Charge Frequency

## Description

Indicates the frequency with which a charge will occur - periodically (typically monthly), based on usage, or one-time

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
| Periodic    | This charge type will occur on a periodic cadence which can be daily, hourly or monthly which indicate charges for the acquisition of a service or resource bought upfront or on a recurring basis. |
| Usage Based | Charges based on the quantity and frquency of a service or resource that was consumed in a given period of time.                                                                                    |
| One time    | Charges that will occur only and indicate a one-time purchase of a contract/commitment or pre-paid service.     
                                                                         

## Introduced (version)

1.0
