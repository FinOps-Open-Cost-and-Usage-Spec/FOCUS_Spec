# Column: ActualQuantity

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                | Column               |
|----------|-------------------------|----------------------|
| AWS      | CUR                     | lineItem/UsageAmount + reservation/TotalReservedUnits |
| Azure    | Cost Details            | quantity |
| GCP      | BigQuery Billing Export | usage.amount |


Existing quanity measurements in billing data will likely need to be transformed to represent a single unit, e.g. per 1000 Requests should be transformed to number of individual requests. 

Depending on the pricing strategy used on a charge the values of PricingQuantity and ActualQuantity maybe the same or different.

## Simple Per-Unit Pricing

Simple Per-Unit Pricing is when you are charged per 1 unit and the purchase and usage lines in the FOCUS dataset are provided per individual unit.

For Simple Per-Unit Pricing both PricingQuantity and ActualQuantity will match.

Exmaples:
    * 5 API requests, charged per unit
        | PricingQuantity | 5 |
        | PricingUnit     | Request |
        | ActualQuantity  | 5 |
        | ActualUnit      | Request |

## Fractional Block Pricing

Fractional Block Pricing is when a service/resource is charged in blocks, however you are able to purchase/use less than the full block. 

For Fractional Block Pricing PricingQuantity is likely to be a fractional amount of a block, ActualQuantity will represent the number of individual units.

Examples:
    * Licenses that come in blocks on 10, but you are able to purchase 5 licenses and pay for half of the block
        | PricingQuantity | 0.5 |
        | PricingUnit     | 10 Licenses |
        | ActualQuantity  | 5 |
        | ActualUnit      | License |
    * A resource is charged per hour, but you can use it for less than a whole hour and you pay for the number of minutes/seconds
        | PricingQuantity | 0.75 |
        | PricingUnit     | Hour |
        | ActualQuantity  | 45 |
        | ActualUnit      | Minutes |


## Stair Step Pricing

Stair Step Pricing occurs when you are charged for a minimum amount no matter the actual amount you purchase/use. As you use more the cost steps up as you cross into the next minimum block. For some this occurs in the initial useage, (e.g. virtual machines with a minimum of 1 minute of usage, after which you pay per second)

For Stair Step Pricing it is expected the ActualQuantity and PricingQuantity differs.

Examples
    * Licenses are sold in blocks of 10, usage is applied per license consumed
        | PricingQuantity | 1 |
        | PricingUnit     | 10 Licenses |
        | ActualQuantity  | 1 |
        | ActualUnit      | License |

## Different Units

Sometimes resources/services are priced using a different unit than the volume of SKU they represent. 

For Different Units it is expected the ActualQuantity and PricingQuantity differs.

Examples
    * Tokens are purchased and can be used against minutes of service usage
        | PricingQuantity | 15 |
        | PricingUnit     | Tokens |
        | ActualQuantity  | 50 |
        | ActualUnit      | Minutes |
    