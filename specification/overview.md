# FOCUS Specification

|  <span style="color:Orange">&#x26A0; Draft</span> |
|:--------------------------|

## Introduction and Overview

FOCUS is a community specification that works to establish an open standard for cloud billing data. It specifies vendor neutral cross-cloud measures for key cost & usage dimensions/metrics. These measures and their derivations establish a baseline schema that enables cloud billing data to be surfaced in a common FinOps-serviceable format.

## Background and History

This project is sponsored and maintained by the [FinOps Foundation][FODO]. Starting as a working group under the FinOps Foundation as the open billing working group. The decision was made in Jan 2023 to begin to migrate the work to a newly formed project under the Linux Foundation called the FinOps Open Cost and Usage Specification (FOCUS project) to better support the creation of a specification.

## Intended Audience

This specification is designed to be used by three major groups:

* Billing File Generators: cloud platforms that generate costs, such as:
  * Cloud Service Providers
  * SaaS Platforms
* FinOps Vendors: companies that provide commercial tools to assist with FinOps
* FinOps Practitioners: companies doing FinOps

## Scope

The Open Cloud Bill working group will develop a common, source-neutral schema of billing, cost, usage, and observability data mapped to a variety of cloud service provider and SaaS product sources, with metadata, dimensions, metrics, and measures for the source and common schema fields.

## Design notes

|  <span style="color:Orange">&#x26A0; Draft</span> |
|:--------------------------|

Explain the difficulty in forming a spec that matches every use. Core considerations kept in mind.

### Perfection is the enemy of done

Winston Churchill once said that “perfection is the enemy of progress”. Knowing the challenges of creating an open billing specification which will suit every situation, it is important that the FOCUS project keeps perfection versus progress philosophy in mind. When faced with different options that have differing pros and cons the item that will improve the specification for the common need should win.

### Extensibility

The core specification should be applicable to most cloud service providers, with particular focus on the major cloud providers. This specification should however aim to be extensible to add optional extensions of this core specification to suit different types of cloud SaaS products and the larger list of cloud service providers.

## Typographic conventions

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in [BCP
14](https://tools.ietf.org/html/bcp14)
[[RFC2119](https://tools.ietf.org/html/rfc2119)]
[[RFC8174](https://tools.ietf.org/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.

An implementation of this specification is not compliant if it fails to
satisfy one or more of the "MUST", "MUST NOT", "REQUIRED", "SHALL", or "SHALL
NOT" requirements defined in this specification. Conversely, an
implementation of this specification is compliant if it satisfies all the
"MUST", "MUST NOT", "REQUIRED", "SHALL", and "SHALL NOT" requirements defined in
this specification.

### Notes and Important

Important information should be highlighted using either of the following conventions.

For general notes and highlights:

| <span style="color:DodgerBlue">&#x261D; Note</span> |
|:--------------------------|
| This is a note            |

### Examples

In order to make the specification easy to understand the use of examples to demonstrate are encouraged. Ideally, the examples are agnostic to a provider, but if it makes the example easier to understand a provider specific example maybe provided.

| <span style="color:DarkSlateGray">&#x2692; Example</span> |
|:--------------------|
| This is an example  |

This is a code example

```text
 def my_example(arg):
    pass
```

### Warnings

Used sparingly throughout the specification to warn the reader. This can be useful to clarify a requirement. E.g. X is (or not) related to Y

| <span style="color:Red">&#x26A1; Warning</span>      |
|:-------------------|
| This is a warning  |

### Draft

Used only within working draft copies of the FOCUS specification. Sections that should be considered under active development should be marked as draft. All draft sections need to be resolved before the specification can be considered a candidate for publication.

|  <span style="color:Orange">&#x26A0; Draft</span> |
|:--------------------------|

## Conformance checkers and Validators

There are no current resources available to test for specification conformance or validators to run on sample data. This is one item under consideration to produce a FOCUS Group to create an official test suite, when this happens this section of the specification will be updated with details.

[FODO]: https://www.finops.org
