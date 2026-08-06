# Examples: AI Prompt Caching

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) distinguishes cached from uncached token [*charges*](#glossary:charge) using the FOCUS-defined [SkuPriceDetails](#datamodel.costandusage.skupricedetails) property CacheRole, and how charges for retaining cached content over time remain a separate metered operation. Provider and model names below are illustrative.

Prompt caching lets a workload reuse previously processed input content across requests. Service providers commonly price this as three distinct price points for the same metered operation: processing input without a cache, placing input into a cache, and serving input from a cache. Because these are the same functionality at different prices, they share a [SkuId](#datamodel.costandusage.skuid) and are distinguished by [SkuPriceId](#datamodel.costandusage.skupriceid), which is the case SkuPriceDetails exists to serve.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token foundation model API to run a generative AI workload with a large reusable prompt prefix.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 500,000 uncached input tokens, writes 2,000,000 input tokens to the cache, reads 8,000,000 input tokens from the cache, and generates 1,500,000 output tokens.
* Uncached input tokens are priced at $3.00 per 1,000,000 tokens and output tokens at $15.00 per 1,000,000 tokens.
* Cache reads are priced at $0.30 per 1,000,000 tokens, a tenth of the uncached input price.

Both scenarios use identical token volumes so that the two pricing structures can be compared directly.

> **Note:** The FOCUS-defined SkuPriceDetails properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Cache Retention Priced Into the Write

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI, which prices cache retention into the write rather than charging for cache storage separately:

* Cache writes are priced at $3.75 per 1,000,000 tokens, a premium over the $3.00 uncached input price.
* No separate charge applies for holding cached content.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_a.csv)

Note the following details in the example dataset:

* The three input-side rows share a single SkuId ("solora-reasoning-pro-input") and a single [SkuMeter](#datamodel.costandusage.skumeter) value ("Input Tokens") because they meter the same operation. They carry distinct SkuPriceId values and distinct CacheRole values of "Uncached", "Write", and "Read".
* The uncached row carries CacheRole "Uncached" explicitly rather than omitting the property. Omission would be indistinguishable from a *service provider* that does not offer caching at all.
* The output row omits CacheRole because the property is not applicable to generated tokens, consistent with the SkuPriceDetails requirement that properties not applicable to the corresponding SkuPriceId are excluded.
* The split between input and output tokens remains structural, carried by separate SkuId and SkuMeter values rather than by a property. Consuming a prompt and generating a completion are different metered operations.
* Model identity properties are common to all four rows because all four describe the same model.
* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) holds the raw token count and [ConsumedUnit](#datamodel.costandusage.consumedunit) is "Tokens", while [PricingQuantity](#datamodel.costandusage.pricingquantity) holds the priced volume and [PricingUnit](#datamodel.costandusage.pricingunit) is "1000000 Tokens".

Identifying the three price points separately supports a return-on-investment analysis of the cache:

* Without caching, the same 10,500,000 input tokens would cost 10.5 x $3.00 = $31.50.
* With caching, the input-side charges total $1.50 + $7.50 + $2.40 = $11.40, a reduction of $20.10.
* The incremental cost of populating the cache is 2.0 x ($3.75 - $3.00) = $1.50, the premium paid over uncached processing.
* The cache therefore returns $20.10 for $1.50 of incremental investment.

Computing the reduction requires only the cache read rows. Computing the return also requires the cache write rows to be identifiable, which is what CacheRole provides.

## Scenario B: Cache Storage Charged Separately

For this scenario, the same model is served by a cloud provider, LatticeScale, which applies no cache write premium and instead charges for holding cached content over time:

* Cache writes are priced at $3.00 per 1,000,000 tokens, the same as uncached input.
* Cached content is charged at $1.00 per 1,000,000 token-hours. The 2,000,000 cached tokens are held for 3 hours, producing 6,000,000 token-hours.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_b.csv)

Note the following details in the example dataset:

* The cache storage row has its own SkuId and a SkuMeter value of "Cache Storage", and omits CacheRole. Holding content over time is different functionality from processing tokens, so it is carried structurally rather than as a price-point property.
* The cache storage row is denominated in token-hours, so ConsumedUnit is "Token-Hours" and PricingUnit is "1000000 Token-Hours", both conforming to [UnitFormat](#attributes.unitformat) compound unit requirements.
* The three input-side rows carry the same CacheRole values as Scenario A even though the underlying price structure differs, which is what makes the two datasets comparable.

The same analysis applied to this scenario yields a different result:

* Without caching, the same 10,500,000 input tokens would cost $31.50.
* With caching, the input-side charges total $1.50 + $6.00 + $2.40 = $9.90, plus $6.00 of cache storage, for $15.90 in total.
* The cache write carries no premium, so the entire cost of populating and holding the cache is the $6.00 storage charge.
* The cache therefore returns $15.60 for $6.00 of investment.

> **Note:** Comparing only the cache write rows across these two scenarios would be misleading. Solora AI recovers retention cost through a $7.50 write charge and LatticeScale through a $6.00 storage charge, so the comparable quantity across *service providers* is the sum of the cache write premium and any cache storage charge, not the write row alone.
