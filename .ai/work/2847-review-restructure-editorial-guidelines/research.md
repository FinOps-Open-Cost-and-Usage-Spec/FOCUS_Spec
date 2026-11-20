# Research: Review of the Editorial Guidelines Restructuring, Step 1

## Purpose

This review checks `supporting_content/guidelines/contributors/editorial-guidelines-restructuring-step-1.md` (Irena Jurica, added to PR #2848 on 17-18 November 2026) for gaps, ambiguities and points open to interpretation. The changes are proposed as a PR stacked on Irena's branch `2847-restructure-editorial-guidelines-and-agents-md` (PR #2848, base `working_draft_interim`).

## Sources

* **Under review:** the step-1 document at `82996ef2` (head of PR #2848 when this review started).
* **Reference:** the "Editorial Guidelines Review" artifact (Joaquin Prado; `grill-with-docs` output): 78 rule IDs reduced to 60 proposed rules in 10 categories, assumptions A-01 to A-42, reviewed against `guidelines/contributors/editorial-guidelines.md` at `e9cdcc7`.
* **Member verdicts** recorded in the artifact (as of 20 November 2026): Joaquin, Matt (F2) and Irena.
* **PR #2848 description:** assumed answers to questions 1-11 of issue #2847, and its Follow-ups list.

## How Findings Were Judged

Irena is the editor of this document; this review supports her. The review therefore adds HTML comments only and changes none of her lines: `git diff 82996ef2` on the step-1 document shows added lines only, all of them comments or blank lines. The Review's wording is offered as an alternative, never applied.

| Situation | Comment added next to the rule |
| :-------- | :----------------------------- |
| No issue found | `<!-- review: In agreement. -->` (18 places) |
| Gap, ambiguity, conflict, duplicate or self-violation | `review(F-xx) [Type]`: the problem, the verdict status of the assumption behind it, and an Alternative (usually the Review's wording) |
| Assumption under question by a reviewer | `review(F-xx) [Open]`: the question and who raised it; no wording imposed |
| Already in the Follow-ups of PR #2848 | Raised only where a step-1 comment claims a merge that the text does not make |

Verdict status is stated exactly in each comment: "approved by all three reviewers" only for A-02, A-05, A-11 and A-12; otherwise, e.g., "approved by Joaquin and Matt; Irena did not vote".

## Member Verdicts

* **Approved by all who voted:** A-01, A-02, A-05, A-07 to A-15, A-17, A-19, A-21 to A-28, A-30, A-32 to A-35, A-37 to A-42. Irena voted on A-02, A-05, A-11 and A-12 (all Approve) and did not vote on the others.
* **Under question:** A-03 (Irena, Matt), A-04 (Irena, Matt), A-06 (Irena, Matt), A-16 (Matt; Joaquin changed Reject to Approve on 20 November 2026, see F-14), A-18 (Irena, Matt), A-20 (Irena, Matt), A-29 (Matt), A-31 (Matt), A-36 (Matt).
* **Notes that shape the step-1 document:**
  * Irena on A-02 proposed the exact heading structure the step-1 document uses.
  * Irena on A-03 prefers readable PascalCase IDs and no retired-ID inventory; this explains why IDs appear only in HTML comments and why "Retired Rule IDs" is marked optional.
  * Irena on A-04 and A-05: guideline documents need more exceptions than ED-STR-03 (linking); one authoritative location per rule; a rule should point to its exceptions.
  * Matt on A-08: the carve-outs should cover every ID declaration section (Dataset ID, Object ID).

## Finding for Joaquin (Not in the Step-1 Document)

* **F-14, A-16 verdict (resolved 20 November 2026):** Joaquin's verdict on A-16 was Reject, recorded against the first version of A-16 (later mentions in plain text), while the note asked for italics. A-16 was then reversed to italics, so the recorded Reject contradicted his position, and Matt asked him to clarify. The verdict is now Approve, with a note explaining that the Reject applied to the earlier version and answering Matt. Still open: Matt's request (verdict Question) for a pilot on one dataset before the follow-up spec work is sized.

## Out of Scope (Recorded for Follow-Up)

* NRG L1060 teaches "MUST equal" in its patterns and needs the same change as ED-WRD-01 (Matt, A-10).
* `pricingunit.md` lines 16-17 say "MUST be semantically equal", which ED-WRD-05 forbids (Irena and Matt, A-18).
* NRG "Column Requirement Standardized Terminology" may overlap ED-WRD-01 to ED-WRD-05 (A-05, open for the NRG review).
* Mixed fence tags in the step-1 document examples (`md` and `markdown`); not a rule violation, left as is.

## Findings

Severity: **High** = a contradiction, or a rule whose meaning is lost or changed; **Medium** = an ambiguity or a gap that leaves a rule open; **Low** = editorial.

Action (all findings are comments; no text of Irena's is changed): **Alternative** = the comment proposes replacement wording; **Options** = the comment lists options for a decision; **Question** = the comment records an open question without wording.

In agreement (no finding): ED-SCP-02, ED-SCP-05, ED-REF-11, ED-REF-13, ED-LNK-02, ED-LNK-03, ED-WRD-02, ED-PUN-01, ED-LST-01, ED-CAL-01, ED-CAL-08, ED-CAL-10, ED-CAL-15, ED-CAL-16, ED-CAL-20, and the "Not Carried Over" entries ED-REF-12, ED-LST-06 and ED-CAL-19.

| ID   | Category          | Severity | Rule IDs                    | Basis                     | Action  | Summary |
| :--- | :---------------- | :------- | :-------------------------- | :------------------------ | :------ | :------ |
| F-00 | Purpose           | High     | All                         | User direction            | Alternative | The document does not state its purpose, status, relation to PR #2848 or next step; a status block is suggested |
| F-01 | Traceability      | Medium   | All                         | -                         | Alternative | "working_draft L###" references have no commit; they match `e9cdcc7` (verified: L99, L153, L185, L300, L413, L460) |
| F-02 | Self-violation    | Low      | ED-PUN-04, ED-PUN-05        | A-21 approved             | Alternative | Em dashes in the introduction break ED-PUN-05; alternative uses spaced hyphens |
| F-03 | Gap               | Medium   | -                           | A-03 open, A-12 approved  | Question | "How to Read These Rules" is empty; content it needs is listed (keywords, IDs, lint verdicts, examples) |
| F-04 | Gap, merge        | High     | ED-SCP-01, ED-REF-05        | A-05 approved by all      | Alternative | The boundary between this guideline and the NRG is not stated; ED-REF-05 bullet still separate although "absorbed" |
| F-05 | Gap               | Medium   | ED-SCP-03                   | A-04 open                 | Alternative | No statement of which files the rules cover; interim note offered, as Irena and Matt suggest |
| F-06 | Ambiguity         | High     | ED-STR-01, ED-STR-02        | A-13, A-28 approved       | Alternative | Illustrative order contradicts the document's own column example; canonical order offered |
| F-07 | Merge not made    | High     | ED-STR-03, ED-STR-04        | A-27, A-34 approved       | Alternative | Two bullets state one rule; Requirements section undefined; ED-CAL-17 bullet can stay (A-36 open) |
| F-08 | Gap               | Medium   | ED-STR-05, ED-STR-06, ED-LNK-04, ED-PUN-06, ED-COD-05 | A-32, A-33, A-40 approved | Alternative | Empty placeholders for rules the build already enforces; rule text offered |
| F-09 | Merge not made    | Medium   | ED-REF-01, ED-REF-02, ED-REF-03 | Proposal; A-08 note  | Alternative | Three bullets remain, "schema" undefined; one rule offered; plural-ID question left open |
| F-10 | Ambiguity         | Medium   | ED-REF-04                   | A-15 approved             | Alternative | Unclear whether IDs in code spans and code blocks count; exemption offered |
| F-11 | Merge not made    | High     | ED-REF-06, ED-REF-07        | A-08 approved             | Alternative | MUST and SHOULD both remain; one rule with carve-outs for every ID section offered |
| F-12 | Ambiguity         | Medium   | ED-REF-08                   | A-13 approved             | Alternative | "Normal text conventions" does not say which spelling is correct |
| F-13 | Open question     | Medium   | ED-REF-09                   | A-06 open                 | Question | Scope by value type (strings, numbers, booleans, null, samples, tables) not decided |
| F-15 | Gap               | High     | ED-LNK-01                   | A-07, A-17 approved       | Alternative | First occurrence is not required to be linked; edge cases and a pointer to the exceptions offered |
| F-16 | Conflict          | High     | ED-WRD-01, ED-WRD-03        | A-10 approved             | Alternative | `BilledCost MUST be 0` fits both rules; examples use backtick values |
| F-17 | Ambiguity         | Low      | ED-WRD-04                   | A-35 approved             | Alternative | Forms to avoid ("at least", `>=`) are not named |
| F-18 | Open question     | Medium   | ED-WRD-05                   | A-18 open                 | Alternative | "semantically" question; the example misquotes pricingunit.md |
| F-19 | Ambiguity         | Medium   | ED-WRD-06                   | A-19, A-22 approved       | Alternative | "DOES NOT", label colon, nested exception, incomplete numeral cases |
| F-20 | Open question     | Medium   | ED-WRD-07                   | A-20 open                 | Question | Scope versus column values, `$` for USD only, symbols versus ISO codes |
| F-21 | Self-violation    | Low      | ED-PUN-02                   | A-22 approved             | Alternative | Label suggests Markdown lists; example nested under a parent without a colon |
| F-22 | Strength, conflict | Medium  | ED-PUN-03, ED-PUN-04, ED-PUN-05 | A-21, A-08 approved   | Alternative | SHOULD NOT weaker than A-21; example uses an Entity ID in prose |
| F-23 | Merge not made    | Low      | ED-LST-02, ED-LST-04, ED-LST-05 | Proposal              | Alternative | Three bullets with one rule; typo; one-level example does not illustrate indentation |
| F-24 | Ambiguity         | High     | ED-LST-03                   | A-22, A-05 approved       | Alternative | Nesting rule contradicted by the document itself; formatting-only rule offered, nesting left to the NRG |
| F-25 | Duplication       | Low      | ED-LST-08                   | Proposal                  | Alternative | Two bullets with one rule |
| F-26 | Gap               | Low      | ED-CAL-02                   | A-09, A-14 approved       | Alternative | Blockquotes reserved for notes only implied in ED-CAL-10 |
| F-27 | Merge not made    | Medium   | ED-CAL-03, ED-CAL-04        | A-09, A-23 approved       | Alternative | Duplicate rule name "Consistent Terminology"; when to use Note versus Notes |
| F-28 | Ambiguity         | Medium   | ED-CAL-05                   | A-34 approved             | Alternative | "Discussing" keywords could allow a requirement in a note |
| F-29 | Ambiguity         | Medium   | ED-CAL-06, ED-CAL-07        | A-23 approved             | Alternative | Line-based note rules depend on wrapping; item-based rules offered |
| F-30 | Gap               | Medium   | ED-CAL-09                   | A-11 approved by all      | Alternative | Only where exceptions may not appear is stated; condition starts with "If" |
| F-31 | Merge not made    | Medium   | ED-CAL-11, ED-CAL-12        | A-11, A-23 approved       | Alternative | Duplicate rule name; parent bullet without colon; Topic in title case |
| F-32 | Ambiguity         | Medium   | ED-CAL-13                   | A-11 approved by all      | Alternative | "Directly associated" not checkable; placement only SHOULD; open: should a rule point to its exceptions |
| F-33 | Self-violation    | Medium   | ED-CAL-14, ED-REF-09        | A-06 (Allowed Values agreed) | Alternative | Example values in backticks |
| F-34 | Ambiguity         | Medium   | ED-CAL-14                   | A-11, A-23 approved       | Alternative | Line-based exception layout depends on wrapping; count-based rule offered |
| F-35 | Gap               | Low      | ED-CAL-21, ED-CAL-22        | A-39 approved             | Alternative | Note label not stated; nothing connects the Conventions section to the notes |
| F-36 | Editorial         | Low      | ED-COD-01                   | Document convention       | Alternative | "for example" where the document uses "e.g." |
| F-37 | Merge not made    | Medium   | ED-COD-02, ED-COD-03        | A-25, A-32, A-40 approved | Alternative | Two bullets remain; "valid and complete" does not cover shortened samples |
| F-38 | Ambiguity         | Low      | ED-COD-04                   | A-25 approved; A-31 open  | Alternative | "Consistent" not defined; measuring left open (A-31) |
| F-39 | Editorial         | Low      | ED-TBL-01                   | Document convention       | Alternative | Example label is plain text, unlike every other example |
| F-40 | Ambiguity         | Low      | ED-TBL-02                   | Proposal                  | Alternative | "Maximum row width" not defined |
| F-41 | Gap               | Low      | -                           | #2847 question 5          | Alternative | Column Editorial Rules has no rules and no status sentence |
| F-42 | Decision          | High     | ED-SCP-04                   | A-14 approved vs #2848 question 7 (b) | Options | Full copy of the column example will drift; three options listed |
| F-43 | Gap               | Medium   | ED-LST-07                   | A-05                      | Alternative | Part of the rule is covered by neither document after the move |
| F-44 | Traceability      | Low      | ED-CAL-18                   | A-24                      | Alternative | The only rule ID not mentioned; an entry is offered |
| F-45 | Open question     | Low      | Retired IDs                 | A-03 open                 | Question | Whether "Not Carried Over" and "Retired Rule IDs" are published |

## Traceability Matrix

State of each rule ID in the step-1 document (unchanged by this review), and the finding that comments on it. "WD" = text kept from `working_draft` at `e9cdcc7`; "Proposal" = text of the Editorial Guidelines Review; "OK" = no finding.

| Rule ID   | Review status | Step-1 state before review                 | Finding |
| :-------- | :------------ | :----------------------------------------- | :------ |
| ED-SCP-01 | Proposed      | WD text; ED-REF-05 bullet kept             | F-04    |
| ED-SCP-02 | Proposed      | Proposal                                   | OK      |
| ED-SCP-03 | Proposed      | WD text (entity scope only)                | F-05    |
| ED-SCP-04 | Removed       | Adapted note kept under Column Examples    | F-42    |
| ED-SCP-05 | Proposed      | WD text                                    | OK      |
| ED-STR-01 | Proposed      | WD text (SHOULD, illustrative order)       | F-06    |
| ED-STR-02 | Proposed      | WD text                                    | F-06    |
| ED-STR-03 | Proposed      | WD text, two bullets                       | F-07    |
| ED-STR-04 | Merged        | Claimed absorbed; bullet remained          | F-07    |
| ED-STR-05 | Proposed      | Empty placeholder                          | F-08    |
| ED-STR-06 | Proposed      | Empty placeholder                          | F-08    |
| ED-REF-01 | Merged        | Claimed absorbed; kept as "Entity ID Case" | F-09    |
| ED-REF-02 | Merged        | Claimed absorbed; bullet remained          | F-09    |
| ED-REF-03 | Proposed      | WD text                                    | F-09    |
| ED-REF-04 | Proposed      | Adapted proposal (code exemption dropped)  | F-10    |
| ED-REF-05 | Merged        | Claimed absorbed; bullet remained          | F-04    |
| ED-REF-06 | Proposed      | WD text (MUST)                             | F-11    |
| ED-REF-07 | Merged        | Claimed absorbed; SHOULD bullet remained   | F-11    |
| ED-REF-08 | Proposed      | WD text (SHOULD)                           | F-12    |
| ED-REF-09 | Proposed      | Adapted proposal                           | F-13    |
| ED-REF-10 | Merged        | Absorbed                                   | OK      |
| ED-REF-11 | Proposed      | Proposal                                   | OK      |
| ED-REF-12 | Moved         | Listed as not carried over                 | OK      |
| ED-REF-13 | Proposed      | Proposal                                   | F-14    |
| ED-LNK-01 | Proposed      | WD text plus added link-target bullets     | F-15    |
| ED-LNK-02 | Proposed      | WD text                                    | OK      |
| ED-LNK-03 | Proposed      | WD text                                    | OK      |
| ED-LNK-04 | Proposed      | Empty placeholder                          | F-08    |
| ED-WRD-01 | Proposed      | WD text                                    | F-16    |
| ED-WRD-02 | Proposed      | WD text                                    | OK      |
| ED-WRD-03 | Proposed      | WD text (backtick values)                  | F-16    |
| ED-WRD-04 | Proposed      | WD text                                    | F-17    |
| ED-WRD-05 | Proposed      | WD text                                    | F-18    |
| ED-WRD-06 | Proposed      | WD text                                    | F-19    |
| ED-WRD-07 | Proposed      | WD text                                    | F-20    |
| ED-PUN-01 | Proposed      | WD text                                    | OK      |
| ED-PUN-02 | Proposed      | WD text                                    | F-21    |
| ED-PUN-03 | Proposed      | WD text                                    | F-22    |
| ED-PUN-04 | Proposed      | WD text (Entity ID in example)             | F-22    |
| ED-PUN-05 | Proposed      | WD text (SHOULD NOT)                       | F-22    |
| ED-PUN-06 | Proposed      | Empty placeholder                          | F-08    |
| ED-LST-01 | Proposed      | WD text                                    | OK      |
| ED-LST-02 | Proposed      | WD text, three bullets                     | F-23    |
| ED-LST-03 | Proposed      | WD text                                    | F-24    |
| ED-LST-04 | Merged        | Claimed absorbed; bullet remained          | F-23    |
| ED-LST-05 | Merged        | Claimed absorbed; bullet remained          | F-23    |
| ED-LST-06 | Moved         | Listed as not carried over                 | OK      |
| ED-LST-07 | Moved         | Listed as not carried over; partly uncovered | F-43  |
| ED-LST-08 | Proposed      | WD text, two bullets                       | F-25    |
| ED-CAL-01 | Proposed      | WD text                                    | OK      |
| ED-CAL-02 | Proposed      | WD text                                    | F-26    |
| ED-CAL-03 | Proposed      | WD text                                    | F-27    |
| ED-CAL-04 | Merged        | Claimed absorbed; bullet remained          | F-27    |
| ED-CAL-05 | Proposed      | WD text plus note                          | F-28    |
| ED-CAL-06 | Proposed      | WD text                                    | F-29    |
| ED-CAL-07 | Proposed      | WD text                                    | F-29    |
| ED-CAL-08 | Proposed      | WD text                                    | OK      |
| ED-CAL-09 | Proposed      | WD text                                    | F-30    |
| ED-CAL-10 | Proposed      | WD text                                    | OK      |
| ED-CAL-11 | Proposed      | WD text                                    | F-31    |
| ED-CAL-12 | Merged        | Claimed absorbed; bullet remained          | F-31    |
| ED-CAL-13 | Proposed      | WD text                                    | F-32    |
| ED-CAL-14 | Proposed      | WD text (backtick values in example)       | F-33, F-34 |
| ED-CAL-15 | Proposed      | WD text                                    | OK      |
| ED-CAL-16 | Proposed      | WD text                                    | OK      |
| ED-CAL-17 | Merged        | Claimed absorbed; bullet kept              | F-07 (A-36 open) |
| ED-CAL-18 | Removed       | Not mentioned                              | F-44    |
| ED-CAL-19 | Removed       | Listed as not carried over                 | OK      |
| ED-CAL-20 | Proposed      | WD text                                    | OK      |
| ED-CAL-21 | Proposed      | WD text                                    | F-35    |
| ED-CAL-22 | Proposed      | WD text                                    | F-35    |
| ED-COD-01 | Proposed      | Proposal                                   | F-36    |
| ED-COD-02 | Proposed      | WD text, two bullets                       | F-37    |
| ED-COD-03 | Merged        | Claimed absorbed; bullet remained          | F-37    |
| ED-COD-04 | Proposed      | WD text                                    | F-38    |
| ED-COD-05 | Proposed      | Empty placeholder                          | F-08    |
| ED-TBL-01 | Proposed      | Proposal                                   | F-39    |
| ED-TBL-02 | Proposed      | WD text                                    | F-40    |

## Verification

* `git diff 82996ef2` on the step-1 document: 78 lines added, 0 removed; every added line is an HTML comment or blank.
* Every rule ID of the Review appears in the step-1 document; no unknown IDs.
* All 155 HTML comments are closed and contain no `--`; the review comments contain no non-ASCII characters.
* `python3 -m pymarkdown --config markdownlnt.cfg scan` (run from `specification/`, with the custom rules MD990 and MD991) passes on the step-1 document. It is under `supporting_content/` and is not part of the build.
* The comments were inserted by a script keyed on Irena's own lines (each anchor unique), so no wording of hers could drift.
