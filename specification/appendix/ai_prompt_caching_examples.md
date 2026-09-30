# Examples: AI Prompt Caching

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) uses the FOCUS-defined [SKU Price Details](#datamodel.costandusage.skupricedetails) properties TokenCacheAction and TokenDirection to distinguish cached from uncached [*token*](#glossary:token) [*charges*](#glossary:charge). They also show how charges for retaining cached content over time remain a separate metered operation. Provider and model names below are illustrative.

[*Service providers*](#glossary:service-provider) meter [*prompt cache*](#glossary:prompt-cache) interactions inconsistently. Some charge to place content into a cache and some do not. Some charge separately to retain it, while others price retention into another charge. Because cache-related [SKU Meter](#datamodel.costandusage.skumeter) names vary widely across *service providers*, TokenCacheAction and TokenDirection normalize this billing data. They identify the specific cache interaction and token direction (input or output) independently of the meter name. This allows practitioners to compute metrics such as cache hit rates and input-to-output ratios across a multi-provider *FOCUS dataset* (see [Resource Usage](#supportedfeatures.resourceusage)).

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token foundation model API to run a generative AI workload with a large reusable prompt prefix.
* During the [*charge period*](#glossary:chargeperiod), the workload processes 500,000 input tokens that are not cached, places 2,000,000 input tokens into the cache, reads 8,000,000 input tokens from the cache, and generates 1,500,000 output tokens.
* Input tokens are priced at $3.00 per 1,000,000 tokens and output tokens at $15.00 per 1,000,000 tokens.
* Cache reads are priced at $0.30 per 1,000,000 tokens, a tenth of the input price.

Both scenarios describe the same workload so that the two pricing structures can be compared directly.

> **Note:** The FOCUS-defined SKU Price Details properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Cache Writes Charged Separately

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI, which charges for cache writes and prices cache retention into that charge:

* Cache writes are priced at $3.75 per 1,000,000 tokens, a premium over the $3.00 input price.
* No separate charge applies for retaining cached content.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_a.csv)

Note the following details in the example dataset:

* Each kind of token is its own [*SKU*](#glossary:sku), with its own [SKU ID](#datamodel.costandusage.skuid), [SKU Price ID](#datamodel.costandusage.skupriceid), and SKU Meter. The three input-side rows are distinguished structurally by SKU Meter values of "Input Tokens", "Cache Write Input Tokens", and "Cache Read Input Tokens".
* TokenCacheAction does not create that distinction; it normalizes it. The property carries "Uncached", "Write", and "Read" on those same three rows, and TokenDirection carries "Input" on all three, so a query can select cache reads, or every input token, without matching on the SKU Meter text.
* Every input token row carries both properties. The output row carries TokenDirection "Output" and no TokenCacheAction, because a cache interaction is a property of tokens consumed from a request, so grouping the input rows by TokenCacheAction produces a breakdown that sums to the total input token cost.
* The "Input Tokens" row carries TokenCacheAction "Uncached" because Solora AI meters cache reads and cache writes as their own charges, so that row holds only the 500,000 input tokens that were neither served from nor placed into the cache. Each token is counted on one row.
* Model identity properties are common to all four rows because all four describe the same model.
* [Consumed Quantity](#datamodel.costandusage.consumedquantity) holds the raw token count and [Consumed Unit](#datamodel.costandusage.consumedunit) is "Tokens", while [Pricing Quantity](#datamodel.costandusage.pricingquantity) holds the priced volume and [Pricing Unit](#datamodel.costandusage.pricingunit) is "1000000 Tokens".

Identifying the cache write separately supports a return-on-investment analysis:

* Without caching, the same 10,500,000 input tokens would cost 10.5 x $3.00 = $31.50.
* With caching, the input-side charges total $1.50 + $7.50 + $2.40 = $11.40, a reduction of $20.10.
* The incremental cost of populating the cache is 2.0 x ($3.75 - $3.00) = $1.50, the premium paid over uncached processing.
* The cache therefore returns $20.10 for $1.50 of incremental investment.

## Scenario B: Cache Storage Charged Separately

For this scenario, the same model is served by a cloud provider, LatticeScale, which applies no cache write charge and instead charges for retaining cached content:

* Tokens placed into the cache are charged at the ordinary $3.00 input price, on the same meter as input tokens that are not cached.
* Retained content is charged at $1.00 per 1,000,000 token-hours. The 2,000,000 cached tokens are retained for three hours, producing 6,000,000 token-hours.

[**CSV Example**](/specification/data/ai_prompt_caching/ai_prompt_caching_b.csv)

Note the following details in the example dataset:

* The SKU Meter wording differs from Scenario A for the same conceptual charge. Cache reads appear on a meter named "Cached Input Tokens" here and "Cache Read Input Tokens" in Scenario A, while both rows carry TokenCacheAction "Read". Matching on TokenCacheAction selects both; matching on SKU Meter text selects neither consistently.
* No row carries TokenCacheAction "Write". This *service provider* does not meter cache writes as their own charge, so no [*SKU Price*](#glossary:sku-price) holds that value.
* The "Input Tokens" row covers 2,500,000 tokens, comprising both the tokens that populated the cache and those processed without caching. The *service provider* does not meter them separately, so the dataset cannot separate them either. The row carries no TokenCacheAction, because "Uncached" would describe the 2,000,000 tokens that populated the cache as uncached, and TokenDirection "Input" still identifies its tokens as input. The cost of populating the cache is not separable on this *service provider*, which is a property of its billing model rather than of the dataset.
* The context cache storage row has its own SKU ID and a SKU Meter value of "Context Cache Storage", and carries neither TokenCacheAction nor TokenDirection. It is denominated in token-hours rather than tokens, so neither property applies to it.
* The context cache storage row conforms to [Unit Format](#attributes.unitformat) compound unit requirements, with Consumed Unit "Token-Hours" and Pricing Unit "1000000 Token-Hours".

The same analysis applied to this scenario yields a different result:

* Without caching, the same 10,500,000 input tokens would cost $31.50.
* With caching, the input-side charges total $7.50 + $2.40 = $9.90, plus $6.00 of context cache storage, for $15.90 in total.
* Because cache writes carry no premium, the entire cost of populating and retaining the cache is the $6.00 storage charge.
* The cache therefore returns $15.60 for $6.00 of investment.

> **Note:** Comparing only the cache-related meters across these two scenarios would be misleading. The $7.50 cache write charge in Scenario A covers the ordinary processing of those 2,000,000 tokens along with the caching premium, while Scenario B bills that same processing on its input meter and charges $6.00 for retention separately. The comparable quantity across *service providers* is therefore the total input-side cost, $11.40 against $15.90, rather than any single cache-related meter.
