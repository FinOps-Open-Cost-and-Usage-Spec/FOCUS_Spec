<!-- review(F-00) [Open]: This document does not state its purpose, its status or how it relates to PR #2848. PR #2848 restructures guidelines/contributors/editorial-guidelines.md as a move-only change; this document instead maps the rules of the Editorial Guidelines Review (rule IDs ED-<CAT>-<NN>, assumptions A-01 to A-42) into the structure Irena proposed in her A-02 note. Alternative (a status block for the author to confirm or edit): "Status: proposal for discussion (step 1). This document shows how the rules of the Editorial Guidelines Review fit the structure proposed in A-02. It does not replace guidelines/contributors/editorial-guidelines.md. Next step (to be decided): adopt this document as the revised guideline, or fold it into PR #2848." -->
<!-- review(F-01) [Traceability]: The line references in this file (e.g., "working_draft L153") match guidelines/contributors/editorial-guidelines.md at commit e9cdcc7, the commit the Editorial Guidelines Review used; working_draft has moved since. "T<n>.<x>" refers to rows of the summary table at the top of that version (L13-147). Alternative: name commit e9cdcc7 once at the top of the file. -->

# Editorial Style Guidelines

<!-- review(F-02) [Editorial]: This paragraph uses two em dashes ("standards[em dash]whether ... information[em dash]we"), which ED-PUN-05 below rules out (A-21, approved by Joaquin and Matt; Irena did not vote). Alternative: "By following the specified standards - whether in formatting, linking, or structuring information - we ensure ..." -->
The "Editorial Style Guidelines" section ensures consistency and clarity across all documentation. Adhering to these guidelines is crucial for maintaining a unified style, which enhances readability and reduces misinterpretation. By following the specified standards—whether in formatting, linking, or structuring information—we ensure that all documents are professional, clear, and aligned with our editorial principles. Consistent application of these guidelines contributes to high-quality, user-friendly documentation.

## Table of Contents

* [How to Read These Rules](#how-to-read-these-rules)
* [Scope and Governance](#scope-and-governance)
* [Core Editorial Rules](#core-editorial-rules)
  * [Document Structure](#document-structure)
  * [Entity References](#entity-references)
  * [Linking](#linking)
  * [Wording](#wording)
  * [Punctuation and Characters](#punctuation-and-characters)
  * [Lists](#lists)
  * [Callouts](#callouts)
  * [Examples](#examples)
  * [Code and JSON](#code-and-json)
  * [Tables](#tables)
* [Column Editorial Rules](#column-editorial-rules)
  * [Column Examples](#column-examples)

<!-- * [Supported Features Editorial Rules](#supported-features-editorial-rules) -->
<!-- * [Retired Rule IDs (Optional)](#retired-rule-ids-optional) -->

## How to Read These Rules

<!-- review(F-03) [Gap]: This section is empty. Content it could hold: (1) what the uppercase keywords mean in this document (BCP 14), given that it is itself a guideline document; (2) how rules are identified - A-03 is under question: Irena and Matt prefer readable PascalCase IDs built from the rule name, and today the IDs exist only in HTML comments, so readers and review tools cannot cite them; (3) whether each rule shows its lint verdict (Existing, Custom, Heuristic, Review) - A-12 was approved by all three reviewers, but no rule shows one; (4) that examples are illustrative (ED-SCP-02 could move here). -->

## Scope and Governance

<!-- ED-SCP-01 (absorbs ED-REF-05) -->
<!-- review(F-04) [Gap]: The section does not state the boundary between this document and the Normative Requirements Guidelines (NRG), which A-05 sets (approved by all three reviewers). Also, the comment says ED-REF-05 was absorbed, but the "Entity ID References" bullet is still a separate rule. Alternative (ED-SCP-01 of the Editorial Guidelines Review, replacing both sentences and the bullet): "Authors MUST write and change normative requirements according to the Normative Requirements Guidelines. The Normative Requirements Guidelines govern how requirements are built. This document governs formatting, punctuation and comparison wording." -->
Normative requirements are defined and authored exclusively according to the Normative Requirements Guidelines.
Authors MUST refer to the [Normative Requirements Guidelines](normative-requirements-guidelines.md) when writing or modifying normative requirements.

* **Entity ID References:** Formatting and usage conventions for normative requirements are defined in the Normative Requirements Guidelines.

<!-- ED-SCP-02 -->
<!-- review: In agreement. -->
<!-- text from proposal (ED-SCP-02); replaces working_draft note L153 -->
> **Note:** Examples in this document are illustrative and non-normative. They do not define requirements and do not override the rules.

<!-- ED-SCP-03 -->
<!-- review(F-05) [Open]: The document does not say which files its rules cover. A-04 (rules cover specification/; guideline documents follow them except ED-STR-03) is under question: Irena and Matt note that the linking rules also do not fit guideline documents, which link to files and to their own headings. Both suggest an interim note as a first step. Alternative (interim note, following Irena's A-04 note): "> **Note:** These rules are written for Markdown sources under `specification/`. Guideline documents under `guidelines/` follow them where they apply. Known exceptions are the restriction of normative keywords to Requirements sections (ED-STR-03) and the linking rules (ED-LNK-01 to ED-LNK-04), whose link targets differ in guideline documents." -->
* **Entity Scope:** These rules apply to all entities defined in the FOCUS specification (e.g., Columns, Attributes, Datasets, Objects).

<!-- ED-SCP-05 -->
<!-- review: In agreement. -->
These guidelines can be modified through a Pull Request (PR), which the members must review and agree upon. This process ensures that any changes are thoughtfully considered and maintains the overall integrity of our editorial standards.

## Core Editorial Rules

### Document Structure

<!-- ED-STR-01 -->
<!-- review(F-06) [Conflict]: The order in the example (Title, Requirements, Entity ID, Display Name, ...) contradicts the column example in this document, which has Usability Constraints after Requirements; "Entity ID" is not a heading the specification uses, and "Title" is not a subsection. The note then says the order is only illustrative, so no order is set. A-28 and A-13 (fixed start and end, free middle) were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-STR-01 of the Editorial Guidelines Review): "Entity definition files MUST use the following subsection order: (1) A column file MUST start with `Requirements` and MUST end with `Column ID`, `Display Name`, `Description`, `Content Constraints` and `Version Introduced`, in that order. (2) An attribute file MAY start with `Overview`, MUST then have `Requirements`, and MUST end with `Attribute ID`, `Attribute Name`, `Description` and `Version Introduced`, in that order. (3) Other sections (e.g., `Allowed Values`, `Usability Constraints`, `Implementation Guidance` or `Examples`) MAY appear between `Requirements` and the fixed ending." -->
* **Consistent Subsection Order:** Sections for the same entity type SHOULD follow a consistent subsection order (e.g., Title, Requirements, Entity ID, Display Name, Description, Content Constraints, Version Introduced).

  > **Note:** The subsection order examples in this section are illustrative unless a canonical order is explicitly defined for a specific entity type.

<!-- ED-STR-02 -->
<!-- review(F-06) [Ambiguity]: "Match exactly across sections of the same entity type" does not say which titles are correct, only that they agree with each other. A-28 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-STR-02 of the Editorial Guidelines Review, once ED-STR-01 lists the fixed subsections): "The fixed subsections MUST use exactly the titles listed in ED-STR-01." -->
* **Consistent Subsection Titles:** Subsection titles SHOULD match exactly across sections of the same entity type.

<!-- ED-STR-03 (absorbs ED-STR-04, ED-CAL-17) -->
<!-- review(F-07) [Duplicate]: The comment says ED-STR-04 was absorbed, but "Normative Scope" and "No Normative Leakage" still state the same rule twice (also listed in the Follow-ups of PR #2848). Neither defines a Requirements section, and neither says whether a keyword in code counts. A-27 and A-34 were approved by Joaquin and Matt; Irena did not vote. The "Informative Examples" bullet (ED-CAL-17) can stay for now, because A-36 (dropping it) is under question by Matt. Alternative (ED-STR-03 of the Editorial Guidelines Review, replacing both bullets): "In specification files, BCP 14 keywords in uppercase MUST appear only in Requirements sections. A Requirements section is a heading whose text, ignoring the SkipTOC marker, is exactly 'Requirements', together with everything under it until the next heading of the same or a higher level. An object section that defines requirements MUST have its own Requirements subsection. A keyword inside a code block or code span is a mention, not a use." -->
* **Normative Scope:** Normative requirements (those using BCP-14 keywords) MUST appear only in the "Requirements" section.
* **No Normative Leakage:** Normative keywords (MUST, SHOULD, MAY, etc.) MUST NOT be used in any section other than "Requirements".

> **Note:** This restriction applies to normative content within FOCUS specification entities and does not prohibit guideline documents, examples, or editorial instructions from discussing normative terminology or authoring rules.

* **Example** (Markdown, illustrative):

  ```md
   Correct:
    ## Requirements
    ...
    * PricingQuantity MUST be greater than 0.
    
   Incorrect:
    ## Description
    ...
    * PricingQuantity MUST be greater than 0.
  ```

* **Informative Examples:** Examples MUST be considered informative and non-normative, and MUST NOT define requirements.

<!-- ED-STR-05 -->
<!-- ED-STR-05: no working_draft source -->
<!-- review(F-08) [Gap]: Empty placeholder. The build already enforces this rule (custom lint rule MD991), and A-33 (checks the build enforces are written down as rules) was approved by Joaquin and Matt; Irena did not vote. An empty placeholder leaves it unclear whether the rule is adopted. Alternative (ED-STR-05 of the Editorial Guidelines Review): "* **Title Case Headings:** Headings MUST use title case." -->

<!-- ED-STR-06 -->
<!-- ED-STR-06: no working_draft source -->
<!-- review(F-08) [Gap]: Empty placeholder. The build already enforces this rule (lint rule MD024, siblings only), and A-33 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-STR-06 of the Editorial Guidelines Review): "* **Unique Sibling Headings:** Headings at the same level under the same parent MUST NOT repeat." -->

### Entity References

<!-- ED-REF-03 (absorbs ED-REF-01, ED-REF-02) -->
<!-- review(F-09) [Duplicate]: The comment says ED-REF-01 and ED-REF-02 were absorbed, but three bullets remain: no spaces; "the exact naming conventions used in the schema", where "schema" is not defined; and "Entity ID Case", which carries no keyword. Alternative (ED-REF-03 of the Editorial Guidelines Review, widened to every ID declaration section as Matt notes on A-08): "* **Entity IDs:** An Entity ID MUST be written exactly as defined in the entity's ID section (e.g., `Column ID`, `Attribute ID`, `Dataset ID` or `Object ID`), including letter case (e.g., CommitmentDiscountId or SkuPriceId)." Open (Irena's and Matt's notes on A-05): the NRG says references SHOULD default to singular form, and the specification pluralizes an ID once ("multiple BillingAccountTypes"); Matt suggests adding "Grammatical number never changes an Entity ID." -->
* **Entity ID Formatting:** Entity IDs MUST be formatted without spaces.
* **Entity ID Naming:** Entity IDs MUST match the exact naming conventions used in the schema (e.g., CommitmentDiscountId).

<!-- added: not in proposal; replaces summary table row T2.a (Column & Attribute IDs) -->
* **Entity ID Case:** FOCUS entity IDs use *Pascal case* (e.g., BilledCost, CommitmentDiscountId). See the related attributes in the specification (e.g., FOCUS Column Handling, Custom Column Handling) for further naming requirements.

<!-- ED-REF-04 -->
<!-- added: not in proposal; adapted from proposal ED-REF-04 (scope worded as in ED-REF-13, "Code blocks are not affected." dropped); replaces summary table row T2.b (Column & Attribute IDs) -->
<!-- review(F-10) [Ambiguity]: With "Code blocks are not affected." dropped, it is unclear whether an Entity ID inside a code span or code block breaks this rule. This document's own examples quote requirement text in code spans (e.g., `BilledCost MUST be 0` under ED-WRD-06), and ED-REF-13 excludes code. A-15 was approved by Joaquin and Matt; Irena did not vote. Alternative: add "Code spans and code blocks are not affected." -->
* **Entity IDs as Plain Text:** Entity IDs in prose, list items and table cells MUST NOT be bold, italic or in backticks.

<!-- ED-REF-06 (absorbs ED-REF-07) -->
<!-- review(F-11) [Conflict]: The comment says ED-REF-07 was absorbed, but the MUST bullet and the SHOULD bullet both remain (also listed in the Follow-ups of PR #2848). Also, "outside Requirements sections" would forbid the ID in the `Column ID` section itself. A-08 (one rule at MUST, with carve-outs) was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-REF-06 of the Editorial Guidelines Review, with the carve-outs widened to every ID section as Matt notes on A-08): "* **Display Names in Non-Normative Prose:** Non-normative prose MUST refer to entities by their Display Name. This rule does not apply to Requirements sections, ID sections (e.g., `Column ID`, `Attribute ID`, `Dataset ID` or `Object ID`), Content Constraints tables or code." -->
* **Entity Display Name References:** References to FOCUS entities in non-normative content (i.e., outside Requirements sections) MUST use Display Names when available.
* **Display Names Usage:** Display Names SHOULD be used in introductory or explanatory sections where natural language context is more appropriate.

<!-- ED-REF-08 -->
<!-- review(F-12) [Ambiguity]: "SHOULD follow normal text conventions" does not say which spelling is correct, and does not cover attributes, whose Display Name is in the `Attribute Name` section. A-13 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-REF-08 of the Editorial Guidelines Review): "* **Display Name Spelling:** A Display Name MUST be written exactly as defined in the entity's `Display Name` section (e.g., Commitment Discount ID). For attributes, the `Attribute Name` section is the Display Name." -->
* **Display Names Formatting:** Display Names SHOULD follow normal text conventions, including spaces between words (e.g., Commitment Discount ID).

<!-- ED-REF-09 (absorbs ED-REF-10) -->
<!-- added: not in proposal; adapted from proposal ED-REF-09 (scope worded as in ED-REF-13, "for example" written as "e.g."); replaces summary table rows T3.a and T3.b (Column Values) and Consistent Formatting (L185) -->
<!-- review(F-13) [Open]: A-06 (column values in double quotes) is under question. Matt suggests double quotes for string and Allowed Value literals only, with numbers, booleans and null unquoted. Irena asks whether formatting should differ for Allowed Values, sample string values (e.g., GB-Hours), numeric, boolean and null values, and values in tables. As written, "a column value" covers all of these, so the scope by value type needs a decision. Not open: both confirm double quotes for Allowed Values in requirements (see the examples under ED-WRD-03 and ED-CAL-14). -->
* **Column Values:** A column value MUST be enclosed in straight double quotes (e.g., "Usage", "Tax") and MUST NOT be bold, italic or in backticks. This applies in prose, list items and table cells.

<!-- ED-REF-11 -->
<!-- text from proposal (ED-REF-11); replaces summary table row T5.a (Glossary) -->
<!-- review: In agreement. -->
* **Glossary Links:** A glossary link MUST use italic link text, in the form `[*term*](#glossary:term)`.

<!-- ED-REF-13 -->
<!-- text from proposal (ED-REF-13); replaces the three worked example lines used as its source (L415, L440, L444) -->
<!-- review: In agreement. This rule answers the open point in the Follow-ups of PR #2848 ("Glossary terms: whether every occurrence is italic, or only the linked one"): unlinked mentions are italic when the word is used in its glossary sense (A-16, approved by Joaquin; Matt's verdict is Question, asking for a pilot on one dataset before the follow-up spec work is sized; A-42, approved by Joaquin and Matt; Irena did not vote on either). -->
* **Unlinked Glossary Mentions:** A mention of a glossary term that is not linked MUST be italic (`*term*`) when the word is used in the sense its glossary entry defines. This applies in prose, list items and table cells, not in headings, code, entity IDs or column values. A word used in its everyday sense stays plain.

### Linking

<!-- ED-LNK-01 -->
<!-- added: not in proposal; link target part of summary table rows T1.b, T2.c, T5.b -->
<!-- review(F-15) [Gap]: "MUST be linked only on their first occurrence" forbids later links but does not require the first one. It also leaves open whether an ID and its Display Name count as one reference, whether an entity is linked in its own definition file, and whether headings and code count. The rule does not point to its exceptions below, which Irena asks for in her notes on A-05 and A-11. A-07 and A-17 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-LNK-01 of the Editorial Guidelines Review, with a pointer to the exceptions; it would replace the "Linking on First Occurrence" bullet and its note): "* **Linking on First Occurrence:** In each source file, the first occurrence of an entity reference (including FOCUS entity IDs, Display Names and glossary terms) MUST be linked, and later occurrences MUST NOT be linked. An entity's ID and its Display Name count as the same reference. An entity MUST NOT be linked in its own definition file. Headings and code MUST NOT contain entity links and do not count as the first occurrence. Content Constraints sections and the Glossary file are exceptions (see below)." -->
* **Entity Link Targets:** When a reference to a FOCUS entity (ID or Display Name) is linked, the link MUST point to the section that defines the entity.
* **Glossary Link Targets:** When a glossary term is linked, the link MUST point to its glossary entry.
* **Linking on First Occurrence:** To avoid excessive linking, entity references (including FOCUS entity IDs, display names, and glossary terms) MUST be linked only on their first occurrence within a given source markdown file.

  > **Note:** Unless otherwise specified, first-occurrence linking is evaluated relative to the containing source markdown file.

**Exceptions:**

<!-- ED-LNK-02 -->
<!-- review: In agreement. -->
* In **Content Constraints** sections, all entity references MUST be linked, regardless of prior occurrence in the source markdown file.

<!-- ED-LNK-03 -->
<!-- review: In agreement. -->
* In the **Glossary** file, entity references MUST be linked only on their first occurrence within each glossary entry, rather than once per source markdown file.

<!-- ED-LNK-04 -->
<!-- ED-LNK-04: no working_draft source -->
<!-- review(F-08) [Gap]: Empty placeholder. The build already enforces this rule (specification/tests/test_spec_links.py); A-32 and A-33 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-LNK-04 of the Editorial Guidelines Review): "* **Internal Links Resolve:** Every internal link (an `#anchor` or a relative path) MUST resolve to an anchor or file in the built specification. External URLs are not checked." -->

### Wording

To ensure consistent language when describing relationships and evaluations between values, normative requirements and standard prose MUST use the following terminology:

<!-- ED-WRD-01 -->
<!-- review(F-16) [Conflict]: A requirement such as "BilledCost MUST be 0" fits both this rule ("equal" for numeric values) and ED-WRD-03 ("be" for a specific value); ED-WRD-06 uses `BilledCost MUST be 0` as its own example. A-10 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-WRD-01 of the Editorial Guidelines Review, limited to two values or a value and a calculation): "* **Numeric Comparisons:** Use 'be equal to' when comparing two numeric values, or a value with a calculation (e.g., 'ContractedCost MUST be equal to BilledCost'). Do not use 'equal' alone, 'equals' or 'match'." Out of scope here (Matt's note on A-10): NRG L1060 teaches "MUST equal" in its patterns. -->
* **Numeric Values:** Use "equal" or "be equal to" when comparing numeric values, costs, quantities, or mathematical sums (e.g., "ContractedCost MUST be equal to BilledCost"). Do not use "match".

<!-- ED-WRD-02 -->
<!-- review: In agreement. -->
* **Identifiers and Strings:** Use "match" when comparing strings, IDs, or names (e.g., "HostProviderName MUST match ServiceProviderName"). Do not use "equal".

<!-- ED-WRD-03 -->
<!-- review(F-16) [Conflict]: For a numeric literal, this rule ("be") and ED-WRD-01 ("equal" for numeric values) both apply. The example also puts the values Purchase and Usage in backticks, while ED-REF-09 requires double quotes. A-10 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-WRD-03 of the Editorial Guidelines Review): "* **State and Literal Values:** Use 'is' or 'be' when a column is compared with a literal value or state, numeric or string (e.g., `when ChargeCategory is "Purchase"` or `BilledCost MUST be 0`). Do not use 'equals', except in the phrases of ED-WRD-04." -->
* **State and Conditions:** Use forms of the verb "to be" (e.g., "is", "are", "be") when evaluating if a column contains a specific value or state (e.g., "when ChargeCategory is `Purchase`" or "ChargeCategory MAY be `Usage`"). Do not use "equals" or "equal", **except** when evaluating inequalities (e.g., "greater than or equal to").

<!-- ED-WRD-04 -->
<!-- review(F-17) [Ambiguity]: The rule names the phrases to use but not the forms to avoid, so a fixed-pattern check has nothing to flag. A-35 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-WRD-04 of the Editorial Guidelines Review): add "Do not use 'at least', 'no more than', 'no less than' or symbols such as `>=`." Matt's caution on A-35: "at least by Service Provider Name" (rate_optimization_and_contract_evaluation.md line 49) is not a range limit, so the check needs a way to pass such uses. -->
* **Inequalities:** When expressing range or directional limits, the standard phrases "greater than or equal to" and "less than or equal to" MUST be used, even for non-numeric data types like timestamps or dates (e.g., "BillingPeriodLastUpdated MUST be greater than or equal to BillingPeriodCreated").

<!-- ED-WRD-05 -->
<!-- review(F-18) [Open]: A-18 (use only "equivalent") is under question by Irena and Matt: does dropping "semantically" lose precision, given other senses of "equivalent" in the specification (e.g., "no equivalent FOCUS column", "PricingCurrency-denominated equivalent of EffectiveCost")? Separately, the example misquotes the specification: pricingunit.md says "MUST be semantically equal", which this rule forbids. Alternative for the example: quote a compliant requirement, and list the two PricingUnit requirements as follow-up spec fixes. -->
* **Semantic Comparisons:** When comparing concepts, formats, or values that share the same meaning but may not be strictly identical strings, use "equivalent" or "semantically equivalent" (e.g., "PricingUnit MUST be semantically equivalent to the corresponding pricing measurement unit..."). Do not use "equal".

> **Note:** Validation of comparison terminology may require contextual understanding of value types, identifiers, semantic equivalence, or domain-specific meaning and may not always be suitable for deterministic editorial validation.

<!-- ED-WRD-06 -->
<!-- review(F-19) [Ambiguity]: (1) The label colon sits outside the bold ("**Spelling Out Numbers**:"). (2) "DOES NOT" in uppercase reads like a BCP 14 keyword. (3) The exception is a nested bullet under a parent that does not end with a colon (see ED-LST-03 and A-22). (4) "Technical values" and "explicit column constraints" leave units, percentages, currency, versions and mixed sentences open. A-19 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-WRD-06 of the Editorial Guidelines Review): "* **Numbers:** In prose, numbers zero to nine MUST be written as words (e.g., 'one', 'nine'), and numbers 10 and above as numerals (e.g., '10', '42'). Numerals MUST also be used for numbers with a unit, a percent sign or a currency; versions and section numbers; values in requirements, tables and code (e.g., `BilledCost MUST be 0`, not `BilledCost MUST be zero`); and any number in a sentence that already uses a numeral of 10 or more." -->
* **Spelling Out Numbers**: In standard prose, numbers zero through nine MUST be spelled out as words (e.g., "one", "two", "nine"), while numbers 10 and above MUST be written as numerals (e.g., "10", "42").
  * **Exception:** This rule DOES NOT apply to technical values, mathematical formulas, JSON examples, or explicit column constraints (e.g., write `BilledCost MUST be 0`, not `BilledCost MUST be zero`).

<!-- ED-WRD-07 -->
<!-- review(F-20) [Open]: A-20 (currency at MUST, `$` for USD and ISO 4217 codes for other currencies) is under question by Irena and Matt. Open points: (1) scope - monetary amounts in explanatory text versus column values, which follow NumericFormat and carry no symbol (e.g., an appendix table shows ListCost as 144.00 next to "$288.00" in its description); (2) whether `$` means only USD; (3) whether other currencies use symbols (e.g., the euro or pound sign) or ISO 4217 codes (e.g., EUR, GBP). Both accept MUST once the scope is set. -->
* **Currency and Dollar Signs:** The `$` symbol SHOULD be used for currency values in prose and tables. For build-pipeline behavior and troubleshooting related to dollar-sign parsing, see [MarkdownPP Guidelines](markdownpp-guidelines.md#currency-and-dollar-sign-handling).

### Punctuation and Characters

<!-- ED-PUN-01 -->
<!-- review: In agreement. -->
* **Sentence Spacing:** Sentences within paragraphs MUST be delineated with a single space.

<!-- ED-PUN-02 -->
<!-- review(F-21) [Editorial]: (1) "Nested Lists" suggests Markdown lists, but the rule is about lists inside a sentence. (2) The example is a nested bullet under a parent that does not end with a colon (see ED-LST-03 and A-22). Alternative: rename the label to "Semicolons in Lists with Internal Commas" (as in the Editorial Guidelines Review), and move the example to a sibling bullet "* **Example** (prose, illustrative):", as the other examples in this document are written. -->
* **Semicolons in Nested Lists:** When a comma-separated list contains one or more items with internal commas, semicolons MUST be used to separate the top-level list items to prevent ambiguity about item boundaries. See [Merriam-Webster's guide to semicolons](https://www.merriam-webster.com/grammar/a-guide-to-using-semicolons) for further reference.
  * **Example** (prose, illustrative):
    * Incorrect: `The columns foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support reliable decision-making.`
    * Correct: `The columns foster data integrity, interoperability, and consistency; improve data analysis and reporting; and support reliable decision-making.`

<!-- ED-PUN-03, ED-PUN-04, ED-PUN-05 -->
<!-- review(F-22) [Strength and Conflict]: (1) "SHOULD NOT" for dash characters is weaker than A-21 (MUST, approved by Joaquin and Matt; Irena did not vote; Matt counts 33 em dashes in linted files), and "special unicode dash characters" does not name en and em dashes. (2) The ED-PUN-04 example uses an Entity ID in prose ("The metric - BilledCost - is required."), which ED-REF-06 forbids. Alternative (Editorial Guidelines Review): third bullet "En dashes, em dashes and HTML dash entities MUST NOT be used."; example "The metric - Billed Cost - is required."; and, for ED-PUN-03, add "because en and em dashes are not used". -->
* **Dash Formatting:**
  * An unspaced hyphen (`-`) MUST be used for compound words (e.g., `cost-only`) and ranges (e.g., `2024-2025`).
  * A spaced hyphen (` - `) MUST be used to set off parenthetical phrases (e.g., `The metric - BilledCost - is required.`).
  * HTML entities and special unicode dash characters SHOULD NOT be used.

<!-- ED-PUN-06 -->
<!-- ED-PUN-06: no working_draft source -->
<!-- review(F-08) [Gap]: Empty placeholder. The build already enforces this rule (custom lint rule MD990), and ED-REF-09 depends on it ("straight double quotes"). A-33 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-PUN-06 of the Editorial Guidelines Review): "* **Straight Quotes and Periods:** Straight quotes and three periods (`...`) MUST be used. Smart quotes and the ellipsis character MUST NOT be used." -->

### Lists

<!-- ED-LST-01 -->
<!-- review: In agreement. -->
* **Unordered List Style:** All unordered lists in Markdown MUST use asterisks (`*`) rather than dashes (`-`) or plus signs (`+`). This maintains visual consistency across the specification and aligns with our automated linting standards.

<!-- ED-LST-02 (absorbs ED-LST-04, ED-LST-05) -->
<!-- review(F-23) [Duplicate]: The comment says ED-LST-04 and ED-LST-05 were absorbed, but three bullets remain, one with the typo "bullets points". The example shows one level only, so it does not illustrate indentation (the ED-LST-03 example does). Alternative (ED-LST-02 of the Editorial Guidelines Review): "* **Indentation:** Nested list items MUST be indented two spaces per level, MUST NOT skip a level, and MUST use the same indentation throughout a list." Consider removing the one-level example. -->
* **Indentation Levels:** Nested bullet points MUST be indented using two spaces per level.
* **No Skipped Levels:** Nested bullets points MUST NOT skip indentation levels.
* **Consistent Indentation:** All bullet points within the same list MUST use consistent indentation.
* **Example** (Markdown, illustrative):

  ```md
  * ... MUST be null when ChargeCategory is "Tax".
  * ... MUST be null when ChargeCategory is "Adjustment".
  ```

<!-- ED-LST-03 -->
<!-- review(F-24) [Conflict]: Read generally, the rule allows nesting only under a composite requirement, which this document breaks itself (Dash Formatting, Exception Label, Status Note Scope); PR #2848 lists this ambiguity in its Follow-ups. A-22 and A-05 were approved by Joaquin and Matt; Irena did not vote (on A-22). Alternative (ED-LST-03 of the Editorial Guidelines Review): "* **Parent Bullets:** A bullet that has nested items MUST end with a colon. When to nest requirements is defined in the Normative Requirements Guidelines ([Composite Requirements](normative-requirements-guidelines.md#composite-requirements))." Also: the example fence is indented four spaces, while the other examples use two. -->
* **Indentation Usage:** A nested indentation level MUST only be introduced when a parent bullet defines a composite (grouping) requirement, typically ending with a colon (:).
* **Example** (illustrative):

    ```md
    ... MUST adhere to the following requirements:

    * ... MUST be of type JSON ...
    * ... MUST adhere to the following nullability requirements:
      * ... SHOULD NOT be null when ...
      * ... MUST be null when ...
      * ... MUST adhere to the following ...
        * ... MUST be of type ...
    ```

<!-- ED-LST-08 -->
<!-- review(F-25) [Duplicate]: The two bullets state one rule, once for notes and once for exceptions. Alternative (ED-LST-08 of the Editorial Guidelines Review): "* **Lists Inside Callouts:** These list rules also apply inside notes and exceptions." -->
* **Bullet Usage in Notes:** When using bullets inside a note, the bullets MUST follow standard bullet formatting rules defined in this document.
* **Bullet Usage in Exceptions:** When using bullets inside an exception, the bullets MUST follow standard bullet formatting rules defined in this document.

### Callouts

#### Notes

<!-- ED-CAL-01 -->
<!-- review: In agreement. -->
* **Permitted in Non-Normative Content Only:** Notes MUST NOT appear in Requirements sections. Notes MAY appear in non-normative sections of the specification and in guidelines documents.

<!-- ED-CAL-02 -->
<!-- review(F-26) [Gap]: The reverse direction (blockquotes are used only for notes) is implied only by a parenthesis in ED-CAL-10 ("which is strictly reserved for Notes"). A-09 and A-14 were approved by Joaquin and Matt; Irena did not vote. Alternative (Editorial Guidelines Review): add "Blockquotes MUST NOT be used for anything other than notes." -->
* **Blockquote Format:** Notes MUST be expressed using Markdown blockquote syntax (`>`). This creates a consistent, parseable container and allows downstream tooling to control visual presentation in HTML and PDF outputs.

<!-- ED-CAL-03 (absorbs ED-CAL-04) -->
<!-- review(F-27) [Duplicate]: The comment says ED-CAL-04 was absorbed, but its "Consistent Terminology" bullet remains. That name is also used under Exceptions, so two rules share a name. "Only the terms ... MUST be used" also does not say when each label applies. A-09 and A-23 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-03 of the Editorial Guidelines Review, replacing both bullets): "* **Note Label:** A note MUST begin with `**Note:**` for one item, `**Notes:**` for a bullet list, or `**Preview:**` only to mark preview content (see [Preview Process](spec-change-guidelines.md#preview-process)). No other label (e.g., 'Important Note' or 'Warning') is allowed." -->
* **Note Label:** Notes MUST begin with the label `**Note:**`, `**Notes:**`, or `**Preview:**` (the term `Note`, `Notes`, or `Preview`, followed by a colon, in bold). The `**Preview:**` label is used only for notes that mark preview content (see [Preview Process](spec-change-guidelines.md#preview-process)).
* **Consistent Terminology:** Only the terms `Note`, `Notes`, or `Preview` MUST be used. Variants such as `Important Note`, `Warning`, or similar terms MUST NOT be used.

<!-- ED-CAL-05 -->
<!-- review(F-28) [Ambiguity]: "Discussing" normative keywords, in the nested note, could be read as allowing a note in a guideline document to state a requirement. A-34 (discussing means mentioning) was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-05 of the Editorial Guidelines Review, folding the nested note into the rule): "* **No Normative Keywords in Notes:** Notes are non-normative. A note MUST NOT state a requirement with a BCP 14 keyword. A note in a guideline document may mention a keyword as a word, in code or in quotes." -->
* **Non-Normative Content:** Notes MUST be informative and non-normative. They MUST NOT contain normative keywords (e.g., MUST, SHOULD, MAY).

  > **Note:** This restriction applies to informative notes within specification content and does not prohibit guideline documents or explanatory examples from discussing normative keywords.

<!-- ED-CAL-06 -->
<!-- review(F-29) [Ambiguity]: "A single blockquote line" depends on line wrapping, so a long note with one item, or one item of several sentences, is not covered. A-23 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-06 of the Editorial Guidelines Review): "* **Single-Item Notes:** A note with one item MUST be one blockquote paragraph after the label. The paragraph may contain more than one sentence." -->
* **Single-Line Notes:** A note containing a single statement MUST be written as a single blockquote line.

* **Example** (Markdown, illustrative):

  ```md
  > **Note:** This is a single-line note.
  ```

<!-- ED-CAL-07 -->
<!-- review(F-29) [Ambiguity]: "A note spanning multiple lines" depends on line wrapping, while the rule is about a note with several items in a bullet list. A-23 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-07 of the Editorial Guidelines Review): label "Multi-Item Notes", and "A note with several items MUST repeat the blockquote prefix (`>`) on each line." -->
* **Multi-Line Notes:** A note spanning multiple lines MUST repeat the blockquote prefix (`>`) on each line. A blank blockquote line (`>`) MUST separate the label from the bullet list.

* **Example** (Markdown, illustrative):

  ```md
  > **Notes:**
  >
  > * This is the first note.
  > * This is the second note, which provides additional information.
  ```

<!-- ED-CAL-08 -->
<!-- review: In agreement. -->
* **Multiple Notes:** When multiple notes are present in the same context, they SHOULD be grouped within a single blockquote and expressed as bullet points.

#### Exceptions

<!-- ED-CAL-09 -->
<!-- review(F-30) [Gap]: The rule names only where exceptions may not appear, which leaves open whether they may appear in non-normative specification text and elsewhere. It also starts a condition with "If". A-11 was approved by all three reviewers. Alternative (ED-CAL-09 of the Editorial Guidelines Review): "* **Where Exceptions Appear:** Exception callouts MAY be used only in guideline documents and in non-normative explanation. Requirements MUST express conditions with 'when' or 'unless', as defined in the Normative Requirements Guidelines." -->
* **Not Permitted in Requirements Sections:** Exceptions MUST NOT appear in Requirements sections of the specification. If a condition represents a normative constraint, authors MUST express it explicitly using structured requirement patterns (e.g., "when", "unless") instead.

<!-- ED-CAL-10 -->
<!-- review: In agreement. -->
* **No Blockquote Usage:** Exceptions MUST NOT be expressed using blockquote syntax (which is strictly reserved for Notes).
* **No Header Usage:** Exceptions MUST NOT use Markdown headers (e.g., `#### Exceptions`).

<!-- ED-CAL-11 (absorbs ED-CAL-12) -->
<!-- review(F-31) [Duplicate]: The comment says ED-CAL-12 was absorbed, but its "Consistent Terminology" bullet remains (the same name as under Notes). The parent bullet of the qualifier items does not end with a colon (see ED-LST-03), and the case of `<Topic>` is not stated. A-11 (approved by all three) and A-23 (approved by Joaquin and Matt) apply. Alternative (ED-CAL-11 of the Editorial Guidelines Review, replacing both bullets): "* **Exception Label:** An exception MUST begin with `**Exception:**` for one item or `**Exceptions:**` for a bullet list. No other term (e.g., 'Special Case' or 'Caveat') is allowed. The label MAY add a qualifier `for <Topic>` before the colon (e.g., `**Exception for Nullability:**`), with `<Topic>` in title case:" followed by the three qualifier items as they are. -->
* **Exception Label:** Exceptions MUST begin with the inline label `**Exception[ for <Topic>]:**` or `**Exceptions[ for <Topic>]:**` (the term `Exception` or `Exceptions`, with or without a semantic qualifier `for <Topic>`, followed by a colon, formatted in bold).
  * A semantic qualifier SHOULD be included in Normative Requirements Guidelines to support cross-referencing and automated processing.
  * A semantic qualifier MAY be included in other guidelines.
  * When used, semantic qualifiers SHOULD be applied consistently throughout the document.
* **Consistent Terminology:** Only the term `Exception` or `Exceptions` MUST be used. Variants such as `Special Case`, `Caveat`, or similar terms MUST NOT be used.

<!-- ED-CAL-13 -->
<!-- review(F-32) [Ambiguity]: "Directly associated" cannot be checked, and the SHOULD makes the placement optional. Irena's note on A-11 asks for exceptions immediately after the content they modify; A-11 was approved by all three reviewers. Alternative (ED-CAL-13 of the Editorial Guidelines Review): "* **Exception Placement:** An exception MUST appear immediately after the content it modifies." Open, from the same note: should the rule an exception modifies also point to it? -->
* **Structural Relationship:** Exceptions MUST be directly associated with the content they modify and SHOULD appear immediately after the relevant content.

<!-- ED-CAL-14 -->
<!-- review(F-34) [Ambiguity]: "Single-Line" and "Multi-Line" depend on line wrapping, while the rule is about one exception versus several. A-11 and A-23 apply (A-11 approved by all three; A-23 by Joaquin and Matt). Alternative (ED-CAL-14 of the Editorial Guidelines Review, replacing both bullets): "* **Exception Layout:** A single exception MUST be plain text on the same line as the label. Several exceptions MUST be a bullet list, separated from the label by a blank line." -->
<!-- review(F-33) [Editorial]: The second example below puts the values Adjustment and Tax in backticks, while ED-REF-09 requires double quotes (both reviewers who questioned A-06 confirm double quotes for Allowed Values). Alternative: 'This rule does not apply when ChargeCategory is "Adjustment".' and 'This rule does not apply when ChargeCategory is "Tax".' -->
* **Single-Line Exceptions:** An exception containing a single statement MUST be written as a single line of plain text immediately following the label.
* **Multi-Line Exceptions:** An exception spanning multiple statements MUST be expressed as a bullet list. A blank line MUST separate the label from the bullet list.
* **Example** (Markdown, illustrative):

  ```md
  **Exception:** This is a single-line exception.
  ```

* **Example** (Markdown, illustrative):

  ```md
  **Exceptions:**

  * This rule does not apply when ChargeCategory is `Adjustment`.
  * This rule does not apply when ChargeCategory is `Tax`.
  ```

#### Status Notes

<!-- ED-CAL-21 -->
<!-- review(F-35) [Gap]: The rule does not say which label the status note uses. A-24 and A-37 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-21 of the Editorial Guidelines Review): add "The note uses the `**Note:**` label (ED-CAL-03)." -->
* **Informative Status Note:** Each of the following files MUST include an informative, non-normative status note directly below its first heading:
  * `specification/overview.md`
  * `specification/supported_features/supported_features_overview.md`
  * `specification/appendix/appendix_overview.md`

<!-- ED-CAL-22 -->
<!-- review(F-35) [Gap]: The Conventions section must repeat the headings and exceptions of the notes, but nothing connects the two, so they can drift. A-39 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-CAL-22 of the Editorial Guidelines Review): end the third item with ", and SHOULD link to each note." -->
* **Informative Status Note Scope:**
  * Each note MUST refer only to the section identified by that heading (e.g., "The Appendix").
  * The note MUST NOT be placed under the subheadings of that heading, including a heading originating from a nested file.
  * The Conventions section in `specification/overview.md` MUST identify the same headings and exceptions as the corresponding notes.
* **Example** (Markdown, illustrative):

  ```md
  > **Note:** The Appendix, except the Rounding Variance Tolerance appendix entry, is informative and non-normative. It does not define requirements.
  ```

### Examples

<!-- ED-CAL-15 -->
<!-- review: In agreement. -->
* **Valid Examples:** Examples MUST reflect valid combinations of values defined in the specification.
  > **Note:** Validation of example correctness may require schema, glossary, or domain-specific review beyond editorial validation.

<!-- ED-CAL-16 -->
<!-- review: In agreement. -->
* **No New Terminology:** Examples MUST NOT introduce terminology that is not defined in the specification.
  > **Note:** Validation of terminology consistency may require comparison against the approved glossary and specification entity definitions.

<!-- ED-CAL-20 -->
<!-- review: In agreement. -->
* **Brand-Free Identifiers:** Resource, host, and pod-level identifiers in appendix examples MUST use neutral, brand-free labels (e.g., `host-prod-07`, `pod-orders-01`) rather than labels derived from fictitious customer or data generator names, so that an identifier does not read as an additional, unintended entity in the example.

### Code and JSON

<!-- ED-COD-01 -->
<!-- text from proposal (ED-COD-01); replaces summary table row T7.a (Key-Value Format) and its JSON sample (L130-136) -->
<!-- review(F-36) [Editorial]: "for example," while the other rules in this document use "e.g.," (the ED-REF-09 comment states this convention). Alternative: "(e.g., `json` or `sql`)". -->
* **Fenced Code Blocks:** Code and JSON MUST be in fenced code blocks with a language tag (for example, `json` or `sql`).

<!-- ED-COD-02 (absorbs ED-COD-03) -->
<!-- review(F-37) [Duplicate and Ambiguity]: The comment says ED-COD-03 was absorbed, but both bullets remain; valid JSON already requires double-quoted keys. "Valid and complete" does not say what to do with shortened samples, which the specification uses. A-25, A-32 and A-40 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-COD-02 of the Editorial Guidelines Review, replacing both bullets): "* **Valid JSON:** Every block fenced as `json` MUST parse as valid JSON. A shortened sample that uses `...` or comments MUST use a `text` fence." -->
* **Valid JSON:** JSON examples MUST be valid and complete.
* **JSON Quotation Marks:** JSON keys MUST use double quotation marks.

<!-- ED-COD-04 -->
<!-- review(F-38) [Ambiguity]: "Consistent formatting and indentation" does not say consistent with what. A-25 was approved by Joaquin and Matt; Irena did not vote. Alternative (ED-COD-04 of the Editorial Guidelines Review): "* **JSON Indentation:** JSON MUST be indented with two spaces per level. A block MUST NOT start with a leading offset: the opening `{` or `[` is at the start of the line." Open (A-31, Matt): how indentation is measured; the smallest step between levels can hide uneven indentation (deprecating_columns_example.md, sibling keys at 7 and 17 spaces). This affects the check, not the rule text. -->
* **Consistent Structure:** JSON examples SHOULD follow consistent formatting and indentation.

<!-- ED-COD-05 -->
<!-- ED-COD-05: no working_draft source -->
<!-- review(F-08) [Gap]: Empty placeholder. The build already enforces this rule (specification/tests/test_sql_blocks.py); A-32, A-33 and A-40 were approved by Joaquin and Matt; Irena did not vote. Alternative (ED-COD-05 of the Editorial Guidelines Review): "* **Valid SQL:** Every block fenced as `sql` in `datasets/` and `supported_features/` MUST be valid SQL and MUST reference only FOCUS Column IDs, custom columns (`x_` prefix) or names defined in the query. Use `?` for values the reader supplies." -->

### Tables

<!-- ED-TBL-01 -->
<!-- text and example from proposal (ED-TBL-01); replaces summary table row T8.a (Tables), the note (L149) and the working_draft example (L460-525) -->
<!-- review(F-39) [Editorial]: The example label below is plain text ("Example (HTML, illustrative):"), while every other example in this document is a bullet with a bold label. Alternative: "* **Example** (HTML, illustrative):", with the code fence indented two spaces under it. -->
* **Markdown or HTML:** Tables MUST be written in Markdown. An HTML table MAY be used only when the table needs merged rows or columns, embedded images or multi-line cell content, or another layout that reviewers agree Markdown cannot express reliably.

Example (HTML, illustrative):

```html
<table>
  <tr>
    <th colspan="2">Heading 1</th>
    <th>Heading 2</th>
  </tr>
  <tr>
    <td>Cell 1</td>
    <td>Cell 2</td>
    <td rowspan="2">Cell 3</td>
  </tr>
  <tr>
    <td colspan="2">Cell 4</td>
  </tr>
</table>
```

<!-- ED-TBL-02 -->
<!-- review(F-40) [Ambiguity]: "Maximum row width" is not defined (rendered width, cell content, or the raw Markdown line). Alternative (ED-TBL-02 of the Editorial Guidelines Review): "When the longest raw line of a Markdown table is shorter than 120 characters, the table SHOULD be padded with spaces so the pipes align. When it is 120 characters or longer, the table SHOULD use exactly one space after each value." -->
* **Markdown Table Spacing:**
  * When a markdown table has a maximum row width of less than 120 characters, the table SHOULD be padded with spaces to align the vertical pipes visually.
  * When a markdown table has a maximum row width of 120 characters or more, the table SHOULD use exactly one space after values without additional padding.

## Column Editorial Rules

<!-- review(F-41) [Gap]: This section holds an example but no rules, and, unlike PR #2848 (answers (b) and (c) to question 5 of #2847), it does not say that column rules are not defined yet. Alternative: "Rules specific to column files are not defined yet. Rules that apply to column files are in Core Editorial Rules (e.g., ED-STR-01, ED-LNK-02)." -->

### Column Examples

<!-- review(F-42) [Decision]: A-14 (replace the worked example with a link to specification/datasets/cost_and_usage/columns/pricingquantity.md, and drop the "may not reflect the latest version" note) was approved by Joaquin and Matt; Irena did not vote. PR #2848 instead chose question 7 (b) of #2847: keep a full copy, refreshed from the specification. This document follows #2848. A full copy will drift from the specification (it matches the specification at e9cdcc7 and at working_draft today); the note admits the drift but does not prevent it. Options: (1) link only, as A-14 proposes; (2) keep the copy and name the commit it was taken from in the visible text; (3) keep the copy and add a check that compares it with the specification file. -->

<!-- added: not in proposal; adapted from working_draft note L300 (ED-SCP-04, removed in proposal); "attribute" changed to "column" -->
> **Note:** Authors should consult the actual FOCUS column specification files as the source of truth, as these guidelines do not necessarily reflect the latest version.

#### Pricing Quantity

<!-- added: not in proposal; copy of specification/datasets/cost_and_usage/columns/pricingquantity.md at e9cdcc7; replaces the working_draft worked example (L413-452) -->
```markdown
# Pricing Quantity

The Pricing Quantity represents the volume of a given [*SKU*](#glossary:sku) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#datamodel.costandusage.pricingunit). Distinct from [Consumed Quantity](#datamodel.costandusage.consumedquantity) (complementary to [Consumed Unit](#datamodel.costandusage.consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

## Requirements

PricingQuantity MUST adhere to the following requirements:

* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingQuantity MUST adhere to the following nullability requirements:
  * PricingQuantity MUST be null when [SkuPriceId](#datamodel.costandusage.skupriceid) is null.
  * PricingQuantity MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.

## Usability Constraints

**Aggregation:** When aggregating Pricing Quantity per [SKU ID](#datamodel.costandusage.skuid) for a SKU that includes both [*covering charges*](#glossary:covering-charge) and their [*covered charges*](#glossary:covered-charge), exclude one or the other, based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude *covered charges* when aggregating on a billed basis, or *covering charges* when aggregating on an accrual basis.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)   |
| Operating model conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0-preview
```

<!-- ## Supported Features Editorial Rules -->

<!-- ## Retired Rule IDs (Optional) -->

<!-- ## (Not in Proposal) Not Carried Over -->

<!-- review(F-45) [Open]: It is unclear whether this list, and the commented-out "Retired Rule IDs (Optional)" section, are meant to be published. A-03 is under question: Irena's note prefers no retired-ID inventory (git history is enough), while the Editorial Guidelines Review lists retired IDs so that they are never reused. Decide together with A-03. -->

<!-- ED-SCP-04: Removed in proposal; replaced by the adapted note under Column Examples
working_draft L300:
> **Note:** Authors should consult the actual FOCUS attribute specification files as the source of truth, as these guidelines do not necessarily reflect the latest version.
-->

<!-- review: In agreement. -->
<!-- ED-REF-12: Moved to NRG; circular reference with no content (review: DEF); the NRG lists the keywords but does not state their formatting
working_draft L99:
           * Formatting follows Editorial Guidelines.<br>
-->

<!-- review: In agreement. -->
<!-- ED-LST-06: Moved to NRG; covered by NRG Structural Anchor
working_draft L233-241:
* **Structural Anchors:** Normative bullet lists MUST be preceded by a structural anchor. See [Normative Requirements Guidelines](normative-requirements-guidelines.md#structural-anchor) for details.

> **Note:** Validation of structural anchors may require contextual editorial judgment and is not always suitable for deterministic editorial validation.

* **Example** (Markdown, illustrative):

  ```md
  ... MUST adhere to the following requirements:
  ```
-->

<!-- review(F-43) [Gap]: The entry below says that the consistency of nested introductory phrases is not covered by the NRG. Moving the rule to the NRG therefore drops that part from both documents. Alternative: keep the uncovered part in this document, or record it for the NRG review that A-05 and ADR 0002 plan. -->
<!-- ED-LST-07: Moved to NRG; the anchor phrase is covered by the NRG canonical form; consistency of nested introductory phrases is not covered
working_draft L243-245:
* **Consistent Introductory Phrases:** Introductory phrases for normative lists SHOULD be consistent within a section.

> **Note:** Authors SHOULD prefer stable introductory patterns such as "... MUST adhere to the following requirements:" within the same section unless contextual variation improves readability.
-->

<!-- review: In agreement. -->

<!-- review(F-44) [Traceability]: ED-CAL-18 is the only rule ID of the Editorial Guidelines Review not mentioned in this document. Alternative: add an entry such as "ED-CAL-18: Removed in proposal; not in working_draft at e9cdcc7 (PR #2775 removed the Example Note Requirement, L294-300 at f1eeb30a7). Status notes are covered by ED-CAL-21 and ED-CAL-22." -->

<!-- ED-CAL-19: Removed in proposal; conflicts with the note label rules (ED-CAL-03); its currency rule is ED-WRD-07
working_draft L121-122:
        <td>> Important Consideration</td>
        <td>* It is added as a note.</td>
working_draft L407:
### Important Text
-->
