## ContractedCost

### Normative Text 1.2

The ContractedCost column adheres to the following requirements:

* ContractedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is null, ContractedCost adheres to the following additional requirements:
  * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ContractedUnitPrice and PricingQuantity MUST match the ContractedCost when ContractedUnitPrice is not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ContractedCost, ContractedUnitPrice, or PricingQuantity MAY exist when ChargeClass is "Correction".

### Normative Text 1.3-cr

## Requirements

ContractedCost adheres to the following requirements:

* ContractedCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is null, ContractedCost adheres to the following additional requirements:
  * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.

### Diff

-The ContractedCost column adheres to the following requirements:
+## Requirements
 
-* ContractedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+ContractedCost adheres to the following requirements:
+
+* ContractedCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
 * ContractedCost MUST be of type Decimal.
 * ContractedCost MUST conform to [NumericFormat](#numericformat) requirements.
 * ContractedCost MUST NOT be null.
@@ -13,8 +15,7 @@ The ContractedCost column adheres to the following requirements:
 * When [ContractedUnitPrice](#contractedunitprice) is null, ContractedCost adheres to the following additional requirements:
   * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
   * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
-* The product of ContractedUnitPrice and PricingQuantity MUST match the ContractedCost when ContractedUnitPrice is not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
-* Discrepancies in ContractedCost, ContractedUnitPrice, or PricingQuantity MAY exist when ChargeClass is "Correction".
+* ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.