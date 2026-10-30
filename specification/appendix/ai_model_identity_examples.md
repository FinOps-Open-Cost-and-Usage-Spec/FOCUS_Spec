---
dataset: CostAndUsage
---

# Examples: AI Model Identity

The following examples illustrate how a [Cost and Usage](#ds) [FOCUS dataset](#term) represents the identity of an [AI model](#term) using FOCUS-defined [SKU Price Details](#col) properties. They also demonstrate how the TokenDirection property labels the structural split between input (i.e., prompt) and output (i.e., generated) [tokens](#term). Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses a per-token AI model API to run a workload.
* The model is priced separately for input and output tokens, denominated per 1,000,000 tokens.
* The model identity (developer, family, identifier, and version) is stable for a given [SKU Price](#term), so it is carried in [SKU Price Details](#col).

> **Note:** The FOCUS-defined [SKU Price Details](#col) properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: AI Model Purchased Directly

For this scenario, Acme Corp purchases the model directly from the model developer, Solora AI:

* Input tokens are priced at $3.00 per 1,000,000 tokens, and output tokens at $15.00 per 1,000,000 tokens.
* During the [charge period](#term), the workload consumes 5,000,000 input tokens and 1,500,000 output tokens.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_a.csv)

Note the following details in the example dataset:

* Model identity is carried in [SKU Price Details](#col) using the FOCUS-defined properties ModelDeveloper, ModelFamily, ModelId, and ModelVersion. These values are common to both rows because both describe the same model.
* The split between input and output tokens is structural. Each is a separate [SKU](#term) with distinct [SKU ID](#col), [SKU Price ID](#col), and [SKU Meter](#col) values. TokenDirection (i.e., "Input" or "Output") normalizes this split so rows can be grouped regardless of meter names. TokenCacheAction is "Uncached" on the input row, as Solora AI meters cache interactions separately (see [Examples: AI Prompt Caching](#appendix.examples:aipromptcaching)), and is absent from the output row.
* [Consumed Quantity](#col) holds the raw token count and [Consumed Unit](#col) is "Tokens", while [Pricing Quantity](#col) holds the priced volume and [Pricing Unit](#col) is "1000000 Tokens".
* Because Acme Corp pays the list price, [List Unit Price](#col) and [Contracted Unit Price](#col) are equal, so [List Cost](#col), [Contracted Cost](#col), [Billed Cost](#col), and [Effective Cost](#col) are equal.

## Scenario B: Same Model Served by a Cloud Provider

For this scenario, the same underlying model is served by a cloud provider, LatticeScale, as its own first-party [service](#term):

* Every participating entity ([Service Provider Name](#col), [Host Provider Name](#col), and [Invoice Issuer Name](#col)) is LatticeScale, the [service provider](#term).
* The model developer, Solora AI, is not the [service provider](#term), and is carried in the ModelDeveloper property.

[**CSV Example**](/specification/data/ai_model_identity/ai_model_identity_b.csv)

Note the following details in the example dataset:

* ModelDeveloper ("Solora AI") differs from [Service Provider Name](#col) ("LatticeScale"). The model developer is not represented by any existing participating-entity column, which is why model identity is carried as its own property.
* The served ModelId is namespaced by the [service provider](#term) ("latticescale.solora-reasoning-pro"), so the other model-identity properties (ModelDeveloper, ModelFamily, and ModelVersion) are what associate the charge with the underlying model across [service providers](#term).
* As in Scenario A, TokenDirection labels the structural split, and model identity is common to both rows. The input row carries no TokenCacheAction because LatticeScale bills tokens placed into a cache on its ordinary input meter.
