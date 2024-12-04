# Correction Handling - (Refund & Credit Handling)

// Need glossary definition?
// Need to call out positive adjustments?

//applies where charge class is correction????

Refunds & late arriving costs are examples of....
 represent line items that appear in the FOCUS data set to support any scenarios where providers need to adjust a charge to a consumer. These scenarios include: 

- experiencing a billing technical error (i.e. charging the incorrect rate for a service line item)
- providing a promotional benefit (i.e. migration credits or new service incentives)

FOCUS supports two distinct models for the representation of corrections (Refunds & Credits) in the specification with the understanding that providers typically support the 'Bulk' record style, but SHOULD support the 'Itemized' record style where possible to improve visibility into this data set.

## Bulk

Single line item correction where both billing period and usage period will share the same value and be represented within the current billing cycle
WHERE 'Charge Class' = Correction & 'Charge Category' SHOULD = Credit / Adjustment

this solution is simpler for providers to implement but adds complexity for FOCUS data consumers as the refund / credit is decoupled form the service being credited for


## Itemized

WHERE 'Charge Class' = Correction & 'Charge Category' SHOULD = Usage / Purchase / Credit
MUST be perSku and perSkuPrice

Multi line item correction that follows the billing format and time period of the items that are being corrected i.e the billing period will be the current billing cycle but the usage period will share the same datetime values for the original line items that are being corrected.

this solution is more complex for providers to implement but alignes the refund line items to the service and time period being refunded providing a more accurate billing history and representation, whilst maintaining support for invoice reconciliation. 

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Current value                      | ChargeCategory | ChargeClass | Scenario                                                                                                                                                                                                                                                                                                                                                   |
| --------- | ---------------------------------- | ---------- |  ---------- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS       | Anniversary / Usage                | Usage      | NULL      | Usage charged at on-demand rate for resources with resource id (EC2, EBS, RDS, RedShift)                                                                                                                                                                                                                                                                   |
| AWS       | Anniversary / Usage                | Usage      | NULL      | Usage charged at on-demand rate for resources with "no resource id" (Support, CloudWatch, DataTransfer)                                                                                                                                                                                                                                                    |
| AWS       | Anniversary / Tax                  | Tax        | NULL      | US sales tax or VAT with "no resource id"                                                                                                                                                                                                                                                                                                                  |
| AWS       | Purchase / Fee                     | Purchase   | NULL      | All upfront and partial upfront fees for RI purchase                                                                                                                                                                                                                                                                                                       |
| AWS       | Purchase / RIFee                   | Purchase   | NULL      | Monthly recurring RI amount for partial upfront and no upfront                                                                                                                                                                                                                                                                                             |
| AWS       | Purchase / SavingsPlanUpfrontFee   | Purchase   | NULL      | All upfront and partial upfront fees for SP purchase                                                                                                                                                                                                                                                                                                       |
| AWS       | Purchase / SavingsPlanRecurringFee | Purchase   | NULL      | Monthly recurring SP amount for partial upfront and no upfront                                                                                                                                                                                                                                                                                             |
| AWS       | Adjustments / SavingsPlanNegation  | Usage      | NULL      | Used to negate the on-demand cost covered by SP                                                                                                                                                                                                                                                                                                            |
| AWS       | Anniversary / BundledDiscount      | Usage      | Correction | Usage based discount for free or discounted price. If a customer uses X units of product/service A, this customer gets Y units of product/service B at a discounted price (with a discount Z%).                                                                                                                                                            |
| AWS       | Refund                             | Adjustment | Correction |
| GCP       | regular                            | Usage      | NULL      | These show up as rows that contain data of usage and costs                                                                                                                                                                                                                                                                                                 |
| GCP       | tax                                | Tax        | NULL      | These show up as monthly rows without a project as a credit and with a project with a debit.                                                                                                                                                                                                                                                               |
| GCP       | adjustment                         | Adjustment | Correction | ![Screenshot of GCP cost details with type and mode columns.](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/af90e4cd-f3c0-448a-bb0f-0249bcf7135c)<br>Example 1:<br>Description: "Billing correction - Adjustment for project X for incorrect Flexible CUD charge"<br>Mode: "MANUAL_ADJUSTMENT"<br>Type: "GENERAL_ADJUSTMENT" |
| GCP       | adjustment                         | Adjustment | Correction | GENERAL_ADJUSTMENT - MANUAL ADJUSTMENT |
| GCP       | adjustment                         | Adjustment | Correction | PRICE_CORRECTION - COMPLETE NEGATION WITH REMONITIZATION |
| GCP       | adjustment                         | Adjustment | Correction | GENERAL_ADJUSTMENT - GOODWILL |
| GCP       | adjustment                         | Adjustment | Correction | NULL - NULL |
| GCP       | adjustment                         | Adjustment | Correction | USAGE_CORRECTION - COMPLETE NEGATION WITH REMONITIZATION |
| GCP       | adjustment                         | Adjustment | Correction | USAGE_CORRECTION - COMPLETE NEGATION |
| GCP       | rounding_error                     | Adjustment | NULL      | These show up as monthly rows without a project as a credit                                                                                                                                                                                                                                                                                                |
| GCP       | credit                             | Adjustment | Correction | THIS IS BROKEN: Fields: type, name, amount, full_name, id<br>![Screenshot of a table with a type column and 5 rows of example values](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/15bcc210-5a36-473b-aeac-c1d2682dfdc8)                                                                                                                    |
| GCP       | credit                             | Adjustment | Correction | DISCOUNT |
| GCP       | credit                             | Adjustment | Correction | PROMOTION |
| GCP       | credit                             | Adjustment | Correction | NULL |
| GCP       | credit                             | Adjustment | NULL       | FREE_TIER ----- should this not be usage? |
| GCP       | credit                             | Adjustment | NULL       | COMMITTED_USAGE_DISCOUNT  ----- should this not be usage?|
| Microsoft | Purchase                           | Purchase   | NULL      | Upfront or recurring fee for Marketplace offers or commitment discounts.                                                                                                                                                                                                                                                                             |
| Microsoft | Usage                              | Usage      | NULL      | Consumption-based usage of deployed resources.                                                                                                                                                                                                                                                                                                             |
| Microsoft | Refund                             | Adjustment | Correction | Refund provided by support.                                                                                                                                                                                                                                                                                                                                |
| Microsoft | Adjustment                         | Adjustment | NULL      | Rounding errors.                                                                                                                                                                                                                                                                                                                                           |
| Microsoft | Tax                                | Tax        | NULL      | US sales tax or VAT.                                                                                                                                                                                                                                                                                                                                       |

## Record Styles Intended Usage

| ChargeCategory | ChargeClass | record style       | SkuId              | SkuPriceId         |
|----------------|-------------|--------------------|--------------------|--------------------|
| Usage          | (null)      | MUST be Itemized   | MUST not be null   | MUST not be null   |
| Usage          | Correction  | SHOULD be Itemized | SHOULD not be null | SHOULD not be null |
| Purchase       | (null)      | MUST be Itemized   | MUST not be null   | MUST not be null   |
| Purchase       | Correction  | SHOULD be Itemized | SHOULD not be null | SHOULD not be null |
| Credit         | (null)      | Not Valid          | MAY be null        | MAY be null        |
| Credit         | Correction  | MAY be bulk        | MAY be null        | MAY be null        |
| Adjustment     | (null)      | MAY be bulk        | MAY be null        | MAY be null        |
| Adjustment     | Correction  | MAY be bulk        | MAY be null        | MAY be null        |
| Tax            | (null)      | MUST be bulk       | MUST be null       | MUST be null       |
| Tax            | Correction  | MUST be bulk       | MUST be null       | MUST be null       |

## Examples

Within the FOCUS specification, the following examples demonstrate how a refund or credit appears across various usage scenarios.

### Bulk Refunds

The entire correction / refund is billed _once_ during the first applicable *billing period*.

```json
[
    {   
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01T00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Standard",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 8760.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 8760.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

### Itemized Refunds

The correction / refund is billed _daily_ during the first applicable *billing period* but adds records to the applicable *charge period*.

```json
[
    {   
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01T00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Standard",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 8760.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 8760.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

