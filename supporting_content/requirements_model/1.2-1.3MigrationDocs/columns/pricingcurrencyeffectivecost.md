## PricingCurrencyEffectiveCost

### Normative Text v1.2

The PricingCurrencyEffectiveCost column adheres to the following requirements:

* PricingCurrencyEffectiveCost presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyEffectiveCost MUST be present in a *FOCUS dataset* when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a *FOCUS dataset* when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be a valid decimal value.
* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.
* PricingCurrencyEffectiveCost MUST be denominated in the [PricingCurrency](#pricingcurrency).

### Normative Text v1.3

## Requirements

PricingCurrencyEffectiveCost adheres to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyEffectiveCost MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be a valid decimal value.
* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.
* PricingCurrencyEffectiveCost MUST be denominated in the [PricingCurrency](#pricingcurrency).


### Diff

-The PricingCurrencyEffectiveCost column adheres to the following requirements:
+## Requirements
 
-* PricingCurrencyEffectiveCost presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
-  * PricingCurrencyEffectiveCost MUST be present in a *FOCUS dataset* when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
-  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a *FOCUS dataset* when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
-  * PricingCurrencyEffectiveCost MAY be present in a *FOCUS dataset* in all other cases.
+PricingCurrencyEffectiveCost adheres to the following requirements:
+
+* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
+  * PricingCurrencyEffectiveCost MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
+  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
+  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
 * PricingCurrencyEffectiveCost MUST be of type Decimal.
 * PricingCurrencyEffectiveCost MUST conform to [NumericFormat](#numericformat) requirements.
 * PricingCurrencyEffectiveCost MUST NOT be null.