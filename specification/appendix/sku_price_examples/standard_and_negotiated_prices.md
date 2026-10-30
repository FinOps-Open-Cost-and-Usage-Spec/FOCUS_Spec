---
dataset: SkuPrice
---

# Standard and Negotiated Prices

Aura Web publishes a public rate for its standard virtual machine and separately grants Acme Corp a negotiated rate for the same machine. Both are prices for the same [SKU](#term), so both carry the same [SkuId](#col) and the same [SkuPriceId](#col).

[**CSV Example**](/specification/data/sku_price_examples/sku_price_standard_and_negotiated.csv)

Note the following details in the example dataset:

* The public rate carries a null [ContractId](#col) and a [UnitPriceType](#col) of "List", which identify it as a list price that is not specific to a contract. [UnitPrice](#col) carries the published rate of 0.384000 per hour.
* The contracted rate carries a [ContractId](#col) of "auraweb:contract::ACCT-123456789012:agreements/ctr-7f3a91b2c4d5" and a [UnitPriceType](#col) of "Contracted", so its [UnitPrice](#col) is populated at 0.326400 per hour, a 15 percent reduction. Comparing a negotiated rate to its public equivalent requires looking up the corresponding SKU Price record where [UnitPriceType](#col) is "List".
* The two records share a [SkuPriceId](#col). A [SKU Price ID](#col) stays consistent across contracts, so the negotiated rate is the same price point under different terms rather than a different price point. [ContractId](#col) is a member of the composite key, which is what allows the two records to coexist.
* [SkuPriceEligibility](#col) is where the two records differ in reach. The public rate uses `IsGlobalScope`, which states that its eligibility is not restricted to an enumerated set of entities:

```json
{
  "IsGlobalScope": true
}
```

* The negotiated rate names the entities that can receive it. The `Inclusions` array carries one rule per dimension, and `InclusionOperator` states how multiple rules combine:

```json
{
  "IsGlobalScope": false,
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": [
        "ACCT-123456789012",
        "ACCT-210987654321"
      ]
    }
  ]
}
```

* The `Dimension` values reference columns in the [Cost and Usage](#ds) dataset. A consumer resolves eligibility by evaluating a [Cost and Usage](#ds) row against these rules, which is why the dimension names are [Cost and Usage](#ds) column names rather than SKU Price column names.
* Both records carry a [QuantityTierMinimum](#col) of zero and a null [QuantityTierMaximum](#col). Aura Web supports quantity tier pricing elsewhere in its catalog, so the columns are present throughout the dataset. On an offering with no quantity thresholds, the minimum is zero and the maximum is null to indicate no upper bound.
