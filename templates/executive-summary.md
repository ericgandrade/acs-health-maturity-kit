# Executive Summary — {{profile["Organization name"]}} Health Maturity Assessment

**Date:** {{profile["Assessment date"]}} · **Prepared for:** {{sponsor role}} · **Purpose:** {{decision the assessment supports}}

<!--
Guidance (delete before issuing)
- One page. Conclusion first. Plain language for a CEO, CFO and board; no acronyms without a short explanation.
- Every number comes from results.json or from the organization. No benchmark, breach-cost or ROI figures.
- Risks are described as consequences for patients and operations, not as control names.
- Use roles, not names. Examples marked "Illustrative" are fictional; remove them.
-->

## Where we stand

{{One or two sentences: overall position and the most important risk.}}

Overall maturity is **{{overall.score}} / 4 ({{overall.level}})**: License Optimization {{services["License Optimization"].score}}, App Modernization {{services["App Modernization"].score}}, Zero Trust {{services["Zero Trust"].score}}. We meet **{{n}} of the 10** HHS Essential Cybersecurity Performance Goals (voluntary sector baseline) and {{n}} of the 10 Enhanced goals. Scores are on a 0–4 scale where 3 means documented and applied across the organization, with evidence.

## What matters most

1. **{{Risk in one sentence}}** — {{consequence for patients and operations}}. ({{question IDs}})
2. **{{Risk}}** — {{consequence}}. ({{question IDs}})
3. **{{Risk}}** — {{consequence}}. ({{question IDs}})

*Illustrative:* **Our backups could be encrypted along with our servers.** If ransomware reached the data center, we could not count on restoring the laboratory system and EHR interfaces, and clinical units would run on downtime procedures for an unknown period. (ZT-19, AM-17, AM-18)

## What we will do in the next 90 days

| Action | Owner (role) | Measure of success | Uses what we already own? |
|---|---|---|---|
| {{action}} | {{role}} | {{baseline → target}} | {{Yes / No}} |
| {{action}} | {{role}} | {{baseline → target}} | |
| {{action}} | {{role}} | {{baseline → target}} | |

*Illustrative:* Enforce multifactor sign-in on all remote access, email, vendor and administrator accounts · IT director · remote entry points with enforced MFA: baseline from inventory → all · Yes.

## What we already own and should use

{{Capabilities from the License-Security Map with status "Licensed but not fully deployed (quick win)", in plain language. Verify against current Microsoft documentation and your agreement.}}

## What it will take

{{Staff time, partner support and any budget items the organization has quantified. If costs are not yet known, say which actions need a quote and by when.}}

## Decisions requested from leadership

| Decision | Why now | If we do not decide |
|---|---|---|
| {{e.g., approve a plan and budget line for unsupported platforms}} | {{deadline or risk}} | {{consequence}} |
| {{decision}} | | |

## How we will report progress

Quarterly: Essential goals met (now {{n}}/10), Horizon 1 actions complete, and the indicators above. Full re-assessment in 6–12 months.

*Self-assessment aid; not legal, licensing or compliance advice; does not certify HIPAA compliance. No PHI is included.*
