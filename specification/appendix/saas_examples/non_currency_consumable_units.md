# Non-Currency Consumable Units

Some providers offer services where the consumption of resources is not directly tied to a currency rate. Instead, another consumable unit is used like a currency, such as tokens, credits, or points. These consumable units are purchased at a currency rate and are consumed based on the usage of the service.

## Scenario

ACME provides a SaaS service where rather than purchased items or usage rates being specified in terms of currency per unit, they are specified in terms of another consumable unit such as tokens. Customers of Awesome Corp agree to purchase these units for a currency rate. The consumption of these tokens are determined by not a dollar figure rate but a token rate. AwesomeCorp features consumed tokens at different rates.

* Token Consumption:
  * Customer contracts include allocations of tokens at a dollar rate and usage results in depletion of these tokens.
  * Once tokens are fully depleted, additional tokens can be purchased.
  * Token usage above allocation results in a negative balance and a payable invoice for the additional tokens.

* Currently-Provided Billing Artifacts:
  * Token and Usage Data: High granularity data showing the amount of credits used regardless of balance for all applicable usage in the product
  * Token Statements: A monthly statement showing the balance of tokens. No currency figures provided.
  * Invoices: Invoices are provided for all purchases of tokens and any other purchases made by the customer.

## Key Factors

* The original purchase and corresponding invoice must align to a purchase record in the supplied FOCUS dataset
* All usage consume tokens
* The token to currency rate will not be the same for each allocation of credit, depending on bulk, overage, or type factors.

## Initial Purchase Records in FOCUS

On April 1st, 2025, ACME executes a contract  and invoices AwesomeCorp $205,000. The sale includes the following items to AwesomeCorp:

* 100000 tokens at $2.00 per token

Entries in the FOCUS dataset: [Initial Purchase Token Allocation](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788)

## Usage Records IN FOCUS

On April 2nd, 2025, ACME's consumption billing system calculates and provides usage and a resource level for the usage of 3 different resources and their applicable SKUS:

* 245 Feature Q Executions which
  * SKU Rate is 1 usage unit = 1 token
* 5 Feature Z Executions
  * SKU Rate is 1 usage unit = 2 tokens
* 120 Feature X Tokens
  * SKU Rate is 1 usage unit = 0.5 tokens

## Token Depletion Resulting in Additional Purchase Credits

In September 2025, AwesomeCorp has fully depleted their tokens and are required to purchase 1500 additional tokens. ACME invoices AwesomeCorp $3000 on October 5th, to compensate for a credit balance of -1500.

Entries in the FOCUS dataset: [Initial Purchase Token Allocation](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788)
