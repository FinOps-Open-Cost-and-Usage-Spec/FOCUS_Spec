# Supporting Analysis: Revising Intro / Description of ListUnitPrice and ContractedUnitPrice

## Revise ambiguous discounts inclusion/exclusion in Contracted and List Unit Price intro

* **Scope:** Intro and Description sections of `ListUnitPrice` and `ContractedUnitPrice`.
* **Related issues:**
  * Ambiguous discount inclusion/exclusion in ContractedUnitPrice;
  * Volume and time-based tiering not explicitly addressed.

> **Note:** The full list of issues is available [here](https://docs.google.com/spreadsheets/d/19ezQml4YRSIEn2Pz3ijUghTLq3q-3YnJKZoRjQimqb0/edit?gid=0#gid=0).

---

### Current Text and Identified Gaps

#### ListUnitPrice

> *"The List Unit Price represents the suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. This price is denominated in the Billing Currency. The List Unit Price is commonly used for calculating savings based on various rate optimization activities."*

**Gap:** The definition is silent on how volume-based or time-based tiered pricing is expected to be reflected. The phrase "exclusive of any discounts" can be read as excluding tiered pricing adjustments, although tiered pricing is part of the service-provider-published pricing configuration for the SKU, not a discount applied on top of it.

#### ContractedUnitPrice

> *"The Contracted Unit Price represents the agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts. This price is denominated in the Billing Currency. The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the List Unit Price."*

**Gaps:**

1. The definition identifies which discounts are included (*negotiated discounts*) and which are excluded (*negotiated commitment discounts or any other discounts*) by name, but does not state the underlying criterion that determines which discounts fall into which category. Without a stated criterion, new discount types and provider-specific constructs cannot be consistently classified.
2. By naming only *negotiated commitment discounts* as excluded, the definition implies by omission that non-negotiated *commitment discounts* may be included, which would break the analytical separation between negotiation savings and commitment savings.
3. The phrase "or any other discounts" has no defined scope. It can be read as excluding tiered pricing adjustments that are already reflected in `ListUnitPrice`.
4. The defaulting rule is anchored to "negotiated discounts" specifically, which is inconsistent with the column's broader role.

---

### Cost Column Trio

FOCUS defines three cost columns that together cover the full savings spectrum:

| Column | What it reflects | Used to measure |
|---|---|---|
| `ListCost` | Service-provider-published price; exclusive of discounts | Baseline |
| `ContractedCost` | Pricing adjustments unconditionally guaranteed by the governing contract | Savings from negotiation |
| `EffectiveCost` | All applicable pricing adjustments, including *commitment discounts* | Total realized savings |

The analytical value of the trio depends on each pair measuring a distinct and non-overlapping dimension of savings:

* `ListCost − ContractedCost` = negotiation savings
* `ContractedCost − EffectiveCost` = commitment savings

This is stated explicitly in the *Cost Comparison* section:

> *"Comparing ListCost against ContractedCost quantifies negotiated discount savings; comparing ContractedCost against EffectiveCost isolates commitment discount savings."*

Any definition of `ContractedUnitPrice` must preserve this separation. If *commitment discounts* are reflected in `ContractedCost`, the `ListCost − ContractedCost` gap would include some commitment savings, and the `ContractedCost − EffectiveCost` gap would undercount them.

---

### Discount Taxonomy

To determine what belongs in `ListUnitPrice` and/or `ContractedUnitPrice`, all identified discount types (price reduction mechanisms) should be taken into account and classified. The analysis is currently organized along the following dimensions:

* **Contract Role**: whether the discount is part of the primary commercial contract or a separately acquired instrument
* **Acquisition Channel**: the commercial relationship through which the discount is obtained
* **CC Offer Category**: Public (standard terms) or Negotiated (privately agreed)
* **Discounting Mechanism**: how the discount is operationally applied (Tiering, Flat Unconditional, Burn-Down, Build-Up)
* **Contingency**: whether the discount depends on the status or consumption of a commitment instrument

The list of dimensions (aspects) and discount mechanisms is non-exhaustive and may be extended as needed.

#### Taxonomy table

The taxonomy table is available in the [accompanying spreadsheet](https://docs.google.com/spreadsheets/d/19ezQml4YRSIEn2Pz3ijUghTLq3q-3YnJKZoRjQimqb0/edit?gid=1676640405#gid=1676640405) (sheet: *Contracts and Discounts*).

| ID | Acquisition Channel | Contract Role | CC Offer Category | Summary | Discounting Mechanism | Discount independent of Commitment Instrument | Included in ContractedUnitPrice | Visible in ListUnitPrice | Covering / Covered Charge Mechanism |
|---|---|---|---|---|---|---|---|---|---|
| A | Primary Non-Negotiated Contract | Primary | Public | | | | | | |
| A-0 | Primary Non-Negotiated Contract | Primary | Public | Non-Negotiated Automatic Tiering Discount | Tiering – Volume or Time | Yes | Yes | Yes | No |
| B | Primary Negotiated Contract | Primary | Negotiated | | | | | | |
| B-0 | Primary Negotiated Contract | Primary | Negotiated | Negotiated Unconditional Discount – Primary Contract | Flat Unconditional | Yes | TBD | No | No |
| B-1 | Primary Negotiated Contract | Primary | Negotiated | Negotiated Burn-Down Commitment Discount – Primary Contract | Burn-Down (covering/covered) | No | TBD | No | Yes |
| B-2 | Primary Negotiated Contract | Primary | Negotiated | Negotiated Build-Up Commitment Discount – Primary Contract | Build-Up | No | TBD | No | No |
| C | Additional Non-Negotiated Contract – Same Provider | Additional | Public | | | | | | |
| C-0 | Additional Non-Negotiated Contract – Same Provider | Additional | Public | Non-Negotiated Unconditional Discount – Separate Contract | Flat Unconditional | Yes | TBD | No | No |
| C-1 | Additional Non-Negotiated Contract – Same Provider | Additional | Public | Non-Negotiated Burn-Down Commitment Discount – Separate Contract | Burn-Down | No | TBD | No | Yes |
| C-2 | Additional Non-Negotiated Contract – Same Provider | Additional | Public | Non-Negotiated Build-Up Commitment Discount – Separate Contract | Build-Up | No | TBD | No | No |
| D | Additional Negotiated Contract – Same Provider | Additional | Negotiated | | | | | | |
| D-0 | Additional Negotiated Contract – Same Provider | Additional | Negotiated | Negotiated Unconditional Discount – Separate Contract, Same Provider | Flat Unconditional | Yes | TBD | No | No |
| D-1 | Additional Negotiated Contract – Same Provider | Additional | Negotiated | Negotiated Burn-Down Commitment Discount – Separate Contract, Same Provider | Burn-Down (covering/covered) | No | TBD | No | Yes |
| D-2 | Additional Negotiated Contract – Same Provider | Additional | Negotiated | Negotiated Build-Up Commitment Discount – Separate Contract, Same Provider | Build-Up | No | TBD | No | No |
| E | Additional Non-Negotiated Contract – Third-Party Provider | Additional | Public | | | | | | |
| E-0 | Additional Non-Negotiated Contract – Third-Party Provider | Additional | Public | Non-Negotiated Automatic Tiering Discount | Tiering – Volume or Time | Yes | Yes | Yes | No |
| F | Additional Negotiated Contract – Third-Party Provider | Additional | Negotiated | | | | | | |
| F-0 | Additional Negotiated Contract – Third-Party Provider | Additional | Negotiated | Negotiated Unconditional Discount – Separate Contract, Third-Party Provider | Flat Unconditional (covered) | Yes | TBD | No | No |
| F-1 | Additional Negotiated Contract – Third-Party Provider | Additional | Negotiated | Negotiated Burn-Down Commitment Discount – Separate Contract, Third-Party Provider | Burn-Down (covered) | No | TBD | No | Yes |
| F-2 | Additional Negotiated Contract – Third-Party Provider | Additional | Negotiated | Negotiated Build-Up Commitment Discount – Separate Contract, Third-Party Provider | Build-Up (covered) | No | TBD | No | No |

#### Out of scope: BYOL and Dynamic pricing

Two pricing constructs sometimes perceived as discounts — BYOL (Bring Your Own License) and Spot / preemptible pricing — are excluded from this taxonomy on the basis of the FOCUS SKU model.

`SkuId` MUST remain consistent regardless of factors that affect price but not functionality. A pricing adjustment qualifies as a discount on a given SKU only if the underlying service delivered is identical.

* **BYOL:** The provider's software license is not included, changing the nature of the service delivered. BYOL is represented as a different `SkuId`, not a discounted price on the same SKU.
* **Spot / preemptible pricing:** Represented via `PricingCategory` set to *Dynamic*. The service is not guaranteed and pricing is set dynamically by the provider, representing a different reliability and availability profile rather than a price reduction on the equivalent Standard-priced service.

Both are treated as separate SKU or SKU Price variants and are not discounts relevant to `ContractedUnitPrice`.

---

### Proposed Criterion

The proposed revision replaces the source-based framing (*negotiated discounts* / *negotiated commitment discounts*) with a criterion based on the conditionality of the pricing adjustment:

> A pricing adjustment is included in `ContractedUnitPrice` if and only if it is unconditionally guaranteed to apply to each eligible *charge* for the duration of the governing *contract*, without requiring the active status, continued activation, or remaining balance of a discount-bearing commitment program.

A pricing adjustment is excluded from `ContractedUnitPrice` if its application depends on:

* the active status of a discount-bearing commitment program, or
* the remaining balance or capacity of a pre-purchased discount-bearing commitment program (Burn-Down), or
* the satisfaction of a consumption or spend threshold within a fulfillment interval (Build-Up).

The criterion is agnostic to whether the discount is publicly available or negotiated, whether it was established within a primary or additional contract, and whether the instrument is operated by the same provider or a third-party provider. The distinction is purely about the conditionality of the pricing adjustment at the *charge* level.

#### Note on terminology

Two candidate terms were considered for expressing the criterion: **contract commitment** and **discount-bearing commitment program**. The term used above is *discount-bearing commitment program*. The reasoning:

*Contract commitment* is known to cover negotiated commitments, but the specification does not yet explicitly state that it also covers *commitment discounts* (i.e., the public variant). This can be inferred from examples in the spec, but the specification itself is still somewhat vague on this point. *Discount-bearing commitment program* avoids this ambiguity by explicitly narrowing to the discount-bearing subset, which is what the criterion is intended to exclude.

#### Application to the taxonomy

| Included | Excluded |
|---|---|
| A-0, E-0 (tiering — also visible in ListUnitPrice) | B-1, B-2 |
| B-0, C-0, D-0, F-0 (flat unconditional) | C-1, C-2 |
| | D-1, D-2, F-1, F-2 |

---

### Tiered Pricing

Volume-based and time-based tiered pricing is a discount type classified in the taxonomy above as A-0 (Primary Non-Negotiated Contract) and E-0 (Additional Non-Negotiated Contract – Third-Party Provider). Its distinguishing characteristic is that the unit price is reduced at higher consumption or duration tiers based on published tier configuration, independent of any discount-bearing commitment program. Per the proposed criterion, it is included in `ContractedUnitPrice`.

Under the working assumption:

* `ListUnitPrice` reflects the public tier configuration of the SKU.
* `ContractedUnitPrice` reflects both the applicable pricing adjustments per the proposed criterion above, and any custom tier range configuration specific to the customer's *contract*.

---

### Proposed Revised Text

Two variants are presented for working group consideration. They differ in how they treat tiered pricing terminologically: Variant A treats tiering as a discount type explicitly, while Variant B avoids the discount terminology for tiering and describes it as an applicable unit price per tier that may be reduced at higher tiers.

---

#### Variant A — Tiering treated as a discount type

##### ListUnitPrice — Intro (Variant A)

> The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts other than volume-based or time-based tiering reflected in the SKU's published pricing configuration. This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

##### ListUnitPrice — Description (Variant A)

> The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts other than volume-based or time-based tiering reflected in the SKU's published pricing configuration.

##### ContractedUnitPrice — Intro (Variant A)

> The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract, including any custom volume-based or time-based tiering configuration specific to the customer's contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program. This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If no such pricing adjustments are applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice).

##### ContractedUnitPrice — Description (Variant A)

> The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract, including any custom volume-based or time-based tiering configuration specific to the customer's contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program.

##### Side-by-Side — ListUnitPrice (Variant A)

| Section | Current (1.4) | Proposal |
|---|---|---|
| Intro | The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts. | The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts other than volume-based or time-based tiering reflected in the SKU's published pricing configuration. |
| Intro | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). |
| Intro | The List Unit Price is commonly used for calculating savings based on various rate optimization activities. | The List Unit Price is commonly used for calculating savings based on various rate optimization activities. |
| Description | The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. | The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts other than volume-based or time-based tiering reflected in the SKU's published pricing configuration. |

##### Side-by-Side — ContractedUnitPrice (Variant A)

| Section | Current (1.4) | Proposal |
|---|---|---|
| Intro | The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. | The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract, including any custom volume-based or time-based tiering configuration specific to the customer's contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program. |
| Intro | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). |
| Intro | The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. | The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. |
| Intro | If negotiated discounts are not applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice). | If no such pricing adjustments are applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice). |
| Description | The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts. | The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract, including any custom volume-based or time-based tiering configuration specific to the customer's contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program. |

---

#### Variant B — Tiering described as applicable unit price per tier

*Rationale: Although tiered pricing meets the definition of a discount in the sense that the unit price is reduced at higher tiers, it differs operationally from other discount types: it is structured through the SKU's published pricing configuration itself, with distinct `SkuPriceId` values per tier, rather than being applied as an adjustment on top of a single published price. Variant B reflects this by avoiding discount terminology for tiering and describing it as the applicable unit price per tier, which may be reduced at higher consumption or duration tiers.*

##### ListUnitPrice — Intro (Variant B)

> List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts. For SKUs with volume-based or time-based tiered pricing, it reflects the applicable published unit price per tier, which may be reduced at higher consumption or duration tiers.
>
> List Unit Price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). List Unit Price is commonly used for calculating savings based on various rate optimization activities.

##### ListUnitPrice — Description (Variant B)

> The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts, reflecting the applicable published unit price per tier for SKUs with volume-based or time-based tiered pricing.

##### ContractedUnitPrice — Intro (Variant B)

> Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of all negotiated pricing adjustments unconditionally guaranteed by the governing contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program. For SKUs with volume-based or time-based tiered pricing, it reflects the applicable unit price per tier under any custom tier configuration specific to the customer's contract. If no negotiated pricing adjustments unconditionally guaranteed by the governing contract are applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice).
>
> Contracted Unit Price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Contracted Unit Price is commonly used for calculating savings based on negotiation activities.

##### ContractedUnitPrice — Description (Variant B)

> The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract and excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program, reflecting the applicable unit price per tier for SKUs with volume-based or time-based tiered pricing.

##### Side-by-Side — ListUnitPrice (Variant B)

| Section | Current (1.4) | Proposal |
|---|---|---|
| Intro | The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts. | The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, exclusive of any discounts. |
| Intro | *(not present)* | For SKUs with volume-based or time-based tiered pricing, it reflects the applicable published unit price per tier, which may be reduced at higher consumption or duration tiers. |
| Intro | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). |
| Intro | The List Unit Price is commonly used for calculating savings based on various rate optimization activities. | The List Unit Price is commonly used for calculating savings based on various rate optimization activities. |
| Description | The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. | The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts, reflecting the applicable published unit price per tier for SKUs with volume-based or time-based tiered pricing. |

##### Side-by-Side — ContractedUnitPrice (Variant B)

| Section | Current (1.4) | Proposal |
|---|---|---|
| Intro | The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. | The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program. |
| Intro | *(not present)* | For SKUs with volume-based or time-based tiered pricing, it reflects the applicable unit price per tier under any custom tier configuration specific to the customer's contract. |
| Intro | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). | This price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). |
| Intro | The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. | The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. |
| Intro | If negotiated discounts are not applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice). | If no such pricing adjustments are applicable, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice). |
| Description | The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts. | The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contract and excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program, reflecting the applicable unit price per tier for SKUs with volume-based or time-based tiered pricing. |
