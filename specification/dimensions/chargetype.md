# Charge Type

A Charge Type indicates whether the record represents an upfront or recurring fee, cost of usage that already occurred,
an after-the-fact adjustment (e.g., credits), or taxes. The Charge Type is commonly used to identify prepaid purchases
separately from usage-based charges, to separate taxes that may require special handling, or to apply finer-grained
allocation logic to purchases or adjustments.

The ChargeType column MUST be present and MUST NOT be null or empty. This column is restricted and MUST be one of the
allowed values.

See [Appendix: Charge Type](#chargetype-1) for details about allowed values and governance criteria for this dimension.

## Column ID

ChargeType

## Display Name

Charge Type

## Description

Indicates whether the record represents an upfront or recurring fee, cost of usage that already occurred, an
after-the-fact adjustment (e.g., credits), or taxes.

## Content Constraints

| Constraint      | Value                                    |
|:----------------|:-----------------------------------------|
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | False                                    |
| Value format    | list-of-values                           |
| Allowed values  | `Adjustment`, `Purchase`, `Tax`, `Usage` |

## Introduced (version)

0.5
