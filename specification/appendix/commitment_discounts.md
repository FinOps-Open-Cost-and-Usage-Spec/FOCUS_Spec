# Commitment Discounts

A commitment discount is a billing discount model that offers reduced rates on preselected SKUs in exchange for an obligated usage or spend amount over a predefined term. Commitment discounts typically consist of a set of purchase and usage records within cost and usage datasets.

Usage-based commitment discounts obligate a customer to a predetermined amount of usage over a preselected term, typically measured in "Hours". In some cases, usage-based commitment discounts allow similar resources of different size classifications to relatively benefit from commitment discount rates. This is typically known as *commitment flexibility*, and can be derived by multiplying the number of actual resource hours consumed by a predefined SKU-based coefficient, sometimes referred to as a *normalization factor* or *ratio*, to derive the number of normalized hours consumed.

Spend-based commitment discounts obligate a customer to a predetermined amount of spend over a preselected term, typically denoted by the invoice's selected billing currency (ex: "USD").

## Purchasing

While customers are bound to the term of a commitment discount, cloud-service providers offer some or all of the following payment options before and/or during the term:

* *Upfront* - The commitment discount is paid in full before the term begins.
* *Recurring* - The commitment discount is paid on a repeated basis, typically over each billing period of the term.
* *Partial* - Some of the commitment discount is paid before the term begins, and the rest is paid repeatedly over the term.

For example, if a customer buys a 1-year, spend-based commitment discount with a $1.00 hourly commit and pays with the partial option, the commitment discount's payment consists of 1 upfront purchase in the beginning of the term *and* monthly recurring purchases with the following totals:

1. *Upfront* - $4,380 (`24 hours * 365 days * $1.00 * 0.5`)
2. *Recurring* - $182.50 (`24 hours * 365 days * $1.00 / 12 months`)

## Usage

Commitment discounts follow a "use-it-or-lose-it" model where the amortization of a commitment discount's purchase applies evenly to eligible resources over each charge period of the term.

For example, if a customer buys a spend-based commitment with a $1.00 hourly commitment in January (31 days), only $1.00 is eligible for consumption for each hourly charge period. If a customer has eligible resources running during this charge period, an amount of up to $1.00 will be allocated to these resources. Conversely, if a customer does have eligible resources running that fully take advantage of this $1.00 during this charge period, then some or all of this amount will go to waste.

## Commitment Discounts in FOCUS

Within the FOCUS specification, the following examples demonstrate how a commitment discount appears across various payment and usage scenarios.

### Purchase Rows

All commitment discount purchases appear with a positive `BilledCost`, `PricingCategory` as "Committed", and with the commitment discount's id populating both the `ResourceId` and `CommitmentDiscountId` value. Upfront purchases appear as a single record with `ChargeCategory` as "Purchase", `ChargeFrequency` as "One-Time", and the total quantity and units for commitment discount's term reflected as `CommitmentDiscountQuantity` and `CommitmentDiscountUnit`, respectively.

Recurring purchases are allocated across all corresponding charge periods of the term when `ChargeCategory` is "Purchase", `ChargeFrequency` is "Recurring", and `CommitmentDiscountQuantity` and `CommitmentDiscountUnit` are reflected only for that charge period.

Using the same commitment discount example as above with a one-year, spend-based commitment discount with a $1.00 hourly commitment purchased on Jan 1, 2023, various purchase options are available:

#### Scenario #1: Upfront

The entire commitment discount is billed _once_ during the first charge period of the term for $8,670 (derived as `24 hours * 365 days * $1.00`).

```json
[
    {   
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01T00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 8760.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 8760.00,
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #2: Recurring

The commitment discount is billed across all 8,760 (`24 hours * 365 days`) charge periods of the term with $1.00 allocated to each charge period over the term.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "Recurring",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 1.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountUnit": "USD"
    },

    /* ... 8,759 more recurring purchase records for the term ... */
]
```

#### Scenario #3: Partial

With a 50/50 split, half of the commitment is billed _once_ during the first charge period of the term for $4,380 (derived as `24 hours * 182.5 days * $1.00`), and the other half is billed across each charge period over the term, derived as (`$1.00 * 8,760 hours * 0.5`). Amortized costs incur half of the amount (i.e. $0.50) from the upfront purchase and the other half from the recurring purchase.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2024-01-01T00:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "One-Time",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 4380.00,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 4380.00,
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "Recurring",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "BilledCost": 0.50,
        "EffectiveCost": 0.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 0.50,
        "CommitmentDiscountUnit": "USD"
    },

    /* ... 8,759 more recurring purchase records for the term ... */
]
```

### Usage Rows

Amortization of commitment discounts occur similarly regardless of how commitment discount purchases are made.  The same usage-based or spend-based amount is applied evenly across all charge periods and potentially allocated to eligible resources.  Continuing with the same commitment discount example, a one-year, spend-based commitment discount with a $1.00 hourly commitment and 1 resource yields 4 types of scenarios that can occur during a charge period:

* Scenario #1: An eligible resource fully consumes the allocated amount (100% utilization)
* Scenario #2: No eligible resource consumes the allocated amount (0% utilization)
* Scenario #3: An eligible resource partially consumes the allocated amount (75% utilization)
* Scenario #4: An eligible resource fully consumes the $1.00 hourly commitment with an overage (100% utilization + overage)

#### Scenario #1: An eligible resource fully consumes the allocated amount (100% utilization)

In this scenario, one eligible resource runs for the full hour and consumes $1.00, so one row allocated to the resource is produced.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #2: No eligible resource consumes the allocated amount (0% utilization)

In this situation, the full eligible, $1.00 amount remained unutilized and results in 1 unused row. In this scenario, it is important to note that while `CommitmentDiscountQuantity` is not because $1 was still drawn down by the commitment discount even though, no resource was allocated, so `ConsumedQuantity` and `ConsumedUnit` are null.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "ConsumedQuantity": null,
        "ConsumedUnit": null,
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Unused",
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #3: An eligible resource partially consumes the allocated amount (75% utilization)

In this scenario, one eligible resource runs for the full hour and consumes $0.75 of the $1.00 allocation. One row shows $0.75 to a resource, and the other shows that $0.25 was unused.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 0.75,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 0.75,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<commitment-discount-id>",
        "ConsumedQuantity": null,
        "ConsumedUnit": null,
        "BilledCost": 0.00,
        "EffectiveCost": 0.25,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 0.25,
        "CommitmentDiscountStatus": "Unused",
        "CommitmentDiscountUnit": "USD"
    }
]
```

#### Scenario #4: An eligible resource fully consumes the $1.00 hourly commitment with an overage (100% utilization + overage)

In this scenario, one eligible resource runs for the full hour and is charged $1.50. One row shows that $1.00 was amortized from the commitment discount, and the other shows that $0.50 was charged as standard, on-demand spend.

```json
[
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<resource-id>",
        "ConsumedQuantity": 1,
        "ConsumedUnit": "Hour",
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "USD"
    },
    {
        "BillingPeriodStartDate": "2023-01-01T00:00:00Z",
        "BillingPeriodEndDate": "2023-02-01T00:00:00Z",
        "ChargePeriodStartDate": "2023-01-01T00:00:00Z",
        "ChargePeriodEndDate": "2023-01-01T01:00:00Z",
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
