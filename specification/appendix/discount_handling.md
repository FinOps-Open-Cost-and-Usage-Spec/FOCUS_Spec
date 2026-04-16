# Discount Handling

While [*service providers*](#glossary:service-provider) may use different terms and mechanisms to describe and represent discounts in their native datasets, FOCUS represents discounts as reduced pricing reflected directly in the [*charges*](#glossary:charge) they pertain to, rather than as separate offsetting *charges*. Unlike discounts, [*credits*](#glossary:credit) are financial incentives or allowances represented as separate *charges* unrelated to other *charges*.

In [Cost and Usage](#datasets.costandusage), cost and unit price columns reflect the effect of discounts. Discounts associated with [*contract commitments*](#glossary:contract-commitment) are further identified and attributed using the [Contract Applied](#datasets.costandusage.contractapplied) column (also serves as an association to the [Contract Commitment](#datasets.contractcommitment) dataset), as well as [*commitment discount*](#glossary:commitment-discount)-specific columns. [*Custom columns*](#glossary:custom-column) may be used when needed to further identify or describe discounts.

For additional context and related normative requirements associated with discount handling, refer to the following specification sections:

| Concept | Description | Entity | Specification Location |
| :--- | :--- | :--- | :--- |
| **General dataset rules** | Handling unused portions, splitting discounted charges, and avoiding negating rows | Dataset | [CostAndUsage](#datasets.costandusage) |
| **Effect of discounts** | Reflecting reduced pricing from discounts | Column | [CostAndUsage.BilledCost](#datasets.costandusage.billedcost)<br>[CostAndUsage.EffectiveCost](#datasets.costandusage.effectivecost)<br>[CostAndUsage.ContractedCost](#datasets.costandusage.contractedcost)<br>[CostAndUsage.ListCost](#datasets.costandusage.listcost)<br>[CostAndUsage.ContractedUnitPrice](#datasets.costandusage.contractedunitprice)<br>[CostAndUsage.ListUnitPrice](#datasets.costandusage.listunitprice) |
| **Commitment Discount specifics** | Identification and utilization of *commitment discounts* | Column | [CostAndUsage.CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)<br>[CostAndUsage.CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) |
| **Resource tracking** | Identifying the exact resource that received the commitment discount | Column | [CostAndUsage.ResourceId](#datasets.costandusage.resourceid) |
| **Contract allocations** | Associating a charge with specific contract commitments | Column | [CostAndUsage.ContractApplied](#datasets.costandusage.contractapplied) |
