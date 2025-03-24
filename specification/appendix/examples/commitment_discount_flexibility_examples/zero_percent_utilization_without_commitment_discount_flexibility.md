# 0% utilization without commitment discount flexibility

## Context

### Provider

For this example, fictitious provider, *TinyCloud*, offers the following SKUs and corresponding unit prices which are used in the example below.

#### SKU Catalog

| Service | Sku ID    | Sku Price ID                            | Sku Price Unit Price | Normalization Factor |
|---------|-----------| ----------------------------------------|----------------------| ---------------------|
| Compute | VM_SMALL  | VM_SMALL_COMMITTED_PURCHASE_NO_UPFRONT  | $0.50                | 1                    |
| Compute | VM_MEDIUM | VM_MEDIUM_COMMITTED_PURCHASE_NO_UPFRONT | $1.00                | 2                    |
| Compute | VM_LARGE  | VM_LARGE_COMMITTED_PURCHASE_NO_UPFRONT  | $1.50                | 3                    |
| Compute | VM_XLARGE | VM_XLARGE_COMMITTED_PURCHASE_NO_UPFRONT | $2.00                | 4                    |
| Compute | VM_SMALL  | VM_SMALL_COMMITTED_HOUR                 | $0.50                | 1                    |
| Compute | VM_MEDIUM | VM_MEDIUM_COMMITTED_HOUR                | $1.00                | 2                    |
| Compute | VM_LARGE  | VM_LARGE_COMMITTED_HOUR                 | $1.50                | 3                    |
| Compute | VM_XLARGE | VM_XLARGE_COMMITTED_HOUR                | $2.00                | 4                    |
| Compute | VM_SMALL  | VM_SMALL_ON_DEMAND_HOUR                 | $1.00                | 1                    |
| Compute | VM_MEDIUM | VM_MEDIUM_ON_DEMAND_HOUR                | $2.00                | 2                    |
| Compute | VM_LARGE  | VM_LARGE_ON_DEMAND_HOUR                 | $3.00                | 3                    |
| Compute | VM_XLARGE | VM_XLARGE_ON_DEMAND_HOUR                | $4.00                | 4                    |

The above records show that this provider only has 1 service that offers 4 virtual machine SKUs at various list unit prices, [*commitment discount*](#glossary:commitmentdiscount) unit prices, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* unit price. Usage-based *commitment discounts* with [*commitment discount flexibility*](#commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

## Scenario

- 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM_LARGE.
- 1 VM_MEDIUM resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

## Outcome

- 1 recurring, purchase record exists for 1 eligible "Hour" of the no upfront, *commitment discount* and incurs a $1.50 [*BilledCost*](#billedcost).
- The VM_LARGE *commitment discount* is unused for the correspending [*charge period*](#glossary:chargeperiod) because no VM_LARGE resources are running and incurs a $1.50 [*EffectiveCost*](#effectivecost).
- 1 hour of on-demand usage is incurred by the VM_MEDIUM resource and incurs a $2.00 *BilledCost* and *EffectiveCost*.

```json
[   
    {
        "BillingPeriodStart": "2023-01-01T00:00:00Z",
        "BillingPeriodEnd": "2023-02-01T00:00:00Z",
        "ChargePeriodStart": "2023-01-01T00:00:00Z",
        "ChargePeriodEnd": "2023-01-01T01:00:00Z",
        "ChargeCategory": "Purchase",
        "ChargeFrequency": "Recurring",
        "PricingCategory": "Standard",
        "ResourceId": "<my-commitment-discount-id>",
        "PricingQuantity": 1.00,
        "ListUnitPrice": 3.00,
        "ListCost": 3.00,
        "x_CommitmentDiscountUnitPrice": 1.50,
        "BilledCost": 1.50,
        "EffectiveCost": 0.00,
        "ConsumedQuantity": null,
        "ConsumedUnit": null,
        "SkuId": "VM_LARGE",
        "SkuPriceId": "VM_LARGE_COMMITTED_PURCHASE_NO_UPFRONT",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountCategory": "Usage",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": null,
        "CommitmentDiscountUnit": "Hour"
    },
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
        "ListUnitPrice": 3.00,
        "ListCost": 3.00,
        "x_CommitmentDiscountUnitPrice": 1.50,
        "BilledCost": 0.00,
        "EffectiveCost": 1.50,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_LARGE",
        "SkuId": "VM_LARGE_COMMITTED_HOUR",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountCategory": "Usage",
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
        "ListUnitPrice": 2.00,
        "ListCost": 2.00,
        "x_CommitmentDiscountUnitPrice": 1.00,
        "BilledCost": 2.00,
        "EffectiveCost": 2.00,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_MEDIUM_ON_DEMAND_HOUR",
        "CommitmentDiscountId": null,
        "CommitmentDiscountCategory": null,
        "CommitmentDiscountQuantity": null,
        "CommitmentDiscountStatus": null,
        "CommitmentDiscountUnit": null
    }
]
```
