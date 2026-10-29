# How to Run an Assessment

A small hospital IT team can complete the assessment in about one to two weeks of part-time effort: roughly five working sessions plus evidence follow-up. This guide gives the schedule, the preparation, the three ways to run it and what to do afterward. The detailed steps are in `workflows/`; the scoring rules are in `docs/methodology.md`.

## Before you start

| Prepare | Why |
|---|---|
| Read `Start Here` in the workbook and `docs/methodology.md` | So the facilitator can explain level anchors and the evidence rule in one sentence. |
| Choose a facilitator | Ideally someone who did not build the controls being assessed; at a small hospital, the IT leader with an AI agent as a neutral second voice works. |
| Agree the purpose with the sponsor | The report is shaped around the decision it supports. |
| Send the Question Guide | The **Question Guide** sheet (or `docs/question-guide.md`) for each service, two working days before its session, so participants can find evidence. |
| Agree evidence handling | Show on screen; record artifact, source and date; no PHI, secrets or addresses (`checklists/privacy-and-safety.md`). |

## Schedule

| Day | Activity | Time | Who | Gate |
|---|---|---|---|---|
| 1 | Intake: Profile, scope, stakeholders, evidence requests (`workflows/01-intake.md`) | 45–60 min | IT leader, sponsor (briefly), privacy/compliance | G1 |
| 2 | License Optimization session; License-Security Map | 60–90 min | IT leader, finance or procurement | G2 |
| 3 | App Modernization session; App Portfolio Triage | 60–90 min | Applications and infrastructure leads, clinical informatics, biomedical engineering | G2 |
| 4 | Zero Trust session; CPG Crosswalk review | 90–120 min | Security lead or IT leader, infrastructure lead, privacy/compliance; managed security provider if any | G2 |
| 5–7 | Evidence follow-up for each service | 30 min each | Evidence owners | — |
| 8 | Score, calibration review | 45 min | Facilitator, IT leader | G3 |
| 8–9 | Consolidation session; drafting (`workflows/03-consolidate-and-report.md`) | 60 min plus drafting | IT leader, CFO, sponsor | — |
| 10 | Quality check and readout | 30–45 min | Sponsor and owners | G4 |

The days need not be consecutive. Avoid go-lives, survey visits and known clinical peaks.

## Scoring a question in four moves

1. **Find the highest anchor that is fully true.** Column D of each service sheet, **Maturity levels (0–4)**, describes what each level looks like for that question. Read from 0 upward; partial coverage takes the level below; score the weakest material part of the scope.
2. **Probe.** Use two or three probing questions from the Question Guide to find where the practice stops.
3. **Check evidence.** A 3 needs a document and system output (or a test result) showing organization-wide coverage, no older than the practice's cycle and never older than 12 months. A 4 also needs a trend and automation or alerting where practical. Without evidence, record per the anchors (2 at most) and add an open item.
4. **Record.** Select the answer in the yellow Answer column; write in Notes the evidence seen, the gap to the next level and any work in progress.

*Illustrative (fictional):* For ZT-01, MFA is enforced on the VPN and email, but two vendor support accounts are excluded with no approval record. The level-3 anchor requires vendor access and documented exceptions, so the answer is 2. Notes: "Access policy list seen in identity provider console, dated this week; vendor accounts excluded without approval; next step: enforce MFA for vendor accounts."

## Option A — Workbook only

1. Open `toolkit/ACS-Health-Maturity-Assessment.xlsx` in Microsoft Excel or LibreOffice Calc. If Excel opens it in Protected View, select **Enable Editing**.
2. Fill the Profile sheet.
3. For each service sheet, read column D and the Question Guide sheet, then answer the yellow cells. Use N/A only when the practice cannot apply, and explain why in Notes.
4. Complete the License-Security Map and App Portfolio Triage sheets.
5. Review the Dashboard, Priority Gaps and CPG Crosswalk sheets; they update automatically.
6. Build the roadmap from `templates/remediation-roadmap.md`, using the prioritization order in `agents/roadmap-strategist.md`.

## Option B — Workbook plus AI agents

1. Open the repository in an AI assistant that can read files (for example Claude Code).
2. Load `agents/acs-maturity-lead.md` (in Claude Code: the `acs-maturity-lead` subagent or the `/acs-assess` command).
3. Run the commands in order: `*start`, `*plan`, `*assess license`, `*assess apps`, `*assess zerotrust`, `*score <file.xlsx>`, `*consolidate`. Use `*status` at any time.
4. The specialists use the service playbooks in `docs/playbooks/` for decision criteria and worked examples.
5. Keep the privacy rules: no PHI, no secrets. Do not upload the workbook to tools your organization has not approved. The agents recommend; your accountable owners decide.

## Option C — Score from the command line

```bash
pip install openpyxl
python tools/score_assessment.py my-assessment.xlsx results
# writes results.json and results.md
```

`results.json` contains `profile`, `overall`, `services` (with `dimensions`), `cpg`, `top_gaps` (up to 20), `license_map`, `top_applications` (up to 10) and `unanswered`. The agents and templates use these field names.

## Common pitfalls

| Pitfall | Avoid it by |
|---|---|
| Scoring intentions ("we're rolling that out") | Scoring what is live today; projects go in Notes. |
| Accepting "we have a tool for that" | Asking to see the policy state and coverage report. |
| One person answering everything | Including at least one non-IT role per session. |
| Using N/A for outsourced or unknown practices | Scoring oversight for outsourced work; leaving unknowns blank with an owner. |
| Loosening the evidence standard at re-assessment | Applying the same thresholds each time so progress is real. |
| A roadmap the team cannot staff | Agreeing a maximum number of concurrent Horizon 1 actions. |

## After the assessment

- Track the roadmap monthly and report Essential goals met and Horizon 1 progress to leadership quarterly.
- Re-assess every 6–12 months with the same workbook and evidence thresholds, and compare `results.json` files.
- Useful public resources for implementation: the Health Industry Cybersecurity Practices released with HHS under the 405(d) effort (https://healthsectorcouncil.org/hicp/), the CISA Known Exploited Vulnerabilities Catalog (https://www.cisa.gov/known-exploited-vulnerabilities-catalog), the ONC SAFER Guides, including Contingency Planning (https://www.healthit.gov/topic/safety/safer-guides), and the Security Risk Assessment Tool (https://www.healthit.gov/topic/privacy-security-and-hipaa/security-risk-assessment-tool).
- Tell us how it went: open an **Adoption report** issue in the repository. It is optional, can be anonymous at the organization level, and helps improve the kit.
