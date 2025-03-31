# Column: PricingCurrencyListUnitPrice

## References and Resources

None

## Discussion / Scratch space

An exchange rate reflective of List Cost can be calculated by the following:

`PricingToBillingListExchangeRate` = `ListUnitPrice` / `PricingCurrencyListUnitPrice`

List Cost can be denominated in [Pricing Currency](#pricingcurrency) through the following calculation:

`PricingCurrencyListCost` = `ListCost` * `ListUnitPrice` / `PricingCurrencyListUnitPrice`
