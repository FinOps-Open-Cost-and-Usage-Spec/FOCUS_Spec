# 100% utilization with commitment discount flexibility with 1 resource

## Context

For this example, fictitious provider, *TinyCloud*, offers the following SKU catalog which is used in the scenario below.

## SKU Catalog

| Service | Sku Id    | Sku Price Id                            | Sku Price Unit Price | Normalization Factor |
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

The above SKU catalog shows that this provider only has 1 service that offers 4 virtual machine SKUs at various list rates, *commitment discount* rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based [*commitment discounts*](#glossary:commitmentdiscount) with [*commitment discount flexibility*](#commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

## Scenario

* 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM_SMALL which has a normalization factor of 1.
* 1 VM_LARGE resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4.

## Outcome

* 1 recurring, purchase record exists for 1 eligible "Normalized Hour" of the no upfront, *commitment discount* and incurs a $0.50 [*BilledCost*](#billedcost).
* The VM_SMALL *commitment discount* is fully utilized within the corresponding [*charge period*](#glossary:chargeperiod), covers 25% of the VM_LARGE resource, and incurs a $0.50 [*EffectiveCost*](#effectivecost).
* The VM_LARGE resource incurs an additional, on-demand $2.25 *BilledCost* and *EffectiveCost*.

[CSV Example](/specification/data/commitment_discount_flexibility/one_hundred_percent_utilization_with_commitment_discount_flexibility_with_1_resource.csv)
