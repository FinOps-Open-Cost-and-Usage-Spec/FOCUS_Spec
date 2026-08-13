'use strict';

const { test } = require('node:test');
const assert = require('node:assert');
const { execFileSync } = require('node:child_process');
const { runVerify } = require('./verify');

test('extractor output passes all verification checks', () => {
  // Regenerate so verification runs against output derived from the current markdown
  // and scripts, then assert the audit (structural + transformation) reports no failures.
  execFileSync(process.execPath, ['extract_rm.js'], { cwd: __dirname, stdio: 'ignore' });
  const { fail } = runVerify({ silent: true });
  assert.equal(fail, 0, 'verify reported failures — run `npm run verify` for the per-check breakdown');
});
