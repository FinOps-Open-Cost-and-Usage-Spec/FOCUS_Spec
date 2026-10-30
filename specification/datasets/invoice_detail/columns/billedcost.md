# Billed Cost

[Billed Cost](#col) represents the cost of a [charge](#term) as invoiced by the [invoice issuer](#term) in a given [billing period](#term).

For all [charges](#term), [Billed Cost](#col) reflects all applicable pricing adjustments (e.g., reduced pricing from [negotiated discounts](#term) or [commitment discounts](#term)). For purchase [charges](#term), [Billed Cost](#col) includes any portion invoiced in the given [billing period](#term). For usage [charges](#term), [Billed Cost](#col) excludes any portion [covered](#term) by related purchase [charges](#term) (e.g., [covering charges](#term) such as [commitments](#term), prepayments, or marketplace purchases), regardless of when those related [charges](#term) are invoiced.

[Billed Cost](#col) is denominated in the [Billing Currency](#col). [Billed Cost](#col) is commonly used to support FinOps activities, including invoice reconciliation, [cash-based](#term) forecasting, budgeting, and cost allocation.

## Requirements

[BilledCost](#col) MUST adhere to the following requirements:

* [BilledCost](#col) MUST be of type Decimal.
* [BilledCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [BilledCost](#col) MUST NOT be null.
* [BilledCost](#col) MUST be denominated in the [BillingCurrency](#col).
* [BilledCost](#col) MUST reflect all applicable pricing adjustments, including but not limited to [negotiated discounts](#term), [commitment discounts](#term), and other applicable discount programs.
* [BilledCost](#col) MUST NOT include any portion of a [covered charge](#term) that is offset by a [covering charge](#term).
* [BilledCost](#col) MUST be 0 for [charges](#term) that are fully [covered](#term) by one or more [covering charges](#term).
* The sum of [BilledCost](#col) for a given [InvoiceDetailId](#col), [InvoiceId](#col), and [InvoiceIssuerName](#col) MUST be equal to the payable amount provided in the corresponding entries on the issued invoice when [InvoiceIssueStatus](#col) is ["Issued"](#val:InvoiceDetail.InvoiceIssueStatus).
* When comparing [BilledCost](#col) aggregated by [InvoiceId](#col) and [InvoiceIssuerName](#col) with [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost) aggregated by [CostAndUsage.InvoiceId](#col:CostAndUsage.InvoiceId) and [CostAndUsage.InvoiceIssuerName](#col:CostAndUsage.InvoiceIssuerName), [BilledCost](#col) MUST adhere to the following requirements:
  * When [ChargeCategory](#col) is not ["Tax"](#val:InvoiceDetail.ChargeCategory) and [InvoiceIssueStatus](#col) is not ["Open"](#val:InvoiceDetail.InvoiceIssueStatus), the sum of [BilledCost](#col) MUST NOT differ from the sum of [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost) by more than `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)` as defined in [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).
  * When [ChargeCategory](#col) is ["Tax"](#val:InvoiceDetail.ChargeCategory) or [InvoiceIssueStatus](#col) is ["Open"](#val:InvoiceDetail.InvoiceIssueStatus), the sum of [BilledCost](#col) MAY differ from the sum of [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost).
* When comparing [BilledCost](#col) aggregated by [InvoiceDetailId](#col), [InvoiceId](#col), and [InvoiceIssuerName](#col) with [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost) aggregated by [CostAndUsage.InvoiceDetailId](#col:CostAndUsage.InvoiceDetailId), [CostAndUsage.InvoiceId](#col:CostAndUsage.InvoiceId), and [CostAndUsage.InvoiceIssuerName](#col:CostAndUsage.InvoiceIssuerName), [BilledCost](#col) MUST adhere to the following requirements:
  * When [InvoiceIssueStatus](#col) is not ["Open"](#val:InvoiceDetail.InvoiceIssueStatus), the sum of [BilledCost](#col) MUST NOT differ from the sum of [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost) by more than `MAX(100 × Subunit, (SQRT(Rows) × 0.5) × Subunit)` as defined in [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).
  * When [InvoiceIssueStatus](#col) is ["Open"](#val:InvoiceDetail.InvoiceIssueStatus), the sum of [BilledCost](#col) MAY differ from the sum of [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost).

## Implementation Guidance

### Handling Rounding Discrepancies

When validating [InvoiceDetail.BilledCost](#col:InvoiceDetail.BilledCost) against [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost), the totals may not be perfectly equal due to precision differences (e.g., 6 decimals in CostAndUsage vs. 2 decimals in InvoiceDetail). The requirement allows for a maximum rounding error based on the statistical probability of rounding variance, which grows with the square root of the row count.  For more information, see the [Rounding Variance Tolerance](#appendix.roundingvariancetolerance) appendix entry.

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

Cost of a [charge](#term) as invoiced by the [invoice issuer](#term) in a given [billing period](#term).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Invoice Detail](#ds)                       |
| Operating model conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | False                                       |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.4
