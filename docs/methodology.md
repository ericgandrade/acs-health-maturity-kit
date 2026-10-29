# Methodology

This document defines how the ACS Health Maturity Kit measures maturity, how answers are scored, how much evidence each score needs, and how the results should and should not be read. The scoring rules are fixed for v0.2.0 and are implemented in `tools/score_assessment.py` and in the workbook formulas. If this document and the tool ever disagree, the tool is the reference and this document has a bug.

## What the kit measures

The kit measures how mature a healthcare organization's practices are in three areas that determine whether its technology is secure, reliable and affordable:

| Service | Questions | Dimensions (in order) |
|---|---|---|
| License Optimization | 24 | Governance & Ownership · Entitlements · Deployment & Usage · Security Value Realization · Cloud Cost · Programs & Negotiation |
| App Modernization | 24 | Portfolio Visibility · Lifecycle & Supportability · Rationalization & Roadmap · Engineering & Release · Resilience & Recovery · Cloud & Data Readiness |
| Zero Trust | 28 | Identity · Devices · Networks · Applications & Workloads · Data · Visibility & Analytics · Governance & Readiness |

It measures **practice**, not technology ownership. Owning a product that can enforce multifactor authentication is not maturity; enforcing it on every remote entry point, and being able to show that, is.

## The scale

Every question is answered on the same five-level scale.

| Answer | General meaning | What you typically see |
|---|---|---|
| 0 – Not in place | The practice does not exist. | Nothing to show; "we don't do that". |
| 1 – Initial | Ad hoc; depends on individuals; not documented. | One person does it when there is time; results live in someone's head or inbox. |
| 2 – Developing | Partly implemented or documented; not applied consistently. | A draft policy, a pilot, coverage of some sites or systems, known exceptions without approval. |
| 3 – Defined | Documented and applied consistently across the organization. | A current document plus system output that shows organization-wide coverage; exceptions are approved and listed. |
| 4 – Optimized | Measured, reviewed regularly and improved; automated where practical. | Level 3 plus metrics over time, review records and automation or alerting on drift. |
| N/A | The practice does not apply. | A reason recorded in Notes (see the N/A rules below). |

### Per-question level anchors

The general scale is too abstract to score consistently on its own: "consistently applied" means something different for MFA than for a renewal calendar. In v0.2.0 every question therefore carries its own **level anchors** (`level_0` to `level_4` in `data/questionnaire.csv`). Each anchor describes what an assessor would actually observe at that level for that specific practice. You will find them in three places:

- column D, **Maturity levels (0–4)**, of each service sheet in the workbook;
- the **Question Guide** sheet of the workbook, which adds probing questions, evidence, red flags, healthcare considerations and next-step actions;
- `docs/question-guide.md`, the same content generated from the CSV for reading outside Excel.

`level_4` replaces the `target_state` field of v0.1.0. The anchors are written to be progressively stricter and mutually exclusive. Use them this way:

1. Read the anchors from 0 upward and stop at the **highest level whose description is fully true today**. If any element of an anchor is not true, the answer is the level below.
2. When coverage is uneven, score the **weakest material part** of the scope. If MFA is enforced everywhere except vendor access, the vendor gap decides the level, because that is where an attacker would go.
3. A partly met higher anchor does not round up. "Mostly 3" is 2. The gap between the two anchors goes into Notes and becomes an action.
4. If the anchors do not fit the organization's situation (for example, an unusual hosting model), score against the general scale above and record why in Notes.

## Evidence thresholds

A score is only as good as the evidence behind it. The kit uses four evidence types:

| Type | Examples | Strength |
|---|---|---|
| **Statement** | A participant says the practice is in place. | Weakest; acceptable only for 0–2. |
| **Document** | Policy, procedure, RACI, contract clause, plan, minutes. | Shows intent and design, not operation. |
| **System output** | Admin console report, policy export, coverage dashboard, log query, ticket history, backup job report. | Shows the practice operating. |
| **Test or exercise result** | Restore test report, tabletop after-action report, penetration test, phishing exercise results, DR test. | Shows the practice works under realistic conditions. |

Minimum evidence by score:

| Score | Minimum evidence | Freshness |
|---|---|---|
| 0–1 | Statement. | Current. |
| 2 | Statement that explains what exists and where it stops; a document or partial output is desirable. | Current. |
| 3 | A document **and** system output (or a test result where the practice is a test, such as restoration or incident response) showing organization-wide coverage, with exceptions listed. | Produced within the practice's own cycle (for example, the last quarterly review for a quarterly practice) and never older than 12 months. |
| 4 | Everything required for 3, **plus** evidence of measurement and review over time (at least two review cycles, or a trend), and automation or alerting where practical. | As for 3. |

Rules that apply to every service:

- **Seen, not copied.** Evidence can be shown on screen. The assessor records *what was seen* (artifact name, date, source system) in Notes, never the content if it contains PHI, credentials or network details.
- **Configured is not enforced.** A policy in report-only, audit or pilot mode counts as 2 at most.
- **Plans are not practice.** A funded project that has not started is 0–2, depending on what is already implemented. Record the plan in Notes; it becomes context for the roadmap, not maturity.
- **Outsourced still counts.** If a managed service provider, the EHR vendor or a SaaS provider performs the practice, the organization scores its *oversight*: does it receive the report, review it and act on it? A vendor's marketing statement is not evidence.
- **No evidence, no 3.** If a participant claims 3 or 4 and evidence is not available during the session, record 2 (or lower if the anchors say so), add the evidence to the open items with an owner, and update the score when the evidence is produced.

## N/A rules

Use N/A only when the practice genuinely cannot apply to the organization. Typical legitimate cases:

- No public cloud subscriptions at all: the Cloud Cost questions (LO-17 to LO-20) and the cloud foundation question (AM-21).
- No software development or configuration scripting of any kind: some Engineering & Release questions. Most hospitals still configure and release changes to vendor systems and interfaces, so N/A here is rare.
- No AI-assisted engineering in use at all: AM-16. If staff use AI tools without approval, the question applies and is scored against its anchors; it is not N/A.

N/A is **not** valid when the practice applies but is done by someone else (score the oversight), when nobody knows the answer (leave blank and add an open item), or when the practice is not done because it seems unimportant (that is a 0).

N/A answers and blanks are both excluded from the averages. They are treated differently in the output: blanks appear in `unanswered` in `results.json`; N/A does not. Report the number of N/A answers in the scope section of the report, because many N/A answers change what a score represents.

## Weights

Each question has a weight that reflects its consequence for patients, operations and PHI:

| Weight | Meaning | Examples |
|---|---|---|
| **3** | Critical to patient safety, continuity of care or protection of PHI. | MFA (ZT-01), isolated backups (ZT-19), unsupported platforms (AM-05), downtime procedures (AM-19), incident response (ZT-24). |
| **2** | Important to control and efficiency. | Device compliance before PHI access (ZT-07), PHI classification (ZT-17), annual entitlement reconciliation (LO-06). |
| **1** | Foundational practices that enable the others. | Licensing cost reporting (LO-04), total cost of ownership (AM-12), a Zero Trust strategy (ZT-28). |

Weights are part of the frozen contract and are the same for every organization.

## Scoring

| Result | Rule | Example |
|---|---|---|
| Question score | The answer, 0–4. | "2 – Developing" → 2. |
| Dimension, service and overall score | Weighted average of answered questions: Σ(score × weight) ÷ Σ(weight), excluding N/A and blanks. | Scores 1 (w3), 3 (w2), 4 (w1) → (3 + 6 + 4) ÷ 6 = 2.17. |
| Level | Integer part of the score, not rounding. | 2.17 → Developing; 2.99 → Developing; 3.00 → Defined. |
| Gap points | (4 − score) × weight, for each answered question below 4. | Score 1, weight 3 → 9 gap points. Score 0, weight 1 → 4. |
| HHS goal status | **Unweighted** average of the answered questions mapped to the goal: 3 or more = Meets; 2 to 2.99 = Partially meets; below 2 = Gap; no answered question = Not assessed. | Multifactor Authentication: ZT-01 at 2, LO-14 at 3, LO-13 at 4 → 3.0 → Meets. |

Why these choices:

- **Truncation, not rounding,** keeps the level conservative: a 2.9 service still has questions at 2 or below, and calling it Defined would hide them.
- **Gap points** combine how far a practice is from 4 with how much it matters, so a weight-3 question at 1 (9 points) outranks a weight-1 question at 0 (4 points).
- **HHS goal averages are unweighted** because the goals are binary sector baselines; each mapped question is one view of the same goal. This is the one place where weights do not apply. A question can map to more than one goal.

Gap points rank the *size* of a gap. They do not decide the order of work on their own. The Roadmap Strategist adds a judgment layer on top of them, always in this order: (1) gap points from the tool, (2) risk to patient care and PHI, (3) effort, (4) dependency, (5) cost-neutral "already licensed" quick wins. Two gates override the ranking: HHS Essential goals with status Gap, and hard deadlines such as end of support. See `agents/roadmap-strategist.md`.

## Reading the results correctly

- **Read dimensions, not just the service score.** A Zero Trust score of 2.4 can hide an Identity dimension at 3.5 and a Data dimension at 0.8. The roadmap is built from dimensions and questions.
- **Scores are comparable over time only if the evidence standard is the same.** Re-assess with the same thresholds; a score that rises because evidence was accepted more loosely is not progress.
- **Scores are not comparable across organizations** in any rigorous sense. The kit is a self-assessment; it has no benchmark data.
- **A Meets on an HHS goal is not compliance.** It means the mapped questions averaged 3 or more on this kit's anchors.
- **Small samples are signals.** A goal mapped to one question rests on one answer; say so when you report it.

## Frameworks referenced

| Framework | Used for |
|---|---|
| HHS Healthcare and Public Health Cybersecurity Performance Goals (10 Essential, 10 Enhanced) | Baseline for the healthcare sector; CPG Crosswalk |
| HIPAA Security Rule (45 CFR Part 164, Subpart C) | Specific safeguards cited in question references |
| NIST Cybersecurity Framework 2.0 | Function and category references |
| CISA Zero Trust Maturity Model v2.0 | Zero Trust pillars |
| NIST SP 800-218 Secure Software Development Framework | Engineering practices |
| ISO/IEC 19770-1 and the FinOps Framework | License and cloud cost management |
| Microsoft Cloud Adoption Framework | Cloud readiness and landing-zone planning (the application disposition list used in the kit is the kit's own) |

The HHS goals are voluntary. A proposed update to the HIPAA Security Rule was published as a notice of proposed rulemaking on January 6, 2025; the kit refers to it only as proposed. Check its current status before relying on it.

The mapping is the kit's interpretation for self-assessment purposes. It does not represent endorsement by any of these organizations, and meeting a mapped question does not establish compliance with the referenced framework or regulation. See `docs/framework-mapping.md`.

## Limits

- Answers are self-reported; their quality depends on the evidence reviewed and on the assessor's discipline in applying the thresholds above.
- Licensing contents change. The License-Security Map must be verified against current Microsoft documentation and your agreement.
- The kit does not test controls technically (no scanning, no penetration testing) and does not replace the HIPAA risk analysis required by 45 CFR 164.308(a)(1)(ii)(A).
- The kit contains no benchmark statistics. Any number in a report comes from the organization's own data or from a cited source.

## Sources

- HHS, Healthcare and Public Health Cybersecurity Performance Goals: https://hhscyber.hhs.gov/cybersecurity-performance-goals.html
- Federal Register, HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information (proposed rule, January 6, 2025): https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information
- eCFR, 45 CFR Part 164 Subpart C: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C
- CISA, Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
- NIST, Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final
