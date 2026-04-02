# Commitment Program Eligibility

## Description

FOCUS supports the identification of [*charges*](#glossary:charge) in the [Cost and Usage](#datasets.costandusage) dataset that are eligible for [*commitment programs*](#glossary:commitment-program). The [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) column captures which *commitment programs* a charge qualifies for, regardless of whether a [*commitment*](#glossary:commitment) is currently applied. This enables practitioners to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

CommitmentProgramEligibility contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific *commitment program*. Both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and capacity-reservation programs (e.g., Advance Resource Commitments) are included in the same array, distinguished by their `ProgramType` value. Providers may include additional custom keys (prefixed with x_) to pass through extra metadata or provider-specific attributes related to the eligibility. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibility), providers should also include negotiated *commitment programs* for which usage is eligible. For more information, see the definition of Commitment Program Eligibility [here](#datasets.costandusage.commitmentprogrameligibility).

### Naming Conventions for ProgramType Values

The `ProgramType` property follows PascalCase by convention, identifying [*commitment programs*](#glossary:commitment-program) supported by the provider. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibility), these values:

* Must equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in the `CommitmentPrograms` array when CommitmentDiscountType is not null.
* Should correspond to terminology disclosed by the [*service provider*](#glossary:service-provider) in public documentation. This guidance is especially relevant for SaaS providers that do not itemize [*commitment discount*](#glossary:commitment-discount) application at the row level, where CommitmentDiscountType is typically not populated.
* Do not encode [*period*](#glossary:period) length, payment option, or other [*commitment*](#glossary:commitment) attributes (e.g., use "FlexibleSpendPlan" rather than "1YearFlexibleSpendPlanNoUpfront"). Where a provider's documented program name inherently includes a period reference (e.g., StackLens's "MonthlyPlatformCommitment"), use the provider name as-is.

## Directly Dependent Columns

* CommitmentProgramEligibility

## Supporting Columns

* BilledCost
* CapacityReservationId
* CapacityReservationStatus
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* CommitmentDiscountId
* CommitmentDiscountStatus
* CommitmentDiscountType
* EffectiveCost
* ServiceName
* ServiceProviderName

## Example SQL Queries

The FOCUS specification implements commitment eligibility via the [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) column, which is defined in [*JSON object format*](#attributes.jsonobjectformat).

Because ANSI SQL does not define a standard for parsing JSON, the following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `UNNEST`). Similar functions are available in all major SQL engines; the examples can be adapted to accommodate any particular database instance. Non-JSON constructs (CTEs, `NULLIF`) are ANSI SQL and should work without modification.

Note: The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

Note: The `CommitmentPrograms` array contains all [*commitment program*](#glossary:commitment-program) types, including both discount-bearing programs and [*capacity reservations*](#glossary:capacity-reservation). The first three queries below focus on discount-bearing programs and use [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) to determine coverage. Capacity reservations are fundamentally different: they secure resource availability rather than provide discounts, and are tracked via [CapacityReservationId](#datasets.costandusage.capacityreservationid) and [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus). A separate query for capacity reservation analysis follows. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type

This query identifies [*charges*](#glossary:charge) that are eligible for [*commitment programs*](#glossary:commitment-program) but are not currently covered by a [*commitment discount*](#glossary:commitment-discount). A practitioner running relevant workloads can use this to quantify the savings opportunity per *commitment program* type (e.g., FlexibleSpendPlan vs. ResourceReservation) and per [*service*](#glossary:service).

The query filters to "Usage" charges where [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) is populated (the charge is eligible) and [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is null (no [*commitment*](#glossary:commitment) is applied). It then expands the `CommitmentPrograms` array to aggregate eligible spend per `ProgramType`. This query uses BilledCost rather than EffectiveCost because the charges are uncovered (CommitmentDiscountId IS NULL), so BilledCost reflects the actual amount paid and the savings opportunity.

Note: When a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.BilledCost) AS TotalEligibleUncoveredCost
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibility, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentDiscountId IS NULL
  AND CU.CommitmentProgramEligibility IS NOT NULL
  -- Replace with provider-specific discount-bearing program types
  AND JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY TotalEligibleUncoveredCost DESC
```

### Calculate Commitment Discount Coverage Rate with Eligibility-Adjusted Denominator

This query computes a [*commitment discount*](#glossary:commitment-discount) coverage rate using only eligible [*charges*](#glossary:charge) as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity. This query targets discount-bearing programs only; for [*capacity reservation*](#glossary:capacity-reservation) utilization, see the capacity reservation query below.

Note: Unused commitment rows (CommitmentDiscountStatus = "Unused") have CommitmentDiscountId populated and will artificially inflate both the numerator and the denominator if left in the dataset. To calculate a true, utilization-adjusted coverage rate, practitioners should additionally filter out these rows (e.g., AND CU.CommitmentDiscountStatus != 'Unused').

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    CU.EffectiveCost,
    CU.CommitmentDiscountId
  FROM focus_data_table CU
  CROSS JOIN
    UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibility, '$.CommitmentPrograms')) AS CP
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    AND CU.CommitmentProgramEligibility IS NOT NULL
    -- Replace with provider-specific discount-bearing program types
    AND JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
)
SELECT
  ServiceProviderName,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END) AS CoveredCost,
  SUM(EffectiveCost) AS TotalEligibleCost,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END)
    / NULLIF(SUM(EffectiveCost), 0) AS CommitmentCoverageRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName
```

### Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across [*commitment program*](#glossary:commitment-program) types.

Note: As with the first query above, when a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Removing the EligibleProgramType grouping without deduplicating would inflate totals.

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    JSON_VALUE(CP, '$.ProgramType') AS ProgramType,
    CU.EffectiveCost,
    CASE WHEN CU.CommitmentDiscountId IS NULL THEN CU.EffectiveCost ELSE 0 END AS UncoveredCost
  FROM focus_data_table CU
  CROSS JOIN
    UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibility, '$.CommitmentPrograms')) AS CP
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    AND CU.CommitmentProgramEligibility IS NOT NULL
    -- Replace with provider-specific discount-bearing program types
    AND JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
)
SELECT
  ServiceProviderName,
  ProgramType AS EligibleProgramType,
  SUM(EffectiveCost) AS TotalEligibleCost,
  SUM(UncoveredCost) AS UncoveredEligibleCost,
  SUM(UncoveredCost) / NULLIF(SUM(EffectiveCost), 0) AS UncoveredRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName, ProgramType
ORDER BY UncoveredEligibleCost DESC
```

### Identify Eligible Capacity Reservation Spend

[*Capacity reservations*](#glossary:capacity-reservation) secure resource availability rather than provide discounts, and are tracked via [CapacityReservationId](#datasets.costandusage.capacityreservationid) and [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) rather than the [*commitment discount*](#glossary:commitment-discount) columns used in the queries above. This query identifies [*charges*](#glossary:charge) eligible for capacity-reservation [*commitment programs*](#glossary:commitment-program), distinguishing between used and unused reservations.

The query filters [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) to rows whose `ProgramType` values correspond to capacity-reservation programs (e.g., "AdvanceResourceCommitment", "ZonalResourceCommitment"). It then uses CapacityReservationId and CapacityReservationStatus to determine reservation utilization.

Note: The FOCUS specification requires CapacityReservationId to not be null when a charge represents unused capacity (MUST), but only recommends (SHOULD) populating it when a charge is related to a used [*capacity reservation*](#glossary:capacity-reservation). Where a provider does not populate CapacityReservationId on used rows, this query will show those rows with a null CapacityReservationStatus.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  CU.CapacityReservationStatus,
  SUM(CU.BilledCost) AS TotalCost,
  COUNT(*) AS RowCount
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibility, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentProgramEligibility IS NOT NULL
  AND JSON_VALUE(CP, '$.ProgramType') IN ('AdvanceResourceCommitment', 'ZonalResourceCommitment')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType'),
  CU.CapacityReservationStatus
ORDER BY TotalCost DESC
```

### Capacity Reservation Eligible Spend

This example demonstrates how [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) interacts with [CapacityReservationId](#datasets.costandusage.capacityreservationid) and [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) for [*capacity reservation*](#glossary:capacity-reservation) programs. Unlike discount-bearing [*commitment programs*](#glossary:commitment-program), capacity reservations secure resource availability and are tracked via their own columns rather than the [*commitment discount*](#glossary:commitment-discount) columns. For discount-bearing program examples, see the [uncovered eligible spend](/specification/data/commitment_eligibility/uncovered_eligible_spend_by_program_type.csv) and [coverage rate](/specification/data/commitment_eligibility/coverage_rate_eligibility_adjusted.csv) CSVs.

Acme Corp runs compute workloads on Aura Web and holds an Advance Resource Commitment (cr-arc-acme-001) for a single charge period (2025-04-01). The `ProgramType` values "AdvanceResourceCommitment" and "ZonalResourceCommitment" are illustrative and do not correspond to a specific provider's program names.

This example focuses on Usage rows, which are the rows that the capacity reservation query above filters on. Purchase rows for the reservation itself are not shown.

Four usage rows for the period:

1. **Used capacity** (Row 1): Compute usage consuming the reservation. [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) is "Used". [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are both &dollar;180.00.
2. **Unused capacity** (Row 2): Reserved capacity that went idle. CapacityReservationStatus is "Unused". BilledCost and EffectiveCost are both &dollar;70.00. Unlike *commitment discount* unused rows (where BilledCost is &dollar;0.00 because the purchase is invoiced separately), capacity reservation rows reflect the cost of reserved capacity whether consumed or not.
3. **Eligible but unreserved** (Row 3): Compute usage eligible for a ZonalResourceCommitment but no reservation is active. CapacityReservationId and CapacityReservationStatus are null. BilledCost and EffectiveCost are both &dollar;120.00 at standard pricing.
4. **Ineligible** (Row 4): A support fee with no [*commitment program*](#glossary:commitment-program) eligibility. CommitmentProgramEligibility is null.

CommitmentProgramEligibility is populated on both Used and Unused rows (Rows 1 and 2). The column requirement states that CommitmentProgramEligibility "MUST NOT be null when a charge is eligible for a commitment program, regardless of whether a commitment was actually applied." Because the underlying resource type remains eligible for the program regardless of utilization status, this example populates the column on both rows. Omitting it on Unused rows would prevent the capacity reservation query from surfacing utilization data. If the Task Force determines that CommitmentProgramEligibility should not be populated on Unused rows, the query would need to use a LEFT JOIN with an OR condition (`CommitmentProgramEligibility IS NOT NULL OR CapacityReservationId IS NOT NULL`) and a COALESCE fallback for `ProgramType`.

The capacity reservation query filters on CommitmentProgramEligibility and specific `ProgramType` values. Row 4 is excluded because CommitmentProgramEligibility is null. Rows 1 through 3 appear in the output, grouped by `ProgramType` and CapacityReservationStatus, allowing practitioners to see used, unused, and unreserved eligible spend separately.

[CSV Example](/specification/data/commitment_eligibility/capacity_reservation_eligible_spend.csv)

## Introduced (Version)

1.4
