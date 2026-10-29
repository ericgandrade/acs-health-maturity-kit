# Modernization Runbook — {{Application}}

**Change:** {{e.g., upgrade database platform / migrate to cloud / retire application}} · **Disposition:** {{Retire / Rehost / Replatform / Refactor / Replace / Isolate}} · **Owner (role):** {{role}} · **Related questions:** AM-05, AM-06, AM-13, AM-14, AM-17, AM-18

> No PHI, credentials or network addresses in this document. Reference secure locations instead.

## 1. Scope and success criteria
- What changes and what does not.
- Acceptance criteria (functional, performance, security), agreed with the application and clinical owners.
- Clinical workflows affected and the downtime window approved.

## 2. Preconditions
- [ ] Application inventory and dependencies confirmed (AM-01, AM-02).
- [ ] Business associate agreement in place for any new provider handling PHI (AM-22).
- [ ] Backup taken and restoration verified before the change (AM-17).
- [ ] Recovery objectives known and accepted for the change window (AM-18).
- [ ] Downtime procedures communicated to clinical departments (AM-19).
- [ ] Change approved through the release process (AM-13).

## 3. Test plan
| Test | Environment | Expected result | Result |
|---|---|---|---|
| Regression of critical clinical workflows | Test | | |
| Interfaces (HL7/FHIR/other) send and receive correctly | Test | | |
| Security checks (access, encryption, logging) | Test | | |
| Performance at expected peak | Test | | |

If AI-assisted engineering is used: approved tools only, no PHI in prompts or test data, and human review of every generated change (AM-16).

## 4. Execution steps
| # | Step | Responsible (role) | Duration | Verification |
|---|---|---|---|---|
| 1 | | | | |

## 5. Rollback plan
- Trigger: {{conditions that require rollback}}.
- Steps to restore the previous state and how to verify it.
- Maximum time before rollback decision.

## 6. Post-change
- [ ] Monitoring and alerts confirmed (AM-20).
- [ ] Inventory and dependency map updated (AM-04).
- [ ] Configuration baseline updated (ZT-08).
- [ ] Decision record, test results and operating instructions handed to the client team.
- [ ] Lessons learned recorded.
