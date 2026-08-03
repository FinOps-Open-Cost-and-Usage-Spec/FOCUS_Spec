<#
Applies FOCUS repository naming conventions (guidelines/contributors/repository-naming-conventions.md)
to files and directories, updates known references, and validates the result.

Throwaway migration tool for issue #1868 - not intended to live long-term.

Rules encoded:
  - FOCUS entity files/dirs (matched via requirements_model EntityId) -> match entity id, no separator
  - Python (.py) files -> left untouched, already snake_case by convention
  - requirements_model rule JSON files -> match entity id (handled by entity map)
  - Tool-owned config (.github, .gemini, etc.) -> left untouched
  - Everything else (.md, .mdpp, .json, .yaml, .css, .csv, images) -> kebab-case

Directories are renamed shallowest-first in one pass, then the tree is
re-walked fresh for files, since a directory rename changes every path
beneath it - renaming files first (or deepest-dir-first) corrupts paths
mid-run.

Rename pairs are tracked explicitly as they're performed, rather than
re-derived from `git status` afterwards - git's rename detection is
content-similarity based and mis-pairs same-named files with similar
content across sibling directories (e.g. scenario CSVs), which corrupts
reference updates if trusted as ground truth.

Usage:
  ./Rename-RepoToConvention.ps1 -Phase 1
  ./Rename-RepoToConvention.ps1 -Phase all -SkipValidation
#>

[CmdletBinding()]
param(
    [ValidateSet('1', '2', '3', 'cleanup', 'all')]
    [string]$Phase = 'all',

    [switch]$SkipValidation
)

$ErrorActionPreference = 'Stop'
$RepoRoot = (git rev-parse --show-toplevel).Trim()
Set-Location $RepoRoot

# --- Phase manifest -----------------------------------------------------
# Paths (relative to repo root) in scope per phase. 'all' unions every phase.
# Phase 1: no open-PR conflicts, safe to run immediately.
# Phase 2: gated on PRs touching these paths merging first.
# Phase 3: gated on the 1.5 Consistency Review starting.
# cleanup: leftover top-level / misc paths, run last.
$PhaseManifest = @{
    '1'       = @('specification/attributes', 'specification/appendix', 'specification/supported_features', 'specification/data')
    '2'       = @('specification/datasets', 'specification/metadata', 'specification/requirements_model')
    '3'       = @('specification/schemas', 'specification/conditions', 'specification/styles', 'specification/images')
    'cleanup' = @('guidelines', 'supporting_content')
}

function Get-ScopedRoots {
    param([string]$Phase)
    if ($Phase -eq 'all') {
        return $PhaseManifest.Values | ForEach-Object { $_ } | Where-Object { Test-Path $_ }
    }
    return $PhaseManifest[$Phase] | Where-Object { Test-Path $_ }
}

# --- Entity map -----------------------------------------------------------
# Ground truth for "this file/dir defines a FOCUS entity": EntityId fields
# in requirements_model rule JSON. Lowercased EntityId is the target name.
function Get-EntityMap {
    $map = @{}
    $ruleFiles = Get-ChildItem -Path 'specification/requirements_model' -Recurse -Filter '*.json' -File -ErrorAction SilentlyContinue
    foreach ($file in $ruleFiles) {
        $json = Get-Content $file.FullName -Raw | ConvertFrom-Json -AsHashtable
        foreach ($rule in $json.Values) {
            if ($rule.EntityId) {
                $map[$rule.EntityId.ToLower()] = $rule.EntityId
            }
        }
    }
    return $map
}

function ConvertTo-KebabCase {
    param([string]$Name)
    # snake_case / camelCase / space separated -> kebab-case, extension preserved
    $ext = [System.IO.Path]::GetExtension($Name)
    $base = [System.IO.Path]::GetFileNameWithoutExtension($Name)
    # case-sensitive replace: PowerShell -replace is case-insensitive by default,
    # which would match [A-Z] against lowercase letters too and hyphenate everything
    $kebab = $base -creplace '([a-z0-9])([A-Z])', '$1-$2'
    $kebab = $kebab -replace '_', '-' -replace ' ', '-'
    $kebab = $kebab -replace '-+', '-'
    return $kebab.ToLower() + $ext
}

function Get-TargetName {
    param([string]$Name, [string]$Extension, [hashtable]$EntityMap)
    $base = if ($Extension) { [System.IO.Path]::GetFileNameWithoutExtension($Name) } else { $Name }
    $key = $base.ToLower().Replace('_', '').Replace('-', '')
    if ($EntityMap.ContainsKey($key)) {
        return $EntityMap[$key].ToLower() + $Extension
    }
    return ConvertTo-KebabCase $Name
}

# --- Directory rename (shallowest first) -----------------------------------------------------
# Returns @{ Roots = <updated root paths>; Renames = <ordered old->new pairs> }.
# Roots are returned because a root itself (e.g. supported_features) may be
# renamed, and callers need the new location to walk for files.
function Rename-Directories {
    param([string[]]$Roots, [hashtable]$EntityMap)

    $renames = [ordered]@{}
    $currentRoots = $Roots

    do {
        # Roots are rename candidates too (e.g. specification/supported_features
        # itself), not just their contents, so seed them into the same walk.
        # Symlinks (e.g. requirements_model/releases/latest -> 1.5) are
        # excluded: -Recurse follows them, which double-visits the target
        # subtree under two different logical paths and corrupts git mv.
        $dirs = foreach ($root in $currentRoots) {
            if (Test-Path $root) {
                Get-Item -Path $root
                Get-ChildItem -Path $root -Recurse -Directory -ErrorAction SilentlyContinue |
                    Where-Object { -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) }
            }
        }
        $dirs = $dirs | Sort-Object { $_.FullName.Split([IO.Path]::DirectorySeparatorChar).Count }

        $didRename = $false
        foreach ($dir in $dirs) {
            if (-not (Test-Path $dir.FullName)) { continue }  # renamed already via an ancestor
            $target = Get-TargetName -Name $dir.Name -Extension '' -EntityMap $EntityMap
            if ($target -ne $dir.Name) {
                $relPath = (Resolve-Path -Relative $dir.FullName) -replace '^\.[/\\]', ''
                $newPath = Join-Path (Split-Path $relPath -Parent) $target
                Write-Host "  $relPath -> $newPath"
                git mv -- $relPath $newPath
                $renames[$relPath] = $newPath
                $didRename = $true

                # If a root itself just got renamed, update it in place so the
                # next iteration (and the final return) reflects the new path.
                # Resolve-Path prefixes relative paths with "./", so both sides
                # must be normalized before comparing or this silently no-ops.
                $currentRoots = $currentRoots | ForEach-Object {
                    if (($_ -replace '^\.[/\\]', '') -eq $relPath) { $newPath } else { $_ }
                }
            }
        }
    } while ($didRename)  # re-walk: renaming a shallow dir changes its children's discoverable paths

    return @{ Roots = $currentRoots; Renames = $renames }
}

# --- File rename (fresh walk, after all directory renames) -----------------------------------------------------
function Rename-Files {
    param([string[]]$Roots, [hashtable]$EntityMap)

    $renames = [ordered]@{}
    $files = foreach ($root in $Roots) {
        if (Test-Path $root) { Get-ChildItem -Path $root -Recurse -File -ErrorAction SilentlyContinue }
    }

    foreach ($file in $files) {
        $ext = $file.Extension.ToLower()
        if ($ext -eq '.py') { continue }  # snake_case already, leave alone
        if ($file.FullName -match '[\\/]\.github[\\/]|[\\/]\.gemini[\\/]|[\\/]\.claude[\\/]|[\\/]\.cursor[\\/]') { continue }  # tool-owned config

        $target = Get-TargetName -Name $file.Name -Extension $ext -EntityMap $EntityMap
        if ($target -ne $file.Name) {
            $relPath = Resolve-Path -Relative $file.FullName
            $newPath = Join-Path (Split-Path $relPath -Parent) $target
            Write-Host "  $relPath -> $newPath"
            git mv -- $relPath $newPath
            $renames[$relPath] = $newPath
        }
    }

    return $renames
}

# --- Reference updaters -----------------------------------------------------
function Update-References {
    param([System.Collections.Specialized.OrderedDictionary]$Renames)

    # Text files likely to reference paths that just moved: spec markdown/mdpp,
    # the Makefile, and the requirements_model Python test/build sources.
    $searchFiles = Get-ChildItem -Path 'specification', 'guidelines' -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.md', '.mdpp', '.py' -or $_.Name -eq 'Makefile' }

    foreach ($entry in $Renames.GetEnumerator()) {
        $oldRel = $entry.Key -replace '^\.[/\\]', ''
        $newRel = $entry.Value -replace '^\.[/\\]', ''
        $oldName = Split-Path $oldRel -Leaf
        $newName = Split-Path $newRel -Leaf
        if ($oldName -eq $newName) { continue }

        # References use relative paths of varying depth (bare basename in a
        # sibling !INCLUDE, "dir/name" from one level up, deeper paths from
        # further away), so the old full path can't be matched as one fixed
        # string. Instead try progressively shorter trailing-path suffixes of
        # oldRel (full path first, down to bare basename) against each file's
        # content. Every variant's START must sit at a real token boundary
        # (quote/paren/whitespace/start-of-string) - never mid-path, right
        # after an unrelated "/" - otherwise a short suffix like
        # "datasets/contract_commitment" would false-match inside a
        # different, out-of-scope tree that happens to share that tail
        # (e.g. schemas/datasets/contract_commitment).
        $oldSegments = $oldRel -split '[/\\]'
        $newSegments = $newRel -split '[/\\]'
        $variants = for ($i = 0; $i -lt $oldSegments.Count; $i++) {
            [PSCustomObject]@{
                Old = ($oldSegments[$i..($oldSegments.Count - 1)] -join '/')
                New = ($newSegments[$i..($newSegments.Count - 1)] -join '/')
            }
        }
        # Longest (most specific) suffix first.
        $variants = $variants | Sort-Object { $_.Old.Length } -Descending
        # A variant's start must be a genuine token boundary: quote, paren,
        # whitespace, or start-of-string/line - NOT a "/" (which would mean
        # the variant is a mid-path tail of some longer, possibly unrelated,
        # path). Only the single longest (full-relative-path) variant is
        # allowed to start right after a "/" mid-token, since that case is
        # covered separately by the token-start anchor already matching its
        # own leading segment.
        $tokenStartBoundary = '(?<=["''(\s]|^)'

        foreach ($file in $searchFiles) {
            if (-not (Test-Path $file.FullName)) { continue }
            $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
            if ($null -eq $content) { continue }

            # Python source reuses directory/file basenames as plain
            # identifiers constantly (e.g. a "model_rules" dict variable,
            # unrelated to the model_rules/ directory), so a bare word-boundary
            # match is not enough to prove it's a path reference. Restrict .py
            # files to rewriting only inside quoted string literals, which is
            # how this codebase spells path segments
            # (os.path.join(x, 'model_rules'), 'json_schemas/json_schemas.json').
            $requireQuoted = $file.Extension -eq '.py'

            $updated = $content
            foreach ($variant in $variants) {
                $escOld = [regex]::Escape($variant.Old)
                $escOldBackslash = [regex]::Escape(($variant.Old -replace '/', '\'))
                $endBoundary = '(?![\w.-])'

                if ($requireQuoted) {
                    # Match ONLY a whole quoted string literal that is
                    # exactly the old name/path, bounded by matching quotes on
                    # both sides ('model_rules' or "model_rules.json"). This
                    # deliberately does not try to reach into a compound
                    # string like 'json_schemas/json_schemas.json' where only
                    # part of it is the old name - a regex can't reliably tell
                    # "inside an open string" from "after a closed string"
                    # (e.g. model['ModelRules'] = model_rules has a same-line
                    # closed 'ModelRules' string immediately before the bare
                    # identifier, which a prefix-scanning approach mistakes
                    # for still being inside quotes). Being conservative here
                    # means a same-file compound path may need a manual
                    # follow-up fix; it will surface via the validation step.
                    $pattern = "(?<=['""])$escOld(?=['""])"
                    $patternBackslash = "(?<=['""])$escOldBackslash(?=['""])"
                    $replacement = $variant.New
                    $replacementBackslash = $variant.New -replace '/', '\'
                }
                else {
                    # The match must start at a genuine token boundary
                    # (quote/paren/whitespace/start-of-string), never mid-path
                    # right after an unrelated "/" - see $tokenStartBoundary
                    # comment above for why.
                    $pattern = "$tokenStartBoundary$escOld$endBoundary"
                    $patternBackslash = "$tokenStartBoundary$escOldBackslash$endBoundary"
                    $replacement = $variant.New
                    $replacementBackslash = $variant.New -replace '/', '\'
                }

                if ($updated -cmatch $pattern -or $updated -cmatch $patternBackslash) {
                    $updated = $updated -creplace $pattern, $replacement
                    $updated = $updated -creplace $patternBackslash, $replacementBackslash
                    if (-not $requireQuoted) { break }  # non-.py: most specific variant matched, stop
                }
            }

            if ($updated -ne $content) {
                Set-Content -Path $file.FullName -Value $updated -NoNewline
                Write-Host "  updated ref: $($file.FullName) ($oldName -> $newName)"
            }
        }
    }
}

# --- Validation -----------------------------------------------------------
function Invoke-Validation {
    Write-Host "`n--- Validating build ---" -ForegroundColor Cyan
    $ok = $true

    Push-Location specification
    try {
        Write-Host 'Running pytest...'
        python3 -m pytest requirements_model/tests/ -q
        if ($LASTEXITCODE -ne 0) { $ok = $false; Write-Host 'pytest FAILED' -ForegroundColor Red }

        Write-Host 'Running build_json.py --build-only...'
        python3 requirements_model/build_json.py --build-only
        if ($LASTEXITCODE -ne 0) { $ok = $false; Write-Host 'build_json.py FAILED' -ForegroundColor Red }

        Write-Host 'Running make force=1...'
        make force=1
        if ($LASTEXITCODE -ne 0) { $ok = $false; Write-Host 'make FAILED' -ForegroundColor Red }
    }
    finally {
        Pop-Location
    }

    return $ok
}

# --- Main -----------------------------------------------------------
Write-Host "Building entity map from requirements_model..."
$entityMap = Get-EntityMap
Write-Host "  $($entityMap.Count) entities found"

$roots = Get-ScopedRoots -Phase $Phase
Write-Host "Phase '$Phase' scoped roots: $($roots -join ', ')"

if (-not $roots) {
    Write-Host 'No roots in scope for this phase.'
    exit 0
}

Write-Host "`n--- Renaming directories ---" -ForegroundColor Cyan
$dirResult = Rename-Directories -Roots $roots -EntityMap $entityMap
$updatedRoots = $dirResult.Roots
$dirRenames = $dirResult.Renames

Write-Host "`n--- Renaming files ---" -ForegroundColor Cyan
$fileRenames = Rename-Files -Roots $updatedRoots -EntityMap $entityMap

Write-Host "`n$($dirRenames.Count) directories, $($fileRenames.Count) files renamed."

if ($dirRenames.Count -eq 0 -and $fileRenames.Count -eq 0) {
    Write-Host 'Nothing to rename.'
    exit 0
}

$allRenames = [ordered]@{}
foreach ($e in $dirRenames.GetEnumerator()) { $allRenames[$e.Key] = $e.Value }
foreach ($e in $fileRenames.GetEnumerator()) { $allRenames[$e.Key] = $e.Value }

Write-Host "`n--- Updating references ---" -ForegroundColor Cyan
Update-References -Renames $allRenames

if (-not $SkipValidation) {
    $passed = Invoke-Validation
    if (-not $passed) {
        Write-Host "`nValidation failed. Working tree left dirty for inspection - fix and re-run validation, or revert with 'git reset --hard' (NOT 'git clean -fd', which would also delete this script if it's untracked)." -ForegroundColor Yellow
        exit 1
    }
    Write-Host "`nValidation passed." -ForegroundColor Green
}

Write-Host "`nDone. Changes are unstaged - review with 'git status' / 'git diff' before committing."
