# Commitment Eligibility

## Description

FOCUS supports the identification of [*charges*](#glossary:charge) in the Cost and Usage dataset that are eligible for [*commitment programs*](#glossary:commitment-program). The [CommitmentEligibilityDetails](#datasets.costandusage.commitmenteligibilitydetails) column captures which *commitment programs* a charge qualifies for, regardless of whether a [*commitment*](#glossary:commitment) is currently applied. This enables practitioners to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

CommitmentEligibilityDetails contains a JSON object with a FOCUS-defined top-level key `CommitmentPrograms` containing an array of objects. Each object has a `ProgramType` property identifying the specific *commitment program*. Both discount-bearing programs (e.g., Savings Plans, committed-use discounts) and capacity-reservation programs (e.g., zonal reservations) are included in the same array, distinguished by their ProgramType value. Providers MAY include additional custom keys (prefixed with `x_`) for other commitment categories. Per the [column requirements](#datasets.costandusage.commitmenteligibilitydetails), providers SHOULD also include negotiated *commitment programs* for which usage is eligible. For more information, see the definition of CommitmentEligibilityDetails [here](#datasets.costandusage.commitmenteligibilitydetails).

### Naming Conventions for ProgramType Values

The `ProgramType` property follows PascalCase by convention, identifying [*commitment programs*](#glossary:commitment-program) supported by the provider. Per the [column requirements](#datasets.costandusage.commitmenteligibilitydetails), these values:

* MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in the CommitmentPrograms array when CommitmentDiscountType is not null.
* SHOULD correspond to terminology disclosed by the [*service provider*](#glossary:service-provider) in public documentation when CommitmentDiscountType is not populated (common for SaaS providers that do not itemize [*commitment discount*](#glossary:commitment-discount) application at the row level).
* Do not encode [*period*](#glossary:period) length, payment option, or other *commitment* attributes. For example, use "SavingsPlan" rather than "1YearSavingsPlanNoUpfront". Where a provider's documented program name inherently includes a period reference (e.g., Datadog's "MonthlyCommitment"), use the provider name as-is.

Illustrative examples of ProgramType values by provider:

| Provider    | Example ProgramType Values                                                | Context                                                    |
|:------------|:--------------------------------------------------------------------------|:-----------------------------------------------------------|
| AWS         | SavingsPlan, ReservedInstance                                             | Consistent with CommitmentDiscountType                     |
| Azure       | SavingsPlan, ReservedInstance                                             | Consistent with CommitmentDiscountType                     |
| GCP         | ResourceBasedCommittedUseDiscount, ComputeFlexibleCommittedUseDiscount    | Granular per commitment program                            |
| Datadog     | MonthlyCommitment, AnnualCommitment                                       | Provider terminology; CommitmentDiscountType not populated  |
| Databricks  | CommittedUseDiscount                                                      | Provider terminology                                       |
| Snowflake   | CapacityCommitment                                                        | Provider terminology                                       |
| AWS         | CapacityReservation, ZonalReservation                                     | Capacity-reservation programs                              |

## Directly Dependent Columns

* CommitmentEligibilityDetails

## Supporting Columns

* BilledCost
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* CommitmentDiscountId
* CommitmentDiscountStatus
* CommitmentDiscountType
* EffectiveCost
* ServiceCategory
* ServiceName
* ServiceProviderName

## Example SQL Queries

The FOCUS specification implements commitment eligibility via the [CommitmentEligibilityDetails](#datasets.costandusage.commitmenteligibilitydetails) column, which is defined in [*JSON object format*](#attributes.jsonobjectformat).

Because ANSI SQL does not inherently support the parsing of JSON, the following queries leverage the JSON functions and utility functions (e.g., SAFE_DIVIDE) found in BigQuery Standard SQL in order to demonstrate this feature's functionality. Similar functions are available in all major SQL engines; thus, the below examples can be slightly modified to accommodate any particular database instance.

Note: The queries below extract from the `CommitmentPrograms` array, which contains all [*commitment program*](#glossary:commitment-program) types (both discount-bearing and capacity-reservation). To target a specific category, filter on ProgramType values. Providers using only custom (`x_`-prefixed) top-level keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Program Type (CSP Example)

This query identifies [*charges*](#glossary:charge) that are eligible for [*commitment programs*](#glossary:commitment-program) but are not currently covered by a [*commitment discount*](#glossary:commitment-discount). A practitioner running AWS workloads can use this to quantify the savings opportunity per *commitment program* type (e.g., SavingsPlan vs. ReservedInstance) and per [*service*](#glossary:service).

The query filters to "Usage" charges where CommitmentEligibilityDetails is populated (the charge is eligible) and CommitmentDiscountId is null (no *commitment* is applied). It then expands the CommitmentPrograms array to aggregate eligible spend per ProgramType. This query uses BilledCost rather than EffectiveCost because the charges are uncovered (CommitmentDiscountId IS NULL), so BilledCost reflects the actual amount paid and the savings opportunity.

Note: When a charge is eligible for multiple *commitment program* types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.BilledCost) AS TotalEligibleUncoveredCost
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentDiscountId IS NULL
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY TotalEligibleUncoveredCost DESC
```

### Calculate Commitment Coverage Rate with Eligibility-Adjusted Denominator

This query computes a [*commitment*](#glossary:commitment) coverage rate using only eligible [*charges*](#glossary:charge) as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity.

By filtering on `CommitmentEligibilityDetails IS NOT NULL`, the denominator includes only charges that could realistically be covered by a *commitment*, producing an eligibility-adjusted coverage metric.

Note: Unused commitment rows (CommitmentDiscountStatus = "Unused") have CommitmentDiscountId populated and are included in CoveredCost. Practitioners seeking a utilization-adjusted rate should additionally filter on CommitmentDiscountStatus = "Used". Whether CommitmentEligibilityDetails MUST be populated on "Unused" rows is not explicitly addressed in the column requirements. If a provider does not populate it on "Unused" rows, the denominator excludes them while the numerator does not, potentially inflating the coverage rate.

```sql
SELECT
  CU.ServiceProviderName,
  SUM(CASE
    WHEN CU.CommitmentDiscountId IS NOT NULL
    THEN CU.EffectiveCost ELSE 0 END) AS CoveredCost,
  SUM(CU.EffectiveCost) AS TotalEligibleCost,
  SAFE_DIVIDE(
    SUM(CASE
      WHEN CU.CommitmentDiscountId IS NOT NULL
      THEN CU.EffectiveCost ELSE 0 END),
    SUM(CU.EffectiveCost)
  ) AS CommitmentCoverageRate
FROM focus_data_table CU
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentEligibilityDetails IS NOT NULL
GROUP BY CU.ServiceProviderName
```

### Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads (e.g., AWS alongside Databricks or Datadog) can identify where uncovered eligible spend is concentrated across [*commitment program*](#glossary:commitment-program) types.

Note: Some SaaS providers may not populate CommitmentDiscountId even when a [*commitment*](#glossary:commitment) is applied. For those providers, EffectiveCost may not reflect *commitment* pricing, and this query captures total eligible spend rather than distinguishing covered from uncovered. Practitioners should consult provider-specific documentation to determine actual *commitment* utilization.

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
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
GROUP BY
  CU.ServiceProviderName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY UncoveredEligibleCost DESC
```

## Introduced (Version)

1.4
