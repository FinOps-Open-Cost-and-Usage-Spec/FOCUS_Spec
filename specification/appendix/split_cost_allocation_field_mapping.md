# Examples: Split Cost Allocation — Producer Field Mapping

> Note: The following section is informative and non-normative. It does not define requirements.

This section provides a complete producer-side field mapping showing how a data generator transforms native billing data into FOCUS [*allocated charge*](#glossary:allocated-charge) rows. It uses Aura Web's native billing export format as the input and shows the corresponding FOCUS column values for each output row, including all [Allocated*](#datasets.costandusage) columns and representative summable metric values.

Practitioners who generate FOCUS data from Aura Web native exports (or any provider that uses a column-augmentation allocation format) should read this section alongside [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements and the worked example in [Examples: Data Generator-Calculated Split Cost Allocation](#appendix.examples:datageneratorcalculatedsplitcostallocation).

## Scenario

Acme Corp runs a shared Aura Web container host (`host-aura-prod-07`) — a single compute instance that provides capacity for multiple application workloads. For the charge period 2026-06-01 to 2026-06-02, the instance runs three consuming workloads. Aura Web's billing export records the full instance cost on a single row with allocation detail in native extension columns. The FOCUS output must split this into four rows — one [*origin charge*](#glossary:origin-charge) row and one *allocated charge* row per consumer — with summable metrics distributed proportionally and all dimension columns preserved.

The origin charge for the period is:

* Resource: `host-aura-prod-07` (a compute instance)
* Aura Web service: "Aura Compute Engine" (fictitious equivalent: Amazon EC2)
* EffectiveCost: $240.00 (full 24-hour period at $10.00/hr)
* BilledCost: $240.00
* ConsumedQuantity: 24 instance-hours
* ListUnitPrice: $12.00 per instance-hour
* ContractedUnitPrice: $10.00 per instance-hour (Resource Reservation discount applied)

The three consuming workloads and their measured allocation ratios for the period are:

| Workload Pod              | Display Name              | Consuming Service       | vCPU-Hours | Allocation Ratio |
| :------------------------ | :------------------------ | :---------------------- | ---------: | ---------------: |
| `pod-aura-api-gateway-01` | aura-api-gateway-01       | Aura App Platform       |         60 |             0.50 |
| `pod-aura-data-ingest-01` | aura-data-ingest-01       | Aura Stream Processing  |         36 |             0.30 |
| `pod-aura-ml-train-01`    | aura-ml-train-01          | LatticeScale ML Runtime |         24 |             0.20 |

## Native Input: Aura Web Billing Export

Aura Web's native export emits one row for the compute instance with allocation detail expressed as per-consumer extension column sets. The native format uses a column-augmentation approach: the full charge appears on a single row alongside the allocation ratios and consumer identifiers.

Key native columns used in this example:

| Native Column                         | Description                                                                                     |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- |
| `resource_id`                         | Identifier of the billed resource (the compute instance)                                        |
| `resource_name`                       | Display name of the billed resource                                                             |
| `product_name`                        | Provider service name                                                                           |
| `product_category`                    | Provider service category                                                                       |
| `charge_period_start`                 | Start of the charge period                                                                      |
| `charge_period_end`                   | End of the charge period                                                                        |
| `line_item_cost`                      | Full billed cost for the instance                                                               |
| `line_item_net_cost`                  | Effective cost after discounts                                                                  |
| `usage_quantity`                      | Instance-hours consumed                                                                         |
| `list_unit_price`                     | On-demand unit price                                                                            |
| `contracted_unit_price`               | Discounted unit price after reservation                                                         |
| `split_resource_id_{n}`               | Identifier of the n-th consuming workload                                                       |
| `split_resource_name_{n}`             | Display name of the n-th consuming workload                                                     |
| `split_service_name_{n}`              | Service name of the n-th consuming workload                                                     |
| `split_allocation_ratio_{n}`          | Proportion of the instance cost allocated to the n-th consumer                                  |
| `split_usage_unit`                    | Unit used to measure consumer utilization (e.g., vCPU-Hours)                                   |
| `split_usage_quantity_{n}`            | Measured utilization for the n-th consumer in `split_usage_unit` units                         |
| `split_method_id`                     | Provider-assigned identifier for the allocation method                                          |

Native input row:

| native column                   | value                          |
| :------------------------------ | :----------------------------- |
| `resource_id`                   | `host-aura-prod-07`            |
| `resource_name`                 | `aura-prod-07`                 |
| `product_name`                  | `Aura Compute Engine`          |
| `product_category`              | `Compute`                      |
| `charge_period_start`           | `2026-06-01T00:00:00Z`         |
| `charge_period_end`             | `2026-06-02T00:00:00Z`         |
| `line_item_cost`                | `288.00`                       |
| `line_item_net_cost`            | `240.00`                       |
| `usage_quantity`                | `24`                           |
| `list_unit_price`               | `12.00`                        |
| `contracted_unit_price`         | `10.00`                        |
| `split_resource_id_1`           | `pod-aura-api-gateway-01`      |
| `split_resource_name_1`         | `aura-api-gateway-01`          |
| `split_service_name_1`          | `Aura App Platform`            |
| `split_allocation_ratio_1`      | `0.50`                         |
| `split_usage_quantity_1`        | `60`                           |
| `split_resource_id_2`           | `pod-aura-data-ingest-01`      |
| `split_resource_name_2`         | `aura-data-ingest-01`          |
| `split_service_name_2`          | `Aura Stream Processing`       |
| `split_allocation_ratio_2`      | `0.30`                         |
| `split_usage_quantity_2`        | `36`                           |
| `split_resource_id_3`           | `pod-aura-ml-train-01`         |
| `split_resource_name_3`         | `aura-ml-train-01`             |
| `split_service_name_3`          | `LatticeScale ML Runtime`      |
| `split_allocation_ratio_3`      | `0.20`                         |
| `split_usage_quantity_3`        | `24`                           |
| `split_usage_unit`              | `vCPU-Hours`                   |
| `split_method_id`               | `aura-vcpu-proportional-v1`    |

## FOCUS Output: Four-Row Transformation

The data generator emits four FOCUS rows from this single native input row. The column-augmentation structure (all consumers on one row) is dissolved: each consumer becomes a separate *allocated charge* row, and the origin row carries the preserved instance dimensions with all summable metrics zeroed.

### Transformation Rules Applied

* **ResourceId, ResourceName, ServiceName, ServiceCategory, ServiceProviderName**: copied unchanged from the native instance columns to every output row — origin and all *allocated charges*.
* **ListUnitPrice, ContractedUnitPrice**: copied unchanged from the native unit price columns to every output row (non-summable metrics are preserved per DataGeneratorCalculatedSplitCostAllocationHandling).
* **EffectiveCost, BilledCost, ConsumedQuantity**: set to $0.00 / 0 on the origin row; multiplied by the consumer's allocation ratio on each *allocated charge* row. The sum across all four rows equals the pre-split origin total.
* **AllocatedResourceId, AllocatedResourceName, AllocatedServiceName**: null on the origin row; populated from `split_resource_id_{n}`, `split_resource_name_{n}`, and `split_service_name_{n}` on each *allocated charge* row.
* **AllocatedMethodId**: null on the origin row; set to `split_method_id` on each *allocated charge* row.
* **AllocatedMethodDetails**: null on the origin row; populated with the consumer's allocation ratio and measured utilization on each *allocated charge* row.
* **ChargeCategory**: `"Usage"` on all rows.

### Row 1 — Origin Charge

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | Provider identity                                   |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name`                                      |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category`                                  |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id`                                       |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name`                                     |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price`                                   |
| ContractedUnitPrice     | `10.00`                                                                                        | `contracted_unit_price`                             |
| ConsumedQuantity        | `0`                                                                                            | Origin zeroed — full quantity distributed below     |
| BilledCost              | `0.00`                                                                                         | Origin zeroed — full cost distributed below         |
| EffectiveCost           | `0.00`                                                                                         | Origin zeroed — full cost distributed below         |
| AllocatedMethodId       | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedMethodDetails  | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedResourceId     | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedResourceName   | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedServiceName    | *(null)*                                                                                       | Not an *allocated charge*                           |

### Row 2 — Allocated Charge: Aura App Platform (50%)

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | Provider identity                                   |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `10.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `12`                                                                                           | `24 × 0.50`                                         |
| BilledCost              | `144.00`                                                                                       | `288.00 × 0.50`                                     |
| EffectiveCost           | `120.00`                                                                                       | `240.00 × 0.50`                                     |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                                  | `split_method_id`                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.50,"UsageUnit":"vCPU-Hours","UsageQuantity":60}]}`           | `split_allocation_ratio_1`, `split_usage_quantity_1` |
| AllocatedResourceId     | `"pod-aura-api-gateway-01"`                                                                    | `split_resource_id_1`                               |
| AllocatedResourceName   | `"aura-api-gateway-01"`                                                                        | `split_resource_name_1`                             |
| AllocatedServiceName    | `"Aura App Platform"`                                                                          | `split_service_name_1`                              |

### Row 3 — Allocated Charge: Aura Stream Processing (30%)

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | Provider identity                                   |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `10.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `7.2`                                                                                          | `24 × 0.30`                                         |
| BilledCost              | `86.40`                                                                                        | `288.00 × 0.30`                                     |
| EffectiveCost           | `72.00`                                                                                        | `240.00 × 0.30`                                     |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                                  | `split_method_id`                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.30,"UsageUnit":"vCPU-Hours","UsageQuantity":36}]}`           | `split_allocation_ratio_2`, `split_usage_quantity_2` |
| AllocatedResourceId     | `"pod-aura-data-ingest-01"`                                                                    | `split_resource_id_2`                               |
| AllocatedResourceName   | `"aura-data-ingest-01"`                                                                        | `split_resource_name_2`                             |
| AllocatedServiceName    | `"Aura Stream Processing"`                                                                     | `split_service_name_2`                              |

### Row 4 — Allocated Charge: LatticeScale ML Runtime (20%)

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | Provider identity                                   |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `10.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `4.8`                                                                                          | `24 × 0.20`                                         |
| BilledCost              | `57.60`                                                                                        | `288.00 × 0.20`                                     |
| EffectiveCost           | `48.00`                                                                                        | `240.00 × 0.20`                                     |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                                  | `split_method_id`                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.20,"UsageUnit":"vCPU-Hours","UsageQuantity":24}]}`           | `split_allocation_ratio_3`, `split_usage_quantity_3` |
| AllocatedResourceId     | `"pod-aura-ml-train-01"`                                                                       | `split_resource_id_3`                               |
| AllocatedResourceName   | `"aura-ml-train-01"`                                                                           | `split_resource_name_3`                             |
| AllocatedServiceName    | `"LatticeScale ML Runtime"`                                                                    | `split_service_name_3`                              |

## Metric Reconciliation

The summable metrics across the four FOCUS rows sum to the pre-split origin totals:

| Metric          | Origin Row | Row 2   | Row 3  | Row 4  | Total    | Pre-Split Origin |
| :-------------- | ---------: | ------: | -----: | -----: | -------: | ---------------: |
| EffectiveCost   | $0.00      | $120.00 | $72.00 | $48.00 | $240.00  | $240.00 ✓        |
| BilledCost      | $0.00      | $144.00 | $86.40 | $57.60 | $288.00  | $288.00 ✓        |
| ConsumedQuantity | 0         | 12      | 7.2    | 4.8    | 24       | 24 ✓             |

Non-summable metrics (ListUnitPrice `$12.00`, ContractedUnitPrice `$10.00`) are identical across all four rows.

## Notes on Cross-Provider Consumers

Row 4's AllocatedServiceName is `"LatticeScale ML Runtime"` — a service from a different provider (LatticeScale, the fictitious GCP equivalent) than the host compute instance (Aura Web). The `AllocatedServiceName` column carries the consuming *service* display name regardless of whether that service is operated by the same provider as the origin resource. The origin row's ServiceProviderName and ServiceName remain `"Aura Web"` and `"Aura Compute Engine"` on all four rows, preserving the invoice-reconcilable origin view. Practitioners querying for Aura Web compute cost see the correct total from all four rows via `SUM(EffectiveCost) WHERE ServiceName = 'Aura Compute Engine'`; practitioners querying for LatticeScale ML cost see Row 4 via `SUM(EffectiveCost) WHERE AllocatedServiceName = 'LatticeScale ML Runtime'`.
