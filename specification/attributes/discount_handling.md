# Amortization Handling

Amortization is a process used to break down and spread purchase costs over the period of time or term of use. 

Amortization is primarily used in purchasable commitment-based discounts. When a purchase is applicable to resources, like commitment-based discounts, the amortized cost of a resource takes the initial payment and term into account and distributes it out based on the resource's usage, attributing the prorated cost for each hour of billing. Amortization provides a method for FinOps practitioners to reallocate purchase charges to the appropriate audience in support of their cost allocation efforts. 

## Attribute ID

AmortizationHandling

## Attribute name

Amortization Handling

## Description

Rules and requirements defining how amortization is shown in the billing data.

## Requirements

* Every charge MUST include all applicable discounts. (e.g., negotiated and commitment-based discounts)
* Discounts SHOULD be applied directly to the charges they are discounting.
* All purchases SHOULD be amortized.
* MUST NOT add extra rows to subtract the costs due to an applied discount.
* When multiple discounts apply to a single row, but are not applicable to the entire charge, those charges SHOULD be split into separate rows.
* Any unused discount’s usage and cost MUST be reflected in the cost data in order to identify the loss of benefit. 

## Exceptions

None

## Introduced (version)

1.0
