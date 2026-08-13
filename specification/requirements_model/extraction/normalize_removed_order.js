#!/usr/bin/env node
'use strict';

/**
 * Set Order to -1 on every Removed rule in a release's model_rules tree.
 *
 * A removed rule is never referenced as a requirement, so its position in the markdown is
 * meaningless. The baseline is inconsistent about this: most removed rules already use -1 while
 * the rest kept whatever Order they had when they were active. The extractor always writes -1, so
 * normalizing the baseline removes that whole class of difference from `npm run diff`.
 *
 * This edits files under releases/, NOT generated output, so it errs heavily toward safety:
 *
 *   * Dry run by default. Nothing is written without --apply.
 *   * Every file is round-tripped first: the parsed JSON is re-serialized with the file's own
 *     indentation and trailing-newline style and compared byte-for-byte against the original. A
 *     file that does not round-trip is reported and skipped, never rewritten, so the only possible
 *     byte change in a rewritten file is the Order values themselves.
 *   * Files needing no change are left untouched (no reformatting sweep).
 *   * The resolved target is printed, since releases/latest is a symlink.
 *   * Uncommitted changes in the target are reported up front, so the edit can be made on a clean
 *     tree and reviewed with `git diff`.
 *
 * Usage:
 *   node normalize_removed_order.js              # dry run against releases/latest
 *   node normalize_removed_order.js --apply      # write the changes
 *   BASELINE_DIR=1.4 node normalize_removed_order.js
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const RELEASES_DIR = path.join(__dirname, '..', 'releases');
const BASELINE_DIR = process.env.BASELINE_DIR || 'latest';
const TARGET = path.join(RELEASES_DIR, BASELINE_DIR, 'model_rules');
const APPLY = process.argv.includes('--apply');

/** Every .json file under `root`, as sorted root-relative paths. */
function walk(root) {
  const out = [];
  (function rec(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) rec(p);
      else if (e.name.endsWith('.json')) out.push(path.relative(root, p));
    }
  })(root);
  return out.sort();
}

/**
 * The file's own serialization style, inferred from its text: the indent width of the first
 * indented line, and whether it ends with a newline. Used so a rewrite reproduces the original
 * byte-for-byte apart from the values that changed.
 */
function styleOf(text) {
  const line = text.split('\n').find((l) => /^\s+\S/.test(l));
  const indent = line ? line.match(/^\s*/)[0].length : 2;
  return { indent, trailingNewline: text.endsWith('\n') };
}

const serialize = (obj, style) => JSON.stringify(obj, null, style.indent) + (style.trailingNewline ? '\n' : '');

/** Uncommitted paths under the target, or null when git cannot answer. */
function uncommitted() {
  try {
    const out = execFileSync('git', ['status', '--porcelain', '--', fs.realpathSync(TARGET)], {
      cwd: __dirname,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'ignore'],
    });
    return out.split('\n').map((l) => l.trim()).filter(Boolean);
  } catch {
    return null;
  }
}

function main() {
  if (!fs.existsSync(TARGET)) {
    console.error(`Target not found: ${TARGET} (set BASELINE_DIR to a directory under releases/)`);
    process.exit(2);
  }
  const resolved = fs.realpathSync(TARGET);
  console.log(`Target: releases/${BASELINE_DIR}/model_rules`);
  if (resolved !== path.resolve(TARGET)) console.log(`        -> ${resolved}  (symlink resolved)`);
  console.log(`Mode:   ${APPLY ? 'APPLY (files will be written)' : 'dry run (no files written)'}\n`);

  const dirty = uncommitted();
  if (dirty && dirty.length) {
    console.log(`⚠ ${dirty.length} file(s) under the target already have uncommitted changes:`);
    for (const d of dirty.slice(0, 10)) console.log(`    ${d}`);
    if (dirty.length > 10) console.log(`    … and ${dirty.length - 10} more`);
    console.log('  Committing first keeps this normalization reviewable on its own.\n');
  }

  const changes = [];   // { rel, rules: [{ id, from }], text }
  const unsafe = [];    // files whose formatting would not round-trip
  let removedTotal = 0;

  for (const rel of walk(TARGET)) {
    const file = path.join(TARGET, rel);
    const text = fs.readFileSync(file, 'utf8');
    let rules;
    try {
      rules = JSON.parse(text);
    } catch (e) {
      unsafe.push({ rel, why: `invalid JSON (${e.message})` });
      continue;
    }
    const style = styleOf(text);
    if (serialize(rules, style) !== text) {
      unsafe.push({ rel, why: `formatting would change on rewrite (indent ${style.indent}${style.trailingNewline ? '' : ', no trailing newline'})` });
      continue;
    }
    const hits = [];
    for (const id of Object.keys(rules)) {
      if (rules[id].Status !== 'Removed') continue;
      removedTotal++;
      if (rules[id].Order === -1) continue;
      hits.push({ id, from: rules[id].Order });
      rules[id].Order = -1;
    }
    if (hits.length) changes.push({ rel, rules: hits, text: serialize(rules, style) });
  }

  if (unsafe.length) {
    console.log(`⚠ ${unsafe.length} file(s) skipped as unsafe to rewrite:`);
    for (const u of unsafe) console.log(`    ${u.rel}\n      ${u.why}`);
    console.log('  Normalize these by hand, or bring their formatting in line first.\n');
  }

  const ruleCount = changes.reduce((n, c) => n + c.rules.length, 0);
  if (!ruleCount) {
    console.log(`Nothing to do: all ${removedTotal} Removed rule(s) already have Order -1.`);
    return unsafe.length ? 1 : 0;
  }

  console.log(`${ruleCount} of ${removedTotal} Removed rule(s) need Order set to -1, across ${changes.length} file(s):`);
  for (const c of changes) {
    console.log(`  ${c.rel}  (${c.rules.length})`);
    for (const r of c.rules) console.log(`      ${r.id}  Order ${r.from} -> -1`);
  }

  if (!APPLY) {
    console.log('\nDry run only. Re-run with --apply to write these changes.');
    return 0;
  }
  for (const c of changes) fs.writeFileSync(path.join(TARGET, c.rel), c.text);
  console.log(`\n✅ Wrote ${changes.length} file(s). Review with: git diff -- ${path.relative(path.join(__dirname, '..', '..', '..'), resolved)}`);
  return unsafe.length ? 1 : 0;
}

process.exit(main());
