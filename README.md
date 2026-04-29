# FinOps Open Cost and Usage Specification (FOCUS) - Working Group

## Overview

The FinOps Open Cost and Usage Specification (FOCUS) is a community-driven, open specification that defines a common schema for technology cost and usage data across cloud, SaaS, data center, and other technology categories.

FOCUS establishes a consistent, vendor-neutral vocabulary for billing and usage data. It defines a set of columns (dimensions and metrics), column-level requirements, and specification-wide attributes that enable interoperable, comparable, and analysis-ready datasets across providers and technology categories.

The project is actively maintained and adopted by a growing ecosystem of cloud providers, SaaS vendors, enterprises, and FinOps tooling platforms. This repository contains the specification releases, source, build and validation tooling, and supporting contributor guidance that help practitioners, platforms, and providers produce and consume data that is consistent, portable, and aligned to FinOps practices.

For a deeper overview of FOCUS, its capabilities, and adoption, see the [FOCUS website](https://focus.finops.org).

## Accessing the Specification

Use the following links to access the latest specification artifacts:

* [Latest Public Release](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases/latest): Stable release for general implementation and reference.
* [Latest Working Draft](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases/tag/latest-draft): In-progress draft reflecting current working-group development.


## Contributor Getting Started

Start here:

* [CONTRIBUTING.md](CONTRIBUTING.md)
* [guidelines/contributors/development-processes.md](guidelines/contributors/development-processes.md)

For topic-specific standards, see:

* [guidelines/contributors/editorial-guidelines.md](guidelines/contributors/editorial-guidelines.md)
* [guidelines/contributors/normative-requirements-guidelines.md](guidelines/contributors/normative-requirements-guidelines.md)
* [guidelines/contributors/spec-change-guidelines.md](guidelines/contributors/spec-change-guidelines.md)
* Additional project guidance: [guidelines/](guidelines/)

---

## Normative Language and Conformance

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in the specification are to be interpreted as described in BCP 14 (RFC2119 and RFC8174), when and only when they appear in all capitals.

FOCUS restricts normative language to this subset as defined in the project’s  
[Normative Requirements Guidelines](guidelines/contributors/normative-requirements-guidelines.md).

An implementation is considered **conformant** if it satisfies all **MUST** and **MUST NOT** requirements defined in the specification. Failure to meet any of these requirements results in non-conformance.

---

## Versioning the Specification

Changes to the specification are documented in [CHANGELOG.md](CHANGELOG.md).

FOCUS uses a versioning approach inspired by [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html), but versions should not be interpreted as strict compatibility guarantees. New versions primarily introduce additive capabilities, clarifications, and expanded coverage while avoiding breaking changes.

Implementations should explicitly declare the version of FOCUS they align to.

For release process details and version planning context, see [RELEASE-PLANNING.md](RELEASE-PLANNING.md).

---

## About the Project

FOCUS is developed under an open governance model with participation from providers, vendors, and practitioners across the ecosystem.

For additional details, see the project repository:

* [Project Charter](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)
* [Operating Procedures](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md)
* [Steering Committee](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/steering_committee.md)
* [Release Planning](RELEASE-PLANNING.md)
* [Contribution Process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/contributing.md)

---

## Project Naming

* The official project name is **FinOps Open Cost and Usage Specification**
* The official acronym is **FOCUS**
* The term **FOCUS Specification** is the accepted shorthand for the project's output