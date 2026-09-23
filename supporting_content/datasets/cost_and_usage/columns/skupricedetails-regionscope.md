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

`SkuPriceEligibility`, also defined on PR #2424, is not a fourth entry in that table. It carries a predicate over arbitrary dimensions rather than a location, and it answers which entities may receive a price rather than how broad an area the price covers. The comparison invites itself because region-shaped eligibility is common: five of the nine examples in that column's appendix constrain `RegionId`. The `IsGlobalScope` flag on the same object is the part most likely to be misread. It marks a price that is not restricted to an enumerated set of entities and carries no geographic meaning, so a price can be regionally scoped and globally eligible at the same time.

**Neither `RegionScope` nor `PricingRegionId` derives the other.** A `PricingRegionId` of "eu" does not say whether "eu" is a region, a macro-region, or the whole world, without a provider-specific lookup. A `RegionScope` of "DataZone" says the breadth without saying which data zone. The pair is more informative than either alone, though it is not complete: which regions sit inside "eu" is recoverable from neither, so testing whether a given charge falls inside the priced area still takes a provider lookup.

Eligibility does not close that gap either. Counting the regions in a `SkuPriceEligibility` inclusion set looks like a way to infer breadth, and it fails twice. Inclusions are required only when a price is neither globally nor complexly scoped, so the public list prices that make up most of a rate card carry `IsGlobalScope` and no region rule to count. Where inclusions are present, a dimension omitted from them is defined as an implicit wildcard, so a regional price whose provider wrote no region rule is indistinguishable from a global one. An enumerated set does not say whether it is the provider's full roster for that boundary or a negotiated subset.

PR #2424's dataset definition relates SKU Price to Cost and Usage through `SkuPriceId`, as a one-to-many relationship: resolving the record that applies to a charge also takes the effective period, `ContractId`, quantity tier, and pricing currency. Once resolved, the two read together as the identifier and its class, so a practitioner working from a charge can reach both the priced area and its breadth without having to infer the breadth from a provider-specific region string.

One consequence for the examples: `RegionId` is defined for "an isolated geographic area where a resource is provisioned or a service is provided", so a macro-region does not belong in it. An earlier draft of the Scenario B data zone row carried a `RegionId` of "eu"; it now carries "northeurope", a single region inside the area the fictitious provider prices as one data zone. The identifier for the data zone itself is what `PricingRegionId` carries.

## If RegionScope Becomes a SKU Price Column

The property is defined in `SkuPriceDetails` for now. @ijurica asked at Task Force 2 on 2026-09-16 that any property that could later move to the SKU Price dataset be checked for consistency with the columns that dataset introduces. This section records what that move would look like and why the two dimensions are worth carrying together, without asserting that it happens.

The SKU Price dataset carries no `SkuPriceDetails` column, so a property that moves there becomes a column. `RegionScope` beside `PricingRegionId` produces no name collision, and the pair reads as identifier plus class.

PR #2424's own supporting content reaches the same diagnosis from the other side and names a different destination. `scope_and_evolution.md` records that `SkuPriceDetails` properties are available only for SKUs an organization has already consumed, which it calls the wrong way round for a dataset whose purpose is pricing what has not been bought yet. The resolution it proposes is a companion SKU Properties dataset joined on `SkuId`, not a SKU Price column. Both routes answer the availability problem, and which one fits turns on the undispositioned question at the end of this file: whether region scope is a property of the SKU or of the SKU price.

What the pair enables on a rate card that neither enables alone, given a value set consistent enough to group on:

* **Premium analysis across the breadth ladder.** Pivoting unit price by `RegionScope` gives the regional-over-global premium per SKU as a group-by. Using `PricingRegionId` alone requires a provider-specific mapping from region strings to breadth before the pivot is possible.
* **Cross-provider rate comparison.** Two rate cards can be compared at the same breadth without decoding each provider's region vocabulary, but only where both providers reached for the same breadth words. The table at the top of this file shows three providers using three vocabularies, so this one is contingent on the value set question below rather than on elevation.
* **Rate-card completeness checks.** Grouping by SKU and counting distinct `RegionScope` values answers whether a provider publishes a global price for every capability it prices regionally. Without the class, that question requires enumerating region identifiers and knowing which are macro-regions.
* **Partition reasoning.** PR #2424 allows a provider to partition price-list delivery, for example by region. `RegionScope` distinguishes a partition that contains no global price points from one that was never delivered. Without it both look like a missing row.
* **Migration forecasting.** Costing a move from regional to data zone pricing means filtering the rate card to the same SKU at a different breadth. That is a predicate on `RegionScope` rather than a guess about which `PricingRegionId` is the data zone.

What elevation would require, and what it does not settle:

* The property becomes a column with its own Content Constraints, feature level, and operating model conditions.
* The relationship to the `SkuPriceDetails` property has to be stated, since a value in two places needs a rule about which wins.
* Elevation does not by itself settle the value set. That question is open today and is recorded below.

## Open Questions

* **Whether the value set becomes normative.** Task Force 2 on 2026-08-19 recorded that FOCUS defines the key and each provider defines the values, and every String property in the `SkuPriceDetails` table lists examples rather than allowed values. The appendix's cross-provider comparisons are stated on that basis: they hold where both providers use the same value, and the table at the top of this file shows three providers using three vocabularies today. That table comes from the Action Item #2672 research, which also notes that "DataZone" is Azure's word while AWS's middle level is a named geography. A closed value set would also change which names are appropriate, since `RegionCategory` becomes available once the enumeration exists, and it would be the place to revisit the "Global" value this property shares with `Redundancy`. Footnote 4 separates the two meanings until then: replication across regions on `Redundancy`, and a price that applies in any region on `RegionScope`.
* **SKU property or SKU price property.** Raised at Task Force 2 on 2026-09-02 and not yet dispositioned.

## Reference

* Action Item #2672, naming research, on PR #2613
* PR #2424, the SKU Price dataset, for `PricingRegionId` and `SkuPriceEligibility`, and its `scope_and_evolution.md` supporting content
* [AWS Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
* [Azure AI Foundry deployment types](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/deployment-types)
* [Google Cloud bucket locations](https://cloud.google.com/storage/docs/locations)
