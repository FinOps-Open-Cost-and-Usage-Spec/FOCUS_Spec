# [AI] Tag plain Display Names, quoted values, and file datasets with the inference rules

## Action Item Details

**Parent Issue:** #2779

**Depends on:** AI #<translations>

**Detailed Description**

After the translations, many references are still plain text. Today's markup doesn't identify them, but their context does: Display Names written as plain words, quoted allowed values, and ColumnIds that several datasets define, in files with no dataset of their own. This AI runs the inference rules approved in AI #<rules> over the files converted in AI #<translations>. Rules the Working Group didn't approve stay off.

The inferences are kept apart from the translations because a wrong inference, once merged, looks like a deliberate choice. A translation only carries over what the markup already said. Each rule is therefore reviewed by its own evidence, not line by line.

Counts are on top of the translations, for `working_draft_interim` at `12770c1a`:

| Rule | Tags | Files | What the PR lists for review |
| :--- | ---: | ---: | :--- |
| Plain Display Names | 866 (674 `col`, 91 `ds`, 50 `meta`, 30 `omc`, 12 `schema`, 8 `attr`, 1 `obj`) | 231 | Each tagged phrase with its count and entity, so the reviewer checks phrases, not lines |
| Values after a column reference | 157 | 53 | Each value tag, grouped by column |
| Values of the file's own column | 67 | 15 | Each value tag, grouped by column |
| File dataset | 166 more `col` tags, from `dataset:` front matter in 56 files | 56 | Each file, its inferred dataset, and the columns that decided it |

* The two value rules overlap and together make 199 value tags. Each file that gets one lists `val: mechanical` in its `semantic:` front matter.
* The file dataset rule leaves 56 of the 223 shared ColumnIds without a dataset. These are in files that mix datasets, such as `rate_optimization_and_contract_evaluation.md` (15) and `price_effectivity_and_currency.md` (13).
* The rendered comparison can't verify an inferred dataset, because the ColumnIds it resolves were plain text before. Each of the 56 is confirmed by a reviewer for its area, or removed.
* With all four rules on, the published `spec.md` differs from the base on 812 lines, compared with 689 after the translations alone. No visible word changes: 450 links are added and 213 removed in all. FOCUS004 then reports 55 untagged ColumnIds, which the semantic review resolves.
* Each rule is a separate commit, so one can be reverted without the others.

The semantic review, which moves kinds from `mechanical` to `reviewed` file by file, is planned as later AIs under FR #2779.

**Definition of Done**

* [ ] Only the inference rules approved in AI #<rules> are switched on, and they have been run on the files in the scope of AI #<translations>.
* [ ] The PR lists the review evidence for each rule, as shown in the table above.
* [ ] Every inferred `dataset:` is confirmed by a reviewer for its area, or removed.
* [ ] Rerunning the converter changes nothing, which CI checks, and the build passes with 0 errors.
* [ ] The PR includes the rendered comparison against its base, and no visible word changed.
* [ ] The PR lists the items still open, for the semantic review.
* [ ] The PR is merged into the branch that 1.6 work targets at that time.
