# SaaS Spend Agreements

Many SaaS providers support billing models that allow (or in some cases require) consumers to agree to an amount to spend over a period. In some cases, customers receive a negotiated discount for usage during that period in exchange for the spend agreement. Spend agreements can have different payment models like billing in arrears or pre-paid contracts and may impose minimum spend requirements for parts of the agreement.

The scenarios described below illustrate how a FOCUS-compliant dataset should look for various spend agreement scenarios.

## Baseline Scenario

The following baseline conditions apply to the scenarios described below:

* AwesomeCorp has signed an agreement with SaaS provider Acme Co to use their database services
* On April 1 2025, AwesomeCorp agrees to spend &dollar;1200 (post-discounts) in the upcoming 12-months
* AwesomeCorp receives a 20% negotiated discount in return for the commitment
* Acme Co calculates the spend counted against the agreements after discounts (like the negotiated discounts). Other providers may use the cost after discounts i.e., using List Cost for calculating the spend commitment.

## Scenario A: Billed in arrears

For this scenario A, contract terms include the following terms in addition to the baseline scenario mentioned above:

* All charges will be billed in arrears at a monthly frequency

### Scenario A1: Billed in arrears with no minimum spend requirement per month

For this scenario, contract terms additionally include the following terms:

* Committed spend can be used anytime within the 1-year term

AwesomeCorp's consumption looks like this:

* In the first month, AwesomeCorp uses &dollar;48 of services (4 server hours). This usage has a List Cost of &dollar;60 (before discounts)
* In the following 2 months, AwesomeCorp has some more usage
* For the final 9 months, AwesomeCorp does not use Acme services

[**CSV Example**](/specification/data/saas_examples/spend_agreements/saas_spend_agreements_a1.csv)

Note the following details in the example dataset:

* A single charge representing the total unused amount from the 12-month agreement is charged during the final month of the 12-month term

### Scenario A2: Billed in arrears with a minimum spend requirement per month

The spend agreement with Acme requires the customer to spend a minimum amount in each Billing Period (monthly). Unused fees are charged per Billing Period when the consumption is below this level (use-it or lose-it). For this scenario, contract terms additionally include the following terms:

* A minimum of &dollar;60 needs to be spent each month

AwesomeCorp's consumption looks like this:

* In the first month, the AwesomeCorp uses &dollar;48 of services (4 server hours). This usage has a List Cost of &dollar;60 (before discounts). For this month, Acme charges &dollar;12 (ListCost of &dollar;15) for not meeting the monthly minimum
* In the following 2 months, AwesomeCorp has usage at or above the minimum requirement
* For the final 9 months, AwesomeCorp does not use Acme services

[**CSV Example**](/specification/data/saas_examples/spend_agreements/saas_spend_agreements_a2.csv)

Note the following details in the example dataset:

* A monthly charge representing the unused minimum monthly amount is charged during months 4 through 11 of the 12-month term
* The final month has a charge that captures the overall unmet spend requirement for the 12-month contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.

## Scenario B: Prepaid contract

For this scenario B, contract terms include the following terms in addition to the baseline scenario mentioned above:

* The charges will be billed in arrears using monthly invoices

### Scenario B1: Prepaid with no minimum spend requirement per month

Scenario B1 is similar to scenario A1 with the difference being that it's a pre-paid contract.

[**CSV Example**](/specification/data/saas_examples/spend_agreements/saas_spend_agreements_b1.csv)

Note the following details in the example dataset:

* A purchase record for the initial &dollar;1200 payment is present representing List, Billed, and Contracted cost of the purchase
* The charge for the unused amount has a &dollar;0 BilledCost (since the total amount was billed with the prepayment). However, the charge captures the unused portion as an EffectiveCost.
* The unused charge rows apply to the entire Charge Period the contract was signed for.
* This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in [ListCost](#listcost) and [ContractedCost](#contractedcost)) where either the [ChargeType](#chargetype) Purchase or Usage rows need to be excluded depending on the reporting scenario.

### Scenario B2: Prepaid with a minimum spend requirement per month

Scenario B2 is similar to A2 with the difference being that it's a pre-paid contract.

[**CSV Example**](/specification/data/saas_examples/spend_agreements/saas_spend_agreements_b2.csv)

Note the following details in the example dataset:

* A purchase record for the initial &dollar;1200 payment is present representing List, Billed, and Contracted cost of the purchase
* The monthly charge for the unused amount has a &dollar;0 BilledCost (since the total amount was billed with the prepayment). However, the charge captures the unused portion as an EffectiveCost.
* The final month has a charge that captures the overall unmet spend requirement for the 12-month contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.
* This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in [ListCost](#listcost) and [ContractedCost](#contractedcost)) where either the Purchase or Usage rows need to be excluded depending on the reporting scenario.
