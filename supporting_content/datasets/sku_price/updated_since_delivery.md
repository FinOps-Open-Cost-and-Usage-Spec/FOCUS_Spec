# SKU Price Period and UpdatedSince Delivery

Background on why the SKU Price dataset requires period configuration (PeriodStart, PeriodEnd, UpdatedSince) and why honoring it is mandatory. This document records design intent and is not normative.

## The Problem

SKU Price uses one row per price type (e.g., "List", "Contracted") with effective dates. That layout is compact when each delivery carries only what changed. When every delivery re-sends every current price, the same layout is larger than the monthly price sheets providers publish today, because one price sheet row becomes several rows.

Most prices do not change from month to month. If a service provider re-sends the full catalog each time, practitioners pay to transfer, store, and deduplicate rows they already have.

## Configuration Options

* PeriodStart: inclusive; defaults to the current billing period start.
* PeriodEnd: exclusive; no default.
* UpdatedSince: only rows last updated after this time. Not set by default.

PeriodStart and PeriodEnd select prices by effective period (SkuPriceEffectiveStart, SkuPriceEffectiveEnd). UpdatedSince selects by SkuPriceLastUpdated. They answer different questions: which prices applied during a period, and which prices changed since a time. A price announced in July for January changes in July, so only UpdatedSince finds it for a practitioner pulling changes in July.

UpdatedSince is not set by default so practitioners fall into the pit of success and receive every row they may need. Setting it is the opt-in that delivers the size savings below. A request-based delivery cannot know whether the practitioner has earlier data, so it never sets it. Scheduled deliveries after the first set it to the latest last-updated value in the previous delivery. PeriodStart and PeriodEnd default independently of UpdatedSince. Scheduled deliveries after the first set PeriodStart to the earliest date so changes (e.g., future-dated prices, retirements) are not missed.

The row key lets a practitioner tell which delivered row a new version supersedes. Cost and Usage has no last-updated column or defined key, so UpdatedSince does not apply to it. A ChargeLastUpdated column could be proposed separately. PeriodStart and PeriodEnd can apply to it using ChargePeriodStart and ChargePeriodEnd once it declares a period.

## Scenarios

| # | Scenario | PeriodStart | PeriodEnd | UpdatedSince | Delivery mechanism |
| --- | --- | --- | --- | --- | --- |
| 1 | Initial or one-time request for current prices | default | default | not set | Overwrite |
| 2 | Initial request for historical prices | date | date | not set | Overwrite |
| 3 | Later request for prices changed since a time | earliest date | none | date | Versioned Append |
| 4 | Scheduled delivery after the first | earliest date | none | latest last-updated value in previous delivery | Versioned Append |
| 5 | Prices active during S to E, only if changed since S1 | S | E | S1 | Versioned Append |
| 6 | Every version of prices active during S to E | S | E | earliest date | Versioned Append |

> **Note:** Versioned Append means each row is a new version that supersedes earlier rows with the same row key. Additive Append, where rows only add, is a different case.

If PeriodStart and PeriodEnd are left at their defaults in scenario 3, only prices active on or after the start of the current billing period are returned.

The first scheduled delivery uses scenario 1 or 2 so the practitioner starts with all prices.

## Size Analysis

Source: 14 monthly Azure EA price sheets (September 2025 to October 2026) for one billing account, converted to both layouts with a FinOps toolkit prototype. Rows and compressed size as stored. "Re-sent" sizes are estimated from the bytes per row of the matching changes-only table.

| Layout | Delivery | Rows | Size |
| --- | --- | --- | --- |
| Today's monthly price sheet (one row per price, all price types as columns) | Full sheet every month | 18.78M | 2.34 GB |
| SKU Price rows (one row per price type) | Changes only | 4.17M | 0.64 GB |
| SKU Price rows | Every current row re-sent every month | 45.79M | ~7.0 GB |
| Price types as columns (one row per price) | Changes only | 1.79M | 0.33 GB |
| Price types as columns | Every current row re-sent every month | 18.78M | ~3.5 GB |

Per-month view for SKU Price rows:

| Measure | Rows |
| --- | --- |
| First delivery (September 2025) | 2.71M |
| Current rows in a full delivery (October 2026) | 3.89M |
| New or changed rows per month, average after the first delivery | 112K |
| Rows closed with an effective end per month, average | 22K |
| UpdatedSince delivery for October 2026 | 149K (3.8% of a full delivery) |

## Findings

* The theory holds. Without UpdatedSince, the SKU Price row layout is about 2.4 times the rows and 3.0 times the size of today's monthly price sheets.
* With UpdatedSince, the same layout is about 3.7 times smaller than today's price sheets and 11 times smaller than re-sending every row.
* Each monthly UpdatedSince delivery is about 4% of a full delivery.
* Closed prices are about one in five changed rows. An UpdatedSince delivery has to carry them as records with an effective end; otherwise a practitioner cannot tell a removed price from an unchanged one.

## Why Mandatory, Not Optional

A period option that a service provider is free to ignore gives practitioners no size guarantee. They would still have to plan storage and pipelines for full re-sends and deduplicate every delivery. The requirements therefore make the configuration mandatory and exclude rows last updated on or before UpdatedSince when it is set.

The cost to a service provider is low. SKU Price Last Updated is already mandatory and already defined as the last time any value on the record changed, so the filter uses data the provider has to produce anyway.

## Avoiding Duplicate Rows

Each changed row must be delivered once. Duplicates raise support requests because practitioners expect unique rows per delivery.

A data generator does not need to track every row it delivered. It can use a dated query instead:

* Pick a cutoff time behind data processing, so no row is still changing at the cutoff.
* Deliver rows last updated after UpdatedSince and up to the cutoff.
* Use the latest last-updated value delivered as UpdatedSince for the next delivery.

Example: for a request at 12:00 with a 1-hour margin, deliver rows updated through 11:00. A row added at 12:01 cannot be missed or repeated, because the next delivery starts after 11:00.

## Implementation Notes

* SKU Price Last Updated has to reflect the last change, not the last time a record was generated. In the prototype, the column holds the last load time, so every current row looks changed in the latest month (all 3.89M current rows show October 2026). An UpdatedSince filter on that value would return the full catalog.
* Practitioners apply an UpdatedSince delivery by superseding rows that share the *row key* and adding the rest.
* A full delivery (UpdatedSince not set) remains available to start over or recover from gaps.

## Reproducing

Source data: monthly Azure EA price sheets. Prototype: FinOps toolkit SKU Price v1.5 preview. "Re-sent" rows are the sum, over all monthly loads, of rows whose effective period covers that month.
