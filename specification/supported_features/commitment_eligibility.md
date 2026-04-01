# Commitment Eligibility

## Description

FOCUS supports the identification of [*charges*](#glossary:charge) in the [Cost and Usage](#datasets.costandusage) dataset that are eligible for [*commitment programs*](#glossary:commitment-program). The [CommitmentProgramEligibility](#datasets.costandusage.commitmentprogrameligibility) column captures which *commitment programs* a charge qualifies for, regardless of whether a [*commitment*](#glossary:commitment) is currently applied. This enables practitioners to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

CommitmentProgramEligibility contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific *commitment program*. Both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and capacity-reservation programs (e.g., Advance Resource Commitments) are included in the same array, distinguished by their ProgramType value. Providers may include additional custom keys (prefixed with `x_`) for other commitment categories. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibility), providers should also include negotiated *commitment programs* for which usage is eligible. For more information, see the definition of Commitment Program Eligibility [here](#datasets.costandusage.commitmentprogrameligibility).

### Naming Conventions for ProgramType Values

The `ProgramType` property follows PascalCase by convention, identifying [*commitment programs*](#glossary:commitment-program) supported by the provider. Per the [column requirements](#datasets.costandusage.commitmentprogrameligibility), these values:

* Must equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in the CommitmentPrograms array when CommitmentDiscountType is not null.
* Should correspond to terminology disclosed by the [*service provider*](#glossary:service-provider) in public documentation. This guidance is especially relevant for SaaS providers that do not itemize [*commitment discount*](#glossary:commitment-discount) application at the row level, where CommitmentDiscountType is typically not populated.
* Do not encode [*period*](#glossary:period) length, payment option, or other *commitment* attributes (e.g., use "FlexibleSpendPlan" rather than "1YearFlexibleSpendPlanNoUpfront"). Where a provider's documented program name inherently includes a period reference (e.g., StackLens's "MonthlyPlatformCommitment"), use the provider name as-is.

## Directly Dependent Columns

* CommitmentProgramEligibility

## Supporting Columns

* BilledCost
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

Because ANSI SQL does not inherently support the parsing of JSON, the following queries leverage the JSON functions and utility functions (e.g., SAFE_DIVIDE) found in BigQuery Standard SQL in order to demonstrate this feature's functionality. Similar functions are available in all major SQL engines; thus, the below examples can be slightly modified to accommodate any particular database instance.

Note: The queries below extract from the `CommitmentPrograms` array, which contains all [*commitment program*](#glossary:commitment-program) types (both discount-bearing and capacity-reservation). To target a specific category, filter on ProgramType values. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type

This query identifies [*charges*](#glossary:charge) that are eligible for [*commitment programs*](#glossary:commitment-program) but are not currently covered by a [*commitment discount*](#glossary:commitment-discount). A practitioner running relevant workloads can use this to quantify the savings opportunity per *commitment program* type (e.g., FlexibleSpendPlan vs. ResourceReservation) and per [*service*](#glossary:service).

The query filters to "Usage" charges where CommitmentProgramEligibility is populated (the charge is eligible) and CommitmentDiscountId is null (no *commitment* is applied). It then expands the CommitmentPrograms array to aggregate eligible spend per ProgramType. This query uses BilledCost rather than EffectiveCost because the charges are uncovered (CommitmentDiscountId IS NULL), so BilledCost reflects the actual amount paid and the savings opportunity.

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
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY TotalEligibleUncoveredCost DESC
```

### Calculate Commitment Coverage Rate with Eligibility-Adjusted Denominator

This query computes a [*commitment*](#glossary:commitment) coverage rate using only eligible [*charges*](#glossary:charge) as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity.

The denominator uses an OR condition: a charge is counted as eligible if it is already covered (CommitmentDiscountId is not null) or if it is flagged as eligible (CommitmentProgramEligibility is not null). This safeguards against providers that omit the eligibility JSON on already-covered rows, which would otherwise exclude covered spend from the denominator and produce a 0% rate.

Note: Unused commitment rows (CommitmentDiscountStatus = "Unused") have CommitmentDiscountId populated and are included in both the numerator and denominator. Practitioners seeking a utilization-adjusted rate should additionally filter on CommitmentDiscountStatus = "Used". Whether CommitmentProgramEligibility must be populated on "Unused" rows is not explicitly addressed in the column requirements.

```sql
SELECT
  CU.ServiceProviderName,
  SUM(CASE
    WHEN CU.CommitmentDiscountId IS NOT NULL
    THEN CU.EffectiveCost ELSE 0 END) AS CoveredCost,
  SUM(CASE
    WHEN CU.CommitmentDiscountId IS NOT NULL
      OR CU.CommitmentProgramEligibility IS NOT NULL
    THEN CU.EffectiveCost ELSE 0 END) AS TotalEligibleCost,
  SAFE_DIVIDE(
    SUM(CASE
      WHEN CU.CommitmentDiscountId IS NOT NULL
      THEN CU.EffectiveCost ELSE 0 END),
    SUM(CASE
      WHEN CU.CommitmentDiscountId IS NOT NULL
        OR CU.CommitmentProgramEligibility IS NOT NULL
      THEN CU.EffectiveCost ELSE 0 END)
  ) AS CommitmentCoverageRate
FROM focus_data_table CU
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
GROUP BY CU.ServiceProviderName
```

### Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across [*commitment program*](#glossary:commitment-program) types.

Note: Some SaaS providers may not populate CommitmentDiscountId even when a [*commitment*](#glossary:commitment) is applied. For those providers, EffectiveCost may not reflect *commitment* pricing, and this query captures total eligible spend rather than distinguishing covered from uncovered. Practitioners should consult provider-specific documentation to determine actual *commitment* utilization.

Note: As with the first query above, when a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Removing the EligibleProgramType grouping without deduplicating would inflate totals.

```sql
SELECT
  CU.ServiceProviderName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.EffectiveCost) AS TotalEligibleCost,
  SUM(CASE
    WHEN CU.CommitmentDiscountId IS NULL
    THEN CU.EffectiveCost ELSE 0 END) AS UncoveredEligibleCost,
  SAFE_DIVIDE(
    SUM(CASE
      WHEN CU.CommitmentDiscountId IS NULL
      THEN CU.EffectiveCost ELSE 0 END),
    SUM(CU.EffectiveCost)
  ) AS UncoveredRate
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibility, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentProgramEligibility IS NOT NULL
GROUP BY
  CU.ServiceProviderName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY UncoveredEligibleCost DESC
```

## Introduced (Version)

1.4
