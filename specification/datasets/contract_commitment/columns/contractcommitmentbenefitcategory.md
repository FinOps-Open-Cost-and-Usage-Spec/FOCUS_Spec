# Contract Commitment Benefit Category

Contract Commitment Benefit Category defines the primary value or advantage received for a [*contract commitment*](#glossary:contract-commitment). It identifies whether the benefit is realized as a price reduction, a monetary offset, a guarantee of service availability, or some other entitlement.

## Implementation Context

### Distinguishing from Technical IDs

**Availability** represents the contractual right to access resources. It must not be confused with technical fields like `CapacityReservationId`. A single **Availability** within a contract may encompass multiple technical reservations across various regions or accounts.

### Primary Benefit Logic

In cases where a commitment provides multiple benefits (e.g., a Discount and an Availability), the value should reflect the **primary commercial driver** of the agreement as defined by the procurement or FinOps team.

## Requirements

ContractCommitmentBenefitCategory adheres to the following requirements:

* ContractCommitmentBenefitCategory MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentBenefitCategory MUST be of type String.
* ContractCommitmentBenefitCategory MUST NOT be null.
* ContractCommitmentBenefitCategory MUST be one of the allowed values.

## Column ID

ContractCommitmentBenefitCategory

## Display Name

Contract Commitment Benefit Category

## Description

Defines the primary value or advantage received for a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value         | Sort Order | Description                                                               | Typical Use Case                                                 |
| ------------- | ---------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Discount      | 10         | Direct reduction in the unit price or list rate applied from the start.   | Flat rate negotiated reductions or Savings Plans.                |
| Monetary Pool | 20         | A shared reservoir of value or credits used to offset costs.              | Credit drawdown agreements or prepaid balances.                  |
| Availability  | 30         | A contractual assurance of resource access and physical capacity.         | Capacity reservations or dedicated host guarantees.              |
| Other         | 40         | Benefits not captured by standard categories.                             | Support access, training, or professional services.              |

## Introduced (version)

1.4
