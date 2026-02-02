# Contract Commitment Benefit Category

Contract Commitment Benefit Category defines the primary value or advantage received for a [*contract commitment*](#glossary:contract-commitment). It identifies whether the benefit is realized as a price reduction, a monetary offset, a guarantee of service availability, or some other entitlement.

## Implementation Context

### Distinguishing from Technical IDs
**Availability Guarantee** represents the contractual right to access resources. It must not be confused with technical fields like `CapacityReservationId`. A single **Availability Guarantee** within a contract may encompass multiple technical reservations across various regions or accounts.

### Primary Benefit Logic
In cases where a commitment provides multiple benefits (e.g., a Discount and an Availability Guarantee), the value should reflect the **primary commercial driver** of the agreement as defined by the procurement or FinOps team.

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

| Value | Sort Order | Description | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Discount** | 10 | Direct reduction in the unit price or list rate of applicable resources. | Savings Plans, RIs, or flat percentage negotiated discounts. |
| **Credit** | 20 | A monetary amount or pool applied to offset total invoice costs. | Migration credits, rebates, or "buy-back" funds. |
| **Availability Guarantee** | 30 | A contractual assurance of resource access and capacity for the term. | Dedicated host guarantees or regional capacity commitments. |
| **Tiered Incentive** | 40 | Benefits that scale or activate based on consumption thresholds. | Volume-based pricing tiers or "growth" discounts. |
| **Other** | 50 | Benefits not captured by standard categories. | Support plan access, training, or professional services. |

## Introduced (version)

1.4
