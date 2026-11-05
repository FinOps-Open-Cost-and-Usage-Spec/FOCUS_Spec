# Discount Handling

While [service providers](#term) may use different terms and mechanisms to describe and represent discounts in their native datasets, FOCUS represents discounts as reduced pricing reflected directly in the [charges](#term) they pertain to, rather than as separate offsetting [charges](#term). Unlike discounts, [credits](#term) are financial incentives or allowances represented as separate [charges](#term) unrelated to other [charges](#term).

In [Cost and Usage](#ds), cost and unit price columns reflect the effect of discounts. Discounts associated with [contract commitments](#term) are further identified and attributed using the [Contract Applied](#col) column (also serves as an association to the [Contract Commitment](#ds) dataset), as well as [commitment discount](#term)-specific columns. [Custom columns](#term) may be used when needed to further identify or describe discounts.

For additional context and related normative requirements associated with discount handling, refer to the following specification sections:

| Concept | Description | Entity | Specification Location |
| :--- | :--- | :--- | :--- |
| **General dataset rules** | Handling unused portions, splitting discounted charges, and avoiding negating rows | Dataset | [CostAndUsage](#datamodel.costandusage) |
| **Effect of discounts** | Reflecting reduced pricing from discounts | Column | [CostAndUsage.BilledCost](#datamodel.costandusage.billedcost)<br>[CostAndUsage.EffectiveCost](#datamodel.costandusage.effectivecost)<br>[CostAndUsage.ContractedCost](#datamodel.costandusage.contractedcost)<br>[CostAndUsage.ListCost](#datamodel.costandusage.listcost)<br>[CostAndUsage.ContractedUnitPrice](#datamodel.costandusage.contractedunitprice)<br>[CostAndUsage.ListUnitPrice](#datamodel.costandusage.listunitprice) |
| **Commitment Discount specifics** | Identification and utilization of *commitment discounts* | Column | [CostAndUsage.CommitmentDiscountId](#datamodel.costandusage.commitmentdiscountid)<br>[CostAndUsage.CommitmentDiscountStatus](#datamodel.costandusage.commitmentdiscountstatus) |
| **Resource tracking** | Identifying the exact resource that received the commitment discount | Column | [CostAndUsage.ResourceId](#datamodel.costandusage.resourceid) |
| **Contract allocations** | Associating a charge with specific contract commitments | Column | [CostAndUsage.ContractApplied](#datamodel.costandusage.contractapplied) |
