# Capacity Reservation Total

Capacity Reservation Total is the numeric value representing the amount of capacity (in number of unnormalized *consumed unit*) that were reserved over the specified charge period by the [*capacity reservation*](#glossary:capacity-reservation) identified in the charge. 

The CapacityReservationTotal column MUST be present in the billing data when the provider supports *capacity-reservations*. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the ConsumedUnit. This column MUST NOT be null when CapacityReservationStatus is not null. 

## Column ID

CapacityReservationTotal

## Display Name

Capacity Reservation Total

## Description

The total amount of capacity specified in unnormalized consumed units that was reserved over the specified charge period for the capacity reservation listed in the charge.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Metric         |
| Feature level   | Conditional    |
| Allows nulls    | True           |
| Data type       | Decimal        |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.1