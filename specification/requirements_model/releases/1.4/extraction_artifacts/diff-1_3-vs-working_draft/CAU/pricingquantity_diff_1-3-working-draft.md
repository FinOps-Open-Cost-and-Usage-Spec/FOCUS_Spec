## Diff

@@ -1,14 +1,12 @@
## Requirements

PricingQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingQuantity MUST be present in a Cost and Usage *FOCUS dataset*.-]
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to NumericFormat requirements.
* PricingQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingQuantity MUST be null when SkuPriceId is null.
  * PricingQuantity MUST be null when ChargeCategory is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * PricingQuantity MAY be null in all other cases.
[-* PricingQuantity MUST be a valid decimal value when not null.-]
* Cost metric (e.g., ContractedCost) MUST equal the product of the corresponding unit price (e.g., ContractedUnitPrice) and PricingQuantity when the unit price is not null and PricingQuantity is not null.
