# Set repo secret AUTOMERGE_TOKEN so Release Please / Dependabot merges trigger push CI.
# Usage: pwsh scripts/setup-automerge-token.ps1
# Optional: $env:AUTOMERGE_TOKEN = "ghp_..."  (otherwise uses `gh auth token`)
$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  Write-Error "ERROR: gh CLI required"
  exit 1
}

$Token = $env:AUTOMERGE_TOKEN
if ([string]::IsNullOrWhiteSpace($Token)) {
  $Token = (gh auth token 2>$null)
}
if ([string]::IsNullOrWhiteSpace($Token)) {
  Write-Error "ERROR: set AUTOMERGE_TOKEN env or run gh auth login"
  exit 1
}

gh secret set AUTOMERGE_TOKEN --body $Token
$repo = gh repo view --json nameWithOwner -q .nameWithOwner
Write-Host "OK AUTOMERGE_TOKEN set on $repo"
Write-Host "Note: classic PATs with workflow scope, or fine-grained tokens with Contents+Workflows, work best."
