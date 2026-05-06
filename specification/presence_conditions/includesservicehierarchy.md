# Includes Service Hierarchy

The Includes Service Hierarchy presence condition represents a verifiable state where the [source operating model](#glossary:source-operating-model) includes more than one level of service categorization.

## Requirements

IncludesServiceHierarchy MUST adhere to the following requirements:

* IncludesServiceHierarchy MUST evaluate to true when the source operating model supports a hierarchy of service categories (e.g., Service, Sub-service).
* IncludesServiceHierarchy MUST evaluate to false when the source operating model uses only a single flat level of service categorization.

## Presence Condition ID

IncludesServiceHierarchy

## Display Name

Includes Service Hierarchy

## Description

A verifiable state indicating whether the source operating model includes more than one level of service categorization.

## Version Introduced

1.5
