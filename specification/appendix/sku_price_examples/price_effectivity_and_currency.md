# Price Effectivity and Currency

A [*SKU Price*](#glossary:sku-price) record is scoped in time and denominated in a currency. Both are members of the composite key, so a price change and a currency variant each produce an additional record rather than replacing an existing one.

## Price Changes Over Time

Aura Web reduced the on-demand rate for its standard virtual machine at the start of 2026. Both the old and the new rate appear in the rate card.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_effectivity.csv)

Note the following details in the example dataset:

* [SkuPriceEffectiveStart](#datamodel.skuprice.skupriceeffectivestart) is inclusive and [SkuPriceEffectiveEnd](#datamodel.skuprice.skupriceeffectiveend) is exclusive, so each record describes a half-open interval. The superseded rate of 0.400000 covers 2025-07-01 up to but not including 2026-01-01, and the current rate of 0.384000 begins at 2026-01-01.
* The two intervals meet at 2026-01-01 with no gap and no overlap. Sharing the boundary timestamp is what makes every point in time resolve to exactly one price for this combination of [ServiceProviderName](#datamodel.skuprice.serviceprovidername), [SkuPriceId](#datamodel.skuprice.skupriceid), [ContractId](#datamodel.skuprice.contractid), [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum), and [PricingCurrency](#datamodel.skuprice.pricingcurrency).
* The current rate carries a null SkuPriceEffectiveEnd, which states that it is active with no scheduled end. The superseded rate carries an end timestamp because it has been replaced.
* Both records carry the same [SkuPriceCreated](#datamodel.skuprice.skupricecreated) of 2025-06-15T09:12:00Z and the same [SkuPriceLastUpdated](#datamodel.skuprice.skupricelastupdated) of 2025-12-18T16:40:00Z. These describe when the catalog record was written and last modified, which is a different question from when the price applies. The 2026 rate was published in December 2025, ahead of taking effect.
* A charge in the [Cost and Usage](#datamodel.costandusage) dataset resolves to one of these records by comparing its charge period start against the effective interval. Retaining superseded records is what makes a historical charge resolvable after a price change.

## Effective Period Boundaries

The two effectivity columns carry meaning as a pair. Either may be null, and a null states that the interval is unbounded on that side, not that the boundary is unknown. Reading either column on its own, or treating a null as missing data, may result in misinterpretation of the row.

| SkuPriceEffectiveStart | SkuPriceEffectiveEnd | Validity period | A charge resolves to the record when | Position in the record chain |
| :--------------------- | :------------------- | :-------------- | :----------------------------------- | :--------------------------- |
| Null | Null | Unbounded in both directions | Always | The only record |
| Populated | Null | From the start timestamp onward | The charge period start is at or after the start timestamp | The last record |
| Null | Populated | Up to the end timestamp | The charge period start is before the end timestamp | The first record |
| Populated | Populated | A closed interval | The charge period start is at or after the start timestamp and before the end timestamp | Any position |

Aura Web offers a burstable virtual machine whose rate changes at the start of 2027, a legacy object storage tier it is withdrawing, and a shared-core virtual machine it has offered at one rate since the catalog began.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_boundaries.csv)

Note the following details in the example dataset:

* The burstable virtual machine carries two records. One record specifies the rate before the rate change and has a SkuPriceEffectiveStart of null and a SkuPriceEffectiveEnd of 2027-01-01. This row has a rate of 0.096000. The second record specifies the rate after the price change. Its SkuPriceEffectiveStart is 2027-01-01 and its SkuPriceEffectiveEnd is null. Its rate is set to 0.088000.
* The 2027 record was created on 2026-07-15T10:22:00Z, and the current record carries that same timestamp in SkuPriceLastUpdated because its end was written when the successor was announced. A record already in effect can acquire an end timestamp without its price changing.
* The legacy storage tier carries a null SkuPriceEffectiveStart on its earlier record. That rate applied before the rate card's history begins and Aura Web publishes no origin date for it, so the record has no lower boundary and any charge before 2026-04-01 resolves to it.
* A null SkuPriceEffectiveStart is not a restatement of when the catalog entry was written. The legacy record was created on 2024-03-04T08:15:00Z and still carries no start timestamp. SkuPriceCreated records when the entry was written, and the effectivity columns record when the price applies.
* The legacy tier's final record ends at 2026-10-01 with nothing following it, which is how a withdrawal appears. A supersession is identical on the record itself, and the two are separated only by whether another record for the same [SkuId](#datamodel.skuprice.skuid) begins at that timestamp. A [*service provider*](#glossary:service-provider) may partition delivery by region, service, or SKU category, so the absence of a successor within one delivery is not on its own evidence that a SKU was withdrawn.
* Resolving a charge against these records needs a predicate that tolerates a null on either side. Comparing [ChargePeriodStart](#datamodel.costandusage.chargeperiodstart) against a null boundary yields an undefined result rather than a match, so writing the interval test as a single pair of comparisons silently drops every record that is unbounded on either side. Each side needs its own test: the record matches when its start is null or the charge period start is at or after it, and when its end is null or the charge period start is before it.
* Because records sharing a combination of ServiceProviderName, SkuPriceId, ContractId, QuantityTierMinimum, and PricingCurrency must not overlap, the null pattern fixes where a record can sit. A record unbounded on both sides is the only record that combination can hold, since any second record would overlap it. That combination is the composite key without SkuPriceEffectiveStart, so records sharing it stay distinct on their start timestamps while their validity periods are barred from overlapping.
* The shared-core virtual machine completes the set. Its single record carries a null SkuPriceEffectiveStart and a null SkuPriceEffectiveEnd, priced at 0.012000 since the catalog began, so it applies to every charge and is the only record its key combination can hold. This is what a *service provider* that publishes no effectivity at all looks like: one record for each combination of the key members, unbounded on both sides.

## Temporary Pricing

A promotional rate applies for a bounded interval and then reverts. Aura Web halved the rate on its managed database for the first quarter of 2026, and the standing rate resumed afterward.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_promotional.csv)

Note the following details in the example dataset:

* Three records describe one price point over time. The standing rate of 0.500000 carries a null SkuPriceEffectiveStart and an end of 2026-01-01, the promotional rate of 0.250000 is closed on both sides at 2026-01-01 and 2026-04-01, and the resumed rate of 0.500000 carries a start of 2026-04-01 and a null SkuPriceEffectiveEnd.
* The bounded promotional record is what a temporary price looks like: a closed interval sitting between two records that are each open on one side. A rate that has simply always applied carries a null SkuPriceEffectiveStart instead, so existence and a temporary price are not the same shape and do not read the same way.
* The pre-promotion and resumed records carry the same 0.500000 rate but are distinct records, separated by SkuPriceEffectiveStart, which is a member of the composite key. A charge before 2026-01-01 and a charge on or after 2026-04-01 resolve to different records that happen to agree on price.

## Multiple Pricing Currencies

The same virtual machine is offered in United States dollars and in euros.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_multi_currency.csv)

Note the following details in the example dataset:

* Both records share a SkuPriceId and differ only in PricingCurrency and [ListUnitPrice](#datamodel.skuprice.listunitprice). PricingCurrency is a member of the composite key, so the two prices coexist as separate records for one price point.
* The euro price of 0.352000 is a published rate in its own right, not a conversion of the dollar price applied at read time. A service provider that publishes prices in several currencies publishes a rate per currency, and the rates need not track a single exchange rate.
* [PricingCurrencyCategory](#datamodel.skuprice.pricingcurrencycategory) is "Payable" on both records. Both currencies are financial instruments a customer can settle in, so multiplying a quantity by either rate yields a financial cost directly.

## Consumption Currency

Aura Web prices its analytics service in platform credits rather than in a [*national currency*](#glossary:national-currency), and sells those credits separately.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_consumable_currency.csv)

Note the following details in the example dataset:

* The analytics rate carries a PricingCurrencyCategory of "Consumable" and a PricingCurrency of "Credit". Multiplying scanned volume by its ListUnitPrice of 4.000000 yields a balance of credits, not a financial cost. Converting that balance to a financial cost requires the second record.
* The credit purchase carries a PricingCurrencyCategory of "Payable" and a PricingCurrency of "USD", with a ListUnitPrice of 0.010000 per credit. A consumer reaches a financial cost by resolving the consumable rate first and then applying the payable rate. Scanning 100 GB consumes 400 credits, which cost 4.00.
* [PricingUnit](#datamodel.skuprice.pricingunit) and PricingCurrency answer different questions and are easy to transpose on a record like this. On the analytics rate the unit is "GB" and the currency is "Credit"; on the credit purchase the unit is "Credits" and the currency is "USD". The unit is what is being measured, and the currency is what it is priced in.
* [PricingRegionId](#datamodel.skuprice.pricingregionid) is null on both records, which states that the rate is not regionally scoped rather than that its region is unknown. The virtual machine and storage rates elsewhere in the rate card carry "us-east-1" because those prices vary by region.
* The credit purchase carries a ChargeCategory of "Purchase" and a null [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype), because a purchased credit balance that does not expire has no term to state. Its [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) is "All Upfront", since the balance is paid for when it is bought.
