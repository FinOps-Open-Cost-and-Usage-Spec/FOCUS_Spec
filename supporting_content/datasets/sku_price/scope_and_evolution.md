# SKU Price Dataset Scope and Evolution

Background on what the initial SKU Price specification sets out to do, what it deliberately leaves undone, and why. This document records design intent and is not normative.

## What the Dataset Is

The SKU Price dataset is a price list. It describes the rates a service provider offers, independent of whether any of those rates was ever used, and it is not derived from Cost and Usage data. A practitioner reads it the way they would read a published pricing page, except that every provider's page has the same shape.

One requirement ties it back to consumption: the dataset contains at least one record for every SKU Price ID referenced in the Cost and Usage dataset. That sets a floor rather than a ceiling. A conformant dataset covers everything that was billed, and a service provider is free to publish the full catalog beyond that.

The distinction matters when reading a query result. A row in SKU Price is an offer. A row in Cost and Usage is an event. What an organization actually paid is answered in Cost and Usage. What it could pay is answered here.

## What the Initial Specification Answers

Two supported features:

* **Catalog Discovery and Price Estimation**: pricing an architecture that does not exist yet, from public rates, accounting for which entities are eligible for a price and the dates that price applies.
* **Rate Optimization and Contract Evaluation**: measuring a negotiated rate against the public rate, resolving which quantity tier observed consumption falls into, and comparing the purchase terms offered for a SKU.

## What the Initial Specification Does Not Answer

### There is No Coverage-Aware Unit Price

The dataset carries List Unit Price and Contracted Unit Price. It does not carry a rate reflecting a commitment discount having been applied. A practitioner cannot ask it what an M5 large will cost given the reservations they already hold.

This is a structural limit rather than a missing column. The same SKU prices differently depending on which commitment covers it: one rate under a one year reservation, another under a three year reservation, another under a savings plan, and different rates again where any of those was itself negotiated. A single coverage-aware price column would have to pick one, and there is no row for it to sit on. Row uniqueness is defined across service provider, SKU Price ID, contract, quantity tier, effective start, and pricing currency, and none of those members distinguish one commitment instrument from another.

Where a service provider needs to express this today, the specification directs them to custom columns, stating that SKU Price should include custom columns needed to identify specific rate card routing logic when FOCUS columns are not sufficient. Guidance for what those columns look like is open under #2590. Whether a pattern emerges from that guidance worth standardizing is the question that follows it.

### The Rate Difference is the Negotiated Portion, Not the Whole Benefit

Subtracting Contracted Unit Price from List Unit Price gives what negotiation reduced the rate by. It does not give everything an agreement was worth, because the effect of applying a commitment to a charge is recognized in Effective Cost on the Cost and Usage side. The Cost Comparison supported feature already states the split: List against Contracted quantifies negotiated discount savings, and Contracted against Effective isolates commitment discount savings.

The boundary case is a negotiation whose discount exists only because a commitment was purchased, such as a rate that applies only when a specific reservation is held. Read strictly, the negotiated portion belongs to the purchase record for that reservation, and the application of it belongs to Effective Cost on the usage records, which places the two halves of one negotiation in different columns of different datasets. Whether that is the right answer is open under #1835 and #2492, with #2602 collecting the scenario as sample data rather than as argument.

### There is No Signal for Dynamic Pricing

A rate that varies with market conditions, such as spot capacity, has no representation distinct from a fixed rate, and no query can separate the two. Options are under analysis in #2565.

### Price History is Not Guaranteed

The dataset represents prices as of the date it is captured. A service provider is not required to publish superseded prices, and the dataset carries no signal saying whether it did, so two conformant instances can return a different number of rows for the same SKU Price ID at the same point in time. Retaining successive instances and comparing them on SKU Price Created and SKU Price Last Updated is how a practitioner reconstructs a history the provider does not publish.

This one is deliberate rather than deferred. Requiring full price history would raise the cost of a first conformant delivery considerably, for a capability most practitioners can reproduce by retaining what they already receive.

## Why the Price List Came First

The fair question to ask of a new pricing dataset is why its first version does not answer what practitioners ask most often, which is what a given resource will actually cost them.

A coverage-aware rate is a composition of two things that have to exist separately before they can be combined: a rate, and a statement of which commitment applies to it. FOCUS can now express the first in a provider-neutral shape. Expressing the second means naming the commitment instruments a provider offers in a schema, with enough fidelity that a query can tell a one year standard reservation from a three year convertible one, and then relating those instruments back to the rates they modify. That is a larger piece of work than adding a column, and building it against an agreed rate structure costs less than building both at once.

The same reasoning explains what did make the initial specification. Quantity tiers, purchase terms, and price eligibility are all present because each changes which rate applies without reference to what was consumed. Coverage is the first thing that depends on consumption, which is why it sits on the other side of the line.

## The Companion SKU Properties Dataset

A SKU Price record prices a SKU. It does not describe one. The only descriptors it carries are SKU ID and SKU Price Description, a free-text string whose contents vary by provider.

That is the difference between a price list a practitioner can look something up in and a price list they can browse. Anyone holding a SKU Price ID can retrieve its rate. Anyone wanting to compare machine families, filter to a size, or price the same workload under a different operating system has nothing structured to filter on, because the dataset carries the price of a thing and not the properties of that thing.

Those properties do exist in FOCUS today, in SKU Price Details on the Cost and Usage dataset, as key-value pairs keyed to SKU Price ID that carry functional and technical specifications. The placement has two consequences. Reaching a property means parsing a key-value structure rather than filtering a column, and, more consequentially, the properties are available only for SKUs an organization has already consumed. For a dataset whose purpose is pricing what has not been bought yet, that is the wrong way round.

A companion SKU Properties dataset, joined on SKU ID, is the natural resolution, with a SKU-level categorization hierarchy alongside it so that comparison across providers rests on shared categories rather than on matching provider-specific strings. Properties are open under #1045 and categorization under #963.

The sequencing follows the same reasoning as the rest of this dataset. Prices attach to SKUs, so a stable SKU identifier and an agreed price structure had to settle before properties could hang off them. A companion dataset adds to what exists here rather than revising it, which is what makes the price list a reasonable thing to have shipped first.

## Open Threads

| Issue | Question |
| :--- | :--- |
| #2492 | Revisiting the List and Contracted cost and unit price specifications, including which discounts Contracted Unit Price excludes (earlier framing in #1835) |
| #2602 | Sample data for a negotiated discount conditioned on a commitment discount |
| #1045 | A companion SKU Properties dataset |
| #963 | SKU categorization and hierarchy |
| #2565 | How to signal dynamic pricing |
| #2590 | Custom column guidance, including rate card routing |
| #2588 | Null value semantics for the effective date columns |
| #2566 | What publishing this dataset obligates a data generator to deliver |
| #2428 | Appendix sample data |
| #2520 | Aligning Cost and Usage charge frequency requirements with this dataset |
| #1625 | Tier handling in the List Unit Price and List Cost requirements |
| #1832 | List price defaulting where a provider publishes no discount-exclusive rate |
| #2478 | An implementation guide for how the pricing columns work together |

## What Sits Outside This Dataset

* **What was actually paid.** Comparing billed, contracted, effective, and list amounts is the Cost Comparison supported feature, against Cost and Usage.
* **Commitment inventory.** What an organization has committed to, and how much of it remains, is the Contract Commitment dataset.
* **Which action to take.** Turning a rate difference into a recommendation is the Recommendation dataset, tracked under #975.
