# Report Quality Checklist

Run with `*qa` before any document leaves the assessment team (quality gate G4). Every item must pass; fix failures rather than waiving them. Record the fix next to the item.

## Accuracy

- [ ] Every score, level and count matches `results.json` from the latest run of `tools/score_assessment.py`.
- [ ] Levels are the integer part of the score (2.9 is Developing), never rounded up.
- [ ] HHS goal names and statuses match the `cpg` field exactly (tool short names, for example "Revoke Credentials for Departing Workforce Members", "Detect and Respond to Relevant Threats and TTPs").
- [ ] HHS goal status is described as the unweighted average of mapped questions; goals resting on one question are flagged.
- [ ] `top_gaps` is not described as the full gap list (it is capped at 20); the Priority Gaps sheet is cited for the full list.
- [ ] Unanswered questions are listed as open items, not treated as zero; N/A answers are listed with reasons.
- [ ] Every finding cites at least one question ID and states its evidence basis.
- [ ] No score of 3 or 4 lacks evidence recorded in Notes.
- [ ] Licensing statements cite the License-Security Map and say "verify against current Microsoft documentation and your agreement".
- [ ] No invented numbers: costs, savings, percentages, benchmarks and dates come from the organization (labeled as such) or from a cited official source.
- [ ] The proposed HIPAA Security Rule update is described as proposed.
- [ ] Windows 10 end of support is stated as October 14, 2025, with Extended Security Updates described as available for a limited period, without prices.
- [ ] Every cited URL opens.

## Privacy and safety

- [ ] No PHI anywhere in the documents, including appendices and Notes copied from the workbook.
- [ ] No passwords, keys, IP addresses, firewall rules or vulnerability details that would help an attacker.
- [ ] No individual is named, quoted or evaluated; roles only.
- [ ] The executive summary is suitable for board distribution (no system-level weaknesses).

## Prioritization and roadmap

- [ ] Prioritization follows the stated order: gap points, risk to patient care and PHI, effort, dependency, already-licensed quick wins; the factors are shown.
- [ ] Every HHS Essential goal with status Gap has at least one Horizon 1 action.
- [ ] No action is scheduled before its prerequisites (for example segmentation before inventory, DLP before classification, migration before a cloud foundation).
- [ ] Every roadmap action has an owner role, a horizon, the question IDs it closes and an indicator with baseline, target and evidence.
- [ ] The number of concurrent Horizon 1 actions is realistic for the IT staff recorded in the Profile.
- [ ] Actions that use capabilities the organization already owns are identified as quick wins.
- [ ] Funding pathways are phrased as options to explore, with no amounts or guaranteed eligibility.

## Usefulness and clarity

- [ ] The executive summary fits on one page, leads with the conclusion and states three risks as consequences for patients and operations.
- [ ] Decisions requested from leadership are explicit, with the consequence of not deciding.
- [ ] Open questions and missing evidence are listed with an owner role.
- [ ] Plain language; acronyms explained once; no filler.
- [ ] Illustrative examples from the templates are removed.

## Positioning

- [ ] The report states that it is a self-assessment aid, not legal, licensing or compliance advice, and does not certify HIPAA compliance.
- [ ] Suggested dispositions and priorities are presented as recommendations for the accountable owners to decide.
- [ ] No claim that any practice or the kit ensures compliance with any regulation.
