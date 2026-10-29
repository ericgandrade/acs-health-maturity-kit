# Agent Layer

A lightweight, file-based agent method for running ACS Health Maturity assessments with an AI assistant. Each agent is a plain Markdown file that defines a role, a mission, activation steps, commands and rules. The approach is inspired by the agent-persona pattern popularized by the open-source BMAD Method, simplified for a single purpose: assessing and improving healthcare technology maturity.

## Roster

| Agent | File | Responsibility |
|---|---|---|
| ACS Maturity Lead | `acs-maturity-lead.md` | Orchestrates the assessment, hands off to specialists, runs scoring |
| License Optimization Analyst | `license-optimization-analyst.md` | LO-01 to LO-24, License-Security Map, quick wins |
| App Modernization Architect | `app-modernization-architect.md` | AM-01 to AM-24, App Portfolio Triage, modernization waves |
| Zero Trust Assessor | `zero-trust-assessor.md` | ZT-01 to ZT-28, HHS goals, ransomware readiness |
| Roadmap Strategist | `roadmap-strategist.md` | Consolidation, prioritization, report, executive summary, roadmap |

## How the pieces fit

```
agents/      who does the work (roles, commands, rules)
workflows/   how the work is done, step by step
templates/   what the outputs look like
checklists/  how quality, evidence, privacy and safety are checked
data/        the questions and reference data (single source of truth)
tools/       scripts: build the workbook, score a completed assessment
toolkit/     the Excel workbook used by the organization
```

Flow: `*start` (intake) → `*assess license` / `*assess apps` / `*assess zerotrust` → `*score` → `*consolidate` (report and roadmap) → `*qa`.

## Using the agents

**Claude Code.** Open the repository folder. Subagents are provided in `.claude/agents/` and the `/acs-assess` command in `.claude/commands/` starts the Maturity Lead. (Their source is in `integrations/claude-code/`; `tools/install_integrations.sh` copies them into place.)

**Other assistants (ChatGPT, Copilot, Gemini and others).** Paste the content of `checklists/privacy-and-safety.md` followed by the agent file as the first message or system instructions, then attach or paste the questions for the service from `data/questionnaire.csv`.

**Rules for every agent:** no PHI, no secrets, evidence over intent, no invented facts, advisory only. See `checklists/privacy-and-safety.md`.

## Extending the method

Each new method published in this kit follows the same pattern:

1. Add questions to `data/questionnaire.csv` (new IDs, mapped to frameworks).
2. Add or update an agent file with commands for the method.
3. Add a workflow, a template and checklist items if needed.
4. Rebuild the workbook with `python tools/build_workbook.py`, update `CHANGELOG.md` and tag a release.
