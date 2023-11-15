# Introduction

*This section is non-normative.*

FOCUS aims to establish a community-driven specification for consumption-based billing data. Due to the lack of a broadly adopted specification, infrastructure and services [*providers*](#glossary:provider) have resorted to proprietary billing schemas and terminology. However, the lack of conformance amongst the billing data generators has forced FinOps practitioners to employ disparate, best-effort schemes which each practitioner must develop individually for each *provider* in order to perform essential FinOps capabilities such as chargeback, cost allocation, budgeting and forecasting.

The FOCUS specification's schema definition and FinOps aligned terminology provide a clear guide for producing FinOps-serviceable billing datasets. Datasets conforming to FOCUS enable FinOps practitioners to perform common FinOps capabilities, like the ones mentioned above, using a generic set of instructions, regardless of the origin of the dataset.

## Background and History

This project is sponsored by the [FinOps Foundation][FODO]. This work initially started under the Open Billing working group under the FinOps Foundation. The decision was made in Jan 2023 to begin to migrate the work to a newly formed project under the Linux Foundation called the FinOps Open Cost and Usage Specification (FOCUS) to better support the creation of a specification.

## Intended Audience

This specification is designed to be used by three major groups:

* Billing data generators: Infrastructure and services *providers* that bill based on consumption, such as (but not limited to):
  * [Cloud Service Providers (CSPs)](#glossary:cloud-service-provider)
  * Software as a Service (SaaS) platforms
  * [Managed Service Providers (MSPs)](#glossary:managed-service-provider)
  * Internal infrastructure and service platforms
* FinOps tool *providers*: Organizations that provide tools to assist with FinOps
* FinOps practitioners: Organizations and individuals consuming billing data for doing FinOps

## Scope

The FOCUS working group will develop an open-source specification for billing data. The schema will define data [*dimensions*](#glossary:dimension), [*metrics*](#glossary:metric), a set of attributes about billing data, and a common lexicon for describing billing data.

## Design Notes

The following principles were considered while building the specification.

### Provider-Neutral Approach by Default

While the schema, naming, terminology and attributes of many *providers* were reviewed during development, this specification aims to be provider-neutral. In some cases, the approach may closely resemble one or more *provider's* implementation, while in other cases, the approach might be new. In all cases, the FOCUS group (community composed of FinOps practitioners, Cloud and SaaS *providers* and FinOps vendors) will attempt to prioritize alignment with the FinOps [Framework][FODOF] and [Capabilities][FODOFC].

### Working Backwards

The FOCUS group working on the specification aims to work backwards from essential FinOps capabilities that practitioners need to perform to prioritize the *dimensions*, *metrics* and the attributes of the billing data that should be defined in the specification to fulfill that capability. Some of the enabled capabilities will be documented in the [Appendix: FinOps Capabilities Enabled by FOCUS (TODO)](#finopscapabilitiesenabledbyfocus).

### Extensibility

The initial specification aims to introduce a common schema and terminology for billing datasets produced by *Cloud Service Providers (CSPs)*. The specification however aims to be extensible to SaaS products and other types of cost datasets. Future versions of the specification will look to expand the content to support a broader set of prioritized FinOps capabilities.

## Typographic Conventions

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)] when, and only when, they appear in all capitals, as shown here.

An implementation of this specification is not compliant if it fails to satisfy one or more of the "MUST", "MUST NOT", "REQUIRED", "SHALL", or "SHALL NOT" requirements defined in the specification. Conversely, an implementation of the specification is compliant if it satisfies all the "MUST", "MUST NOT", "REQUIRED", "SHALL", and "SHALL NOT" requirements defined in
the specification.

## Conformance Checkers and Validators

There are no current resources available to test for specification conformance or validators to run on sample data. When one becomes available, this section of the specification will be updated with details.

[FODO]: https://www.finops.org
[FODOF]: https://www.finops.org/framework/
[FODOFC]: https://www.finops.org/framework/capabilities/
