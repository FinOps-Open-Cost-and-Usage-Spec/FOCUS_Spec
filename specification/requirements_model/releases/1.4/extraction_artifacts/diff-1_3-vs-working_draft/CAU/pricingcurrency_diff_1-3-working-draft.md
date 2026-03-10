## Diff

PricingCurrency [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCurrency MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports pricing and billing in different currencies.-]
* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* PricingCurrency MUST conform to [-[CurrencyFormat](#currencyformat)-]{+[CurrencyFormat](#attributes.currencyformat)+} requirements.
* PricingCurrency MUST NOT be null.

