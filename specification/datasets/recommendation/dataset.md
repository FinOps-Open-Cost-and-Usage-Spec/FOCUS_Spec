# Recommendation

The Recommendation dataset is a supporting dataset that describes optimization recommendations for [*resources*](#glossary:resource) or [*services*](#glossary:service), generated for a [*practitioner*](#glossary:practitioner) by a [*service provider*](#glossary:service-provider) or other tooling. Recommendations span optimization domains such as cost, performance, reliability, and security.

## Columns<!--SkipTOC-->

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| [Billing Account ID](#datamodel.recommendation.billingaccountid) | Dimension | Mandatory | True | String |
| [Billing Account Name](#datamodel.recommendation.billingaccountname) | Dimension | Mandatory | True | String |
| [Commitment Discount Category](#datamodel.recommendation.commitmentdiscountcategory) | Dimension | [Conditional](#operatingmodelconditions.includescontractcommitmentrecommendations) | True | String |
| [Contract Commitment Duration Type](#datamodel.recommendation.contractcommitmentdurationtype) | Dimension | [Conditional](#operatingmodelconditions.includescontractcommitmentrecommendations) | True | String |
| [Contract Commitment Payment Model](#datamodel.recommendation.contractcommitmentpaymentmodel) | Dimension | [Conditional](#operatingmodelconditions.includescontractcommitmentrecommendations) | True | String |
| [Contract Commitment Type](#datamodel.recommendation.contractcommitmenttype) | Dimension | [Conditional](#operatingmodelconditions.includescontractcommitmentrecommendations) | True | String |
| [Currency](#datamodel.recommendation.currency) | Dimension | Mandatory | True | String |
| [Estimated Monthly Cost Impact](#datamodel.recommendation.estimatedmonthlycostimpact) | Metric | Mandatory | True | Decimal |
| [Evaluation Period End](#datamodel.recommendation.evaluationperiodend) | Dimension | Optional | True | Date/Time |
| [Evaluation Period Start](#datamodel.recommendation.evaluationperiodstart) | Dimension | Optional | True | Date/Time |
| [Implementation Effort](#datamodel.recommendation.implementationeffort) | Dimension | Optional | True | String |
| [Implementation Risk](#datamodel.recommendation.implementationrisk) | Dimension | Optional | True | String |
| [Recommendation Category](#datamodel.recommendation.recommendationcategory) | Dimension | Mandatory | False | String |
| [Recommendation Created](#datamodel.recommendation.recommendationcreated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Description](#datamodel.recommendation.recommendationdescription) | Dimension | Mandatory | True | String |
| [Recommendation Details](#datamodel.recommendation.recommendationdetails) | Dimension | Mandatory | True | JSON |
| [Recommendation ID](#datamodel.recommendation.recommendationid) | Dimension | Mandatory | False | String |
| [Recommendation Last Updated](#datamodel.recommendation.recommendationlastupdated) | Dimension | Mandatory | False | Date/Time |
| [Recommendation Provider Name](#datamodel.recommendation.recommendationprovidername) | Dimension | Mandatory | False | String |
| [Recommendation Status](#datamodel.recommendation.recommendationstatus) | Dimension | Mandatory | False | String |
| [Recommendation Subcategory](#datamodel.recommendation.recommendationsubcategory) | Dimension | Mandatory | False | String |
| [Region ID](#datamodel.recommendation.regionid) | Dimension | [Conditional](#operatingmodelconditions.includesregions) | True | String |
| [Region Name](#datamodel.recommendation.regionname) | Dimension | [Conditional](#operatingmodelconditions.includesregions) | True | String |
| [Resource Configuration Details Current](#datamodel.recommendation.resourceconfigurationdetailscurrent) | Dimension | [Conditional](#operatingmodelconditions.includesresourceconfigurationrecommendations) | True | JSON |
| [Resource Configuration Details Recommended](#datamodel.recommendation.resourceconfigurationdetailsrecommended) | Dimension | [Conditional](#operatingmodelconditions.includesresourceconfigurationrecommendations) | True | JSON |
| [Resource ID](#datamodel.recommendation.resourceid) | Dimension | Mandatory | True | String |
| [Resource Name](#datamodel.recommendation.resourcename) | Dimension | Mandatory | True | String |
| [Resource Type](#datamodel.recommendation.resourcetype) | Dimension | [Conditional](#operatingmodelconditions.includesresourcetypeassignment) | True | String |
| [Service Category](#datamodel.recommendation.servicecategory) | Dimension | Mandatory | True | String |
| [Service Name](#datamodel.recommendation.servicename) | Dimension | Mandatory | True | String |
| [Service Provider Name](#datamodel.recommendation.serviceprovidername) | Dimension | Mandatory | False | String |
| [Service Subcategory](#datamodel.recommendation.servicesubcategory) | Dimension | Recommended | True | String |
| [Sub Account ID](#datamodel.recommendation.subaccountid) | Dimension | [Conditional](#operatingmodelconditions.includessubaccounts) | True | String |
| [Sub Account Name](#datamodel.recommendation.subaccountname) | Dimension | [Conditional](#operatingmodelconditions.includessubaccounts) | True | String |

## Relationships<!--SkipTOC-->

The Recommendation dataset can be joined to the [Cost and Usage](#datamodel.costandusage) dataset through identifiers shared between the two datasets.

* Resource ID associates a recommendation with the *resource* whose cost and usage the recommendation seeks to optimize.
* Billing Account ID associates a recommendation with the [*billing account*](#glossary:billing-account) under which the related cost and usage is reported.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| -------------- | ------------------ | -------------- | ------------------ |
| Recommendation | Resource ID        | Cost and Usage | Resource ID        |
| Recommendation | Billing Account ID | Cost and Usage | Billing Account ID |

## Requirements<!--SkipTOC-->

Recommendation MUST adhere to the following requirements:

* Recommendation column presence MUST adhere to the following requirements:
  * Recommendation MUST include [BillingAccountId](#datamodel.recommendation.billingaccountid).
  * Recommendation MUST include [BillingAccountName](#datamodel.recommendation.billingaccountname).
  * Recommendation MUST include [CommitmentDiscountCategory](#datamodel.recommendation.commitmentdiscountcategory) when the [*operating model*](#glossary:operating-model) [includes contract commitment recommendations](#operatingmodelconditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [ContractCommitmentDurationType](#datamodel.recommendation.contractcommitmentdurationtype) when the *operating model* [includes contract commitment recommendations](#operatingmodelconditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [ContractCommitmentPaymentModel](#datamodel.recommendation.contractcommitmentpaymentmodel) when the *operating model* [includes contract commitment recommendations](#operatingmodelconditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [ContractCommitmentType](#datamodel.recommendation.contractcommitmenttype) when the *operating model* [includes contract commitment recommendations](#operatingmodelconditions.includescontractcommitmentrecommendations).
  * Recommendation MUST include [Currency](#datamodel.recommendation.currency).
  * Recommendation MUST include [EstimatedMonthlyCostImpact](#datamodel.recommendation.estimatedmonthlycostimpact).
  * Recommendation MAY include [EvaluationPeriodEnd](#datamodel.recommendation.evaluationperiodend).
  * Recommendation MAY include [EvaluationPeriodStart](#datamodel.recommendation.evaluationperiodstart).
  * Recommendation MAY include [ImplementationEffort](#datamodel.recommendation.implementationeffort).
  * Recommendation MAY include [ImplementationRisk](#datamodel.recommendation.implementationrisk).
  * Recommendation MUST include [RecommendationCategory](#datamodel.recommendation.recommendationcategory).
  * Recommendation MUST include [RecommendationCreated](#datamodel.recommendation.recommendationcreated).
  * Recommendation MUST include [RecommendationDescription](#datamodel.recommendation.recommendationdescription).
  * Recommendation MUST include [RecommendationDetails](#datamodel.recommendation.recommendationdetails).
  * Recommendation MUST include [RecommendationId](#datamodel.recommendation.recommendationid).
  * Recommendation MUST include [RecommendationLastUpdated](#datamodel.recommendation.recommendationlastupdated).
  * Recommendation MUST include [RecommendationProviderName](#datamodel.recommendation.recommendationprovidername).
  * Recommendation MUST include [RecommendationStatus](#datamodel.recommendation.recommendationstatus).
  * Recommendation MUST include [RecommendationSubcategory](#datamodel.recommendation.recommendationsubcategory).
  * Recommendation MUST include [RegionId](#datamodel.recommendation.regionid) when the *operating model* [includes regions](#operatingmodelconditions.includesregions).
  * Recommendation MUST include [RegionName](#datamodel.recommendation.regionname) when the *operating model* [includes regions](#operatingmodelconditions.includesregions).
  * Recommendation MUST include [ResourceConfigurationDetailsCurrent](#datamodel.recommendation.resourceconfigurationdetailscurrent) when the *operating model* [includes resource configuration recommendations](#operatingmodelconditions.includesresourceconfigurationrecommendations).
  * Recommendation MUST include [ResourceConfigurationDetailsRecommended](#datamodel.recommendation.resourceconfigurationdetailsrecommended) when the *operating model* [includes resource configuration recommendations](#operatingmodelconditions.includesresourceconfigurationrecommendations).
  * Recommendation MUST include [ResourceId](#datamodel.recommendation.resourceid).
  * Recommendation MUST include [ResourceName](#datamodel.recommendation.resourcename).
  * Recommendation MUST include [ResourceType](#datamodel.recommendation.resourcetype) when the *operating model* [includes resource type assignment](#operatingmodelconditions.includesresourcetypeassignment).
  * Recommendation MUST include [ServiceCategory](#datamodel.recommendation.servicecategory).
  * Recommendation MUST include [ServiceName](#datamodel.recommendation.servicename).
  * Recommendation MUST include [ServiceProviderName](#datamodel.recommendation.serviceprovidername).
  * Recommendation SHOULD include [ServiceSubcategory](#datamodel.recommendation.servicesubcategory).
  * Recommendation MUST include [SubAccountId](#datamodel.recommendation.subaccountid) when the *operating model* [includes sub accounts](#operatingmodelconditions.includessubaccounts).
  * Recommendation MUST include [SubAccountName](#datamodel.recommendation.subaccountname) when the *operating model* [includes sub accounts](#operatingmodelconditions.includessubaccounts).
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
