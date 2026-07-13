# Examples: Data Generator-Calculated Split Cost Allocation

> Note: The following section is informative and non-normative. It does not define requirements.

This section demonstrates how [AllocatedServiceName](#datasets.costandusage.allocatedservicename) enables consumer *service* identification on [*allocated charges*](#glossary:allocated-charge) when a data generator preserves origin dimensions in accordance with [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements.

## Origin Preservation and the Consumer Service Identity Gap

DataGeneratorCalculatedSplitCostAllocationHandling requires that the origin [ServiceName](#datasets.costandusage.servicename) and [ServiceCategory](#datasets.costandusage.servicecategory) are preserved on all *allocated charge* rows so that the dataset reconciles to the invoice on the origin *service*. This means a practitioner can always filter by origin ServiceName to obtain the correct invoice-reconciled total.

The side-effect of this requirement is that the consuming *service* identity is not expressed in ServiceName on *allocated charge* rows. Without AllocatedServiceName, the consuming *service* can only be inferred from [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) through an external lookup maintained by the practitioner.

AllocatedServiceName closes this gap: the data generator populates it with the consuming *service* display name on each *allocated charge* row, leaving the origin ServiceName intact.

## Shared Infrastructure Split Across Multiple Consumer Services

Acme Corp runs a shared Aura Web container cluster (`cluster-aura-shared-01`) for a single charge period (2026-04-01). The cluster hosts workloads belonging to three distinct consuming *services*. The data generator is configured to split the cluster host cost across the consuming workloads by measured vCPU-hour consumption.

The origin charge EffectiveCost for the period is $100.00. The data generator measures consumer utilization as:

* `pod-aura-orders-01` (Orders Service): 40 vCPU-hours (40%)
* `pod-aura-scoring-01` (ML Inference Service): 35 vCPU-hours (35%)
* `pod-aura-frontend-01` (Web Frontend Service): 25 vCPU-hours (25%)

The data generator emits one origin charge row and three *allocated charge* rows. Per DataGeneratorCalculatedSplitCostAllocationHandling, the origin dimensions (ServiceName, ServiceCategory, ResourceId) are preserved across all four rows. AllocatedServiceName identifies the consuming *service* on each *allocated charge* row.

Rows for the period:

1. **Origin charge** (Row 1): The origin charge row carrying the preserved origin dimensions. AllocatedResourceId is null, AllocatedServiceName is null. ServiceName is "Aura Container Runtime", ServiceCategory is "Compute". EffectiveCost is $0.00, since the full $100.00 host cost is sliced across the three allocated charge rows below.
2. **Allocated charge — Orders Service** (Row 2): 40% of the origin charge allocated to `pod-aura-orders-01`. ServiceName remains "Aura Container Runtime" (preserved from the origin charge). AllocatedResourceId is `pod-aura-orders-01`, AllocatedServiceName is "Aura Order Management". EffectiveCost is $40.00.
3. **Allocated charge — ML Inference Service** (Row 3): 35% allocated to `pod-aura-scoring-01`. ServiceName remains "Aura Container Runtime". AllocatedResourceId is `pod-aura-scoring-01`, AllocatedServiceName is "Aura ML Inference". EffectiveCost is $35.00.
4. **Allocated charge — Web Frontend Service** (Row 4): 25% allocated to `pod-aura-frontend-01`. ServiceName remains "Aura Container Runtime". AllocatedResourceId is `pod-aura-frontend-01`, AllocatedServiceName is "Aura Edge Delivery". EffectiveCost is $25.00.

The three allocated charge EffectiveCost values sum to $40.00 + $35.00 + $25.00 = $100.00, matching the origin charge total. Per DataGeneratorCalculatedSplitCostAllocationHandling, the sum of a summable metric across the allocated charges equals the corresponding origin charge, so the cost is sliced out of the origin charge rather than added alongside it. The origin charge row keeps its preserved dimensions with EffectiveCost reduced to $0.00, and no separate offsetting rows are needed.

| Row | ResourceId                  | ServiceName             | ServiceCategory | AllocatedResourceId      | AllocatedServiceName   | EffectiveCost |
| :-- | :-------------------------- | :---------------------- | :-------------- | :----------------------- | :--------------------- | ------------: |
| 1   | `cluster-aura-shared-01`    | Aura Container Runtime  | Compute         | *(null)*                 | *(null)*               |         $0.00 |
| 2   | `cluster-aura-shared-01`    | Aura Container Runtime  | Compute         | `pod-aura-orders-01`     | Aura Order Management  |        $40.00 |
| 3   | `cluster-aura-shared-01`    | Aura Container Runtime  | Compute         | `pod-aura-scoring-01`    | Aura ML Inference      |        $35.00 |
| 4   | `cluster-aura-shared-01`    | Aura Container Runtime  | Compute         | `pod-aura-frontend-01`   | Aura Edge Delivery     |        $25.00 |

## Analysis Queries Enabled by AllocatedServiceName

Practitioners can now answer two distinct questions against the same dataset without external lookups:

* **Origin-side analysis** (grouped by ServiceName): The full $100.00 remains attributed to "Aura Container Runtime", preserving the *origin charge* perspective needed for invoice reconciliation and platform team cost tracking.
* **Consumer-side analysis** (grouped by AllocatedServiceName, filtered to rows where AllocatedResourceId is not null): $40.00 is attributed to "Aura Order Management", $35.00 to "Aura ML Inference", and $25.00 to "Aura Edge Delivery", enabling showback and chargeback by the *service* that consumed the shared resource.

Without AllocatedServiceName, the consuming *service* is inferable only by joining AllocatedResourceId to an external pod-to-service mapping maintained outside the dataset.
