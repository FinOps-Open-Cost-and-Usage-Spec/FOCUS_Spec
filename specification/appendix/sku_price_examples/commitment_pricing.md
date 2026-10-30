# Commitment Pricing

[Commitment discounts](#term) appear in a [price list](#term) as two different kinds of records: commitment purchase SKU Price records, and usage SKU Price records for usage covered by those commitments. [ChargeCategory](#col:SkuPrice.ChargeCategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments, each under three payment models. A reservation commits to a specific resource, the standard virtual machine, and is bought for a one-year term. A flexible spend plan commits to an amount of spend rather than to a resource, and is bought at face value, one unit of price for each unit of committed spend. The on-demand rate for the standard machine is 0.384000 per hour.

## Commitment Purchases

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six commitment purchase records have a ChargeCategory of "Purchase". [PurchaseDurationType](#col) is "1 Year", and [PurchasePaymentModel](#col) identifies the payment model.
* Each payment model is a distinct price offering and is therefore represented by a separate record with its own [SkuPriceId](#col:SkuPrice.SkuPriceId), even when the records share the same [UnitPrice](#col). A [service provider](#term) may set different [UnitPrice](#col) values for different payment models, or may charge the same [UnitPrice](#col) across payment models. The reservation and the spend plan in this example illustrate these two patterns.
* The reservation purchase prices are 1893.600000, 1998.800000, and 2104.000000 for "All Upfront", "Partial Upfront", and "No Upfront", respectively. [PricingUnit](#col:SkuPrice.PricingUnit) is "Units", so [UnitPrice](#col) represents the price of one reservation, and [PurchaseDurationType](#col) specifies the one-year term. The payment model affects the [UnitPrice](#col).
* The spend plan purchase price is 1.000000 for all three payment models. The plan is purchased per unit of committed spend, so [UnitPrice](#col) represents the price of one unit of commitment. The payment model does not affect the [UnitPrice](#col), so the three records share the same [UnitPrice](#col) while remaining separate price offerings. PricingUnit is "USD", representing the unit in which the commitment is measured, and [PricingCurrency](#col:SkuPrice.PricingCurrency) is also "USD", representing the currency in which the purchase is priced. These columns describe different aspects of the price: the unit of the commitment and the currency of the price.
* The two commitment instruments have different [SkuId](#col:SkuPrice.SkuId) values because they represent different products. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD", while the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND". [CommitmentDiscountCategory](#col:SkuPrice.CommitmentDiscountCategory) also separates them: "Usage" on the reservation records, which commit to a resource, and "Spend" on the spend plan records, which commit to an amount of spend.

## Committed Usage Alongside Commitment Purchases

The rate for consumption covered by a commitment is represented by a separate record from the commitment purchase fee. This extract includes the on-demand usage record, the three reservation purchase records, and the three usage records associated with those reservations, allowing the purchase and usage records for the reservation to be viewed together.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The four usage records have a ChargeCategory of "Usage" and null [PurchaseDurationType](#col) and [PurchasePaymentModel](#col). The purchase records in the same extract have values for both columns. [PurchaseDurationType](#col) and [PurchasePaymentModel](#col) describe the commitment purchase and therefore do not apply to usage records.
* For the three records representing usage covered by a reservation, [ContractId](#col:SkuPrice.ContractId) is null and [UnitPriceType](#col) is "List", so [UnitPrice](#col) corresponds to the [ListUnitPrice](#col) for the resource. When a particular consumption record is covered by a commitment, this is reflected in the [EffectiveCost](#col) and [BilledCost](#col:CostAndUsage.BilledCost) columns in the [Cost and Usage](#ds) dataset, but not in the [ListCost](#col), [ContractedCost](#col), [ContractedUnitPrice](#col), or [ListUnitPrice](#col). Therefore, the three covered records have the same [UnitPrice](#col) as the on-demand usage record, 0.384000.
* Although the [UnitPrice](#col) is identical across the four usage records, each record represents a distinct price offering and therefore has its own SkuPriceId. The distinct SkuPriceId values associate each usage record with the commitment that covers it. The on-demand record carries a null CommitmentDiscountCategory, while the three covered records carry "Usage", the category of the reservation that covers them.
