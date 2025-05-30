# FinOps Open Cost and Usage Specification (FOCUS) - Working Group

## Overview

The FinOps Open Cost and Usage Specification (FOCUS) is a community-driven effort to develop a standard schema for cloud, SaaS, and other billing data. The primary goal of the FOCUS specification is to make it easier to understand, report on, and manage cloud costs. The FOCUS specification is intended to be adaptable across a variety of cloud service provider and SaaS product sources and defines columns (dimensions and metrics), column-specific requirements, and attributes (spec-wide requirements).  This repo also provides supporting content that includes example mappings between well-known provider datasets and what's defined in the FOCUS specification.

The vision of the FOCUS project is to help the cloud and SaaS industry move toward a common vocabulary around usage and billing data.  This will not only help FinOps professionals in the analysis of billing data from disparate sources but will also help software engineering teams by providing a target format for the usage and billing data that their products will generate.

Some of the use cases this capability can enable:

- The FOCUS spec will make it easier for FinOps practitioners to approach a new billing data source, as common concepts have been mapped to the common vocabulary of the spec.
- The FOCUS spec will make it easier to merge multiple billing data sources together, and perform cross-cloud and cross-vendor analysis and cost reporting.
- The FOCUS spec should make it easier to open source more FinOps visibility tools, and to accelerate the FinOps framework capability of data ingestion and normalization.

## Notation Conventions and Compliance

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in the
[specification][] are to be interpreted as described in [BCP
14](https://tools.ietf.org/html/bcp14)
[[RFC2119](https://tools.ietf.org/html/rfc2119)]
[[RFC8174](https://tools.ietf.org/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.

An implementation of the specification is not compliant if it fails to
satisfy one or more of the "MUST", "MUST NOT", "REQUIRED", "SHALL", or "SHALL
NOT" requirements defined in the specification. Conversely, an
implementation of the specification is compliant if it satisfies all the
"MUST", "MUST NOT", "REQUIRED", "SHALL", and "SHALL NOT" requirements defined in
the specification.

## Versioning the Specification

Changes to the [specification](./specification/overview.md) are described in [CHANGELOG.md](CHANGELOG.md) and versioned based on [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html). However, versioning does not strictly follow SemVer in terms of implied compatibility via major, minor, and patch versions. Layout changes are not versioned. Specific implementations of the specification should specify which version they implement.

## Project Naming

- The official project name is "FinOps Open Cost and Usage Specification".
- The official acronym used by the FinOps Open Cost and Usage Specification project is "FOCUS".
- While the official acronym includes the word "Specification", it is still acceptable to refer to this working group's output as the "FOCUS Specification".

## About the project

See the [project repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation) for information about the following, and more:

- [Project Charter](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)
- [Operating Procedures](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md)
- [Steering Committee](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/steering_committee.md)
- [Release Planning](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/RELEASE-PLANNING.md)
- [Change / contribution process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/contributing.md)

