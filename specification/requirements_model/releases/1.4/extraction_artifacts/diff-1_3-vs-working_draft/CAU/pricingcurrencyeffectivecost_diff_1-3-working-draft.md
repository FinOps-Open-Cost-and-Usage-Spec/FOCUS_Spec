## Diff

@@ -1,14 +1,9 @@
## Requirements

PricingCurrencyEffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCurrencyEffectiveCost presence in a Cost and Usage *FOCUS dataset* is defined as follows:-]
[-  * PricingCurrencyEffectiveCost MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]
[-  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.-]
[-  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.-]
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to NumericFormat requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
[-* PricingCurrencyEffectiveCost MUST be a valid decimal value.-]
[-* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.-]
* PricingCurrencyEffectiveCost MUST be denominated in the PricingCurrency.
{+* PricingCurrencyEffectiveCost MUST be the PricingCurrency-denominated equivalent of EffectiveCost.+}
