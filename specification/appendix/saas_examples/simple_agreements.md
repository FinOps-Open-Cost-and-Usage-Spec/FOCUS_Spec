# Simple SaaS Agreements

Many SaaS providers provide simple contract terms, therefore don't need to support complex scenarios like spend commitments or pricing strategies in their billing data.

The scenarios described below illustrate how a FOCUS-compliant dataset should look for simple SaaS agreement scenarios (these scenarios may not be specific to SaaS agreements only).

## Scenario A2: Invoice Up-front for a Quantity of a Service

ACME Corp offers its customer the ability to purchase a fixed quantity of licenses for their service. ACME provides AwesomeCorp with a single invoice for their usage. ACME does not provide detailed cost and usage reports to AwesomeCorp throughout the Charge Period after the initial purchase.

On April 1st, 2025, ACME executes a contract and invoices AwesomeCorp &dollar;50,000 (Billed Cost) for a Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also &dollar;50,000.

**Example FOCUS dataset:** On April 1st 2025, Acme Corp provides the following FOCUS dataset for the above transaction: [Invoice up-front entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803&range=A11)

Note the following details in the dataset:

* The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
* A single charge representing the total payment for the 12-month agreement is charged in the first invoice. Billed Cost and Effective Cost are both realized in the same record since detailed usage records will not be provided during the 12-month period to realize amortized portions of this up-front payment.
* The single charge provided includes a ListUnitPrice for the licenses and a Pricing Quantity.

## Scenario A3: Additional Purchase Records Provided in the SaaS Provider's FOCUS Data

On June 1st 2025 ACME provides the following records due to AwesomeCorp's &dollar;1,000 mid-contract purchase of an additional 10 licenses for the same Charge Period (April 1st 2025 to April 1st 2026).

**Example FOCUS dataset:** [Additional license purchase entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803&range=A14)

Note the following additional details in the dataset:

* The Charge Period is still April 1st 2025 to April 1st 2026. The Billing Period is now the month of June 2025 (when the additional licenses were ordered) and therefore will appear in the June 2025 invoice.

## Scenario B: Billed in Arrears for a Quantity of a Service

Similar to Scenario A above, ACME Corp offers its customer the ability to purchase their service with a fixed quantity of licenses. However, in Scenario B, ACME issues the invoice at the end of the usage period.

On April 1st, 2026, ACME invoices AwesomeCorp &dollar;50,000 (Billed Cost) for the Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also &dollar;50,000.

**Example FOCUS dataset:** [Billed in arrears entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803&range=A17)

Note the following additional details in the dataset:

* The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is now the month of March 2026 (since this charge is invoiced as of the last month of the Charge Period).
