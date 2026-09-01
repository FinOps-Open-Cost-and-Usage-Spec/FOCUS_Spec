# Examples: Recommendations

## Overview

The [Recommendation](#datasets.recommendation) dataset normalizes optimization recommendations so that proposals from a service provider and from third-party tooling can be reviewed in one place. Where the [Cost and Usage](#datasets.costandusage) dataset records what has already been spent, the Recommendation dataset records what a [data generator](#metadata.datagenerator) proposes changing, what that change is expected to cost or save, and where the proposal currently sits in its lifecycle.

The scenarios below use the fictitious cloud service provider Aura Web, the fictitious cost management platform Budget Beacon, and the fictitious customer Acme Corp.

## Example Dataset

[**CSV Example**](/specification/data/recommendations/recommendation_scenarios.csv)

The example contains eight recommendations covering a single Aura Web billing account. Five are produced by Aura Web itself and three by Budget Beacon, a third-party platform analyzing the same environment. Together they cover five Recommendation Categories and four Recommendation Statuses.

### Cost Recommendations

Four recommendations reduce cost, each using a different Recommendation Subcategory.

Note the following details in the example dataset:

* `rec-aura-000001` is a Rightsizing proposal. Resource Configuration Details Current and Resource Configuration Details Recommended both carry a JSON object describing the instance before and after the change, using the same property keys in each so the two can be compared directly. Recommendation Details carries the observed metrics the proposal was derived from, each key combining a metric name with a calculation, so that an average and a 95th percentile of the same metric are separately queryable.
* `rec-aura-000002` is a Commitment Purchase. It is the only row where the Contract Commitment columns are populated, and they are populated together: a one-year term, an all-upfront payment model, and a resource reservation. Commitment Discount Category records that the proposed commitment is usage-based, and Recommendation Details sizes it at 70,080 instance-hours, being eight reserved instances across the 8,760 hours of the one-year term. It has no Resource ID, because the proposal applies to a service rather than to one resource, so Resource Name and Resource Type are also null.
* `rec-aura-000003` is an Idle Resource Removal. Resource Configuration Details Current describes the volume to be deleted, while Resource Configuration Details Recommended is null because no target state exists once the resource is removed. Recommendation Details records zero disk operations across the evaluation period, which is the evidence for the proposal.
* `rec-aura-000005` is a Modernization proposal with a Recommendation Status of "Implemented", showing that acted-upon recommendations remain in the dataset rather than disappearing from it. Recommendation Details identifies the proposed SKU using the FOCUS-defined "SkuId" and "SkuPriceId" keys, which name a catalog offering rather than the resource configuration held in Resource Configuration Details Recommended.

### Recommendations Beyond Cost

Four recommendations address domains other than cost, which is why Estimated Monthly Cost Impact is not populated on all of them.

Note the following details in the example dataset:

* `rec-beacon-000101` is a Security proposal with a Recommendation Status of "Deferred", representing a finding that has been reviewed and accepted as valid but scheduled for later action. Resource Configuration Details Current and Resource Configuration Details Recommended carry the access level before and after the change, so the proposal states the target state rather than only the problem. Recommendation Details carries the count of exposed objects as supporting evidence, using a custom "x_" prefixed key because a public access finding has no FOCUS-defined equivalent.
* `rec-aura-000004` is a Reliability proposal that *increases* cost. Estimated Monthly Cost Impact is a positive value, because the column is signed and expresses a change in effective cost rather than a saving.
* `rec-beacon-000102` is a Performance proposal produced by Budget Beacon against an Aura Web resource. Recommendation Provider Name and Service Provider Name therefore hold different values.
* `rec-beacon-000103` is an Operational Excellence proposal naming the single virtual machine that is missing required tags, rather than reporting that tagging is incomplete somewhere in the environment. Recommendation Details names the tag keys that are absent and the policy that requires them, so the finding can be acted on without a separate investigation to determine which resource is affected.

### Evaluation Periods

Evaluation Period Start and Evaluation Period End record the period a recommendation was derived from, which lets a reviewer judge how much observation supports a proposal.

Note the following details in the example dataset:

* `rec-aura-000001`, `rec-aura-000002`, and `rec-aura-000003` are each derived from a 30-day period, the window Aura Web evaluates. `rec-beacon-000102` is derived from a 14-day period, showing that two generators analyzing the same environment may evaluate different windows.
* `rec-aura-000002` has an Evaluation Period End of '2026-07-01T00:00:00Z' but a Recommendation Created of '2026-07-05T00:00:00Z', showing that a generator may evaluate through the end of a prior period rather than through the moment the recommendation is generated. Elsewhere the two coincide.
* Evaluation Period End is an *exclusive end bound*, so a period ending '2026-07-01T00:00:00Z' includes behavior observed through June 30 but nothing observed on July 1.

### Null Handling in Practice

The example is constructed to exercise the conditional nullability rules defined on the individual columns.

Note the following details in the example dataset:

* Currency and Estimated Monthly Cost Impact are always both populated or both null. The three recommendations with no monetary estimate carry no currency, because a currency without an amount conveys nothing.
* Every recommendation with a Recommendation Category of "Cost" carries an Estimated Monthly Cost Impact. Recommendations in other categories may omit it.
* `rec-beacon-000102` has no Billing Account ID. A third-party generator can identify the resource to optimize without necessarily having access to the billing account under which it is billed, so Billing Account ID and Billing Account Name are both null.
* Recommendation Subcategory always resolves to exactly one parent Recommendation Category. Categories without a specific subcategory defined use their own catch-all value, such as "Other (Security)".
* Resource Name and Resource Type are null wherever Resource ID is null, and Region Name is null wherever Region ID is null.
* Recommendation Details is null only for `rec-aura-000004`, where Resource Configuration Details Current and Resource Configuration Details Recommended already convey the proposed change in full and no supporting detail remains to record. The column is mandatory, so it is present in every row even where its value is null.
* Evaluation Period Start and Evaluation Period End are either both populated or both null. They are null for the four recommendations derived from the configuration of a resource rather than from behavior observed over time, such as `rec-beacon-000101`, which reports a bucket that is currently readable by anonymous principals.
* Commitment Discount Category is populated only for `rec-aura-000002`, alongside the other Contract Commitment columns, and is null wherever a recommendation does not propose the purchase of a contract commitment.
