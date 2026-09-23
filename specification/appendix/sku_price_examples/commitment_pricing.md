# Commitment Pricing

[*Commitment discount*](#glossary:commitment-discount) appear in a [*price list*](#glossary:price-list) as two different kinds of records: commitment purchase SKU Price records, and usage SKU Price records for usage covered by those commitments. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments, each under three payment models. A reservation commits to a specific resource, the standard virtual machine, and is bought for a one-year term. A flexible spend plan commits to an amount of spend rather than to a resource, and is bought at face value, one unit of price for each unit of committed spend. The on-demand rate for the standard machine is 0.384000 per hour.

## Commitment Purchases

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six records have a ChargeCategory of "Purchase", identifying them as commitment purchase records. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) is "1 Year", and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) identifies the payment model.
* Each payment model is represented by a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid). The records therefore represent distinct price offerings even when other columns, including UnitPrice, are the same.
* The reservation purchase prices are 1893.600000, 1998.800000, and 2104.000000 for "All Upfront", "Partial Upfront", and "No Upfront", respectively. [PricingUnit](#datamodel.skuprice.pricingunit) is "Units", so [UnitPrice](#datamodel.skuprice.unitprice) represents the price of one reservation. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) specifies the one-year term, while [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) specifies the payment model. In this example, the payment model affects the UnitPrice of the reservation purchase.
* The spend plan purchase price is 1.000000 for all three payment models. The plan is purchased per unit of committed spend, so [UnitPrice](#datamodel.skuprice.unitprice) represents the price of one unit of commitment. In this example, the payment model does not affect the UnitPrice, so all three payment models have the same UnitPrice while remaining separate price offerings with distinct SkuPriceId values. [PricingUnit](#datamodel.skuprice.pricingunit) is "USD", representing the unit in which the commitment is measured, and [PricingCurrency](#datamodel.skuprice.pricingcurrency) is also "USD", representing the currency in which the purchase is priced. These columns describe different aspects of the price: the unit of the commitment and the currency of the price.
* The two commitment instruments have different [SkuId](#datamodel.skuprice.skuid) values because they represent different products. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD", while the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND".

## Committed Usage Alongside Commitment Purchases

The rate for consumption covered by a commitment is represented by a separate record from the commitment purchase fee. This extract includes the on-demand usage record, the three reservation purchase records, and the three usage records associated with those reservations, allowing the purchase and usage records for the reservation to be viewed together.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The four usage records have a ChargeCategory of "Usage" and null PurchaseDurationType and PurchasePaymentModel. The purchase records in the same extract have values for both columns. PurchaseDurationType and PurchasePaymentModel describe the commitment purchase and therefore do not apply to usage records.
* This separation reflects the distinction between pricing information and the application of a commitment to consumption. A price list describes available rates and purchase offers before consumption occurs. Whether a particular consumption record is covered by a commitment is reflected in the [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) columns in the [Cost and Usage](#datamodel.costandusage) dataset, rather than in the price record.
* All four usage records have a UnitPrice of 0.384000. For the three records representing usage covered by a reservation, ContractId is null, so UnitPrice represents the standard public list price for the resource. The commitment does not reduce this UnitPrice; the effect of applying the commitment is reflected in the resulting cost, including [EffectiveCost](#datamodel.costandusage.effectivecost), rather than in UnitPrice.
* Although the UnitPrice is identical across the four usage records, each record represents a distinct price offering and therefore has its own [SkuPriceId](#datamodel.skuprice.skupriceid). The distinct SkuPriceId values associate each usage record with the commitment that covers it.
