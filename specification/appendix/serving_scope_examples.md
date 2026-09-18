# Examples: Serving Scope

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) distinguishes serving that is routed across a broad geographic area from serving that is pinned to a narrower one, using the FOCUS-defined ServingScope property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails). Provider, model, and region names below are illustrative.

Serving scope is a property of the [*SKU Price*](#glossary:sku-price) rather than of the individual charge, because a [*service provider*](#glossary:service-provider) prices each scope separately. The dimension is not specific to AI; the same distinction applies wherever a *service provider* offers the same capability at more than one geographic breadth. AI model serving is where *service providers* price it most distinctly today, which is why both scenarios below use AI [*SKUs*](#glossary:sku). Other offerings that vary geographic breadth commonly bundle it with replication, which the Redundancy property describes instead.

In the scenarios below, ServingScope appears only on rows for a capability the *service provider* prices at more than one serving scope. An absent ServingScope does not indicate that a [*charge*](#glossary:charge) was globally routed, so an analysis measuring the share of spend at a given scope treats rows without ServingScope as unclassified rather than folding them into either scope.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp runs the same foundation model, Solora Reasoning Pro, on two *service providers*.
* Each *service provider* offers the model at more than one serving scope, and prices each scope separately.
* Each serving scope is a distinct *SKU* with its own [SkuId](#datamodel.costandusage.skuid) and [SkuPriceId](#datamodel.costandusage.skupriceid), so the price difference between scopes is visible as a difference in [ListUnitPrice](#datamodel.costandusage.listunitprice) across rows.
* Acme Corp pays list price, so [ListCost](#datamodel.costandusage.listcost), [ContractedCost](#datamodel.costandusage.contractedcost), [BilledCost](#datamodel.costandusage.billedcost), and [EffectiveCost](#datamodel.costandusage.effectivecost) are equal on every row.

> **Note:** The SkuPriceDetails properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Global and Region-Pinned Serving of the Same Model

For this scenario, Acme Corp runs the model on Aura Web under two serving scopes during the same [*charge period*](#glossary:chargeperiod):

* Globally routed serving is priced at $2.50 per 1,000,000 input tokens and $12.50 per 1,000,000 output tokens.
* Region-pinned serving of the same model is priced 20% higher, at $3.00 and $15.00 respectively.
* The globally routed workload consumes 4,000,000 input tokens and 1,000,000 output tokens. The region-pinned workload consumes 2,000,000 input tokens and 500,000 output tokens.

[**CSV Example**](/specification/data/serving_scope/serving_scope_a.csv)

Note the following details in the example dataset:

* ServingScope carries the routing breadth ("Global" or "Regional"), and the model-identity properties are identical across all four rows because every row describes the same model. Grouping by ServingScope therefore isolates the cost of each scope for one model.
* [RegionId](#datamodel.costandusage.regionid) and ServingScope answer different questions. The region-pinned rows carry a RegionId of "us-east-1", while the globally routed rows carry no RegionId, because those requests are not served from a distinct region.
* A null RegionId on its own does not identify globally routed serving. RegionId is also null for [*services*](#glossary:service) that are simply not regionalized, so ServingScope is what separates the two cases.
* The price difference between scopes is carried as a difference in ListUnitPrice between rows, not as a multiplier or formula. Region pinning costs $0.50 more per 1,000,000 input tokens here, which is the figure a practitioner weighs against the governance or latency benefit of pinning.
* The input and output split remains structural, as established for model identity: each is a separate *SKU* distinguished by [SkuMeter](#datamodel.costandusage.skumeter). Serving scope multiplies against that split rather than replacing it, which is why four rows describe one model.

## Scenario B: Three Serving Scopes on a Second Service Provider

For this scenario, the same model is served by CrestNode, which offers a third scope between global and regional: a data zone that keeps serving within a named group of regions.

* Global deployment is priced at $2.40 per 1,000,000 input tokens, data zone deployment 10% higher at $2.64, and regional deployment 20% higher at $2.88.
* Only input tokens are shown, since the input and output split is already illustrated in Scenario A.
* A fourth row covers a second model, Solora Reasoning Lite, which CrestNode offers at a single serving scope and therefore prices without a scope distinction.

[**CSV Example**](/specification/data/serving_scope/serving_scope_b.csv)

Note the following details in the example dataset:

* The SkuMeter values ("Glbl Std Inp Tokens", "DZ Std Inp Tokens", and "Rgnl Std Inp Tokens") are abbreviated in a way specific to this *service provider*, and they do not match the meter names Aura Web uses in Scenario A. SkuMeter has no FOCUS-defined value set, so it cannot be matched across *service providers*. ServingScope is what makes the serving scopes comparable across the two datasets.
* "DataZone" shows that the value set is not limited to the global and regional pair. A data zone is narrower than global serving and broader than a single region.
* The data zone row carries a RegionId of "eu", a macro-region CrestNode publishes as an identifier, while the regional row carries "westeurope". The global row carries none, because CrestNode publishes no identifier for the area global routing draws on. Both "eu" and "westeurope" are region identifiers; the ServingScope value is what distinguishes a price that applies across the whole data zone from one pinned to a single region.
* The Solora Reasoning Lite row carries no ServingScope, because CrestNode prices that model without a scope distinction. It is not a globally routed charge; it is a charge to which the scope distinction does not apply. Measuring the share of spend at each scope counts it as unclassified rather than assigning it to a scope, which is why the three scoped rows sum to $48.48 against a scenario total of $51.48.
* Comparing the two scenarios, globally routed serving of the same model costs $2.50 per 1,000,000 input tokens on Aura Web and $2.40 on CrestNode. ServingScope establishes that both rows describe global serving, and the model-identity properties establish that both describe the same model, so neither fact requires interpreting a *service-provider*-specific *SKU* identifier. Pairing the rows as input token prices relies on SkuMeter, which carries the metered dimension as *service-provider*-specific text; a FOCUS-defined property for that dimension would remove the remaining interpretation step from this comparison.
