'use strict';

const fs = require('fs');
const path = require('path');

/**
 * Shared markdown helpers used by the extractor, the verifier, and the validator.
 *
 * Centralized so the rule producer (extract_rm.js) and the checkers (verify.js,
 * validate_markdown.js) derive rendered text and output paths identically — a
 * divergence here previously let HTML-escaped text slip into the output while the
 * verifier, sharing the same flaw, reported all-green.
 */

// marked's token.text HTML-escapes these; decode them back to literal characters
// so MustSatisfy values match the source (and the previous-release baselines).
const ENTITY = { '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&#x27;': "'", '&#x2F;': '/' };

function decodeEntities(s) {
  return s.replace(/&(?:amp|lt|gt|quot|#39|#x27|#x2F);/g, (m) => ENTITY[m]);
}

/** Render inline AST tokens to plain text: keep link/emphasis display text, decode
 *  HTML entities. Recurses into nested tokens so emphasis/link markers are dropped at
 *  the source (a link's `.text` is the RAW inner string, e.g. "*FOCUS dataset column*",
 *  whereas its `.tokens` hold the parsed em). This avoids a blanket `*` strip, so a
 *  literal asterisk (e.g. a multiplication operator) is preserved. */
function renderInline(tokens) {
  const text = (tokens || [])
    .map((t) => (t.tokens && t.tokens.length ? renderInline(t.tokens) : t.text !== undefined ? t.text : ''))
    .join('');
  return decodeEntities(text).trim();
}

/** Normalize a heading's parsed text: drop HTML comments (e.g. <!--SkipTOC-->) and trim. */
function normalizeHeading(text) {
  return text.replace(/<!--.*?-->/g, '').trim();
}

/** Output JSON filename for a dataset folder (e.g. "billing_period" -> "billingperiod.json"). */
function datasetJsonName(folder) {
  return `${folder.replace(/_/g, '')}.json`;
}

/** Dataset folders to process: the DATASET_FOLDERS override, else every subdir with a dataset.md. */
function resolveDatasetFolders(datasetsLocationAbs) {
  if (process.env.DATASET_FOLDERS) {
    return process.env.DATASET_FOLDERS.split(',').map((s) => s.trim()).filter(Boolean);
  }
  return fs.readdirSync(datasetsLocationAbs, { withFileTypes: true })
    .filter((e) => e.isDirectory() && fs.existsSync(path.join(datasetsLocationAbs, e.name, 'dataset.md')))
    .map((e) => e.name)
    .sort();
}

/** Rename a rule's legacy `ApplicabilityCriteria` key to `Conditions`, preserving key order. */
function renameConditions(rule) {
  if (!('ApplicabilityCriteria' in rule)) return rule;
  const out = {};
  for (const k of Object.keys(rule)) out[k === 'ApplicabilityCriteria' ? 'Conditions' : k] = rule[k];
  return out;
}

module.exports = { decodeEntities, renderInline, normalizeHeading, datasetJsonName, resolveDatasetFolders, renameConditions };
