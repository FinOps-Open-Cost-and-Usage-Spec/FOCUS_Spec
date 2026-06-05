# Recommendation

The Recommendation dataset is a supporting dataset that describes cost optimization recommendations generated for a [*practitioner*](#glossary:practitioner) by a [*service provider*](#glossary:service-provider). The dataset focuses on recommendations that reduce the monetary cost of [*resources*](#glossary:resource) or [*services*](#glossary:service).

## Columns

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| [Billing Account ID](#datasets.recommendation.billingaccountid) | Dimension | Mandatory | True | String |
| [Billing Currency](#datasets.recommendation.billingcurrency) | Dimension | Mandatory | True | String |
| [Contract Commitment Duration Type](#datasets.recommendation.contractcommitmentdurationtype) | Dimension | Conditional | True | String |
| [Contract Commitment Payment Model](#datasets.recommendation.contractcommitmentpaymentmodel) | Dimension | Conditional | True | String |
| [Contract Commitment Type](#datasets.recommendation.contractcommitmenttype) | Dimension | Conditional | True | String |
| [Current Resource Configuration](#datasets.recommendation.currentresourceconfiguration) | Dimension | Conditional | True | String |
| [Data Generator Name](#datasets.recommendation.datageneratorname) | Dimension | Mandatory | False | String |
| [Estimated Cost Savings](#datasets.recommendation.estimatedcostsavings) | Metric | Mandatory | True | Decimal |
| [Estimated Savings Frequency](#datasets.recommendation.estimatedsavingsfrequency) | Dimension | Conditional | True | String |
| [Implementation Effort](#datasets.recommendation.implementationeffort) | Dimension | Conditional | True | String |
| [Implementation Risk](#datasets.recommendation.implementationrisk) | Dimension | Conditional | True | String |
| [Recommendation Action](#datasets.recommendation.recommendationaction) | Dimension | Mandatory | False | String |
| [Recommendation Created](#datasets.recommendation.recommendationcreated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Description](#datasets.recommendation.recommendationdescription) | Dimension | Mandatory | True | String |
| [Recommendation ID](#datasets.recommendation.recommendationid) | Dimension | Mandatory | False | String |
| [Recommendation Last Updated](#datasets.recommendation.recommendationlastupdated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Status](#datasets.recommendation.recommendationstatus) | Dimension | Mandatory | False | String |
| [Recommended Resource Configuration](#datasets.recommendation.recommendedresourceconfiguration) | Dimension | Conditional | True | String |
| [Resource ID](#datasets.recommendation.resourceid) | Dimension | Mandatory | True | String |
| [Resource Name](#datasets.recommendation.resourcename) | Dimension | Mandatory | True | String |
| [Service Name](#datasets.recommendation.servicename) | Dimension | Mandatory | True | String |
| [Service Provider Name](#datasets.recommendation.serviceprovidername) | Dimension | Mandatory | False | String |
| [Sub Account ID](#datasets.recommendation.subaccountid) | Dimension | Conditional | True | String |

## Relationships<!--SkipTOC-->

The Recommendation dataset can be joined to the [Cost and Usage](#datasets.costandusage) dataset through identifiers shared between the two datasets.

* Resource ID associates a recommendation with the *resource* whose cost and usage the recommendation seeks to optimize.
* Billing Account ID associates a recommendation with the [*billing account*](#glossary:billing-account) under which the related cost and usage is reported.

| Dataset A      | Dataset A Column | Dataset B      | Dataset B Column |
| -------------- | ---------------- | -------------- | ---------------- |
| Recommendation | Resource ID      | Cost and Usage | Resource ID      |
| Recommendation | Billing Account ID | Cost and Usage | Billing Account ID |

## Requirements<!--SkipTOC-->

Recommendation MUST adhere to the following requirements:

* Recommendation column presence MUST adhere to the following requirements:
  * Recommendation MUST include [BillingAccountId](#datasets.recommendation.billingaccountid).
  * Recommendation MUST include [BillingCurrency](#datasets.recommendation.billingcurrency).
  * Recommendation MUST include [ContractCommitmentDurationType](#datasets.recommendation.contractcommitmentdurationtype) when a recommendation proposes the purchase of a contract commitment.
  * Recommendation MUST include [ContractCommitmentPaymentModel](#datasets.recommendation.contractcommitmentpaymentmodel) when a recommendation proposes the purchase of a contract commitment.
  * Recommendation MUST include [ContractCommitmentType](#datasets.recommendation.contractcommitmenttype) when a recommendation proposes the purchase of a contract commitment.
  * Recommendation MUST include [CurrentResourceConfiguration](#datasets.recommendation.currentresourceconfiguration) when a recommendation proposes a change to the configuration of a resource.
  * Recommendation MUST include [DataGeneratorName](#datasets.recommendation.datageneratorname).
  * Recommendation MUST include [EstimatedCostSavings](#datasets.recommendation.estimatedcostsavings).
  * Recommendation MUST include [EstimatedSavingsFrequency](#datasets.recommendation.estimatedsavingsfrequency) when EstimatedCostSavings is not null.
  * Recommendation MUST include [ImplementationEffort](#datasets.recommendation.implementationeffort) when the level of effort to act on a recommendation is available.
  * Recommendation MUST include [ImplementationRisk](#datasets.recommendation.implementationrisk) when the level of risk associated with a recommendation is available.
  * Recommendation MUST include [RecommendationAction](#datasets.recommendation.recommendationaction).
  * Recommendation MUST include [RecommendationCreated](#datasets.recommendation.recommendationcreated).
  * Recommendation MUST include [RecommendationDescription](#datasets.recommendation.recommendationdescription).
  * Recommendation MUST include [RecommendationId](#datasets.recommendation.recommendationid).
  * Recommendation MUST include [RecommendationLastUpdated](#datasets.recommendation.recommendationlastupdated).
  * Recommendation MUST include [RecommendationStatus](#datasets.recommendation.recommendationstatus).
  * Recommendation MUST include [RecommendedResourceConfiguration](#datasets.recommendation.recommendedresourceconfiguration) when a recommendation proposes a change to the configuration of a resource.
  * Recommendation MUST include [ResourceId](#datasets.recommendation.resourceid).
  * Recommendation MUST include [ResourceName](#datasets.recommendation.resourcename).
  * Recommendation MUST include [ServiceName](#datasets.recommendation.servicename).
  * Recommendation MUST include [ServiceProviderName](#datasets.recommendation.serviceprovidername).
  * Recommendation MUST include [SubAccountId](#datasets.recommendation.subaccountid) when a recommendation is associated with a sub account.
* Recommendation MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* Recommendation MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* Recommendation MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* Recommendation [*FOCUS columns*](#glossary:FOCUS-column) MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* Recommendation *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* Recommendation [*custom columns*](#glossary:custom-column) MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

Recommendation

## Display Name<!--SkipTOC-->

Recommendation

## Description<!--SkipTOC-->

Describes cost optimization recommendations generated for a *practitioner* by a *service provider* or other tooling.

## Version Introduced<!--SkipTOC-->

1.5
