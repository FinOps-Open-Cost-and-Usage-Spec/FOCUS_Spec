# ModelRules Test Coverage Report

This report documents the suite of automated tests validating the ModelRules JSON. The tests cover schema compliance, identifiers, dependencies, suffix alignment, applicability, function semantics, and orphan detection.

## Test Descriptions

### Schema & Structural Compliance

#### test_schema.py

*Purpose*: Validate ModelRules JSON against the official schema.

*Description*: Ensures the built cr-*.json file conforms to model_schema.json. Checks structural integrity, required properties, data types, and schema-defined constraints. Guarantees the final JSON is schema-compliant and stable.

#### test_static_type_requirement.py

*Purpose*: Enforce Requirement rules for Static vs Dynamic.

*Description*: Validates that Static rules have a non-empty ValidationCriteria.Requirement, while Dynamic rules must always have {}. Prevents mismatches between type and requirement definition.

#### test_dynamic_type_requirement.py

*Purpose*: Explicit check for Dynamic rules.

*Description*: Strengthens guarantees that Dynamic rules never contain validation logic inside Requirement. Protects against improperly assigned requirements for rules that should be externally driven.

### Identifier & Naming Integrity

#### test_unique_ids.py

*Purpose*: Verify unique ConformanceRule IDs in built JSON.

*Description*: Ensures no duplicate rule IDs appear in the final merged JSON output. Prevents accidental overwrites after Python’s JSON merge.

#### test_rule_id_duplicates_in_sources.py

*Purpose*: Detect duplicate IDs at source.

*Description*: Checks all individual JSON source files in model_rules for duplicate keys. Fails early before merge, so no silent overwriting occurs.

#### test_rule_number_sequences.py

*Purpose*: Validate rule numbering is sequential.

*Description*: For each rule prefix (e.g., ChargePeriodEnd-C-), ensures numbering starts at 000 and increments without gaps. Detects missing numbers and enforces consistency in sequence.

#### test_reference_prefix_for_columns.py

*Purpose*: Ensure Column rules align Reference with ID.

*Description*: Validates that for EntityType=Column, the Reference property matches the prefix of the rule ID. Prevents mismatches between identifier and reference.

#### test_entityid_format.py

*Purpose*: Validate EntityType → ID format convention.

*Description*: Ensures Attribute rules use -A-, Column rules use -C-, and Dataset rules use -D- in their IDs. Enforces strict naming consistency across entity types.

### Dependencies & Connectivity

#### test_ruleid_dependencies.py

*Purpose*: Ensure Dependencies reference existing rules.

*Description*: Confirms every ID in a rule’s ValidationCriteria.Dependencies exists in ModelRules. Prevents dangling links.

#### test_dependencies_exist.py

*Purpose*: Cross-verify dependency integrity.

*Description*: Validates all dependencies resolve to real ModelRules. Redundant with test_ruleid_dependencies but ensures complete coverage of dependency fields.

#### test_dependencies.py

*Purpose*: Enforce dependency consistency rules.

*Description*: Ensures dependencies reference valid rule IDs with correct relationships (e.g., Columns depending on matching Datasets). Prevents invalid cross-entity references.

#### test_no_duplicate_dependencies.py

*Purpose*: Prevent duplicate dependencies.

*Description*: Ensures no rule repeats the same dependency in its Dependencies array. Keeps dependency lists clean.

#### test_no_duplicate_checkconformancerule_items.py

*Purpose*: Prevent duplicate references inside Composite Items.

*Description*: In Composite rules with AND/OR, ensures the same CheckModelRule is not listed twice in Items. Avoids redundant logic.

#### test_datasets_rules_exist.py

*Purpose*: Validate Dataset → Rule references.

*Description*: Ensures that every rule ID listed under ModelDatasets.*.ModelRules exists in ModelRules. Prevents dataset stubs pointing to missing rules.

#### test_orphan_rules.py

*Purpose*: Detect orphaned rules.

*Description*: Finds rules not referenced by other rules or datasets. Allows exceptions for deprecated rules, base rules (-D-000-*), and specific column-to-dataset dependencies. Ensures no “dead” rules remain active.

#### test_orphan_attributes.py

*Purpose*: Detect orphaned attributes.

*Description*: Finds attributes not referenced by other check functions, rules or datasets. Allows exceptions for deprecated rules. Ensures no “dead” attributes remain active.

### Suffix, Scope & Keyword Alignment

#### test_suffix_by_keyword_and_scope.py

*Purpose*: Enforce suffix rules (-C, -M, -O).

*Description*: Unified precedence engine:
Scope present (Applicability, Condition, or “when/unless”) ⇒ must end in -C.
No scope:
Composite rules:
All Requirement-linked scoped ⇒ -C
Presence deps: MUST/SHOULD ⇒ -M; others ⇒ -O
Base rules: MUST/MUST NOT ⇒ -M; MAY/RECOMMENDED ⇒ -O.
Ensures suffix semantics align with scope and intent.

#### test_keyword_in_mustsatisfy.py

*Purpose*: Validate Keyword is present in MustSatisfy.

*Description*: Ensures ValidationCriteria.Keyword (MUST, SHOULD, RECOMMENDED, etc.) appears explicitly in MustSatisfy. Excludes false matches like treating “MUST NOT” as “MUST”. Guards against case issues by enforcing uppercase keywords only.

#### test_provider_supports_requires_applicability.py

*Purpose*: Require Applicability when provider support is implied.

*Description*: If MustSatisfy text mentions “provider supports…”, the rule must include explicit ApplicabilityCriteria. Guarantees textual conditions are codified structurally.

#### test_applicability_criteria.py

*Purpose*: Validate ApplicabilityCriteria references.

*Description*: Ensures all IDs listed in ApplicabilityCriteria are defined in the root ApplicabilityCriteria object. Prevents invalid or missing references.

### Function-to-Text Consistency

#### test_type_function.py

*Purpose*: Enforce semantic consistency for functions.

*Description*:
"Nullability" ⇒ Must reference null-related conditions in text.
"Format" ⇒ Must reference format.
"Type" ⇒ Must include “of type”.
"Composite" ⇒ Must use AND/OR with at least one CheckModelRule.

#### test_nullability_function.py

*Purpose*: Match Nullability with text.

*Description*: Ensures that any rule text referencing “null” uses Function="Nullability", except for composites.

#### test_format_function.py

*Purpose*: Match Format with text.

*Description*: Ensures any rule mentioning “format” uses Function="Format".

#### test_composite_when_and_or.py

*Purpose*: Validate composite structure.

*Description*: Requires that rules with Requirement.CheckFunction=AND/OR and CheckModelRule items must declare Function="Composite". Enforces structural correctness of composites.

#### test_no_spurious_composite.py

*Purpose*: Forbid invalid composites.

*Description*: Rules marked as Composite must contain AND/OR with at least one CheckModelRule. Prevents false use of Composite.

### Function Coverage & Cross-References

#### test_check_functions.py

*Purpose*: Validate referenced CheckFunctions.

*Description*: Walks all Requirement/Condition trees to ensure every CheckFunction value is defined in the CheckFunctions dictionary. Prevents use of undefined functions.

#### test_formatattributes_ruleids_exist.py

*Purpose*: Verify FormatAttributes references.

*Description*: Ensures all IDs listed in CheckFunctions.FormatAttributes arrays exist in ModelRules. Prevents dangling references.

#### test_unused_checkfunctions.py

*Purpose*: Ensure no unused CheckFunctions exist.

*Description*: Validates that every defined CheckFunction is referenced at least once. Prevents unused or obsolete definitions from lingering.

### Column–Dataset Alignment

#### test_c000_d_deps_presence_reference.py

*Purpose*: Validate Column-000 rules link to Datasets.

*Description*: Ensures all *-C-000-* Column rules depend on at least one -D- Dataset rule. If the Dataset dep is Presence, its Reference must match the Column’s. For Composite Datasets, all nested -D- rules must also share the same Reference. Guarantees column base rules are anchored to dataset presence definitions.

### Other Tests

#### test_mustsatisfy_ends_with_colon_or_period

*Purpose*: Validate MustSatisfy punctuation.

*Description*: Ensures all MustSatisfy lines end with either a '.' or ':'

### Summary Table

| Test File                                                | Purpose                                | Description                                                                                                                                                     |
| -------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **test\_schema.py**                                      | Validate schema compliance             | Ensures the built JSON file matches the official `model_schema.json`, verifying structure, required fields, and data types.                                        |
| **test\_static\_type\_requirement.py**                   | Enforce Static vs Dynamic requirements | Requires `Static` rules to have non-empty `Requirement` and `Dynamic` rules to have `{}`.                                                                       |
| **test\_dynamic\_type\_requirement.py**                  | Check Dynamic rules                    | Explicitly enforces that `Dynamic` rules never carry validation logic inside `Requirement`.                                                                     |
| **test\_unique\_ids.py**                                 | Ensure unique IDs                      | Confirms all ConformanceRule IDs are unique in the final built JSON.                                                                                            |
| **test\_rule\_id\_duplicates\_in\_sources.py**           | Detect source duplicate IDs            | Catches duplicate rule IDs across raw JSON files before merge, preventing silent overwrites.                                                                    |
| **test\_rule\_number\_sequences.py**                     | Validate numbering                     | Ensures rule numbers start at `000` and increment sequentially without gaps.                                                                                    |
| **test\_reference\_prefix\_for\_columns.py**             | Align Column reference                 | Validates Column rules’ `Reference` matches their rule ID prefix.                                                                                               |
| **test\_entityid\_format.py**                            | Enforce ID markers                     | Ensures Attributes use `-A-`, Columns use `-C-`, and Datasets use `-D-` in IDs.                                                                                 |
| **test\_ruleid\_dependencies.py**                        | Verify dependency links                | Ensures every dependency listed in a rule exists in `ModelRules`.                                                                                         |
| **test\_dependencies\_exist.py**                         | Check dependencies exist               | Cross-checks all dependency IDs to guarantee they resolve to valid rules.                                                                                       |
| **test\_dependencies.py**                                | Dependency consistency                 | Enforces dependency rules (e.g., correct entity type relationships).                                                                                            |
| **test\_no\_duplicate\_dependencies.py**                 | Prevent duplicate deps                 | Ensures no rule lists the same dependency more than once.                                                                                                       |
| **test\_no\_duplicate\_checkconformancerule\_items.py**  | Prevent duplicate Items                | Ensures Composite `AND/OR` lists don’t include the same `CheckModelRule` twice.                                                                           |
| **test\_datasets\_rules\_exist.py**                      | Validate dataset references            | Ensures all rule IDs listed in `ModelDatasets` are present in `ModelRules`.                                                                         |
| **test\_orphan\_rules.py**                               | Detect orphaned rules                  | Flags rules not referenced elsewhere, allowing exceptions for deprecations and base rules.                                                                      |

| **test\_orphan\_attributes.py**                           | Detect orphaned attributes            | Flags attributes not referenced elsewhere, allowing exceptions for deprecations.                                                                      |

| **test\_suffix\_by\_keyword\_and\_scope.py**             | Enforce suffix rules                   | Applies unified precedence: scope ⇒ `-C`; otherwise, MUST ⇒ `-M`, MAY/RECOMMENDED ⇒ `-O`, with Composite dependency logic.                                      |
| **test\_keyword\_in\_mustsatisfy.py**                    | Keyword must match text                | Ensures `Keyword` (MUST, SHOULD, RECOMMENDED) is explicitly in `MustSatisfy` without false matches (e.g., “MUST NOT” ≠ “MUST”).                                 |
| **test\_provider\_supports\_requires\_applicability.py** | Require applicability                  | Rules mentioning “provider supports” must include explicit `ApplicabilityCriteria`.                                                                             |
| **test\_applicability\_criteria.py**                     | Validate applicability keys            | Ensures all IDs in `ApplicabilityCriteria` arrays exist in the global Applicability dictionary.                                                                 |
| **test\_type\_function.py**                              | Function ↔ text consistency            | Validates function alignment: `Nullability` ↔ nulls, `Format` ↔ format, `Type` ↔ “of type”, `Composite` ↔ AND/OR with child rules.                              |
| **test\_nullability\_function.py**                       | Match nullability                      | Ensures rules mentioning “null” use `Function="Nullability"` (non-composites).                                                                                  |
| **test\_format\_function.py**                            | Match format                           | Ensures rules mentioning “format” use `Function="Format"`.                                                                                                      |
| **test\_composite\_when\_and\_or.py**                    | Validate composites                    | Ensures AND/OR requirements with `CheckModelRule` are marked as `Composite`.                                                                              |
| **test\_no\_spurious\_composite.py**                     | Forbid invalid composites              | Ensures rules marked `Composite` actually implement AND/OR with child rules.                                                                                    |
| **test\_check\_functions.py**                            | Verify CheckFunctions                  | Ensures all referenced `CheckFunctions` are defined in the CheckFunctions dictionary.                                                                           |
| **test\_formatattributes\_ruleids\_exist.py**            | Validate FormatAttributes              | Ensures IDs listed in `CheckFunctions.FormatAttributes` exist in `ModelRules`.                                                                            |
| **test\_unused\_checkfunctions.py**                      | Eliminate unused CheckFunctions        | Ensures every defined CheckFunction is used at least once.                                                                                                      |
| **test\_c000\_d\_deps\_presence\_reference.py**          | Validate Column-000 dependencies       | Ensures all `*-C-000-*` rules depend on at least one `-D-` rule; if Presence, the `Reference` must match. Composite D rules must also share the same reference. |
| **test_mustsatisfy_ends_with_colon_or_period.py**.       | Validate MustSatisfy punctuation       | Ensures all MustSatisfy lines end with `.` or `:`. |
