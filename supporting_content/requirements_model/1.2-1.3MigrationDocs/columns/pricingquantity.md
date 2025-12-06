## PricingQuantity

### Normative Text v1.2

The PricingQuantity column adheres to the following requirements:

* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* PricingQuantity nullability is defined as follows:
  * PricingQuantity MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.
* When PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
  * PricingQuantity MUST be a valid decimal value.
  * The product of PricingQuantity and a unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) MUST match the corresponding cost metric (e.g., [ContractedCost](#contractedcost)) when the unit price is not null and ChargeClass is not "Correction".
* Discrepancies in PricingQuantity, unit prices (e.g., ContractedUnitPrice), or costs (e.g., ContractedCost) MAY exist when ChargeClass is "Correction".

### Normative Text v1.3

## Requirements

PricingQuantity adheres to the following requirements:

* PricingQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* PricingQuantity nullability is defined as follows:
  * PricingQuantity MUST be null when [SkuPriceId](#skupriceid) is null.
  * PricingQuantity MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.
* PricingQuantity MUST be a valid decimal value when not null.
* Cost metric (e.g., [ContractedCost](#contractedcost)) MUST equal the product of the corresponding unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) and PricingQuantity when the unit price is not null and PricingQuantity is not null.

### Diff

-The PricingQuantity column adheres to the following requirements:
+## Requirements
 
-* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+PricingQuantity adheres to the following requirements:
+
+* PricingQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
 * PricingQuantity MUST be of type Decimal.
 * PricingQuantity MUST conform to [NumericFormat](#numericformat) requirements.
 * PricingQuantity nullability is defined as follows:
+  * PricingQuantity MUST be null when [SkuPriceId](#skupriceid) is null.
   * PricingQuantity MUST be null when [ChargeCategory](#chargecategory) is "Tax".
   * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
   * PricingQuantity MAY be null in all other cases.
-* When PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
-  * PricingQuantity MUST be a valid decimal value.
-  * The product of PricingQuantity and a unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) MUST match the corresponding cost metric (e.g., [ContractedCost](#contractedcost)) when the unit price is not null and ChargeClass is not "Correction".
-* Discrepancies in PricingQuantity, unit prices (e.g., ContractedUnitPrice), or costs (e.g., ContractedCost) MAY exist when ChargeClass is "Correction".
+* PricingQuantity MUST be a valid decimal value when not null.
+* Cost metric (e.g., [ContractedCost](#contractedcost)) MUST equal the product of the corresponding unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) and PricingQuantity when the unit price is not null and PricingQuantity is not null.