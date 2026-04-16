# Commitment Program Eligibility Details

## Description

FOCUS supports the identification of [*charges*](#glossary:charge) in the [Cost and Usage](#datasets.costandusage) dataset that are eligible for [*commitment programs*](#glossary:commitment-program). The [Commitment Program Eligibility Details](#datasets.costandusage.commitmentprogrameligibilitydetails) column captures which *commitment programs* a charge qualifies for, regardless of whether a [*commitment*](#glossary:commitment) is currently applied. This enables practitioners to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

CommitmentProgramEligibilityDetails contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific *commitment program*. Both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and capacity-reservation programs (e.g., Advance Resource Commitments) are included in the same array, distinguished by their `ProgramType` value. [*Data generators*](#metadata:datagenerator) may include additional custom keys (prefixed with x_) to pass through extra metadata or provider-specific attributes related to the eligibility. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibilitydetails), service providers may include negotiated *commitment programs* when the usage is eligible and the program is not broadly applicable across the service provider's service catalog. For more information, see the CommitmentProgramEligibilityDetails column definition.

### Naming Conventions for ProgramType Values

The `ProgramType` property identifies *commitment programs* supported by the provider using readable display names. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibilitydetails), these values:

* Equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in the CommitmentPrograms array when CommitmentDiscountType is not null.
* Correspond to terminology disclosed by the service provider in public documentation. This guidance is especially relevant for SaaS providers that do not itemize commitment discount application at the row level, where CommitmentDiscountType is typically not populated.
* Do not encode period length, payment option, or other commitment attributes (e.g., use "Flexible Spend Plan" rather than "1 Year Flexible Spend Plan No Upfront").
* Use the provider name as-is where a provider's documented program name inherently includes a period reference (e.g., StackLens's "Monthly Platform Commitment").

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
* CommitmentDiscountType
* EffectiveCost
* ServiceName
* ServiceProviderName

## Example SQL Queries

> Note: The following examples are informative and non-normative. They do not define requirements.

The FOCUS specification implements commitment eligibility via the [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) column, which is defined in [*JSON object format*](#attributes.jsonobjectformat).

Because ANSI SQL does not define a standard for parsing JSON, the following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `UNNEST`). Similar functions are available in all major SQL engines; the examples can be adapted to accommodate any particular database instance. Non-JSON constructs (CTEs, `NULLIF`) are ANSI SQL and should work without modification.

> Important Consideration: The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

Note: The `CommitmentPrograms` array contains all [*commitment program*](#glossary:commitment-program) types, including both discount-bearing programs and [*capacity reservations*](#glossary:capacity-reservation). The first three queries below focus on discount-bearing programs and use [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) to determine coverage. Capacity reservations are fundamentally different: they secure resource availability rather than provide discounts, and are tracked via [CapacityReservationId](#datasets.costandusage.capacityreservationid) and [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus). A separate query for capacity reservation analysis follows. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type

This query identifies [*charges*](#glossary:charge) that are eligible for [*commitment programs*](#glossary:commitment-program) but are not currently covered by a [*commitment discount*](#glossary:commitment-discount). A practitioner running relevant workloads can use this to quantify the savings opportunity per *commitment program* type (e.g., Flexible Spend Plan vs. Resource Reservation) and per [*service*](#glossary:service).

The query filters to "Usage" charges where [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) is populated (the charge is eligible) and [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is null (no [*commitment*](#glossary:commitment) is applied). It then expands the `CommitmentPrograms` array to aggregate eligible spend per `ProgramType`. This query uses BilledCost rather than EffectiveCost because the charges are uncovered (CommitmentDiscountId IS NULL), so BilledCost reflects the actual amount paid and the savings opportunity.

Note: When a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.BilledCost) AS EligibleUncoveredCost
FROM focus_data_table CU
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

This query computes a [*commitment discount*](#glossary:commitment-discount) coverage rate using only eligible [*charges*](#glossary:charge) as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity. This query targets discount-bearing programs only; for [*capacity reservation*](#glossary:capacity-reservation) utilization, see the capacity reservation query below.

Note: Unused commitment rows (CommitmentDiscountStatus = "Unused") have CommitmentDiscountId populated and will artificially inflate both the numerator and the denominator if left in the dataset. To calculate a true, utilization-adjusted coverage rate, practitioners should additionally filter out these rows (e.g., AND CU.CommitmentDiscountStatus != 'Unused').

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    CU.EffectiveCost,
    CU.CommitmentDiscountId
  FROM focus_data_table CU
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
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

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across [*commitment program*](#glossary:commitment-program) types.

Note: As with the first query above, when a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Removing the EligibleProgramType grouping without deduplicating would inflate totals.

```sql
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    JSON_VALUE(CP, '$.ProgramType') AS ProgramType,
    CU.EffectiveCost,
    -- EffectiveCost = BilledCost for uncovered rows; used here for ratio consistency
    CASE WHEN CU.CommitmentDiscountId IS NULL THEN CU.EffectiveCost ELSE 0 END AS UncoveredCost
  FROM focus_data_table CU
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

[*Capacity reservations*](#glossary:capacity-reservation) secure resource availability rather than provide discounts, and are tracked via [CapacityReservationId](#datasets.costandusage.capacityreservationid) and [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) rather than the [*commitment discount*](#glossary:commitment-discount) columns used in the queries above. This query identifies [*charges*](#glossary:charge) eligible for capacity-reservation [*commitment programs*](#glossary:commitment-program), distinguishing between used and unused reservations.

The query filters [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) to rows whose `ProgramType` values correspond to capacity-reservation programs (e.g., "Advance Resource Commitment", "Zonal Resource Commitment"). It then uses CapacityReservationId and CapacityReservationStatus to determine reservation utilization.

Note: The FOCUS specification requires CapacityReservationId to not be null when a charge represents unused capacity, but only recommends populating it when a charge is related to a used *capacity reservation*. Where a data generator does not populate CapacityReservationId on used rows, this query will show those rows with a null CapacityReservationStatus.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  CU.CapacityReservationStatus,
  SUM(CU.BilledCost) AS BilledCost,
  COUNT(*) AS RowCount
FROM focus_data_table CU
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
  CU.CapacityReservationStatus
ORDER BY BilledCost DESC
```

## Introduced (version)

1.4
