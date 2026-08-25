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

## Multiple Pricing Currencies

The same virtual machine is offered in United States dollars and in euros.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_multi_currency.csv)

Note the following details in the example dataset:

* Both records share a SkuPriceId and differ only in PricingCurrency and [ListUnitPrice](#datamodel.skuprice.listunitprice). PricingCurrency is a member of the composite key, so the two prices coexist as separate records for one price point.
* The euro price of 0.352000 is a published rate in its own right, not a conversion of the dollar price applied at read time. A service provider that publishes prices in several currencies publishes a rate per currency, and the rates need not track a single exchange rate.
* [PricingCurrencyCategory](#datamodel.skuprice.pricingcurrencycategory) is "Payable" on both records. Both currencies are financial instruments a customer can settle in, so multiplying a quantity by either rate yields a financial cost directly.

## Consumption Currency

Aura Web prices its analytics service in platform credits rather than in a [*national currency*](#glossary:national-currency), sells those credits separately, and also grants them promotionally.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_consumable_currency.csv)

Note the following details in the example dataset:

* The analytics rate carries a PricingCurrencyCategory of "Consumable" and a PricingCurrency of "Credit". Multiplying scanned volume by its ListUnitPrice of 4.000000 yields a balance of credits, not a financial cost. Converting that balance to a financial cost requires the second record.
* The credit purchase carries a PricingCurrencyCategory of "Payable" and a PricingCurrency of "USD", with a ListUnitPrice of 0.010000 per credit. A consumer reaches a financial cost by resolving the consumable rate first and then applying the payable rate. Scanning 100 GB consumes 400 credits, which cost 4.00.
* [PricingUnit](#datamodel.skuprice.pricingunit) and PricingCurrency answer different questions and are easy to transpose on a record like this. On the analytics rate the unit is "GB" and the currency is "Credit"; on the credit purchase the unit is "Credits" and the currency is "USD". The unit is what is being measured, and the currency is what it is priced in.
* [PricingRegionId](#datamodel.skuprice.pricingregionid) is null on all three records, which states that the rate is not regionally scoped rather than that its region is unknown. The virtual machine and storage rates elsewhere in the rate card carry "us-east-1" because those prices vary by region.
* The credit purchase carries a [ChargeCategory](#datamodel.skuprice.chargecategory) of "Purchase" and a null [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype), because a purchased credit balance that does not expire has no term to state. Its [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) is "All Upfront", since the balance is paid for when it is bought.
* The third record carries a ChargeCategory of "Credit", which classifies the price point rather than naming the currency, and describes that same platform credit granted rather than sold. Its ListUnitPrice of 0.010000 is the unit value the service provider publishes for the grant, which is what makes a granted balance reportable against a financial figure. Both PurchaseDurationType and PurchasePaymentModel are null, because a grant is not a purchase. Its own SkuPriceId of "AURAWEB-GLOBAL-CREDITS-PROMOTIONAL" is what separates it from the purchased balance under row uniqueness, and it shares that record's [SkuId](#datamodel.skuprice.skuid) because a granted credit and a purchased one are the same SKU at two price points.
