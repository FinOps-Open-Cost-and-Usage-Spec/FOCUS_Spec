Request is to make avaialble an invoice ID column that will be updated at invoice generation time to add the invoice ID to the rows of data for easier reconcilliation of spend to invoice ID

# The Problem:
Without Invoice ID there are situations like when an account is moved between different Billing Accounts, where you loose track and are unable to properly match those.
Invoice reconcilliation is harder to achieve when practiioners are not able to determine which charges in a month relate to the invoice for the invoie month.
Credits are har to allocate as each creadit or refund will receive a new credit memo and is not linked to previous invoices or invoice months.
Another important use case are Credit Memos (Refund Invoices): AWS creates Credit Memos and they show up in the CUR at that point in time, however there is a manual process involved to request that Credit Memo to be applied to a given regular Invoice. The result is that you cannot usually include the credit memo in the same billing period. We set the applicable billing period for each Credit Memo to take them into account, and for that we need the Invoice ID to be able to discriminate the right rows of data in the input. PR #675 https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/675 should be reviewed for credit/refund details

## Use Cases
We need to distribute all cost back to each cost center and then group cost by Billing Account ID, Invoice Issuer and Invoice ID so that our finance department can charge back the business units and pay the invoices.
The sum of the invoices for a given Billing Account ID and Invoice Issuer must match to the cent the sum of the chargeback per business unit for that same perimeter.

# Provider information on invoice handling
## Google
Invoices do not contain any row level details or product details; they only contain a link to the cost table in the billing console which is linked to the invoice.month column.
Invoices may show different totals to finops dashboards as an invoice month may be calculated differently to a calendar month, practitioner would need to understand this difference and how to map the data in Finops reports to calendar month and invoice month, they would require a report in their finops reporting tools that showed the detailed report for invoice month and calendar month: https://cloud.google.com/billing/docs/how-to/cost-table.
Google invoices are issued on the last day of the month and contain a document number which is the invoice ID. Depending on your google structure you have one primary billing accounts and invoices would be issued against the primary billing account ID. Generally, non service provider cloud users will have one billing account, SaaS providers or service providers may have sub billing account id's to separate out charges for customers but are all rolled up to the primary billing account id.

## Microsoft
Microsoft invoices are detailed containing every product item charged in the month.
Invoices are generated around the 5th of the following month and align to calendar month views
The invoice contains the billing account ID and the invoice ID
There is no direct correlation between FOCUS or cost export data and the invoice data
Billing account ID are used for invoice section ID in the invoice data
You can have one billing ID in MSFT or structure your MSFT environment for multiple billing account ID using the Landing zone structure leverages accounts and departments to create "virtual billing accounts"
It may be necessary to link part number from the invoice to SKU ID or Sku Price ID to find the correct allocation against the invoice and the finops reporting tool to properly allocate the invoice amount.
Adding an invoice ID to FOCUS exports in the current form would require a backfill of data to be done by MSFT for each row as well as identifying each invoice section ID linked to the billing ID structure created by each customer

## AWS
Not enough detail in AWS yet for me to work this out but will get more invoice detail shortly.

# SaaS providers
Here we will add invoice handling information from SaaS Providers for discussion on how we may include SaaS invoice ID's
