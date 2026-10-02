# Examples: AI Model Billing

The following examples illustrate how a [Cost and Usage](#datamodel.costandusage) [*FOCUS dataset*](#glossary:FOCUS-dataset) represents usage-based billing for AI model APIs, where consumption is measured in tokens rather than in the compute, storage, or networking units common to infrastructure services. Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp runs model workloads billed on token consumption.
* Input and output tokens are priced separately, denominated per 1,000,000 tokens, so each token type is carried as its own row rather than blended into a single rate.
* Token billing is represented using existing Cost and Usage columns. No AI-specific column is needed.

The following examples illustrate model billing scenarios across direct billing, multiple models on one invoice, cloud marketplace purchases, a CSP-served third-party model, commitment drawdown, and cached token metering. Charges for a model and its underlying infrastructure appearing on the same invoice are outside the scope of this section.

| Example | Invoice Issuer / Host Provider | Service Provider | Scenario |
| :--- | :--- | :--- | :--- |
| Per-Token AI Model API | Solora AI | Solora AI | Model developer bills the customer directly |
| Multi-Model Usage | Solora AI | Solora AI | Multiple models on one invoice, each priced separately |
| Cached Tokens via CSP Marketplace | Aura Web | Solora AI | Marketplace seller (model developer) as service provider; CSP hosts and invoices; cache-only metering slice |
| CSP-Served Third-Party Model | Aura Web | Aura Web | Cloud provider bills for its own service serving a third-party model |
| Drawdown via Prepayment | Solora AI | Solora AI | Commitment purchase with subsequent token drawdown |
| Multi-Model Invoice via CSP Marketplace | LatticeScale | Solora AI | Marketplace seller as service provider; CSP hosts and invoices; multiple models and cache meters |

Note the following column usage on the token usage rows in the scenarios below:

* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) and [ConsumedUnit](#datamodel.costandusage.consumedunit) carry the raw token count and unit of measure.
* [PricingQuantity](#datamodel.costandusage.pricingquantity) and [PricingUnit](#datamodel.costandusage.pricingunit) carry the same consumption expressed in the [*block pricing*](#glossary:block-pricing) increment the provider prices against.
* [SkuId](#datamodel.costandusage.skuid) identifies the priced model offering and [SkuMeter](#datamodel.costandusage.skumeter) distinguishes the token type being charged.
* [ServiceCategory](#datamodel.costandusage.servicecategory) is "AI and Machine Learning" and [ServiceSubcategory](#datamodel.costandusage.servicesubcategory) is "Generative AI".
* Model identity is carried in [SkuPriceDetails](#datamodel.costandusage.skupricedetails) using the properties described in the [Examples: AI Model Identity](#appendix.examples:aimodelidentity) section, which are not restated here.
* The TokenDirection and TokenCacheAction properties of SkuPriceDetails label the direction of the metered tokens and their interaction with a cache, independently of the SkuMeter name.
* Solora AI meters cache reads and cache writes separately from other input tokens, so the "Input Tokens" rows it sells carry TokenCacheAction "Uncached".
* [PrincipalId](#datamodel.costandusage.principalid) identifies the [*principal*](#glossary:principal) associated with a charge, where one applies.
* [CredentialId](#datamodel.costandusage.credentialid) identifies the [*credential*](#glossary:credential) presented on the request that produced the charge, where one applies.
* [RequesterDetails](#datamodel.costandusage.requesterdetails) carries the published attributes of each (see [Examples: Requester Attribution](#appendix.examples:requesterattribution) and [Examples: Requester Details](#appendix.examples:jsonobject.examples:requesterdetails)); it is populated wherever PrincipalId or CredentialId is set.

The same examples can be read by axis. An example may appear under more than one heading.

### Participating Entity Arrangements

| Arrangement | Applicable Examples |
| :--- | :--- |
| Model developer sells, hosts, and invoices | <ul><li>Per-Token AI Model API</li><li>Multi-Model Usage</li><li>Drawdown via Prepayment</li></ul> |
| CSP sells, hosts, and invoices a third-party model | <ul><li>CSP-Served Third-Party Model</li></ul> |
| Marketplace seller (model developer) sells; CSP hosts and invoices (scenario 3.1.3 in [Examples: Participating Entity Identification](#appendix.examples:participatingentityidentification)) | <ul><li>Cached Tokens via CSP Marketplace</li><li>Multi-Model Invoice via CSP Marketplace</li></ul> |

### Billing Mechanics

| Mechanic | Applicable Examples |
| :--- | :--- |
| Per-token pricing in block increments | <ul><li>*All examples*</li></ul> |
| Commitment purchase and drawdown | <ul><li>Drawdown via Prepayment (the only example with PricingCategory "Committed" usage rows)</li></ul> |

### Token Metering

| Metering Feature | Applicable Examples |
| :--- | :--- |
| Input and output tokens priced separately | <ul><li>*All examples except Cached Tokens via CSP Marketplace*</li></ul> |
| Cache read and cache write | <ul><li>Cached Tokens via CSP Marketplace</li><li>Multi-Model Invoice via CSP Marketplace</li></ul> |
| Multiple models on one invoice | <ul><li>Multi-Model Usage</li><li>Multi-Model Invoice via CSP Marketplace</li></ul> |
