# Introduction

*This section is non-normative.*

FOCUS aims to establish a community-driven specification for consumption-based billing data. Due to the lack of a broadly adopted specification, infrastructure and services providers have resorted to proprietary billing schemas and terminologies that they feel best serve their customers needs. However, the lack of conformance amongst the billing data generators has forced FinOps practitioners to employ disparate, best-effort schemes for each provider a in order to perform essential FinOps capabilities such as chargeback, cost allocation, budgeting and forecasting etc.

The FOCUS specification's schema definition and FinOps aligned terminology provide a clear guideline for producing FinOps-serviceable billing datasets. Datasets conforming to FOCUS enable FinOps practitioners to perform common FinOps capabilities, like the ones mentioned above, using a generic set of instructions, regardless of the origin of the dataset.

## Background and History

This project is sponsored and maintained by the [FinOps Foundation][FODO]. This work initially started under the Open Billing working group under the FinOps Foundation. The decision was made in Jan 2023 to begin to migrate the work to a newly formed project under the Linux Foundation called the FinOps Open Cost and Usage Specification (FOCUS) to better support the creation of a specification.

## Intended Audience

This specification is designed to be used by three major groups:

* Billing data generators: Infrastructure and services providers that generate costs data, such as (but not limited to):
  * Cloud Service Providers (CSPs)
  * Software as a Service (SaaS) platforms
  * Internal infrastructure and service platforms
* FinOps tool providers: Organizations that provide tools to assist with FinOps
* FinOps practitioners: Organizations and individuals consuming billing data for doing FinOps

## Scope

he FOCUS working group will develop an open-source specification for billing data. The schema will define data dimensions, metrics, as well as a set of attributes about billing data.

## Design notes

Schema, terminology and data attributes defined in the specification were selected in order to enable a set of essential FinOps capabilities which are documented within the specification.

### Provider neutral approach by default

While the schema, naming, terminology and attributes of many providers were reviewed during development, this specification aims to be provider neutral. In some cases, the approach or naming may closely resemble a vendors implementation while in other cases, the naming or approach might be new. In all cases, the approach is selected by the FOCUS group - which is a broad community of FinOps practitioners, Cloud and SaaS providers and FinOps vendors.

### Working backwards

The FOCUS group working on the specification aims to work backwards from essential FinOps capabilities that practitioners need to perform to prioritize the dimensions, metrics and the attributes of the billing data that should be defined in the specification. The enabled capabilities will be documented within the FOCUS specification.

### Extensibility

The initial specification aims to help solve cost reporting and chargeback use cases for cloud service provider datasets. The specification should however aim to be extensible to SaaS products and other types of cost data in order to solve the full set of FinOps capabilities.

## Typographic conventions

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)] when, and only when, they appear in all capitals, as shown here.

An implementation of this specification is not compliant if it fails to satisfy one or more of the "MUST", "MUST NOT", "REQUIRED", "SHALL", or "SHALL NOT" requirements defined in the specification. Conversely, an implementation of the specification is compliant if it satisfies all the "MUST", "MUST NOT", "REQUIRED", "SHALL", and "SHALL NOT" requirements defined in
the specification.

## Conformance checkers and Validators

There are no current resources available to test for specification conformance or validators to run on sample data. When one becomes available, this section of the specification will be updated with details.

[FODO]: https://www.finops.org
