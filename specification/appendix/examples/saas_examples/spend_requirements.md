# Spend Requirements

Many SaaS and other service providers support billing models that allow (on in some cases require) consumers to commit to use an amount of spend over a period. In some cases, these spend requirements provide customers a negotiated discount in exchange for the requirement. These spend requirements support different payment models (billed in arrears or pre-paid) and may contain further requirements for minimum periodic spend requirements.

## Baseline Scenario

The scenarios described below show how a FOCUS-compliant dataset should look for various scenarios when spend requirements are involved. The following baseline conditions apply to all scenarios described here. Below this section, we look at how some variations of this baseline scenario can be presented in a FOCUS-compliant dataset.

* AwesomeCorp has signed on with SaaS provider Acme Co to use their database services
* On April 1 2025, AwesomeCorp agrees to spend $1200 (post-discounts) in the upcoming 12-months
* AwesomeCorp receives a 20% negotiated discount in return for the commitment
* In this section, spend requirements are calculated *after discounts* (like the negotiated discounts) are applied. Providers could use cost prior to discounts i.e., List Cost for their committed spend calculations as well.

## Scenario A: Billed in arrears

For this scenario, the contract terms include the following items in addition to the baseline scenarios:

* The charges will be billed in arrears using monthly invoices

### Scenario A1: Billed in arrears with no minimum spend requirement per month

For this scenario, the contract terms additionally include the following items:

* Committed spend can be used anytime within the 1-year

AwesomeCorps consumption looks like this:

* In the first month, the AwesomeCorp uses $48 of services (4 server hours). This usage has a List Cost of $60 (before discounts).
* In the following 2 months, AwesomeCorp has more usage
* After that, AwesomeCorp does not use Acme services and gets a charge on the final month for the unused portion of the $1200 requirement

#### Example FOCUS data

See an example dataset for Scenario A1 [here](https://docs.google.com/spreadsheets/d/1H69HmngVv-mKpFR-sveY-fSAdR49syqQd7AKOPPQ64A/edit?gid=1740845023#gid=1740845023&range=A15)

Note the following details in the dataset:

* Unused fees are charged at the end of the 12-month term with a row that captures the entire charge period the contract was signed for.

### Scenario A2: Billed in arrears with a minimum spend requirement per month

A minimum spend requirement requires a customer to spend at least the minimum amount in a given Billing Period. Fees are applied per Billing Period when the consumption is below this level (use-it or lose-it). For this scenario, the contract terms include the following items:

* A minimum of a $60 needs to be spent each month

AwesomeCorps consumption looks like this:

* In the first month, the AwesomeCorp uses $48 of services (4 server hours). This usage has a List Cost of $60 (before discounts). For this month, Acme charges 12$ (ListCost of $15) for not meeting the monthly minimum.
* In the following 2 months, AwesomeCorp has usage at or above the minimum requirement
* In the following 9 months, AwesomeCorp does not use Acme services and gets a charge each month for the minimum spend of $60.
* In the final month of the contract ChargePeriod, Acme charges the total unused portion of the spend requirement

#### Example FOCUS data

See an example dataset for Scenario A2 [here](https://docs.google.com/spreadsheets/d/1H69HmngVv-mKpFR-sveY-fSAdR49syqQd7AKOPPQ64A/edit?gid=1740845023#gid=1740845023&range=A25)

Note the following details in the dataset:

* Unused fees are charged monthly with a row that captures the unmet monthly minimum spend.
* The final month has a charge that captures the overall unmet spend requirement for the contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.

## Scenario B: Prepaid contract

For this scenario, the contract terms include the following items in addition to the baseline scenarios:

* The charges will be billed in arrears using monthly invoices

### Scenario B1: Prepaid with no minimum spend requirement per month

Scenario B1 is similar to A1 with the difference being that it's a pre-paid contract.

#### Example FOCUS data

See an example dataset for Scenario A1 [here](https://docs.google.com/spreadsheets/d/1H69HmngVv-mKpFR-sveY-fSAdR49syqQd7AKOPPQ64A/edit?gid=1740845023#gid=1740845023&range=A46)

Note the following details in the dataset:

* There is a purchase record for the initial $1200 payment
* Unused fees are charged without a BilledCost at the end of the 12-month term with a row that captures the entire charge period the contract was signed for.
* This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in [ListCost](#ListCost) and [ContractedCost](#ContractedCost)) where either the Purchase or Usage rows need to be excluded depending on the reporting scenario.

### Scenario B2: Billed in arrears with a minimum spend requirement per month

Scenario B2 is similar to A2 with the difference being that it's a pre-paid contract.

#### Example FOCUS data

See an example dataset for Scenario A2 [here](https://docs.google.com/spreadsheets/d/1H69HmngVv-mKpFR-sveY-fSAdR49syqQd7AKOPPQ64A/edit?gid=1740845023#gid=1740845023&range=A58)

Note the following details in the dataset:

* There is a purchase record for the initial $1200 payment
* Unused fees are charged monthly with a row that captures the unmet monthly minimum spend.
* The final month has a charge that captures the overall unmet spend requirement for the contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.
* This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in [ListCost](#ListCost) and [ContractedCost](#ContractedCost)) where either the Purchase or Usage rows need to be excluded depending on the reporting scenario.
