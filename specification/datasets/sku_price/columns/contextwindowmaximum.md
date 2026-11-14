# Context Window Maximum

Context Window Maximum represents the inclusive upper boundary of a context-window pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in input [*tokens*](#glossary:token), including cached input *tokens* served from or placed into a [*prompt cache*](#glossary:prompt-cache), consumed from a single request.

When combined with [Context Window Minimum](#datamodel.skuprice.contextwindowminimum), this column defines the range of input *tokens*, including cached input *tokens*, consumed from a single request for which a specific unit price applies. When a *SKU Price* represents a context-window pricing tier with no upper bound, this value is null and Context Window Minimum is non-null. When the *SKU Price*'s price does not depend on context-window size, both columns are null: the qualifier does not apply.

## Requirements

ContextWindowMaximum MUST adhere to the following requirements:

* ContextWindowMaximum MUST be of type Decimal.
* ContextWindowMaximum MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContextWindowMaximum MUST represent a count of input *tokens*, including cached input *tokens*, consumed from a single request when ContextWindowMaximum is not null.
* ContextWindowMaximum MUST adhere to the following nullability requirements:
  * ContextWindowMaximum MUST be null when the price for the record does not depend on context-window size.
  * ContextWindowMaximum MUST be null when ContextWindowMinimum is not null and there is no upper limit for the context-window pricing tier.
  * ContextWindowMaximum MUST NOT be null when ContextWindowMinimum is not null and the context-window pricing tier has an upper bound.
* When ContextWindowMaximum is not null, ContextWindowMaximum MUST adhere to the following requirements:
  * ContextWindowMaximum MUST be strictly greater than ContextWindowMinimum.
  * ContextWindowMaximum MUST be the inclusive upper bound of the context-window pricing tier.

## Implementation Guidance

Context-window qualifiers apply only when Context Window Minimum is non-null. For such a record, a request falls within a tier when the number of input *tokens*, including cached input *tokens*, consumed from that request is strictly greater than Context Window Minimum and, when Context Window Maximum is not null, less than or equal to Context Window Maximum. The count includes cached input *tokens*, whether served from or placed into a *prompt cache*. Cache activity does not change the unit used to measure the context-window bounds.

Both columns default to null. A data generator populates them only for records whose price depends on context-window size. When a tier schedule covers every positive input-token count, the lowest tier uses a Context Window Minimum of 0. A threshold-only surcharge can start above zero; its unqualified base price has null in both columns. Records whose price does not depend on context size have null in both columns, not a 0-to-null tier. For a context-window tier with no upper bound, Context Window Maximum is null. Its non-null Context Window Minimum distinguishes an unbounded tier from an inapplicable qualifier.

Adjacent tiers meet at a shared boundary value with no gap or overlap. Each tier is a distinct [SKU Price ID](#datamodel.skuprice.skupriceid), following the SKU Price dataset guidance for quantity tiers. Every record priced by the tier (input, output, cache read, and cache write) carries the same boundaries, and each keeps its own [Pricing Unit](#datamodel.skuprice.pricingunit). The bounds identify the tier; whether its price applies to all tokens or only those within the tier is a property of the published pricing terms, not of the bounds.

Data generators convert the service provider's boundary wording once, to exact Decimal values. Token counts are whole numbers in practice; for those counts, an inclusive starting threshold is represented by an exclusive lower bound one token below it. This conversion depends on the discrete token-count domain, not the Decimal storage type. For example, "over 200,000" becomes a tier boundary of 200000, while "200,000 tokens and above" becomes a boundary of 199999. An ambiguous provider threshold is not guessed; it is confirmed with the service provider before conversion.

The boundaries are evaluated against each request, not against [Consumed Quantity](#datamodel.costandusage.consumedquantity). A [Cost and Usage](#datamodel.costandusage) row aggregates *tokens* from many requests over a [*charge period*](#glossary:chargeperiod). When cache reads and writes are metered on their own rows, a *token* served from or placed into a *prompt cache* is counted only on its row with TokenCacheAction "Read" or "Write". When cached and uncached request *tokens* share a meter, TokenCacheAction is omitted under the shared-meter requirement of SKU Price Details. The tier of a request therefore cannot be recovered by summing Cost and Usage rows. The data generator assigns each request's *tokens* to the SKU Price IDs of the matching tier before aggregation.

## Column ID

ContextWindowMaximum

## Display Name

Context Window Maximum

## Description

The inclusive upper boundary of a context-window pricing tier, measured in input tokens, including cached input tokens, consumed from a single request.

## Content Constraints

| Constraint                 | Value                                                                                     |
| :------------------------- | :---------------------------------------------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                                                          |
| Operating Model Conditions | [Includes Context Window Pricing](#operatingmodelconditions.includescontextwindowpricing) |
| Column type                | Metric                                                                                    |
| Feature level              | Conditional                                                                               |
| Allows nulls               | True                                                                                      |
| Data type                  | Decimal                                                                                   |
| Value format               | [Numeric Format](#attributes.numericformat)                                               |
| Number range               | Any valid non-negative decimal value                                                      |

## Version Introduced

Preview: 1.6
