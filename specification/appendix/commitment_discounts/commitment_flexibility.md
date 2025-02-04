# Commitment Flexibility

A usage-based commitment discount obligates a customer to a usage amount for one or more related SKUs in return for reduced rates.  For example, a usage-based commitment discount is purchased to cover a specific database SKU, this commitment will cover every hour over the term where at least one instance of this SKU is running. It can also cover eligible resources wholly, where 1 hour is covered by 1 resource, or partially, where 1 committed hour can be split across multiple resources or 1 resource can be fully covered with unused commitment discount costs. These latter two examples are commonly known as *commitment flexibility*.

When mixing usage-based commitment discounts with and without commitment flexibility with `CommitmentDiscountQuantity` measured by time, it is important to differentiate the `CommitmentDiscountUnit` for each type of commitment discount. In each scenario below, commitment discounts *without* commitment flexibility applied use "Hour" as a `CommitmentDiscountUnit`, and conversely commitment discounts *with* commitment flexibility use "Normalized Hour" as a `CommitmentDiscountUnit`.

Since providers have different rules for when commitment flexibility is or is not enabled, the following, fictitious SKU pricing attributes will be used in each example below, and each example will be categorized under commitment flexibility enabled or disabled sections.

## SKUs & Rates

| ProviderName | Service | SkuId     | ListUnitPrice  | x_CommitmentDiscountUnitPrice | x_NormalizationFactor |
| ------------ | ------- | --------- | -------------- | ------------------------------| --------------------- |
| TinyCloud    | Compute | VM_Small  | $0.50          | $0.25                         | 1                     |
| TinyCloud    | Compute | VM_Medium | $1.00          | $0.50                         | 2                     |
| TinyCloud    | Compute | VM_Large  | $2.00          | $1.00                         | 4                     |
| TinyCloud    | Compute | VM_XLarge | $4.00          | $2.00                         | 8                     |

The above, fictitious SKU pricing attributes show that this provider, *TinyCloud*, only has 1 service that offers 4 virtual machine SKUs with various list rates, committed rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its committed rate. Usage-based commitment discounts with commitment flexibility can fully cover any combination of 1 or more SKUs where the sum of their normalization factor equals the normalization factor of the commitment discount.

### Scenarios *without* commitment flexibility

#### Scenario #1: 100% utilization with matching resources

Purchase: 1 commitment discount purchased for 1 year (2023) for 1 VM_Large.
Usage: 1 VM_Large resource runs from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

The commitment discount covers the first charge period for 1 VM_Large resource (i.e. <my-vm-id>) resulting in a $1 amortized cost.

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
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "Hour"
    }
]
```

#### Scenario #2: 0% utilization with a non-matching resource

Purchase: 1 commitment discount purchased for 1 year (2023) for 1 VM_Large.
Usage: 1 VM_Medium resource runs from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

The VM_Large commitment discount is unused because no VM_Large resources are running. Additionally, 1 hour of on-demand usage was incurred by the running VM_Medium resource. These charges result in a $2 amortized cost.

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

### Scenarios *with* commitment flexibility

#### Scenario #1: 100% utilization with 2 VM_medium resources

Purchase: 1 commitment discount purchased for 1 year (2023) for 1 VM_XLarge with a normalization factor of 8.
Usage: 2 VM_Medium resources run from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4 for each resource.

1 commitment discount for a VM_XLarge has a normalization factor of 8, and 2 VM_Medium resources have a normalization factor of 4, each. With commitment flexibility, 1 VM_XLarge commitment discount can fully cover 2 VM_Medium resources resulting in a $2 amortized cost.

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
        "ResourceId": "<my-medium-vm-id>",
        "PricingQuantity": 1.00,
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Medium",
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
        "PricingCategory": "Committed",
        "ResourceId": "<my-medium-vm-id>",
        "PricingQuantity": 1.00,
        "BilledCost": 0.00,
        "EffectiveCost": 1.00,
        "ConsumedQuantity": 1.00,
        "ConsumedUnit": "Hour",
        "SkuId": "VM_Medium",
        "CommitmentDiscountId": "<commitment-discount-id>",
        "CommitmentDiscountQuantity": 1.00,
        "CommitmentDiscountStatus": "Used",
        "CommitmentDiscountUnit": "Normalized Hour"
    }
]
```

#### Scenario #2: 100% utilization with 1 VM_Large resource

Purchase: 1 commitment discount purchased for 1 year (2023) for 1 VM_Small with a normalization factor of 1.
Usage: 1 VM_Large resource runs from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4.

The VM_Small commitment discount was fully utilized but still only covered 25% of the VM_Large resource, so the rest of the VM incurred an on-demand cost of $1.50, and the amortized cost for this resource is $1.75.

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
