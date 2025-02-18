

--------------------------------------------------------------------------------

## Record Styles Intended Usage

| ChargeCategory | ChargeClass | record style       | SkuId              | SkuPriceId         |
|----------------|-------------|--------------------|--------------------|--------------------|
| Usage          | (null)      | MUST be Itemized   | MUST not be null   | MUST not be null   |
| Usage          | Correction  | SHOULD be Itemized | SHOULD not be null | SHOULD not be null |
| Purchase       | (null)      | MUST be Itemized   | MUST not be null   | MUST not be null   |
| Purchase       | Correction  | SHOULD be Itemized | SHOULD not be null | SHOULD not be null |
| Credit         | (null)      | MAY be bulk        | MAY be null        | MAY be null        |
| Credit         | Correction  | MAY be bulk        | MAY be null        | MAY be null        |
| Adjustment     | (null)      | MAY be bulk        | MAY be null        | MAY be null        |
| Adjustment     | Correction  | MAY be bulk        | MAY be null        | MAY be null        |
| Tax            | (null)      | MUST be bulk       | MUST be null       | MUST be null       |
| Tax            | Correction  | MUST be bulk       | MUST be null       | MUST be null       |

## Examples

Show scenarios where correction happens within current billing periond and also where it applies to previous billing period.... highlight charge period differences and itemized vs not itemized... note in billing period segmentation 

Within the FOCUS specification, the following examples demonstrate how a refund or credit appears across various usage scenarios.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Bulk | Correction to multiple billing errors | Correction | Usage | NULL | NULL | -5000 | 2023-02-01T00:00:00Z | 2023-02-01T00:00:00Z |

In this scenario we are correcting multiple errors in a bulk single line item. This is NOT PREFERRED as the correction record is not represented agains the accounts where the original usage was incurred.

All Corrections in the below examples should be itemized to the ResourceId and SkuPriceId

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Usage & Cost | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Usage & Cost | Correction to Compute usage in US East | Correction | Usage | -300 | 1 | -300 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |

In this scenario we are correcting the usage and the associated cost for this misbilled usage maintaining cost calculation integrity rules.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Simple Usage | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Simple Usage | Correction to Compute usage in US East | Correction | Usage | -300 | NULL | NULL | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |

In this scenario we are utilizing the NULLABILITY of the Rate and Cost columns to make a correction to a usage volume that did NOT have a corresponding impact on cost.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Simple Rate  | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Simple Rate  | Correction to Compute usage in US East | Correction | Usage | NULL | NULL | -300 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |

In this scenario we are utilizing the NULLABILITY of the Rate and Volume columns to make a correction to a cost that did NOT have a corresponding impact on the volume of serviece consumed.

Riley:
Usage and billing correction done at separate times and as separate line items (NOTE: the usage corrections may be multiple line items but the cost corrections may be in bulk --- THIS IS NOT PREFERRED)
| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Separate Events | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Separate Events | Correction to Compute usage in US East | Correction | Usage | -300 | NULL | NULL | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Separate Events | Corrected Compute cost in US East | Correction | Usage | NULL | NULL | -300 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |




### PREFERRED CORRECTION APPROATCH

The main difference here is that usage / corrections are supplied in triplicate which improves transparency and data consistency. NOTE: this increases data volumes compared to the duplicate mechanism describes above

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Accounting Usage | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Accounting Usage | Correction to Compute usage in US East | Correction | Usage | -1500 | 1 | -1500 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Accounting Usage | Corrected Compute usage in US East | Correction | Usage | 1300 | 1 | 1300 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |

In this scenario we maintain cost calculation integrity rules by using the first correction record to fully negate the original record that contained the error. We then supply a new complete billing record containing the corrected usage data. This follows accounting data principals.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|
| Accounting Rate | Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Accounting Rate | Correction to Compute usage in US East | Correction | Usage | -1500 | 1 | -1500 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |
| Accounting Rate | Corrected Compute usage in US East | Correction | Usage | 1500 | 0.8 | 1200 | 2023-02-01T00:00:00Z | 2023-01-01T00:00:00Z |

In this scenario we maintain cost calculation integrity rules by using the first correction record to fully negate the original record that contained the error. We then supply a new complete billing record containing the corrected rate and cost data. This follows accounting data principals.


### In the Event of Billing File Regeneration / Restatement

FOCUS billing generators MUST NOT regenerate historic billing data from PREVIOUSLY CLOSED BILLING PERIODS as it decouples the invoicing cycle from the billing activity data.

In this case where historic billing data is regenerated practicioners are not able to reconclie the billing period start to when they are invoiced for the correction.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start | Invoice ID |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|---------------|
| Simple  | REMOVED - Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z | ID123 |
| Simple  | Compute usage in US East | NULL| Usage | 1200 | 1 | 1200 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z | ID456 |

NOTE: this correction record will be invoiced in 2023-02 but will appear in the billing data for 2023-01

### In the Event of Late Arriving Costs

FOCUS billing generators MUST NOT regenerate historic billing data from PREVIOUSLY CLOSED BILLING PERIODS as it decouples the invoicing cycle from the billing activity data.

In this case where historic billing data is regenerated practicioners are not able to reconclie the billing period start to when they are invoiced for the correction.

| Example Scenario | Item Description | ChargeCategory | ChargeClass | Volume | Rate | Cost | Billing Period Start | Charge Period Start | Invoice ID |
|------------------|------------------|----------------|-------------|--------|------|------|----------------------|-----------------|---------------|
| Simple  | REMOVED - Compute usage in US East | NULL | Usage | 1500 | 1 | 1500 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z | ID123 |
| Simple  | Compute usage in US East | NULL| Usage | 1200 | 1 | 1200 | 2023-01-01T00:00:00Z | 2023-01-01T00:00:00Z | ID456 |

NOTE: this correction record will be invoiced in 2023-02 but will appear in the billing data for 2023-01


DO AN EXAMPLE WITH A PURELY USAGE CORRECTION--- DOES THIS IMPACT>?>?
do i need to show a difference between billed vs effective cost???
Restated Field?????

once boundar is crosed we cancorect the charge
usage is corrected retrospecifely
???
does the billed vs effecttive help with this


#### NOTES

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

# Correction Handling (incl. Refunds & Credits)

this document assumes we do not support regenerating/restating data from previously closed billing periods
you SHOULD NOT regenerate data from previoulsy closed billing periods

Corrections are line items that appear in the FOCUS data set to support any scenarios where providers need to adjust a charge to a consumer. These scenarios include: 

- [*Refund*](#glossary:refund) - experiencing a billing technical error (i.e. charging the incorrect rate/volume for a service line item)
- [*Credit*](#glossary:credit) - providing a promotional benefit (i.e. migration incentives or new service incentives)

Refunds are applied to retrospective charge records where the usage has already been incurred whereas credits are applied in a forward looking perspective and are consumed ('burned-down') by future usage.

[*Refunds*](#glossary:refund) are intentionally not a separate 'Charge Category' in FOCUS as the objective is to have these adjustments handled as itemized 'Usage' or 'Purchase' correction records that can be recorded alongside the itemised charge record that is being refunded. This eliminates the chargeback reverse-enginnering practicioners face when handling bulk refunds that are submitted as a single line item (as the practicioner then needs to split that line item up and work out who should be refunded for what).

FOCUS supports two distinct models for the representation of corrections (Refunds & Credits) in the specification with the understanding that providers typically support the 'Bulk' record style, but SHOULD support the 'Itemized' record style where possible to improve visibility into this data set.

# Credit (you can have a refund/correcton of a credit)
Credits can be supplied as bulk or itemised charge line items as most appropriate. Credits may also have subsequent correction records that should follow the format of the original record.

do we expect negative values? (TODO: look at all charge categories)


# Refund
## Bulk

Single line item correction where both billing period and usage period will share the same value and be represented within the current billing cycle
WHERE 'Charge Class' = Correction & 'Charge Category' SHOULD = Credit / Adjustment

this solution is simpler for providers to implement but adds complexity for FOCUS data consumers as the refund / credit is decoupled form the service being credited for


## Itemized

WHERE 'Charge Class' = Correction & 'Charge Category' SHOULD = Usage / Purchase / Credit
MUST be perSku and perSkuPrice

Multi line item correction that follows the billing format and time period of the items that are being corrected i.e the billing period will be the current billing cycle but the usage period will share the same datetime values for the original line items that are being corrected.

this solution is more complex for providers to implement but alignes the refund line items to the service and time period being refunded providing a more accurate billing history and representation, whilst maintaining support for invoice reconciliation. 
