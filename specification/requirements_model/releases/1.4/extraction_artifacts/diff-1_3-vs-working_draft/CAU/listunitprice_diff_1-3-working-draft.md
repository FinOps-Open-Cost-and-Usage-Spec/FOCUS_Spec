## Diff

ListUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.-]
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to NumericFormat requirements.
* ListUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ListUnitPrice MUST be null when SkuPriceId is null.
  * ListUnitPrice MUST be null when ChargeCategory is "Tax".
  * ListUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
* ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.

