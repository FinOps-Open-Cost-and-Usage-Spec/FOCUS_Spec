#!/usr/bin/env node
'use strict';

/**
 * Correctness audit for the extractor output.
 *
 * Two layers:
 *  1. Structural integrity over EVERY generated file (no duplicate IDs, sorted,
 *     active-rule dependencies resolve within the file or to external ATT-* rules,
 *     composite Items == Dependencies, Keyword matches MustSatisfy).
 *  2. A deep transformation audit of the billing_period DATASET file, independently
 *     re-deriving expectations from its two inputs — the baseline JSON in
 *     releases/latest and the current dataset markdown.
 *
 * Verifies the transformation, not parity with the hand-authored target release.
 * Exits non-zero on any failure. Honors BASELINE_DIR / NEW_VERSION / DATASET_FOLDER.
 */

const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
const { renderInline, datasetJsonName, renameConditions } = require('./markdown_util');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..');
const RELEASES_DIR = path.join(__dirname, '..', 'releases');
const CONTRACT_PATH = path.join(__dirname, 'requirements_model_contract.json');
const OUTPUT_ROOT = path.join(__dirname, 'output', 'model_rules');

// Must resolve the same baseline as extract_rm.js, or the audit re-derives its
// expectations from a different release than the output was generated against.
const BASELINE_DIR = process.env.BASELINE_DIR || 'latest';
const NEW_VERSION = process.env.NEW_VERSION || baselineModelVersion();
const DATASET_FOLDER = process.env.DATASET_FOLDER || 'billing_period';

/** ModelVersion recorded in the baseline's model_details.json; falls back to the directory name. */
function baselineModelVersion() {
  const file = path.join(RELEASES_DIR, BASELINE_DIR, 'model_details.json');
  if (!fs.existsSync(file)) return BASELINE_DIR;
  const details = JSON.parse(fs.readFileSync(file, 'utf8')).Details || {};
  return details.ModelVersion || BASELINE_DIR;
}

const normalize = (t) => t.trim().replace(/\s+/g, ' ');
const numericIdOf = (id) => { const m = id.match(/-(\d+)-[A-Z]$/); return m ? parseInt(m[1], 10) : -1; };

/** Every ModelRuleId named inside a Requirement or Condition, in traversal order. */
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

// Independent of renderInline: raw HTML entities must never reach MustSatisfy. This
// guards against an encoding regression in markdown_util that the markdown-derived
// oracle (which shares renderInline) could not otherwise detect.
const HTML_ENTITY = /&(?:amp|lt|gt|quot|#\d+|#x[0-9a-f]+);/i;

function walkFiles(dir) {
  const out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walkFiles(p));
    else if (e.name.endsWith('.json')) out.push(p);
  }
  return out;
}

// --- Layer 1: structural integrity for every generated file -----------------
function structuralChecks(check, warn) {
  const files = walkFiles(OUTPUT_ROOT);
  // Global ID sets so cross-file dependencies can be resolved and removed rules detected.
  const allIds = new Set();
  const removedIds = new Set();
  for (const file of files) {
    const rules = JSON.parse(fs.readFileSync(file, 'utf8'));
    for (const id of Object.keys(rules)) { allIds.add(id); if (rules[id].Status === 'Removed') removedIds.add(id); }
  }
  let dupIds = 0, dupNums = 0, unsorted = 0, dangling = 0, inconsistent = 0, entities = 0, prefixMismatch = 0, undeclared = 0, dupOrders = 0;
  for (const file of files) {
    const rules = JSON.parse(fs.readFileSync(file, 'utf8'));
    const ids = Object.keys(rules);
    // Dataset/column rules must carry their DatasetType and an ID prefixed with it.
    const isDatasetScoped = path.sep + 'datasets' + path.sep;
    for (const id of ids) {
      const r = rules[id];
      if (r.Status === 'Removed') continue;
      if (file.includes(isDatasetScoped)) {
        if (!r.DatasetType) { prefixMismatch++; console.log('     missing DatasetType', id, 'in', path.basename(file)); }
        else if (!id.startsWith(r.DatasetType + '-')) { prefixMismatch++; console.log('     ID prefix != DatasetType', id, 'in', path.basename(file)); }
      }
    }
    const keys = new Set(ids);
    if (keys.size !== ids.length) { dupIds++; console.log('     dup IDs in', file); }
    const nums = ids.map(numericIdOf);
    if (new Set(nums).size !== nums.length) { dupNums++; console.log('     dup NumericIds in', file); }
    if (!ids.every((id, i) => i === 0 || numericIdOf(ids[i - 1]) <= numericIdOf(id))) { unsorted++; console.log('     unsorted', file); }
    // Order places a rule in the markdown, so two active rules in one entity must never share
    // one (the guard against an Order insertion having no integer room between its neighbours).
    const activeOrders = ids.filter((id) => rules[id].Status !== 'Removed').map((id) => rules[id].Order);
    if (new Set(activeOrders).size !== activeOrders.length) { dupOrders++; console.log('     duplicate Order in', path.basename(file)); }
    for (const id of ids) {
      const r = rules[id];
      if (HTML_ENTITY.test(r.ValidationCriteria.MustSatisfy)) { entities++; console.log('     HTML entity in MustSatisfy', id, 'in', path.basename(file)); }
      if (r.Status === 'Removed') continue;
      for (const d of r.ValidationCriteria.Dependencies) {
        if (!allIds.has(d)) { dangling++; console.log('     unresolved dep', id, '->', d, 'in', path.basename(file)); }
        else if (removedIds.has(d)) warn(`active rule ${id} references removed rule ${d}`);
      }
      if (r.Function === 'Composite') {
        // Items must LEAD Dependencies rather than equal them: a root composite carries extra
        // edges after its children (a column root also depends on the dataset rule requiring
        // that column), and Dependencies legitimately holds non-CheckModelRule entries.
        const items = (r.ValidationCriteria.Requirement.Items || []).map((i) => i.ModelRuleId);
        const deps = r.ValidationCriteria.Dependencies;
        if (items.join(',') !== deps.slice(0, items.length).join(',')) {
          inconsistent++;
          console.log('     Composite Items are not the leading Dependencies', id);
        }
      }
      // A rule that evaluates another through CheckModelRule depends on it, so every ModelRuleId
      // named by the Requirement or the Condition has to be declared in Dependencies.
      for (const ref of modelRuleRefs(r.ValidationCriteria.Requirement).concat(modelRuleRefs(r.ValidationCriteria.Condition))) {
        if (!r.ValidationCriteria.Dependencies.includes(ref)) {
          undeclared++;
          console.log('     ModelRuleId not in Dependencies', id, '->', ref, 'in', path.basename(file));
        }
      }
      const kw = r.ValidationCriteria.MustSatisfy.match(/\b(MUST NOT|MUST|SHALL NOT|SHALL|SHOULD NOT|SHOULD|MAY)\b/);
      if (!kw || kw[1] !== r.ValidationCriteria.Keyword) { inconsistent++; console.log('     Keyword mismatch', id); }
    }
  }
  check(true, `Scanned ${files.length} output files`);
  check(dupIds === 0, 'No duplicate Rule IDs in any file');
  check(dupNums === 0, 'No duplicate NumericIds in any file');
  check(unsorted === 0, 'Every file sorted by NumericId');
  check(dangling === 0, 'Active-rule dependencies resolve across all generated files (incl. ATT-*)');
  check(inconsistent === 0, 'Composite Items lead Dependencies and Keyword==MustSatisfy keyword');
  check(entities === 0, 'No raw HTML entities in MustSatisfy (entity-decode regression guard)');
  check(prefixMismatch === 0, 'Dataset/column rules carry DatasetType and an ID prefixed with it');
  check(undeclared === 0, 'Every CheckModelRule ModelRuleId in a Requirement/Condition is declared in Dependencies');
  check(dupOrders === 0, 'No two active rules in an entity share an Order');
}

// --- Layer 2: deep transformation audit of the dataset file ------------------
function datasetAudit(check) {
  const contract = JSON.parse(fs.readFileSync(CONTRACT_PATH, 'utf8'));
  const reqHeading = contract.Datasets.Headings.Requirements;
  const out = JSON.parse(fs.readFileSync(path.join(OUTPUT_ROOT, 'datasets', DATASET_FOLDER, datasetJsonName(DATASET_FOLDER)), 'utf8'));

  const baselineDir = path.join(RELEASES_DIR, BASELINE_DIR, 'model_rules', 'datasets', DATASET_FOLDER);
  const baseline = {};
  if (fs.existsSync(baselineDir)) for (const f of fs.readdirSync(baselineDir)) if (f.endsWith('.json')) Object.assign(baseline, JSON.parse(fs.readFileSync(path.join(baselineDir, f), 'utf8')));

  const md = fs.readFileSync(path.join(REPO_ROOT, contract.Datasets.Location, DATASET_FOLDER, 'dataset.md'), 'utf8');
  const tokens = marked.lexer(md);
  const body = (() => { const i = tokens.findIndex((t) => t.type === 'heading' && t.text.replace(/<!--.*?-->/g, '').trim() === reqHeading); const b = []; for (let j = i + 1; j < tokens.length; j++) { if (tokens[j].type === 'heading') break; b.push(tokens[j]); } return b; })();
  const expected = new Set([normalize(renderInline(body.find((t) => t.type === 'paragraph').tokens))]);
  (function walk(list) { for (const it of list.items) { const tt = it.tokens.find((t) => t.type === 'text'); expected.add(normalize(renderInline(tt.tokens))); const sub = it.tokens.find((t) => t.type === 'list'); if (sub) walk(sub); } })(body.find((t) => t.type === 'list'));

  const baseByText = new Map(); let baselineMax = -1;
  for (const id of Object.keys(baseline)) { baseByText.set(normalize(baseline[id].ValidationCriteria.MustSatisfy), id); baselineMax = Math.max(baselineMax, numericIdOf(id)); }

  const active = {}; for (const id of Object.keys(out)) if (out[id].Status !== 'Removed') active[id] = out[id];
  const activeTexts = new Set(Object.values(active).map((r) => normalize(r.ValidationCriteria.MustSatisfy)));

  check(activeTexts.size === expected.size && [...expected].every((t) => activeTexts.has(t)),
    `[dataset] Active rules cover exactly the ${expected.size} markdown requirements (got ${activeTexts.size})`);

  let idIssues = 0;
  for (const id of Object.keys(active)) {
    const t = normalize(active[id].ValidationCriteria.MustSatisfy);
    if (baseByText.has(t)) { if (id !== baseByText.get(t)) idIssues++; }
    else if (numericIdOf(id) <= baselineMax) idIssues++;
  }
  check(idIssues === 0, `[dataset] Reused IDs match baseline; new IDs above baseline max (${baselineMax})`);

  let versionIssues = 0;
  for (const id of Object.keys(active)) {
    const t = normalize(active[id].ValidationCriteria.MustSatisfy);
    const want = baseByText.has(t) ? baseline[baseByText.get(t)].ModelVersionIntroduced : NEW_VERSION;
    if (active[id].ModelVersionIntroduced !== want) versionIssues++;
  }
  check(versionIssues === 0, '[dataset] ModelVersionIntroduced correct (reused vs new)');

  // A baseline rule introduced in NEW_VERSION never shipped, so dropping it beats tombstoning
  // the removal of something no consumer saw. Anything older must be tombstoned.
  const unpublished = (id) => baseline[id].ModelVersionIntroduced === NEW_VERSION;

  let tombIssues = 0, dropIssues = 0;
  for (const id of Object.keys(baseline)) {
    const t = normalize(baseline[id].ValidationCriteria.MustSatisfy);
    if (expected.has(t)) continue;
    if (unpublished(id)) { if (out[id]) dropIssues++; continue; }
    if (!out[id]) { tombIssues++; continue; }
    if (baseline[id].Status === 'Removed') { if (JSON.stringify(out[id]) !== JSON.stringify(renameConditions(JSON.parse(JSON.stringify(baseline[id]))))) tombIssues++; }
    else if (out[id].Status !== 'Removed' || out[id].ModelVersionRemoved !== NEW_VERSION) tombIssues++;
  }
  check(tombIssues === 0, '[dataset] Unmatched baseline rules tombstoned (already-removed carried unchanged)');
  check(dropIssues === 0, `[dataset] Unmatched baseline rules introduced in ${NEW_VERSION} dropped, not tombstoned`);

  const expectedIds = new Set([...Object.keys(active), ...Object.keys(baseline).filter((id) => !expected.has(normalize(baseline[id].ValidationCriteria.MustSatisfy)) && !unpublished(id))]);
  const outIds = new Set(Object.keys(out));
  check(expectedIds.size === outIds.size && [...outIds].every((id) => expectedIds.has(id)), '[dataset] Output = derived-active ∪ tombstones (no orphans)');
}

/** Run all checks. Returns { pass, fail, warnings }. Logs each check unless silent. */
function runVerify({ silent = false } = {}) {
  let pass = 0, fail = 0;
  const warnings = [];
  const check = (ok, msg) => { if (!silent) console.log((ok ? '✅' : '❌') + ' ' + msg); ok ? pass++ : fail++; };
  const warn = (msg) => warnings.push(msg);
  structuralChecks(check, warn);
  datasetAudit(check);
  if (!silent) {
    if (warnings.length) {
      console.log(`\n⚠ ${warnings.length} warning(s):`);
      for (const w of warnings) console.log('   ' + w);
    }
    console.log(`\n${pass} checks passed, ${fail} failed, ${warnings.length} warning(s).`);
  }
  return { pass, fail, warnings };
}

if (require.main === module) {
  const { fail } = runVerify();
  process.exit(fail ? 1 : 0);
}

module.exports = { runVerify };
