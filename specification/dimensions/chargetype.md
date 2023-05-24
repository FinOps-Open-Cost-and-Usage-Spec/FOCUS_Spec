# Charge type

A charge type indicates whether the record represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact adjustment (e.g., credits), or taxes. The charge type is commonly used to identify prepaid purchases separately from usage-based charges, to separate taxes that may require special handling, or to apply finer-grained allocation logic to purchases or adjustments.

The ChargeType column MUST be present and MUST NOT be null or empty. This column is restricted and MUST be one of the allowed values.

## Column ID

ChargeType

## Display name

Charge Type

## Description

Indicates whether the record represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact adjustment (e.g., credits), or taxes.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column required | True           |
| Data type       | String         |
| Allows nulls    | False          |
| Value format    | list-of-values |

### Allowed values

| Value        | Description                                                                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Adjustment` | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.                                                 |
| `Purchase`   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.                                                                                  |
| `Tax`        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| `Usage`      | Charges based on the quantity of a service or resource that was consumed over a given period of time.                                                                         |

## Introduced (version)

0.5
