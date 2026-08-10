# Quantity Tier Pricing

Aura Web prices object storage in three quantity tiers, and grants Acme Corp a negotiated rate on the middle tier. Tiered pricing is represented as one record per tier, each carrying its own unit price and its own quantity boundaries.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_quantity_tiers.csv)

Note the following details in the example dataset:

* All four records share a [SkuPriceId](#datamodel.skuprice.skupriceid) of "AURAWEB-USEAST1-STORAGE-OBJECT-STANDARD". [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum) is a member of the composite key, which is what allows the tiers to coexist as separate records for one price point.
* QuantityTierMinimum is an exclusive lower bound and [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum) is an inclusive upper bound, so each pair describes a half-open quantity interval. A quantity falls in a tier when it is strictly greater than the minimum and less than or equal to the maximum. The three public tiers therefore cover the following quantities, measured in the [PricingUnit](#datamodel.skuprice.pricingunit) of "GB-Months":

| Quantity range | QuantityTierMinimum | QuantityTierMaximum | ListUnitPrice |
| :--- | ---: | ---: | ---: |
| Up to and including 51,200 | 0 | 51200 | 0.023000 |
| Above 51,200, up to and including 512,000 | 51200 | 512000 | 0.022000 |
| Above 512,000 | 512000 | *null* | 0.021000 |

* Adjacent tiers meet at a shared boundary value rather than at consecutive values. The first tier ends at 51,200 and the second begins at 51,200, and because the first bound is inclusive and the second exclusive, a quantity of exactly 51,200 falls in the first tier only. Setting the second tier's minimum to 51,201 would leave every fractional quantity between the two unpriced.
* The highest tier carries a null QuantityTierMaximum to indicate no upper bound. Only the highest tier does; a tier with a higher tier above it carries a maximum, which is what closes the gap between them.
* These boundaries identify which tier a quantity falls in. Whether the tier's unit price applies only to the units inside that tier or to every unit consumed is a property of the published pricing terms for the offering, and is not expressed by the boundaries themselves.
* The fourth record is a negotiated rate on the middle tier, carrying a populated [ContractId](#datamodel.skuprice.contractid) and a [ContractedUnitPrice](#datamodel.skuprice.contractedunitprice) of 0.018700 against a [ListUnitPrice](#datamodel.skuprice.listunitprice) of 0.022000. It repeats the tier boundaries of the public middle tier rather than defining new ones, because the negotiation changed the price within that tier rather than where the tier begins and ends.
* Two members of the composite key differ between the negotiated record and the public middle tier: ContractId and, relative to the other two public tiers, QuantityTierMinimum. Both records describe the same quantity interval without colliding.
