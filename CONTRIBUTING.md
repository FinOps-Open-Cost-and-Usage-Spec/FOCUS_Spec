# Contributing to the FOCUS Specification

This repository represents the written spec, not working code.  As such, most people will not need any development environment - most of the work around the spec happens in regularly scheduled discussions and issues here in Github.  If you wish to get involved please see the [FinOps Foundation website](https://focus.finops.org/) and consider [signing the CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA).

Please see the [contribution policy](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/contributing.md) for more information.

## FOCUS Specification Development Environment

The following is mostly needed by the FinOps Foundation staff members who maintain the FOCUS Repositories and associated document build pipelines. Currently, the only tested (supported) environment is a MacOS setup, however the build pipeline in GitHub uses Ubuntu so should be possible to run on a Linux environment.

### Setup Steps

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

### Assembling the specification locally

1. Move into the `specification` folder
2. Use make to generate the spec `make`
