# License-Based Transactions and FOCUS Data

Many vendors provide the option to purchase their products on a license-seat basis, allowing the buyer to procure a number of licenses for usage, usually based on a number of expected users. In this case, the vendor's FOCUS-compliant billing data would include records that express the cost of the purchase aligned with the number of licenses purchased from the SaaS vendor.

## Key Factors

* The original and any additional purchase record(s) and corresponding invoice(s) must contain the purchase record in the supplied FOCUS dataset.

## Scenario A: Invoice Up-front

ACME Corp offers its customer the ability to purchase their service with a fixed quantity of licenses. ACME provides AwesomeCorp with a Single invoice for their usage. ACME also provides a detailed usage report to AwesomeCorp.

On April 1st, 2025, ACME executes a contract and invoices AwesomeCorp $50,000 (Billed Cost) for a Charge Period of April 1st 2025 - April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

The contract includes the following items:

* $50,000 for 500 Licenses

### Example FOCUS Data

On April 1st 2025, Acme Corp provides the following FOCUS dataset for the above transaction: [License Pre-Purchase FOCUS Entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803)

### Additional Purchase Records Provided in the SaaS Provider's FOCUS Data

On June 1st ACME provides the following records due to AwesomeCorp's $1,000 mid-contract purchase of an additional 10 licenses for the same Charge Period (April 1st 2025 - April 1st 2026).

The contract includes the following items:

* $1,000 for 10 Licenses

### Example FOCUS Data

On April 1st 2025, Acme Corp provides the following FOCUS dataset for the above transaction: [Additional License Purchase FOCUS Entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803)

## Scenario B: Billed in Arrears

Similar to the case above, ACME Corp offers its customer the ability to purchase their service with a fixed quantity of licenses. However, in this scenario, ACME issues the invoice at the end of the usage period.

On April 1st, 2026, ACME executes a contract and invoices AwesomeCorp $50,000 (Billed Cost) for a Charge Period of April 1st 2025 - April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

The contract includes the following items:

* $50,000 for 500 Licenses

### Example FOCUS Data

On April 1st 2026, Acme Corp provides the following records in their FOCUS data for the $50,000 usage bill: [License Post-Purchase FOCUS Entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=694253803#gid=694253803)

## Scenario C: Usage Records on Monthly Usage Statements

TODO @RileyJenkins I think it would be a good idea to provide an example for this case (E.g. shows Billed Cost of 0 and an Effective Cost for ths usage in a given period -- in this case, say a monthly charge? $100/12 for used licenses and similar rate for unused licenses?). This all depends on if the provider measures usage and provides this detail. If usage data/statements aren't provided, the Billed Cost and Effective Cost would be recognized in the same records.