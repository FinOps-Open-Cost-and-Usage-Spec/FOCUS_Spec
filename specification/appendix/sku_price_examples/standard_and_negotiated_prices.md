# Standard and Negotiated Prices

Aura Web publishes a public rate for its standard virtual machine and separately grants Acme Corp a negotiated rate for the same machine. Both are prices for the same [*SKU*](#glossary:sku), so both carry the same [SkuId](#datamodel.skuprice.skuid) and the same [SkuPriceId](#datamodel.skuprice.skupriceid).

[**CSV Example**](/specification/data/sku_price_examples/sku_price_standard_and_negotiated.csv)

Note the following details in the example dataset:

* The public unit price carries a null [ContractId](#datamodel.skuprice.contractid), which is what identifies it as a list price available to any customer. [ListUnitPrice](#datamodel.skuprice.listunitprice) carries the published unit price of 0.384000 per hour, and [ContractedUnitPrice](#datamodel.skuprice.contractedunitprice) carries the same 0.384000, because no negotiation applies to a record with no contract. A query comparing the two columns across the catalog reads a unit price on every record rather than a null.
* The negotiated unit price carries a ContractId of "auraweb:contract::ACCT-123456789012:agreements/ctr-7f3a91b2c4d5", so its ContractedUnitPrice is populated at 0.326400 per hour, a 15 percent reduction. Its ListUnitPrice remains 0.384000, the unit price the reduction was negotiated against. Carrying both prices on one record means comparing a negotiated unit price to its public equivalent requires no join.
* The two records share a SkuPriceId. A SKU Price ID stays consistent across contracts, so the negotiated unit price is the same price point under different terms rather than a different price point. ContractId is a member of the composite key, which is what allows the two records to coexist.
* [SkuPriceEligibility](#datamodel.skuprice.skupriceeligibility) is where the two records differ in reach. The public rate uses `IsGlobalScope`, which states that its eligibility is not restricted to an enumerated set of entities:

```json
{
  "IsGlobalScope": true
}
```

* The negotiated unit price names the entities that can receive it. The `Inclusions` array carries one rule per dimension, and `InclusionOperator` states how multiple rules combine:

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

* The `Dimension` values reference columns in the [Cost and Usage](#datamodel.costandusage) dataset. A consumer resolves eligibility by evaluating a Cost and Usage row against these rules, which is why the dimension names are Cost and Usage column names rather than SKU Price column names.
* Both records carry a [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum) of zero and a null [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum). Aura Web supports quantity tier pricing elsewhere in its catalog, so the columns are present throughout the dataset. On an offering with no quantity thresholds, the minimum is zero and the maximum is null to indicate no upper bound.
