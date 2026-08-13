#!/usr/bin/env node
'use strict';

/**
 * Requirements Model extractor.
 *
 * Generates Requirements Model JSON from FOCUS specification markdown, driven by
 * `requirements_model_contract.json`. Markdown is parsed into an AST (via the
 * `marked` lexer) and the nested bullet list under each entity's `## Requirements`
 * heading is expanded into a rule family (a root composite, sub-composites, and a
 * rule per leaf bullet).
 *
 * Entity scope: DataModel (data_model.md), Datasets (<dataset>/dataset.md), and
 * Columns (<dataset>/columns/*.md). Each entity is written to its own file,
 * mirroring the releases/<v>/model_rules/ tree, under ./output/model_rules/.
 *
 * Rule IDs are <DatasetType>-<ArtifactName>-<ArtifactType>-<NumericId>-<Status>
 * for dataset-scoped entities (DatasetType prefix from the contract's DatasetTypes
 * map) and <ArtifactName>-<ArtifactType>-<NumericId>-<Status> otherwise (e.g. the
 * data model). IDs are STABLE: existing IDs are read from the baseline model in
 * releases/latest and reused when a derived rule's MustSatisfy exactly matches an Active
 * baseline rule; anything else (no match, or a match against only a non-Active baseline
 * rule) takes the next free NumericId as a new rule; baseline rules absent from the
 * markdown are tombstoned (Status "Removed"). Status (M/O/C) is derived from the keyword
 * and conditional phrasing.
 *
 * Leaf classification: composites become an AND over their children; "MUST include"
 * becomes a presence rule (ColumnPresent for datasets); leaves whose sentence matches
 * the per-release check-function lookup get a populated domain Requirement
 * (Type/Format/Nullability/...); "MUST conform to <Attr>" leaves link the attribute
 * via Dependencies; any remaining leaf is emitted with an empty Requirement, and is
 * recorded as a warning so the lookup can be extended unless it reused an Active previous
 * rule that was itself curated as Dynamic, in which case it is accepted as-is.
 * A populated Requirement is Static, an empty one Dynamic.
 * Conditions are resolved from `#conditions.<anchor>`
 * links to their Condition IDs.
 */

const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
const { renderInline, normalizeHeading, datasetJsonName, resolveDatasetFolders, renameConditions } = require('./markdown_util');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..');
const RELEASES_DIR = path.join(__dirname, '..', 'releases');
const CONTRACT_PATH = path.join(__dirname, 'requirements_model_contract.json');
const OUTPUT_ROOT = path.join(__dirname, 'output', 'model_rules');

// The baseline is always the `latest` release directory: extraction compares the current
// branch's markdown against the most recently published model, so corrections made there are
// picked up without touching this file. BASELINE_DIR overrides it for a one-off diff against
// an older release (e.g. BASELINE_DIR=1.4).
const BASELINE_DIR = process.env.BASELINE_DIR || 'latest';

// Version labels, resolved from the baseline's model_details.json in main(). PREVIOUS_VERSION
// is for reporting only; NEW_VERSION is stamped into ModelVersionIntroduced/Removed. The
// branch is the working draft of the version `latest` holds, so both resolve to it and new
// rules are introduced in the version being drafted. NEW_VERSION overrides for a version bump.
let PREVIOUS_VERSION = BASELINE_DIR;
let NEW_VERSION = process.env.NEW_VERSION || BASELINE_DIR;

// Ordered so multi-word variants win over their prefixes (e.g. "MUST NOT" before "MUST").
const BCP14_KEYWORD = /\b(MUST NOT|MUST|SHALL NOT|SHALL|SHOULD NOT|SHOULD|MAY)\b/;
// A presence bullet names one column after the keyword; the obligation strength (MUST /
// SHOULD / MAY) is carried by the rule's Keyword and Rule-ID status letter, not by whether
// it is a presence rule at all. The capture requires a PascalCase identifier so that prose
// "include" sentences (e.g. "MUST include custom columns", "MUST include separate charges",
// "MUST include all tag keys") are not read as a column name; those fall through to the
// unclassified path. Link text renders to the bare id, so "[Tags](#...)" matches.
const INCLUDE_RE = /\b(?:MUST|SHOULD|MAY) include ([A-Z]\w*)\b/;
const CONFORM_RE = /MUST conform to (\w+) requirements/;
const CONDITIONAL_RE = /\bwhen\b/;

// Loaded once in main(): the per-release sentence -> check-function lookup, the
// condition anchor -> ConditionId map, and a dedup'd set of unmapped sentences.
let CHECK_LOOKUP = {};
let CONDITIONS = {};
const WARNINGS = [];
// Leaves with no derivable check function that matched an Active baseline rule already
// curated as Dynamic: accepted, not warned about, but counted so the tally stays visible.
const ACCEPTED_DYNAMIC = [];
// Baseline rules introduced in NEW_VERSION and no longer in the markdown: dropped from the
// output rather than tombstoned, and reported because the baseline copy needs deleting.
const UNPUBLISHED_REMOVALS = [];
// Rules whose baseline Order sits at or below the preceding rule's, so the baseline disagrees
// with the markdown about where they belong. Renumbered here and reported.
const ORDER_CONFLICTS = [];
const EMITTED = []; // { outPath, rules } per file, written after the carry-forward post-pass

// ---------------------------------------------------------------------------
// Text / id helpers
// ---------------------------------------------------------------------------

/** Split a PascalCase id into a spaced Display Name (e.g. "BillingPeriodEnd" -> "Billing Period End"). */
function pascalToDisplay(id) {
  return id
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2');
}

/** Map a BCP-14 keyword to a Rule-ID status letter (M=Mandatory, O=Optional, C=Conditional). */
function statusLetter(keyword, hasCondition) {
  if (hasCondition) return 'C';
  if (keyword === 'SHOULD' || keyword === 'SHOULD NOT' || keyword === 'MAY') return 'O';
  return 'M';
}

/** Build a Rule ID. `ctx.idPrefix` (DatasetType for datasets/columns, "ATT" for attributes) is optional. */
function buildRuleId(ctx, numericId, status) {
  const padded = String(numericId).padStart(3, '0');
  const prefix = ctx.idPrefix ? `${ctx.idPrefix}-` : '';
  return `${prefix}${ctx.artifactName}-${ctx.artifactType}-${padded}-${status}`;
}

/** Parse the NumericId out of a Rule ID (e.g. "BIP-BillingPeriod-D-004-M" -> 4). */
function numericIdOf(ruleId) {
  const m = ruleId.match(/-(\d+)-[A-Z]$/);
  return m ? parseInt(m[1], 10) : -1;
}

/**
 * Normalize MustSatisfy text for cross-version matching: strip inline-code backticks
 * (the extractor emits plain text, but older baselines stored the markdown backticks),
 * then trim and collapse whitespace. Applied to both sides of a comparison, so it only
 * affects ID reuse, never the stored MustSatisfy value.
 */
function normalizeMustSatisfy(text) {
  return text.replace(/`/g, '').trim().replace(/\s+/g, ' ');
}

/**
 * Every ModelRuleId named inside a Requirement or Condition, in traversal order. Nested
 * CheckModelRule entries (an AND whose Items are themselves composites) are included.
 */
function modelRuleRefs(value) {
  const out = [];
  (function rec(v) {
    if (Array.isArray(v)) return v.forEach(rec);
    if (!v || typeof v !== 'object') return;
    for (const k of Object.keys(v)) {
      if (k === 'ModelRuleId' && typeof v[k] === 'string') out.push(v[k]);
      else rec(v[k]);
    }
  })(value);
  return out;
}

// ---------------------------------------------------------------------------
// Markdown parsing
// ---------------------------------------------------------------------------

/** Body tokens of the H2 section introduced by `headingText`. */
function getSectionTokens(tokens, headingText, depth = 2) {
  const start = tokens.findIndex(
    (t) => t.type === 'heading' && t.depth === depth && normalizeHeading(t.text) === headingText
  );
  if (start === -1) throw new Error(`Heading not found: "${headingText}" (depth ${depth})`);
  const body = [];
  for (let i = start + 1; i < tokens.length; i++) {
    if (tokens[i].type === 'heading' && tokens[i].depth <= depth) break;
    body.push(tokens[i]);
  }
  return body;
}

/** Whether an H2 section with the given heading text exists (used to skip overview files). */
function hasSection(tokens, headingText, depth = 2) {
  return tokens.some((t) => t.type === 'heading' && t.depth === depth && normalizeHeading(t.text) === headingText);
}

/** Plain text of the first paragraph token in a section (a simple-value or anchor line). */
function getSectionText(tokens, headingText, depth = 2) {
  const paragraph = getSectionTokens(tokens, headingText, depth).find((t) => t.type === 'paragraph');
  if (!paragraph) throw new Error(`No paragraph found in section "${headingText}"`);
  return renderInline(paragraph.tokens);
}

/** Collect condition anchors from inline tokens (links whose href is "#conditions.<anchor>"). */
function conditionAnchorsOf(tokens) {
  const out = [];
  for (const t of tokens || []) {
    if (t.type === 'link' && t.href) {
      const m = t.href.match(/^#conditions\.(.+)$/);
      if (m) out.push(m[1]);
    }
    if (t.tokens) out.push(...conditionAnchorsOf(t.tokens));
  }
  return out;
}

/** Parse a `list` token's items into a tree of { text, children, conditionAnchors }. */
function parseListItems(listToken) {
  return listToken.items.map((item) => {
    const textToken = item.tokens.find((t) => t.type === 'text');
    const subList = item.tokens.find((t) => t.type === 'list');
    return {
      text: textToken ? renderInline(textToken.tokens) : '',
      conditionAnchors: textToken ? conditionAnchorsOf(textToken.tokens) : [],
      children: subList ? parseListItems(subList) : [],
    };
  });
}

/** Build the requirement tree for an entity: a root composite over its top-level bullets. */
function parseRequirementTree(tokens, requirementsHeading) {
  const body = getSectionTokens(tokens, requirementsHeading);
  const anchor = body.find((t) => t.type === 'paragraph');
  const list = body.find((t) => t.type === 'list');
  if (!anchor || !list) throw new Error('Requirements section missing anchor paragraph or bullet list.');
  return { text: renderInline(anchor.tokens), conditionAnchors: conditionAnchorsOf(anchor.tokens), children: parseListItems(list) };
}

/** Flatten a requirement tree into a pre-order array of { node, text, childIdx[] } specs. */
function flattenTree(root) {
  const specs = [];
  (function visit(node) {
    const idx = specs.length;
    specs.push({ node, text: node.text, childIdx: [] });
    for (const child of node.children) specs[idx].childIdx.push(visit(child));
    return idx;
  })(root);
  return specs;
}

// ---------------------------------------------------------------------------
// Rule construction
// ---------------------------------------------------------------------------

/** Resolve a sentence against the check-function lookup; null when unmapped. */
function checkFunctionFor(text, artifactName) {
  const norm = text.split(artifactName).join('{entity}');
  const entry = CHECK_LOOKUP[norm];
  if (!entry) return null;
  const requirement = JSON.parse(JSON.stringify(entry.requirement).split('{entity}').join(artifactName));
  return { Function: entry.function, Requirement: requirement };
}

/**
 * Classify a requirement node into Function / Reference / Requirement / Dependencies.
 * Type is derived later from whether Requirement is populated. Leaf order matters:
 * composite -> include -> check-function lookup -> attribute conformance -> unclassified.
 */
function classify(node, childKeys, ctx) {
  if (node.children.length) {
    return {
      Function: 'Composite',
      Reference: ctx.artifactName,
      Requirement: {
        CheckFunction: 'AND',
        Items: childKeys.map((k) => ({ CheckFunction: 'CheckModelRule', ModelRuleId: k })),
      },
      Dependencies: childKeys.slice(),
    };
  }
  const include = node.text.match(INCLUDE_RE);
  if (include) {
    // Datasets check column presence; the data model includes datasets (generic for now).
    const requirement = ctx.entityType === 'Dataset' ? { CheckFunction: 'ColumnPresent', ColumnName: include[1] } : {};
    return { Function: 'Presence', Reference: include[1], Requirement: requirement, Dependencies: [] };
  }
  // Check-function lookup (covers type/format/nullability leaves, incl. format conformance).
  const looked = checkFunctionFor(node.text, ctx.artifactName);
  if (looked) {
    return { Function: looked.Function, Reference: ctx.artifactName, Requirement: looked.Requirement, Dependencies: [] };
  }
  // Attribute conformance: a dependency only when X is a real (generated) attribute.
  const conform = node.text.match(CONFORM_RE);
  if (conform && ctx.attrRoots && ctx.attrRoots[conform[1]]) {
    return { Function: 'Validation', Reference: ctx.artifactName, Requirement: {}, Dependencies: [ctx.attrRoots[conform[1]]] };
  }
  // Unclassified leaf: no check function found — empty Requirement, flagged for a warning.
  return { Function: 'Validation', Reference: ctx.artifactName, Requirement: {}, Dependencies: [], unclassified: true };
}

/** Construct a single model rule object from a requirement-tree node. */
function makeRule(node, order, childKeys, ctx, modelVersionIntroduced, status, prevRule) {
  const c = classify(node, childKeys, ctx);
  const keyword = node.text.match(BCP14_KEYWORD);

  // Adopt the baseline rule's curation when the current derivation produced no Requirement
  // (the current lookup wins whenever it does resolve one). `prevRule` is set only for a
  // reused id, i.e. this sentence matched an Active baseline rule's MustSatisfy exactly, so
  // that rule's curation is what the model already says about this exact requirement.
  //
  // Two cases, both adopted the same way:
  //   * Baseline Requirement populated - enum value lists and functions like
  //     CheckNationalCurrency live only in the model and cannot be re-derived from the
  //     sentence text, so regenerating from the lookup alone would drop them.
  //   * Baseline Requirement empty - the rule is already curated as intentionally Dynamic
  //     (no check function is expected), so it is accepted rather than reported as unmapped.
  //
  // Adoption is optimistic. A carried Requirement / Dependencies may reference other rules
  // (CheckModelRule / Dependencies) whose NumericId shifted between versions, so the global
  // post-pass in main() reverts any carry whose references do not resolve. Everything that
  // resolves is kept, recovering curation the lookup cannot derive.
  const prevVc = (prevRule && prevRule.ValidationCriteria) || null;
  const prevReq = (prevVc && prevVc.Requirement) || {};
  const adoptCurated = Object.keys(prevReq).length
    // Any branch that derived no Requirement yields to a curated one.
    ? !Object.keys(c.Requirement).length
    // An empty baseline Requirement only settles a leaf that derived nothing at all; the
    // Presence and attribute-conformance branches keep their own derived Dependencies.
    : Boolean(prevVc) && Boolean(c.unclassified);
  if (adoptCurated) {
    c.accepted = !Object.keys(prevReq).length;
    c.unclassified = false;
    c.carried = true;
    c.Function = prevRule.Function;
    c.Reference = prevRule.Reference;
    c.Requirement = JSON.parse(JSON.stringify(prevReq));
    c.Dependencies = (prevVc.Dependencies || []).slice();
    c.carriedCondition = prevVc.Condition && Object.keys(prevVc.Condition).length
      ? JSON.parse(JSON.stringify(prevVc.Condition)) : null;
  }
  const entityName = c.Reference === ctx.artifactName ? ctx.displayName : pascalToDisplay(c.Reference);

  if (c.unclassified) {
    WARNINGS.push({ entity: `${ctx.entityType} ${ctx.artifactName}`, text: node.text });
  } else if (c.accepted) {
    ACCEPTED_DYNAMIC.push({ entity: `${ctx.entityType} ${ctx.artifactName}`, text: node.text });
  }

  // A populated Requirement (a check-function template) is Static; an empty one is Dynamic.
  const type = Object.keys(c.Requirement).length > 0 ? 'Static' : 'Dynamic';
  const conditions = (node.conditionAnchors || []).map((a) => CONDITIONS[a] || a);

  const rule = {
    Function: c.Function,
    Reference: c.Reference,
    EntityType: ctx.entityType,
    EntityName: entityName,
    EntityId: c.Reference,
    Notes: '',
    ModelVersionIntroduced: modelVersionIntroduced,
    Status: status || 'Active',
    Conditions: conditions,
    Type: type,
    Order: order,
  };
  // Model 1.5 onwards, every rule carries all three fields. DatasetType is the dataset's type
  // code for dataset-scoped entities and the entity's own ID prefix otherwise (ATT for
  // attributes, DMO for the data model, matching the CON prefix the conditions rules use).
  // DatasetId and DatasetName are null unless the rule really belongs to a dataset.
  rule.DatasetType = ctx.datasetType || ctx.idPrefix || null;
  rule.DatasetId = ctx.datasetId || null;
  rule.DatasetName = ctx.datasetName || null;
  rule.ValidationCriteria = {
    MustSatisfy: node.text,
    Keyword: keyword ? keyword[1] : '',
    Requirement: c.Requirement,
    Condition: c.carriedCondition || {},
    Dependencies: c.Dependencies,
  };
  // Invariant: a rule that evaluates another rule through CheckModelRule depends on it, so every
  // ModelRuleId named by the Requirement or the Condition must appear in Dependencies. Existing
  // entries keep their order and only missing refs are appended: Dependencies may legitimately
  // hold non-CheckModelRule entries (an attribute root from "MUST conform to <Attr>"), and the
  // baseline does not always list the refs first, so rewriting the order would churn rules that
  // already match.
  const deps = rule.ValidationCriteria.Dependencies;
  for (const ref of modelRuleRefs(c.Requirement).concat(modelRuleRefs(rule.ValidationCriteria.Condition))) {
    if (!deps.includes(ref)) deps.push(ref);
  }
  // Transient marker (stripped before write) so the post-pass can validate carried refs
  // and re-warn if it must revert one.
  if (c.carried) rule.__carried = { entity: `${ctx.entityType} ${ctx.artifactName}`, text: node.text };
  return rule;
}

// ---------------------------------------------------------------------------
// Baselines + stable-ID expansion
// ---------------------------------------------------------------------------

/** Merge all rule JSON files directly inside a baseline model_rules subdirectory. */
function loadBaselineDir(...relParts) {
  const dir = path.join(RELEASES_DIR, BASELINE_DIR, 'model_rules', ...relParts);
  if (!fs.existsSync(dir)) return null;
  const rules = {};
  for (const f of fs.readdirSync(dir)) {
    if (f.endsWith('.json')) Object.assign(rules, JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')));
  }
  return Object.keys(rules).length ? rules : null;
}

/** Load a single baseline rule JSON file. */
function loadBaselineFile(...relParts) {
  const file = path.join(RELEASES_DIR, BASELINE_DIR, 'model_rules', ...relParts);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

/**
 * Baseline file holding the rules for an output path. The output tree mirrors
 * releases/<v>/model_rules/, so the relative path maps across directly. Returned relative to
 * requirements_model/ for display.
 */
function baselineFileFor(outPath) {
  return path.join('releases', BASELINE_DIR, 'model_rules', path.relative(OUTPUT_ROOT, outPath));
}

/** ModelVersion recorded in the baseline's model_details.json; falls back to the directory name. */
function baselineModelVersion() {
  const file = path.join(RELEASES_DIR, BASELINE_DIR, 'model_details.json');
  if (!fs.existsSync(file)) return BASELINE_DIR;
  const details = JSON.parse(fs.readFileSync(file, 'utf8')).Details || {};
  return details.ModelVersion || BASELINE_DIR;
}

/** Load the baseline's check-function lookup (sentence -> { function, requirement }); {} if absent. */
function loadCheckLookup() {
  const file = path.join(RELEASES_DIR, BASELINE_DIR, 'check_function_lookup.json');
  return fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : {};
}

/** Map a condition anchor (lowercased id) to its Condition ID by scanning the conditions dir. */
function loadConditions(locationAbs, idHeading) {
  const map = {};
  if (!fs.existsSync(locationAbs)) return map;
  for (const file of fs.readdirSync(locationAbs).filter((f) => f.endsWith('.md'))) {
    const tokens = marked.lexer(fs.readFileSync(path.join(locationAbs, file), 'utf8'));
    if (!hasSection(tokens, idHeading)) continue;
    const id = getSectionText(tokens, idHeading);
    map[id.toLowerCase()] = id;
  }
  return map;
}

/** The column whose presence a dataset rule asserts, or null. */
function assertedColumn(rule) {
  const req = rule.ValidationCriteria.Requirement || {};
  if (req.CheckFunction === 'ColumnPresent' && req.ColumnName) return req.ColumnName;
  // A Presence rule left Dynamic (empty Requirement) still names its column in the sentence.
  if (rule.Function === 'Presence') {
    const m = (rule.ValidationCriteria.MustSatisfy || '').match(INCLUDE_RE);
    if (m) return m[1];
  }
  return null;
}

/**
 * Map each column to the dataset rule that governs its presence: the topmost dataset rule whose
 * subtree asserts presence for that column and nothing else. For most columns that is the single
 * "MUST include <Column>" leaf. For a column with several conditional presence rules it is the
 * composite grouping them (e.g. PricingCurrencyContractedUnitPrice resolves to the
 * "...MUST adhere to the following PricingCurrencyContractedUnitPrice presence requirements:"
 * composite, not to any one of its three MUST/SHOULD/MAY leaves).
 *
 * Ambiguous columns are omitted rather than guessed at.
 */
function presenceRulesByColumn(dsRules) {
  const columns = new Map(); // ruleId -> columns asserted anywhere in its subtree
  const reaches = new Map(); // ruleId -> rule ids in its subtree
  const visit = (id) => {
    if (columns.has(id)) return;
    columns.set(id, new Set());
    reaches.set(id, new Set());
    const rule = dsRules[id];
    if (!rule || rule.Status === 'Removed') return;
    const cols = columns.get(id);
    const reach = reaches.get(id);
    const col = assertedColumn(rule);
    if (col) cols.add(col);
    for (const ref of modelRuleRefs(rule.ValidationCriteria.Requirement || {})) {
      visit(ref);
      reach.add(ref);
      for (const c of columns.get(ref)) cols.add(c);
      for (const r of reaches.get(ref)) reach.add(r);
    }
  };
  for (const id of Object.keys(dsRules)) visit(id);

  const candidates = {};
  for (const [id, cols] of columns) {
    if (cols.size !== 1) continue; // asserts nothing, or spans several columns
    const col = [...cols][0];
    (candidates[col] = candidates[col] || []).push(id);
  }
  const byColumn = {};
  for (const col of Object.keys(candidates)) {
    // Candidates for one column form an ancestor chain; the topmost is the one no other reaches.
    const top = candidates[col].filter((a) => !candidates[col].some((b) => b !== a && reaches.get(b).has(a)));
    if (top.length === 1) byColumn[col] = top[0];
  }
  return byColumn;
}

/**
 * Order values for a requirement tree, one per spec in markdown (pre-order) sequence.
 *
 * Order records where a rule sits in the markdown, so it has to increase strictly down the
 * document. NumericIds cannot supply it: they are historical and reused, so a rule that moved
 * keeps its old number. The assignment is therefore:
 *
 *   * A rule found in the baseline keeps the Order the baseline gave it, as long as that value
 *     still sits above the previous rule's. This keeps established rules stable.
 *   * A baseline Order at or below the previous rule's is out of sequence, so it is discarded and
 *     the rule renumbered (recorded in ORDER_CONFLICTS, since the baseline disagrees with the
 *     markdown about position).
 *   * A rule needing a fresh value takes the next multiple of ten above the previous rule.
 *   * Unless the following rule already holds a baseline Order that the next multiple of ten
 *     would collide with or overshoot. Then it takes the midpoint of the surrounding pair, so
 *     inserting a rule never forces the rules after it out of sequence.
 *
 * A negative baseline Order (the -1 on a tombstone) never counts as a usable value.
 */
function assignOrders(idByIdx, prevRules, ctx) {
  const baselineOrder = (idx) => {
    const prev = idx < idByIdx.length && prevRules ? prevRules[idByIdx[idx]] : null;
    return prev && typeof prev.Order === 'number' && prev.Order >= 0 ? prev.Order : null;
  };

  const orders = [];
  let prev = -1; // so the first rule lands on 0
  for (let i = 0; i < idByIdx.length; i++) {
    const own = baselineOrder(i);
    if (own !== null && own > prev) {
      orders.push(own);
      prev = own;
      continue;
    }
    if (own !== null) {
      ORDER_CONFLICTS.push({ entity: `${ctx.entityType} ${ctx.artifactName}`, ruleId: idByIdx[i], baseline: own, after: prev });
    }
    const rounded = Math.floor(prev / 10) * 10 + 10;
    const next = baselineOrder(i + 1);
    let assigned = rounded;
    if (next !== null && next > prev && rounded >= next) {
      const mid = Math.floor((prev + next) / 2);
      // With no integer between the pair there is no room; fall back to the rounded value and
      // let the following rule be renumbered rather than emit a duplicate Order.
      if (mid > prev) assigned = mid;
    }
    orders.push(assigned);
    prev = assigned;
  }
  return orders;
}

/** Expand a requirement tree into { RuleId: rule }, reusing stable IDs and tombstoning removals. */
function expandTree(root, ctx, prevRules, outPath) {
  const specs = flattenTree(root);

  // Only Active previous rules are eligible for ID reuse: an exact MustSatisfy match
  // means the requirement is already in the model. A match against a non-Active rule
  // (Removed/Deprecated) does NOT count; that text gets a new NumericId. All previous
  // IDs still advance maxNumericId so tombstoned numbers are never reassigned.
  const prevByText = new Map();
  let maxNumericId = -1;
  if (prevRules) {
    for (const id of Object.keys(prevRules)) {
      maxNumericId = Math.max(maxNumericId, numericIdOf(id));
      if (prevRules[id].Status === 'Active') {
        prevByText.set(normalizeMustSatisfy(prevRules[id].ValidationCriteria.MustSatisfy), id);
      }
    }
  }

  const reusedIds = new Set();
  let nextNumericId = maxNumericId + 1;
  const idByIdx = specs.map((spec) => {
    const prevId = prevByText.get(normalizeMustSatisfy(spec.text));
    if (prevId) {
      reusedIds.add(prevId);
      return prevId;
    }
    const keyword = spec.text.match(BCP14_KEYWORD);
    const status = statusLetter(keyword && keyword[1], CONDITIONAL_RE.test(spec.text));
    return buildRuleId(ctx, nextNumericId++, status);
  });

  const orders = assignOrders(idByIdx, prevRules, ctx);

  const output = {};
  specs.forEach((spec, idx) => {
    const id = idByIdx[idx];
    const childKeys = spec.childIdx.map((ci) => idByIdx[ci]);
    // A reused id always came from an Active previous rule (reuse is Active-only), so
    // the rule is emitted Active; only its introduced version carries over.
    const prev = prevRules && prevRules[id];
    const introduced = prev ? prev.ModelVersionIntroduced : NEW_VERSION;
    output[id] = makeRule(spec.node, orders[idx], childKeys, ctx, introduced, 'Active', prev);
  });

  // A column's requirements only bind when the dataset includes the column, so the column's root
  // composite depends on the dataset rule governing that column's presence. Appended after the
  // child rules so Items stay the leading Dependencies.
  const presenceId = ctx.presenceByColumn && ctx.presenceByColumn[ctx.artifactName];
  if (presenceId && specs.length) {
    const deps = output[idByIdx[0]].ValidationCriteria.Dependencies;
    if (!deps.includes(presenceId)) deps.push(presenceId);
  }

  if (prevRules) {
    for (const id of Object.keys(prevRules)) {
      if (reusedIds.has(id)) continue;
      const carried = renameConditions(JSON.parse(JSON.stringify(prevRules[id])));
      // A baseline rule introduced in the version being drafted was never published, so a
      // tombstone would announce the removal of something no consumer ever saw: drop it from
      // the output instead. The baseline still holds a copy that this run cannot edit, so
      // record it for the report - that copy has to be deleted by hand.
      if (carried.ModelVersionIntroduced === NEW_VERSION) {
        UNPUBLISHED_REMOVALS.push({
          entity: `${ctx.entityType} ${ctx.artifactName}`,
          ruleId: id,
          file: baselineFileFor(outPath),
          text: (carried.ValidationCriteria || {}).MustSatisfy || '',
        });
        continue;
      }
      if (!carried.ModelVersionRemoved) {
        carried.Status = 'Removed';
        carried.ModelVersionRemoved = NEW_VERSION;
        carried.Order = -1; // removed rules are never referenced as a requirement
      }
      output[id] = carried;
    }
  }

  const sorted = {};
  for (const id of Object.keys(output).sort((a, b) => numericIdOf(a) - numericIdOf(b))) sorted[id] = output[id];
  return sorted;
}

// ---------------------------------------------------------------------------
// Per-entity emit + main
// ---------------------------------------------------------------------------

// 2-space indent and a trailing newline match the hand-authored baseline files, so a fully
// derived entity is byte-identical to its baseline copy and `npm run diff` reads clean.
function writeJson(outPath, obj) {
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify(obj, null, 2) + '\n');
}

/**
 * Parse one markdown file and expand it against its baseline. Output is collected in
 * EMITTED (not written yet) so the global carry-forward post-pass can run with every
 * rule ID visible before anything is persisted.
 */
function emit(mdPath, ctx, headings, baseline, outPath) {
  const tokens = marked.lexer(fs.readFileSync(mdPath, 'utf8'));
  const tree = parseRequirementTree(tokens, headings.Requirements);
  const rules = expandTree(tree, ctx, baseline, outPath);
  EMITTED.push({ outPath, rules });
  return rules;
}

/**
 * RuleIds a rule points at (for cross-version ref validation). Covers the Condition as well as
 * the Requirement: a carried Condition can name a rule whose NumericId shifted between versions,
 * and that carry has to be reverted just like an unresolvable Requirement ref.
 */
function referencedIds(rule) {
  const vc = rule.ValidationCriteria;
  return modelRuleRefs(vc.Requirement).concat(modelRuleRefs(vc.Condition), vc.Dependencies || []);
}

/**
 * Validate every carried-forward Requirement against the full set of generated rule IDs.
 * A carry whose references don't all resolve (e.g. a baseline dependency whose NumericId
 * shifted) is reverted to an empty, Dynamic rule and re-flagged as unmapped. Then strip
 * the transient marker and persist every file.
 */
function finalizeEmitted() {
  const liveIds = new Set();
  for (const { rules } of EMITTED) {
    for (const id of Object.keys(rules)) if (rules[id].Status !== 'Removed') liveIds.add(id);
  }
  for (const { rules } of EMITTED) {
    for (const id of Object.keys(rules)) {
      const r = rules[id];
      const carried = r.__carried;
      delete r.__carried;
      if (!carried || r.Status === 'Removed') continue;
      if (referencedIds(r).every((x) => liveIds.has(x))) continue;
      r.Function = 'Validation';
      r.Type = 'Dynamic';
      r.ValidationCriteria.Requirement = {};
      r.ValidationCriteria.Condition = {};
      r.ValidationCriteria.Dependencies = [];
      WARNINGS.push(carried);
    }
  }
  for (const { outPath, rules } of EMITTED) writeJson(outPath, rules);
}

function main() {
  const contract = JSON.parse(fs.readFileSync(CONTRACT_PATH, 'utf8'));
  const summary = [];

  const baselineRoot = path.join(RELEASES_DIR, BASELINE_DIR);
  if (!fs.existsSync(path.join(baselineRoot, 'model_rules'))) {
    throw new Error(`Baseline not found: ${baselineRoot}/model_rules (set BASELINE_DIR to a directory under releases/)`);
  }
  PREVIOUS_VERSION = baselineModelVersion();
  if (!process.env.NEW_VERSION) NEW_VERSION = PREVIOUS_VERSION;

  CHECK_LOOKUP = loadCheckLookup();
  CONDITIONS = loadConditions(path.join(REPO_ROOT, contract.Conditions.Location), contract.Conditions.Headings.Id);

  // --- DataModel ---
  {
    const dm = contract.DataModel;
    const mdPath = path.join(REPO_ROOT, dm.Location);
    const tokens = marked.lexer(fs.readFileSync(mdPath, 'utf8'));
    const ctx = {
      entityType: dm.EntityType,
      artifactType: dm.ArtifactType,
      idPrefix: dm.IdPrefix,
      artifactName: getSectionText(tokens, dm.Headings.Id),
      displayName: getSectionText(tokens, dm.Headings.DisplayName),
    };
    const rules = emit(mdPath, ctx, dm.Headings, loadBaselineDir('datamodel'), path.join(OUTPUT_ROOT, 'datamodel.json'));
    summary.push([`DataModel (${ctx.artifactName})`, Object.keys(rules).length]);
  }

  // --- Attributes (first: dataset/column "conform to X" rules depend on their root IDs) ---
  const attrRoots = {}; // attribute EntityId -> its root rule ID (e.g. NullHandling -> ATT-NullHandling-A-000-C)
  const att = contract.Attributes;
  const attrDir = path.join(REPO_ROOT, att.Location);
  for (const file of fs.readdirSync(attrDir).filter((f) => f.endsWith('.md'))) {
    const attrMdPath = path.join(attrDir, file);
    const attrTokens = marked.lexer(fs.readFileSync(attrMdPath, 'utf8'));
    // Skip non-entity files (e.g. attributes_overview.md) that lack the entity sections.
    if (!hasSection(attrTokens, att.Headings.Id) || !hasSection(attrTokens, att.Headings.Requirements)) continue;
    const attrId = getSectionText(attrTokens, att.Headings.Id);
    const attrCtx = { entityType: att.EntityType, artifactType: att.ArtifactType, idPrefix: att.IdPrefix, artifactName: attrId, displayName: getSectionText(attrTokens, att.Headings.DisplayName) };
    const outName = datasetJsonName(path.basename(file, '.md'));
    const attrOut = path.join(OUTPUT_ROOT, 'attributes', outName);
    const attrRules = emit(attrMdPath, attrCtx, att.Headings, loadBaselineFile('attributes', outName), attrOut);
    attrRoots[attrId] = Object.keys(attrRules).find((k) => numericIdOf(k) === 0);
    summary.push([`Attribute ${attrId}`, Object.keys(attrRules).length]);
  }

  // --- Datasets + their Columns ---
  const datasetFolders = resolveDatasetFolders(path.join(REPO_ROOT, contract.Datasets.Location));
  for (const folder of datasetFolders) {
    const ds = contract.Datasets;
    const dsMdPath = path.join(REPO_ROOT, ds.Location, folder, 'dataset.md');
    const dsTokens = marked.lexer(fs.readFileSync(dsMdPath, 'utf8'));
    const datasetId = getSectionText(dsTokens, ds.Headings.Id);
    const datasetName = getSectionText(dsTokens, ds.Headings.DisplayName);
    const datasetType = contract.DatasetTypes[datasetId];
    const dsCtx = { entityType: ds.EntityType, artifactType: ds.ArtifactType, idPrefix: datasetType, artifactName: datasetId, displayName: datasetName, datasetType, datasetId, datasetName, attrRoots };
    const dsOut = path.join(OUTPUT_ROOT, 'datasets', folder, datasetJsonName(folder));
    const dsRules = emit(dsMdPath, dsCtx, ds.Headings, loadBaselineDir('datasets', folder), dsOut);
    summary.push([`Dataset ${datasetId}`, Object.keys(dsRules).length]);

    // Derived from the dataset's own rules, so each column root can depend on the rule that
    // requires it. Columns are emitted after their dataset, so those IDs are already settled.
    const presenceByColumn = presenceRulesByColumn(dsRules);

    const cc = contract.Columns;
    const colDir = path.join(REPO_ROOT, ds.Location, folder, 'columns');
    for (const file of fs.readdirSync(colDir).filter((f) => f.endsWith('.md'))) {
      const colMdPath = path.join(colDir, file);
      const colTokens = marked.lexer(fs.readFileSync(colMdPath, 'utf8'));
      const colId = getSectionText(colTokens, cc.Headings.Id);
      const colCtx = { entityType: cc.EntityType, artifactType: cc.ArtifactType, idPrefix: datasetType, artifactName: colId, displayName: getSectionText(colTokens, cc.Headings.DisplayName), datasetType, datasetId, datasetName, attrRoots, presenceByColumn };
      const base = path.basename(file, '.md');
      const colOut = path.join(OUTPUT_ROOT, 'datasets', folder, 'columns', `${base}.json`);
      const colRules = emit(colMdPath, colCtx, cc.Headings, loadBaselineFile('datasets', folder, 'columns', `${base}.json`), colOut);
      summary.push([`  Column ${colId}`, Object.keys(colRules).length]);
    }
  }

  finalizeEmitted();

  console.log(`Baseline: releases/${BASELINE_DIR} (model version ${PREVIOUS_VERSION})`);
  console.log(`Wrote model rules under ${OUTPUT_ROOT} (new rules stamped ${NEW_VERSION}):`);
  for (const [name, count] of summary) console.log(`  ${name}: ${count} rules`);

  if (ACCEPTED_DYNAMIC.length) {
    console.log(`\n${ACCEPTED_DYNAMIC.length} requirement sentence(s) accepted as Dynamic (matched a baseline rule already curated with an empty Requirement).`);
  }

  if (UNPUBLISHED_REMOVALS.length) {
    console.warn(`\n⚠ ${UNPUBLISHED_REMOVALS.length} baseline rule(s) introduced in ${NEW_VERSION} are no longer in the markdown`);
    console.warn(`  (dropped from the output, not tombstoned, because ${NEW_VERSION} is unpublished).`);
    console.warn('  This output folder is not the baseline, so delete each one from its baseline file by hand:');
    for (const r of UNPUBLISHED_REMOVALS) {
      console.warn(`    ${r.ruleId}  [${r.entity}]  ${r.file}`);
      if (r.text) console.warn(`      "${r.text}"`);
    }
  }

  if (ORDER_CONFLICTS.length) {
    console.warn(`\n⚠ ${ORDER_CONFLICTS.length} rule(s) had a baseline Order out of markdown sequence`);
    console.warn('  (renumbered here; the baseline Order sat at or below the preceding rule\'s):');
    for (const c of ORDER_CONFLICTS) console.warn(`    ${c.ruleId}  [${c.entity}]  baseline Order ${c.baseline} follows ${c.after}`);
  }

  if (WARNINGS.length) {
    console.warn(`\n⚠ ${WARNINGS.length} requirement sentence(s) have no check-function mapping`);
    console.warn('  (Requirement left empty, Type set to Dynamic). Add entries to the lookup to resolve:');
    for (const w of WARNINGS) console.warn(`    [${w.entity}] ${w.text}`);
  }
}

main();
