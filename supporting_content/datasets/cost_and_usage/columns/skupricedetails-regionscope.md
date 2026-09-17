# Property: RegionScope (SkuPriceDetails)

Background for the FOCUS-defined `RegionScope` property of `SkuPriceDetails`, added under FR #2414. Records why the property exists, how it is named, how it relates to `RegionId` in Cost and Usage and to `PricingRegionId` in the SKU Price dataset, and what changes if the property is later elevated to a SKU Price column.

## The Axis

Service providers price the same capability at more than one geographic breadth and charge differently for each. The breadth is a property of the price, not of the resource: two charges can run in the same region and carry different unit prices because one was bought at a global rate and the other at a regional rate.

Each provider names the axis and its levels differently. The table below is from @flanakin's naming research on Action Item #2672.

| Provider | Term for the axis | Levels |
|---|---|---|
| AWS Bedrock | "Geo scope" | In-Region, Geo, Global inference profiles |
| Azure AI Foundry | "deployment type" | Global, Data zone, Azure geography |
| Google Cloud | "location type" | region, dual-region, multi-region, zone |

Three of the three name the axis with a classifier word. None uses "serving", which is why the original `ServingScope` name did not survive review.

AI model serving is where providers price this most distinctly today, which is why both appendix scenarios use AI SKUs. The dimension is not AI-specific: it applies wherever a provider prices one capability at more than one geographic breadth. Other offerings that vary breadth commonly bundle it with replication, which the `Redundancy` property already describes.

## Naming

Task Force 2 settled the base word on 2026-09-02: "region", with the qualifier left open. The final name is `RegionScope`, recommended by the Action Item #2672 research and proposed independently by @marc-perreaut on 2026-09-03.

Candidates considered, and why each was set aside:

| Candidate | Why not |
|---|---|
| `ServingScope` | No provider uses "serving" for this axis. |
| `PricingRegionScope` | None of the other 17 `SkuPriceDetails` properties carries a pricing qualifier. `Redundancy`, `StorageClass`, and `OperatingSystem` describe the SKU price without saying so, because the column already sets that context. Identical prefixes against `PricingRegionId` also invite the confusion the next section separates, since one holds an identifier and the other a class. |
| `GeographicScope`, `GeoScope` | "Geo" is reserved for a later geographic aspect of resource regions. In AWS's own taxonomy "Geo" is the middle level rather than the axis, so `GeoScope` = "Global" names a non-geo geo-scope. `GeoScope` additionally abbreviates. |
| `Region`, bare `Scope` | `Region` collides with `RegionId` and `RegionName` on the same row and says nothing about what it holds. A bare `Scope` was ruled out for a location property. |
| `RegionCategory` | Every `*Category` column in FOCUS carries a normative allowed-value list. The name would promise a closed enumeration this property does not define. |
| `RegionType`, `RegionGranularity` | Both workable. `RegionType` reads softer on rows where `RegionId` is null; `RegionGranularity` is less natural to say. Neither improves on `RegionScope`. |

## Relationship to RegionId and PricingRegionId

Three questions sit close together. Each has its own home, and none of them substitutes for another.

| Property | Dataset | Question it answers | Value it holds |
|---|---|---|---|
| `RegionId` | Cost and Usage | Which single region was the resource provisioned in? | A region identifier, for example "us-east-1" |
| `RegionScope` | Cost and Usage, inside `SkuPriceDetails` | How broad an area does the price on this charge cover? | A breadth class, for example "Global" or "DataZone" |
| `PricingRegionId` | SKU Price, defined on PR #2424 | Which area does this unit price apply to? | A boundary identifier, including a macro-region, for example "eu" |

PR #2424 draws the first half of this distinction itself, in the `PricingRegionId` Implementation Guidance: Pricing Region ID defines the geographic boundary for which the rate is valid, and Region ID defines the physical location where a resource is provisioned. `RegionScope` is the Cost and Usage side of the same axis, carried as a class rather than as an identifier, because Cost and Usage has no column for the priced area.

**Neither `RegionScope` nor `PricingRegionId` derives the other.** A `PricingRegionId` of "eu" does not say whether "eu" is a region, a macro-region, or the whole world, without a provider-specific lookup. A `RegionScope` of "DataZone" says the breadth without saying which data zone. The pair is lossless where either alone is not.

PR #2424's dataset definition relates SKU Price to Cost and Usage through `SkuPriceId`. On that join the two read together as the identifier and its class, so a practitioner working from a charge can reach both the priced area and its breadth without decoding a provider-specific region string.

One consequence for the examples: `RegionId` is defined for "an isolated geographic area where a resource is provisioned or a service is provided", so a macro-region does not belong in it. An earlier draft of the Scenario B data zone row carried a `RegionId` of "eu"; it now carries "northeurope", a single region inside the area the fictitious provider prices as one data zone. The identifier for the data zone itself is what `PricingRegionId` carries.

## If RegionScope Becomes a SKU Price Column

The property is defined in `SkuPriceDetails` for now. @ijurica asked at Task Force 2 on 2026-09-16 that any property that could later move to the SKU Price dataset be checked for consistency with the columns that dataset introduces. This section records what that move would look like and why the two dimensions are worth carrying together, without asserting that it happens.

The SKU Price dataset carries no `SkuPriceDetails` column, so a property that moves there becomes a column. `RegionScope` beside `PricingRegionId` produces no name collision, and the pair reads as identifier plus class.

What the pair enables on a rate card that neither enables alone:

* **Premium analysis across the breadth ladder.** Pivoting unit price by `RegionScope` gives the regional-over-global premium per SKU as a group-by. Using `PricingRegionId` alone requires a provider-specific mapping from region strings to breadth before the pivot is possible.
* **Cross-provider rate comparison.** Two rate cards can be compared at the same breadth without decoding each provider's region vocabulary. This is stronger on SKU Price than on Cost and Usage, because a rate card carries every price point rather than only the ones a customer used.
* **Rate-card completeness checks.** Grouping by SKU and counting distinct `RegionScope` values answers whether a provider publishes a global price for every capability it prices regionally. Without the class, that question requires enumerating region identifiers and knowing which are macro-regions.
* **Partition reasoning.** PR #2424 allows a provider to partition price-list delivery, for example by region. `RegionScope` distinguishes a partition that contains no global price points from one that was never delivered. Without it both look like a missing row.
* **Migration forecasting.** Costing a move from regional to data zone pricing means filtering the rate card to the same SKU at a different breadth. That is a predicate on `RegionScope` rather than a guess about which `PricingRegionId` is the data zone.
* **Disambiguating "global" on the same row.** `SkuPriceEligibility.IsGlobalScope` on PR #2424 is a non-geographic flag: it marks a price that applies to all entities. An explicit geographic-breadth column makes clear that `IsGlobalScope` is about who is eligible rather than where the price applies.

What elevation would require, and what it does not settle:

* The property becomes a column with its own Content Constraints, feature level, and operating model conditions.
* The relationship to the `SkuPriceDetails` property has to be stated, since a value in two places needs a rule about which wins.
* Elevation does not by itself settle the value set. That question is open today and is recorded below.

## Open Questions

* **The value set is not normative.** Task Force 2 on 2026-08-19 recorded that FOCUS defines the key and each provider defines the values, and every String property in the `SkuPriceDetails` table lists examples rather than allowed values. Two lines in the appendix read as though the values were standardized. Those hold only where providers converge on the same words, and the table at the top of this file shows that they do not. Either the values get a normative set, or the appendix claims soften to what provider-defined values support. The Action Item #2672 research reaches the same place from terminology, noting that "DataZone" is Azure's word while AWS's middle level is a named geography. A closed value set also changes which names are appropriate, since `RegionCategory` becomes available once the enumeration exists.
* **Value overlap with `Redundancy` on "Global".** `Redundancy` example values are "Local", "Zonal", and "Global"; this property's are "Global", "Regional", and "DataZone". The definitions are separated in footnote 4 and a SKU may carry both, so one row can read "Global" twice meaning two different things. The two ladders should either align or differ visibly.
* **SKU property or SKU price property.** Raised at Task Force 2 on 2026-09-02 and not yet dispositioned.

## Reference

* Action Item #2672, naming research, on PR #2613
* PR #2424, the SKU Price dataset, for `PricingRegionId` and `SkuPriceEligibility`
* [AWS Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
* [Azure AI Foundry deployment types](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/deployment-types)
* [Google Cloud bucket locations](https://cloud.google.com/storage/docs/locations)
