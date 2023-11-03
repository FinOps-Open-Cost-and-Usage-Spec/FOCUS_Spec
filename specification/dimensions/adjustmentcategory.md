# Adjustment Category

An adjustment is a positive or negative change in cost applied after the original usage or purchase record(s). Adjustments may be related to one or more charges and are identified by the ChargeType column.

Adjustment Category indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

- The AdjustmentCategory column MUST be present and MUST NOT be null or empty when ChargeType is "Adjustment".
- AdjustmentCategory MUST be null when ChargeType is not "Adjustment". 
- This column is of type String and MUST be one of the allowed values.
- When AdjustmentCategory is "Refund" or "Credit", the charge MUST be negative.
- When an adjustment applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the adjustment pertains to.

## Column ID

AdjustmentCategory

## Display Name

Adjustment Category

## Description

A positive or negative change in cost applied after the original usage or purchase record(s).

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | True                                     |
| Value format    | list-of-values                           |

Allowed values:

| Value      | Description                                                                                                                                                                   |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Refund | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts.
| Credit  | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.
| Rounding Error | Positive or negative charges that are needed to ensure raw cost and usage data aggregations match the total cost on the invoice, which may be rounded. |
| General Adjustment | Positive or negative charges the provider applies that do not fall into other adjustment category values. |

## Introduced (version)

1.0
