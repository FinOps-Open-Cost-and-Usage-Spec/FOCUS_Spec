# Drawdown via Prepayment

For this scenario, Acme Corp prepays a Solora AI token commitment and then draws it down against Solora Saturn usage:

* Acme Corp purchases a one-year spend commitment of $500,000.00 for Solora AI token consumption.
* Input tokens are priced at $5.00 per 1,000,000 tokens, and output tokens at $25.00 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 5,000,000 input tokens and 1,500,000 output tokens against that commitment.

[**CSV Example**](/specification/data/ai_billing/drawdown_via_prepayment_frontier_model_api.csv)

Note the following details in the example dataset:

* The purchase row uses [ChargeCategory](#datamodel.costandusage.chargecategory) "Purchase" with [BilledCost](#datamodel.costandusage.billedcost) of $500,000.00 and [EffectiveCost](#datamodel.costandusage.effectivecost) of $0.00, which is the prepaid commitment outlay rather than period usage cost.
* The usage rows reference the same [*commitment discount*](#glossary:commitment-discount) through [CommitmentDiscountId](#datamodel.costandusage.commitmentdiscountid), with [CommitmentDiscountStatus](#datamodel.costandusage.commitmentdiscountstatus) "Used" and [PricingCategory](#datamodel.costandusage.pricingcategory) "Committed".
* Usage rows carry the list rate in both [ListUnitPrice](#datamodel.costandusage.listunitprice) and [ContractedUnitPrice](#datamodel.costandusage.contractedunitprice), so [ListCost](#datamodel.costandusage.listcost) and [ContractedCost](#datamodel.costandusage.contractedcost) are equal ($25.00 input and $37.50 output). The 20% commitment benefit appears in EffectiveCost alone.
* On the usage rows, BilledCost is $0.00 while EffectiveCost carries the amortized drawdown ($20.00 input and $30.00 output), matching the covering-purchase pattern used elsewhere for commitment discounts.
* Solora AI is both the [*service provider*](#glossary:service-provider) and the [*invoice issuer*](#glossary:invoice-issuer). Each token type remains a separate [*SKU*](#glossary:sku), with the TokenDirection property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) labeling the usage rows "Input" or "Output".
