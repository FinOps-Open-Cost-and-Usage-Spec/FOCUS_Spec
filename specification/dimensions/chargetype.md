# Charge type

A charge type indicates whether the record represents a prepayment (e.g., up-front or recurring fee), cost of usage that already occurred, an after-the-fact adjustment (e.g., credits), or taxes. The charge type is commonly used to identify and analyze prepaid purchases or usage-based charges.

The ChargeType column MUST be present and MUST NOT be null or empty. This column MUST be of the following values:

| Value        | Description                                                                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Usage`      | Charges based on the amount of a service or resource that was consumed over a given period of time.                                                                           |
| `Purchase`   | Charges for the acquisition of a service or resource bought upfront for a fixed period of time.                                                                               |
| `Adjustment` | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.                                                 |
| `Tax`        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |

## Column ID

ChargeType

## Display name

Charge Type

## Description

Indicates whether the record represents a prepayment (e.g., up-front or recurring fee), cost of usage that already occurred, an after-the-fact adjustment (e.g., credits), or taxes.

## Content constraints

| Constraint       | Value                                    |
| ---------------- | ---------------------------------------- |
| Column required  | True                                     |
| Data type        | String                                   |
| Allows nulls     | False                                    |
| Value format     | list-of-values                           |
| Supported values | `Purchase`, `Usage`, `Adjustment`, `Tax` |

## Introduced (version)

0.5
