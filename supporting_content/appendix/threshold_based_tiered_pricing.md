## 3. Candidate Term Comparison (Concise)

> **Note on "volume-based":** this phrase is not used consistently even among the sources checked. FOCUS and AWS/Azure use it for the **threshold dimension** (a quantity of Pricing Unit). Stripe and Oracle NetSuite use "Volume(-based) pricing" for a completely different axis — the **tier application model** (the whole quantity repriced at the tier reached, as opposed to "Graduated," where only the portion within each tier is repriced). Same word, two unrelated meanings, depending on source.

| Concept | Candidate Term | FOCUS Usage | Same Meaning Elsewhere | Different Meaning Elsewhere | Pros | Cons |
|---|---|---|---|---|---|---|
| Threshold-Based Tiered Pricing (umbrella) | **Threshold-Based Tiered Pricing** | "threshold" ×3, never as a defined term | None found | — | Explicit umbrella covering quantity/spend/duration | No external precedent |
| | **Tiered Pricing** (bare) | "tiered pricing" ×8 | AWS, Azure, Stripe | — | Strong external precedent | Not used as an umbrella anywhere; quantity-only bias |
| Quantity-Based sub-type | **Volume-Based Tiered Pricing** | ×3 "volume-based tier(s)" + existing (unratified) columns `VolumeTier*` | AWS, Azure | Stripe, NetSuite (different axis — see note above) | Matches unratified column names; matches AWS/Azure | Collides with Stripe/NetSuite meaning; not self-explanatory |
| | **Quantity-Based Tiered Pricing** | "quantity-based" ×3, but unrelated context (Contract Commitment, not tiering) | None found | — | Self-explanatory; matches `PricingQuantity`/`PricingUnit`; lowest rename cost (dataset unratified) | No external precedent |
| | **Usage-Based Tiered Pricing** | "usage-based" ×56 (general); `ContractCommitmentCategory` = "Usage"/"Spend" is FOCUS's closest ratified dichotomy | Industry-wide, but for consumption pricing generally | "Usage-based" already means "any metered pricing" elsewhere in FOCUS/industry | Reuses FOCUS's own Usage/Spend dichotomy | Most overloaded — likely to be misread as "any consumption pricing" |

# Inventory of All "tier" Occurrences in FOCUS-spec (2026-07-21)

## Classification legend

For each citation, an assessment is given against the following four categories:

- **Threshold-Based Tiered Pricing** — the citation refers to a pricing mechanism where the applicable unit price changes based on reaching a predefined quantity, spend, or duration threshold (i.e., the concept this appendix topic is meant to formalize).
- **Storage Tier** — the citation refers to a qualitative service/product classification (e.g., a storage class or performance tier such as "Hot"/"Archive"/"Nearline"), not a pricing mechanism.
- **Feature Tier** — the citation refers to a product/plan tier that bundles a different set of features or capabilities (commonly seen in SaaS subscription plans), not a volume-based pricing mechanism.
- **Other / Unclear** — the citation uses "tier" in a way that does not clearly map to any of the above three categories, is a structural/navigational mention (e.g., only appears in a heading or a cross-reference link), or is too ambiguous to classify with confidence.

---

## 3. Data Model

### 3.1. Cost and Usage

#### 3.1.42. Pricing Category
##### 3.1.42.2. Allowed Values
Anchor: `#datamodel.costandusage.pricingcategory.allowedvalues`

Table header: `| Value | Description |`

Row (Value = "Standard"):
> "Standard — *Charges* priced at the agreed upon rate for the billing account, including [*negotiated discounts*](#glossary:negotiated-discount). This pricing includes any flat rate and volume/tiered pricing but does not include dynamic pricing or reduced pricing due to the application of a *commitment discount*. This does include the purchase of a commitment discount at agreed upon rates."

**Assessment:** Threshold-Based Tiered Pricing. "Volume/tiered pricing" is listed as a form of standard, non-discounted-by-commitment pricing — consistent with a threshold/volume-based mechanism, though not defined further here.

---

#### 3.1.58. SKU ID
Anchor: `#datamodel.costandusage.skuid`

Citation 1:
> "Pricing tiers (e.g., free tier or volume-based tiers)."

**Assessment:** Threshold-Based Tiered Pricing (with a "free tier" variant, which is arguably a zero-priced threshold tier). Listed as an example of why SKU Price varies within a single SKU ID.

Citation 2:
> "SKU ID is commonly used for analyzing and comparing costs for the same SKU across different price details (e.g., *period*, tier, location)."

**Assessment:** Other / Unclear. "Tier" appears in a generic list of price-detail dimensions alongside "period" and "location," without enough context to determine which tier concept (volume, storage, or feature) is intended.

---

#### 3.1.60. SKU Price Details
Anchor: `#datamodel.costandusage.skupricedetails`

Citation 1:
> "SKU Price Details represent a list of [*SKU Price*](#glossary:sku-price) properties (key-value pairs) associated with a specific [SKU Price ID](#datasets.costandusage.skupriceid). These properties include qualitative and quantitative properties of a [*SKUs*](#glossary:sku) (e.g., functionality and technical specifications), along with core stable pricing properties (e.g., pricing [*periods*](#glossary:period), tiers, etc.), excluding dynamic or negotiable pricing elements such as unit price amounts; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific factors (e.g., contract or account identifiers, and negotiable discounts)."

**Assessment:** Other / Unclear. "Tiers" is listed as a "core stable pricing property" alongside "periods," without specifying whether this refers to volume-based thresholds, feature tiers, or something else.

Citation 2:
> "Additionally, the SKU Price Details may be used to analyze costs based on pricing properties such as *periods* and tiers."

**Assessment:** Other / Unclear. Same ambiguity as above — "tiers" used generically as a pricing property.

##### 3.1.60.2. FOCUS-Defined Properties
Anchor: `#datamodel.costandusage.skupricedetails.focus-definedproperties`

Table header: `| Key | Description | Data Type | Unit of Measure (numeric) or example values (string) |`

Row:
> "StorageClass — Class or tier of storage provided — String — Examples: \"Hot\", \"Archive\", \"Nearline\""

**Assessment:** Storage Tier. The examples ("Hot", "Archive", "Nearline") are explicitly storage performance/access classes, not volume-based pricing thresholds.

---

#### 3.1.61. SKU Price ID
Anchor: `#datamodel.costandusage.skupriceid`

> "Additionally, the SKU Price ID is commonly used to analyze costs based on pricing properties such as [*periods*](#glossary:period) and tiers."

**Assessment:** Other / Unclear. Same generic usage as the SKU Price Details citations above.

---

### 3.3. Contract Commitment

#### 3.3.3. Contract Commitment Benefit Category
##### 3.3.3.2. Allowed Values
Anchor: `#datamodel.contractcommitment.contractcommitmentbenefitcategory.allowedvalues`

Table header: `| Value | Sort Order | Description | Typical Use Case |`

Row (Value = "Discount"):
> "Discount | 10 | A financial reduction in the unit price or list rate, whether applied immediately or conditionally upon meeting usage or spend thresholds. | Flat rate negotiated reductions, Savings Plans, growth rebates, or volume-tier discounts."

**Assessment:** Threshold-Based Tiered Pricing. "Volume-tier discounts" is listed as a Typical Use Case example, and the Description column explicitly references "meeting usage or spend thresholds."

Row (Value = "Entitlement"):
> "Entitlement | 20 | The contractual right to access and consume specific products, features, or software tiers that would otherwise be unavailable. | Marketplace SaaS purchases, Enterprise Agreements (e.g., Snowflake), or paid Proof of Concepts."

**Assessment:** Feature Tier. "Software tiers" here refers to access to specific products/features, not a volume-based unit price mechanism.

---

#### 3.3.8. Contract Commitment Discount Percentage
##### 3.3.8.1. Requirements
Anchor: `#datamodel.contractcommitment.contractcommitmentdiscountpercentage.requirements`

> "For contracts with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), ContractCommitmentDiscountPercentage MUST adhere to the following additional requirements:
> - ContractCommitmentDiscountPercentage MUST reflect the discount percentage defined for the specific pricing tier represented by the Contract Commitment row.
> - ContractCommitmentDiscountPercentage MUST correspond to only one pricing tier per Contract Commitment row."

**Assessment:** Threshold-Based Tiered Pricing. The parenthetical example ("5% discount up to 1M, 10% above 1M") is a textbook volume/spend-threshold pricing structure.

##### 3.3.8.2. Implementation Guidance
###### 3.3.8.2.3. Tiered Incentives
Anchor: `#datamodel.contractcommitment.contractcommitmentdiscountpercentage.implementationguidance.tieredincentives`

> "For commitments with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), this column should represent the **active** or **base** discount percentage applicable to the current contract row."

**Assessment:** Threshold-Based Tiered Pricing. Same example and mechanism as above.

---

#### 3.3.10. Contract Commitment Fulfillment Interval
##### 3.3.10.2. Allowed Values
Anchor: `#datamodel.contractcommitment.contractcommitmentfulfillmentinterval.allowedvalues`

Table header: `| Value | Sort Order | Description | Typical Use Case |`

Row (Value = "Monthly"):
> "Monthly | 40 | Measured over a calendar month. | Discontinuous Model: SaaS MRR minimums or tiered discounts."

**Assessment:** Threshold-Based Tiered Pricing. "Tiered discounts" appears alongside "SaaS MRR minimums" as an example of a discontinuous fulfillment model — consistent with volume/spend-threshold pricing, though the SaaS context could also imply overlap with Feature Tier scenarios; flagged as primarily Threshold-Based given the "discounts" framing.

---

### 3.5. SKU Price

#### 3.5.1. Columns
Anchor: `#datamodel.skuprice.columns`

Table header: `| Column | Column Type | Feature Level | Allows Nulls | Data Type |`

Row 1:
> "Volume Tier Maximum | Metric | Conditional | True | Decimal"

Row 2:
> "Volume Tier Minimum | Metric | Conditional | False | Decimal"

Row 3:
> "Volume Tier Name | Dimension | Conditional | True | String"

**Assessment (all three rows):** Threshold-Based Tiered Pricing. These are the three new normative columns in the SKU Price dataset that directly model volume-based pricing tiers.

---

#### 3.5.2. Relationships
Anchor: `#datamodel.skuprice.relationships`

> "The SKU Price dataset relates to the Cost and Usage dataset through the SKU Price ID, enabling the attribution of catalog rates to incurred usage. This is a one-to-many relationship: a single SKU Price ID corresponds to multiple SKU Price records, because a SKU's price varies by effective period, contract, volume tier, pricing currency, and unit price category. Resolving the price that applies to a Cost and Usage charge therefore requires more than the SKU Price ID alone. The charge must also be aligned to the SKU Price record whose effective period contains the charge period, whose Contract ID matches the agreement under which the charge was incurred (or is null for a public list price), whose volume tier contains the charged quantity, whose pricing currency matches the currency in which the charge is denominated, and whose unit price category matches the price type applied to the charge. The SKU Price dataset can also optionally join to the Contract Commitment dataset to relate a specific contracted price to an overarching negotiated agreement."

**Assessment:** Threshold-Based Tiered Pricing. "Volume tier" is used twice as one of the dimensions that differentiates SKU Price records and that a charge must be matched against — directly describing the volume-threshold routing mechanism.

---

#### 3.5.3. Requirements
Anchor: `#datamodel.skuprice.requirements`

> "SkuPrice MUST include [VolumeTierMaximum](#datasets.skuprice.volumetiermaximum) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing).
> SkuPrice MUST include [VolumeTierMinimum](#datasets.skuprice.volumetierminimum) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing).
> SkuPrice MUST include [VolumeTierName](#datasets.skuprice.volumetiername) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing)."

**Assessment:** Threshold-Based Tiered Pricing. Normative conditional-inclusion requirements for the three Volume Tier columns.

> "SkuPrice MUST maintain row uniqueness across the composite key of ServiceProviderName, SkuPriceId, ContractId, VolumeTierMinimum, SkuPriceEffectiveStart, PricingCurrency, and UnitPriceCategory."

**Assessment:** Threshold-Based Tiered Pricing. VolumeTierMinimum is included as part of the composite uniqueness key, confirming each tier boundary produces a distinct row.

> "SkuPrice MUST NOT contain records whose validity periods, defined by SkuPriceEffectiveStart and SkuPriceEffectiveEnd, overlap for the same combination of ServiceProviderName, SkuPriceId, ContractId, VolumeTierMinimum, PricingCurrency, and UnitPriceCategory."

**Assessment:** Threshold-Based Tiered Pricing. Same composite-key logic applied to a non-overlap requirement.

---

#### 3.5.18. SKU ID
Anchor: `#datamodel.skuprice.skuid`

Citation 1:
> "Pricing tiers (e.g., free tier or volume-based tiers)."

**Assessment:** Threshold-Based Tiered Pricing. This is the SKU Price dataset's own restatement of the same example found in the Cost and Usage SKU ID section (3.1.58).

Citation 2:
> "SKU ID is the primary identifier used to look up detailed information about the *SKU* within a catalog or [*price list*](#glossary:price-list) published by a service provider. SKU ID is commonly used to join rate card data with actual usage or to analyze price variations for the same SKU across different price details (e.g., *period*, tier, location)."

**Assessment:** Other / Unclear. Same generic "tier" usage pattern as the equivalent Cost and Usage section (3.1.58), without further specification.

---

#### 3.5.24. SKU Price ID
Anchor: `#datamodel.skuprice.skupriceid`

> "The composition of properties associated with the SKU Price ID may differ across service providers and across *SKUs* within the same service provider. However, the exclusion of dynamic or negotiable pricing properties - such as unit price amount; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts) - ensures that the SKU Price ID remains consistent across different billing periods and billing accounts within a service provider. This consistency enables efficient tracking of price fluctuations (e.g., changes in unit price amounts) over time and across accounts. Additionally, the SKU Price ID is commonly used to differentiate prices based on properties such as [*periods*](#glossary:period) and tiers."

**Assessment:** Other / Unclear. Same generic "tiers" usage as the equivalent Cost and Usage SKU Price ID section (3.1.61).

---

#### 3.5.29. Volume Tier Maximum
Anchor: `#datamodel.skuprice.volumetiermaximum`

> "Volume Tier Maximum represents the inclusive upper boundary of a volume-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datasets.skuprice.pricingunit)."

**Assessment:** Threshold-Based Tiered Pricing.

> "When combined with [Volume Tier Minimum](#datasets.skuprice.volumetierminimum), this column defines the exact volume envelope for which a specific unit price applies. If a unit price represents the highest volume tier (or if the offering uses a flat-rate pricing model with no volume limits), this value remains null to indicate there is no upper bound."

**Assessment:** Threshold-Based Tiered Pricing.

##### 3.5.29.1. Requirements
Anchor: `#datamodel.skuprice.volumetiermaximum.requirements`

> "VolumeTierMaximum MUST be null when there is no upper limit for the pricing tier."
> "VolumeTierMaximum MUST NOT be null when a subsequent, higher-volume pricing tier exists for the same offering."
> "VolumeTierMaximum MUST be the inclusive upper bound of the volume-based pricing tier."

**Assessment (all three):** Threshold-Based Tiered Pricing.

##### 3.5.29.2. Implementation Guidance
Anchor: `#datamodel.skuprice.volumetiermaximum.implementationguidance`

> "Because Volume Tier Minimum is the exclusive lower bound and Volume Tier Maximum is the inclusive upper bound, the two columns define a half-open volume interval. Practitioners route a usage quantity to the tier where the quantity is strictly greater than Volume Tier Minimum and less than or equal to Volume Tier Maximum. The highest tier carries a null Volume Tier Maximum and has no upper bound, and adjacent tiers meet at a shared boundary value with no gap or overlap."

**Assessment:** Threshold-Based Tiered Pricing. This is a precise description of the graduated/step boundary mechanism (half-open interval, adjacent tiers, no gap or overlap) — directly relevant to formalizing the tier-boundary logic in your appendix draft.

##### 3.5.29.5. Description
Anchor: `#datamodel.skuprice.volumetiermaximum.description`

> "The inclusive upper boundary of a volume-based pricing tier, measured in the designated Pricing Unit."

**Assessment:** Threshold-Based Tiered Pricing.

##### 3.5.29.6. Content Constraints
Anchor: `#datamodel.skuprice.volumetiermaximum.contentconstraints`

Table header: `| Constraint | Value |`

Row:
> "Condition | [Includes volume tier pricing](#conditions.includesvolumetierpricing)"

**Assessment:** Threshold-Based Tiered Pricing. Links this column's conditional presence to the "Includes Volume Tier Pricing" condition (see 4.28 below).

---

#### 3.5.30. Volume Tier Minimum
Anchor: `#datamodel.skuprice.volumetierminimum`

> "Volume Tier Minimum represents the exclusive lower boundary of a volume-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datasets.skuprice.pricingunit)."

**Assessment:** Threshold-Based Tiered Pricing.

> "When combined with [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum), this column defines the exact volume envelope for which a specific unit price applies. Service providers frequently employ step-tiered pricing models where the unit price decreases as consumption volume increases. The Volume Tier Minimum explicitly defines the volume threshold above which the specified unit price becomes applicable. For flat-rate or non-tiered pricing models, this value is typically zero."

**Assessment:** Threshold-Based Tiered Pricing. Notably, this is the one place in the document that uses the word "threshold" explicitly in connection with tiered pricing ("the volume threshold above which the specified unit price becomes applicable").

##### 3.5.30.1. Requirements
Anchor: `#datamodel.skuprice.volumetierminimum.requirements`

> "VolumeTierMinimum MUST be strictly less than [VolumeTierMaximum](#datasets.skuprice.volumetiermaximum) when VolumeTierMaximum is not null."
> "VolumeTierMinimum MUST be the exclusive lower bound of the volume-based pricing tier."

**Assessment (both):** Threshold-Based Tiered Pricing.

##### 3.5.30.4. Description
Anchor: `#datamodel.skuprice.volumetierminimum.description`

> "The exclusive lower boundary of a volume-based pricing tier, measured in the designated Pricing Unit."

**Assessment:** Threshold-Based Tiered Pricing.

##### 3.5.30.5. Content Constraints
Anchor: `#datamodel.skuprice.volumetierminimum.contentconstraints`

Table header: `| Constraint | Value |`

Row:
> "Condition | [Includes volume tier pricing](#conditions.includesvolumetierpricing)"

**Assessment:** Threshold-Based Tiered Pricing.

---

#### 3.5.31. Volume Tier Name
Anchor: `#datamodel.skuprice.volumetiername`

> "Volume Tier Name represents a service-provider-specified display name or label for a specific volume-based pricing tier associated with a [*SKU Price*](#glossary:sku-price)."

**Assessment:** Threshold-Based Tiered Pricing.

> "While [Volume Tier Minimum](#datasets.skuprice.volumetierminimum) and [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum) define the strict mathematical boundaries of the volume envelope, Volume Tier Name provides a human-readable identifier. This column is commonly used for displaying rate cards in reports, reconciling against vendor pricing pages, or understanding the sequential order of tiers (e.g., \"First 1000 Units\", \"Tier 1\", \"Over 50 TB\")."

**Assessment:** Threshold-Based Tiered Pricing. The examples ("First 1000 Units", "Tier 1", "Over 50 TB") are volume-range labels, not storage classes or feature-tier names.

##### 3.5.31.1. Requirements
Anchor: `#datamodel.skuprice.volumetiername.requirements`

> "VolumeTierName MUST be semantically equal to the tier name or label provided in the service-provider-published [*price list*](#glossary:price-list)."

**Assessment:** Threshold-Based Tiered Pricing.

##### 3.5.31.4. Description
Anchor: `#datamodel.skuprice.volumetiername.description`

> "A service-provider-specified display name or label for a volume-based pricing tier."

**Assessment:** Threshold-Based Tiered Pricing.

##### 3.5.31.5. Content Constraints
Anchor: `#datamodel.skuprice.volumetiername.contentconstraints`

Table header: `| Constraint | Value |`

Row:
> "Condition | [Includes volume tier pricing](#conditions.includesvolumetierpricing)"

**Assessment:** Threshold-Based Tiered Pricing.

---

## 4. Conditions

### 4.1. Condition List
Anchor: `#conditions.conditionlist`

Table header: `| Condition | Category | Description |`

Row:
> "Includes Volume Tier Pricing | Pricing | Operating model includes volume-based tier pricing."

**Assessment:** Threshold-Based Tiered Pricing.

---

### 4.28. Includes Volume Tier Pricing
Anchor: `#conditions.includesvolumetierpricing`

> "The Includes Volume Tier Pricing condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes volume-based pricing tiers."

**Assessment:** Threshold-Based Tiered Pricing.

#### 4.28.1. Requirements
Anchor: `#conditions.includesvolumetierpricing.requirements`

> "IncludesVolumeTierPricing MUST evaluate to true when the *operating model* includes volume-based pricing tiers."
> "IncludesVolumeTierPricing MUST evaluate to false when the *operating model* does not include volume-based pricing tiers."

**Assessment (both):** Threshold-Based Tiered Pricing.

#### 4.28.4. Description
Anchor: `#conditions.includesvolumetierpricing.description`

> "A verifiable state indicating whether the *operating model* includes volume-based pricing tiers."

**Assessment:** Threshold-Based Tiered Pricing.

---

## 8. Glossary
Anchor: `#glossary`

### Block Pricing
Anchor: `#glossary:block-pricing`

> "A pricing approach where the cost of a particular resource or service is determined based on predefined quantities or tiers of usage. In these scenarios, the Pricing Unit and the corresponding Pricing Quantity can be different from the Consumed Unit and Consumed Quantity."

**Assessment:** Threshold-Based Tiered Pricing. This remains the only glossary-level definition touching the tier concept, and it is still not cross-referenced to the new Volume Tier Maximum/Minimum/Name columns (3.5.29–3.5.31) or to the Includes Volume Tier Pricing condition (4.28).

---

## 9. Appendix

### 9.5. Examples: Contract Commitments

#### 9.5.2.4.3. Commitment 3: Cross-Cloud Data Connector (Tiered Usage)
Anchor: `#appendix.examples:contractcommitments.examples.scenario2:saasexpansion&hybridconnector.commitment3:cross-clouddataconnectortieredusage`

(The word "Tiered" appears only in the section heading itself; the body text under this heading does not contain an additional sentence using the word "tier.")

**Assessment:** Other / Unclear (heading-only occurrence; underlying scenario describes usage-based commitment on data volume, so if classified by scenario content it would lean Threshold-Based, but the word itself only appears in the title).

#### 9.5.2.5. Data Example: AGR-44-GAMMA
Anchor: `#appendix.examples:contractcommitments.examples.dataexample:agr-44-gamma`

Table header: `| Column | Commitment 1: AI Training | Commitment 2: Observability Seats | Commitment 3: Data Connector |`

Row:
> "CC Description | `H100 GPU Reservation - Q1` | `StackLens Monitoring Seats` | `Inter-Cloud Egress Tier`"

**Assessment:** Threshold-Based Tiered Pricing. "Inter-Cloud Egress Tier" describes the Commitment 3 data connector, which per the scenario narrative (9.5.2.4.3) is a usage/volume-based commitment on data egress.

Row:
> "CC Type | `Resource Reservation` | `SaaS Subscription` | `Usage Tier`"

**Assessment:** Threshold-Based Tiered Pricing, for Commitment 3 ("Usage Tier"). Note: `ContractCommitmentType` is a free-text, service-provider-assigned display field with no formal Allowed Values list, so this is an illustrative example value, not a normative term.

#### 9.5.2.6. Scenario 3: Scale-Out & Overage
Anchor: `#appendix.examples:contractcommitments.examples.scenario3:scale-out&overage`

> "This scenario focuses on how the model handles growth beyond initial estimates. In the master agreement `AGR-11-DELTA`, the customer has established \"safety nets\" and tiered pricing to ensure that scale-out events are still covered by negotiated rates, even after a primary pool is exhausted."

**Assessment:** Threshold-Based Tiered Pricing. Describes an overage/scale-out mechanism tied to exceeding a committed volume — consistent with a threshold-triggered pricing change.

##### 9.5.2.6.1. Commitment 1 & 2: Database Storage Tiers (Base + Overage)
Anchor: `#appendix.examples:contractcommitments.examples.scenario3:scale-out&overage.commitment1&2:databasestoragetiersbase+overage`

> "**Context:** The customer commits to a base of 100TB of Database storage. To avoid \"sticker shock\" if they grow to 150TB, they have a pre-negotiated **Overage Tier**."

**Assessment:** Threshold-Based Tiered Pricing. Despite the section heading using "Storage Tiers," the actual mechanism described is a volume-threshold overage rate applied once a committed storage quantity (100TB) is exceeded — this is a threshold/volume pricing concept applied to a storage resource, not a storage-class/performance-tier concept like the StorageClass example in 3.1.60.2/3.5's FOCUS-Defined Properties. Flagging this as a point of potential terminology ambiguity: the heading says "Storage Tiers" but the mechanism is threshold-based, not a storage class.

#### 9.5.2.7. Data Example: AGR-11-DELTA
Anchor: `#appendix.examples:contractcommitments.examples.dataexample:agr-11-delta`

Table header: `| Column | Commitment 1: Base Storage | Commitment 2: Storage Overage | Commitment 3: CDN Annual |`

Row:
> "CC Description | `Base 100TB DB Storage` | `Tier 2 Storage Overage` | `1PB Annual CDN Volume`"

**Assessment:** Threshold-Based Tiered Pricing. "Tier 2 Storage Overage" for Commitment 2 corresponds to the overage tier described in 9.5.2.6.1 above — a volume-threshold overage rate, not a storage class.

Row:
> "CC Type | `Usage Tier` | `Usage Tier` | `Volume Commitment`"

**Assessment:** Threshold-Based Tiered Pricing (for Commitment 1 and 2, both `Usage Tier`). As above, `ContractCommitmentType` is free text with no formal Allowed Values list.

---

### 9.11. Examples: SaaS

#### 9.11.3. Virtual Currency Pricing Model
##### 9.11.3.4. Scenario A2: Usage of Virtual Currency Purchased Without a Discount
Anchor: `#appendix.examples:saas.virtualcurrencypricingmodel.scenarioa2:usageofvirtualcurrencypurchasedwithoutadiscount`

> "PricingQuantity reflects the amount of usage of the PricingUnit for each charge and is equivalent to ConsumedQuantity. While relevant to this example, there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same."

**Assessment:** Threshold-Based Tiered Pricing. Generic reference to tiered pricing as a scenario where PricingQuantity and ConsumedQuantity diverge — consistent with a volume-threshold mechanism, though no further detail is given here.

##### 9.11.3.7. Scenario B2: Usage of Virtual Currency Purchased at a Discount
Anchor: `#appendix.examples:saas.virtualcurrencypricingmodel.scenariob2:usageofvirtualcurrencypurchasedatadiscount`

> "PricingQuantity reflects the amount of usage of the PricingUnit for each charge and is equivalent to ConsumedQuantity. While relevant to this example, there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same."

**Assessment:** Threshold-Based Tiered Pricing. Identical sentence repeated verbatim from Scenario A2 above.

---

#### 9.11.4. Billing Scenario Examples
Anchor: `#appendix.examples:saas.billingscenarioexamples`

Table header: `| Scenario | Service Provider | What You'll Learn |`

Row:
> "[Tiered Pricing with Committed Minimum](#appendix.examples:saas.billingscenarioexamples.tieredpricingwithcommittedminimum:emailapiplatform) | PulseMail | Plan fee as a usage-denominated *commitment discount* with Used/Unused split and overage pricing. `CommitmentDiscountCategory` = \"Usage\". Two billing periods showing under- and over-minimum scenarios."

**Assessment:** Threshold-Based Tiered Pricing. The scenario title and description describe a usage allowance/overage mechanism, i.e., a threshold-based pricing change.

##### 9.11.4.5. Flat-Rate SaaS Licensing: Fixed Monthly Subscription
Anchor: `#appendix.examples:saas.billingscenarioexamples.flat-ratesaaslicensing:fixedmonthlysubscription`

> "A team communications [*service provider*](#glossary:service-provider), CollabChat, offers both per-user and flat-rate subscription tiers. This example uses the flat-rate option, where all features and unlimited users are included for a fixed monthly fee with no per-user pricing."

**Assessment:** Feature Tier. "Subscription tiers" here refers to different SaaS plan options (per-user vs. flat-rate), not a volume/threshold-based unit price mechanism — this is a plan/feature-bundling concept.

##### 9.11.4.7. Tiered Pricing with Committed Minimum: Email API Platform
Anchor: `#appendix.examples:saas.billingscenarioexamples.tieredpricingwithcommittedminimum:emailapiplatform`

(Section heading itself: "Tiered Pricing with Committed Minimum: Email API Platform" — heading-only occurrence, not a separate sentence.)

**Assessment:** Threshold-Based Tiered Pricing (based on heading and the body text quoted below).

> "A SaaS email API [*service provider*](#glossary:service-provider), PulseMail, offers tiered plans that include a monthly email allowance. Emails sent within the allowance are covered by the plan fee. Emails exceeding the allowance are billed at a per-email overage rate. The plan minimum functions as a usage-denominated [*commitment discount*](#glossary:commitment-discount) because the customer pays a fixed fee for a quantity of usage units."

**Assessment:** Threshold-Based Tiered Pricing. This describes an allowance/overage threshold mechanism (emails within allowance vs. exceeding allowance), though it is modeled here as a commitment discount rather than through the new Volume Tier columns — worth noting as a possible inconsistency in how the spec represents threshold-based scenarios across different mechanisms (SKU Price Volume Tier columns vs. Contract Commitment/CommitmentDiscount modeling).

> "[**CSV Example**](/specification/data/saas_examples/tiered_pricing_committed_minimum_a.csv)"

**Assessment:** Other / Unclear. This is a file link reference, not a substantive usage of the term.

---

## Summary: Where "tier" Is Used and For What

| Location | Context of "tier" Usage | Classification |
| :--- | :--- | :--- |
| 3.1.42.2 (Pricing Category) | "volume/tiered pricing" as part of "Standard" pricing category | Threshold-Based Tiered Pricing |
| 3.1.58 / 3.5.18 (SKU ID, both datasets) | Pricing tier as a reason for price variation within a SKU; generic "tier" in price-detail examples | Threshold-Based Tiered Pricing / Other-Unclear (mixed, see individual citations) |
| 3.1.60 / 3.5.24 (SKU Price Details / SKU Price ID) | "Tiers" listed as a generic "core stable pricing property" | Other / Unclear |
| 3.1.60.2 (FOCUS-Defined Properties — StorageClass) | "Class or tier of storage" — Hot/Archive/Nearline | Storage Tier |
| 3.3.3.2 (Contract Commitment Benefit Category) | "volume-tier discounts" (Discount row); "software tiers" (Entitlement row) | Threshold-Based Tiered Pricing / Feature Tier |
| 3.3.8 (Contract Commitment Discount Percentage) | Normative "multiple tiers" / "pricing tier" requirement, with volume/spend example | Threshold-Based Tiered Pricing |
| 3.3.10.2 (Contract Commitment Fulfillment Interval) | "tiered discounts" as a Monthly interval example | Threshold-Based Tiered Pricing |
| **3.5.1, 3.5.2, 3.5.3 (SKU Price dataset structure)** | Volume Tier Maximum/Minimum/Name as normative columns; "volume tier" in relationship and uniqueness logic | **Threshold-Based Tiered Pricing** |
| **3.5.29–3.5.31 (Volume Tier Maximum / Minimum / Name)** | Full normative definitions of the three new columns; explicit "threshold" language in 3.5.30 | **Threshold-Based Tiered Pricing** |
| **4.1, 4.28 (Includes Volume Tier Pricing condition)** | Normative condition gating the three Volume Tier columns | **Threshold-Based Tiered Pricing** |
| Glossary: Block Pricing | "predefined quantities or tiers of usage" | Threshold-Based Tiered Pricing |
| Appendix 9.5 (Contract Commitment examples) | "Tier"/"Tiered" in CC Description/CC Type free-text example values; "Overage Tier" mechanism | Threshold-Based Tiered Pricing (predominantly) |
| Appendix 9.11 (SaaS examples) | "Tiered pricing" generic scenario reference; "subscription tiers" (flat-rate vs. per-user); "tiered plans" with allowance/overage | Threshold-Based Tiered Pricing / Feature Tier (mixed) |
