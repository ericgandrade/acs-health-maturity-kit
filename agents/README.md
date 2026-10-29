# Agent Layer

A lightweight, file-based agent method for running ACS Health Maturity assessments with an AI assistant. Each agent is a plain Markdown file that defines a role, a mission, activation steps, commands, an interview playbook, domain knowledge, scoring rules, an output specification, guardrails and a handoff protocol. The approach is inspired by the agent-persona pattern popularized by the open-source BMAD Method, simplified for a single purpose: assessing and improving healthcare technology maturity.

## Roster

| Agent | File | Responsibility | Key commands |
|---|---|---|---|
| ACS Maturity Lead | `acs-maturity-lead.md` | Engagement setup, stakeholder map, evidence governance, cross-service score calibration, quality gates, scoring | `*start` `*plan` `*assess <service>` `*score` `*consolidate` `*status` |
| License Optimization Analyst | `license-optimization-analyst.md` | LO-01 to LO-24, License-Security Map, licensed-but-not-deployed quick wins | see file |
| App Modernization Architect | `app-modernization-architect.md` | AM-01 to AM-24, App Portfolio Triage, dispositions and modernization waves | see file |
| Zero Trust Assessor | `zero-trust-assessor.md` | ZT-01 to ZT-28, HHS goals, ransomware readiness | see file |
| Roadmap Strategist | `roadmap-strategist.md` | Prioritization, sequencing, report, executive summary, roadmap, quality check | `*prioritize` `*roadmap` `*report` `*exec-summary` `*qa` |

## How the pieces fit

```
agents/          who does the work (roles, commands, rules)
workflows/       how the work is done, step by step, with time boxes and quality gates
templates/       what the outputs look like
checklists/      how quality, evidence, privacy and safety are checked
docs/            method, how-to, framework mapping, Question Guide and service playbooks
data/            the questions and reference data (single source of truth)
tools/           scripts: build the workbook, score a completed assessment
toolkit/         the Excel workbook used by the organization
```

### What each agent reads

| Source | Used for |
|---|---|
| `data/questionnaire.csv` | Questions, weights, HHS goal mapping, level anchors (`level_0` to `level_4`), probing questions, evidence, red flags, healthcare considerations, next-step actions and sources. |
| Workbook column D **Maturity levels (0–4)** and the **Question Guide** sheet | The same anchors and guidance, inside Excel, during the session. |
| `docs/question-guide.md` | The Question Guide as a readable document, generated from the CSV. |
| `docs/methodology.md` | Scale, evidence thresholds, N/A rules and scoring. |
| `docs/playbooks/license-optimization.md`, `docs/playbooks/app-modernization.md`, `docs/playbooks/zero-trust.md` | Practitioner guidance per service: method, decision criteria, worked examples, quick wins, common mistakes. |
| `results.json` from `tools/score_assessment.py` | Scores, HHS goal status, top gaps, license quick wins and top applications for consolidation. |

## Flow

```
*start ──► *plan ──► G1 ──► *assess license ─┐
                            *assess apps ────┼──► G2 per service ──► *score ──► calibration (G3)
                            *assess zerotrust┘
                                                       │
                     *consolidate ──► *prioritize ──► *roadmap / *report / *exec-summary ──► *qa (G4) ──► readout
```

| Gate | Meaning |
|---|---|
| G1 Plan approved | Profile, scope, participants and evidence requests agreed. |
| G2 Service complete | Every question answered, N/A with reason, or listed as open; every 3 or 4 cites evidence. |
| G3 Calibrated | Shared practices scored consistently across services; re-scored. |
| G4 Report ready | Report quality checklist fully passed. |

Details are in `workflows/01-intake.md`, `workflows/02-service-assessment.md` and `workflows/03-consolidate-and-report.md`.

## Using the agents

**Claude Code.** Open the repository folder. Subagents are provided in `.claude/agents/` and the `/acs-assess` command in `.claude/commands/` starts the Maturity Lead. (Their source is in `integrations/claude-code/`; `tools/install_integrations.sh` copies them into place.)

**Other assistants (ChatGPT, Copilot, Gemini and others).** Paste the content of `checklists/privacy-and-safety.md` followed by the agent file as the first message or system instructions, then attach or paste the questions for the service from `data/questionnaire.csv` (or the relevant part of `docs/question-guide.md`) and, for a specialist, its playbook.

**Rules for every agent:** no PHI, no secrets, evidence over intent, no invented facts, advisory only. See `checklists/privacy-and-safety.md`.

## Extending the method

Each new method published in this kit follows the same pattern:

1. Add questions to `data/questionnaire.csv` (new IDs, mapped to frameworks), with all v0.2 fields: level anchors, probing questions, evidence, red flags, healthcare considerations, actions and sources.
2. Add or update an agent file with commands for the method, following the section order used by the existing agents.
3. Add a workflow, a template, a playbook in `docs/playbooks/` and checklist items if needed.
4. Rebuild the workbook with `python tools/build_workbook.py`, regenerate `docs/question-guide.md`, update `CHANGELOG.md` and tag a release.
