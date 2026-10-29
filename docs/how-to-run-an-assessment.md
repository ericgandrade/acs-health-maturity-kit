# How to Run an Assessment

A small hospital IT team can complete the assessment in about one week of part-time effort.

| Day | Activity | Who |
|---|---|---|
| 1 | Read `Start Here`, fill the Profile sheet, agree participants and evidence (`workflows/01-intake.md`) | IT leader |
| 2 | License Optimization session; complete the License-Security Map | IT leader, procurement/finance |
| 3 | App Modernization session; start the App Portfolio Triage | Applications and infrastructure leads, clinical informatics |
| 4 | Zero Trust session; review the CPG Crosswalk | Security lead, compliance/privacy officer |
| 5 | Score, prioritize and draft the roadmap (`workflows/03-consolidate-and-report.md`) | IT leader with leadership review |

## Option A — Workbook only

1. Open `toolkit/ACS-Health-Maturity-Assessment.xlsx` in Microsoft Excel (or LibreOffice Calc).
2. Answer the yellow cells. The Dashboard, Priority Gaps and CPG Crosswalk update automatically.
3. Copy the priorities into `templates/remediation-roadmap.md`.

## Option B — Workbook plus AI agents

1. Open the repository in an AI coding assistant that can read files (for example Claude Code).
2. Load `agents/acs-maturity-lead.md` (in Claude Code: use the `acs-maturity-lead` subagent or the `/acs-assess` command).
3. Follow the commands: `*start`, `*assess license`, `*assess apps`, `*assess zerotrust`, `*score <file>`, `*consolidate`.
4. Keep the privacy rules: no PHI, no secrets. Do not upload the workbook to tools your organization has not approved.

## Option C — Score from the command line

```bash
pip install openpyxl
python tools/score_assessment.py my-assessment.xlsx results
# writes results.json and results.md
```

## After the assessment

- Re-assess every 6–12 months with the same workbook to measure progress.
- Tell us how it went: open an **Adoption report** issue in the repository. It is optional, can be anonymous at the organization level, and helps improve the kit.
