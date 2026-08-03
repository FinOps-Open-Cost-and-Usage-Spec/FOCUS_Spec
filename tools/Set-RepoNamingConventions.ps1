<#
Applies guidelines/contributors/repository-naming-conventions.md to files
and directories via git mv, updates known references, and validates the
result. Throwaway migration tool for issue #1868.

Usage:
  ./Set-RepoNamingConventions.ps1 -Phase 1
  ./Set-RepoNamingConventions.ps1 -Phase all -SkipValidation
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

# Phase 1: no open-PR conflicts, safe to run immediately.
# Phase 2: gated on PRs touching these paths merging first.
# Phase 3: gated on the 1.5 Consistency Review starting.
# cleanup: everything else needing a rename outside specification/.
$PhaseManifest = @{
    '1'       = @('specification/attributes', 'specification/appendix', 'specification/supported_features', 'specification/data')
    '2'       = @('specification/datasets', 'specification/metadata', 'specification/requirements_model')
    '3'       = @('specification/schemas', 'specification/conditions', 'specification/styles', 'specification/images')
    'cleanup' = @('specification/versions', 'guidelines', 'supporting_content', 'custom_linter_rules')
}

function Get-ScopedRoots {
    param([string]$Phase)
    if ($Phase -eq 'all') {
        return $PhaseManifest.Values | ForEach-Object { $_ } | Where-Object { Test-Path $_ }
    }
    return $PhaseManifest[$Phase] | Where-Object { Test-Path $_ }
}

# Ground truth for FOCUS entity names: EntityId fields in requirements_model rule JSON.
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
    $ext = [System.IO.Path]::GetExtension($Name)
    $base = [System.IO.Path]::GetFileNameWithoutExtension($Name)
    # -creplace: case-sensitive, else [A-Z] also matches lowercase and hyphenates everything
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

# Renames directories shallowest-first; returns updated roots (a root itself may get renamed) + old->new pairs.
function Rename-Directories {
    param([string[]]$Roots, [hashtable]$EntityMap)

    $renames = [ordered]@{}
    $currentRoots = $Roots

    do {
        # Symlinks (e.g. releases/latest) are excluded: -Recurse follows them and double-visits the target.
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
            if (-not (Test-Path $dir.FullName)) { continue }
            $target = Get-TargetName -Name $dir.Name -Extension '' -EntityMap $EntityMap
            if ($target -ne $dir.Name) {
                $relPath = (Resolve-Path -Relative $dir.FullName) -replace '^\.[/\\]', ''
                $parent = Split-Path $relPath -Parent
                $newPath = if ($parent) { Join-Path $parent $target } else { $target }
                Write-Host "  $relPath -> $newPath"
                git mv -- $relPath $newPath
                $renames[$relPath] = $newPath
                $didRename = $true
                # Resolve-Path prefixes "./"; normalize both sides or this silently no-ops.
                $currentRoots = $currentRoots | ForEach-Object {
                    if (($_ -replace '^\.[/\\]', '') -eq $relPath) { $newPath } else { $_ }
                }
            }
        }
    } while ($didRename)  # re-walk: a rename changes its children's discoverable paths

    return @{ Roots = $currentRoots; Renames = $renames }
}

# Fresh file walk after all directory renames complete.
function Rename-Files {
    param([string[]]$Roots, [hashtable]$EntityMap)

    $renames = [ordered]@{}
    $files = foreach ($root in $Roots) {
        if (Test-Path $root) { Get-ChildItem -Path $root -Recurse -File -ErrorAction SilentlyContinue }
    }

    foreach ($file in $files) {
        $ext = $file.Extension.ToLower()
        if ($ext -eq '.py') { continue }  # already snake_case
        if ($file.FullName -match '[\\/]\.github[\\/]|[\\/]\.gemini[\\/]|[\\/]\.claude[\\/]|[\\/]\.cursor[\\/]') { continue }  # tool-owned config

        $target = Get-TargetName -Name $file.Name -Extension $ext -EntityMap $EntityMap
        if ($target -ne $file.Name) {
            $relPath = Resolve-Path -Relative $file.FullName
            $parent = Split-Path $relPath -Parent
            $newPath = if ($parent) { Join-Path $parent $target } else { $target }
            Write-Host "  $relPath -> $newPath"
            git mv -- $relPath $newPath
            $renames[$relPath] = $newPath
        }
    }

    return $renames
}

function Update-References {
    param([System.Collections.Specialized.OrderedDictionary]$Renames)

    $searchFiles = Get-ChildItem -Path 'specification', 'guidelines' -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.md', '.mdpp', '.py' -or $_.Name -eq 'Makefile' }

    foreach ($entry in $Renames.GetEnumerator()) {
        $oldRel = $entry.Key -replace '^\.[/\\]', ''
        $newRel = $entry.Value -replace '^\.[/\\]', ''
        $oldName = Split-Path $oldRel -Leaf
        $newName = Split-Path $newRel -Leaf
        if ($oldName -eq $newName) { continue }

        # Try trailing-path suffixes of oldRel, longest first, so a short suffix
        # (e.g. "datasets/contract_commitment") can't false-match a different,
        # out-of-scope tree sharing that tail (e.g. schemas/datasets/contract_commitment).
        $oldSegments = $oldRel -split '[/\\]'
        $newSegments = $newRel -split '[/\\]'
        $variants = for ($i = 0; $i -lt $oldSegments.Count; $i++) {
            [PSCustomObject]@{
                Old = ($oldSegments[$i..($oldSegments.Count - 1)] -join '/')
                New = ($newSegments[$i..($newSegments.Count - 1)] -join '/')
            }
        }
        $variants = $variants | Sort-Object { $_.Old.Length } -Descending
        # Must start at a real token boundary (quote/paren/whitespace/start), never mid-path after an unrelated "/".
        $tokenStartBoundary = '(?<=["''(\s]|^)'

        foreach ($file in $searchFiles) {
            if (-not (Test-Path $file.FullName)) { continue }
            $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
            if ($null -eq $content) { continue }

            # .py identifiers reuse path basenames constantly (e.g. a model_rules dict var);
            # restrict to whole quoted-string matches so bare identifiers are never touched.
            $requireQuoted = $file.Extension -eq '.py'

            $updated = $content
            foreach ($variant in $variants) {
                $escOld = [regex]::Escape($variant.Old)
                $escOldBackslash = [regex]::Escape(($variant.Old -replace '/', '\'))
                $endBoundary = '(?![\w.-])'

                if ($requireQuoted) {
                    # Whole-string match only; won't reach into a compound string like
                    # 'json_schemas/json_schemas.json' - regex can't reliably tell "inside an
                    # open string" from "after a closed string" earlier on the same line.
                    $pattern = "(?<=['""])$escOld(?=['""])"
                    $patternBackslash = "(?<=['""])$escOldBackslash(?=['""])"
                }
                else {
                    $pattern = "$tokenStartBoundary$escOld$endBoundary"
                    $patternBackslash = "$tokenStartBoundary$escOldBackslash$endBoundary"
                }
                $replacement = $variant.New
                $replacementBackslash = $variant.New -replace '/', '\'

                if ($updated -cmatch $pattern -or $updated -cmatch $patternBackslash) {
                    $updated = $updated -creplace $pattern, $replacement
                    $updated = $updated -creplace $patternBackslash, $replacementBackslash
                    if (-not $requireQuoted) { break }
                }
            }

            if ($updated -ne $content) {
                Set-Content -Path $file.FullName -Value $updated -NoNewline
                Write-Host "  updated ref: $($file.FullName) ($oldName -> $newName)"
            }
        }
    }
}

function Invoke-Validation {
    Write-Host "`n--- Validating build ---" -ForegroundColor Cyan
    $ok = $true

    Push-Location specification
    try {
        Write-Host 'Running pytest...'
        python3 -m pytest requirements_model/tests/ -q
        if ($LASTEXITCODE -ne 0) { $ok = $false; Write-Host 'pytest FAILED' -ForegroundColor Red }

        Push-Location requirements_model
        Write-Host 'Running build_json.py --build-only...'
        python3 build_json.py --build-only
        if ($LASTEXITCODE -ne 0) { $ok = $false; Write-Host 'build_json.py FAILED' -ForegroundColor Red }
        Pop-Location

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
        Write-Host "`nValidation failed. Working tree left dirty for inspection - fix and re-run, or 'git reset --hard' (NOT 'git clean -fd', which deletes this script if untracked)." -ForegroundColor Yellow
        exit 1
    }
    Write-Host "`nValidation passed." -ForegroundColor Green
}

Write-Host "`nDone. Changes are unstaged - review with 'git status' / 'git diff' before committing."
