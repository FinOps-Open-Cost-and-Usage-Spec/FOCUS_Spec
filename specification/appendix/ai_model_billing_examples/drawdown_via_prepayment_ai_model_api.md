---
dataset: CostAndUsage
---

# Drawdown via Prepayment

For this scenario, Acme Corp prepays a Solora AI token commitment and then draws it down against Solora Saturn usage:

* Acme Corp purchases a one-year spend commitment of $500,000.00 for Solora AI token consumption.
* Input tokens are priced at $5.00 per 1,000,000 tokens, and output tokens at $25.00 per 1,000,000 tokens.
* During the [charge period](#term), the workload consumes 5,000,000 input tokens and 1,500,000 output tokens against that commitment.

[**CSV Example**](/specification/data/ai_model_billing/drawdown_via_prepayment_ai_model_api.csv)

Note the following details in the example dataset:

* The purchase row uses [ChargeCategory](#col) "Purchase" with [BilledCost](#col) of $500,000.00 and [EffectiveCost](#col) of $0.00, which is the prepaid commitment outlay rather than period usage cost.
* The usage rows reference the same [commitment discount](#term) through [CommitmentDiscountId](#col), with [CommitmentDiscountStatus](#col) "Used" and [PricingCategory](#col) "Committed".
* Usage rows carry the list rate in both [ListUnitPrice](#col) and [ContractedUnitPrice](#col), so [ListCost](#col) and [ContractedCost](#col) are equal ($25.00 input and $37.50 output). The 20% commitment benefit appears in [EffectiveCost](#col) alone.
* On the usage rows, [BilledCost](#col) is $0.00 while [EffectiveCost](#col) carries the amortized drawdown ($20.00 input and $30.00 output), matching the covering-purchase pattern used elsewhere for commitment discounts.
* Solora AI is both the [service provider](#term) and the [invoice issuer](#term). Each token type remains a separate [SKU](#term), with the TokenDirection property of [SkuPriceDetails](#col) labeling the usage rows "Input" or "Output".
