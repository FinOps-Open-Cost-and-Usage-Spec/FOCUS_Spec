# Tags

The Tags column represents the set of finalized user-defined and/or provider-defined tags assigned to Tag Sources.  Tags are commonly used for scenarios like adding business context to billing data to identify and accurately allocate charges.

A tag is 'finalized' after a single tag value is chosen from a set of corresponding tag values for a single tag key.  Whether a tag key can have multiple, possible values is determined by the Provider.

The Tags column adheres to the following requirements:

* The Tags column MUST contain user-defined and/or provider-defined tags.
* The Tags column MUST only contain finalized tags.
* The Tags column MUST be in Key-Value Format.
* A Tag without a specified value MUST have its value set to null.
* Providers MUST NOT alter user-defined Tag keys or values.

Provider-defined Tags additionally adhere to the following requirements:

* Provider-defined tags MUST be prefixed with a provider-specified tag key prefix.
* Providers SHOULD publish all provider-specified tag key prefixes within their respective documentation.

## Provider-Defined vs. User-Defined Tags

The following is an example of one user-defined tag and one provider-defined tag, respectively, with tag key, `foo`.  The first tag, which is user-defined, is not prefixed. The second tag is prefixed with marketplace/ which the provider has specified as a reserved tag key prefix.

```json
    {
        "foo":"bar",
        "marketplace/foo": "bar"
    }
```

## Finalized Tags

A tag can either be static or dynamic. If a tag is static, its value is immutable. If a tag is dynamic, its value is determined by a set of predefined user or provider rules. A finalized tag is the final result of any static or dynamic Tag.

As a example, let's assume 1 sub account exists with 1 virtual machine with the following details:

* Sub account
  * id: *my-account*
  * user-defined tags: *team:ops*, *env:prod*
* Virtual machine
  * id: *my-vm*
  * user-defined tags: *team:web*

The table below represents a finalized cost and usage dataset with these resources.  It also shows the finalized state after all resource-oriented, tag inheritance rules are processed.

| ResourceType    | ResourceId | Tags                                        |
| :---------------| :----------| :-------------------------------------------|
| Account         | my-account | { "team": "ops", "env": "prod" }            |
| Virtual Machine | my-vm      | { "team": "web", *"env": "prod"* }          |

Because the the Virtual Machine Resource did not have an `env` tag, it inherited tag, `env:prod` (italicized), from its parent Account.  Conversely, because the Virtual Machine Resource already has a `team` tag (`team:web`), it did not inherit `team:ops` from its parent Account.

## Column ID

Tags

## Display Name

Tags

## Description

The set of finalized tags assigned to Tag Sources.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | JSON Object      |
| Allows nulls    | True             |
| Value format    | Key-Value Format |

## Introduced (version)

1.0
