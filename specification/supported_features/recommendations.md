# Recommendations

## Description

FOCUS supports the normalization of optimization recommendations produced by service providers and third-party tooling. Recommendations are carried in a separate [Recommendation](#datamodel.recommendation) dataset, which can be joined to the [Cost and Usage](#datamodel.costandusage) dataset through the Resource ID and Billing Account ID shared between them. This enables practitioners to evaluate proposed changes against the spend those changes affect, using a single schema across every generator. For a worked dataset covering cost and non-cost recommendations produced by both a service provider and a third-party platform, see [Examples: Recommendations](#appendix.examples:recommendations).

Recommendations are classified by Recommendation Category, spanning cost, performance, reliability, security, sustainability, and operational excellence. Estimated Monthly Cost Impact expresses the projected change in effective cost over a one-month period as a signed value. Recommendations that increase cost, such as adding redundancy for reliability, are therefore represented alongside those that reduce it. Because the impact is normalized to a fixed period, recommendations from different generators can be ranked and aggregated without adjusting for differing time windows.

Recommendation Provider Name identifies the entity that produced each recommendation, which may differ from the Service Provider Name of the resource being optimized. This supports deduplicating overlapping recommendations reported by multiple tools and attributing each recommendation to the tool that surfaced it.

Recommendation Details carries supporting detail that is not expressed in other columns, such as the size of a proposed commitment discount or the metrics a recommendation was derived from. FOCUS-defined property keys make that detail queryable across providers. Evaluation Period Start and Evaluation Period End express the period a recommendation was derived from. This supports weighing the confidence of a recommendation and comparing recommendations produced by generators that evaluate different periods.

Implementation Effort expresses the relative effort to act on a recommendation, and Implementation Risk the relative risk of disruption. A worklist can be ordered by what takes the least effort to act on before the size of the projected saving. Recommendation Created and Recommendation Last Updated record when a recommendation was produced and when it last changed. This distinguishes a newly surfaced proposal from one that has been restated over time.

## Directly Dependent Columns

* [Recommendation](#datamodel.recommendation)
  * Currency
  * EstimatedMonthlyCostImpact
  * RecommendationCategory
  * RecommendationCreated
  * RecommendationDescription
  * RecommendationDetails
  * RecommendationId
  * RecommendationLastUpdated
  * RecommendationProviderName
  * ServiceProviderName

## Supporting Columns

* [Recommendation](#datasets.recommendation)
  * BillingAccountId
  * BillingAccountName
  * EvaluationPeriodEnd
  * EvaluationPeriodStart
  * ImplementationEffort
  * ImplementationRisk
  * RegionId
  * RegionName
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
  * ChargePeriodEnd
  * ChargePeriodStart
  * EffectiveCost
  * ResourceId

## Example SQL Queries

The following queries use ANSI SQL and can be run against any major database engine without modification. Recommendation Details is conveyed as a JSON key-value object and is returned as-is; reading individual properties from within it requires the JSON functions of a specific SQL dialect.

### Prioritize Cost Savings by Service

This query aggregates recommendations that reduce cost, grouped by ServiceName, ordering the largest projected savings first. Because Estimated Monthly Cost Impact is signed, savings are negative values and ascending order surfaces the largest opportunities.

```sql
SELECT
  ServiceName,
  COUNT(*) AS RecommendationCount,
  SUM(EstimatedMonthlyCostImpact) AS EstimatedMonthlyCostImpact
FROM Recommendation
WHERE RecommendationCategory = 'Cost'
  AND EstimatedMonthlyCostImpact < 0
GROUP BY ServiceName
ORDER BY SUM(EstimatedMonthlyCostImpact) ASC
```

### Compare Projected Impact Against Current Spend

This query takes inputs of a time range via ChargePeriodStart and ChargePeriodEnd, then joins cost recommendations to the Cost and Usage dataset on ResourceId and BillingAccountId. It presents the effective cost already incurred for each resource alongside the projected monthly impact. A proposed change can then be evaluated in proportion to what the resource currently costs. The join is an outer join, so a recommendation that names no resource, such as a proposal to purchase a commitment, is still returned. The time range and the BillingAccountId comparison are expressed in the join condition. A WHERE predicate on a Cost and Usage column would discard the unmatched recommendations the outer join is there to keep. CurrentEffectiveCost is null for those recommendations, recording that no comparable spend was matched.

```sql
SELECT
  REC.RecommendationId,
  REC.ResourceId,
  REC.ResourceName,
  SUM(CU.EffectiveCost) AS CurrentEffectiveCost,
  REC.EstimatedMonthlyCostImpact
FROM Recommendation REC
LEFT JOIN CostAndUsage CU
  ON REC.ResourceId = CU.ResourceId
  AND (REC.BillingAccountId IS NULL OR REC.BillingAccountId = CU.BillingAccountId)
  AND CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
WHERE REC.RecommendationCategory = 'Cost'
GROUP BY REC.RecommendationId, REC.ResourceId, REC.ResourceName, REC.EstimatedMonthlyCostImpact
ORDER BY REC.EstimatedMonthlyCostImpact ASC
```

### Build a Triage Queue

This query presents a worklist of recommendations. The least effort appears first and the largest saving breaks ties. Implementation Effort and Implementation Risk are ordinal rather than numeric, so a CASE expression establishes their order. A second CASE expression places recommendations with no Estimated Monthly Cost Impact last, because database engines differ in where they sort nulls by default. Recommendation ID breaks any remaining tie, giving the worklist the same order on every engine. Recommendation Details is returned alongside the description, giving a reviewer the proposed change and its cost in a single row.

```sql
SELECT
  RecommendationId,
  RecommendationDescription,
  ResourceType,
  RecommendationDetails,
  ImplementationEffort,
  ImplementationRisk,
  EstimatedMonthlyCostImpact,
  Currency,
  RecommendationLastUpdated
FROM Recommendation
ORDER BY
  CASE ImplementationEffort
    WHEN 'Very Low' THEN 1
    WHEN 'Low' THEN 2
    WHEN 'Medium' THEN 3
    WHEN 'High' THEN 4
    WHEN 'Very High' THEN 5
    ELSE 6
  END ASC,
  CASE WHEN EstimatedMonthlyCostImpact IS NULL THEN 1 ELSE 0 END ASC,
  EstimatedMonthlyCostImpact ASC,
  RecommendationId ASC
```

## Version Introduced

1.5
