# SaaS Spend Agreements

Many SaaS providers support billing models that utilize a non-standard currency unit such as credits, tokens or points. The provider sells these tokens at a currency rate. Usage of their product consumes these tokens. 

The scenarios described below illustrate how a FOCUS-compliant dataset should look for various scenarios where a provider utilizes this pricing model.

## Baseline Scenario

The following baseline conditions apply to the scenarios described below:

* AwesomeCorp has signed an agreement with SaaS provider Acme Co to use their SaaS platform services
* Acme Co offers a token-based pricing model for their services, requiring a purchase of tokens in advance of usage. 
* Acme Co requires purchase of additional tokens in the event of usage exceeding purchased tokens.
* Acme Co publicly lists the cost of their tokens at &dollar;2 per token.
* Acme Co publicly lists their usage to token rates. These rates are as follows:
  * 1 Q Widget Execution = 1 token
  * 1 Z Widget Execution = 2 tokens
  * 1 Workflow Operation = 3 tokens

## Scenario A: Tokens Not Offered at a Discount

For this scenario, contract terms include the following terms in addition to the baseline scenario mentioned above:
    * Acme Corp offers no discount for purchased tokens

## Scenario A1: Initial Purchase of Tokens Non Discounted

For this scenario for the initial purchase of tokens the purchase executed is as follows:
* On April 1, 2025, AwesomeCorp agrees to purchase 100,000 tokens at &dollar;2 per token for a total spend &dollar;200,000. These tokens are only valid for 12 months.

**Example FOCUS dataset:** [Initial Purchase of Tokens without a Discount](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=2:3)

Note the following details in the dataset:

* The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
* Because Acme Co uses token based pricing for usage and publishes their token price in terms of dollars and their usage cost in terms of tokens, their FOCUS dataset includes the columns PricingCurrency,PricingCurrencyContractedUnitPrice, PricingCurrencyEffectiveCost, and PricingCurrencyListUnitPrice.
* A single charge representing the total payment for the initial token purchase agreement (&dollar;200,000) is charged in the first invoice. * 
  * ListCost, BilledCost, and Contracted cost of the purchase are all represented in this charge, however EffectCost is zero since the tokens are not yet consumed.
* Pricing Quantity is set to the total tokens purchased
* Because Awesome Corp is paying the list price ListUnitPrice and ContractedUnitPrice are all set to the same value of &dollar;2.

## Scenario A2: Usage of Tokens that were Purchased Without a Discount

Awesome Corp uses ACME's services consuming tokens as follows in the first day:
* 245 executions of Q Widget
* 5 executions of Z widget
* 120 operations of Workflow

**Example FOCUS dataset:** [Usage of Tokens that were Purchased Without a Discount](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=5:8)

Note the following details in the dataset:

* The Charge Period is April 1st 2025 - April 2nd 2025. The Billing Period is the month of April 2025.
* PricingCurrency for these usage charges reflects the per usage token price of the particular usage
* PricingQuantity Reflects the amount of usage of the Pricing Unit for each charge and is equivalent to consumed quantity. While this is relevant to this example there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same.
* Because Awesome Corp's usage includes no discount on usage to token rates, PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are equivalent.

## Scenario B: Tokens offered at a Discount

For this scenario, contract terms include the following terms in addition to the baseline scenario mentioned above:
* Acme Corp offers a discount for purchased tokens

## Scenario B1: Initial Purchase of Tokens at a Discount

For this scenario for the initial purchase of tokens the purchase executed is as follows:
* On April 1, 2025, AwesomeCorp agrees to purchase 100,000 tokens at &dollar;1 per token for a total spend &dollar;100,000. These tokens are only valid for 12 months.

**Example FOCUS dataset:** [Initial Purchase of Tokens at a Discount](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=11:12)

Note the following details in the dataset:

* The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
* Because Acme Co uses token based pricing for usage and publishes their token price in terms of dollars and their usage cost in terms of tokens, their FOCUS dataset includes the columns PricingCurrency,PricingCurrencyContractedUnitPrice, PricingCurrencyEffectiveCost, and PricingCurrencyListUnitPrice.
* A single charge representing the total payment for the initial token purchase agreement (&dollar;100,000) is charged in the first invoice.
    * ListCost, BilledCost, and Contracted cost of the purchase are all represented in this charge, however EffectCost is zero since the tokens are not yet consumed.
* Pricing Quantity is set to the total tokens purchased
* Because Awesome Corp is receiving a discount on the token price, the ListUnitPrice is set to &dollar;2 and the ContractedUnitPrice is set to &dollar;1. A ListCost of (&dollar;200,000) and ContractedCost (&dollar;100,000) reflect the cost of the tokens at the list price and contracted price respectively. The BilledCost is set to &dollar;100,000 since this is the amount that Awesome Corp will be charged for the purchase of tokens.

## Scenario B2: Usage of Tokens that were Purchased at a Discount

Awesome Corp uses ACME's services consuming tokens as follows in the first day:
* 245 executions of Q Widget
* 5 executions of Z widget
* 120 operations of Workflow

**Example FOCUS dataset:** [Usage of Tokens that were Purchased at a Discount](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=14:17)

Note the following details in the dataset:

* PricingQuantity Reflects the amount of usage of the Pricing Unit for each charge and is equivalent to consumed quantity. While this is relevant to this example there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same.
* Because Awesome Corp's usage includes no discount on usage to token rates, PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are equivalent.

## Scenario B3: Usage of Tokens that were Purchased at a Discount

Awesome Corp uses ACME's services consuming tokens as follows in the first day:
* 245 executions of Q Widget
* 5 executions of Z widget
* 120 operations of Workflow

Additionally, Acme Co offers a modified usage to token ratio for one of their services as follows:
* 1 Workflow Operation = 2 tokens

**Example FOCUS dataset:** [Usage of Tokens with a Modified Rate](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=19:22)

Note the following details in the dataset:

* Because of the modified rate for Workflow Operations, the PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are different for this charge. The ContractedUnitPrice is set to &dollar;1 and the ListUnitPrice is set to &dollar;2. 
* The PricingCurrencyEffectiveCost is 240 tokens for this charge, which is less that example B2 above due to the modified rate. 
* ListCost reflects the cost of the charge at both the list cost and the list usage to token ratio. 

## Scenario C: Handling Overages

For this scenario, Awesome Corp has exceeded their purchased tokens on October 1st 2025 by 1500 tokens and Acme Co has charged them for the overage. The following conditions apply:
* Acme Co has charged Awesome Corp for the cost of tokens at the list price of &dollar;2 per token and this purchase is effective from April 1st 2025 to The date of the Purchase October 1st 2025.
* Awesome Corp purchases an additional 25,000 token to facilitate usage to the end of their contract. These tokens are valid from October 1st 2025 to March 30th 2026. 

**Example FOCUS dataset:** [Handling Overages](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788&range=25:27)

Note the following details in the dataset:
* The Charge Period for the Overage Purchase is April 1st 2025 - October 1st 2025. This is because the overage charge is to cover the period of time the overage token purchase is applicable to. 
* The Charge Period for the Additional Purchase is October 1st 2025 - April 1st 2026. This is because the additional purchase is to cover the period of time the additional token purchase is applicable to. Because end dates are exclusive a ChargePeriodEnd is April 1st 2026.
