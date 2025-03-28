# Column: PricingToBillingEffectiveExchangeRate

## References and Resources

None

## Discussion / Scratch space

The Pricing To Billing Effective Exchange Rate can indeed be calculated through the use of two other columns in the specification.  

`PricingToBillingEffectiveExchangeRate` = `EffectiveCost` / `PricingCurrencyEffectiveCost`

However, some involved in these discussions felt it would be helpful to explicitly state the exchange rate.  Per Mike F:

> My understanding was to make the existing exchange rate in the PR to be clear it is related to the EffectiveCost column and at this stage avoid the addition of any exchange rates for the Unit cost columns and lean on explanations on how to calculate the exchange rates for these lines to the use case library. This leaves the possibly for those other exchange rates to be added later if there is demand and value in adding them. From the conversations I have had I believe the practitioner is looking for the exchange rate when dealing with national currencies so this special extra handling in FOCUS now is clearer for the common use case vs leaving it up to manual calculation.
