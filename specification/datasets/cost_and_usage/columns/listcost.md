# List Cost

[List Cost](#col) represents the cost of a [charge](#term) based on the service-provider-suggested pricing. It is the cost before any [negotiated pricing terms](#term) or any discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)) are applied to the [charge](#term).

When [List Unit Price](#col) and [Pricing Quantity](#col) are provided for the [charge](#term), [List Cost](#col) is calculated by multiplying the List Unit Price by the corresponding [Pricing Quantity](#col).

[List Cost](#col) is denominated in the [Billing Currency](#col). [List Cost](#col) is commonly used to calculate savings based on negotiation and rate optimization activities by comparing it with [Contracted Cost](#col), [Billed Cost](#col), and [Effective Cost](#col).

## Requirements

[ListCost](#col) MUST adhere to the following requirements:

* [ListCost](#col) MUST be of type Decimal.
* [ListCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ListCost](#col) MUST NOT be null.
* [ListCost](#col) MUST be denominated in the [BillingCurrency](#col).
* When [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass), [ListCost](#col) MUST adhere to the following requirements:
  * [ListCost](#col) MUST represent the cost of the [charge](#term) based on the service-provider-suggested pricing.
  * [ListCost](#col) MUST NOT reflect [negotiated pricing terms](#term).
  * [ListCost](#col) MUST NOT reflect any cost impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).
* [ListCost](#col) MUST equal [BilledCost](#col) when [ChargeCategory](#col) is ["Credit"](#val:CostAndUsage.ChargeCategory).
* [ListCost](#col) MUST be calculated based on the [ListCost](#col) of the related [charges](#term) when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
* [ListCost](#col) MUST equal the product of [ListUnitPrice](#col) and [PricingQuantity](#col) when [ListUnitPrice](#col) is not null and [PricingQuantity](#col) is not null.

## Usability Constraints

**Aggregation:** When aggregating [List Cost](#col) for savings calculations, exclude either the [covering charges](#term) (e.g., [commitment discount](#term) purchases) or the [covered charges](#term) (e.g., usage charges applied against [commitment discounts](#term)), based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude [covered charges](#term) when aggregating on a billed basis, or [covering charges](#term) when aggregating on an accrual basis.

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost of a [charge](#term) based on the service-provider-suggested pricing.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | False                                       |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0-preview
