# 0% utilization without commitment discount flexibility

## Context

For this example, fictitious service provider, _TinyCloud_, offers the following SKU catalog which is used in the scenario below.

## SKU Catalog

| Service | Sku Id    | Sku Price Id                            | Sku Price Unit Price | Normalization Factor |
| ------- | --------- | --------------------------------------- | -------------------- | -------------------- |
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

The above SKU Catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list unit prices, [_commitment discount_](#glossary:commitmentdiscount) unit prices, and normalization factors. Each SKU's normalization factor classifies its relative size to its _commitment discount_ unit price. Usage-based _commitment discounts_ with [_commitment discount flexibility_](#appendix.examples:commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the _commitment discount_.

## Scenario

- 1 no upfront _commitment discount_ is purchased for 1 year (2023) for 1 VM_LARGE.
- 1 VM_MEDIUM resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

## Outcome

- 1 recurring, purchase record exists for 1 eligible "Hour" of the no upfront, _commitment discount_ and incurs a $1.50 [_BilledCost_](#datasets.costandusage.billedcost).
- The VM_LARGE _commitment discount_ is unused for the corresponding [_charge period_](#glossary:chargeperiod) because no VM_LARGE resources are running and incurs a $1.50 [_EffectiveCost_](#datasets.costandusage.effectivecost).
- 1 hour of on-demand usage is incurred by the VM_MEDIUM resource and incurs a $2.00 _BilledCost_ and _EffectiveCost_.

[CSV Example](/specification/data/commitment_discount_flexibility/zero_percent_utilization_without_commitment_discount_flexibility.csv)
