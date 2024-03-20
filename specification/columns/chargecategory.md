# Charge Category

A Charge Category is the highest level classification for the type of charge that the billing row represents. The Charge Category is commonly used to identify prepaid purchases separately from usage-based charges or to separate charges that may require special handling from regular usage.

The ChargeCategory column MUST be present and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Indicates whether the row represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact *adjustment* (e.g., credits), or taxes.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Column required | True           |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Adjustment      | Positive or negative charges the provider applies that do not fall into other category values.    |
| Credit      | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.     |


## Introduced (version)

0.5
