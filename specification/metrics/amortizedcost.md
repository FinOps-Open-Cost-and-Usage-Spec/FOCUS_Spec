# Amortized Cost

Amortized cost represents the sum of the amortized upfront fees, amortized recurring fees, and the usage cost of the line item. This column is often used to show spending trends that include on demand rates, effective commitment-based discount rates, recurring commitments, as well as amortization of upfront fees. The fee and upfront amortization portion of this column's value should be proportional to the number of units for the line item and the time granularity of the data. The currency for the value specified in Amortized Cost can be found in the [Billing Currency](#billingcurrency) column. The aggregated Amortized Cost for a billing period may not match the charge received on the invoice for the same billing period.

Practitioners are faced with two main challenges with respect to this metric:

1. Practitioners need to amortize upfront fees over the duration of the commitment and distribute those fees to the appropriate reporting groups (e.g. tags, resources).
2. Many commitment based discount constructs include a recurring expense for the commitment for every billing period and must distribute this cost to the resources using the commitment. This forces reconciliation between the initial commitment line item per period and the actual usage line items.

The AmortizedCost column MUST be present in the billing data. This column MUST be a numeric value of type Decimal and MUST NOT contain null values.

## Column ID

AmortizedCost

## Display name

Amortized Cost

## Description

The cost inclusive of amortized upfront fees, amortized recurring fees, and the usage cost of the line item.

### Concerning Granularity and Distribution of Recurring Fee

Providers should distribute the commitment purchase amount instead of including a line item at the beginning of a period so practitioners do not need to manually distribute the fee themselves.

### Concerning Amortization Approaches

The amortization of the upfront charge should be amortized using a methodology determined by the provider that reflects the needs of their customer base and is proportional with usage quantity and the time granularity of the line item.  Should a practitioner desire to amortize upfront fees using a different approach, the practitioner can do so using the Billed Cost for the line item representing the initial purchase.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Allows nulls    | False           |
| Value format    | Numeric value   |

## Introduced (version)

0.5
