# Examples: AI Processing Tier

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) uses the FOCUS-defined [SKU Price Details](#datamodel.costandusage.skupricedetails) property ProcessingTier to distinguish the prices a [*service provider*](#glossary:service-provider) charges for the same [*AI model*](#glossary:ai-model) at different processing tiers. Provider and model names below are illustrative.

*Service providers* commonly price the same model at more than one processing tier. A "Batch" price for work submitted as an asynchronous job is typically half the "Standard" price, a "Flex" price for latency-tolerant synchronous work may carry a similar discount, and a "Priority" price for work served ahead of "Standard" carries a premium. Each tier is metered on its own [*SKU*](#glossary:sku), but the tier appears only in *service-provider*-specific [SKU Meter](#datamodel.costandusage.skumeter) names, SKU identifiers, or API endpoint names. ProcessingTier carries the tier as a common value, so a practitioner can group spend by tier, quantify the price difference between tiers for one model, and identify "Standard" spend that could move to a cheaper tier, without matching on *service-provider*-specific text.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp runs workloads on the same foundation model, Solora Reasoning Pro, through two *service providers*.
* Each *service provider* prices the model at more than one processing tier, and each tier is a distinct *SKU* with its own [SKU ID](#datamodel.costandusage.skuid) and [SKU Price ID](#datamodel.costandusage.skupriceid), so the price difference between tiers is visible as a difference in [List Unit Price](#datamodel.costandusage.listunitprice) across rows.
* Acme Corp pays list price, so [List Cost](#datamodel.costandusage.listcost), [Contracted Cost](#datamodel.costandusage.contractedcost), [Billed Cost](#datamodel.costandusage.billedcost), and [Effective Cost](#datamodel.costandusage.effectivecost) are equal on every row.
* Every tier is a predetermined rate, so [Pricing Category](#datamodel.costandusage.pricingcategory) is "Standard" on every row, including the "Priority", "Flex", and "Batch" rows.

> **Note:** The FOCUS-defined SKU Price Details properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Standard and Batch Pricing of the Same Model

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI, which prices two processing tiers:

* "Standard" processing is priced at $3.00 per 1,000,000 input tokens and $15.00 per 1,000,000 output tokens.
* "Batch" processing, for jobs completed within 24 hours, is priced at half the "Standard" price, at $1.50 and $7.50 respectively.
* An interactive workload consumes 6,000,000 input tokens and 1,000,000 output tokens at "Standard". A nightly document classification job consumes 20,000,000 input tokens and 4,000,000 output tokens at "Batch".

[**CSV Example**](/specification/data/ai_processing_tier/ai_processing_tier_a.csv)

Note the following details in the example dataset:

* ProcessingTier carries "Standard" on two rows and "Batch" on the other two, and the model identity properties are identical across all four rows because every row describes the same model. Grouping by ProcessingTier therefore isolates the cost of each tier for one model: $33.00 at "Standard" and $60.00 at "Batch", for a total of $93.00.
* ProcessingTier is orthogonal to TokenDirection and TokenCacheAction. Each tier is split into input and output *SKUs*, so four rows describe one model at two tiers, and the input rows carry TokenCacheAction "Uncached" as they do in [Examples: AI Prompt Caching](#appendix.examples:aipromptcaching).
* The price difference between tiers is carried as a difference in List Unit Price between rows, not as a multiplier. Running the batch job at "Standard" would have cost 20.0 x $3.00 + 4.0 x $15.00 = $120.00, so the "Batch" tier saved $60.00 on that job.
* The same rows support the optimization question in reverse. The "Standard" rows hold $33.00 of spend; were that workload latency-tolerant, the same volume at "Batch" would cost 6.0 x $1.50 + 1.0 x $7.50 = $16.50, a reduction of $16.50. Whether it can move is a workload decision, but ProcessingTier is what identifies the spend to evaluate.

## Scenario B: Four Processing Tiers on a Cloud Provider

For this scenario, the same model is served by a cloud provider, LatticeScale, which prices four processing tiers for input tokens:

* "Standard" processing is priced at $3.00 per 1,000,000 input tokens, "Priority" at a 1.8x premium of $5.40, and both "Flex" and "Batch" at a 50% discount of $1.50.
* Acme Corp submits 2,500,000 input tokens at "Priority". LatticeScale serves 2,000,000 of them at "Priority" and, lacking spare priority capacity, serves and bills the remaining 500,000 at its "Standard" price. A further 4,500,000 input tokens are submitted at "Standard", 8,000,000 at "Flex", and 10,000,000 as a "Batch" job.
* Only input tokens are shown, since the input and output split is already illustrated in Scenario A.
* A fifth row covers a second model, Solora Reasoning Lite, which LatticeScale prices at a single processing tier.

[**CSV Example**](/specification/data/ai_processing_tier/ai_processing_tier_b.csv)

Note the following details in the example dataset:

* The SKU Meter values ("Input Tokens", "Priority Input Tokens", "Flex Input Tokens", and "Batch Prediction Input Tokens") are specific to this *service provider*, and the "Batch" meter does not match the "Batch Input Tokens" meter Solora AI uses in Scenario A. ProcessingTier carries "Batch" on both, so a query selects batch spend across both *service providers* without matching on SKU Meter text.
* The "Flex" and "Batch" rows share a List Unit Price of $1.50 but describe different tiers. Unit price alone cannot separate them, and ProcessingTier can.
* The "Standard" row holds 5,000,000 tokens: the 4,500,000 submitted at "Standard" and the 500,000 submitted at "Priority" that LatticeScale billed at its "Standard" price. ProcessingTier identifies the tier at which each [*SKU Price*](#glossary:sku-price) applies, not the tier requested, so the "Priority" row holds only the 2,000,000 tokens billed at the premium.
* The "Priority" premium on this workload is 2.0 x ($5.40 - $3.00) = $4.80, the figure a practitioner weighs against the latency benefit of the tier.
* The Solora Reasoning Lite row carries no ProcessingTier, because LatticeScale prices that model at a single tier. It is not a "Standard" charge; it is a charge to which the tier distinction does not apply. Measuring the share of spend at each tier counts it as unclassified, which is why the four tiered rows sum to $52.80 against a scenario total of $55.80.
* Comparing the two scenarios, "Standard" input tokens for the same model cost $3.00 per 1,000,000 on both *service providers*, and "Batch" input tokens cost $1.50 on both. ProcessingTier establishes that the rows describe the same tier, and the shared model identity properties establish that they describe the same model, so neither fact requires interpreting a *service-provider*-specific SKU identifier.
