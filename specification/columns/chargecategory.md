# Charge Category

A Charge Category is the highest level classification for the type of charge that the billing row represents. The Charge Category is commonly used to identify prepaid purchases separately from usage-based charges or to separate charges that may require special handling from regular usage.

The ChargeCategory column MUST be present in the billing data and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

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
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Usage      | Positive or negative charges based on the quantity of a service or resource that was consumed over a given period of time including refunds.     |
| Purchase   | Positive or negative charges for the acquisition of a service or resource bought upfront or on a recurring basis inluding refunds.              |
| Tax        | Positive or negative applicable taxes that are levied by the relevant authorities including refunds. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Credit      | Positive or negative charges granted by the provider for various scenarios e.g promotional credits or corrections to promotional credits.     |
| Adjustment      | Positive or negative charges the provider applies that do not fall into other category values.    |

## Introduced (version)

0.5
