# 100% utilization without commitment discount flexibility

## Context

For this example, fictitious provider, *TinyCloud*, offers the following SKU catalog which is used in the scenario below.

### SKU Catalog

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

The above SKU pricing attributes show that this provider only has 1 service that offers 4 virtual machine SKUs at various list rates, [*commitment discount*](#glossary:commitmentdiscount) rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based *commitment discounts* with [*commitment discount flexibility*](#commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

## Scenario

* 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM_LARGE.
* 1 VM_LARGE resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

## Outcome

* 1 recurring, purchase record exists for 1 eligible "Hour" of the no upfront, *commitment discount* and incurs a $1.50 [*BilledCost*](#billedcost).
* The *commitment discount* covers the first [*charge period*](#glossary:chargeperiod) for 1 VM_LARGE resource incurring a $1.50 [*EffectiveCost*](#effectivecost).

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
        "SkuPriceId": "VM_LARGE_COMMITTED_HOUR",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountCategory": "Usage",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "Hour"
    }
]
```
