# Column: PricingCurrencyEffectiveCost

## References and Resources

None

## Discussion / Scratch space

A so-called "effective" exchange rate from Pricing Currency to Billing Currency can be calculated through the use of two other columns in the specification:

* `PricingToBillingEffectiveExchangeRate` = `EffectiveCost` / `PricingCurrencyEffectiveCost`

Such a column was considered for inclusion in FOCUS 1.2.  However, the group decided to defer the inclusion of this exchange rate to a future release, when it could potentially be included in the specification alongside multiple other possible exchange rates, such as List and Contracted.  In the interim, those exchange rates can also be calculated from existing columns in the specification.  For example:

* `PricingToBillingListExchangeRate` = `ListUnitPrice` / `PricingCurrencyListUnitPrice`
* `PricingToBillingContractedExchangeRate` = `ContractedUnitPrice` / `PricingCurrencyContractedUnitPrice`


