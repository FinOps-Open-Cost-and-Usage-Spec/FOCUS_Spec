# Examples: Data Generator-Calculated Split Cost Allocation

> Note: The following section is informative and non-normative. It does not define requirements.

This section demonstrates how [AllocatedServiceName](#datasets.costandusage.allocatedservicename) enables consumer *service* identification on [*allocated charges*](#glossary:allocated-charge) when a data generator preserves origin dimensions in accordance with [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements. It also covers the structural transformation a data generator must perform when mapping native billing data into FOCUS split allocation rows, and documents common practitioner query patterns for working with split allocation data.

## Origin Preservation and the Consumer Service Identity Gap

DataGeneratorCalculatedSplitCostAllocationHandling requires that the origin [ServiceName](#datasets.costandusage.servicename) and [ServiceCategory](#datasets.costandusage.servicecategory) are preserved on all *allocated charge* rows so that the dataset reconciles to the invoice on the origin *service*. This means a practitioner can always filter by origin ServiceName to obtain the correct invoice-reconciled total.

The side-effect of this requirement is that the consuming *service* identity is not expressed in ServiceName on *allocated charge* rows. Without AllocatedServiceName, the consuming *service* can only be inferred from [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) through an external lookup maintained by the practitioner.

AllocatedServiceName closes this gap: the data generator populates it with the consuming *service* display name on each *allocated charge* row, leaving the origin ServiceName intact.

## Shared Infrastructure Split Across Multiple Consumer Services

Acme Corp runs a shared Aura Web container cluster (`cluster-acme-shared-01`) for a single charge period (2026-04-01). The cluster hosts workloads belonging to three distinct consuming *services*. The data generator is configured to split the cluster host cost across the consuming workloads by measured vCPU-hour consumption.

The origin charge EffectiveCost for the period is $100.00. The data generator measures consumer utilization as:

* `pod-acme-orders-01` (Orders Service): 40 vCPU-hours (40%)
* `pod-acme-scoring-01` (ML Inference Service): 35 vCPU-hours (35%)
* `pod-acme-frontend-01` (Web Frontend Service): 25 vCPU-hours (25%)

The data generator emits one origin charge row and three *allocated charge* rows. Per DataGeneratorCalculatedSplitCostAllocationHandling, the origin dimensions (ServiceName, ServiceCategory, ResourceId) are preserved across all four rows. AllocatedServiceName identifies the consuming *service* on each *allocated charge* row.

Rows for the period:

1. **Origin charge** (Row 1): The origin charge row carrying the preserved origin dimensions. AllocatedResourceId is null, AllocatedServiceName is null. ServiceName is "Aura Container Runtime", ServiceCategory is "Compute". EffectiveCost is $0.00, since the full $100.00 host cost is sliced across the three allocated charge rows below.
2. **Allocated charge — Orders Service** (Row 2): 40% of the origin charge allocated to `pod-acme-orders-01`. ServiceName remains "Aura Container Runtime" (preserved from the origin charge). AllocatedResourceId is `pod-acme-orders-01`, AllocatedServiceName is "Aura Order Management". EffectiveCost is $40.00.
3. **Allocated charge — ML Inference Service** (Row 3): 35% allocated to `pod-acme-scoring-01`. ServiceName remains "Aura Container Runtime". AllocatedResourceId is `pod-acme-scoring-01`, AllocatedServiceName is "Aura ML Inference". EffectiveCost is $35.00.
4. **Allocated charge — Web Frontend Service** (Row 4): 25% allocated to `pod-acme-frontend-01`. ServiceName remains "Aura Container Runtime". AllocatedResourceId is `pod-acme-frontend-01`, AllocatedServiceName is "Aura Edge Delivery". EffectiveCost is $25.00.

The three allocated charge EffectiveCost values sum to $40.00 + $35.00 + $25.00 = $100.00, matching the origin charge total. Per DataGeneratorCalculatedSplitCostAllocationHandling, the sum of a summable metric across the allocated charges equals the corresponding origin charge, so the cost is sliced out of the origin charge rather than added alongside it. The origin charge row keeps its preserved dimensions with EffectiveCost reduced to $0.00, and no separate offsetting rows are needed.

| Row | ResourceId                  | ServiceName             | ServiceCategory | AllocatedResourceId      | AllocatedServiceName   | EffectiveCost |
| :-- | :-------------------------- | :---------------------- | :-------------- | :----------------------- | :--------------------- | ------------: |
| 1   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | *(null)*                 | *(null)*               |         $0.00 |
| 2   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `pod-acme-orders-01`     | Aura Order Management  |        $40.00 |
| 3   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `pod-acme-scoring-01`    | Aura ML Inference      |        $35.00 |
| 4   | `cluster-acme-shared-01`    | Aura Container Runtime  | Compute         | `pod-acme-frontend-01`   | Aura Edge Delivery     |        $25.00 |

## Analysis Queries Enabled by AllocatedServiceName

Practitioners can now answer two distinct questions against the same dataset without external lookups:

* **Origin-side analysis** (grouped by ServiceName): The full $100.00 remains attributed to "Aura Container Runtime", preserving the *origin charge* perspective needed for invoice reconciliation and platform team cost tracking.
* **Consumer-side analysis** (grouped by AllocatedServiceName, filtered to rows where AllocatedResourceId is not null): $40.00 is attributed to "Aura Order Management", $35.00 to "Aura ML Inference", and $25.00 to "Aura Edge Delivery", enabling showback and chargeback by the *service* that consumed the shared resource.

Without AllocatedServiceName, the consuming *service* is inferable only by joining AllocatedResourceId to an external pod-to-service mapping maintained outside the dataset.

## Producer-Side Transformation: Row Splitting vs. Column Augmentation

Some native billing formats include split allocation detail as additional columns on a single row — the origin row is augmented with allocation metadata without creating separate rows for each consumer. FOCUS takes a different structural approach: the origin charge is split into multiple rows, one per consumer, with the summable metrics (cost, usage quantities) distributed across those rows so they sum back to the origin.

This structural difference has a concrete implication for data generators: it is not sufficient to copy provider-native allocation columns into the corresponding FOCUS `Allocated*` columns on the origin row. The data generator must emit new rows — one per consumer — and reduce the summable metrics on the origin row accordingly.

### Native Input Data (Aura Web CUR-Style Format)

Aura Web's native billing export uses a column-augmentation approach. A single cluster row carries the allocation detail for all consumers in extension columns. Acme Corp's cluster `cluster-acme-shared-01` for the same period appears as:

| native_resource_id       | native_cost | native_allocated_resource_id_1 | native_allocated_ratio_1 | native_allocated_resource_id_2 | native_allocated_ratio_2 | native_allocated_resource_id_3 | native_allocated_ratio_3 |
| :----------------------- | ----------: | :----------------------------- | -----------------------: | :----------------------------- | -----------------------: | :----------------------------- | -----------------------: |
| `cluster-acme-shared-01` |     $100.00 | `pod-acme-orders-01`           |                     0.40 | `pod-acme-scoring-01`          |                     0.35 | `pod-acme-frontend-01`         |                     0.25 |

This single row carries all three allocation ratios in extension columns. Copying the `Allocated*` values onto the single origin row and leaving cost at $100.00 is **not** a valid FOCUS transformation: it would produce one row where AllocatedResourceId can only reference one consumer, the sum-to-origin requirement would not be satisfiable across multiple rows, and the remaining two consumers would be unrepresented.

### FOCUS Row-Split Output

The correct transformation emits four rows: one origin charge row with EffectiveCost zeroed, and three *allocated charge* rows each carrying one consumer's share. The result is the table shown in the [example above](#appendix.examples:datageneratorcalculatedsplitcostallocation). The key rules that govern this transformation are:

* **Dimension columns** (ServiceName, ServiceCategory, ResourceId, and all other non-summable columns): carry the origin charge value unchanged on every row, including all *allocated charge* rows.
* **Non-summable metric columns** (unit prices, rates): carry the origin charge value unchanged on every row.
* **Summable metric columns** (EffectiveCost, BilledCost, ConsumedQuantity, and others): are distributed across the *allocated charge* rows proportional to each consumer's allocation ratio. The origin charge row carries $0.00 (or 0) for each summable metric so that the sum across all rows — origin plus all *allocated charges* — equals the original pre-split total.
* **`Allocated*` columns** (AllocatedResourceId, AllocatedResourceName, AllocatedServiceName, AllocatedMethodId, AllocatedMethodDetails): are null on the origin charge row and populated on each *allocated charge* row to identify the consumer and method.

The complete four-row FOCUS output for this example is shown in the table in the section above, with AllocatedMethodDetails omitted for readability. A representative AllocatedMethodDetails JSON value for Row 2 (40% allocation by vCPU-hours) is:

```json
{
  "Elements": [
    {
      "AllocatedRatio": 0.40,
      "UsageUnit": "vCPU-Hours",
      "UsageQuantity": 40
    }
  ]
}
```

### Identifying the Unallocated Remainder

Not all shared-resource cost is always allocated. When a portion of origin charge cost is not attributable to any specific consumer — for example, when a cluster has idle capacity — the data generator may emit an additional *allocated charge* row with AllocatedResourceId set to null to represent the unallocated remainder. In this example the full $100.00 is distributed across three consumers with no remainder. When an unallocated remainder exists, all four rows (origin plus all *allocated charges* including the null-AllocatedResourceId remainder row) must still sum to the original pre-split EffectiveCost.

## Practitioner Query Patterns

The following SQL patterns use the dataset shown in the example above. All patterns assume a table named `focus_data` filtered to the relevant charge period and ChargeCategory.

### Query 1 — Total Cost by Origin Resource (Platform Team View)

This query answers "what is the total cost of the shared cluster?" using origin ServiceName. Because the origin row's EffectiveCost is $0.00 and the allocated rows carry the full $100.00, summing across all rows where ResourceId matches gives the correct total regardless of allocation state.

```sql
SELECT
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data
WHERE ResourceId = 'cluster-acme-shared-01'
GROUP BY ResourceId
```

Expected result: `cluster-acme-shared-01` → $100.00. The $0.00 origin row and the three allocated rows sum to $100.00.

### Query 2 — Total Cost by Consumer Service (Showback/Chargeback View)

This query answers "how much did each consuming service spend on shared infrastructure?" by grouping on AllocatedServiceName. Filtering to rows where AllocatedResourceId is not null excludes the origin row and any non-split rows.

```sql
SELECT
  AllocatedServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data
WHERE AllocatedResourceId IS NOT NULL
GROUP BY AllocatedServiceName
```

Expected results: Aura Order Management → $40.00, Aura ML Inference → $35.00, Aura Edge Delivery → $25.00.

### Query 3 — Total Cost by Consumer Resource (Pod-Level View)

This query answers "how much did each consuming pod spend?" grouped by AllocatedResourceId rather than AllocatedServiceName, for cases where pod-level granularity is needed rather than service-level.

```sql
SELECT
  AllocatedResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data
WHERE AllocatedResourceId IS NOT NULL
GROUP BY AllocatedResourceId
```

Expected results: `pod-acme-orders-01` → $40.00, `pod-acme-scoring-01` → $35.00, `pod-acme-frontend-01` → $25.00.

### Query 4 — Unallocated Remainder by Resource

This query surfaces any portion of origin cost that was not distributed to a specific consumer — rows where the origin resource was split but the split did not fully allocate the cost. In this example no unallocated remainder exists, so this query returns no rows. When a remainder does exist it appears as a row where AllocatedMethodId is not null (indicating the row participates in a split) but AllocatedResourceId is null (indicating no specific consumer was identified).

```sql
SELECT
  ResourceId,
  SUM(EffectiveCost) AS UnallocatedEffectiveCost
FROM focus_data
WHERE AllocatedMethodId IS NOT NULL
  AND AllocatedResourceId IS NULL
GROUP BY ResourceId
```

### Query 5 — Full Resource Breakdown (Origin Perspective Plus Consumer Detail)

This query produces a single result set that shows the origin resource in one column and each consumer (or "Unallocated" for the remainder) in a second column. It combines the origin ServiceName and ResourceId with the consumer identity, using COALESCE to label the remainder row. Because the origin row has EffectiveCost $0.00 it does not inflate totals when unioned with the allocated rows.

```sql
SELECT
  ResourceId,
  COALESCE(AllocatedServiceName, 'Unallocated') AS ConsumerService,
  COALESCE(AllocatedResourceId, 'Unallocated')  AS ConsumerResource,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data
WHERE AllocatedMethodId IS NOT NULL
GROUP BY
  ResourceId,
  COALESCE(AllocatedServiceName, 'Unallocated'),
  COALESCE(AllocatedResourceId, 'Unallocated')
```

Expected results for this example:

| ResourceId               | ConsumerService        | ConsumerResource         | TotalEffectiveCost |
| :----------------------- | :--------------------- | :----------------------- | -----------------: |
| `cluster-acme-shared-01` | Unallocated            | Unallocated              |              $0.00 |
| `cluster-acme-shared-01` | Aura Order Management  | `pod-acme-orders-01`     |             $40.00 |
| `cluster-acme-shared-01` | Aura ML Inference      | `pod-acme-scoring-01`    |             $35.00 |
| `cluster-acme-shared-01` | Aura Edge Delivery     | `pod-acme-frontend-01`   |             $25.00 |

### Query 6 — Verify Sum-to-Origin (Data Quality Check)

This query validates that the *allocated charge* rows for each origin resource sum back to the expected pre-split total. A data quality issue exists when the sum of summable metrics across allocated rows does not match the original origin total. In a correct dataset this query returns no rows; any rows returned indicate a discrepancy.

```sql
SELECT
  origin.ResourceId,
  origin.OriginTotal,
  allocated.AllocatedTotal,
  origin.OriginTotal - allocated.AllocatedTotal AS Discrepancy
FROM (
  SELECT
    ResourceId,
    SUM(EffectiveCost) AS OriginTotal
  FROM focus_data
  WHERE AllocatedMethodId IS NOT NULL
  GROUP BY ResourceId
) origin
JOIN (
  SELECT
    ResourceId,
    SUM(EffectiveCost) AS AllocatedTotal
  FROM focus_data
  WHERE AllocatedMethodId IS NOT NULL
    AND AllocatedResourceId IS NOT NULL
  GROUP BY ResourceId
) allocated ON origin.ResourceId = allocated.ResourceId
WHERE ABS(origin.OriginTotal - allocated.AllocatedTotal) > 0.01
```

> **Note:** The threshold `0.01` accommodates rounding variance. Adjust this value based on the precision requirements documented in [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).

### Double-Counting Warning

A common error when querying split allocation data is summing EffectiveCost across all rows without filtering on allocation state. Because the dataset contains both origin rows (EffectiveCost $0.00) and allocated rows (EffectiveCost distributed), an unfiltered SUM returns the correct total in the common case — but only because the origin row is already zeroed. If a data generator incorrectly leaves the origin row's EffectiveCost at the pre-split amount instead of zeroing it, an unfiltered SUM will double-count the full cost once for the origin row and once across the allocated rows. The sum-to-origin verification in Query 6 above detects this condition.

A second double-counting risk arises when joining or filtering on both ResourceId and AllocatedResourceId. These columns serve different purposes: ResourceId identifies the origin resource on every row (both origin and allocated), while AllocatedResourceId identifies the consuming resource on allocated rows only. Filtering `WHERE ResourceId = X OR AllocatedResourceId = X` for the same resource value X retrieves both the origin row and any allocated row where that resource appears as a consumer, which will sum to more than the correct total.
