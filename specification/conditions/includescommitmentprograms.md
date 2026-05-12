# Includes Commitment Programs

The Includes Commitment Programs presence condition represents a verifiable state where the source operating model includes at least one [*commitment program*](#glossary:commitment-program).

## Requirements

IncludesCommitmentPrograms MUST adhere to the following requirements:

* IncludesCommitmentPrograms MUST evaluate to true when the source operating model includes one or more programs where a customer commits to a level of usage or spend in exchange for reduced rates.
* IncludesCommitmentPrograms MUST evaluate to false when the source operating model does not include any commitment-based pricing or discount programs.

## Presence Condition ID

IncludesCommitmentPrograms

## Display Name

Includes Commitment Programs

## Description

A verifiable state indicating whether the source operating model includes at least one commitment program.

## Version Introduced

1.5
