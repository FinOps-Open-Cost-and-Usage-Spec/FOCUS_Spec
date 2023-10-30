# Tags

The Tags column represents the set of finalized user-defined and/or provider-defined tags assigned to Tag Sources.  Tags commonly add business context to billing data to identify and accurately allocate charges.

If a Tag is subject to a set of prioritized rules for determining its value, it is finalized after a single value is chosen from a set of corresponding values.  Otherwise, a Tag and a finalized Tag are equal.

Tags adhere to the following requirements:

* Tags MUST only contain finalized tags.
* Tags MUST standardize to Key-Value Format.
* A Tag without a specified value MUST have its value set to null.
* Providers MUST NOT alter User-Defined Tag keys.

Provider-defined Tags additionally adhere to the following requirements:

* Provider-defined Tags MUST be prefixed with a provider-defined prefix.
* Providers SHOULD publish all provider-defined prefixes within their respective documentation.

## Provider-Defined vs. User-Defined Tags

The following is an example of one User-Defined Tag and one Provider-Defined Tag, respectively, with tag key, `foo`.  The first property is not prefixed, and the Provider has a pre-selected prefix, `marketplace/`, applied to denote that it is a different type of tag.

```json
    {
        "foo":"bar",
        "marketplace/foo": "bar"
    }
```

## Finalized Tags

A Tag can either be static or dynamic. If a Tag is static, its value is immutable. If a Tag is dynamic, its value is determined by a set of predefined user or provider rules. A finalized Tag is the final result of any static or dynamic Tag.

| ResourceType    | ResourceId | Column                             |
| :---------------| :----------| :----------------------------------|
| Account         | my-account | { "team": "web", "env": "prod" }   |
| Virtual Machine | my-vm      | { "team": "web", *"env": "prod"* } |

After all tag inheritance rules are processed, the finalized cost and usage dataset shows that the Virtual Machine Resource did inherit tag, `env:prod`, from its corresponding Account because no tag with the same key exists.  Conversely, the Virtual Machine Resource did not inherit tag, `team:web`, because the Provider's tag inheritance rules determine that a Resource already containing a tag with the same key maintains that same tag.

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
| Data type       | Object           |
| Allows nulls    | True             |
| Value format    | MUST adhere to KeyValueFormat Attribute |

## Introduced (version)

1.0
