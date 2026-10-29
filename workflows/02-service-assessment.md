# Workflow 02 — Service Assessment

**Owner:** the specialist agent for the service · **Time:** 60–90 minutes per service · **Output:** answered questionnaire sheet, findings and open questions

## Steps

1. **Load the questions** for the service from `data/questionnaire.csv`, grouped by dimension.
2. **For each dimension:**
   1. Read the question and the "What 4 – Optimized looks like" statement.
   2. Ask what is in place today and what evidence shows it (use the Evidence column).
   3. Propose an answer on the 0–4 scale and explain why, using the scale in `docs/methodology.md`.
   4. If the participant claims 3 or 4, confirm the evidence. Without evidence, propose 2 at most and record the evidence as an open item.
   5. Record the agreed answer in the yellow Answer column and any context in Notes (no PHI, no secrets).
   6. Use N/A only when the practice genuinely does not apply (for example, no cloud use at all) and explain why in Notes.
3. **Close the dimension:** summarize the dimension score and the main gap in one sentence; confirm with the participant.
4. **Service-specific tools:**
   - License Optimization → complete the License-Security Map sheet.
   - App Modernization → complete the App Portfolio Triage sheet.
   - Zero Trust → review the CPG Crosswalk sheet.
5. **Score:** run `python tools/score_assessment.py <workbook.xlsx>`.
6. **Findings:** produce the service section of `templates/assessment-report.md`.

## Calibration guidance

| If you hear… | Typical answer |
|---|---|
| "We don't do that." | 0 |
| "One person does it when they have time." | 1 |
| "It's done for some systems / sites, or there's a draft policy." | 2 |
| "It's documented and done everywhere; I can show you." | 3 |
| "It's measured, reviewed and automated; here is the report." | 4 |

## Exit criteria

- Every question answered or marked N/A with a reason.
- Open evidence items listed with an owner.
- Service findings drafted and confirmed by the participants.
