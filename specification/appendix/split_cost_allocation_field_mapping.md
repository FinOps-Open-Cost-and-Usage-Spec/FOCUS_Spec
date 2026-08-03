# Examples: Split Cost Allocation Field Mapping

> Note: The following section is informative and non-normative. It does not define requirements.

DataGeneratorCalculatedSplitCostAllocationHandling defines the requirements for split cost allocation, but does not show how a data generator gets there from its own native billing data. This is a non-obvious step for data generators whose native export uses a column-augmentation format — a single row carrying per-consumer allocation detail in extension columns, rather than a separate row per consumer. Without a worked example, data generators using this format have had to reverse-engineer the transformation independently. This section closes that gap with a worked example showing how such a native input transforms into FOCUS [*allocated charge*](#glossary:allocated-charge) rows. It shows the resulting [*origin charge*](#glossary:origin-charge) and *allocated charge* rows, including the [Allocated*](#datasets.costandusage) columns used in this scenario, and verifies that summable metrics reconcile across the split.

Data generators that produce FOCUS data from a column-augmentation allocation format should read this section alongside [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements and the worked example in [Examples: Data Generator-Calculated Split Cost Allocation](#appendix.examples:datagenerator-calculatedsplitcostallocation).

## Scenario

Acme Corp runs a shared Aura Web container host (`host-aura-prod-07`) — a single compute instance that provides capacity for multiple application workloads. For the charge period 2026-06-01 to 2026-06-02, the instance runs three consuming workloads. Aura Web's billing export uses a column-augmentation format: the full instance charge appears on a single row, with per-consumer allocation detail — consumer identifiers, service names, allocation ratios, and measured utilization — expressed as extension columns on that same row. In this example, the data generator splits this into four rows — one *origin charge* row and one *allocated charge* row per consumer — with summable metrics distributed proportionally and all dimension columns preserved.

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

## FOCUS Output: Four-Row Transformation

The data generator emits four FOCUS rows for this charge period. The column-augmentation structure (all consumers on one native row) is dissolved: each consumer becomes a separate *allocated charge* row, and the origin row carries the preserved instance dimensions with all summable metrics zeroed. Retaining a zeroed origin row is the representation chosen for this example; DataGeneratorCalculatedSplitCostAllocationHandling requires only that summable metrics across the *allocated charges* reconcile to the origin total, not that the origin row be retained, omitted, or zeroed in any particular way.

### Column Interactions

* **ResourceId, ResourceName, ServiceName, ServiceCategory, ServiceProviderName**: preserved unchanged on every output row — origin and all *allocated charges* — since these dimensions describe the shared instance, not the individual consumer.
* **ListUnitPrice, ContractedUnitPrice**: preserved unchanged on every output row (non-summable metrics are preserved per DataGeneratorCalculatedSplitCostAllocationHandling). ContractedUnitPrice defaults to ListUnitPrice here because Resource Reservation is a commitment discount, not a negotiated discount, so it does not reduce ContractedUnitPrice.
* **ListCost, ContractedCost, EffectiveCost, ConsumedQuantity**: zeroed on the origin row; distributed across the three *allocated charge* rows in proportion to each consumer's allocation ratio. The sum across all four rows equals the pre-split origin total for each metric.
* **BilledCost**: `$0.00` on all four rows. The origin charge is fully covered by the Resource Reservation's purchase charge (not shown in this example), and each *allocated charge* inherits that covered status since it represents a portion of the same covered usage.
* **ConsumedUnit**: `"Hours"` on every row, since ConsumedQuantity (including the origin row's zeroed value) is populated on all four rows.
* **AllocatedResourceId, AllocatedResourceName, AllocatedServiceName**: null on the origin row, since no *allocation* was made *to* the origin row itself; populated with each consumer's identifier, display name, and service name on the corresponding *allocated charge* row.
* **AllocatedMethodId**: set to the allocation method identifier on every row, including the origin row — the origin row is *related to* the data generator-calculated split cost allocation even though it is not itself an *allocated charge*.
* **AllocatedMethodDetails**: present (non-null) on every row. On the origin row, `Elements` is an empty array, since there is no allocated portion to describe on that row; on each *allocated charge* row, it carries that consumer's allocation ratio and measured utilization.
* **ChargeCategory**: `"Usage"` on all rows.

> Note: AllocatedMethodId's nullability is keyed on a charge being "related to" a data generator-calculated split cost allocation, not on being an *allocated charge* itself. This example treats the origin row as related (it is part of the same split operation, even though nothing was allocated to it) and therefore populates AllocatedMethodId on it — consistent with the "Find Total Unallocated Split Costs by ResourceId" query in Data Generator-Calculated Split Cost Allocation, whose `AllocatedMethodId IS NOT NULL AND AllocatedResourceId IS NULL` predicate only returns rows under this reading. This question is tracked for the specification text itself in issue #2578.

### Origin Charge Row Details

| Column                 | Value                                                                                | Explanation                                                      |
| :---------------------- | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------ |
| ChargeCategory          | `"Usage"`                                                                            | Fixed                                                             |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                               | Charge period start                                               |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                               | Charge period end                                                 |
| ServiceProviderName     | `"Aura Web"`                                                                         | Provider identity                                                 |
| ServiceName             | `"Aura Compute Engine"`                                                              | Service billed                                                    |
| ServiceCategory         | `"Compute"`                                                                          | Service category                                                  |
| ResourceId              | `"host-aura-prod-07"`                                                                | Identifier of the shared instance                                 |
| ResourceName            | `"aura-prod-07"`                                                                     | Display name of the shared instance                                |
| ListUnitPrice           | `12.00`                                                                              | On-demand unit price                                              |
| ContractedUnitPrice     | `12.00`                                                                              | Defaults to List Unit Price — no negotiated discount applies       |
| ConsumedQuantity        | `0`                                                                                  | Zeroed — full quantity distributed across allocated charge rows    |
| ConsumedUnit            | `"Hours"`                                                                            | Fixed                                                             |
| ListCost                | `0.00`                                                                               | Zeroed — full cost distributed across allocated charge rows        |
| ContractedCost          | `0.00`                                                                               | Zeroed — full cost distributed across allocated charge rows        |
| BilledCost              | `0.00`                                                                               | Fully covered by the Resource Reservation purchase (not shown)     |
| EffectiveCost           | `0.00`                                                                               | Zeroed — full cost distributed across allocated charge rows        |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                        | Related to the split cost allocation (see note above)               |
| AllocatedMethodDetails  | `{"Elements":[]}`                                                                    | Related to the split, but no allocated portion to describe here     |
| AllocatedResourceId     | *(null)*                                                                             | Not an *allocated charge*                                          |
| AllocatedResourceName   | *(null)*                                                                             | Not an *allocated charge*                                          |
| AllocatedServiceName    | *(null)*                                                                             | Not an *allocated charge*                                          |

### Allocated Charge Row Details: Aura App Platform (50%)

| Column                 | Value                                                                                | Explanation                                                  |
| :---------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                            | Fixed                                                         |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                               | Charge period start                                           |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                               | Charge period end                                              |
| ServiceProviderName     | `"Aura Web"`                                                                         | Preserved from the origin charge                               |
| ServiceName             | `"Aura Compute Engine"`                                                              | Preserved from the origin charge                               |
| ServiceCategory         | `"Compute"`                                                                          | Preserved from the origin charge                               |
| ResourceId              | `"host-aura-prod-07"`                                                                | Preserved from the origin charge                               |
| ResourceName            | `"aura-prod-07"`                                                                     | Preserved from the origin charge                               |
| ListUnitPrice           | `12.00`                                                                              | Preserved from the origin charge                               |
| ContractedUnitPrice     | `12.00`                                                                              | Preserved from the origin charge                               |
| ConsumedQuantity        | `12`                                                                                 | 50% of the origin's 24 instance-hours                          |
| ConsumedUnit            | `"Hours"`                                                                            | Fixed                                                         |
| ListCost                | `144.00`                                                                             | 50% of the origin's $288.00 pre-split ListCost                 |
| ContractedCost          | `144.00`                                                                             | 50% of the origin's $288.00 pre-split ContractedCost            |
| BilledCost              | `0.00`                                                                               | Fully covered — inherits the origin's covered status            |
| EffectiveCost           | `120.00`                                                                             | 50% of the origin's $240.00 pre-split EffectiveCost             |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                        | Allocation method identifier                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.50,"UsageUnit":"vCPU-Hours","UsageQuantity":60}]}` | Allocation ratio and measured utilization for this consumer    |
| AllocatedResourceId     | `"pod-aura-api-gateway-01"`                                                          | Consumer identifier                                             |
| AllocatedResourceName   | `"aura-api-gateway-01"`                                                              | Consumer display name                                           |
| AllocatedServiceName    | `"Aura App Platform"`                                                                | Consuming service                                               |

### Allocated Charge Row Details: Aura Stream Processing (30%)

| Column                 | Value                                                                                | Explanation                                                  |
| :---------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                            | Fixed                                                         |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                               | Charge period start                                           |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                               | Charge period end                                              |
| ServiceProviderName     | `"Aura Web"`                                                                         | Preserved from the origin charge                               |
| ServiceName             | `"Aura Compute Engine"`                                                              | Preserved from the origin charge                               |
| ServiceCategory         | `"Compute"`                                                                          | Preserved from the origin charge                               |
| ResourceId              | `"host-aura-prod-07"`                                                                | Preserved from the origin charge                               |
| ResourceName            | `"aura-prod-07"`                                                                     | Preserved from the origin charge                               |
| ListUnitPrice           | `12.00`                                                                              | Preserved from the origin charge                               |
| ContractedUnitPrice     | `12.00`                                                                              | Preserved from the origin charge                               |
| ConsumedQuantity        | `7.2`                                                                                | 30% of the origin's 24 instance-hours                          |
| ConsumedUnit            | `"Hours"`                                                                            | Fixed                                                         |
| ListCost                | `86.40`                                                                              | 30% of the origin's $288.00 pre-split ListCost                 |
| ContractedCost          | `86.40`                                                                              | 30% of the origin's $288.00 pre-split ContractedCost            |
| BilledCost              | `0.00`                                                                               | Fully covered — inherits the origin's covered status            |
| EffectiveCost           | `72.00`                                                                              | 30% of the origin's $240.00 pre-split EffectiveCost             |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                        | Allocation method identifier                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.30,"UsageUnit":"vCPU-Hours","UsageQuantity":36}]}` | Allocation ratio and measured utilization for this consumer    |
| AllocatedResourceId     | `"pod-aura-data-ingest-01"`                                                          | Consumer identifier                                             |
| AllocatedResourceName   | `"aura-data-ingest-01"`                                                              | Consumer display name                                           |
| AllocatedServiceName    | `"Aura Stream Processing"`                                                           | Consuming service                                               |

### Allocated Charge Row Details: Aura ML Platform (20%)

| Column                 | Value                                                                                | Explanation                                                  |
| :---------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| ChargeCategory          | `"Usage"`                                                                            | Fixed                                                         |
| ChargePeriodStart       | `2026-06-01T00:00:00Z`                                                               | Charge period start                                           |
| ChargePeriodEnd         | `2026-06-02T00:00:00Z`                                                               | Charge period end                                              |
| ServiceProviderName     | `"Aura Web"`                                                                         | Preserved from the origin charge                               |
| ServiceName             | `"Aura Compute Engine"`                                                              | Preserved from the origin charge                               |
| ServiceCategory         | `"Compute"`                                                                          | Preserved from the origin charge                               |
| ResourceId              | `"host-aura-prod-07"`                                                                | Preserved from the origin charge                               |
| ResourceName            | `"aura-prod-07"`                                                                     | Preserved from the origin charge                               |
| ListUnitPrice           | `12.00`                                                                              | Preserved from the origin charge                               |
| ContractedUnitPrice     | `12.00`                                                                              | Preserved from the origin charge                               |
| ConsumedQuantity        | `4.8`                                                                                | 20% of the origin's 24 instance-hours                          |
| ConsumedUnit            | `"Hours"`                                                                            | Fixed                                                         |
| ListCost                | `57.60`                                                                              | 20% of the origin's $288.00 pre-split ListCost                 |
| ContractedCost          | `57.60`                                                                              | 20% of the origin's $288.00 pre-split ContractedCost            |
| BilledCost              | `0.00`                                                                               | Fully covered — inherits the origin's covered status            |
| EffectiveCost           | `48.00`                                                                              | 20% of the origin's $240.00 pre-split EffectiveCost             |
| AllocatedMethodId       | `"aura-vcpu-proportional-v1"`                                                        | Allocation method identifier                                   |
| AllocatedMethodDetails  | `{"Elements":[{"AllocatedRatio":0.20,"UsageUnit":"vCPU-Hours","UsageQuantity":24}]}` | Allocation ratio and measured utilization for this consumer    |
| AllocatedResourceId     | `"pod-aura-ml-train-01"`                                                             | Consumer identifier                                             |
| AllocatedResourceName   | `"aura-ml-train-01"`                                                                 | Consumer display name                                           |
| AllocatedServiceName    | `"Aura ML Platform"`                                                                 | Consuming service                                               |

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
