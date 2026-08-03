# Examples: Split Cost Allocation Field Mapping

> Note: The following section is informative and non-normative. It does not define requirements.

This section provides a complete field mapping showing how a data generator transforms native billing data into FOCUS [*allocated charge*](#glossary:allocated-charge) rows. It uses Aura Web's native billing export format as the input and shows the corresponding FOCUS column values for each output row, including the [Allocated*](#datasets.costandusage) columns used in this scenario and representative summable metric values.

Data generators that produce FOCUS data from Aura Web native exports (or any provider that uses a column-augmentation allocation format) should read this section alongside [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements and the worked example in [Examples: Data Generator-Calculated Split Cost Allocation](#appendix.examples:datagenerator-calculatedsplitcostallocation).

## Scenario

Acme Corp runs a shared Aura Web container host (`host-aura-prod-07`) — a single compute instance that provides capacity for multiple application workloads. For the charge period 2026-06-01 to 2026-06-02, the instance runs three consuming workloads. Aura Web's billing export records the full instance cost on a single row with allocation detail in native extension columns. In this example, the data generator splits this into four rows — one [*origin charge*](#glossary:origin-charge) row and one *allocated charge* row per consumer — with summable metrics distributed proportionally and all dimension columns preserved.

The origin charge for the period is:

* Resource: `host-aura-prod-07` (a compute instance)
* Aura Web service: "Aura Compute Engine" (fictitious equivalent: Amazon EC2)
* EffectiveCost: $240.00 (full 24-hour period at $10.00/hr, reflecting the Resource Reservation commitment discount)
* BilledCost: $0.00
* ConsumedQuantity: 24 instance-hours
* ListUnitPrice: $12.00 per instance-hour
* ContractedUnitPrice: $12.00 per instance-hour (defaults to List Unit Price — Resource Reservation is a commitment discount, which does not affect ContractedUnitPrice)

The three consuming workloads and their measured allocation ratios for the period are:

| Workload Pod              | Display Name              | Consuming Service       | vCPU-Hours | Allocation Ratio |
| :------------------------ | :------------------------ | :---------------------- | ---------: | ---------------: |
| `pod-aura-api-gateway-01` | aura-api-gateway-01       | Aura App Platform       |         60 |             0.50 |
| `pod-aura-data-ingest-01` | aura-data-ingest-01       | Aura Stream Processing  |         36 |             0.30 |
| `pod-aura-ml-train-01`    | aura-ml-train-01          | Aura ML Platform        |         24 |             0.20 |

## Native Input: Aura Web Billing Export

Aura Web's native export emits one row for the compute instance with allocation detail expressed as per-consumer extension column sets. The native format uses a column-augmentation approach: the full charge appears on a single row alongside the allocation ratios and consumer identifiers.

Key native columns used in this example:

| Native Column                         | Description                                                                                     |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- |
| `resource_id`                         | Identifier of the billed resource (the compute instance)                                        |
| `resource_name`                       | Display name of the billed resource                                                             |
| `provider_name`                       | Provider identity                                                                                |
| `product_name`                        | Provider service name                                                                           |
| `product_category`                    | Provider service category                                                                       |
| `charge_period_start`                 | Start of the charge period                                                                      |
| `charge_period_end`                   | End of the charge period                                                                        |
| `line_item_cost`                      | Full billed cost for the instance                                                               |
| `line_item_net_cost`                  | Effective cost after discounts                                                                  |
| `usage_quantity`                      | Instance-hours consumed                                                                         |
| `list_unit_price`                     | On-demand unit price                                                                            |
| `contracted_unit_price`               | Unit price after negotiated discounts (defaults to list price when none apply)                  |
| `split_resource_id_{n}`               | Identifier of the n-th consuming workload                                                       |
| `split_resource_name_{n}`             | Display name of the n-th consuming workload                                                     |
| `split_service_name_{n}`              | Service name of the n-th consuming workload                                                     |
| `split_allocation_ratio_{n}`          | Proportion of the instance cost allocated to the n-th consumer                                  |
| `split_usage_unit`                    | Unit used to measure consumer utilization (e.g., vCPU-Hours)                                   |
| `split_usage_quantity_{n}`            | Measured utilization for the n-th consumer in `split_usage_unit` units                         |
| `split_method_id`                     | Provider-assigned identifier for the allocation method                                          |

Native input row:

| Native Column                   | Value                          |
| :------------------------------ | :----------------------------- |
| `resource_id`                   | `host-aura-prod-07`            |
| `resource_name`                 | `aura-prod-07`                 |
| `provider_name`                 | `Aura Web`                     |
| `product_name`                  | `Aura Compute Engine`          |
| `product_category`              | `Compute`                      |
| `charge_period_start`           | `2026-06-01T00:00:00Z`         |
| `charge_period_end`             | `2026-06-02T00:00:00Z`         |
| `line_item_cost`                | `0.00`                         |
| `line_item_net_cost`            | `240.00`                       |
| `usage_quantity`                | `24`                           |
| `list_unit_price`               | `12.00`                        |
| `contracted_unit_price`         | `12.00`                        |
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
| `split_service_name_3`          | `Aura ML Platform`             |
| `split_allocation_ratio_3`      | `0.20`                         |
| `split_usage_quantity_3`        | `24`                           |
| `split_usage_unit`              | `vCPU-Hours`                   |
| `split_method_id`               | `aura-vcpu-proportional-v1`    |

## FOCUS Output: Four-Row Transformation

The data generator emits four FOCUS rows from this single native input row. The column-augmentation structure (all consumers on one row) is dissolved: each consumer becomes a separate *allocated charge* row, and the origin row carries the preserved instance dimensions with all summable metrics zeroed. Retaining a zeroed origin row is the representation chosen for this example; DataGeneratorCalculatedSplitCostAllocationHandling requires only that summable metrics across the *allocated charges* reconcile to the origin total, not that the origin row be retained, omitted, or zeroed in any particular way.

### Transformation Rules Applied

* **ResourceId, ResourceName, ServiceName, ServiceCategory**: copied unchanged from the native instance columns to every output row — origin and all *allocated charges*.
* **ServiceProviderName**: copied unchanged from `provider_name` to every output row — origin and all *allocated charges*.
* **ListUnitPrice, ContractedUnitPrice**: copied unchanged from the native unit price columns to every output row (non-summable metrics are preserved per DataGeneratorCalculatedSplitCostAllocationHandling). ContractedUnitPrice defaults to ListUnitPrice here because Resource Reservation is a commitment discount, not a negotiated discount, so it does not reduce ContractedUnitPrice.
* **ListCost, ContractedCost, EffectiveCost, ConsumedQuantity**: set to $0.00 / 0 on the origin row; multiplied by the consumer's allocation ratio on each *allocated charge* row. The sum across all four rows equals the pre-split origin total for each metric.
* **BilledCost**: `$0.00` on all four rows. The origin charge is fully covered by the Resource Reservation's purchase charge (not shown in this example), and each *allocated charge* inherits that covered status since it represents a portion of the same covered usage.
* **ConsumedUnit**: `"Hours"` on every row, since ConsumedQuantity (including the origin row's zeroed value) is populated on all four rows.
* **AllocatedResourceId, AllocatedResourceName, AllocatedServiceName**: null on the origin row; populated from `split_resource_id_{n}`, `split_resource_name_{n}`, and `split_service_name_{n}` on each *allocated charge* row.
* **AllocatedMethodId, AllocatedMethodDetails**: null on the origin row; set to `split_method_id` and to the consumer's allocation ratio and measured utilization, respectively, on each *allocated charge* row.
* **ChargeCategory**: `"Usage"` on all rows.

> Note: This example treats the retained, zeroed origin row as not "related to" the data generator-calculated split cost allocation for AllocatedMethodId/AllocatedMethodDetails nullability purposes, so both are left null on that row. Whether a zeroed origin row should instead carry AllocatedMethodId is an open question under task force discussion; this example will be updated to match once that question is resolved.

### Row 1 — Origin Charge

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | `provider_name`                                     |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name`                                      |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category`                                  |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id`                                       |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name`                                     |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price`                                   |
| ContractedUnitPrice     | `12.00`                                                                                        | `contracted_unit_price` — defaults to ListUnitPrice |
| ConsumedQuantity        | `0`                                                                                            | Origin zeroed — full quantity distributed below     |
| ConsumedUnit            | `"Hours"`                                                                                      | Fixed                                               |
| ListCost                | `0.00`                                                                                         | Origin zeroed — full cost distributed below         |
| ContractedCost          | `0.00`                                                                                         | Origin zeroed — full cost distributed below         |
| BilledCost              | `0.00`                                                                                         | `line_item_cost` — fully covered by Resource Reservation purchase (not shown) |
| EffectiveCost           | `0.00`                                                                                         | Origin zeroed — full cost distributed below         |
| AllocatedMethodId       | *(null)*                                                                                       | Not related to the split cost allocation (see note above) |
| AllocatedMethodDetails  | *(null)*                                                                                       | Not related to the split cost allocation (see note above) |
| AllocatedResourceId     | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedResourceName   | *(null)*                                                                                       | Not an *allocated charge*                           |
| AllocatedServiceName    | *(null)*                                                                                       | Not an *allocated charge*                           |

### Row 2 — Allocated Charge: Aura App Platform (50%)

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | `provider_name` — preserved from origin             |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `12.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `12`                                                                                           | `24 × 0.50`                                         |
| ConsumedUnit            | `"Hours"`                                                                                      | Fixed                                               |
| ListCost                | `144.00`                                                                                       | `list_unit_price` × `usage_quantity` × 0.50         |
| ContractedCost          | `144.00`                                                                                       | `contracted_unit_price` × `usage_quantity` × 0.50   |
| BilledCost              | `0.00`                                                                                         | Fully covered — inherits origin's covered status    |
| EffectiveCost           | `120.00`                                                                                       | `line_item_net_cost` × 0.50                         |
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
| ServiceProviderName     | `"Aura Web"`                                                                                   | `provider_name` — preserved from origin             |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `12.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `7.2`                                                                                          | `24 × 0.30`                                         |
| ConsumedUnit            | `"Hours"`                                                                                      | Fixed                                               |
| ListCost                | `86.40`                                                                                        | `list_unit_price` × `usage_quantity` × 0.30         |
| ContractedCost          | `86.40`                                                                                        | `contracted_unit_price` × `usage_quantity` × 0.30   |
| BilledCost              | `0.00`                                                                                         | Fully covered — inherits origin's covered status    |
| EffectiveCost           | `72.00`                                                                                        | `line_item_net_cost` × 0.30                         |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                                  | `split_method_id`                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.30,"UsageUnit":"vCPU-Hours","UsageQuantity":36}]}`           | `split_allocation_ratio_2`, `split_usage_quantity_2` |
| AllocatedResourceId     | `"pod-aura-data-ingest-01"`                                                                    | `split_resource_id_2`                               |
| AllocatedResourceName   | `"aura-data-ingest-01"`                                                                        | `split_resource_name_2`                             |
| AllocatedServiceName    | `"Aura Stream Processing"`                                                                     | `split_service_name_2`                              |

### Row 4 — Allocated Charge: Aura ML Platform (20%)

| FOCUS Column            | Value                                                                                          | Source                                              |
| :---------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                                      | Fixed                                               |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                                         | `charge_period_start`                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                                         | `charge_period_end`                                 |
| ServiceProviderName     | `"Aura Web"`                                                                                   | `provider_name` — preserved from origin             |
| ServiceName             | `"Aura Compute Engine"`                                                                        | `product_name` — preserved from origin              |
| ServiceCategory         | `"Compute"`                                                                                    | `product_category` — preserved from origin          |
| ResourceId              | `"host-aura-prod-07"`                                                                          | `resource_id` — preserved from origin               |
| ResourceName            | `"aura-prod-07"`                                                                               | `resource_name` — preserved from origin             |
| ListUnitPrice           | `12.00`                                                                                        | `list_unit_price` — preserved from origin           |
| ContractedUnitPrice     | `12.00`                                                                                        | `contracted_unit_price` — preserved from origin     |
| ConsumedQuantity        | `4.8`                                                                                          | `24 × 0.20`                                         |
| ConsumedUnit            | `"Hours"`                                                                                      | Fixed                                               |
| ListCost                | `57.60`                                                                                        | `list_unit_price` × `usage_quantity` × 0.20         |
| ContractedCost          | `57.60`                                                                                        | `contracted_unit_price` × `usage_quantity` × 0.20   |
| BilledCost              | `0.00`                                                                                         | Fully covered — inherits origin's covered status    |
| EffectiveCost           | `48.00`                                                                                        | `line_item_net_cost` × 0.20                         |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                                  | `split_method_id`                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.20,"UsageUnit":"vCPU-Hours","UsageQuantity":24}]}`           | `split_allocation_ratio_3`, `split_usage_quantity_3` |
| AllocatedResourceId     | `"pod-aura-ml-train-01"`                                                                       | `split_resource_id_3`                               |
| AllocatedResourceName   | `"aura-ml-train-01"`                                                                           | `split_resource_name_3`                             |
| AllocatedServiceName    | `"Aura ML Platform"`                                                                           | `split_service_name_3`                              |

## Metric Reconciliation

The summable metrics across the four FOCUS rows sum to the pre-split origin totals:

| Metric          | Origin Row | Row 2   | Row 3  | Row 4  | Total    | Pre-Split Origin |
| :-------------- | ---------: | ------: | -----: | -----: | -------: | ---------------: |
| ListCost        | $0.00      | $144.00 | $86.40 | $57.60 | $288.00  | $288.00 ✓        |
| ContractedCost  | $0.00      | $144.00 | $86.40 | $57.60 | $288.00  | $288.00 ✓        |
| BilledCost      | $0.00      | $0.00   | $0.00  | $0.00  | $0.00    | $0.00 ✓          |
| EffectiveCost   | $0.00      | $120.00 | $72.00 | $48.00 | $240.00  | $240.00 ✓        |
| ConsumedQuantity | 0         | 12      | 7.2    | 4.8    | 24       | 24 ✓             |

ListCost and ContractedCost are numerically identical in this scenario because ContractedUnitPrice defaults to ListUnitPrice: Resource Reservation is a commitment discount, and commitment discounts affect EffectiveCost (through amortization) but not ContractedUnitPrice, which excludes them by definition. BilledCost is $0.00 across all four rows because this usage is fully covered by the Resource Reservation's purchase charge — a *covering charge* not itself shown in this example — leaving EffectiveCost as the only metric that reflects the $240.00 amortized cost of the reservation.

Non-summable metrics (ListUnitPrice `$12.00`, ContractedUnitPrice `$12.00`, ConsumedUnit `"Hours"`) are identical across all four rows.

> Note: ListCost and ContractedCost use ConsumedQuantity in place of PricingQuantity in this scenario. Pricing Unit and Consumed Unit are both instance-hours here, so the two quantities are numerically equivalent; a data generator whose Pricing Unit differs from its Consumed Unit would compute these metrics from PricingQuantity instead.
