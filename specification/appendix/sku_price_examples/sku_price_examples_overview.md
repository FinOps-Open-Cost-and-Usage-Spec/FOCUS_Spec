# Examples: SKU Price

> Note: The following section is informative and non-normative. It does not define requirements.

The following section contains examples of how a [*service provider*](#glossary:service-provider) may represent a published [*price list*](#glossary:price-list) as a [SKU Price](#datamodel.skuprice) [*FOCUS dataset*](#glossary:FOCUS-dataset). The scenarios use a fictitious service provider, Aura Web, and a fictitious customer, Acme Corp. Provider, service, and identifier names are illustrative.

The scenarios draw on a single *price list* rather than a separate dataset per scenario, because several SKU Price constructs are only visible when the records sit side by side. Row uniqueness, tier boundaries, and price effectivity each depend on how a record relates to its neighbors.

[**CSV Example: complete price list**](/specification/data/sku_price_examples/aura_web_price_list_full.csv)

The *price list* contains 18 records across six SKUs:

* A general purpose virtual machine offered at a current and a superseded standard unit price, at a second standard unit price in another currency, at a negotiated unit price, and at three committed usage unit prices.
* A one-year virtual machine reservation, offered under two payment models.
* A one-year flexible spend plan, offered under two payment models.
* Object storage priced across three quantity tiers, with one negotiated tier.
* An analytics service priced in a [*consumption currency*](#glossary:consumption-currency).
* A purchasable balance of that consumption currency, and the published unit value of a granted promotional credit.

Each scenario below links a CSV extract containing the records from the *price list* that the scenario discusses. The extracts are subsets of the complete *price list*, not separate datasets.

## Reading a SKU Price Record

Two properties of the dataset shape every scenario that follows.

The first is row uniqueness. A SKU Price record is identified by the combination of ServiceProviderName, SkuPriceId, ContractId, SkuPriceEffectiveStart, and PricingCurrency. Two records that differ in any one of those five values are distinct prices for the same SKU Price ID. Two records that match on all five are the same price, and only one of them belongs in the dataset. Every scenario below that shows several records sharing a SKU Price ID is separating them on one of those five values.

The second is that the dataset describes prices, not charges. A *price list* is published before consumption happens, so it records what a price is and who is eligible for it. It does not record whether a price was used, how much was consumed, or what a customer was ultimately billed. Those belong to the [Cost and Usage](#datamodel.costandusage) dataset.
