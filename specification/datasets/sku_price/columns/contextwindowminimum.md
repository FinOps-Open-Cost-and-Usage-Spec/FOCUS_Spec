# Context Window Minimum

Context Window Minimum represents the exclusive lower boundary of a context-window pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in input [*tokens*](#glossary:token), including cached input *tokens* served from or placed into a [*prompt cache*](#glossary:prompt-cache), consumed from a single request.

When combined with [Context Window Maximum](#datamodel.skuprice.contextwindowmaximum), this column defines the range of input *tokens*, including cached input *tokens*, consumed from a single request for which a specific unit price applies. For a tier schedule that covers every positive input-token count, the lowest tier starts at zero. A threshold-only surcharge can have a lowest applicable band above zero. When the *SKU Price*'s price does not depend on context-window size, this value is null: the qualifier does not apply, and no additional SKU Price record is created to represent it.

## Requirements

ContextWindowMinimum MUST adhere to the following requirements:

* ContextWindowMinimum MUST be of type Decimal.
* ContextWindowMinimum MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContextWindowMinimum MUST represent a count of input *tokens*, including cached input *tokens*, consumed from a single request when ContextWindowMinimum is not null.
* ContextWindowMinimum MUST adhere to the following nullability requirements:
  * ContextWindowMinimum MUST be null when the price for the record does not depend on context-window size.
  * ContextWindowMinimum MUST NOT be null when the price for the record depends on context-window size.
* ContextWindowMinimum MUST be a non-negative decimal value when ContextWindowMinimum is not null.
* ContextWindowMinimum MUST be the exclusive lower bound of the context-window pricing tier when ContextWindowMinimum is not null.

## Column ID

ContextWindowMinimum

## Display Name

Context Window Minimum

## Description

The exclusive lower boundary of a context-window pricing tier, measured in input tokens, including cached input tokens, consumed from a single request.

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
