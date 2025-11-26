# PricingCurrencyListUnitPrice

## Normative Text 1.2

The PricingCurrencyListUnitPrice column adheres to the following requirements:

PricingCurrencyListUnitPrice presence in a FOCUS dataset is defined as follows:
PricingCurrencyListUnitPrice MUST be present in a FOCUS dataset when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
PricingCurrencyListUnitPrice is RECOMMENDED to be present in a FOCUS dataset when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
PricingCurrencyListUnitPrice MAY be present in a FOCUS dataset in all other cases.
PricingCurrencyListUnitPrice MUST be of type Decimal.
PricingCurrencyListUnitPrice MUST conform to NumericFormat requirements.
PricingCurrencyListUnitPrice nullability is defined as follows:
PricingCurrencyListUnitPrice MUST be null when ChargeCategory is "Tax".
PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
PricingCurrencyListUnitPrice MAY be null in all other cases.
When PricingCurrencyListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.
Discrepancies in PricingCurrencyListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

## Normative Text 1.3

PricingCurrencyListUnitPrice adheres to the following requirements:

PricingCurrencyListUnitPrice presence in a Cost and Usage FOCUS dataset is defined as follows:
PricingCurrencyListUnitPrice MUST be present in a Cost and Usage FOCUS dataset when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
PricingCurrencyListUnitPrice is RECOMMENDED to be present in a Cost and Usage FOCUS dataset when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
PricingCurrencyListUnitPrice MAY be present in a Cost and Usage FOCUS dataset in all other cases.
PricingCurrencyListUnitPrice MUST be of type Decimal.
PricingCurrencyListUnitPrice MUST conform to NumericFormat requirements.
PricingCurrencyListUnitPrice nullability is defined as follows:
PricingCurrencyListUnitPrice MUST be null when SkuPriceId is null.
PricingCurrencyListUnitPrice MUST be null when ChargeCategory is "Tax".
PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.
PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
PricingCurrencyListUnitPrice MAY be null in all other cases.
When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice adheres to the following additional requirements:
PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

## Diff

-The PricingCurrencyListUnitPrice column adheres to the following requirements:
+## Requirements

-* PricingCurrencyListUnitPrice presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:

 - PricingCurrencyListUnitPrice MUST be present in a *FOCUS dataset* when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
 - PricingCurrencyListUnitPrice is RECOMMENDED to be present in a *FOCUS dataset* when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
 - PricingCurrencyListUnitPrice MAY be present in a *FOCUS dataset* in all other cases.
+PricingCurrencyListUnitPrice adheres to the following requirements:

+

+* PricingCurrencyListUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
- - PricingCurrencyListUnitPrice MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
- - PricingCurrencyListUnitPrice is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
- - PricingCurrencyListUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.

- PricingCurrencyListUnitPrice MUST be of type Decimal.
- PricingCurrencyListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
- PricingCurrencyListUnitPrice nullability is defined as follows:

+ - PricingCurrencyListUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
  - PricingCurrencyListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
- - PricingCurrencyListUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
  - PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  - PricingCurrencyListUnitPrice MAY be null in all other cases.
-*When PricingCurrencyListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
+* When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice adheres to the following additional requirements:
  - PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  - PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

 - Discrepancies in PricingCurrencyListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".
