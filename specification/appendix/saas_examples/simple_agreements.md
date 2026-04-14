# Simple SaaS Agreements

Many SaaS providers provide simple contract terms, therefore don't need to support complex scenarios like spend commitments or pricing strategies in their billing data.

The scenarios described below illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) should look for simple SaaS agreement scenarios (these scenarios may not be specific to SaaS agreements only).

## Scenario A1: Invoice Up-front for a Purchase of a Service

StackLens allows its customers to purchase their service for a term (in this case, a year) for a $10,000. StackLens provides Acme Corp with a single invoice for their usage. StackLens does not provide detailed cost and usage reports to Acme Corp throughout the Charge Period after the initial purchase.

Given that StackLens does not charge based on or track usage, its usage details are irrelevant to this scenario.

[**CSV Example**](/specification/data/saas_examples/simple_agreements/simple_saas_agreements_a1.csv)

Note the following details in the example dataset:

* The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
* A single charge representing the total payment for the 12-month agreement ($10,000) is charged in the first invoice. BilledCost and EffectiveCost are realized in the same record since detailed usage records will not be provided during the 12-month period to realize amortized portions of this up-front payment.
* The single charge record does not include a List Unit Price, Pricing Quantity, or SKU-related information. Alternatively, the Pricing Quantity could have been set to 1, and the List Unit Price could be the same as the total charge.
  
## Scenario A2: Invoice Up-front for a Quantity of a Service

StackLens offers its customer the ability to purchase a fixed quantity of licenses for their service. StackLens provides Acme Corp with a single invoice for their usage. StackLens does not provide detailed cost and usage reports to Acme Corp throughout the Charge Period after the initial purchase.

On April 1st, 2025, StackLens executes a contract and invoices Acme Corp $50,000 (Billed Cost) for a Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

[**CSV Example**](/specification/data/saas_examples/simple_agreements/simple_saas_agreements_a2.csv)

Note the following details in the example dataset:

* The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
* A single charge representing the total payment for the 12-month agreement is charged in the first invoice. Billed Cost and Effective Cost are both realized in the same record since detailed usage records will not be provided during the 12-month period to realize amortized portions of this up-front payment.
* The single charge provided includes a ListUnitPrice for the licenses and a Pricing Quantity.

## Scenario A3: Additional Purchase Records Provided in the SaaS Data Generator's FOCUS Dataset

On June 1st 2025 StackLens provides the following records due to Acme Corp's $1,000 mid-contract purchase of an additional 10 licenses for the same Charge Period (April 1st 2025 to April 1st 2026).

[**CSV Example**](/specification/data/saas_examples/simple_agreements/simple_saas_agreements_a3.csv)

Note the following additional details in the example dataset:

* The Charge Period is still April 1st 2025 to April 1st 2026. The Billing Period is now the month of June 2025 (when the additional licenses were ordered) and therefore will appear in the June 2025 invoice.

## Scenario B: Billed in Arrears for a Quantity of a Service

Similar to Scenario A above, StackLens offers its customer the ability to purchase their service with a fixed quantity of licenses. However, in Scenario B, StackLens issues the invoice at the end of the usage period.

On April 1st, 2026, StackLens invoices Acme Corp $50,000 (Billed Cost) for the Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

[**CSV Example**](/specification/data/saas_examples/simple_agreements/simple_saas_agreements_b.csv)

Note the following additional details in the example dataset:

* The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is now the month of March 2026 (since this charge is invoiced as of the last month of the Charge Period).

## Scenario C: Simple SaaS Agreement with Monthly Billing

Like Scenario A2 above, StackLens offers its customers the ability to purchase their service with a fixed quantity of licenses. However, in Scenario C, StackLens issues invoices at the end of each month (usage period).
For this scenario, contract terms additionally include the following terms:

* StackLens charges users monthly for the licenses that were consumed in that Billing Period
* The licenses are charged at $20 per license per month

Acme Corp's consumption looks like this:

* In April 2025, Acme Corp uses 505 licenses
* In May 2025, Acme Corp uses 650 licenses
* In June 2025, Acme Corp uses 635 licenses

[**CSV Example**](/specification/data/saas_examples/simple_agreements/simple_saas_agreements_c.csv)

Note the following additional details in the example dataset:

* The Charge Period and Billing Period are April 1st, 2025, to May 1st, 2025, for the first month. Subsequent months increment the Charge Period and Billing Period by one month to match the month the charges are incurred.
* Billed Cost and Effective Cost are the same value since there is no up-front payment to amortize
