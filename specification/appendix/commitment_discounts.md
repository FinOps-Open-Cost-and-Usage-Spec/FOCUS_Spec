# Commitment Discounts

A commitment discount is a billing discount that offers reduced rates on preselected SKUs in exchange for an obligated usage or spend amount over a predefined term. Within cost and usage datasets, commitment discounts typically consist of a set of purchases and usage records.

## Purchases

While customers are bound to the term of a commitment discount, cloud-service providers, or CSPs, offer various payment options before and/or during the term:

* In-Advance - The commitment discount is paid in full before the term begins
* Monthly - The commitment discount is paid monthly over the term.
* Hybrid (In-Advance & Monthly) - Half of the commitment discount is paid in-advance and half is paid monthly over the term.

For example, if a customer buys a spend-based commitment discount for 1 year, with a $1.00 hourly commitment, and pays with the hybrid option, their purchase schedule is:

* In-Advance: $4,380 (24 hours \* 365 days \* $1.00 \* 0.5)
* Monthly: $182.50 (24 hours \* 365 days \* $1.00 / 12 months)

## Usage

Commitment discounts follow a "use-it-or-lose-it" model where the amortization of a commitment discount's purchase applies evenly over each charge period (typically hourly) over the term.

For example, if a customer buys a spend-based commitment with a $1.00 hourly commitment in January (31 days), only $1.00 is eligible for amortization for each hourly charge period.  This means that if I have eligible resources running during this charge period, some or all of the $1.00 allocated to the charge period will be also be allocated to one or more resources.  Conversely, if I don't have eligible resources running during this charge period, the $1.00 allocated to the charge period is wasted.

## Commitment Discounts in FOCUS

Within the FOCUS specification, the following examples demonstrate how a commitment discount would appear across various payment and amortization scenarios.

### Purchase Rows

All commitment discount purchases appear with a positive `BilledCost`, `PricingCategory:Committed`, and the commitment discount's id as both the `ResourceId` and `CommitmentDiscountId` value. In-advance purchases appear as a single record also with `ChargeCategory:Purchase`, `ChargeFrequency:One-Time`, and the commitment discount's entire purchased quantity, `CommitmentDiscountPurchasedQuantity`, and units, `CommitmentDiscountUnit` for the term.

Monthly purchases are spread across all corresponding charge periods of the term also with `ChargeCateogry:Purchase`, `ChargeFrequency:One-Time`, and the commitment discount's purchase quantity, `CommitmentDiscountPurchasedQuantity`, and units, `CommitmentDiscountUnit` for the charge period.

Using the same example as above, various purchase for a one-year, spend-based commitment discount with a $1.00 hourly commitment purchased on Jan 1, 2023 can be seen as:

#### In-Advance

The entire commitment is billed _once_ during the first charge period of the term for $8,670 (24 hours \* 365 days \* $1.00).

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

#### Monthly

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

    /* ... more recurring purchase records ... */
]
```

#### Hybrid (In-Advance & Monthly)

Half of the commitment is billed _once_ during the first charge period of the term _and_ the other half is billed across each charge period over the term. Amortized costs incur half of the amount (i.e. $0.50) from the in-advance purchase and the other half from monthly purchase.

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
        "BilledCost": 1.00,
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

    /* ... more recurring purchase records ... */
]
```

### Usage Rows

Amortization of commitment discounts occur the same way no matter how a purchase(s) are made.  The same fixed usage-based or spend-based amount is applied evenly across all charge periods to eligible resources.  Continuing with the same one-year, spend-based commitment discount with a $1.00 hourly commitment as above, there are 4 possible types of scenarios that can occur with eligible resource(s) during a charge period:

* Scenario 1: 1 resource runs for $1.00 (100% utilization)
* Scenario 2: No eligible resources run (0% utilization)
* Scenario 3: 1 resource runs for $0.75 (75% utilization)
* Scenario 4: 1 resource runs for over the $1.00 hourly commitment (100% utilization + overage)

#### Scenario 1: 1 resource runs for $1.00 (100% utilization)

In this scenario, one eligible resource runs for the full hour and costs $1.00.

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
        "ConsumedUnit": "Hour"
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountConsumedQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario 2: No eligible resources run (0% utilization)

In this scenario, the entire, eligible amount was unused and remained allocated to the commitment discount.

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

#### Scenario 3: 1 resource runs for $0.75 (75% utilization)

In this scenario, one eligible resource runs for the full hour, costs $0.75, and leaves $0.25 as unused.

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

#### Scenario 4: 1 resource runs for over the $1.00 hourly commitment (100% utilization + overage)

In this scenario, one eligible resource runs for the full hour and costs $1.50. $1.00 was amortized from the commitment discount, and $0.50 was charge as standard, on-demand spend.

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
