# Remediation Roadmap — {{profile["Organization name"]}}

**Based on assessment of:** {{profile["Assessment date"]}} · **Overall:** {{overall.score}} / 4 ({{overall.level}}) · **Review cadence:** monthly status, quarterly leadership report, full re-assessment in 6–12 months

<!--
Guidance (delete before issuing)
- Built by the Roadmap Strategist (agents/roadmap-strategist.md).
- Prioritization, always in this order: (1) gap points from the tool, (2) risk to patient care and PHI (C: 3/2/1),
  (3) effort (E: 1/2/3), (4) dependency, (5) cost-neutral "already licensed" quick wins.
  Priority index = gap points × C ÷ E. Gates: every HHS Essential goal at Gap has a Horizon 1 action;
  every hard deadline is met.
- Sequencing: identity and backups first; inventory before segmentation; classification before DLP;
  cloud foundation before migration.
- Owner = role. Dates only if the organization provides them. Costs only if the organization provides them.
- Examples marked "Illustrative" are fictional; remove them.
-->

## How to read this roadmap

Each action closes one or more assessment questions, names the role that owns it, and has an indicator with a baseline, a target and the evidence that will prove it. "Expected re-score" is the level the closed questions should reach at the next assessment if the action is completed as described.

## Capacity check

| Item | Value |
|---|---|
| IT staff (FTE) | {{profile["IT staff (FTE)"]}} |
| External support | {{managed service provider, managed detection provider, vendors}} |
| Maximum concurrent Horizon 1 actions agreed | {{n}} |

## Horizon 1 — 0 to 90 days (protect identity and the ability to recover; use what we own)

| # | Action | Closes (question IDs) | HHS goal | Owner (role) | Effort (E) | Depends on | Indicator: baseline → target (evidence) | Expected re-score | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | *Illustrative:* Enforce MFA on all remote access, email, vendor and administrator accounts; remove undocumented exclusions | LO-14, ZT-01 | Essential: Multifactor Authentication | IT director | 1 | — | Remote entry points with MFA enforced: 3 of 5 → 5 of 5 (policy state export) | 2 → 3 | Not started |
| 1.2 | *Illustrative:* Isolate one backup copy of critical systems and test a full restore of one clinical system | AM-17, AM-18, ZT-19 | — | Systems administrator | 2 | — | Critical systems with isolated copy and restore test in last quarter: 0 → all tier-1 systems (restore test report) | 1 → 3 | Not started |
| 1.3 | | | | | | | | | Not started |

## Horizon 2 — 3 to 6 months (see the estate and control access)

| # | Action | Closes | HHS goal | Owner (role) | Effort (E) | Depends on | Indicator: baseline → target (evidence) | Expected re-score | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2.1 | | | | | | | | | Not started |

## Horizon 3 — 6 to 18 months (modernize and optimize)

| # | Action | Closes | HHS goal | Owner (role) | Effort (E) | Depends on | Indicator: baseline → target (evidence) | Expected re-score | Status |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | | | | | | | | | Not started |

Status values: Not started · In progress · Blocked (state why) · Complete (evidence seen) · Deferred (decision recorded).

## Prioritization record

Kept so that owners can see why each action is where it is.

| Action | Gap points (sum) | C | E | Index | Quick win | Gate | Horizon |
|---|---|---|---|---|---|---|---|
| *Illustrative:* 1.1 | 12 | 3 | 1 | 36 | Yes (licensed) | Essential: Multifactor Authentication at Gap | 1 |

## Dependencies

| Action | Requires first | Why |
|---|---|---|
| *Illustrative:* Segment medical devices (ZT-09, AM-08) | Device inventory (ZT-05, AM-01) | Cannot segment what is not known. |
| | | |

## Deadlines

| Deadline | Source (organization-provided or official) | Actions | On track? |
|---|---|---|---|
| {{e.g., contract renewal, end of support}} | | | |

## Funding pathways to explore

Do not state amounts or assume eligibility.

| Action | Pathway (already licensed · operating budget · capital budget · renewal negotiation · state or federal program to ask about) | Next step | Owner (role) |
|---|---|---|---|
| | | | |

## Risks to the plan

| Risk | Effect on the plan | Mitigation or compensating control | Owner (role) |
|---|---|---|---|
| *Illustrative:* Vendor support for a clinical system ends before its replacement is live | Unsupported system remains on the network | Isolate (AM-08) and restrict vendor access (ZT-10) until replaced | Applications lead |

## Governance

- Monthly: owners update Status and indicators; the IT leader reviews blocked items.
- Quarterly: report Essential goals met, Horizon 1 completion and indicators to the sponsor and board.
- Changes to horizons or deferrals are recorded with the decision and the role that made it.
- Re-assess in 6–12 months with the same evidence thresholds.

*Self-assessment aid; not legal, licensing or compliance advice. No PHI is included.*
