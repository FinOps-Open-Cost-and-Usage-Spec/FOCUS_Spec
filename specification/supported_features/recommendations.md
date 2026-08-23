# Recommendations

## Description

FOCUS supports the normalization of optimization recommendations produced by service providers and third-party tooling. Recommendations are carried in a separate [Recommendation](#datasets.recommendation) dataset, which can be joined to the [Cost and Usage](#datasets.costandusage) dataset through the Resource ID and Billing Account ID shared between them. This allows a practitioner to evaluate proposed changes against the spend those changes would affect, using a single schema across every generator rather than one report format per provider or vendor. For a worked dataset covering cost and non-cost recommendations produced by both a service provider and a third-party platform, see [Examples: Recommendations](#appendix.examples:recommendations).

Recommendations are classified by Recommendation Category and Recommendation Subcategory, spanning cost, performance, reliability, security, sustainability, and operational excellence. Estimated Monthly Cost Impact expresses the projected change in effective cost over a one-month period as a signed value, so that recommendations which increase cost, such as adding redundancy for reliability, are represented alongside those which reduce it. Because the impact is normalized to a fixed period, recommendations from different generators can be ranked and aggregated without adjusting for differing time windows.

Recommendation Provider Name identifies the entity that produced each recommendation, which may differ from the Service Provider Name of the resource being optimized. This supports deduplicating overlapping recommendations reported by multiple tools and attributing realized savings to the tool that surfaced the opportunity.

Recommendation Details carries supporting detail that is not expressed in other columns, such as the size of a proposed commitment discount or the metrics a recommendation was derived from, using FOCUS-defined property keys so that detail is queryable across providers. Evaluation Period Start and Evaluation Period End express the period a recommendation was derived from, allowing a practitioner to weigh the confidence of a recommendation and to compare recommendations produced by generators that evaluate different periods.

## Directly Dependent Columns

* [Recommendation](#datasets.recommendation)
  * Currency
  * EstimatedMonthlyCostImpact
  * RecommendationCategory
  * RecommendationCreated
  * RecommendationDescription
  * RecommendationDetails
  * RecommendationId
  * RecommendationLastUpdated
  * RecommendationProviderName
  * RecommendationStatus
  * RecommendationSubcategory
  * ServiceProviderName

## Supporting Columns

* [Recommendation](#datasets.recommendation)
  * BillingAccountId
  * BillingAccountName
  * CommitmentDiscountCategory
  * ContractCommitmentDurationType
  * ContractCommitmentPaymentModel
  * ContractCommitmentType
  * EvaluationPeriodEnd
  * EvaluationPeriodStart
  * ImplementationEffort
  * ImplementationRisk
  * RegionId
  * RegionName
  * ResourceConfigurationDetailsCurrent
  * ResourceConfigurationDetailsRecommended
  * ResourceId
  * ResourceName
  * ResourceType
  * ServiceCategory
  * ServiceName
  * ServiceSubcategory
  * SubAccountId
  * SubAccountName
* [CostAndUsage](#datasets.costandusage)
  * BillingAccountId
  * EffectiveCost
  * ResourceId

## Example SQL Queries

The following queries use ANSI SQL and can be run against any major database engine without modification. Resource configuration details are conveyed as JSON key-value objects and are returned as-is; reading individual properties from within them requires the JSON functions of a specific SQL dialect.

### Prioritize Open Cost Savings by Service

This query aggregates open recommendations that reduce cost, grouped by ServiceName and RecommendationSubcategory, ordering the largest projected savings first. Because Estimated Monthly Cost Impact is signed, savings are negative values and ascending order surfaces the largest opportunities.

```sql
SELECT
  ServiceName,
  RecommendationSubcategory,
  COUNT(*) AS RecommendationCount,
  SUM(EstimatedMonthlyCostImpact) AS EstimatedMonthlyCostImpact
FROM Recommendation
WHERE RecommendationCategory = 'Cost'
  AND RecommendationStatus = 'Open'
  AND EstimatedMonthlyCostImpact < 0
GROUP BY ServiceName, RecommendationSubcategory
ORDER BY SUM(EstimatedMonthlyCostImpact) ASC
```

### Compare Projected Impact Against Current Spend

This query takes inputs of a time range via ChargePeriodStart and ChargePeriodEnd, then joins open cost recommendations to the Cost and Usage dataset on ResourceId and BillingAccountId. It presents the effective cost already incurred for each resource alongside the projected monthly impact, so that a proposed change can be evaluated in proportion to what the resource currently costs.

```sql
SELECT
  REC.RecommendationId,
  REC.ResourceId,
  REC.ResourceName,
  REC.RecommendationSubcategory,
  SUM(CU.EffectiveCost) AS CurrentEffectiveCost,
  REC.EstimatedMonthlyCostImpact
FROM Recommendation REC
INNER JOIN CostAndUsage CU
  ON REC.ResourceId = CU.ResourceId
  AND REC.BillingAccountId = CU.BillingAccountId
WHERE REC.RecommendationCategory = 'Cost'
  AND REC.RecommendationStatus = 'Open'
  AND CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
GROUP BY REC.RecommendationId, REC.ResourceId, REC.ResourceName, REC.RecommendationSubcategory, REC.EstimatedMonthlyCostImpact
ORDER BY REC.EstimatedMonthlyCostImpact ASC
```

### Track Recommendation Adoption by Recommendation Provider

This query takes inputs of a time range via RecommendationCreated, then reports how many recommendations each recommendation provider produced per category and how many of those have been implemented. This supports comparing the yield of the recommendation sources in use.

```sql
SELECT
  RecommendationProviderName,
  RecommendationCategory,
  COUNT(*) AS RecommendationCount,
  SUM(CASE WHEN RecommendationStatus = 'Implemented' THEN 1 ELSE 0 END) AS ImplementedCount
FROM Recommendation
WHERE RecommendationCreated >= ? AND RecommendationCreated < ?
GROUP BY RecommendationProviderName, RecommendationCategory
ORDER BY RecommendationProviderName, RecommendationCategory
```

### Build a Triage Queue for Open Recommendations

This query presents a worklist of recommendations awaiting action, ordered so that the least effort appears first and the largest saving breaks ties. Implementation Effort and Implementation Risk are ordinal rather than numeric, so a CASE expression establishes their order. The current and recommended configurations are returned alongside the description, giving a reviewer the proposed change and its cost in a single row.

```sql
SELECT
  RecommendationId,
  RecommendationDescription,
  ResourceType,
  ResourceConfigurationDetailsCurrent,
  ResourceConfigurationDetailsRecommended,
  ImplementationEffort,
  ImplementationRisk,
  EstimatedMonthlyCostImpact,
  Currency,
  RecommendationLastUpdated
FROM Recommendation
WHERE RecommendationStatus IN ('Open', 'Deferred')
ORDER BY
  CASE ImplementationEffort
    WHEN 'Very Low' THEN 1
    WHEN 'Low' THEN 2
    WHEN 'Medium' THEN 3
    WHEN 'High' THEN 4
    WHEN 'Very High' THEN 5
    ELSE 6
  END ASC,
  EstimatedMonthlyCostImpact ASC
```

### Evaluate Commitment Purchase Recommendations

This query isolates recommendations proposing the purchase of a contract commitment and reports the terms of each proposal. The Contract Commitment columns are populated only for this subcategory, so filtering on it avoids returning rows where those columns are null. Commitment Discount Category classifies each proposal as spend-based or usage-based independently of the provider-specific Contract Commitment Type value.

```sql
SELECT
  RecommendationId,
  ServiceProviderName,
  CommitmentDiscountCategory,
  ContractCommitmentType,
  ContractCommitmentPaymentModel,
  ContractCommitmentDurationType,
  EstimatedMonthlyCostImpact,
  Currency
FROM Recommendation
WHERE RecommendationSubcategory = 'Commitment Purchase'
  AND RecommendationStatus = 'Open'
ORDER BY EstimatedMonthlyCostImpact ASC
```

## Version Introduced

1.5
