#!/usr/bin/env node
'use strict';

/**
 * Completeness diff: the generated extract vs the baseline Requirements Model.
 *
 * The extractor is "complete" for an entity when its generated file is byte-identical to the
 * hand-authored copy in releases/<BASELINE_DIR>/model_rules/. Anything short of that is a gap
 * in the derivation (a missing check-function mapping, a curated Requirement that cannot be
 * re-derived, a rule the markdown no longer expresses). This reports those gaps per entity.
 *
 * Entities are compared by mirrored relative path, since the output tree mirrors the baseline
 * layout. Each shared entity lands in one of four buckets:
 *   identical        - byte-equal; fully derived
 *   formatting only  - same rules and key order, different whitespace
 *   key order only   - same rules and values, different key order
 *   content differs  - rules added, removed, or changed
 *
 * Baseline entities with no generated counterpart are split by cause so that out-of-scope
 * entity kinds and dead tombstone files never read as extraction gaps.
 *
 * Run `npm run extract` first. Exits 0 unless --strict is passed.
 *
 * Flags: --summary (counts only)  --strict (exit non-zero on a content gap)
 */

const fs = require('fs');
const path = require('path');

const RELEASES_DIR = path.join(__dirname, '..', 'releases');
const OUTPUT_ROOT = path.join(__dirname, 'output', 'model_rules');
const BASELINE_DIR = process.env.BASELINE_DIR || 'latest';
const BASELINE_ROOT = path.join(RELEASES_DIR, BASELINE_DIR, 'model_rules');

// Entity kinds the extractor does not generate: the contract defines no Objects entity, and
// conditions markdown is read only for the anchor -> ConditionId map, never expanded into rules.
const OUT_OF_SCOPE = (rel) => {
  const parts = rel.split(path.sep);
  return parts[0] === 'conditions' || parts.includes('objects');
};

const SUMMARY_ONLY = process.argv.includes('--summary');
const STRICT = process.argv.includes('--strict');
const MAX_VALUE = 88;

/** Every .json file under `root`, as sorted root-relative paths. */
function walk(root) {
  const out = [];
  if (!fs.existsSync(root)) return out;
  (function rec(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) rec(p);
      else if (e.name.endsWith('.json')) out.push(path.relative(root, p));
    }
  })(root);
  return out.sort();
}

/** Recursively key-sorted copy, so two values compare equal regardless of key order. */
function canonical(v) {
  if (Array.isArray(v)) return v.map(canonical);
  if (v && typeof v === 'object') {
    const out = {};
    for (const k of Object.keys(v).sort()) out[k] = canonical(v[k]);
    return out;
  }
  return v;
}

const sameContent = (a, b) => JSON.stringify(canonical(a)) === JSON.stringify(canonical(b));
const sameOrder = (a, b) => JSON.stringify(a) === JSON.stringify(b);

/**
 * Leaf-level differences between two rules as [{ path, baseline, generated }]. Objects recurse;
 * arrays compare whole, since a reordered Dependencies list is one meaningful difference rather
 * than several.
 */
function fieldDiffs(a, b, prefix = '') {
  const isObj = (v) => v && typeof v === 'object' && !Array.isArray(v);
  if (isObj(a) && isObj(b)) {
    const out = [];
    for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) {
      out.push(...fieldDiffs(a[k], b[k], prefix ? `${prefix}.${k}` : k));
    }
    return out;
  }
  if (sameOrder(a, b)) return [];
  return [{ path: prefix, baseline: a, generated: b }];
}

const render = (v) => {
  if (v === undefined) return '(absent)';
  const s = JSON.stringify(v);
  return s.length > MAX_VALUE ? s.slice(0, MAX_VALUE - 1) + '…' : s;
};

/** Compare one shared entity. Returns its bucket plus rule-level detail when content differs. */
function compareEntity(rel) {
  const baseText = fs.readFileSync(path.join(BASELINE_ROOT, rel), 'utf8');
  const outText = fs.readFileSync(path.join(OUTPUT_ROOT, rel), 'utf8');
  if (baseText === outText) return { rel, bucket: 'identical' };

  const base = JSON.parse(baseText);
  const out = JSON.parse(outText);
  if (sameOrder(base, out)) return { rel, bucket: 'formatting' };
  if (sameContent(base, out)) return { rel, bucket: 'keyOrder' };

  const baseOnly = Object.keys(base).filter((id) => !(id in out));
  const outOnly = Object.keys(out).filter((id) => !(id in base));
  const changed = Object.keys(base)
    .filter((id) => id in out && !sameOrder(base[id], out[id]))
    .map((id) => ({ id, diffs: fieldDiffs(base[id], out[id]) }));
  return { rel, bucket: 'content', baseOnly, outOnly, changed };
}

/** Split baseline-only entities by cause: out of scope, dead tombstone file, or a real gap. */
function classifyBaselineOnly(rel) {
  if (OUT_OF_SCOPE(rel)) return 'outOfScope';
  const rules = JSON.parse(fs.readFileSync(path.join(BASELINE_ROOT, rel), 'utf8'));
  const ids = Object.keys(rules);
  // Every rule already Removed means the markdown is gone and there is nothing left to derive.
  return ids.length && ids.every((id) => rules[id].Status === 'Removed') ? 'tombstoneOnly' : 'missing';
}

function main() {
  if (!fs.existsSync(BASELINE_ROOT)) {
    console.error(`Baseline not found: ${BASELINE_ROOT} (set BASELINE_DIR to a directory under releases/)`);
    process.exit(2);
  }
  if (!fs.existsSync(OUTPUT_ROOT)) {
    console.error(`No generated output at ${OUTPUT_ROOT}. Run \`npm run extract\` first.`);
    process.exit(2);
  }

  const baseFiles = walk(BASELINE_ROOT);
  const outFiles = walk(OUTPUT_ROOT);
  const outSet = new Set(outFiles);
  const baseSet = new Set(baseFiles);

  const shared = baseFiles.filter((f) => outSet.has(f)).map(compareEntity);
  const buckets = { identical: [], formatting: [], keyOrder: [], content: [] };
  for (const e of shared) buckets[e.bucket].push(e);

  const baselineOnly = { outOfScope: [], tombstoneOnly: [], missing: [] };
  for (const rel of baseFiles.filter((f) => !outSet.has(f))) baselineOnly[classifyBaselineOnly(rel)].push(rel);
  const generatedOnly = outFiles.filter((f) => !baseSet.has(f));

  const pct = shared.length ? Math.round((buckets.identical.length / shared.length) * 100) : 0;
  const row = (label, n, note) => console.log(`  ${label.padEnd(28)}${String(n).padStart(4)}${note ? '   ' + note : ''}`);

  console.log(`Model completeness: generated extract vs releases/${BASELINE_DIR}\n`);
  console.log(`Shared entities              ${String(shared.length).padStart(4)}`);
  row('identical (byte-equal)', buckets.identical.length, `${pct}% of shared`);
  row('formatting only', buckets.formatting.length);
  row('key order only', buckets.keyOrder.length);
  row('content differs', buckets.content.length);
  console.log(`\nBaseline entities not generated ${String(baseFiles.length - shared.length).padStart(1)}`);
  row('out of extractor scope', baselineOnly.outOfScope.length, 'conditions/, objects/');
  row('tombstone-only', baselineOnly.tombstoneOnly.length, 'no markdown; nothing to derive');
  row('missing (has active rules)', baselineOnly.missing.length, baselineOnly.missing.length ? '<- gap' : '');
  if (generatedOnly.length) {
    console.log(`\nGenerated entities not in baseline ${String(generatedOnly.length).padStart(1)}`);
    for (const rel of generatedOnly) console.log(`    ${rel}`);
  }

  // A content gap is a derivation failure: rules the extractor cannot reproduce, or entities
  // one side lacks. Key order and whitespace are serialization drift in the hand-authored
  // baseline (which carries 25 distinct key orders), not something the extractor got wrong, so
  // they are reported separately and do not fail --strict.
  const gaps = buckets.content.length + baselineOnly.missing.length + generatedOnly.length;
  const drift = buckets.formatting.length + buckets.keyOrder.length;
  const entities = (n) => (n === 1 ? '1 entity differs' : `${n} entities differ`);
  if (gaps) console.log(`\n❌ Model has gaps: ${entities(gaps)} from the baseline in content.`);
  else if (drift) console.log(`\n✅ Content COMPLETE: every in-scope entity matches the baseline. ${entities(drift)} only in key order or whitespace, which is baseline drift to normalize.`);
  else console.log('\n✅ Model COMPLETE: every in-scope entity is byte-identical to the baseline.');

  if (SUMMARY_ONLY || !(gaps + drift)) return gaps;

  if (baselineOnly.missing.length) {
    console.log('\n── Baseline entities with active rules and no generated file ──');
    for (const rel of baselineOnly.missing) console.log(`  ${rel}`);
  }

  const detailed = [...buckets.content, ...buckets.keyOrder, ...buckets.formatting];
  if (detailed.length) console.log('\n── Entities that differ ──');
  for (const e of detailed) {
    if (e.bucket !== 'content') {
      console.log(`\n${e.rel}\n  (${e.bucket === 'formatting' ? 'whitespace only' : 'key order only'}; rules and values match)`);
      continue;
    }
    const n = e.baseOnly.length + e.outOnly.length + e.changed.length;
    console.log(`\n${e.rel}  (${n} rule${n === 1 ? '' : 's'})`);
    for (const id of e.baseOnly) console.log(`  - ${id}  in baseline only`);
    for (const id of e.outOnly) console.log(`  + ${id}  generated only`);
    for (const { id, diffs } of e.changed) {
      console.log(`  ~ ${id}`);
      for (const d of diffs) console.log(`      ${d.path}: ${render(d.baseline)} -> ${render(d.generated)}`);
    }
  }
  return gaps;
}

const gaps = main();
process.exit(STRICT && gaps ? 1 : 0);
