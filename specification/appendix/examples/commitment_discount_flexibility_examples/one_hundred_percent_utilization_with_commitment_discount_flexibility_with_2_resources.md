# 100% utilization with commitment discount flexibility with 2 resources

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

The above SKU Catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list rates, _commitment discount_ rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its _commitment discount_ rate. Usage-based [_commitment discounts_](#glossary:commitmentdiscount) with [_commitment discount flexibility_](#appendix.examples:commitmentdiscountflexibility) can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the _commitment discount_.

## Scenario

- 1 no upfront _commitment discount_ is purchased for 1 year (2023) for 1 VM_XLARGE which has a normalization factor of 8.
- 2 VM_MEDIUM resources run for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4 for each.

## Outcome

- 1 recurring, purchase record exists for 1 eligible "Normalized Hour" for a no upfront, _commitment discount_ and incurs a $2.00 [_BilledCost_](#datasets.costandusage.billedcost).
- With _commitment discount flexibility_, 1 _commitment discount_ for a VM_XLARGE covers 2 VM_MEDIUM resources within the corresponding [_charge period_](#glossary:chargeperiod) and incurs a $2.00 total [_EffectiveCost_](#datasets.costandusage.effectivecost).
  - 1 _commitment discount_ with a normalization factor of 8 covers 2 resources with normalization factors of 4 (i.e 4 + 4 = 8).

[CSV Example](/specification/data/commitment_discount_flexibility/one_hundred_percent_utilization_with_commitment_discount_flexibility_with_2_resources.csv)
