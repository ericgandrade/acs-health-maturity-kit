# Methodology

## What the kit measures

The ACS Health Maturity Kit measures how mature a healthcare organization's practices are in three areas that determine whether its technology is secure, reliable and affordable:

| Service | Questions | Dimensions |
|---|---|---|
| License Optimization | 24 | Governance & Ownership · Entitlements · Deployment & Usage · Security Value Realization · Cloud Cost · Programs & Negotiation |
| App Modernization | 24 | Portfolio Visibility · Lifecycle & Supportability · Rationalization & Roadmap · Engineering & Release · Resilience & Recovery · Cloud & Data Readiness |
| Zero Trust | 28 | Identity · Devices · Networks · Applications & Workloads · Data · Visibility & Analytics · Governance & Readiness |

## Scale

| Answer | Meaning |
|---|---|
| 0 – Not in place | The practice does not exist. |
| 1 – Initial | Ad hoc; depends on individuals; not documented. |
| 2 – Developing | Partly implemented or documented; not applied consistently. |
| 3 – Defined | Documented and applied consistently across the organization. |
| 4 – Optimized | Measured, reviewed regularly and improved; automated where practical. |
| N/A | The practice does not apply (explain why in Notes). |

Answers reflect what is in place today, supported by evidence. Plans count as 0–2 depending on how much is already implemented.

## Weights

- **3** — critical to patient safety, continuity of care or protection of PHI (for example MFA, backups, unsupported platforms).
- **2** — important to control and efficiency.
- **1** — foundational practices that enable the others.

## Scoring

- Question score: 0–4.
- Dimension, service and overall scores: weighted average of answered questions (N/A and blanks excluded).
- Level: the integer part of the score (for example 2.6 → Developing).
- Gap points: (4 − score) × weight. They rank the Priority Gaps.
- HHS goal status: average of the questions mapped to the goal; 3 or more = Meets, 2 to 2.99 = Partially meets, below 2 = Gap.

## Frameworks referenced

| Framework | Used for |
|---|---|
| HHS Healthcare and Public Health Cybersecurity Performance Goals (10 Essential, 10 Enhanced) | Baseline for the healthcare sector; CPG Crosswalk |
| HIPAA Security Rule (45 CFR Part 164, Subpart C) | Specific safeguards cited in question references |
| NIST Cybersecurity Framework 2.0 | Function and category references |
| CISA Zero Trust Maturity Model v2.0 | Zero Trust pillars |
| NIST SP 800-218 Secure Software Development Framework | Engineering practices |
| ISO/IEC 19770-1 and the FinOps Framework | License and cloud cost management |
| Microsoft Cloud Adoption Framework | Modernization planning and cloud readiness |

The mapping is the author's interpretation for self-assessment purposes. It does not represent endorsement by any of these organizations, and meeting a mapped question does not establish compliance with the referenced framework or regulation. See `docs/framework-mapping.md`.

## Limits

- Self-reported answers; quality depends on evidence reviewed.
- Licensing contents change; the License-Security Map must be verified against current Microsoft documentation and your agreement.
- The proposed HIPAA Security Rule update is referenced as proposed; check its current status.
