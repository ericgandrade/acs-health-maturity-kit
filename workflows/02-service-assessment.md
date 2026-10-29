# Workflow 02 — Service Assessment

**Owner:** the specialist agent for the service, with the ACS Maturity Lead observing · **Time:** 60–90 minutes (License Optimization, App Modernization), 90–120 minutes (Zero Trust), plus a 30-minute evidence follow-up · **Output:** answered service sheet, findings, open evidence items · **Gate:** G2 Service complete

## Roles

| Role | Responsibility |
|---|---|
| Specialist agent (or facilitator) | Asks the questions, proposes scores against the anchors, records Notes. |
| ACS Maturity Lead | Keeps time, applies evidence governance, watches for drift from the methodology. |
| Participants (see the intake plan) | Describe what is in place and show evidence on screen. |
| Recorder (can be the specialist) | Enters the answer in the yellow Answer column and evidence references in Notes. |

## Inputs

- The service sheet in the workbook: column D **Maturity levels (0–4)**, the Evidence column and the yellow Answer column.
- The **Question Guide** sheet (or `docs/question-guide.md`): probing questions, evidence, red flags, healthcare considerations and actions per question.
- The service playbook: `docs/playbooks/license-optimization.md`, `docs/playbooks/app-modernization.md` or `docs/playbooks/zero-trust.md`.
- Evidence already gathered under the intake requests.

## Agenda

| Segment | Time | Content |
|---|---|---|
| Opening | 5 min | Rules (no PHI, no secrets, show don't send); purpose; how scoring works in one sentence: "We pick the highest level whose description is fully true today, and a 3 or 4 needs evidence we can see." |
| Dimensions | 8–15 min each | One dimension at a time, in the order of the sheet. Zero Trust: run the Essential-goal questions first if time is tight (see the Zero Trust Assessor). |
| Service-specific sheet | 10–15 min | License-Security Map, App Portfolio Triage or CPG Crosswalk review. |
| Close | 5–10 min | Read back dimension summaries; confirm open evidence items, owners and due dates. |

## Steps for each question

1. **Ask the opening question** in the participant's language, not the questionnaire's. "How does someone from a vendor get into your network to support a system?" works better than reading ZT-10 aloud.
2. **Probe** with the probing questions from the Question Guide. Choose the two or three that fit; the goal is to find where the practice stops, not to read every probe.
3. **Locate the answer on the anchors.** Read the level descriptions in column D from 0 upward and stop at the highest level that is *fully* true. Partial coverage takes the level below. Score the weakest material part of the scope.
4. **Check evidence against the threshold** in `docs/methodology.md`: 3 needs a document and system output (or a test result) showing organization-wide coverage, no older than the practice's cycle and never older than 12 months; 4 also needs measurement over time and automation or alerting where practical.
5. **Check the red flags** for the question. If one applies, ask about it directly.
6. **Apply the healthcare considerations.** For example, shared clinical workstations, medical devices that cannot take agents, vendor-hosted systems. Score the organization's controls, not the manufacturer's or vendor's choices — but do check that compensating controls exist.
7. **Propose the score and say why** in one sentence referencing the anchor: "That's a 2: MFA is on the VPN and email, but vendor accounts are excluded without an approval record."
8. **Record** the answer in the yellow Answer column and, in Notes: evidence seen (artifact, source system, date), the gap to the next level, and any plan in progress. No PHI, credentials or addresses.

## Handling difficult moments

| Situation | Response |
|---|---|
| "We're working on it." | Ask what is live today. Score that. Record the project, its owner and start date in Notes as context for the roadmap. |
| A 3 or 4 claimed without evidence | "Let's look at it together — which report or console shows that?" If not available now, record per the anchors at 2 or lower and create `EV-<ID>` with owner and due date. Revisit in the follow-up. |
| Participants disagree | Go to the evidence; if none, record the lower score and both views in Notes without names (see `agents/acs-maturity-lead.md`). |
| "The vendor does that." | Ask for the vendor's report and how the organization reviews it. Score oversight. |
| "We don't know." | Leave blank, add an open item with an owner. Do not guess and do not use N/A. |
| A question does not apply | Use N/A only per the rules in `docs/methodology.md`, with the reason in Notes. |
| The conversation turns to solutions | Note the idea in Notes for the roadmap and return to today's state. |
| Time is running out | Stop at the end of a dimension; schedule the remainder. |

## Calibration aid

The level anchors in column D take precedence. When an anchor does not fit, the general scale applies:

| If you hear… | Typical answer |
|---|---|
| "We don't do that." | 0 |
| "One person does it when they have time." | 1 |
| "It's done for some systems or sites, or there's a draft policy." | 2 |
| "It's documented and done everywhere; I can show you." | 3 |
| "It's measured, reviewed and automated; here is the trend report." | 4 |

## Close each dimension

Summarize in one sentence the dimension's state and its main gap, and confirm it with participants: "Identity: MFA and offboarding are solid; the main gap is shared logins on nursing-unit workstations (ZT-02)."

## Service-specific tools

- **License Optimization** → complete the License-Security Map sheet: Licensed? and Deployed? for each capability. Verify every line against current Microsoft documentation and your agreement.
- **App Modernization** → complete the App Portfolio Triage sheet for at least the applications rated criticality 4–5. The suggested disposition is a starting point; owners record the final decision.
- **Zero Trust** → review the CPG Crosswalk sheet with the participants; confirm every Essential goal has its mapped questions answered.

## Score and findings

1. Run `python tools/score_assessment.py <workbook.xlsx> [output_basename]`.
2. Draft the service section of `templates/assessment-report.md`: dimension table, findings with question IDs, evidence gaps.
3. Return findings to the Maturity Lead using the handoff protocol in the specialist agent file.

## Outputs

- Answered service sheet with Notes citing evidence.
- Service findings with question IDs.
- Open evidence items with owner roles and due dates.
- N/A list with reasons.

## Quality gate G2 — Service complete

- [ ] Every question answered, marked N/A with a reason, or listed as unanswered with a follow-up date.
- [ ] Every 3 and 4 cites the evidence seen (artifact, source, date) in Notes.
- [ ] No Notes contain PHI, credentials, network addresses or vulnerability details.
- [ ] Dimension summaries confirmed by participants.
- [ ] The service-specific sheet is completed.
- [ ] Findings returned to the Maturity Lead.
