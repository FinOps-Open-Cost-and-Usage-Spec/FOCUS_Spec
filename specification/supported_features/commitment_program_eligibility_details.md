---
dataset: CostAndUsage
---

# Commitment Program Eligibility Details

## Description

FOCUS supports the identification of [charges](#term) in the [Cost and Usage](#ds) dataset that are eligible for [commitment programs](#term). The [Commitment Program Eligibility Details](#col) column captures which [commitment programs](#term) a [charge](#term) qualifies for, regardless of whether a [commitment](#term) is currently applied. This enables [practitioners](#term) to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

[Commitment Program Eligibility Details](#col) contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific [commitment program](#term). Both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and capacity-reservation programs (e.g., Advance Resource Commitments) are included in the same array, distinguished by their `ProgramType` value. [Data generators](#meta:DataGenerator) may include additional custom keys (prefixed with x_) to pass through extra metadata or provider-specific attributes related to the eligibility. Per the [column requirements](#col:CommitmentProgramEligibilityDetails), [service providers](#term) may include negotiated [commitment programs](#term) when the usage is eligible and the program is not broadly applicable across the *service provider's* service catalog. For more information, see the [Commitment Program Eligibility Details](#col) column definition.

### Naming Conventions for ProgramType Values

The `ProgramType` property identifies [commitment programs](#term) supported by the provider using readable display names. Per the [column requirements](#col:CommitmentProgramEligibilityDetails), these values:

* Equal [CommitmentDiscountType](#col) for one object in the CommitmentPrograms array when [CommitmentDiscountType](#col) is not null.
* Correspond to terminology disclosed by the service provider in public documentation. This guidance is especially relevant for SaaS providers that do not itemize commitment discount application at the row level, where [CommitmentDiscountType](#col) is typically not populated.
* Do not encode period length, payment option, or other commitment attributes (e.g., use "Flexible Spend Plan" rather than "1 Year Flexible Spend Plan No Upfront").

## Directly Dependent Columns

* [CommitmentProgramEligibilityDetails](#col)

## Supporting Columns

* [BilledCost](#col)
* [CapacityReservationId](#col)
* [CapacityReservationStatus](#col)
* [ChargeCategory](#col)
* [ChargePeriodEnd](#col)
* [ChargePeriodStart](#col)
* [CommitmentDiscountId](#col)
* [CommitmentDiscountStatus](#col)
* [EffectiveCost](#col)
* [ServiceName](#col)
* [ServiceProviderName](#col)

## Example SQL Queries

The FOCUS specification implements commitment eligibility via the [Commitment Program Eligibility Details](#col) column, which is defined in [JSON object format](#attr).

Because ANSI SQL does not define a standard for parsing JSON, the following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `UNNEST`). Similar functions are available in all major SQL engines; the examples can be adapted to accommodate any particular database instance. Non-JSON constructs (CTEs, `NULLIF`) are ANSI SQL and should work without modification.

> **Notes:**
>
> * The following queries assume FOCUS-conformant [dataset artifacts](#term). [Practitioners](#term) should verify provider conformance before relying on these queries. Non-conformant [dataset artifacts](#term) may produce inaccurate results.
> * The `CommitmentPrograms` array contains all [commitment program](#term) types, including both discount-bearing programs and [capacity reservations](#term). The first three queries below focus on discount-bearing programs and use [Commitment Discount ID](#col) to determine coverage. [Capacity reservations](#term) are fundamentally different: they secure [resource](#term) availability rather than provide discounts, and are tracked via [Capacity Reservation ID](#col) and [Capacity Reservation Status](#col). A separate query for [capacity reservation](#term) analysis follows. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type

This query identifies [charges](#term) that are eligible for [commitment programs](#term) but are not currently covered by a [commitment discount](#term). A [practitioner](#term) running relevant workloads can use this to quantify the savings opportunity per [commitment program](#term) type (e.g., "Flexible Spend Plan" vs. "Resource Reservation") and per [service](#term).

The query filters to [charges](#term) where [Charge Category](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory), [Commitment Program Eligibility Details](#col) is populated (the [charge](#term) is eligible), and [Commitment Discount ID](#col) is null (no [commitment](#term) is applied). It then expands the `CommitmentPrograms` array to aggregate eligible spend per `ProgramType`. This query uses [Billed Cost](#col) rather than [Effective Cost](#col) because the [charges](#term) are uncovered ([Commitment Discount ID](#col) is null), so [Billed Cost](#col) reflects the actual amount paid and the savings opportunity.

> **Note:** When a [charge](#term) is eligible for multiple [commitment program](#term) types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.BilledCost) AS EligibleUncoveredCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentDiscountId IS NULL
  AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
  -- Replace with provider-specific discount-bearing program types
  AND JSON_VALUE(CP, '$.ProgramType') IN ('Flexible Spend Plan', 'Resource Reservation')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY EligibleUncoveredCost DESC
```

### Calculate Commitment Discount Coverage Rate with Eligibility-Adjusted Denominator

This query computes a [commitment discount](#term) coverage rate using only eligible [charges](#term) as the denominator. Without eligibility data, [practitioners](#term) typically divide covered spend by total spend, which produces a coverage rate that includes ineligible [charges](#term) (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity. This query targets discount-bearing programs only; for [capacity reservation](#term) utilization, see the [capacity reservation](#term) query below.

> **Note:** Unused [commitment discount](#term) rows ([Commitment Discount Status](#col) is ["Unused"](#val:CostAndUsage.CommitmentDiscountStatus)) have [Commitment Discount ID](#col) populated and would artificially inflate both the numerator and the denominator, so the query excludes them. [Commitment Discount Status](#col) is null on rows without a [commitment discount](#term), so the filter also keeps null values.

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    CU.EffectiveCost,
    CU.CommitmentDiscountId
  FROM CostAndUsage CU
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    -- Exclude unused commitment rows; keep rows without a commitment discount
    AND (CU.CommitmentDiscountStatus IS NULL OR CU.CommitmentDiscountStatus != 'Unused')
    AND (
      -- Include covered rows in the denominator
      CU.CommitmentDiscountId IS NOT NULL
      -- If uncovered, check if the JSON array contains an eligible program type
      OR EXISTS (
        SELECT 1
        FROM UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
        WHERE JSON_VALUE(CP, '$.ProgramType') IN ('Flexible Spend Plan', 'Resource Reservation')
      )
    )
)
SELECT
  ServiceProviderName,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END) AS CoveredCost,
  SUM(EffectiveCost) AS EligibleCost,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END)
    / NULLIF(SUM(EffectiveCost), 0) AS CommitmentCoverageRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName
```

### Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A [practitioner](#term) managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across [commitment program](#term) types.

> **Note:** As with the first query above, when a [charge](#term) is eligible for multiple [commitment program](#term) types, it appears once per eligible type. Removing the `EligibleProgramType` grouping without deduplicating would inflate totals.

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    JSON_VALUE(CP, '$.ProgramType') AS ProgramType,
    CU.EffectiveCost,
    -- EffectiveCost = BilledCost for uncovered rows; used here for ratio consistency
    CASE WHEN CU.CommitmentDiscountId IS NULL THEN CU.EffectiveCost ELSE 0 END AS UncoveredCost
  FROM CostAndUsage CU
  CROSS JOIN
    UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
    -- Replace with provider-specific discount-bearing program types
    AND JSON_VALUE(CP, '$.ProgramType') IN ('Flexible Spend Plan', 'Resource Reservation')
)
SELECT
  ServiceProviderName,
  ProgramType AS EligibleProgramType,
  SUM(EffectiveCost) AS EligibleCost,
  SUM(UncoveredCost) AS UncoveredEligibleCost,
  SUM(UncoveredCost) / NULLIF(SUM(EffectiveCost), 0) AS UncoveredRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName, ProgramType
ORDER BY UncoveredEligibleCost DESC
```

### Identify Eligible Capacity Reservation Spend

[Capacity reservations](#term) secure [resource](#term) availability rather than provide discounts, and are tracked via [Capacity Reservation ID](#col) and [Capacity Reservation Status](#col) rather than the [commitment discount](#term) columns used in the queries above. This query identifies [charges](#term) eligible for capacity-reservation [commitment programs](#term), distinguishing between used and unused reservations.

The query filters [Commitment Program Eligibility Details](#col) to rows whose `ProgramType` values correspond to capacity-reservation programs (e.g., "Advance Resource Commitment", "Zonal Resource Commitment"). It then uses [Capacity Reservation ID](#col) and [Capacity Reservation Status](#col) to determine reservation utilization.

> **Note:** The FOCUS specification requires [Capacity Reservation ID](#col) to not be null when a [charge](#term) represents unused capacity, but only recommends populating it when a [charge](#term) is related to a used [capacity reservation](#term). Where a data generator does not populate [Capacity Reservation ID](#col) on used rows, this query will show those rows with a null [Capacity Reservation Status](#col).

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  CU.CapacityReservationId,
  CU.CapacityReservationStatus,
  SUM(CU.BilledCost) AS BilledCost,
  COUNT(*) AS RowCount
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
  AND JSON_VALUE(CP, '$.ProgramType') IN ('Advance Resource Commitment', 'Zonal Resource Commitment')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType'),
  CU.CapacityReservationId,
  CU.CapacityReservationStatus
ORDER BY BilledCost DESC
```

## Version Introduced

1.4
