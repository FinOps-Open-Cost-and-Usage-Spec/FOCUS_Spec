# Non-Currency Consumable Units

Some providers offer services where the consumption of resources is not directly tied to a currency rate. Instead, another consumable unit is used like a currency, such as tokens, credits, or points. These consumable units are purchased at a currency rate and are consumed based on the usage of the service.

## Scenario

ACME provides a SAAS service where rather than purchased items or usage rates being specified in terms of currency per unit, they are specified in terms of another consumable unit such as tokens. Customers of Awesome Corp agree to purchase these units for a currency rate. The consumption of these tokens are determined by not a dollar figure rate but a token rate. AwesomeCorp offers different classes of tokens that cover different areas of their product.
- Token Types:
    - Standard tokens: These are the primary tokens that are consumed for most usage. Customer contracts balances include a continually depleted balance of standard tokens.
        - Z widget tokens: These are specialty tokens that are allocated for specific consumption of the z token feature, when depleted standard tokens are consumed
    - X tokens: These are tokens that are consumed for a specific for the X feature and do not consume any other credits once depleted. Customer contracts balances include a continually depleted balance of standard tokens.

- Currently-Provided Billing Artifacts:
    - Token and Usage Data: High granularity data showing the amount of credits used regardless of balance for all applicable usage in the product
    - Token Statements: A monthly statement showing the balance of all token types and the usage of each token type. Balances are at a token type and subtype level. No currency figures provided.
    - Invoices: Invoices are provided for all purchases of tokens and any other purchases made by the customer.

## Key Factors

- The original purchase and corresponding invoice must align to a purchase record in the supplied FOCUS dataset
- Because all usage consumes tokens, and tokens may be purchased at a different rate
- Tokens have the ability to be consumed in a waterfall approach
    - A usage may consume a primary type of token and then if depleted consume a secondary type of token.
- The token to currency rate will not be the same for each allocation of credit, depending on bulk, overage, or type factors.

-<TODO SNAGS>
- Effective cost is not optional but only considers amortization of upfront and committed purchase...but not blended rates
- Vendors that use tokens may not want to provide effective cost because cost attribution approaches differ by customer.
- Forward Allocations of tokens immediately invoiced are included in one invoice but may be allocated on a different schedule

## Initial Purchase Records in FOCUS
On April 1st, 2025, ACME executes a contract  and invoices AwesomeCorp $205,000. The sale includes the following items to AwesomeCorp:
- 100000 Standard tokens at $2.00 per token
- 1200 Standard - Specialized Z widget tokens at $0.00 per token, effectively giving AwesomeCorp 100 tokens worth of usage for the z widget per month before usage impacts their standard token balance. These are allocated to awesome corp in monthly 100 credit groups.
- 5000 X Tokens at $1.00 per token 5000 z widget specialty token.

Entries in the FOCUS dataset:

SEE: SCENARIO Initial Purchase Token Allocation https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788

## Recurring Allocations
As part of AwesomeCorp's contract with ACME, AwesomeCorp receives a monthly allocation of 100 Z widget tokens. These tokens are allocated on the first of each month.
<TODO>

## Usage Records IN FOCUS
On April 2nd, 2025, ACME's consumption billing system calculates and provies usage and a resource level for the usage of 3 different resouces and their applicable SKUS:
- 245 Feature Q Executions which
    - SKU Rate is 1 usage unit = 1 token
- 5 Feature Z Executions
    - SKU Rate is 1 usage unit = 2 tokens
- 120 Feature X Tokens
    - SKU Rate is 1 usage unit = 0.5 tokens

## Token Depletion Resulting in Additional Purchase Credits
In September 2025, AwesomeCorp has depleted their standard tokens and are required to purchase 1500 additional tokens. ACME invoices AwesomeCorp $3000 on October 5th, to compensate for a credit balance of -1500.


Entries in the FOCUS dataset:

SEE: SCENARIO Initial Purchase Token Allocation https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1940546788#gid=1940546788


The updated schema related metadata could look like this:


For an example of how ACME ensures the schema metadata reference requirement is met see: [Schema Metadata to FOCUS Data Reference](#schemametadatatofocusdatareference)
