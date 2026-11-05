# Examples: Data Generator-Calculated Split Cost Allocation

This section demonstrates how [AllocatedServiceName](#col) enables consumer [service](#term) identification on [allocated charges](#term) when a data generator preserves origin dimensions in accordance with [DataGeneratorCalculatedSplitCostAllocationHandling](#attr) requirements.

## Origin Preservation and the Consumer Service Identity Gap

[DataGeneratorCalculatedSplitCostAllocationHandling](#attr) requires that the origin [ServiceName](#col) and [ServiceCategory](#col) are preserved on all [allocated charge](#term) rows so that the dataset reconciles to the invoice on the origin [service](#term). This means a practitioner can always filter by origin [ServiceName](#col) to obtain the correct invoice-reconciled total.

The side-effect of this requirement is that the consuming [service](#term) identity is not expressed in [ServiceName](#col) on [allocated charge](#term) rows. Without [AllocatedServiceName](#col), the consuming [service](#term) can only be inferred from [AllocatedResourceId](#col) through an external lookup maintained by the practitioner.

[AllocatedServiceName](#col) closes this gap: the data generator populates it with the consuming [service](#term) display name on each [allocated charge](#term) row, leaving the origin [ServiceName](#col) intact.

## Shared Infrastructure Split Across Multiple Consumer Services

Acme Corp runs a shared Aura Web container cluster (`cluster-shared-01`) for a single charge period (2026-04-01). The cluster hosts workloads belonging to three distinct consuming [services](#term). The data generator is configured to split the cluster host cost across the consuming workloads by measured vCPU-hour consumption.

The origin charge [EffectiveCost](#col) for the period is $100.00. The data generator measures consumer utilization as:

* `pod-orders-01` (Orders Service): 40 vCPU-hours (40%)
* `pod-scoring-01` (ML Inference Service): 35 vCPU-hours (35%)
* `pod-frontend-01` (Web Frontend Service): 25 vCPU-hours (25%)

The data generator emits one origin charge row and three [allocated charge](#term) rows. Per [DataGeneratorCalculatedSplitCostAllocationHandling](#attr), the origin dimensions ([ServiceName](#col), [ServiceCategory](#col), [ResourceId](#col)) are preserved across all four rows. [AllocatedServiceName](#col) identifies the consuming [service](#term) on each [allocated charge](#term) row.

Rows for the period:

1. **Origin charge** (Row 1): The origin charge row carrying the preserved origin dimensions. [AllocatedResourceId](#col) is null, [AllocatedServiceName](#col) is null. [ServiceName](#col) is "Aura Container Runtime", [ServiceCategory](#col) is ["Compute"](#val:CostAndUsage.ServiceCategory). [EffectiveCost](#col) is $0.00, since the full $100.00 host cost is sliced across the three allocated charge rows below.
2. **Allocated charge — Orders Service** (Row 2): 40% of the origin charge allocated to `pod-orders-01`. [ServiceName](#col) remains "Aura Container Runtime" (preserved from the origin charge). [AllocatedResourceId](#col) is `pod-orders-01`, [AllocatedServiceName](#col) is "Aura Order Management". [EffectiveCost](#col) is $40.00.
3. **Allocated charge — ML Inference Service** (Row 3): 35% allocated to `pod-scoring-01`. [ServiceName](#col) remains "Aura Container Runtime". [AllocatedResourceId](#col) is `pod-scoring-01`, [AllocatedServiceName](#col) is "Aura ML Inference". [EffectiveCost](#col) is $35.00.
4. **Allocated charge — Web Frontend Service** (Row 4): 25% allocated to `pod-frontend-01`. [ServiceName](#col) remains "Aura Container Runtime". [AllocatedResourceId](#col) is `pod-frontend-01`, [AllocatedServiceName](#col) is "Aura Edge Delivery". [EffectiveCost](#col) is $25.00.

The three allocated charge [EffectiveCost](#col) values sum to $40.00 + $35.00 + $25.00 = $100.00, matching the origin charge total, which satisfies the [DataGeneratorCalculatedSplitCostAllocationHandling](#attr) requirement that a summable metric sums to the origin charge across the allocated charges. In this example, the data generator represents that split by reducing the origin charge row's [EffectiveCost](#col) to $0.00 and moving the full amount to the allocated charge rows, with no separate offsetting rows. [DataGeneratorCalculatedSplitCostAllocationHandling](#attr) does not itself prescribe whether the origin charge row is zeroed, omitted, or paired with a separate offsetting row, only that the allocated charges sum to the origin total.

| Row | ResourceId | ServiceName | ServiceCategory | AllocatedResourceId | AllocatedServiceName | EffectiveCost |
| :-- | :--- | :--- | :--- | :--- | :--- | ---: |
| 1 | `cluster-shared-01` | Aura Container Runtime | Compute | *(null)* | *(null)* | $0.00 |
| 2 | `cluster-shared-01` | Aura Container Runtime | Compute | `pod-orders-01` | Aura Order Management | $40.00 |
| 3 | `cluster-shared-01` | Aura Container Runtime | Compute | `pod-scoring-01` | Aura ML Inference | $35.00 |
| 4 | `cluster-shared-01` | Aura Container Runtime | Compute | `pod-frontend-01` | Aura Edge Delivery | $25.00 |

## Analysis Queries Enabled by Allocated Service Name

Practitioners can now answer two distinct questions against the same dataset without external lookups:

* **Origin-side analysis** (grouped by [ServiceName](#col)): The full $100.00 remains attributed to "Aura Container Runtime", preserving the [origin charge](#term) perspective needed for invoice reconciliation and platform team cost tracking.
* **Consumer-side analysis** (grouped by [AllocatedServiceName](#col), filtered to rows where [AllocatedResourceId](#col) is not null): $40.00 is attributed to "Aura Order Management", $35.00 to "Aura ML Inference", and $25.00 to "Aura Edge Delivery", enabling showback and chargeback by the [service](#term) that consumed the shared resource.

Without [AllocatedServiceName](#col), the consuming [service](#term) is inferable only by joining [AllocatedResourceId](#col) to an external pod-to-service mapping maintained outside the dataset.
