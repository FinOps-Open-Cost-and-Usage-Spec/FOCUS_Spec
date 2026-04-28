## Diff

diff --git a/tmp/pricingcurrencycontractedunitprice_v13.md b/tmp/pricingcurrencycontractedunitprice_working.md
index 2b7989ed..18edf444 100644
--- a/tmp/pricingcurrencycontractedunitprice_v13.md
+++ b/tmp/pricingcurrencycontractedunitprice_working.md
@@ -4,24 +4,24 @@ The Pricing Currency Contracted Unit Price represents the agreed-upon unit price

## Requirements

PricingCurrencyContractedUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCurrencyContractedUnitPrice presence in a Cost and Usage *FOCUS dataset* is defined as follows:-]
[-  * PricingCurrencyContractedUnitPrice MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]
[-  * PricingCurrencyContractedUnitPrice is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.-]
[-  * PricingCurrencyContractedUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.-]
* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to NumericFormat requirements.
* PricingCurrencyContractedUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCurrencyContractedUnitPrice MUST be null when SkuPriceId is null.
  * PricingCurrencyContractedUnitPrice MUST be null when ChargeCategory is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.

