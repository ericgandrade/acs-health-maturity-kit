# Changelog

All notable changes to this kit are documented here. Versions follow semantic versioning.

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
