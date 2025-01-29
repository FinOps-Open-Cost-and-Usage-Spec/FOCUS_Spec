Request is to make avaialble an invoice ID column that will be updated at invoice generation time to add the invoice ID to the rows of data for easier reconcilliation of spend to invoice ID
# Options
## Option 1 - Add InvoiceID column to FOCUS table
Adding a new column called InvoiceID
This option is probably less complex than option 2 but requires providers to do an update on millions and millions of rows of data at the end of each period to inlcude the relevant invoiceID for the billing period. 
It may increase data sizes and doubles the export requirements for practitioners at the end of each month.
We will need to work through how to determine the InvoiceID or Invoice section ID and how to links to the specific rows of data for the billing period noting we may have some invoice month items land in a different billing period outside the invoice month.

## Option 2 - Create an invoice Schema outside of FOCUS - preffered
Discussing this option with Riley, it sounds like a very suitable option for linking InvoiceID back to billed rows of data for a billing period. 
We would create a new schema for Invoice data which can be updated at the end of each month and would use dimension data to provide a unique link back to each row of data the invoice was associated to
Examples of this can eb found here: https://docs.google.com/spreadsheets/d/1fzLutxkXWoxDifz8YgGHQxbEyO67lA_6_EHr-E5Jlzk/edit?gid=1540478077#gid=1540478077

# The Problem:
Without Invoice ID there are situations like when an account is moved between different Billing Accounts, where you loose track and are unable to properly match those.
Invoice reconcilliation is harder to achieve when practiioners are not able to determine which charges in a month relate to the invoice for the invoie month.
Credits are hard to allocate as each credit or refund will receive a new credit memo and is not linked to previous invoices or invoice months.
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
AWS invoice will either be per account ID or if account ID's are linked to a primary accoutn for billing all details will be in a single invoice with linked account ID at the end of the invoice that the invoice applies to. the invoice from what i can see does not contain SKU's or part numbers in the invoice.

# SaaS providers
Here we will add invoice handling information from SaaS Providers for discussion on how we may include SaaS invoice ID's
@Riley could you add something here around SaaS handling


# TF2 meeting notes 30/01/2025
Pre generate invoice number in FOCUS for invoice month rqther than invoice ID at invoice generation time
Ensures invoice ID is in FOCUS 
Include detailed invoice schem ID in Dataset to view detailed invoice information
what does a change look like
is there rewrite required on this
