## Diff

ListCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* ListCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ListCost MUST be of type Decimal.
* ListCost MUST conform to NumericFormat requirements.
* ListCost MUST NOT be null.
[-* ListCost MUST be a valid decimal value.-]
* ListCost MUST be denominated in the BillingCurrency.
* When ListUnitPrice is null, ListCost [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ListCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the ListCost of those related *charges*.
  * ListCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [-[BilledCost](#billedcost).-]{+[BilledCost](#datasets.costandusage.billedcost).+}
* ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.

