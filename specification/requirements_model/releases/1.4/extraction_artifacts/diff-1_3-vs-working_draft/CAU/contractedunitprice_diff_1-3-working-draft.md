## Diff

ContractedUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractedUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports negotiated pricing concepts.-]
[-* ContractedUnitPrice adheres to the following additional requirements:-]
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to NumericFormat requirements.
* ContractedUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractedUnitPrice MUST be null when SkuPriceId is null.
  * ContractedUnitPrice MUST be null when ChargeCategory is "Tax".
  * ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
[-* [ContractedCost](#contractedcost) MUST equal the product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) when ContractedUnitPrice is not null and PricingQuantity is not null.-]