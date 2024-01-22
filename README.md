# FinOps Open Cost and Usage Specification (FOCUS) - Specification Working Group

The Open Cloud Bill working group will develop a common, source-neutral schema of
billing, cost, usage, and observability data mapped to a variety of cloud service provider and SaaS product
sources, with metadata, dimensions, metrics, and measures for the source and common schema fields. As per the [Working Group Charter]() **Link TBC**

## Notation Conventions and Compliance

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in the
[specification][] are to be interpreted as described in [BCP
14](https://tools.ietf.org/html/bcp14)
[[RFC2119](https://tools.ietf.org/html/rfc2119)]
[[RFC8174](https://tools.ietf.org/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.

An implementation of the [specification][] is not compliant if it fails to
satisfy one or more of the "MUST", "MUST NOT", "REQUIRED", "SHALL", or "SHALL
NOT" requirements defined in the [specification][]. Conversely, an
implementation of the [specification][] is compliant if it satisfies all the
"MUST", "MUST NOT", "REQUIRED", "SHALL", and "SHALL NOT" requirements defined in
the [specification][].

## Versioning the Specification

Changes to the [specification](./specification/overview.md) are versioned according to [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html) and described in [CHANGELOG.md](CHANGELOG.md). Layout changes are not versioned. Specific implementations of the specification should specify which version they implement.

## Project Naming

- The official project name is "FinOps Open Cost and Usage Specification"
- The official acronym used by the FinOps Open Cost and Usage Specification project is "FOCUS"
- While the official acronym includes the word "Specification", it is still acceptable to refer to this working groups output as the "FOCUS Specification"

## About the project

See the [project repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation) for information about the following, and more:

- [Change / contribution process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/contributing.md)

## FOCUS Specification Development Environment

Most people will not need any development environment, it is mostly needed by the FinOps Foundation staff members who maintain the FOCUS Repositories and associated document build pipelines.

### Setup Steps (MacOS)

1. Install homebrew (as per: https://brew.sh)
2. Setup cask

	`brew install cask`
3. Install python

	`brew install python`
4. Add packages for python

	`pip3 install -r requirements.txt`
5. Install pandoc and required filter library

	`brew install pandoc`

	`brew install --cask wkhtmltopdf`
6. If your machine does not have git/make etc, you might fun the following: Install developer command line tools for MacOS

	`xcode-select --install`

### Setup Steps (Fedora Linux)

1. Clone the repository and enter the project folder
2. Install pandoc, wkhtmltopdf, and make

	`sudo dnf install pandoc wkhtmltopdf make`
3. Create a python virtual environment and switch to it

	`python -m venv focus`

	`source focus/bin/activate`
4. Add packages for python

	`pip3 install -r requirements.txt`

### Assembling the specification locally

1. Move into the `specification` folder
2. Use make to generate the spec `make`
