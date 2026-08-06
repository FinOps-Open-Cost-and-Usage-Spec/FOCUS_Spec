# Examples: AI Prompt Caching

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) distinguishes cached from uncached token [*charges*](#glossary:charge) using the FOCUS-defined [SkuPriceDetails](#datamodel.costandusage.skupricedetails) property CacheRole, and how charges for retaining cached content over time remain a separate metered operation. Provider and model names below are illustrative.

Prompt caching lets a workload reuse previously processed input content across requests. *Service providers* meter this differently from one another. Some charge for placing content into a cache, some do not. Some charge separately for retaining it, some price retention into another charge. Where a charge exists, it typically appears as its own [SkuMeter](#datamodel.costandusage.skumeter), but the wording of that meter varies across *service providers* and is not drawn from a defined value set. CacheRole identifies the role a [*SKU Price*](#glossary:sku-price) plays in the cache lifecycle independently of how a given *service provider* names or structures its meters, so that cached and uncached charges can be compared across a multi-provider [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token foundation model API to run a generative AI workload with a large reusable prompt prefix.
* During the [*charge period*](#glossary:chargeperiod), the workload processes 500,000 input tokens that are not cached, places 2,000,000 input tokens into the cache, reads 8,000,000 input tokens from the cache, and generates 1,500,000 output tokens.
* Input tokens are priced at $3.00 per 1,000,000 tokens and output tokens at $15.00 per 1,000,000 tokens.
* Cache reads are priced at $0.30 per 1,000,000 tokens, a tenth of the input price.

Both scenarios describe the same workload so that the two pricing structures can be compared directly.

> **Note:** The FOCUS-defined SkuPriceDetails properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Cache Writes Charged Separately

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI, which charges for cache writes and prices cache retention into that charge:

* Cache writes are priced at $3.75 per 1,000,000 tokens, a premium over the $3.00 input price.
* No separate charge applies for retaining cached content.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_a.csv)

Note the following details in the example dataset:

* Each token type is its own [*SKU*](#glossary:sku), with its own [SkuId](#datamodel.costandusage.skuid), [SkuPriceId](#datamodel.costandusage.skupriceid), and SkuMeter. The three input-side rows are distinguished structurally by SkuMeter values of "Input Tokens", "Cache Write Input Tokens", and "Cache Read Input Tokens".
* CacheRole does not create that distinction; it normalizes it. The property carries "Uncached", "Write", and "Read" on those same three rows, so a query can select cache reads without matching on the SkuMeter text.
* The uncached row carries CacheRole "Uncached" explicitly rather than omitting the property. Omission would be indistinguishable from a *service provider* that does not offer caching at all.
* The output row omits CacheRole because the property is not applicable to generated tokens, consistent with the SkuPriceDetails requirement that properties not applicable to the corresponding SkuPriceId are excluded.
* Model identity properties are common to all four rows because all four describe the same model.
* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) holds the raw token count and [ConsumedUnit](#datamodel.costandusage.consumedunit) is "Tokens", while [PricingQuantity](#datamodel.costandusage.pricingquantity) holds the priced volume and [PricingUnit](#datamodel.costandusage.pricingunit) is "1000000 Tokens".

Identifying the cache write separately supports a return-on-investment analysis:

* Without caching, the same 10,500,000 input tokens would cost 10.5 x $3.00 = $31.50.
* With caching, the input-side charges total $1.50 + $7.50 + $2.40 = $11.40, a reduction of $20.10.
* The incremental cost of populating the cache is 2.0 x ($3.75 - $3.00) = $1.50, the premium paid over uncached processing.
* The cache therefore returns $20.10 for $1.50 of incremental investment.

## Scenario B: Cache Storage Charged Separately

For this scenario, the same model is served by a cloud provider, LatticeScale, which applies no cache write charge and instead charges for retaining cached content:

* Tokens placed into the cache are charged at the ordinary $3.00 input price, on the same meter as input tokens that are not cached.
* Retained content is charged at $1.00 per 1,000,000 token-hours. The 2,000,000 cached tokens are retained for 3 hours, producing 6,000,000 token-hours.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_b.csv)

Note the following details in the example dataset:

* The SkuMeter wording differs from Scenario A for the same conceptual charge. Cache reads appear on a meter named "Cached Input Tokens" here and "Cache Read Input Tokens" in Scenario A, while both rows carry CacheRole "Read". Matching on CacheRole selects both; matching on SkuMeter text selects neither consistently.
* No row carries CacheRole "Write". This *service provider* does not price cache writes, so no *SKU Price* holds that role, and the property is omitted rather than applied to a charge that does not exist.
* The "Input Tokens" row covers 2,500,000 tokens, comprising both the tokens that populated the cache and those processed without caching. The *service provider* does not meter them separately, so the dataset cannot separate them either. The cost of populating the cache is not separable on this *service provider*, which is a property of its billing model rather than of the dataset.
* The context cache storage row has its own SkuId and a SkuMeter value of "Context Cache Storage", and omits CacheRole. Retaining content over time is a different metered operation from processing tokens, so it is identified structurally rather than by this property.
* The context cache storage row is denominated in token-hours, so ConsumedUnit is "Token-Hours" and PricingUnit is "1000000 Token-Hours", both conforming to [UnitFormat](#attributes.unitformat) compound unit requirements.

The same analysis applied to this scenario yields a different result:

* Without caching, the same 10,500,000 input tokens would cost $31.50.
* With caching, the input-side charges total $7.50 + $2.40 = $9.90, plus $6.00 of context cache storage, for $15.90 in total.
* Because cache writes carry no premium, the entire cost of populating and retaining the cache is the $6.00 storage charge.
* The cache therefore returns $15.60 for $6.00 of investment.

> **Note:** Comparing only the cache-related meters across these two scenarios would be misleading. Solora AI recovers retention cost through a $7.50 cache write charge and LatticeScale through a $6.00 storage charge, so the comparable quantity across *service providers* is the sum of any cache write charge and any cache storage charge, not either one alone.
