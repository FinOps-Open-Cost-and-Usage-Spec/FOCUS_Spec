# Examples: AI Model Identity

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) represents the identity of an [*AI model*](#glossary:ai-model) using FOCUS-defined [SKU Price Details](#datamodel.costandusage.skupricedetails) properties. They also demonstrate how the TokenDirection property labels the structural split between input (i.e., prompt) and output (i.e., generated) [*tokens*](#glossary:token). Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token AI model API to run a workload.
* The model is priced separately for input and output tokens, denominated per 1,000,000 tokens.
* The model identity (developer, family, identifier, and version) is stable for a given [*SKU Price*](#glossary:sku-price), so it is carried in SKU Price Details.

> **Note:** The FOCUS-defined SKU Price Details properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: AI Model Purchased Directly

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI:

* Input tokens are priced at $3.00 per 1,000,000 tokens, and output tokens at $15.00 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 5,000,000 input tokens and 1,500,000 output tokens.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_a.csv)

Note the following details in the example dataset:

* Model identity is carried in SKU Price Details using the FOCUS-defined properties ModelDeveloper, ModelFamily, ModelId, and ModelVersion. These values are common to both rows because both describe the same model.
* The split between input and output tokens is structural. Each is a separate [*SKU*](#glossary:sku) with distinct [SKU ID](#datamodel.costandusage.skuid), [SKU Price ID](#datamodel.costandusage.skupriceid), and [SKU Meter](#datamodel.costandusage.skumeter) values. TokenDirection (i.e., "Input" or "Output") normalizes this split so rows can be grouped regardless of meter names. TokenCacheAction is "Uncached" on the input row, as Solora AI meters cache interactions separately (see [Examples: AI Prompt Caching](#appendix.examples:aipromptcaching)), and is absent from the output row.
* [Consumed Quantity](#datamodel.costandusage.consumedquantity) holds the raw token count and [Consumed Unit](#datamodel.costandusage.consumedunit) is "Tokens", while [Pricing Quantity](#datamodel.costandusage.pricingquantity) holds the priced volume and [Pricing Unit](#datamodel.costandusage.pricingunit) is "1000000 Tokens".
* Because Acme Corp pays the list price, [List Unit Price](#datamodel.costandusage.listunitprice) and [Contracted Unit Price](#datamodel.costandusage.contractedunitprice) are equal, so [List Cost](#datamodel.costandusage.listcost), [Contracted Cost](#datamodel.costandusage.contractedcost), [Billed Cost](#datamodel.costandusage.billedcost), and [Effective Cost](#datamodel.costandusage.effectivecost) are equal.

## Scenario B: Same Model Served by a Cloud Provider

For this scenario, the same underlying model is served by a cloud provider, LatticeScale, as its own first-party [*service*](#glossary:service):

* Every participating entity ([Service Provider Name](#datamodel.costandusage.serviceprovidername), [Host Provider Name](#datamodel.costandusage.hostprovidername), and [Invoice Issuer Name](#datamodel.costandusage.invoiceissuername)) is LatticeScale, the [*service provider*](#glossary:service-provider).
* The model developer, Solora AI, is not the *service provider*, and is carried in the ModelDeveloper property.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_b.csv)

Note the following details in the example dataset:

* ModelDeveloper ("Solora AI") differs from Service Provider Name ("LatticeScale"). The model developer is not represented by any existing participating-entity column, which is why model identity is carried as its own property.
* The served ModelId is namespaced by the *service provider* ("latticescale.solora-reasoning-pro"), so the other model-identity properties (ModelDeveloper, ModelFamily, and ModelVersion) are what associate the charge with the underlying model across *service providers*.
* As in Scenario A, TokenDirection labels the structural split, and model identity is common to both rows. The input row carries no TokenCacheAction because LatticeScale bills tokens placed into a cache on its ordinary input meter.
