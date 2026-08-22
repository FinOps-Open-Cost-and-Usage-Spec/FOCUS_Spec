# Writing Specification Content

Instructions for generating or editing specification content. AI agents generating content MUST act as strict technical editors enforcing the FOCUS standards. Focus entirely on specification documents, schema definitions, and markdown formatting.

These content rules also apply when reviewing specification changes; see `.agents/reviewing-changes.md` for review conduct.

## Specification Structure

* `specification/spec.mdpp` - Main template that includes all sections
* `specification/datasets/` - Supported datasets
* `specification/datasets/{dataset}/columns/` - Column definitions per dataset
* `specification/attributes/` - Rules that govern datasets, rows, columns, and values
* `specification/metadata/` - Dataset metadata schemas
* `specification/supported_features/` - Catalog of FinOps capabilities enabled by FOCUS datasets
* `specification/appendix/` - Examples and supplementary content
* `supporting_content/` - Background info from spec development

## File Organization

* Each section has a `.mdpp` template that includes individual `.md` files
* All `.md` files in a directory must be included in the corresponding `.mdpp`
* Code blocks must be aligned to start of line (not indented)

## Normative Language & Requirements

* **BCP-14 Keywords:** Use MUST, MUST NOT, SHOULD, SHOULD NOT, MAY (uppercase). NEVER use: "REQUIRED", "SHALL", "SHALL NOT", "RECOMMENDED", "NOT RECOMMENDED", "OPTIONAL".
* **Location:** Capitalized BCP-14 keywords MUST NOT appear outside "Requirements" sections unless quoted. Do not apply this rule to files under `guidelines/` folder, where BCP-14 keywords may be used to describe authoring policies, requirement patterns, and examples.

* **Structure:** Use bulleted lists. Each bullet MUST express exactly one verifiable state. Split bullets that combine multiple obligations.
* **Nested Requirements:** Introduce nested bullets only when expressing composite requirements. Preserve the established indentation hierarchy and never skip nesting levels.
* **Requirement Ownership (DRY):** Each normative requirement MUST be defined exactly once. When the same normative behavior applies in multiple locations, authors MUST reference the existing requirement or reusable Attribute rather than duplicating the requirement text.
* **Structural Grouping Bullets:** Organizational bullets (such as headings introducing groups of requirements) MUST NOT be authored as normative requirements. They exist solely to organize subordinate normative requirements and are not independently verifiable.
* **Composite Requirements:** When a requirement introduces multiple subordinate requirements, the parent requirement MUST establish the applicability or scope while nested requirements define the independently verifiable normative obligations. Each nested bullet MUST remain independently verifiable.
* **Allowed Subjects:** MUST be schema-level entities (e.g., `FOCUS dataset`, `BilledCost`). Actors (e.g., Data Generator) and Processes MUST NOT be subjects.
* **State vs. Behavior:** Describe a state, not behavior. Prohibited process verbs: *ensure, handle, support, provide, alter, prefix, document* (though they MAY appear in conditional clauses).
* **Conditional Phrasing:** Use ONLY: `when / unless / only when / except when`. (DO NOT use `if`).
* **Mathematical Accuracy:** `and/or` is permitted ONLY in mathematical validations or conditional clauses.
* **Comparison Terminology:** Select comparison terminology according to the semantics of the comparison:
  * use `equal` for numeric comparisons;
  * use `match` for identifiers and string values;
  * use `be` when evaluating states or enumerated values; and
  * use `equivalent` for semantic equivalence.
  * use `remain consistent` when requiring a value to be stable across time, records, or another defined scope.
* **Structural Anchors:** Requirements sections, including reusable Attribute requirement sections, MUST begin with a non-verifiable anchor phrase ending in a colon (e.g., `<Entity> MUST adhere to the following requirements:`). Anchor requirements exist solely to establish the parsing structure of subordinate requirements and MUST NOT be interpreted as independently verifiable normative requirements.
* **Terminology:** Normative references to columns MUST use `ColumnId`s, never column Display Names. Requirements governing a specific dataset MUST use its `DatasetId` as the subject (e.g., `SkuPrice`). Requirements applying generically to all FOCUS datasets MUST use `FOCUS dataset`. Otherwise, authors MUST use the abstraction that precisely matches the requirement (e.g., `dataset instance` or `dataset artifact`) and MUST avoid using `FOCUS dataset` when a narrower abstraction is intended.
* **Tone:** Use formal language. Contractions (e.g., *don't, can't*) MUST NOT be used in normative requirements.
* **Inline Examples:** Any non-normative examples embedded within a requirement MUST be enclosed in parentheses using "e.g." (e.g., `...without lossy transformations (e.g., rounding)`).
* **Subsection Ordering:** When generating new specification entities, preserve the subsection ordering already established for that entity type within the specification. Do not invent alternative subsection sequences.

## Editorial Conventions

* **Column/Attribute IDs:** PascalCase without spaces (e.g., PricingQuantity). Entity IDs MUST be used in normative text sections.
* **Column/Attribute References in Non-Normative Content:**
  * Display Names SHOULD be used for conceptual, reader-facing references.
  * Canonical IDs MAY be used for schema-facing references.
  * A reference is schema-facing when it identifies a field in code, JSON, SQL, a schema, a table header, or an object/property path, or when the surrounding sentence describes that field being populated, omitted, null, serialized, validated, matched, compared, grouped, filtered, joined, aggregated, or repeated.
  * When none of the schema-facing conditions above applies, treat the reference as conceptual.
  * Reviewers MUST NOT create a finding solely because a schema-facing non-normative reference uses its canonical ID.
  * A canonical ID used for a conceptual non-normative reference MAY produce a suggestion, but MUST NOT produce an error or warning.
* **No Mixing:** Do not mix Entity IDs and Display Names within the same normative requirement.
* **Column values:** When a column value appears in prose or normative text, enclose it in double quotation marks (e.g., `"Usage"`, `"Tax"`). In an Allowed Values table, list values without quotation marks because the `Value` column identifies them as literals, unless quotation marks are part of the value itself.
* **Glossary terms:** Link with `[*term*](#glossary:term)` format.
* **Linking Rule:** For each distinct entity or glossary destination in a source Markdown file:
  * Ignore occurrences in document titles and section headings.
  * Link the first remaining occurrence in reading order.
  * Leave all later occurrences unlinked.
  * When no remaining occurrence exists, no link is required.
  Exceptions:
  * A link whose anchor text is not an entity name or glossary term does not count toward first occurrence.
  * Content Constraints sections link every entity reference.
  * Glossary entries apply this rule independently within each entry.
  * An entity catalog table MAY link the entity that identifies each row, even when that entity was linked earlier in the file. Treat a table as an entity catalog only when each data row represents and identifies a distinct specification entity.
  * Each normative requirement bullet MAY link its first reference to each distinct FOCUS entity, glossary term, or FOCUS Condition, even when the same destination was linked earlier in the file. Do not link later references to that destination within the same bullet.
* **Lists:** All unordered lists MUST use asterisks (`*`), never dashes (`-`) or plus signs (`+`). Nested bullet points MUST use exactly two spaces per level.
* **Notes:** Important notes must use the blockquote format (`> **Note:**`).
* **Notes versus Exceptions:** Use Notes only for informative or explanatory material. Normative conditions and exceptions MUST be expressed as requirements rather than embedded inside Notes.
* **Anchors:** Pandoc auto-generates custom heading anchors. DO NOT flag missing HTML `<a name="">` tags.
* **Markdown Tables:** Format Markdown tables for readability. Align compact tables where practical and prefer compact formatting for wide tables.
* **Numbers in Prose:** In explanatory prose, spell out numbers zero through nine and use numerals beginning at 10. Preserve numeric notation in JSON, mathematics, schema constraints, identifiers, and technical examples.
* **Dash Usage:** Use hyphens for compound modifiers and spaced dashes only for parenthetical interruptions. Apply each form consistently according to its purpose.

## Validation & Schema Accuracy

* **Mathematical & Schema Accuracy:** AI reviewers MUST rigorously calculate, parse, and verify all data within examples (especially JSON snippets and tables). Flag any mathematical inconsistencies or hallucinated data.
* **JSON Formatting:** JSON blocks MUST use double quotation marks for keys. Verify that the JSON is structurally valid.
* **JSON Object Requirements:** Requirements governing a JSON object MUST be authored with the object definition. Column-level requirements MUST remain with the column definition. Requirements for object properties SHOULD reference properties using dot notation where appropriate to distinguish object-level constraints from property-level constraints.
* **Example Disclaimer:** Top-level sections with examples and no normative requirements MUST begin with: `> Note: The following section is informative and non-normative. It does not define requirements.` Enforce ONLY on Level-2 headings in `spec.md` or major section overview files (e.g., `appendix_overview.md`). Ignore nested .md files.
