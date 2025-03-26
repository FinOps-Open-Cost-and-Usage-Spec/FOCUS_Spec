# Marketplace Transactions and FOCUS Data

Many vendors provide the option to purchase their products through a CSP marketplace or other marketplace. In this case both the CSP's FOCUS data and the SaaS Vendors FOCUS would include records that include information about the purchase, without duplicating the Billed Cost.

## Scenario

ACME Corp offers its customer the ability to purchase their service via CSPCorps public marketplace. AwesomeCorp purchases ACME's service through the marketplace. ACME provides AwesomeCorp with a monthly invoice for their usage. ACME also provides a detailed usage report to AwesomeCorp. CSPCorp, as the [Invoice Issuer](#invoiceissuer), provides marketplace entries within their FOCUS data. CSPCorp issues payable invoices for their customers which includes expenses incurred for marketplace purchases.

On April 1st, 2025, ACME executes a contract  and invoices AwesomeCorp $100,000, public list cost of their purchase items would be $150,000.

The contract includes the following items:

* $50,000 for A Widgets
* $50,000 for B Licenses

## Key Factors

* In order to ensure consistent aggregation of cost and usage data the marketplace's FOCUS data, must include BilledCost that aligns with the invoiced amount. This is because the marketplace is considered the Invoice Issuer. The Provider would not include a BilledCost, else the billed cost would be double counted if aggregating both record sets.

## Initial Purchase Records Provided in the CSP's FOCUS Data

On April 1st CSPCorp provides the following records in their FOCUS data:

Entries in the FOCUS dataset:[CSPs Marketplace FOCUS Entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1092393377#gid=1092393377)

* The CSP marketplace data reflects the invoiced amount in the BilledCost column for the purchase executed through the marketplace.

## Initial Purchase Records Provided in the SaaS Provider's FOCUS Data

On April 1st ACME provides the following records in their FOCUS data:

Entries in the FOCUS dataset: [SaaS Providers FOCUS Entries](https://docs.google.com/spreadsheets/d/1kQTDK3Sk9BnNcn6Ovyaa37T1aMaXfHaDahsuk1Notn4/edit?gid=1092393377#gid=1092393377)

* The SaaS Provider's data does not include a Billed Cost equivalent to the purchase amount because they are not the Invoice Issuer, however they do provide a purchase record.
* The SaaS Provider's FOCUS purchase record entries may be at a higher level of granularity than that of the CSP providers focus data, and therefore may not match the purchase records in the CSP's FOCUS data.
