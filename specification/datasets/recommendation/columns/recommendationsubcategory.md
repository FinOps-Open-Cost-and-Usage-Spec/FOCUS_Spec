# Recommendation Subcategory

Recommendation Subcategory is a secondary classification of the [Recommendation Category](#datasets.recommendation.recommendationcategory) that identifies the specific optimization activity a recommendation proposes (e.g., Rightsizing within the Cost category). Recommendation Subcategory (in conjunction with the Recommendation Category) is commonly used to route recommendations to the team responsible for the corresponding activity.

## Requirements

RecommendationSubcategory MUST adhere to the following requirements:

* RecommendationSubcategory MUST be of type String.
* RecommendationSubcategory MUST NOT be null.
* RecommendationSubcategory MUST be one of the allowed values.
* Each RecommendationSubcategory other than "Other" MUST have one and only one parent RecommendationCategory as specified in the allowed values below.
* RecommendationSubcategory "Other" MAY be used with any RecommendationCategory.

## Allowed Values

| Recommendation Category | Recommendation Subcategory | Description                                                                         |
| ----------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| Cost                    | Rightsizing                | Adjusting the configuration or capacity of a resource to better match utilization.  |
| Cost                    | Scaling                    | Adjusting the number of running instances of a resource to match demand.            |
| Cost                    | Commitment Purchase        | Purchasing a commitment-based discount to reduce the rate paid for usage.           |
| Cost                    | Idle Resource Removal      | Stopping or deleting a resource that is idle or unused.                             |
| Cost                    | Modernization              | Migrating a resource or service to a newer or more efficient alternative.           |
| Any                     | Other                      | A recommendation that does not fall into one of the defined subcategories.          |

## Column ID

RecommendationSubcategory

## Display Name

Recommendation Subcategory

## Description

Secondary classification of the Recommendation Category that identifies the specific optimization activity a recommendation proposes.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | False                                          |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
