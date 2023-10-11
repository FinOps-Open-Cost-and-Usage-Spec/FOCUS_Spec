# Commitment Utilization

Commitment Utilization indicates whether a charge utilized a commitment during the charge period. Commitment Utilization applies to all commitments and commitment types applied to the current charge. This includes, but is not limited to capacity commitments and commitment-based disocunts represented by the Commitment Disocunt ID. Commitment Utilization is commonly used to identify wastage when a commitment has not been used and to calculate commitment utilization.

The CommitmentUtilization column MUST be present and MUST NOT be null when a commitment is applied or CommitmentDiscountId is set. This column is of type String and MUST be one of the allowed values.

## Column ID

CommitmentUtilization

## Display Name

Commitment Utilization

## Description

Indicates whether a charge utilized a commitment during the charge period.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column required | True           |
| Data type       | String         |
| Allows nulls    | True           |
| Value format    | list-of-values |

Allowed values:

| Value    | Description                                                                                                                            |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------|
| Used     | Charges that benefit from a discounted unit price due to one or more commitments.                                                      |
| Not Used | Charges that are a result of not fully utilizing a commitment. The line item reflects the capacity or monetary value that went unused. |

## Introduced (version)

1.0
