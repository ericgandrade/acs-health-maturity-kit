# Workflow 03 — Consolidate and Report

**Owner:** Roadmap Strategist, with the ACS Maturity Lead · **Time:** 45-minute calibration review, 60-minute consolidation session, then drafting · **Output:** executive summary, assessment report, remediation roadmap · **Gates:** G3 Calibrated, G4 Report ready

## Roles

| Role | Responsibility |
|---|---|
| ACS Maturity Lead | Runs the calibration review; confirms G3. |
| Roadmap Strategist | Prioritizes, drafts the three documents, runs the quality check. |
| IT leader | Confirms risk and effort factors, owner roles and capacity. |
| CFO | Confirms budget cycle, contract timing and any cost data (organization-provided only). |
| Executive sponsor | Receives the readout; makes the decisions requested. |

## Inputs

- Completed workbook (all three service sheets, License-Security Map, App Portfolio Triage).
- Specialist findings and evidence register.
- Intake purpose and sponsor.
- Previous `results.json`, for re-assessments.

## Step 1 — Score (5 minutes)

```bash
python tools/score_assessment.py <workbook.xlsx> results
# writes results.json and results.md
```

Check `overall.answered` against `overall.questions` and the `unanswered` list. If essential questions are blank, schedule follow-ups before reporting.

## Step 2 — Calibration review (45 minutes, gate G3)

Run section 7 of `agents/acs-maturity-lead.md`: evidence check on every 3 and 4; consistency of shared practices across services (for example LO-11 and ZT-04, LO-14 and ZT-01, AM-17 and ZT-19); specialist drift; N/A audit. Re-score after changes.

**G3 passes when:** every 3/4 cites evidence; every shared-practice difference of more than one level is explained in Notes; the N/A list is justified; `results.json` is regenerated.

## Step 3 — Review results (15 minutes)

With the Lead, read in this order:

1. `cpg` — Essential goals with status Gap or Partially meets.
2. `services[...].dimensions` — the lowest dimensions per service.
3. `top_gaps` — up to 20 gaps by gap points (the Priority Gaps sheet has the full list).
4. `license_map` — items with status `Licensed but not fully deployed (quick win)`.
5. `top_applications` — highest priority (technical risk × criticality).
6. `unanswered` — open items.

## Step 4 — Prioritize (consolidation session, 60 minutes)

Apply the method in `agents/roadmap-strategist.md`, always in this order: (1) gap points from the tool, (2) risk to patient care and PHI, (3) effort, (4) dependency, (5) cost-neutral "already licensed" quick wins. Then apply the two gates: every Essential goal at Gap gets a Horizon 1 action; every hard deadline is met.

| Segment | Time | Output |
|---|---|---|
| Results walkthrough | 10 min | Surprises resolved or logged as scoring questions. |
| Risk to patient care | 15 min | C factor for each top action. |
| Effort and capacity | 15 min | E factor and owner role; realistic number of concurrent Horizon 1 actions for the team size. |
| Funding and constraints | 10 min | Quick wins; budget cycle; renewals. |
| Commitments | 10 min | Three actions to start within 30 days. |

Merge related gaps across services into one action when they share an owner and outcome.

## Step 5 — Draft (drafting time varies)

| Document | Template | Audience | Length |
|---|---|---|---|
| Executive summary | `templates/executive-summary.md` | CEO, board, CFO | One page |
| Assessment report | `templates/assessment-report.md` | IT leader, compliance, auditors | As needed |
| Remediation roadmap | `templates/remediation-roadmap.md` | IT team and owners | Three horizons |

Every number comes from `results.json` or from the organization. Every finding cites question IDs.

## Step 6 — Quality check (gate G4)

Run `checklists/report-quality-checklist.md` with `*qa`. Fix every failed item; do not waive items.

## Step 7 — Readout (30–45 minutes)

Present the executive summary; walk through Horizon 1; ask for the decisions listed. Record decisions and changes in the roadmap.

## Step 8 — Track and re-assess

- Monthly: update the roadmap Status column and indicators.
- Quarterly: report the Essential goal count and Horizon 1 progress to leadership.
- Every 6–12 months: re-assess with the same workbook **and the same evidence thresholds**, and compare `results.json` files.

## Outputs

- `results.json`, `results.md`.
- Executive summary, assessment report, remediation roadmap.
- Decision log from the readout.

## Exit criteria

- G3 and G4 passed.
- Owners have reviewed the roadmap and agreed the Horizon 1 actions.
- Open evidence items and unanswered questions have owner roles.
