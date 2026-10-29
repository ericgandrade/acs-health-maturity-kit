# Workflow 01 — Intake

**Owner:** ACS Maturity Lead · **Time:** 30–45 minutes, plus 15 minutes to confirm the plan · **Output:** completed Profile sheet, assessment plan, evidence requests · **Gate:** G1 Plan approved

## Purpose

Set the engagement up so that the service sessions produce comparable, evidence-backed scores. Most assessment quality problems — missing voices, unclear scope, evidence that never arrives — start at intake.

## Roles

| Role | Responsibility in this workflow |
|---|---|
| ACS Maturity Lead (agent or facilitator) | Runs the session, fills the Profile, drafts the plan. |
| IT leader | Primary participant; confirms scope, participants and evidence. |
| Executive sponsor (CEO, administrator or CFO) | Confirms the decision the assessment supports; approves the plan (can be by message). |
| Privacy or compliance officer | Confirms the rules on PHI and evidence handling. |

## Inputs

- `toolkit/ACS-Health-Maturity-Assessment.xlsx` (blank, or a previous assessment for a re-assessment).
- Previous `results.json`, if any.
- Known constraints: go-lives, survey visits, change freezes, budget cycle dates.

## Agenda

| # | Segment | Time | What happens |
|---|---|---|---|
| 1 | Rules of engagement | 5 min | No PHI, no passwords or keys, no network addresses. Evidence is shown on screen, not sent. Answers describe what is in place today. Results are a self-assessment aid, not compliance advice. |
| 2 | Purpose | 5 min | Ask: "What decision should this assessment help you make in the next six months?" Record it with the sponsor role. |
| 3 | Profile | 10 min | Fill the Profile sheet (below). |
| 4 | Scope | 5–10 min | Services (all three by default); sites and entities; systems out of scope and why; vendor-hosted and outsourced services. |
| 5 | Stakeholders | 5–10 min | Map roles to sessions using the stakeholder map in `agents/acs-maturity-lead.md`. Note roles held by the same person. |
| 6 | Evidence plan and calendar | 5 min | Send evidence requests from `checklists/evidence-checklist.md`; book sessions. |

## Profile sheet fields

| Field | Guidance |
|---|---|
| Organization name | As it should appear on the report. |
| State | Two-letter or full name. |
| Organization type | Choose from the list (critical access hospital, rural emergency hospital, community hospital, health system, academic medical center, clinic or physician group, other). |
| Licensed beds | Leave blank for clinics. |
| Workforce size (approx.) | Including employed clinicians; approximate is fine. |
| IT staff (FTE) | Internal staff only; note managed service providers in Notes elsewhere. |
| Primary EHR | Product category or vendor name and whether it is vendor-hosted. |
| Microsoft agreement | Enterprise Agreement, CSP, MCA, or other/unknown. |
| Microsoft 365 plan | E3, E5, Business Premium, mixed, or other/unknown. "Unknown" is a valid answer and an early License Optimization finding. |
| Assessment date | The date answers are recorded; evidence freshness is measured from it. |
| Assessed by (role) | Role, not name. |

## Scope decisions to make explicitly

- **Multi-entity organizations:** assess as one organization (and score the weakest entity, per the methodology) or run one workbook per entity. Do not mix.
- **Vendor-hosted EHR and SaaS:** in scope; the organization's oversight is scored.
- **Medical devices:** in scope for inventory, segmentation and vendor access; patching is assessed against manufacturer guidance.
- **Affiliated physician practices on shared infrastructure:** in scope if they share identity, network or email.

## Session plan

| Session | Time box | Required roles | Specialist |
|---|---|---|---|
| License Optimization | 60–90 min | IT leader, finance or procurement; licensing partner if any | License Optimization Analyst |
| App Modernization | 60–90 min | Applications lead, infrastructure lead, clinical informatics; biomedical engineering for AM-08 | App Modernization Architect |
| Zero Trust | 90–120 min | Security lead or IT leader, infrastructure lead, privacy/compliance officer; managed security provider if any | Zero Trust Assessor |
| Evidence follow-up | 30 min per service, within 5 working days | Evidence owners | Same specialist |
| Consolidation | 60 min | IT leader, CFO, sponsor | Roadmap Strategist |

Each service session must include at least one non-IT role. Send the Question Guide sheet (or `docs/question-guide.md`) for the service to participants at least two working days in advance so they can locate evidence.

## Outputs

1. Completed Profile sheet.
2. Assessment plan (format in `agents/acs-maturity-lead.md`, section 9): purpose, scope, sessions, evidence requests with owner roles and due dates, quality gates.
3. Evidence requests sent.

## Quality gate G1 — Plan approved

- [ ] Profile sheet complete (unknowns marked as unknown, not left blank).
- [ ] Purpose and sponsor role recorded.
- [ ] Scope and exclusions written, with reasons.
- [ ] Every service has named participant roles, including at least one non-IT role.
- [ ] Evidence requests sent with owner roles and due dates.
- [ ] The sponsor or IT leader has confirmed the plan.

Next: `workflows/02-service-assessment.md` for the first service.
