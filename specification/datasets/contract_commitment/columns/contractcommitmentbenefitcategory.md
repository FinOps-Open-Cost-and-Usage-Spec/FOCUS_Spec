# Contract Commitment Benefit Category

Contract Commitment Benefit Category defines the primary value or advantage received for a [*contract commitment*](#glossary:contract-commitment). It identifies whether the benefit is realized as a price reduction, a feature entitlement, a guarantee of service availability, or some other commercial outcome.

## Implementation Context

### Distinguishing Outcomes from Mechanisms

When categorizing a commitment, the value reflects the actual commercial benefit received, rather than the funding or consumption mechanism used to acquire it. For example, a prepaid "monetary pool" or a drawdown fund is a mechanism; the *benefit* of that pool is typically the right to use the feature (**Entitlement**) or the reduced rate unlocked by the commitment (**Discount**).

### Distinguishing from Technical IDs

**Availability** represents the contractual right to access resources. It must not be confused with technical fields like `CapacityReservationId`. A single **Availability** within a contract may encompass multiple technical reservations across various regions or accounts.

### Primary Benefit Logic

In cases where a commitment provides multiple benefits (e.g., an Entitlement that also includes a Discount), the value should reflect the **primary commercial driver** of the agreement as defined by the procurement or FinOps team.

## Requirements

ContractCommitmentBenefitCategory MUST adhere to the following requirements:

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
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value | Sort Order | Description | Typical Use Case |
| :--- | :--- | :--- | :--- |
| Discount | 10 | A financial reduction in the unit price or list rate, whether applied immediately or conditionally upon meeting usage or spend thresholds. | Flat rate negotiated reductions, Savings Plans, growth rebates, or volume-tier discounts. |
| Entitlement | 20 | The contractual right to access and consume specific products, features, or software tiers that would otherwise be unavailable. | Marketplace SaaS purchases, Enterprise Agreements (e.g., Snowflake), or paid Proof of Concepts. |
| Availability | 30 | A contractual assurance of resource access and physical capacity. | Capacity reservations or dedicated host guarantees. |
| Other | 40 | Benefits not captured by standard categories. | Support access, training, or professional services. |

## Version Introduced

1.4
