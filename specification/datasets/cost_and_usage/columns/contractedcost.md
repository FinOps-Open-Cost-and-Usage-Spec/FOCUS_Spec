# Contracted Cost

[Contracted Cost](#col) represents the cost of a [charge](#term) based on [negotiated pricing terms](#term) before any discount-bearing [commitment programs](#term) (e.g., [commitment discounts](#term)) are applied to the [charge](#term).

When [Contracted Unit Price](#col) and [Pricing Quantity](#col) are provided for the [charge](#term), [Contracted Cost](#col) is calculated by multiplying the [Contracted Unit Price](#col) by the corresponding [Pricing Quantity](#col). When no [negotiated pricing terms](#term) apply to a usage or purchase [charge](#term), [Contracted Cost](#col) defaults to [List Cost](#col).

[Contracted Cost](#col) is denominated in the [Billing Currency](#col). [Contracted Cost](#col) is commonly used to calculate savings based on negotiation and rate optimization activities by comparing it with [List Cost](#col), [Billed Cost](#col), and [Effective Cost](#col).

## Requirements

[ContractedCost](#col) MUST adhere to the following requirements:

* [ContractedCost](#col) MUST be of type Decimal.
* [ContractedCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractedCost](#col) MUST NOT be null.
* [ContractedCost](#col) MUST be denominated in the [BillingCurrency](#col).
* When [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass), [ContractedCost](#col) MUST adhere to the following requirements:
  * [ContractedCost](#col) MUST reflect [negotiated pricing terms](#term) that are independent of any discount-bearing [commitment programs](#term) being applied to the [charge](#term).
  * [ContractedCost](#col) MUST NOT reflect any cost impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).
  * [ContractedCost](#col) MUST equal [ListCost](#col) when no [negotiated pricing terms](#term) apply to the [charge](#term).
* [ContractedCost](#col) MUST equal [BilledCost](#col) when [ChargeCategory](#col) is ["Credit"](#val:CostAndUsage.ChargeCategory).
* [ContractedCost](#col) MUST be calculated based on the [ContractedCost](#col) of the related [charges](#term) when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
* [ContractedCost](#col) MUST equal the product of [ContractedUnitPrice](#col) and [PricingQuantity](#col) when [ContractedUnitPrice](#col) is not null and [PricingQuantity](#col) is not null.

## Usability Constraints

**Aggregation:** When aggregating [Contracted Cost](#col) for savings calculations, exclude either the [covering charges](#term) (e.g., [commitment discount](#term) purchases) or the [covered charges](#term) (e.g., usage charges applied against [commitment discounts](#term)), based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude [covered charges](#term) when aggregating on a billed basis, or [covering charges](#term) when aggregating on an accrual basis.

## Column ID

ContractedCost

## Display Name

Contracted Cost

## Description

Cost of a [charge](#term) based on [negotiated pricing terms](#term) before any discount-bearing [commitment programs](#term) (e.g., [commitment discounts](#term)) are applied to the [charge](#term).

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

1.0
