# Examples: Recommendations

## Overview

The [Recommendation](#datasets.recommendation) dataset normalizes optimization recommendations so that proposals from a service provider and from third-party tooling can be reviewed in one place. Where the [Cost and Usage](#datasets.costandusage) dataset records what has already been spent, the Recommendation dataset records what a [*data generator*](#metadata.datagenerator) proposes changing, what that change is expected to cost or save, and where the proposal currently sits in its lifecycle.

The scenarios below use the fictitious cloud service provider Aura Web, the fictitious cost management platform Budget Beacon, and the fictitious customer Acme Corp.

## Example Dataset

[**CSV Example**](/specification/data/recommendations/recommendation_scenarios.csv)

The example contains eight recommendations covering a single Aura Web billing account. Five are produced by Aura Web itself and three by Budget Beacon, a third-party platform analyzing the same environment. Together they cover five Recommendation Categories and four Recommendation Statuses.

### Cost Recommendations

Four recommendations reduce cost, each using a different Recommendation Subcategory.

Note the following details in the example dataset:

* `rec-aura-000001` is a Rightsizing proposal. Resource Configuration Details Current and Resource Configuration Details Recommended both carry a JSON object describing the instance before and after the change, using the same property keys in each so the two can be compared directly.
* `rec-aura-000002` is a Commitment Purchase. It is the only row where the Contract Commitment columns are populated, and they are populated together: a one-year term, an all-upfront payment model, and a resource reservation. It has no Resource ID, because the proposal applies to a service rather than to one resource, so Resource Name and Resource Type are also null.
* `rec-aura-000003` is an Idle Resource Removal. Resource Configuration Details Current describes the volume to be deleted, while Resource Configuration Details Recommended is null because no target state exists once the resource is removed.
* `rec-aura-000005` is a Modernization proposal with a Recommendation Status of "Implemented", showing that acted-upon recommendations remain in the dataset rather than disappearing from it.

### Recommendations Beyond Cost

Four recommendations address domains other than cost, which is why Estimated Monthly Cost Impact is not populated on all of them.

Note the following details in the example dataset:

* `rec-beacon-000101` is a Security proposal with a Recommendation Status of "Deferred", representing a finding that has been reviewed and accepted as valid but scheduled for later action.
* `rec-aura-000004` is a Reliability proposal that *increases* cost. Estimated Monthly Cost Impact is a positive value, because the column is signed and expresses a change in effective cost rather than a saving.
* `rec-beacon-000102` is a Performance proposal produced by Budget Beacon against an Aura Web resource. Data Generator Name and Service Provider Name therefore hold different values.
* `rec-beacon-000103` is an Operational Excellence proposal scoped to the billing account rather than to any single resource or service, so Resource ID, Service Name, Service Category, and Service Subcategory are all null.

### Null Handling in Practice

The example is constructed to exercise the conditional nullability rules defined on the individual columns.

Note the following details in the example dataset:

* Currency and Estimated Monthly Cost Impact are always both populated or both null. The three recommendations with no monetary estimate carry no currency, because a currency without an amount conveys nothing.
* Every recommendation with a Recommendation Category of "Cost" carries an Estimated Monthly Cost Impact. Recommendations in other categories may omit it.
* `rec-beacon-000102` has no Billing Account ID. A third-party generator can identify the resource to optimize without necessarily having access to the billing account under which it is billed, so Billing Account ID and Billing Account Name are both null.
* Recommendation Subcategory always resolves to exactly one parent Recommendation Category. Categories without a specific subcategory defined use their own catch-all value, such as "Other (Security)".
* Resource Name and Resource Type are null wherever Resource ID is null, and Region Name is null wherever Region ID is null.
