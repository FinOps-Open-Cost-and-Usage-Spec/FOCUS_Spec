## PricingCurrency
### Normative Text v1.2

The PricingCurrency column adheres to the following requirements:

* PricingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports pricing and billing in different currencies.
* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#currencyformat) requirements.
* PricingCurrency MUST NOT be null.

### Normative Text v1.3

## Requirements

PricingCurrency adheres to the following requirements:

* PricingCurrency MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports pricing and billing in different currencies.
* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#currencyformat) requirements.
* PricingCurrency MUST NOT be null.

### Diff

-The PricingCurrency column adheres to the following requirements:
+## Requirements
 
-* PricingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports pricing and billing in different currencies.
+PricingCurrency adheres to the following requirements:
+
+* PricingCurrency MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports pricing and billing in different currencies.
 * PricingCurrency MUST be of type String.
 * PricingCurrency MUST conform to [StringHandling](#stringhandling) requirements.
 * PricingCurrency MUST conform to [CurrencyFormat](#currencyformat) requirements.