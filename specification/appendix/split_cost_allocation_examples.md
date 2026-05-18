# Examples: Data Generator-Calculated Split Cost Allocation

> Note: The following examples are informative and non-normative. They do not define requirements.

This section demonstrates how [AllocatedServiceName](#datasets.costandusage.allocatedservicename) and [AllocatedServiceCategory](#datasets.costandusage.allocatedservicecategory) interact with the other Allocated\* columns in a [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling) scenario where a shared [*resource*](#glossary:resource) hosts multiple consumer [*services*](#glossary:service) of a different [ServiceCategory](#datasets.costandusage.servicecategory) than the [*origin charge*](#glossary:origin-charge).

## Shared Compute Hosting Multiple Consumer Services

Acme Corp runs a shared Aura Web container host (*origin charge resource* `cluster-acme-shared-01`, ServiceName "Aura Container Runtime", ServiceCategory "Compute") for a single charge period (2026-04-01). Three workloads run on the cluster and the data generator is configured to split the host cost across the workloads by measured vCPU-hour consumption. Each split row represents cost allocated to a consumer *service* of a different ServiceCategory than the origin Compute charge.

The origin charge EffectiveCost for the period is $100.00. The data generator measures consumer utilization as:

* `db-acme-orders-01`: 40 vCPU-hours (40%)
* `ml-acme-scoring-01`: 35 vCPU-hours (35%)
* `web-acme-frontend-01`: 25 vCPU-hours (25%)

The data generator emits one origin charge row and three [*allocated charges*](#glossary:allocated-charge). Per [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling), the origin dimensions (ServiceName, ServiceCategory, ResourceId) are preserved across all four rows; the new AllocatedServiceName and AllocatedServiceCategory identify the consumer *service* on allocated charges.

Rows for the period:

1. **Origin charge** (Row 1): The full host cost. ChargeClass is null, AllocatedResourceId is null, AllocatedServiceName is null, AllocatedServiceCategory is null. ServiceName is "Aura Container Runtime", ServiceCategory is "Compute". EffectiveCost is $100.00.
2. **Allocated charge to Databases** (Row 2): 40% of the origin charge allocated to `db-acme-orders-01`. ChargeClass is "Correction" (a negative-offset row) plus a positive allocated row; the table below shows the positive allocated row only. ServiceName remains "Aura Container Runtime" and ServiceCategory remains "Compute" (preserved from the origin charge). AllocatedResourceId is `db-acme-orders-01`, AllocatedServiceName is "StoreStack DB", AllocatedServiceCategory is "Databases". EffectiveCost is $40.00.
3. **Allocated charge to AI and Machine Learning** (Row 3): 35% allocated to `ml-acme-scoring-01`. AllocatedResourceId is `ml-acme-scoring-01`, AllocatedServiceName is "Aura ML Inference", AllocatedServiceCategory is "AI and Machine Learning". EffectiveCost is $35.00.
4. **Allocated charge to Web** (Row 4): 25% allocated to `web-acme-frontend-01`. AllocatedResourceId is `web-acme-frontend-01`, AllocatedServiceName is "Aura Edge Delivery", AllocatedServiceCategory is "Web". EffectiveCost is $25.00.

The four EffectiveCost values sum to $100.00 (origin) + $40.00 + $35.00 + $25.00 = $200.00. To preserve invoice totals, the data generator also emits correction rows that offset the origin charge by the allocated amounts so the net sum across the four rows equals the $100.00 invoice total. Correction rows are omitted from the table below for readability; see [Correction Handling](#appendix.examples:correctionhandling) for the full offset mechanics.

| Row | ResourceId                  | ServiceName             | ServiceCategory | AllocatedResourceId      | AllocatedServiceName   | AllocatedServiceCategory  | EffectiveCost |
| :-- | :-------------------------- | :---------------------- | :-------------- | :----------------------- | :--------------------- | :------------------------ | ------------: |
| 1   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | *(null)*                 | *(null)*               | *(null)*                  |       $100.00 |
| 2   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `db-acme-orders-01`      | StoreStack DB          | Databases                 |        $40.00 |
| 3   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `ml-acme-scoring-01`     | Aura ML Inference      | AI and Machine Learning   |        $35.00 |
| 4   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `web-acme-frontend-01`   | Aura Edge Delivery     | Web                       |        $25.00 |

## Analysis Queries Enabled by the New Columns

Practitioners can now answer two distinct questions against the same dataset:

* **Origin-side analysis** (grouped by ServiceName / ServiceCategory): The full $100.00 remains attributed to "Aura Container Runtime" / "Compute", preserving the *origin charge* perspective needed for invoice reconciliation and platform team cost tracking.
* **Consumer-side analysis** (grouped by AllocatedServiceName / AllocatedServiceCategory, filtered to rows where AllocatedResourceId is not null): $40.00 is attributed to "Databases", $35.00 to "AI and Machine Learning", and $25.00 to "Web", enabling showback and chargeback by the *service* that actually consumed the shared resource.

Prior to the introduction of AllocatedServiceName and AllocatedServiceCategory, the consumer *service* was inferable only from AllocatedResourceId through an external lookup maintained by the practitioner. The new columns let the data generator express that mapping directly on each allocated charge row.
