# Commitment Eligibility

## Description

FOCUS supports the identification of charges that are eligible for commitment programs. The [*CommitmentEligibilityDetails*](#datasets.costandusage.commitmenteligibilitydetails) column captures which commitment programs a charge qualifies for, regardless of whether a [*commitment discount*](#glossary:commitment-discount) is currently applied. This enables practitioners to calculate eligibility-adjusted commitment coverage rates, identify uncovered savings opportunities, and compare commitment options across providers.

CommitmentEligibilityDetails contains a JSON object whose FOCUS-defined key is `CommitmentDiscountTypes`, an array where each entry identifies a specific commitment program via a `Type` property. Providers may include additional custom keys (prefixed with `x_`) for other commitment categories. For more information, see the definition of CommitmentEligibilityDetails [here](#datasets.costandusage.commitmenteligibilitydetails).

### Naming Conventions for Commitment Discount Types

The `Type` property follows PascalCase by convention, identifying commitment programs supported by the provider. Per the [column requirements](#datasets.costandusage.commitmenteligibilitydetails), these values:

* Are consistent with [*CommitmentDiscountType*](#datasets.costandusage.commitmentdiscounttype) strings when that column is populated.
* Should correspond to the provider's documented terminology when CommitmentDiscountType is not populated (common for SaaS providers that do not itemize commitment discount application at the line-item level).
* Do not encode term length, payment option, or other commitment attributes. For example, use "SavingsPlan" rather than "1YearSavingsPlanNoUpfront".

Illustrative examples of Type values by provider:

| Provider    | Example Type Values                                                       | Context                                                    |
|:------------|:--------------------------------------------------------------------------|:-----------------------------------------------------------|
| AWS         | SavingsPlan, ReservedInstance                                             | Consistent with CommitmentDiscountType                     |
| Azure       | SavingsPlan, ReservedInstance                                             | Consistent with CommitmentDiscountType                     |
| GCP         | ResourceBasedCommittedUseDiscount, ComputeFlexibleCommittedUseDiscount    | Granular per commitment program                            |
| Datadog     | MonthlyCommitment, AnnualCommitment                                       | Provider terminology; CommitmentDiscountType not populated  |
| Databricks  | CommittedUseDiscount                                                      | Provider terminology                                       |

## Directly Dependent Columns

* CommitmentEligibilityDetails

## Supporting Columns

* BilledCost
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

The FOCUS specification implements commitment eligibility via the [*CommitmentEligibilityDetails*](#datasets.costandusage.commitmenteligibilitydetails) column, which is defined in [*JSON object format*](#attributes.jsonobjectformat).

Because ANSI SQL does not inherently support the parsing of JSON, the following queries leverage the JSON functions found in BigQuery Standard SQL in order to demonstrate this feature's functionality. Similar JSON functions are available in all major SQL engines; thus, the below examples can be slightly modified to accommodate any particular database instance.

Note: The queries below target the FOCUS-defined `CommitmentDiscountTypes` key. Providers using only custom (`x_`-prefixed) keys would require modified JSON paths.

### Identify Eligible Uncovered Spend by Commitment Type (CSP Example)

This query identifies on-demand charges that are eligible for commitment programs but are not currently covered by a commitment discount. A practitioner running AWS workloads can use this to quantify the savings opportunity per commitment program type (e.g., SavingsPlan vs. ReservedInstance) and per service.

The query filters to Usage charges where CommitmentEligibilityDetails is populated (the charge is eligible) and CommitmentDiscountId is null (no commitment is applied). It then expands the CommitmentDiscountTypes array to aggregate eligible spend per Type.

Note: When a charge is eligible for multiple commitment types, it appears once per eligible type. Costs are not deduplicated across types, since each type represents an independent purchasing opportunity.

```sql
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CDT, '$.Type') AS EligibleCommitmentType,
  SUM(CU.BilledCost) AS TotalEligibleUncoveredCost
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentEligibilityDetails, '$.CommitmentDiscountTypes')) AS CDT
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentDiscountId IS NULL
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CDT, '$.Type')
ORDER BY TotalEligibleUncoveredCost DESC
```

### Calculate Commitment Coverage Rate with Eligibility-Adjusted Denominator

This query computes a commitment coverage rate using only eligible charges as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity.

By filtering on `CommitmentEligibilityDetails IS NOT NULL`, the denominator includes only charges that could realistically be covered by a commitment, producing an eligibility-adjusted coverage metric.

Note: Unused commitment rows (CommitmentDiscountStatus = "Unused") have CommitmentDiscountId populated and are included in CoveredCost. This reflects that commitment capacity was purchased and allocated, even if not fully consumed. Practitioners seeking a utilization-adjusted rate should additionally filter on CommitmentDiscountStatus = "Used".

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

This query aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads (e.g., AWS alongside Databricks or Datadog) can identify where uncovered eligible spend is concentrated across commitment program types.

Note: Some SaaS providers may not populate CommitmentDiscountId even when a commitment is applied. For those providers, EffectiveCost may not reflect commitment pricing, and this query captures total eligible spend rather than distinguishing covered from uncovered. Practitioners should consult provider-specific documentation to determine actual commitment utilization.

```sql
SELECT
  CU.ServiceProviderName,
  JSON_VALUE(CDT, '$.Type') AS EligibleCommitmentType,
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
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentEligibilityDetails, '$.CommitmentDiscountTypes')) AS CDT
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
GROUP BY
  CU.ServiceProviderName,
  JSON_VALUE(CDT, '$.Type')
ORDER BY UncoveredEligibleCost DESC
```

## Introduced (Version)

1.4
