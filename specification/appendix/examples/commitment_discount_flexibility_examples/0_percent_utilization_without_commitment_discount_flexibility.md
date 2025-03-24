# 0% utilization with a non-matching resource without commitment discount flexibility with 1 resource

## Context

### Provider

For this example, fictitious provider, *TinyCloud*, offers the following SKU pricing details which are used in the example below.

#### SKUs & Rates

| ProviderName | Service | SkuId     | ListUnitPrice  | x_CommitmentDiscountUnitPrice  | x_NormalizationFactor |
|--------------|---------|-----------|----------------|--------------------------------|-----------------------|
| TinyCloud    | Compute | VM_Small  | $0.50          | $0.25                          | 1                     |
| TinyCloud    | Compute | VM_Medium | $1.00          | $0.50                          | 2                     |
| TinyCloud    | Compute | VM_Large  | $2.00          | $1.00                          | 4                     |
| TinyCloud    | Compute | VM_XLarge | $4.00          | $2.00                          | 8                     |

The above SKU pricing attributes show that this provider only has 1 service that offers 4 virtual machine SKUs at various list rates, [*commitment discount*](#glossary:commitmentdiscount) rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based *commitment discounts* with [*commitment discount flexibility*](#commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor equals the normalization factor of the *commitment discount*.

## Scenario

- 1 *commitment discount* is purchased for 1 year (2023) for 1 VM_Large.
- 1 VM_Medium resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

## Outcome

The VM_Large *commitment discount* is unused because no VM_Large resources are running. Additionally, 1 hour of on-demand usage was incurred by the running VM_Medium resource. These charges result in a $2 amortized cost.

```json
[
    {
        "BillingPeriodStart": "2023-01-01T00:00:00Z",
        "BillingPeriodEnd": "2023-02-01T00:00:00Z",
        "ChargePeriodStart": "2023-01-01T00:00:00Z",
        "ChargePeriodEnd": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Committed",
        "ResourceId": "<my-large-vm-id>",
        "PricingQuantity": 1.00,
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Large",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Unused",
        "CommitmentDiscountUnit": "Hour"
    },
    {
        "BillingPeriodStart": "2023-01-01T00:00:00Z",
        "BillingPeriodEnd": "2023-02-01T00:00:00Z",
        "ChargePeriodStart": "2023-01-01T00:00:00Z",
        "ChargePeriodEnd": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Standard",
        "ResourceId": "<my-medium-vm-id>",
        "PricingQuantity": 1.00,
        "BilledCost": 1.00,
        "EffectiveCost": 1.00,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Medium"
    }
]
```