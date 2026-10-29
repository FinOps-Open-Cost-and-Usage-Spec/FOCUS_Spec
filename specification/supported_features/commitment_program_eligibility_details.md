# Commitment Program Eligibility Details

## Description

FOCUS supports the identification of [*charges*](#glossary:charge) in the [Cost and Usage](#datamodel.costandusage) dataset that are eligible for [*commitment programs*](#glossary:commitment-program). The [Commitment Program Eligibility Details](#datamodel.costandusage.commitmentprogrameligibilitydetails) column captures which *commitment programs* a *charge* qualifies for, regardless of whether a [*commitment*](#glossary:commitment) is currently applied. This enables [*practitioners*](#glossary:practitioner) to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

Commitment Program Eligibility Details contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific *commitment program*. Both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and capacity-reservation programs (e.g., Advance Resource Commitments) are included in the same array, distinguished by their `ProgramType` value. [*Data generators*](#metadata.datagenerator) may include additional custom keys (prefixed with x_) to pass through extra metadata or provider-specific attributes related to the eligibility. Per the [column requirements](#datamodel.costandusage.commitmentprogrameligibilitydetails), [*service providers*](#glossary:service-provider) may include negotiated *commitment programs* when the usage is eligible and the program is not broadly applicable across the *service provider's* service catalog. For more information, see the Commitment Program Eligibility Details column definition.

### Naming Conventions for ProgramType Values

The `ProgramType` property identifies *commitment programs* supported by the provider using readable display names. Per the [column requirements](#datamodel.costandusage.commitmentprogrameligibilitydetails), these values:

* Equal [CommitmentDiscountType](#datamodel.costandusage.commitmentdiscounttype) for one object in the CommitmentPrograms array when CommitmentDiscountType is not null.
* Correspond to terminology disclosed by the service provider in public documentation. This guidance is especially relevant for SaaS providers that do not itemize commitment discount application at the row level, where CommitmentDiscountType is typically not populated.
* Do not encode period length, payment option, or other commitment attributes (e.g., use "Flexible Spend Plan" rather than "1 Year Flexible Spend Plan No Upfront").

## Directly Dependent Columns

* CommitmentProgramEligibilityDetails

## Supporting Columns

* BilledCost
* CapacityReservationId
* CapacityReservationStatus
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* CommitmentDiscountId
* CommitmentDiscountStatus
* EffectiveCost
* ServiceName
* ServiceProviderName

## Example SQL Queries

The FOCUS specification implements commitment eligibility via the Commitment Program Eligibility Details column, which is defined in [*JSON object format*](#attributes.jsonobjectformat).

Because ANSI SQL does not define a standard for parsing JSON, the following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `UNNEST`). Similar functions are available in all major SQL engines; the examples can be adapted to accommodate any particular database instance. Non-JSON constructs (CTEs, `NULLIF`) are ANSI SQL and should work without modification.

> Important Consideration: The following queries assume FOCUS-conformant [*dataset artifacts*](#glossary:dataset-artifact). *Practitioners* should verify provider conformance before relying on these queries. Non-conformant *dataset artifacts* may produce inaccurate results.
>
> **Note:** The `CommitmentPrograms` array contains all *commitment program* types, including both discount-bearing programs and [*capacity reservations*](#glossary:capacity-reservation). The first three queries below focus on discount-bearing programs and use [Commitment Discount ID](#datamodel.costandusage.commitmentdiscountid) to determine coverage. *Capacity reservations* are fundamentally different: they secure [*resource*](#glossary:resource) availability rather than provide discounts, and are tracked via [Capacity Reservation ID](#datamodel.costandusage.capacityreservationid) and [Capacity Reservation Status](#datamodel.costandusage.capacityreservationstatus). A separate query for *capacity reservation* analysis follows. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type

This query identifies *charges* that are eligible for *commitment programs* but are not currently covered by a [*commitment discount*](#glossary:commitment-discount). A *practitioner* running relevant workloads can use this to quantify the savings opportunity per *commitment program* type (e.g., "Flexible Spend Plan" vs. "Resource Reservation") and per [*service*](#glossary:service).

The query filters to *charges* where [Charge Category](#datamodel.costandusage.chargecategory) is "Usage", Commitment Program Eligibility Details is populated (the *charge* is eligible), and Commitment Discount ID is null (no *commitment* is applied). It then expands the `CommitmentPrograms` array to aggregate eligible spend per `ProgramType`. This query uses [Billed Cost](#datamodel.costandusage.billedcost) rather than [Effective Cost](#datamodel.costandusage.effectivecost) because the *charges* are uncovered (Commitment Discount ID is null), so Billed Cost reflects the actual amount paid and the savings opportunity.

> **Note:** When a *charge* is eligible for multiple *commitment program* types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

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

This query computes a *commitment discount* coverage rate using only eligible *charges* as the denominator. Without eligibility data, *practitioners* typically divide covered spend by total spend, which produces a coverage rate that includes ineligible *charges* (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity. This query targets discount-bearing programs only; for *capacity reservation* utilization, see the *capacity reservation* query below.

> **Note:** Unused *commitment discount* rows ([Commitment Discount Status](#datamodel.costandusage.commitmentdiscountstatus) is "Unused") have Commitment Discount ID populated and would artificially inflate both the numerator and the denominator, so the query excludes them. Commitment Discount Status is null on rows without a *commitment discount*, so the filter also keeps null values.

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

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A *practitioner* managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across *commitment program* types.

> **Note:** As with the first query above, when a *charge* is eligible for multiple *commitment program* types, it appears once per eligible type. Removing the `EligibleProgramType` grouping without deduplicating would inflate totals.

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

*Capacity reservations* secure *resource* availability rather than provide discounts, and are tracked via Capacity Reservation ID and Capacity Reservation Status rather than the *commitment discount* columns used in the queries above. This query identifies *charges* eligible for capacity-reservation *commitment programs*, distinguishing between used and unused reservations.

The query filters Commitment Program Eligibility Details to rows whose `ProgramType` values correspond to capacity-reservation programs (e.g., "Advance Resource Commitment", "Zonal Resource Commitment"). It then uses Capacity Reservation ID and Capacity Reservation Status to determine reservation utilization.

> **Note:** The FOCUS specification requires Capacity Reservation ID to not be null when a *charge* represents unused capacity, but only recommends populating it when a *charge* is related to a used *capacity reservation*. Where a data generator does not populate Capacity Reservation ID on used rows, this query will show those rows with a null Capacity Reservation Status.

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
