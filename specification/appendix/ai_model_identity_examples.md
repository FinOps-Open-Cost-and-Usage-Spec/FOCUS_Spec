# Examples: AI Model Identity

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) represents the identity of an AI model using FOCUS-defined [SkuPriceDetails](#datasets.costandusage.skupricedetails) properties, and how the split between input (prompt) and output (generated) tokens is carried structurally rather than through a dedicated property. Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token foundation model API to run a generative AI workload.
* The model is priced separately for input and output tokens, denominated per 1,000,000 tokens.
* The model identity (provider, family, identifier, variant, and version) is stable for a given [*SKU Price*](#glossary:sku-price), so it is carried in SkuPriceDetails.

## Scenario A: Foundation Model Purchased Directly

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI:

* Input tokens are priced at $3.00 per 1,000,000 tokens, and output tokens at $15.00 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 5,000,000 input tokens and 1,500,000 output tokens.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_a.csv)

Note the following details in the example dataset:

* Model identity is carried in SkuPriceDetails using the FOCUS-defined properties ModelDeveloper, ModelFamily, ModelId, ModelVariant, and ModelVersion. These values are common to both rows because both describe the same model.
* The split between input and output tokens is structural. Each is a separate [*SKU*](#glossary:sku) with its own [SkuId](#datasets.costandusage.skuid) and [SkuPriceId](#datasets.costandusage.skupriceid), distinguished by [SkuMeter](#datasets.costandusage.skumeter) values of "Input Tokens" and "Output Tokens". No separate token-type property is used.
* [ConsumedQuantity](#datasets.costandusage.consumedquantity) holds the raw token count and [ConsumedUnit](#datasets.costandusage.consumedunit) is "Tokens", while [PricingQuantity](#datasets.costandusage.pricingquantity) holds the priced volume and [PricingUnit](#datasets.costandusage.pricingunit) is "1000000 Tokens".
* Because Acme Corp pays the list price, [ListUnitPrice](#datasets.costandusage.listunitprice) and [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) are equal, so [ListCost](#datasets.costandusage.listcost), [ContractedCost](#datasets.costandusage.contractedcost), [BilledCost](#datasets.costandusage.billedcost), and [EffectiveCost](#datasets.costandusage.effectivecost) are equal.

## Scenario B: Same Model Served by a Cloud Provider

For this scenario, the same underlying model is served by a cloud provider, LatticeScale, as its own first-party [*service*](#glossary:service):

* Every participating entity ([ServiceProviderName](#datasets.costandusage.serviceprovidername), [HostProviderName](#datasets.costandusage.hostprovidername), and [InvoiceIssuerName](#datasets.costandusage.invoiceissuername)) is LatticeScale, the seller.
* The model developer, Solora AI, is not the seller, and is carried in the ModelDeveloper property.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_b.csv)

Note the following details in the example dataset:

* ModelDeveloper ("Solora AI") differs from ServiceProviderName ("LatticeScale"). The model developer is not represented by any existing participating-entity column, which is why model identity is carried as its own property.
* The served ModelId is namespaced by the cloud provider ("latticescale.solora-reasoning-pro"), so the other model-identity properties (ModelDeveloper, ModelFamily, ModelVariant, and ModelVersion) are what associate the charge with the underlying model across sellers.
* As in Scenario A, the input and output split is structural, and the model-identity properties are common to both rows.
