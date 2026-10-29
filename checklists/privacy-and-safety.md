# Privacy and Safety Rules (all agents)

Every agent in this kit loads these rules first and follows them throughout the session. Human facilitators follow the same rules.

## Core rules

1. **No protected health information (PHI).** Never request, accept, store or repeat patient names, medical record numbers, dates of birth, diagnoses, images or any other PHI. If the user shares PHI, stop, ask them to remove it, and do not use it.
2. **No secrets.** Never request or record passwords, keys, tokens, connection strings, recovery codes, IP addresses or network diagrams with addresses.
3. **No attack detail.** Record whether a control exists and how widely it applies — never specific vulnerabilities, unpatched system names tied to exposures, firewall rules or anything that would help an attacker.
4. **Evidence over intent.** A practice counts only if it is in place today. Plans and intentions are recorded as notes, not as maturity.
5. **No invented facts.** Never invent scores, metrics, costs, savings, product capabilities, license entitlements, regulations, deadlines, statistics or quotes. If something is unknown, record it as unknown and add it to the open questions.
6. **Cite the framework.** Every finding references the question ID and, where mapped, the HHS Cybersecurity Performance Goal, HIPAA Security Rule section or other reference from `data/questionnaire.csv`.
7. **Advisory only.** Outputs are a self-assessment aid. They are not legal, licensing or compliance advice and do not certify HIPAA compliance. Say so in every report.
8. **Licensing claims are verified.** Statements about what a license includes come from `data/license_security_map.csv` and are labeled "verify against current Microsoft documentation and your agreement".
9. **Human decision.** Agents recommend; the organization's accountable owners decide. Never present a suggested disposition or priority as a final decision.
10. **Practices, not people.** Record roles, not names. Do not attribute statements, evaluate or rank individuals.

## Handling evidence safely

| Situation | What to do |
|---|---|
| Evidence on screen shows patient data (for example an access log with patient names) | Ask the participant to filter or hide the columns; record only "access review report seen, dated …". |
| A screenshot or export with PHI or credentials is pasted into the chat | Stop; ask the user to delete it from the conversation where possible; do not quote or summarize it. |
| A participant reads out a password or key | Ask them to rotate it after the session; do not record it. |
| A diagram shows addresses | Describe zones only ("medical devices are on a separate segment from corporate devices"). |
| A finding would reveal an exploitable weakness | Write it at control level ("vendor access is not time-limited"), not exposure level. |

## Tool and data handling

- Use only AI tools the organization has approved for its data. Do not upload the workbook, notes or evidence elsewhere.
- Keep the workbook in the organization's approved storage. Treat the completed workbook and reports as internal and confidential: they describe security weaknesses.
- Share reports on a need-to-know basis; executive summaries for boards should not list specific system weaknesses.

## Regulatory statements

- The HHS Cybersecurity Performance Goals are voluntary.
- The HIPAA Security Rule update published as a notice of proposed rulemaking on January 6, 2025 is described only as **proposed**, unless the user provides a newer official source showing otherwise.
- The assessment does not replace the HIPAA security risk analysis (45 CFR 164.308(a)(1)(ii)(A)).

## Medical device and clinical safety

- Never recommend patching, scanning, installing agents on or reconfiguring a medical device outside the manufacturer's guidance. Point to manufacturer disclosures, MDS2 forms and SBOMs, and to compensating controls (inventory, segmentation, controlled vendor access).
- Any recommended change to clinical systems must respect change control, downtime procedures and clinical sign-off.
- Active security testing is out of scope for this kit; if the organization wants it, it should be authorized, scheduled and coordinated with clinical operations.
