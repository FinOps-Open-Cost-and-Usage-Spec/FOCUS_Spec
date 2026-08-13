#!/usr/bin/env node
'use strict';

/**
 * Structural validator for the specification markdown the extractor consumes.
 *
 * Confirms each in-scope entity file is written the way extract_rm.js expects, and
 * reports every violation with a file:line location. Validates (per the contract's
 * Headings for the entity):
 *   - the required "## <Requirements>", "## <Id>", "## <DisplayName>" sections exist (once each)
 *   - the Id value is a single PascalCase token; the Display Name is a single value
 *   - the Requirements section opens with an anchor paragraph ending in
 *     "adhere to the following requirements:" followed by a bullet list
 *   - every requirement bullet uses a "*" marker and contains a BCP-14 keyword
 *
 * Used as a library (validateEntity / collectErrors) by the test suite, and as a
 * CLI that prints all errors and exits non-zero when any file is malformed.
 */

const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
const { renderInline, normalizeHeading, resolveDatasetFolders } = require('./markdown_util');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..');
const CONTRACT_PATH = path.join(__dirname, 'requirements_model_contract.json');

const BCP14_KEYWORD = /\b(MUST NOT|MUST|SHALL NOT|SHALL|SHOULD NOT|SHOULD|MAY)\b/;
const ANCHOR_SUFFIX = /adhere to the following requirements:$/;

const stripComment = normalizeHeading;

/**
 * Validate one entity's markdown. Returns an array of { file, line, message }.
 * `headings` is { Requirements, Id, DisplayName } (the contract's heading names).
 */
function validateEntity(content, file, headings) {
  const errors = [];
  const add = (line, message) => errors.push({ file, line, message });

  let tokens;
  try {
    tokens = marked.lexer(content);
  } catch (e) {
    add(1, `Markdown failed to parse: ${e.message}`);
    return errors;
  }

  // Absolute char offset of each top-level token, for line lookup.
  const offsetOf = new Map();
  let pos = 0;
  for (const t of tokens) { offsetOf.set(t, pos); pos += t.raw.length; }
  const lineAt = (offset) => content.slice(0, offset).split('\n').length;
  const headingLine = (t) => lineAt(offsetOf.get(t));

  const headings2 = tokens.filter((t) => t.type === 'heading' && t.depth === 2);
  const matching = (name) => headings2.filter((h) => stripComment(h.text) === name);

  // Required sections present exactly once.
  for (const key of ['Requirements', 'Id', 'DisplayName']) {
    const name = headings[key];
    const found = matching(name);
    if (found.length === 0) add(1, `Missing required "## ${name}" section`);
    else if (found.length > 1) add(headingLine(found[1]), `Duplicate "## ${name}" section`);
  }

  const bodyAfter = (name) => {
    const h = matching(name)[0];
    if (!h) return null;
    const idx = tokens.indexOf(h);
    const body = [];
    for (let i = idx + 1; i < tokens.length; i++) {
      if (tokens[i].type === 'heading' && tokens[i].depth <= 2) break;
      body.push(tokens[i]);
    }
    return { heading: h, body };
  };

  // Id / Display Name single value (Id must be PascalCase, no spaces).
  for (const key of ['Id', 'DisplayName']) {
    const sec = bodyAfter(headings[key]);
    if (!sec) continue;
    const para = sec.body.find((t) => t.type === 'paragraph');
    if (!para) { add(headingLine(sec.heading), `"## ${headings[key]}" section has no value`); continue; }
    const value = renderInline(para.tokens);
    if (key === 'Id' && !/^[A-Za-z][A-Za-z0-9]*$/.test(value)) {
      add(lineAt(offsetOf.get(para)), `${headings.Id} "${value}" must be PascalCase with no spaces`);
    }
  }

  // Requirements structure.
  const req = bodyAfter(headings.Requirements);
  if (req) {
    const anchor = req.body.find((t) => t.type === 'paragraph');
    const list = req.body.find((t) => t.type === 'list');
    if (!anchor) add(headingLine(req.heading), 'Requirements section is missing its anchor paragraph');
    else if (!ANCHOR_SUFFIX.test(renderInline(anchor.tokens))) {
      add(lineAt(offsetOf.get(anchor)), 'Requirements anchor must end with "adhere to the following requirements:"');
    }
    if (!list) add(headingLine(req.heading), 'Requirements section is missing a bullet list');
    else checkBullets(list, offsetOf.get(list));
  }

  function checkBullets(list, baseOffset) {
    let offset = baseOffset;
    for (const item of list.items) {
      const line = lineAt(offset);
      const firstChar = item.raw.replace(/^\s*/, '')[0];
      if (firstChar && firstChar !== '*') add(line, `Requirement bullet must use a "*" marker, found "${firstChar}"`);
      const textToken = item.tokens.find((t) => t.type === 'text');
      const text = textToken ? renderInline(textToken.tokens) : '';
      if (text && !BCP14_KEYWORD.test(text)) {
        add(line, `Requirement bullet has no BCP-14 keyword (MUST/SHOULD/MAY): "${text.slice(0, 60)}"`);
      }
      const sub = item.tokens.find((t) => t.type === 'list');
      if (sub) {
        const rel = item.raw.indexOf(sub.raw);
        if (rel >= 0) checkBullets(sub, offset + rel);
      }
      offset += item.raw.length;
    }
  }

  return errors;
}

/** Collect validation errors across every in-scope markdown file, driven by the contract. */
function collectErrors() {
  const contract = JSON.parse(fs.readFileSync(CONTRACT_PATH, 'utf8'));
  const rel = (p) => path.relative(REPO_ROOT, p);
  const errors = [];

  const dm = contract.DataModel;
  const dmPath = path.join(REPO_ROOT, dm.Location);
  errors.push(...validateEntity(fs.readFileSync(dmPath, 'utf8'), rel(dmPath), dm.Headings));

  for (const folder of resolveDatasetFolders(path.join(REPO_ROOT, contract.Datasets.Location))) {
    const ds = contract.Datasets;
    const dsPath = path.join(REPO_ROOT, ds.Location, folder, 'dataset.md');
    errors.push(...validateEntity(fs.readFileSync(dsPath, 'utf8'), rel(dsPath), ds.Headings));

    const cc = contract.Columns;
    const colDir = path.join(REPO_ROOT, ds.Location, folder, 'columns');
    for (const f of fs.readdirSync(colDir).filter((n) => n.endsWith('.md'))) {
      const colPath = path.join(colDir, f);
      errors.push(...validateEntity(fs.readFileSync(colPath, 'utf8'), rel(colPath), cc.Headings));
    }
  }
  return errors;
}

function main() {
  const errors = collectErrors();
  if (errors.length === 0) {
    console.log('✅ All in-scope specification markdown is structurally valid.');
    return;
  }
  for (const e of errors) console.error(`${e.file}:${e.line}: ${e.message}`);
  console.error(`\n❌ ${errors.length} markdown validation error(s).`);
  process.exit(1);
}

if (require.main === module) main();

module.exports = { validateEntity, collectErrors };
