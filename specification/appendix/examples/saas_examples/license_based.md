# License-Based Transactions and FOCUS Data

Many vendors provide the option to purchase their products on a license-seat basis, allowing the buyer to procure a number of licenses for usage, usually based on a number of expected users. In this case, the vendor's FOCUS would include records that express the cost of the purchase aligned with the number of licenses purchased from the SAAS vendor. 

## Key Factors
- The original -- and any additional -- purchase record(s) and corresponding invoice(s) must align to a purchase record in the supplied FOCUS dataset.

## Scenario A

ACME Corp offers its customer the ability to purchase their service with a fixed quantity of licenses. ACME provides AwesomeCorp with a Single invoice for their usage; ACME also provides a detailed usage report to AwesomeCorp. 

On April 1st, 2025, ACME executes a contract and invoices AwesomeCorp $100,000, public list cost of their purchase items would be $150,000.
The contract includes the following items:
- $50,000 for 500 Licenses

## Initial Purchase Record
On April 1st, Acme Corp provides the following records in their FOCUS data for the $100,000 usage bill:

Entries in the FOCUS dataset:
SEE: License Pre-Purchase FOCUS Entries https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803

## Additional Purchase Records Provided in the SAAS Provider's FOCUS Data

On June 1st ACME provides the following records due to AwesomeCorp's $10,000 mid-contract purchase of an additional 100 licenses. 

Entries in the FOCUS dataset:
SEE: Additional License Purchase FOCUS Entries https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803

## Scenario B

Same as above, ACME Corp offers its customer the ability to purchase their service with a fixed quantity of licenses. ACME provides AwesomeCorp with a Single invoice for their usage; ACME also provides a detailed usage report to AwesomeCorp. Distinct in this scenario, ACME only issues the invoice at the end of the usage period. 

On April 1st, 2025, ACME audits the AwesomeCorp usage for the previous year executes a contract and invoices AwesomeCorp $100,000, public list cost of their purchase items would be $150,000.
The contract includes the following items:
- $50,000 for 500 Licenses

## Initial Purchase Record
On April 1st, Acme Corp provides the following records in their FOCUS data for the $100,000 usage bill:

Entries in the FOCUS dataset:
SEE: License Post-Purchase FOCUS Entries https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803
