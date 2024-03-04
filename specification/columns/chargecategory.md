# Charge Category

A Charge Category indicates whether the row represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact [*adjustment*](#glossary:adjustment) (e.g., credits), or taxes. The Charge Category is commonly used to identify prepaid purchases separately from usage-based charges, to separate taxes that may require special handling, or to apply finer-grained
allocation logic to purchases or *adjustments*.

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
| FOCUS Essential | True           |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Adjustment | Any adjustments that are applied after the original usage or purchase row. Adjustments may be related to multiple charges.   |
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |

## Introduced (version)

0.5
