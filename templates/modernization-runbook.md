# Modernization Runbook — {{Application}}

**Change:** {{e.g., upgrade database platform / migrate to cloud / retire application}} · **Disposition:** {{Retire / Retain / Rehost / Replatform / Refactor / Replace / Isolate}} · **Owner (role):** {{role}} · **Change record:** {{reference}} · **Related questions:** AM-02, AM-05, AM-06, AM-13, AM-14, AM-17, AM-18, AM-19, AM-20, AM-22

> No PHI, credentials or network addresses in this document. Reference secure locations instead. Test data must be synthetic or de-identified. See `docs/playbooks/app-modernization.md` for guidance.

## 1. Scope and success criteria
- What changes and what does not (application version, operating system, database, hosting, interfaces).
- Acceptance criteria (functional, performance, security), agreed with the application and clinical owners.
- Clinical workflows affected and the downtime window approved.

| Item | Value |
|---|---|
| Application and criticality (1–5) | |
| Approved window (start, end, time zone) | |
| Maximum tolerable downtime agreed by clinical owner | |
| Rollback decision point (latest time to decide) | |
| Recovery objectives for this change (RTO / RPO) | |
| Vendor involved and certification reference for target versions | |

**Roles (names kept in the change record, roles here)**

| Role | Responsibility |
|---|---|
| Change lead | Runs the runbook, calls go/no-go and rollback |
| Application analyst | Executes application steps |
| Interface analyst | Pauses, tests and replays interfaces |
| Infrastructure lead | Servers, database, backup and restore |
| Clinical informatics lead | Clinical validation and sign-off |
| Department representatives | Downtime procedures and user acceptance in each affected unit |
| Vendor contact | Vendor-performed steps and escalation |
| Communications | Notices to units, help desk and leadership |

## 2. Preconditions
- [ ] Application inventory and dependencies confirmed, including interfaces outside the engine and shared infrastructure (AM-01, AM-02).
- [ ] Vendor certification of target operating system, database and runtime versions obtained in writing (AM-05, AM-07).
- [ ] Business associate agreement in place for any new provider handling PHI (AM-22).
- [ ] Backup taken and restoration verified before the change (AM-17).
- [ ] Recovery objectives known and accepted for the change window (AM-18).
- [ ] Downtime procedures communicated to clinical departments (AM-19).
- [ ] Change approved through the release process (AM-13).

### 2.1 Pre-checks (T–7 to T–1 days)
- [ ] Test environment results complete and signed (section 3).
- [ ] Rollback method rehearsed in test, with measured duration.
- [ ] Capacity and licensing for the target environment confirmed (verify against your agreement).
- [ ] Monitoring for the new environment configured and alert routing tested (AM-20).
- [ ] Security checks done on the target: access roles, encryption, logging, vulnerability scan.
- [ ] Downtime reports or read-only copy refreshed and checked in each affected unit.
- [ ] Freeze on other changes to dependent systems during the window.
- [ ] Vendor resources confirmed for the window and for hypercare.

### 2.2 Downtime communication

| When | Audience | Message | Channel | Sent (time / by) |
|---|---|---|---|---|
| T–5 days | Affected units, help desk, leadership | Window, impact, downtime procedures to use | | |
| T–1 day | Same, plus house supervisor | Reminder, contacts, downtime forms location | | |
| Start | Units, help desk | Downtime started; use downtime procedures | | |
| Go-live or rollback | Units, help desk | System available (or rollback); back-entry instructions | | |
| End of hypercare | Owners, leadership | Change closed; issues summary | | |

## 3. Test plan
| Test | Environment | Expected result | Result |
|---|---|---|---|
| Regression of critical clinical workflows | Test | | |
| Interfaces (HL7/FHIR/other) send and receive correctly | Test | | |
| Security checks (access, encryption, logging) | Test | | |
| Performance at expected peak | Test | | |
| Reports, printing and label printers used by clinical units | Test | | |
| Restore of the target environment from backup | Test | | |

### 3.1 Interface testing

| Interface | Direction | Message types | Test performed | Ack / result | Tester (role) |
|---|---|---|---|---|---|
| | Inbound / outbound | e.g., ADT, ORM, ORU, FHIR resource | Test message through engine, mapping checked | | |

Confirm for each interface: correct routing, field mapping, character handling, acknowledgments, error queue empty, and no duplicate messages.

### 3.2 Clinical validation sign-off

| Workflow | Script reference | Result | Signed by (role) | Date |
|---|---|---|---|---|
| e.g., order to result | | Pass / Fail | Clinical informatics lead | |
| e.g., medication order to administration | | | | |
| e.g., registration to charge | | | | |

Go-live requires a pass on every patient-safety workflow. Any exception needs written acceptance by the clinical owner.

If AI-assisted engineering is used: approved tools only, no PHI in prompts or test data, and human review of every generated change (AM-16).

## 4. Execution steps
| # | Step | Responsible (role) | Duration | Verification |
|---|---|---|---|---|
| 1 | Go/no-go confirmation (section 4.1) | Change lead | | Recorded decision |
| 2 | Announce downtime start | Communications | | Notice sent |
| 3 | Pause or queue interfaces; record queue position | Interface analyst | | Queue depth noted |
| 4 | Final backup or snapshot | Infrastructure lead | | Backup verified |
| 5 | Execute change steps | Application analyst / vendor | | Per step |
| 6 | Smoke tests and interface tests | Application and interface analysts | | Section 3.1 |
| 7 | Clinical validation in production | Clinical informatics lead | | Section 3.2 |
| 8 | Release interfaces; replay queued messages; reconcile | Interface analyst | | Queues drained, counts match |
| 9 | Announce availability and back-entry instructions | Communications | | Notice sent |

### 4.1 Go/no-go criteria

| Criterion | Status (Go / No-go) |
|---|---|
| All preconditions and pre-checks complete | |
| Clinical validation and interface tests passed in test | |
| Backup verified and rollback rehearsed within the decision window | |
| Required staff and vendor available for the window and hypercare | |
| No active incident, surge or diversion affecting the affected units | |
| Downtime procedures staffed in each affected unit | |

Any No-go postpones the change. Record who decided and why.

## 5. Rollback plan
- Trigger: {{conditions that require rollback}}.
- Steps to restore the previous state and how to verify it.
- Maximum time before rollback decision.

**Rollback triggers (adapt):**
- A patient-safety workflow fails clinical validation and cannot be fixed before the decision point.
- An interface cannot send or receive correctly before the decision point.
- A data integrity check fails (record counts, sample comparisons).
- Performance is unacceptable to clinical users at expected load.
- The change will exceed the approved window or the maximum tolerable downtime.

**After a rollback:** verify the previous version with the same smoke and interface tests, replay or reconcile queued messages, announce status, and record the cause before rescheduling.

## 6. Post-change
- [ ] Monitoring and alerts confirmed (AM-20).
- [ ] Inventory and dependency map updated (AM-04).
- [ ] Configuration baseline updated (ZT-08).
- [ ] Decision record, test results and operating instructions handed to the client team.
- [ ] Lessons learned recorded.
- [ ] Back-entry of downtime documentation completed and reconciled by each unit.
- [ ] Old environment retained read-only until the agreed date, then decommissioned per retention rules (AM-24).
- [ ] Recovery objectives retested if the hosting or backup method changed (AM-18).

### 6.1 Hypercare

| Item | Value |
|---|---|
| Hypercare period (agreed with owners) | |
| Support coverage (hours, on-call roles, vendor) | |
| Daily check: interface queues, error logs, performance, open issues | |
| Exit criteria (e.g., no open high-severity issues, clinical owner acceptance) | |

| # | Issue | Severity | Owner (role) | Status |
|---|---|---|---|---|
| 1 | | | | |
