# Amortized Cost

Amortized cost represents the sum of the amortization of upfront fees, the amortization of recurring fees, and the discounted variable rate of the line item. This column is often used to show spending trends that include on demand rates, reservation rates, recurring commitments, as well as amortization of upfront fees. The Fee and Upfront amortization portion of this column’s value should be proportional to the number of units for the line item and the time granularity of the data. The currency for the value specified in Billed Cost can be found in the [Billing Currency](#billingcurrency) column.

The AmortizedCost column MUST be present in the billing data. This column MUST be a numeric value of type Decimal and MUST NOT contain null values. The aggregated Amortized Cost for a billing period WILL NOT match the charge received on the invoice for the same billing period.


Practitioners are faced with two main challenges in respect to this metric:
1. Practitioners need to amortize upfront fees over the duration of the commitment and distribute those fees to the appropriate reporting groups (e.g. tags, resources)
2. Many reservation-like functions include a recurring expense for the commitment for every billing period and must distribute this cost to the resources using the commitment. Thus forcing reconciliation between the initial commitment line item per period and the actual usage line items.


## Column ID

AmortizedCost

## Display name

Amortized Cost

## Description

The cost inclusive of amortized upfront charges, recurring fees, and negotiated discount rates for the line item.

### Concerning Granularity and Distribution of Recurring Fee

While some providers may include a line item at the beginning of each applicable period for the amount of the commitment, Amortized Cost should include that cost distributed such that there is not a need to distribute this fee. Thus the practitioner is not required to distribute this commitment, following that particular construct's logic, but rather the provider must distribute these fees over the line items for the usage of this commitment. See examples section for further clarity.

### Concerning Amortization Approaches
The amortization of the upfront charge should be amortized using a methodology determined by the provider that reflects the needs of their customer base and is proportional with usage quantity and the time granularity of the line item.  Should a practitioner desire to amortize upfront fees using a different approach, the practioner can do so using the BilledCost for the line item representing the initial purchase.


## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Allows nulls    | False           |
| Value format    | Numeric value   |

## Introduced (version)

0.5
