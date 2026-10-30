---
dataset: SkuPrice
---

# Examples: SKU Price

> **Preview:** The [SKU Price](#ds) dataset is a preview in this version of FOCUS, so these examples may change in the next version based on implementation feedback. The preview also covers two requirements outside the dataset, which are excluded from conformance, and two operating model conditions and a schema that exist only for SKU Price. [Issue #2768](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2768) tracks the preview and lists each one.

The following section contains examples of how a [service provider](#term) may represent a published [price list](#term) as a SKU Price [FOCUS dataset](#term). The scenarios use a fictitious service provider, Aura Web, and a fictitious customer, Acme Corp. Provider, service, and identifier names are illustrative.

The scenarios draw on a single [price list](#term) rather than a separate dataset per scenario, because several SKU Price constructs are only visible when the records sit side by side. Row uniqueness, tier boundaries, and price effectivity each depend on how a record relates to its neighbors.

[**CSV Example: complete price list**](/specification/data/sku_price_examples/aura_web_rate_card_full.csv)

The [price list](#term) contains 28 records across 10 SKUs:

* A general purpose virtual machine offered at a current and a superseded on-demand rate, at a second on-demand rate in another currency, at a negotiated rate, and at three committed rates, one for each reservation payment model under which its consumption can be covered.
* A burstable virtual machine whose on-demand rate changes at the start of 2027, announced ahead of taking effect.
* A shared-core virtual machine offered at a single rate that carries no effective start or end date.
* A one-year virtual machine reservation, offered under three payment models.
* A one-year flexible spend plan, offered under three payment models.
* Object storage priced across three quantity tiers, with one negotiated tier.
* A legacy object storage tier with no published origin date, scheduled for withdrawal.
* A managed database offered at a standing rate, with a promotional rate for the first quarter of 2026.
* An analytics service priced in a [consumption currency](#term).
* A purchasable balance of that consumption currency, and the published unit value of a granted promotional credit.

Each scenario below links a CSV extract containing the records from the rate card that the scenario discusses. The extracts are subsets of the complete rate card, not separate datasets.

## Reading a SKU Price Record

Two properties of the dataset shape every scenario that follows.

The first is row uniqueness. A SKU Price record is identified by the combination of [ServiceProviderName](#col), [SkuPriceId](#col), [ContractId](#col), [SkuPriceEffectiveStart](#col), [PricingCurrency](#col), and [UnitPriceType](#col). Two records that differ in any one of those six values are distinct prices for the same [SKU Price ID](#col). Two records that match on all six are the same price, and only one of them belongs in the dataset. Every scenario below that shows several records sharing a [SKU Price ID](#col) is separating them on one of those six values.

The second is that the dataset describes prices, not charges. A price list is published before consumption happens, so it records what a price is and who is eligible for it. It does not record whether a price was used, how much was consumed, or what a customer was ultimately billed. Those belong to the [Cost and Usage](#ds) dataset.
