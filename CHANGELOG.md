# Changelog

All notable changes to this kit are documented here. Versions follow semantic versioning.

## [Unreleased]

### Fixed
- Dashboard charts in Excel: the axis labels were hidden, chart titles overlapped the plot and each point had its own colour. The charts now show the category and value axes, one colour and a title above the plot, and the radar charts have more room for long dimension names.

### Changed
- The README opens with a plain-language explanation of the kit instead of release notes, and text that still described three areas now describes four.
- The sample screenshots in `docs/images/` were recaptured from the current workbook (Excel, illustrative sample answers).

## [0.3.0] — 2026-11-19

### Added
- A fourth scored area, **Automation Readiness**, with 24 questions (AR-01 to AR-24) in six dimensions of four questions each: Process Ownership & Baselines, Data & Integration Readiness, Controls & Human Review, AI Governance & Data Protection, Workforce & Change Management, and Value & Continuous Improvement. It covers prior authorization, eligibility verification, patient intake and referrals, including baselines, standard transactions, interface and API readiness, CMS-0057-F electronic prior authorization planning, automation identities, human review, audit logging, fallback procedures, AI governance, no PHI in prompts, AI vendor assessment and post-go-live monitoring, staff involvement and training, a plan for freed staff time, a pilot and go-live decision, benefit measured against the baseline, review and retirement of automations, and the full cost of automation and AI tools.
- Every new question has `level_0` to `level_3`, `target_state`, evidence, recommended action, the path to levels 2, 3 and 4, weight (1–3), references, healthcare considerations, probing questions, red flags and sources, in the same columns as the existing questions.
- *Automation Readiness* sheet, Dashboard section and radar chart, and Question Guide entries in the workbook; `docs/question-guide.md` and `docs/framework-mapping.md` regenerated from the question bank.
- N/A rules for Automation Readiness in `docs/methodology.md` (AR-09, AR-10, AR-11, AR-16, AR-21 and AR-23 only; AR-12, AR-14, AR-22 and AR-24 are never N/A).
- `tools/cache_values.py` stores calculated formula values in the built workbook (requires the optional `formulas` package), so results display in viewers that do not recalculate, as in earlier releases.

### Changed
- `tools/score_assessment.py` and `tools/build_workbook.py` handle four areas. The scorer still reads v0.2.0 workbooks (three areas).
- The overall score now averages four areas and 100 questions. It is not directly comparable with a v0.2.0 overall score; the per-area, per-dimension and per-question results are comparable (see `docs/methodology.md`).
- README, CITATION and methodology updated for v0.3.0 and the fourth area.

### Unchanged
- All 76 question IDs, dimensions, weights, level anchors, HHS Cybersecurity Performance Goal mappings and scoring rules. The Automation Readiness questions are not mapped to HHS goals, so the CPG Crosswalk is the same as in v0.2.0.
- The five AI agents, the workflows, templates and checklists, and the three playbooks still describe and cover the three original areas. An Automation Readiness agent and playbook are not part of this release.
- Tag `v0.2.0` and the release asset of v0.2.0.

## [0.2.0] — 2026-10-29

### Added
- Observable scoring criteria for levels 0–4 on all 76 questions (`level_0` to `level_3` and `target_state` in `data/questionnaire.csv`; *Maturity levels (0–4)* column in the workbook).
- Interview guidance for every question: probing questions, evidence and how to obtain it, red flags, healthcare considerations, the path to levels 2, 3 and 4, and sources.
- *Question Guide* sheet in the workbook and `docs/question-guide.md`, generated from the question bank.
- Practitioner playbooks: `docs/playbooks/license-optimization.md`, `docs/playbooks/app-modernization.md`, `docs/playbooks/zero-trust.md`.
- New agent commands: `*shelfware` and `*right-size` (License Optimization Analyst), `*runbook` (App Modernization Architect), `*evidence-list` and `*vendor-access` (Zero Trust Assessor).
- `tools/build_docs.py` to regenerate `docs/framework-mapping.md` and `docs/question-guide.md`.
- README: direct download link, a 15-minute test based on the ten HHS Essential Goals, and illustrative screenshots.

### Changed
- All five agents rewritten with interview playbooks, domain knowledge, scoring rules, red flags and output specifications.
- Workflows, report templates, the modernization runbook and the evidence, privacy and report-quality checklists expanded.
- Methodology and how-to guide expanded, including the rule of evidence for choosing a level.
- Evidence and recommended actions rewritten to be specific and actionable; several framework references added.
- License-Security Map re-verified against Microsoft Learn on 2026-10-29; statements remain "typical" and must be checked against your agreement.
- AM-09 now lists *isolate* among the dispositions, matching the kit's disposition list.
- The workbook is saved with calculated values, so results display in viewers that do not recalculate.

### Unchanged
- Question IDs, dimensions, weights, HHS Cybersecurity Performance Goal mappings and scoring rules. Results from v0.1.0 remain comparable.

## [0.1.0] — 2026-10-29

### Added
- Assessment workbook with 76 questions: License Optimization (24), App Modernization (24), Zero Trust (28).
- Dashboard, Priority Gaps and HHS Cybersecurity Performance Goals crosswalk (all 20 goals).
- App Portfolio Triage sheet with technical risk scoring and suggested dispositions.
- License-Security Map for common Microsoft licensing.
- Agent layer: Maturity Lead, License Optimization Analyst, App Modernization Architect, Zero Trust Assessor, Roadmap Strategist.
- Workflows (intake, service assessment, consolidation), modernization runbook template, report templates and quality, evidence and privacy checklists.
- Tools: workbook builder and scoring script.
