## PricingCurrencyContractedUnitPrice

### Normative Text v1.2

The PricingCurrencyContractedUnitPrice column adheres to the following requirements:

* PricingCurrencyContractedUnitPrice presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be present in a *FOCUS dataset* when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * PricingCurrencyContractedUnitPrice is RECOMMENDED to be present in a *FOCUS dataset* when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyContractedUnitPrice MAY be present in a *FOCUS dataset* in all other cases.
* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyContractedUnitPrice nullability is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice adheres to the following additional requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.
* Discrepancies in PricingCurrencyContractedUnitPrice, [ContractedCost](#contractedcost), or [PricingQuantity](#pricingquantity) MAY exist when ChargeClass is "Correction".

### Normative Text v1.3

## Requirements

PricingCurrencyContractedUnitPrice adheres to the following requirements:

* PricingCurrencyContractedUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * PricingCurrencyContractedUnitPrice is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyContractedUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyContractedUnitPrice nullability is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
  * PricingCurrencyContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice adheres to the following additional requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.

### Diff

-The PricingCurrencyContractedUnitPrice column adheres to the following requirements:
+## Requirements
 
-* PricingCurrencyContractedUnitPrice presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
-  * PricingCurrencyContractedUnitPrice MUST be present in a *FOCUS dataset* when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
-  * PricingCurrencyContractedUnitPrice is RECOMMENDED to be present in a *FOCUS dataset* when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
-  * PricingCurrencyContractedUnitPrice MAY be present in a *FOCUS dataset* in all other cases.
+PricingCurrencyContractedUnitPrice adheres to the following requirements:
+
+* PricingCurrencyContractedUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
+  * PricingCurrencyContractedUnitPrice MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
+  * PricingCurrencyContractedUnitPrice is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
+  * PricingCurrencyContractedUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
 * PricingCurrencyContractedUnitPrice MUST be of type Decimal.
 * PricingCurrencyContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
 * PricingCurrencyContractedUnitPrice nullability is defined as follows:
+  * PricingCurrencyContractedUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
   * PricingCurrencyContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
+  * PricingCurrencyContractedUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
   * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".