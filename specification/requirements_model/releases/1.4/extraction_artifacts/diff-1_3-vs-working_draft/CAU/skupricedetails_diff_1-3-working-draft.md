## Diff

SkuPriceDetails [-adheres-]{+MUST adhere+} to the following requirements:

* SkuPriceDetails MUST[-be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.-]
[-* SkuPriceDetails MUST-] conform to [-[KeyValueFormat](#key-valueformat)-]{+[KeyValueFormat](#attributes.key-valueformat)+} requirements.
* SkuPriceDetails property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * SkuPriceDetails MUST be associated with a given SkuPriceId.
  * SkuPriceDetails MUST include the FOCUS-defined SKU Price property when an equivalent property is included as a custom property.
  * SkuPriceDetails MUST NOT include properties that are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all custom SKU Price properties that are applicable to the corresponding SkuPriceId when there is no equivalent FOCUS-defined property.
  * SkuPriceDetails MAY include properties that are already captured in other dedicated columns.
  * SkuPriceDetails properties for a given SkuPriceId {+MUST+} adhere to the following[-additional-] requirements:
    * Existing SkuPriceDetails properties SHOULD remain consistent over time.
    * Existing SkuPriceDetails properties SHOULD NOT be removed.
    * Additional SkuPriceDetails properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable *SKUs* having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property value MUST represent the value for a single [-[PricingUnit](#pricingunit)-]{+[PricingUnit](#datasets.costandusage.pricingunit)+} when the property holds a numeric value.
* FOCUS-defined SKU Price properties {+MUST+} adhere to the following[-additional-] requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST represent the value for a single PricingUnit, denominated in the unit of measure specified for that property when the property holds a numeric value.

