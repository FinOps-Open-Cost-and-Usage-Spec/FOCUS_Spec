## Diff

ContractedCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractedCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [-[ContractedUnitPrice](#contractedunitprice)-]{+[ContractedUnitPrice](#datasets.costandusage.contractedunitprice)+} is null, ContractedCost [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [-[BilledCost](#billedcost).-]{+[BilledCost](#datasets.costandusage.billedcost).+}
* ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.

