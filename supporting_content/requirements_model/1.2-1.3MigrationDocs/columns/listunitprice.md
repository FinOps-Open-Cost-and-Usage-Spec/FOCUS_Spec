## ListUnitPrice

### Normative Text v1.2

The ListUnitPrice column adheres to the following requirements:

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY exist when ChargeClass is "Correction".


### Normative Text v1.3 

## Requirements

ListUnitPrice adheres to the following requirements:

* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
* [ListCost](#listcost) MUST equal the product of ListUnitPrice and [PricingQuantity](#pricingquantity) when ListUnitPrice is not null and PricingQuantity is not null.

### Diff

-The ListUnitPrice column adheres to the following requirements:
+## Requirements
 
-* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
+ListUnitPrice adheres to the following requirements:
+
+* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.
 * ListUnitPrice MUST be of type Decimal.
 * ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
 * ListUnitPrice nullability is defined as follows:
+  * ListUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
   * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
+  * ListUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
   * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
   * ListUnitPrice MAY be null in all other cases.
 * When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
   * ListUnitPrice MUST be a non-negative decimal value.
   * ListUnitPrice MUST be denominated in the BillingCurrency.
-  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
-  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY exist when ChargeClass is "Correction".
+* [ListCost](#listcost) MUST equal the product of ListUnitPrice and [PricingQuantity](#pricingquantity) when ListUnitPrice is not null and PricingQuantity is not null.

