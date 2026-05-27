# Includes Commitment Programs

The Includes Commitment Programs condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes at least one [*commitment program*](#glossary:commitment-program).

## Requirements

IncludesCommitmentPrograms MUST adhere to the following requirements:

* IncludesCommitmentPrograms MUST evaluate to true when the *operating model* includes one or more programs where a customer commits to a level of usage or spend in exchange for reduced rates.
* IncludesCommitmentPrograms MUST evaluate to false when the *operating model* does not include any commitment-based pricing or discount programs.

## Condition ID

IncludesCommitmentPrograms

## Display Name

Includes Commitment Programs

## Description

A verifiable state indicating whether the *operating model* includes at least one commitment program.

## Version Introduced

1.5
