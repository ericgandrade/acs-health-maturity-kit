#!/usr/bin/env bash
# Copies the Claude Code agents/commands and the GitHub issue forms into place.
# Run once from the repository root before your first commit:  bash tools/install_integrations.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .claude .github
cp -R integrations/claude-code/agents integrations/claude-code/commands .claude/
cp -R integrations/github/ISSUE_TEMPLATE .github/
echo "Installed .claude/agents, .claude/commands and .github/ISSUE_TEMPLATE"
