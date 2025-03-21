# 100% utilization with 1 VM_Large resource with commitment discount flexibility with 1 resource

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

The above SKU pricing attributes show that this provider only has 1 service that offers 4 virtual machine SKUs at various list rates, *commitment discount* rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based [*commitment discounts*](#glossary:commitmentdiscount) with [*commitment discount flexibility*](#commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor equals the normalization factor of the *commitment discount*.

## Scenario

1 *commitment discount* is purchased for 1 year (2023) for 1 VM_Small which has a normalization factor of 1.
1 VM_Large resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4.

## Outcome

The VM_Small *commitment discount* was fully utilized but still only covered 25% of the VM_Large resource, so the rest of the VM incurred an on-demand cost of $1.50, and the amortized cost for this resource is $1.75.

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
        "PricingQuantity": 0.25,
        "BilledCost": 0.00,
        "EffectiveCost": 0.25,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Large",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "Normalized Hour"
    },
    {
        "BillingPeriodStart": "2023-01-01T00:00:00Z",
        "BillingPeriodEnd": "2023-02-01T00:00:00Z",
        "ChargePeriodStart": "2023-01-01T00:00:00Z",
        "ChargePeriodEnd": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Usage",
        "ChargeFrequency": "Usage-Based",
        "PricingCategory": "Standard",
        "ResourceId": "<my-large-vm-id>",
        "PricingQuantity": 0.75,
        "BilledCost": 1.50,
        "EffectiveCost": 1.50,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Large"
    }
]
```