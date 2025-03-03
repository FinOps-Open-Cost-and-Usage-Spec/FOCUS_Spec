# Marketplace Transactions and FOCUS Data

Many vendors provide the option to purchase their products through a CSP marketplace or other marketplace. In this case both the CSP's FOCUS data and the SaaS Vendors FOCUS would include records that express the cost of the purchase aligning with payable invoices and more detailed cost and usage data from the SaaS Provider.

## Scenario

ACME Corp offers its customer the ability to purchase their service via CSPCorps public marketplace. AwesomeCorp purchases ACME's service through the marketplace. ACME provides AwesomeCorp with a monthly invoice for their usage. ACME also provides a detailed usage report to AwesomeCorp. CSPCorp provides marketplace entries within their FOCUS data. CSPCorp issues payable invoices for their customers which includes expenses incurred for marketplace purchases.

On April 1st, 2025, ACME executes a contract  and invoices AwesomeCorp $100,000, public list cost of their purchase items would be $150,000.
The contract includes the following items:
- $50,000 for A Widgets
- $50,000 for B Licenses

## Key Factors
- In order to ensure consistent aggregation of cost and usage data the marketplaces FOCUS data must reflect the payable invoice amount, without duplicative BilledCost values in the data provided by the vendor that would result in double counting the invoice amount payable by the end customer.


## Initial Purchase Records Provided in the CSP's FOCUS Data
On April 1st CSPCorp provides the following records in their FOCUS data:

Entries in the FOCUS dataset:
SEE: CSPs Marketplace FOCUS Entries https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1092393377#gid=1092393377

- The CSP marketplace data reflects the invoiced amount in the BilledCost column for the purchase executed through the marketplace.

## Initial Purchase Records Provided in the SaaS Provider's FOCUS Data
On April 1st ACME provides the following records in their FOCUS data:

Entries in the FOCUS dataset:
SEE: SaaS Providers FOCUS Entries  https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1092393377#gid=1092393377

- The SaaS Provider's data reflects the invoiced amount in the BilledCost column for the purchase executed, the SaaS vendor ensures that the BilledCost for purchases is zero because they are not issuing payable invoices. 
- The SaaS Provider's FOCUS purchase record entries may be at a higher level of granularity than that of the CSP providers focus data, and therefore may not match the purchase records in the CSP's FOCUS data.

## Token Depletion Resulting in Additional Purchase Credits
In September 2025, AwesomeCorp has depleted their standard tokens and are required to purchase 1500 additional tokens. ACME invoices AwesomeCorp $3000 on October 5th, to compensate for a credit balance of -1500. 

