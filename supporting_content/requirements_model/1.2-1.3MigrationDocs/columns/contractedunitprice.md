## ContractedUnitPrice

### Normative Text v1.2

The ContractedUnitPrice column adheres to the following requirements:

* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ContractedUnitPrice nullability is defined as follows:
  * ContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) when PricingQuantity is not null and ChargeClass is not "Correction".
* Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY exist when ChargeClass is "Correction".


### Normative Text v1.3

## Requirements

ContractedUnitPrice adheres to the following requirements:

* ContractedUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports negotiated pricing concepts.
* ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ContractedUnitPrice nullability is defined as follows:
  * ContractedUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
  * ContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
* [ContractedCost](#contractedcost) MUST equal the product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) when ContractedUnitPrice is not null and PricingQuantity is not null.

### Diff

-The ContractedUnitPrice column adheres to the following requirements:
+## Requirements
 
-* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
+ContractedUnitPrice adheres to the following requirements:
+
+* ContractedUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports negotiated pricing concepts.
 * ContractedUnitPrice adheres to the following additional requirements:
 * ContractedUnitPrice MUST be of type Decimal.
 * ContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
 * ContractedUnitPrice nullability is defined as follows:
+  * ContractedUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
   * ContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
+  * ContractedUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
   * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
   * ContractedUnitPrice MAY be null in all other cases.
 * When ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
   * ContractedUnitPrice MUST be a non-negative decimal value.
   * ContractedUnitPrice MUST be denominated in the BillingCurrency.
-  * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) when PricingQuantity is not null and ChargeClass is not "Correction".
-* Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY exist when ChargeClass is "Correction".
+* [ContractedCost](#contractedcost) MUST equal the product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) when ContractedUnitPrice is not null and PricingQuantity is not null.