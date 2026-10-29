# Health Maturity Assessment Report — {{profile["Organization name"]}}

**Assessment date:** {{profile["Assessment date"]}} · **Assessed by (role):** {{profile["Assessed by (role)"]}} · **Kit version:** ACS Health Maturity Kit {{version}}

> This report is a self-assessment aid. It is not legal, licensing or compliance advice and does not certify compliance with HIPAA or any other requirement. It contains no protected health information.

<!--
How to use this template
- Placeholders in {{double braces}} name the field in results.json from tools/score_assessment.py.
  Example: {{services["Zero Trust"].dimensions["Identity"].score}}.
- Delete guidance comments before issuing.
- Every finding cites at least one question ID. Every number comes from results.json or from the organization.
- Examples marked "Illustrative" are fictional. Remove them.
-->

## 1. Summary

<!-- Conclusion first: two or three sentences on overall position and the single most important risk. -->

{{Two to three sentences.}}

| Service | Score (0–4) | Level | Answered |
|---|---|---|---|
| License Optimization | {{services["License Optimization"].score}} | {{services["License Optimization"].level}} | {{answered}}/{{questions}} |
| App Modernization | {{services["App Modernization"].score}} | {{services["App Modernization"].level}} | {{answered}}/{{questions}} |
| Zero Trust | {{services["Zero Trust"].score}} | {{services["Zero Trust"].level}} | {{answered}}/{{questions}} |
| **Overall** | {{overall.score}} | {{overall.level}} | {{overall.answered}}/{{overall.questions}} |

**HHS Cybersecurity Performance Goals:** Essential goals with status Meets {{count of cpg["Essential: …"].status == "Meets"}}/10 · Enhanced goals with status Meets {{count}}/10 · Essential goals at Gap: {{list}}

**Three most important actions:**

1. {{action}} — closes {{question IDs}} — {{HHS goal}}
2. {{action}} — closes {{question IDs}} — {{HHS goal}}
3. {{action}} — closes {{question IDs}} — {{HHS goal}}

## 2. Scope and method

| Item | Content |
|---|---|
| Purpose | {{decision the assessment supports, from intake}} |
| Organization profile | {{Organization type}}, {{State}}, {{Licensed beds}} licensed beds, {{Workforce size (approx.)}} workforce, {{IT staff (FTE)}} IT FTE, primary EHR {{Primary EHR}}, {{Microsoft agreement}}, {{Microsoft 365 plan}} |
| Services assessed | {{services}} |
| Scope exclusions | {{systems, sites or entities excluded, with reasons}} |
| Participants (roles) | {{roles per session}} |
| Evidence reviewed | {{count of artifacts seen, by type: document / system output / test result}} |
| N/A answers | {{count and IDs, with reasons}} |
| Unanswered | {{unanswered}} |

**How to read the scores.** Each question was scored 0–4 against question-specific level anchors; a 3 or 4 required evidence seen during the assessment. Dimension, service and overall scores are weighted averages (weights 3/2/1) excluding N/A and blanks; the level is the integer part of the score, so 2.9 is Developing. HHS goal status is the unweighted average of the mapped questions: 3 or more Meets, 2 to 2.99 Partially meets, below 2 Gap. See `docs/methodology.md`.

**Limitations.** {{unanswered questions; evidence not available; self-reported answers; no technical testing performed}}.

## 3. License Optimization

| Dimension | Score | Level |
|---|---|---|
| Governance & Ownership | {{services["License Optimization"].dimensions["Governance & Ownership"].score}} | {{level}} |
| Entitlements | | |
| Deployment & Usage | | |
| Security Value Realization | | |
| Cloud Cost | | |
| Programs & Negotiation | | |

**Findings.** Write each as: what is true today → why it matters → question IDs. Conclusion first.

| # | Finding | Question IDs | Evidence basis | Severity (C) |
|---|---|---|---|---|
| LO-F1 | *Illustrative:* Departing staff keep active licenses and accounts for weeks because offboarding depends on a manual ticket from HR. | LO-11, ZT-04 | HR separation list compared with directory, last quarter | 3 |

**Quick wins — licensed but not fully deployed** (from `license_map` where `status` = `Licensed but not fully deployed (quick win)`; verify against current Microsoft documentation and your agreement):

| Capability | Licensing (as recorded) | Licensed | Deployed | Related questions |
|---|---|---|---|---|
| {{license_map[].capability}} | {{licensing}} | {{licensed}} | {{deployed}} | {{from License-Security Map}} |

Items with status `Confirm licensing` or `Not answered` go to section 7.

## 4. App Modernization

| Dimension | Score | Level |
|---|---|---|
| Portfolio Visibility | | |
| Lifecycle & Supportability | | |
| Rationalization & Roadmap | | |
| Engineering & Release | | |
| Resilience & Recovery | | |
| Cloud & Data Readiness | | |

**Findings:**

| # | Finding | Question IDs | Evidence basis | Severity (C) |
|---|---|---|---|---|
| AM-F1 | | | | |

**Applications with highest priority** (from `top_applications`; priority = technical risk × criticality):

| Application | Hosting | Platform | Technical risk (0–8) | Criticality (1–5) | Business value (1–5) | Priority (0–40) | Final decision |
|---|---|---|---|---|---|---|---|
| *Illustrative:* Laboratory system | On-premises | Unsupported server OS | 6 | 5 | 4 | 30 | Pending owner decision |

**Unsupported platforms and proposed plans** (AM-05, AM-06): {{platform, applications affected, proposed plan — upgrade, isolate, retire or purchase extended security updates — and owner role}}. Windows 10 reached end of support on October 14, 2025; Extended Security Updates are available for a limited period — verify terms with Microsoft.

## 5. Zero Trust

| Pillar / dimension | Score | Level |
|---|---|---|
| Identity | | |
| Devices | | |
| Networks | | |
| Applications & Workloads | | |
| Data | | |
| Visibility & Analytics | | |
| Governance & Readiness | | |

**Status of HHS Cybersecurity Performance Goals** (from `cpg`; goal names exactly as in the tool output):

| Goal | Questions | Average | Status |
|---|---|---|---|
| Essential: Multifactor Authentication | {{cpg["Essential: Multifactor Authentication"].questions}} | {{average}} | {{status}} |
| … all 10 Essential, then all 10 Enhanced … | | | |

Note goals that rest on a single question: a single answer is a signal, not a robust measurement.

**Ransomware readiness.** One paragraph each: can attackers get in (ZT-01, ZT-10, ZT-12, ZT-06), can they spread and escalate (ZT-03, ZT-09), would we see them (ZT-20, ZT-21), can we keep caring for patients and recover (AM-19, ZT-24, ZT-19, AM-17, AM-18).

**Findings:**

| # | Finding | Question IDs | HHS goal | Evidence basis | Severity (C) |
|---|---|---|---|---|---|
| ZT-F1 | | | | | |

## 6. Prioritized recommendations

Prioritized by gap points, then risk to patient care and PHI, effort, dependency and already-licensed quick wins; every Essential goal at Gap has a Horizon 1 action. Full plan in the remediation roadmap.

| # | Action | Closes | HHS goal | Owner (role) | Indicator (baseline → target) | Horizon |
|---|---|---|---|---|---|---|
| 1 | | | | | | 1 |

## 7. Open questions and missing evidence

| Item | Question ID | Type (unanswered / evidence pending / confirm licensing) | Owner (role) | Due |
|---|---|---|---|---|
| | | | | |

## 8. Changes since the last assessment (re-assessments only)

| Service | Previous score | Current score | Change | Main driver |
|---|---|---|---|---|
| | | | | |

Compare only if the same evidence thresholds were applied.

## Appendix A — Top gaps

From `top_gaps` (up to 20; the Priority Gaps sheet has the full list):

| # | ID | Service | Dimension | Score | Weight | Gap points | Recommended action |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Appendix B — Results by question

{{Attach results.md from tools/score_assessment.py}}
