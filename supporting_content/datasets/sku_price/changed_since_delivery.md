# SKU Price Changed-Since Delivery

Background on why the SKU Price dataset requires a changed-since configuration and why honoring it is mandatory. This document records design intent and is not normative.

## The Problem

SKU Price uses one row per price type (e.g., "List", "Contracted") with effective dates. That layout is compact when each delivery carries only what changed. When every delivery re-sends every current price, the same layout is larger than the monthly price sheets providers publish today, because one price sheet row becomes several rows.

Most prices do not change from month to month. If a service provider re-sends the full catalog each time, practitioners pay to transfer, store, and deduplicate rows they already have.

## Size Analysis

Source: 14 monthly Azure EA price sheets (September 2025 to October 2026) for one billing account, converted to both layouts with a FinOps toolkit prototype. Rows and compressed size as stored. "Re-sent" sizes are estimated from the bytes per row of the matching changes-only table.

| Layout | Delivery | Rows | Size |
| --- | --- | --- | --- |
| Today's monthly price sheet (one row per price, all price types as columns) | Full sheet every month | 18.78M | 2.34 GB |
| SKU Price rows (one row per price type) | Changes only | 4.17M | 0.64 GB |
| SKU Price rows | Every current row re-sent every month | 45.79M | ~7.5 GB |
| Price types as columns (one row per price) | Changes only | 1.79M | 0.33 GB |
| Price types as columns | Every current row re-sent every month | 18.78M | ~3.7 GB |

Per-month view for SKU Price rows:

| Measure | Rows |
| --- | --- |
| First delivery (September 2025) | 2.71M |
| Current rows in a full delivery (October 2026) | 3.89M |
| New or changed rows per month, average after the first delivery | 112K |
| Rows closed with an effective end per month, average | 22K |
| Changed-since delivery for October 2026 | 149K (3.8% of a full delivery) |

## Findings

* The theory holds. Without changed-since delivery, the SKU Price row layout is about 2.4 times the rows and 3.2 times the size of today's monthly price sheets.
* With changed-since delivery, the same layout is about 3.7 times smaller than today's price sheets and 12 times smaller than re-sending every row.
* Each monthly changed-since delivery is about 4% of a full delivery.
* Closed prices are about one in five changed rows. A changed-since delivery has to carry them as records with an effective end; otherwise a practitioner cannot tell a removed price from an unchanged one.

## Why MUST, Not MAY

A changed-since option that a service provider is free to ignore gives practitioners no size guarantee. They would still have to plan storage and pipelines for full re-sends and deduplicate every delivery. The requirement therefore makes the configuration mandatory and requires that unchanged records be excluded when it is used.

The cost to a service provider is low. SKU Price Last Updated is already mandatory and already defined as the last time any value on the record changed, so the filter uses data the provider has to produce anyway.

## Implementation Notes

* SKU Price Last Updated has to reflect the last change, not the last time a record was generated. In the prototype, the column holds the last load time, so every current row looks changed in the latest month (all 3.89M current rows show October 2026). A changed-since filter on that value would return the full catalog.
* Practitioners apply a changed-since delivery by replacing rows that share the dataset key (ServiceProviderName, SkuPriceId, ContractId, SkuPriceEffectiveStart, PricingCurrency, UnitPriceType) and adding the rest.
* A full delivery (no changed-since point) remains available to start over or recover from gaps.

## Reproducing

Source data: monthly Azure EA price sheets. Prototype: FinOps toolkit SKU Price v1.5 preview. "Re-sent" rows are the sum, over all monthly loads, of rows whose effective period covers that month.
