# Recommendation

The Recommendation dataset is a supporting dataset that describes optimization recommendations for [*resources*](#glossary:resource) or [*services*](#glossary:service), generated for a [*practitioner*](#glossary:practitioner) by a [*service provider*](#glossary:service-provider) or other tooling. Recommendations span optimization domains such as cost, performance, reliability, and security.

## Columns<!--SkipTOC-->

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| [Billing Account ID](#datasets.recommendation.billingaccountid) | Dimension | Mandatory | True | String |
| [Billing Account Name](#datasets.recommendation.billingaccountname) | Dimension | Mandatory | True | String |
| [Contract Commitment Duration Type](#datasets.recommendation.contractcommitmentdurationtype) | Dimension | [Conditional](#conditions.includescontractcommitmentrecommendations) | True | String |
| [Contract Commitment Payment Model](#datasets.recommendation.contractcommitmentpaymentmodel) | Dimension | [Conditional](#conditions.includescontractcommitmentrecommendations) | True | String |
| [Contract Commitment Type](#datasets.recommendation.contractcommitmenttype) | Dimension | [Conditional](#conditions.includescontractcommitmentrecommendations) | True | String |
| [Currency](#datasets.recommendation.currency) | Dimension | Mandatory | True | String |
| [Data Generator Name](#datasets.recommendation.datageneratorname) | Dimension | Mandatory | False | String |
| [Estimated Monthly Cost Impact](#datasets.recommendation.estimatedmonthlycostimpact) | Metric | Mandatory | True | Decimal |
| [Implementation Effort](#datasets.recommendation.implementationeffort) | Dimension | Optional | True | String |
| [Implementation Risk](#datasets.recommendation.implementationrisk) | Dimension | Optional | True | String |
| [Recommendation Category](#datasets.recommendation.recommendationcategory) | Dimension | Mandatory | False | String |
| [Recommendation Created](#datasets.recommendation.recommendationcreated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Description](#datasets.recommendation.recommendationdescription) | Dimension | Mandatory | True | String |
| [Recommendation ID](#datasets.recommendation.recommendationid) | Dimension | Mandatory | False | String |
| [Recommendation Last Updated](#datasets.recommendation.recommendationlastupdated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Status](#datasets.recommendation.recommendationstatus) | Dimension | Mandatory | False | String |
| [Recommendation Subcategory](#datasets.recommendation.recommendationsubcategory) | Dimension | Mandatory | False | String |
| [Region ID](#datasets.recommendation.regionid) | Dimension | [Conditional](#conditions.includesregions) | True | String |
| [Region Name](#datasets.recommendation.regionname) | Dimension | [Conditional](#conditions.includesregions) | True | String |
| [Resource Configuration Details Current](#datasets.recommendation.resourceconfigurationdetailscurrent) | Dimension | [Conditional](#conditions.includesresourceconfigurationrecommendations) | True | JSON |
| [Resource Configuration Details Recommended](#datasets.recommendation.resourceconfigurationdetailsrecommended) | Dimension | [Conditional](#conditions.includesresourceconfigurationrecommendations) | True | JSON |
| [Resource ID](#datasets.recommendation.resourceid) | Dimension | Mandatory | True | String |
| [Resource Name](#datasets.recommendation.resourcename) | Dimension | Mandatory | True | String |
| [Resource Type](#datasets.recommendation.resourcetype) | Dimension | [Conditional](#conditions.includesresourcetypeassignment) | True | String |
| [Service Category](#datasets.recommendation.servicecategory) | Dimension | Mandatory | True | String |
| [Service Name](#datasets.recommendation.servicename) | Dimension | Mandatory | True | String |
| [Service Provider Name](#datasets.recommendation.serviceprovidername) | Dimension | Mandatory | False | String |
| [Service Subcategory](#datasets.recommendation.servicesubcategory) | Dimension | Recommended | True | String |
| [Sub Account ID](#datasets.recommendation.subaccountid) | Dimension | [Conditional](#conditions.includessubaccounts) | True | String |
| [Sub Account Name](#datasets.recommendation.subaccountname) | Dimension | [Conditional](#conditions.includessubaccounts) | True | String |

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
  * Recommendation MUST include [BillingAccountName](#datasets.recommendation.billingaccountname).
  * Recommendation MUST include [ContractCommitmentDurationType](#datasets.recommendation.contractcommitmentdurationtype) when the [*operating model*](#glossary:operating-model) [includes contract commitment recommendations](#conditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [ContractCommitmentPaymentModel](#datasets.recommendation.contractcommitmentpaymentmodel) when the *operating model* [includes contract commitment recommendations](#conditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [ContractCommitmentType](#datasets.recommendation.contractcommitmenttype) when the *operating model* [includes contract commitment recommendations](#conditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [Currency](#datasets.recommendation.currency).
  * Recommendation MUST include [DataGeneratorName](#datasets.recommendation.datageneratorname).
  * Recommendation MUST include [EstimatedMonthlyCostImpact](#datasets.recommendation.estimatedmonthlycostimpact).
  * Recommendation MAY include [ImplementationEffort](#datasets.recommendation.implementationeffort).
  * Recommendation MAY include [ImplementationRisk](#datasets.recommendation.implementationrisk).
  * Recommendation MUST include [RecommendationCategory](#datasets.recommendation.recommendationcategory).
  * Recommendation MUST include [RecommendationCreated](#datasets.recommendation.recommendationcreated).
  * Recommendation MUST include [RecommendationDescription](#datasets.recommendation.recommendationdescription).
  * Recommendation MUST include [RecommendationId](#datasets.recommendation.recommendationid).
  * Recommendation MUST include [RecommendationLastUpdated](#datasets.recommendation.recommendationlastupdated).
  * Recommendation MUST include [RecommendationStatus](#datasets.recommendation.recommendationstatus).
  * Recommendation MUST include [RecommendationSubcategory](#datasets.recommendation.recommendationsubcategory).
  * Recommendation MUST include [RegionId](#datasets.recommendation.regionid) when the *operating model* [includes regions](#conditions.includesregions).
  * Recommendation MUST include [RegionName](#datasets.recommendation.regionname) when the *operating model* [includes regions](#conditions.includesregions).
  * Recommendation MUST include [ResourceConfigurationDetailsCurrent](#datasets.recommendation.resourceconfigurationdetailscurrent) when the *operating model* [includes resource configuration recommendations](#conditions.includesresourceconfigurationrecommendations).
  * Recommendation MUST include [ResourceConfigurationDetailsRecommended](#datasets.recommendation.resourceconfigurationdetailsrecommended) when the *operating model* [includes resource configuration recommendations](#conditions.includesresourceconfigurationrecommendations).
  * Recommendation MUST include [ResourceId](#datasets.recommendation.resourceid).
  * Recommendation MUST include [ResourceName](#datasets.recommendation.resourcename).
  * Recommendation MUST include [ResourceType](#datasets.recommendation.resourcetype) when the *operating model* [includes resource type assignment](#conditions.includesresourcetypeassignment).
  * Recommendation MUST include [ServiceCategory](#datasets.recommendation.servicecategory).
  * Recommendation MUST include [ServiceName](#datasets.recommendation.servicename).
  * Recommendation MUST include [ServiceProviderName](#datasets.recommendation.serviceprovidername).
  * Recommendation SHOULD include [ServiceSubcategory](#datasets.recommendation.servicesubcategory).
  * Recommendation MUST include [SubAccountId](#datasets.recommendation.subaccountid) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
  * Recommendation MUST include [SubAccountName](#datasets.recommendation.subaccountname) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
* Recommendation MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
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

Describes optimization recommendations generated for a *practitioner* by a *service provider* or other tooling.

## Version Introduced<!--SkipTOC-->

1.5
