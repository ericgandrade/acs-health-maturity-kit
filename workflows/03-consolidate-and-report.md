# Workflow 03 — Consolidate and Report

**Owner:** Roadmap Strategist · **Time:** 60 minutes plus drafting · **Output:** executive summary, assessment report and remediation roadmap

## Steps

1. **Score** the completed workbook: `python tools/score_assessment.py <workbook.xlsx> results`.
2. **Review results** with the Maturity Lead: overall and service scores, HHS goal status, top gaps, license quick wins, highest-priority applications, unanswered questions.
3. **Prioritize** actions with the method in `agents/roadmap-strategist.md`. Merge related gaps across services.
4. **Draft** the three documents from `templates/`:
   - `executive-summary.md` (one page, for leadership),
   - `assessment-report.md` (full findings),
   - `remediation-roadmap.md` (0–90 days, 3–6 months, 6–18 months).
5. **Quality check** with `checklists/report-quality-checklist.md`; fix every failed item.
6. **Review** the drafts with the organization's accountable owners; record decisions and changes.
7. **Re-assess** after 6–12 months with the same workbook to measure progress.

## Exit criteria

- Quality checklist fully passed.
- Owners have reviewed the roadmap and agreed on the first-horizon actions.
