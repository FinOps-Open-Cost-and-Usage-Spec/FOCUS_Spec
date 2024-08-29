# Commitment Discounts

A commitment discount is a billing discount model that offers reduced rates on preselected SKUs in exchange for an obligated usage or spend amount over a predefined term. Commitment discounts typically consist of a set of purchase and usage records within cost and usage datasets.

Usage-based commitment discounts obligate a customer to a total quantity of time of a preselected term, typically measured in "Hours".  In some cases, usage-based commitment discounts allow similar resources of different size classifications to relatively benefit from commitment discount rates.  This is typically known as "size flexibility", and is determined by multiplying the number of actual hours consumed by a resource by its predetermined normalization factor to derive the number of "Normalized Hours" consumed.

Spend-based commitment discounts obligate a customer to total monetary quantity over a preselected term, typically denoted by the invoice's selected billing currency (ex: "USD").

## Purchasing

While customers are bound to the term of a commitment discount, cloud-service providers, or CSPs, offer various payment options before and/or during the term:

* *Upfront* - The commitment discount is paid in full before the term begins.
* *Recurring* - The commitment discount is paid on a repeated basis, typically over each billing period of the term.
* *Hybrid* - Some of the commitment discount is paid before the term begins, and the rest is paid repeatedly over the term.

For example, if a customer buys a spend-based commitment discount for 1 year, with a $1.00 hourly commitment, and pays with the hybrid option, the commitment discount's payment consists of both:

1. *Upfront* - $4,380 (`24 hours * 365 days * $1.00 * 0.5`)
2. *Recurring* - $182.50 (`24 hours * 365 days * $1.00 / 12 months`)

## Usage

Commitment discounts follow a "use-it-or-lose-it" model where the amortization of a commitment discount's purchase applies evenly over each charge period of eligible resources over the term.

For example, if a customer buys a spend-based commitment with a $1.00 hourly commitment in January (31 days), only $1.00 is eligible for consumption for each hourly charge period.  This means that if a customer has eligible resources running during this charge period, some or all of the $1.00 that is allocated to the charge period will also be allocated to some or all of these resources.  Conversely, if a customer does not have eligible resources running during this charge period, the $1.00 allocated to the charge period is wasted.

## Commitment Discounts in FOCUS

Within the FOCUS specification, the following examples demonstrate how a commitment discount would appear across various payment and usage scenarios.

### Purchase Rows

All commitment discount purchases appear with a positive `BilledCost`, `PricingCategory` as "Committed", and the commitment discount's id populating both the `ResourceId` and `CommitmentDiscountId` value. Upfront purchases appear as a single record also with `ChargeCategory` as "Purchase", `ChargeFrequency` as "One-Time", and the total quantity and units for commitment discount's term as `CommitmentDiscountPurchasedQuantity` and `CommitmentDiscountUnit`, respectively.

Recurring purchases are allocated across all corresponding charge periods of the term when `ChargeCategory` is "Purchase", `ChargeFrequency` is "One-Time", and `CommitmentDiscountPurchasedQuantity` and `CommitmentDiscountUnit` are reflected only for that charge period.

Using the same commitment discount example as above, a one-year, spend-based commitment discount with a $1.00 hourly commitment purchased on Jan 1, 2023, various purchase options can occur:

#### Scenario #1: Upfront

The entire commitment is billed _once_ during the first charge period of the term for $8,670 (derived as `24 hours * 365 days * $1.00`).

```json
[
    {   
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01 00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 8760.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountPurchasedQuantity": 8760.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #2: Recurring

The commitment is billed across all 8,760 charge periods of the term with $1.00 allocated to each charge period over the term.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "Recurring",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 1.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountPurchasedQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    },

    /* ... 743 more recurring purchase records for the billing period ... */
]
```

#### Scenario #3: Hybrid

Half of the commitment is billed _once_ during the first charge period of the term for $4,380 (derived as `24 hours * 182.5 days * $1.00`), and the other half is billed across each charge period over the term, derived as (`$1.00 * 8,760 hours * 0.5`). Amortized costs incur half of the amount (i.e. $0.50) from the upfront purchase and the other half from the recurring purchase.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01 00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 4380.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountPurchasedQuantity": 4380.00,
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "Recurring",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 0.50,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountPurchasedQuantity": 0.50,
        "CommitmentDiscountUnit": "USD"
    },

    /* ... 743 more recurring purchase records for the billing period ... */
]
```

### Usage Rows

Amortization of commitment discounts occur the same way regardless of how one or more purchases are made.  The same usage-based or spend-based amount is applied evenly across all charge periods and potentially allocated to eligible resources.  Continuing with the same commitment discount example, a one-year, spend-based commitment discount with a $1.00 hourly commitment, 4 types of scenarios can occur during a charge period:

* Scenario #1: Eligible resource(s) runs for $1.00 (100% utilization)
* Scenario #2: No eligible resources run (0% utilization)
* Scenario #3: Eligible resource(s) runs for $0.75 (75% utilization)
* Scenario #4: Eligible resource(s) runs for over the $1.00 hourly commitment (100% utilization + overage)

#### Scenario #1: Eligible resource(s) runs for $1.00 (100% utilization)

In this scenario, one eligible resource runs for the full hour, so one row allocated to the resource is produced.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountConsumedQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #2: No eligible resources run (0% utilization)

In this scenario, the entire, eligible amount was unused, so one unused row, allocated to the commitment discount, was produced. Most notably, ConsumedQuantity and ConsumedUnit are null while CommitmentDiscountConsumedQuantity is not because $1 was still drawn down by the commitment discount even though it was not consumed by a resource.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "ConsumedQuantity": null,
        "ConsumedUnit": null,
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Unused",
        "CommitmentDiscountConsumedQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #3: Eligible resource(s) runs for $0.75 (75% utilization)

In this scenario, one eligible resource runs for the full hour. One row shows $0.75 to a resource, and the other shows that $0.25 remained unused.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 0.75,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountConsumedQuantity": 0.75,
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "ConsumedQuantity": null,
        "ConsumedUnit": null,
        "BilledCost": 0.00,
        "EffectiveCost": 0.25,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Unused",
        "CommitmentDiscountConsumedQuantity": 0.25,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #4: Eligible resource(s) runs for over the $1.00 hourly commitment (100% utilization + overage)

In this scenario, one eligible resource runs for the full hour and costs $1.50. One row shows that $1.00 was amortized from the commitment discount, and the other shows that $0.50 was charged as standard, on-demand spend.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountConsumedQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01 00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01 00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01 00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01 01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Standard",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.50,
        "EffectiveCost": 0.00
    }
]
```
