# Playbook: App Modernization

A practitioner guide for IT leaders of small and mid-sized U.S. hospitals and clinics. It goes with the App Modernization Architect agent (`agents/app-modernization-architect.md`), questions AM-01 to AM-24, the App Portfolio Triage sheet of the workbook and `templates/modernization-runbook.md`.

> No PHI, credentials or network addresses belong in any artifact produced with this playbook. All examples are fictional and labeled Illustrative.

## 1. Why it matters in healthcare

A small hospital typically runs a large number of applications for its size: the EHR (often vendor-hosted), plus laboratory, pharmacy, imaging, blood bank, dietary, scheduling, document imaging, dictation, revenue cycle and a long tail of departmental tools. Many of them run on platforms the hospital does not fully control. Some sit on servers the vendor manages. Some are attached to regulated medical devices. Many connect through an interface engine that one analyst understands.

Three things make modernization different here:

1. **Failure is a clinical event.** A silent results interface, a failed overnight upgrade or a lost pharmacy system affects patient care, not only productivity.
2. **Constraints are external.** Vendors certify specific operating system and database versions. Device manufacturers control patching of regulated software. Records must be retained for periods set by law and policy.
3. **Teams are small.** The same few people run operations, projects and on-call. A roadmap that ignores their capacity fails.

The goal is not to modernize everything. It is to know what you have, decide deliberately what happens to each application, remove the unsupported-platform risk that attackers exploit, and be able to change and recover clinical systems safely.

## 2. Method overview

| Step | Output | Questions | Typical time (small hospital) |
|---|---|---|---|
| 1. Build the inventory | App Portfolio Triage sheet filled | AM-01, AM-03, AM-05 | 1 week |
| 2. Map dependencies | Interface catalog, dependency map for critical apps | AM-02 | 1–3 weeks |
| 3. Triage | Suggested dispositions, top 10 by priority | AM-09 | 1–2 days |
| 4. Decide | Owner-approved final dispositions | AM-09, AM-11, AM-12 | 2–4 weeks |
| 5. Handle unsupported platforms | Plan per platform | AM-05, AM-06, AM-08 | 2–4 weeks |
| 6. Plan waves | Roadmap | AM-10 | 2 weeks |
| 7. Execute safely | Runbooks, cutover, hypercare | AM-13, AM-14, AM-17–AM-20 | Per change |

## 3. Build the portfolio inventory in a week

The aim is a usable inventory, not a perfect one. It should be complete enough to rank risk, with gaps marked "Unknown" rather than left blank. The triage formula scores "Unknown" almost as high as "No", so unknowns surface naturally.

**Day 1: harvest lists.** Collect, without interviewing anyone yet:
- the accounts payable vendor list for the last 24 months, filtered to software, maintenance and SaaS;
- the contract list from procurement;
- the interface engine channel list;
- the single sign-on application list;
- installed-software and operating system reports from endpoint and server management tools;
- the EHR's list of third-party integrations;
- the list of applications in the disaster recovery plan.

**Day 2: consolidate.** Create one row per application in the App Portfolio Triage sheet. Merge duplicates: one application may appear as a vendor, a server and three interfaces. Fill the Application, Business function, Vendor and Hosting columns. Mark what you cannot fill as Unknown.

**Day 3: platform and risk inputs.** For each row, record the operating system and database (Platform / OS), whether the platform is supported (Yes/No/Unknown, checked against the vendor's official lifecycle page), whether there are open critical vulnerabilities (from the vulnerability scanner, or Unknown), whether the application handles PHI, and the integration count from the interface catalog.

**Day 4: owners and criticality.** Hold a 60-minute session with clinical informatics and department leaders. Assign business owners and rate criticality (1–5) and business value (1–5). Use a short, written scale:

| Criticality | Meaning (illustrative criteria the organization should adapt) |
|---|---|
| 5 | Loss stops or endangers patient care within hours (EHR access, results, medication administration, blood bank). |
| 4 | Loss degrades patient care or forces diversion decisions within a day. |
| 3 | Loss disrupts operations or revenue within days. |
| 2 | Loss is an inconvenience; workarounds exist for weeks. |
| 1 | No operational effect if lost. |

**Day 5: annual cost and gaps.** Add annual cost from accounts payable. Then run three checks:
- Do five vendors picked at random from accounts payable appear in the sheet?
- Do the interface engine channels map to applications?
- Do the device workstations clinical engineering knows about appear?

List the gaps as open items.

**Common gaps to look for:** departmental SaaS bought on a card; dictation, fax and secure messaging tools; device-attached workstations in imaging, laboratory and cardiology; downtime report workstations; reference laboratory and registry interfaces; and scheduled scripts that move files between systems.

## 4. Map dependencies

For each criticality 4–5 application, document:
- inbound and outbound interfaces (message type, transport, through the engine or not);
- database server and any shared databases;
- file shares and print services;
- the identity service (directory, single sign-on);
- network dependencies (VPN tunnels, vendor connections);
- the vendor's remote access path.

Rules of thumb:
- **The engine is not the catalog.** Point-to-point feeds, nightly file drops, direct database reads and vendor tunnels are often missing from the engine view.
- **Shared infrastructure binds waves.** If four applications share one database server, they move in the same wave or in a defined order.
- **Write down who notices.** For each critical interface, record who is alerted when it stops and how long until someone notices. That answer drives monitoring (AM-20).

## 5. Disposition decisions

### 5.1 The kit's dispositions

The kit uses seven dispositions: Retire, Retain, Rehost, Replatform, Refactor, Replace, Isolate. It is the kit's own list, aligned with common portfolio practice.

### 5.2 Decision tree

Work through the questions in order and stop at the first "yes".

| # | Question | If yes |
|---|---|---|
| 1 | Is business value low and criticality low (both 2 or less), or is the function duplicated elsewhere? | **Retire** (after records retention is agreed) or consolidate into the system that duplicates it. |
| 2 | Is the system kept only to look up historical records? | **Retire** to a read-only archive approved by records management. |
| 3 | Is the platform unsupported or the product end of life, and is the application valuable? | Can the vendor certify a supported platform? If yes, **Replatform**. If the product itself is end of life, **Replace**. |
| 4 | Is it unsupported but cannot change soon (device-attached, vendor-locked, replacement more than a year away)? | **Isolate** now, with an exit plan (Replace or Replatform later). |
| 5 | Is it in-house or heavily customized code that is insecure or unmaintainable? | **Refactor** if someone can maintain the result; otherwise **Replace**. |
| 6 | Does the EHR or another platform you already own provide the function adequately? | **Replace** (consolidate) after clinical workflow review. |
| 7 | Must the hardware or hosting location change (failing hardware, data center exit), on a supported platform? | **Rehost**. |
| 8 | None of the above. | **Retain**: invest if value is high, monitor if not. |

### 5.3 Criteria table

| Disposition | Key criteria | Evidence needed before approval | Common trap |
|---|---|---|---|
| Retire | Low value and criticality, duplicate, or lookup only | Records retention decision, interface impact check, user sign-off | Decommissioning with a hidden interface still feeding it |
| Retain | Supported, acceptable risk | Support end date beyond the roadmap horizon | Retaining by default because no one looked |
| Rehost | Infrastructure change only | Vendor support for the target environment | Rehosting an unsupported OS: the risk moves with it |
| Replatform | Upgrade OS, database or runtime; move to a managed service | Vendor certification of target versions; interface test plan | Upgrading the database before the vendor certifies it |
| Refactor | Owned code that must change | Maintainer, tests, secure development practices | Refactoring code no one will maintain |
| Replace | Product end of life or function available elsewhere | Total cost of ownership, workflow fit, data migration and retention plan | Buying a point solution the EHR already includes |
| Isolate | Cannot change soon | Allowed flows, brokered vendor access, exception record, exit plan | Isolation as a permanent state |

### 5.4 How the workbook suggests a disposition

The App Portfolio Triage sheet calculates:

- **Technical risk (0–8)** = unsupported platform 3 (Unknown 2) + open critical vulnerabilities 3 (Unknown 2) + handles PHI 1 + more than 5 integrations 1.
- **Priority (0–40)** = technical risk × criticality.
- **Suggested disposition**, checked in this order:
  1. business value ≤ 2 and criticality ≤ 2 → "Retire or consolidate";
  2. risk ≥ 5 and value ≥ 3 → "Modernize first (upgrade or replatform)";
  3. risk ≥ 5 → "Isolate and plan replacement";
  4. value ≥ 4 → "Retain and invest";
  5. otherwise → "Retain and monitor".

These five labels are suggestions. The owner records the final decision from the seven dispositions in the Final decision column.

### 5.5 Illustrative triage of five applications

All names and values are fictional.

| Application | Platform supported? | Open critical vulns? | PHI? | Integrations | Risk calculation | Criticality | Value | Priority | Suggested (workbook) | Proposed final |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Laboratory information system (self-hosted) | No (SQL Server 2014) | Unknown | Yes | 7 | 3 + 2 + 1 + 1 = **7** | 5 | 4 | 7 × 5 = **35** | Modernize first (upgrade or replatform) | Replatform |
| B. Cardiology device-attached review workstation | No (Windows 10, not enrolled in ESU) | Yes | Yes | 2 | 3 + 3 + 1 + 0 = **7** | 3 | 2 | 7 × 3 = **21** | Isolate and plan replacement | Isolate, then Replace |
| C. Legacy forms tool | Unknown | Unknown | Yes | 0 | 2 + 2 + 1 + 0 = **5** | 2 | 1 | 5 × 2 = **10** | Retire or consolidate | Retire |
| D. Vendor-hosted EHR | Yes | No | Yes | 12 | 0 + 0 + 1 + 1 = **2** | 5 | 5 | 2 × 5 = **10** | Retain and invest | Retain |
| E. Dietary management system | Yes (Windows Server 2016) | Unknown | Yes | 2 | 0 + 2 + 1 + 0 = **3** | 3 | 3 | 3 × 3 = **9** | Retain and monitor | Retain, then Replatform before January 2027 |

Reading the example:
- **A** ranks first. Modernize first means replatform, after the vendor certifies a supported SQL Server version. Pair it with interface regression across seven feeds and clinical validation by the laboratory.
- **B** has high risk but low value. Rule 1 does not apply because criticality is 3, so the workbook suggests isolation. Clinical engineering asks the manufacturer for its supported configuration and MDS2. The workstation moves into a restricted segment while a replacement is budgeted.
- **C** shows that rule 1 wins even with risk 5. Retiring it still requires records management to agree how its records are retained.
- **D** has low technical risk. Its 12 integrations make it the hub of the dependency map, so every other wave must schedule interface testing with it.
- **E** shows why the formula is not the whole story. Windows Server 2016 is supported today (risk counts it as supported) but reaches end of extended support in January 2027, so the roadmap must place it in an early wave anyway.

## 6. Unsupported-platform playbook

### 6.1 Facts to anchor on (verify on the official lifecycle pages)

- **Windows 10** reached end of support on October 14, 2025. Organizations can enroll devices running Windows 10, version 22H2 in the paid Extended Security Updates (ESU) program for a limited period. ESU delivers security updates only: no new features or general support.
- **Windows Server 2012 / 2012 R2** extended support ended in October 2023.
- **SQL Server 2014** extended support ended in July 2024. **SQL Server 2016** extended support ended in July 2026.
- **Windows Server 2016** extended support ends in January 2027.

ESU terms, eligibility and duration differ by product. Read the lifecycle page and the ESU FAQ for each one, and verify against your agreement. This playbook does not state prices.

### 6.2 Steps

1. **Find them.** From discovery data and the triage sheet, list every application that depends on an unsupported operating system, database, runtime or browser. Include device-attached and vendor-managed systems that discovery misses (ask clinical engineering and vendors).
2. **Classify the constraint.** For each one, decide which applies:
   - IT can upgrade it;
   - the vendor must certify an upgrade first;
   - the manufacturer controls it (regulated device);
   - the product is end of life.
3. **Choose a path.**

| Constraint | Path | Bridge while waiting |
|---|---|---|
| IT can upgrade | Upgrade (Replatform) in the next wave | ESU if eligible and the wave is months away |
| Vendor must certify | Request a written certification date; escalate at renewal | Isolate; ESU if eligible |
| Manufacturer controls | Follow manufacturer guidance; request MDS2, SBOM and patch plan | Isolate with brokered vendor access |
| Product end of life | Replace; plan data migration and retention | Isolate; consider retiring early |

4. **Fund and own it.** Each path needs an owner, a target date and approved funding (AM-06). Where the hospital accepts residual risk, have the accountable executive sign an exception with a review date.
5. **Isolate meanwhile.** Use a restricted segment that allows only documented flows, blocks user-workstation access and has no internet access unless required. Vendor access must be brokered and time-limited. Monitor traffic and keep an exception record (AM-08).
6. **Verify.** Confirm ESU enrollment on the devices, not only the purchase. Rescan after each upgrade. Update the triage sheet.

### 6.3 Medical devices

Device manufacturers have premarket cybersecurity obligations under section 524B of the FD&C Act, and FDA publishes guidance for them. Hospitals should not patch or reconfigure regulated device software outside the manufacturer's guidance. Hospitals can:
- request the MDS2 form and a software bill of materials;
- track manufacturer advisories and validated patches;
- isolate devices on restricted segments;
- include cybersecurity support terms in purchasing;
- involve clinical engineering in every decision.

## 7. Wave planning

### 7.1 Principles

- **Dependencies first.** Applications that share infrastructure move together or in a defined order. Upstream systems (identity, interface engine, database servers) are changed before or separately from the applications that depend on them.
- **Risk first, then value.** Sort by Priority, then adjust for dependencies, deadlines and capacity.
- **Capacity is the constraint.** Count the interface analyst, clinical informatics and vendor services hours each wave needs. In a small hospital, one or two people may be needed in every wave.
- **Respect clinical calendars.** Avoid EHR upgrade windows, regulatory surveys, seasonal census peaks and month-end billing.
- **Small waves.** Three to six applications per wave is manageable for a small team. Each wave should end with the inventory, dependency map and runbooks updated.

### 7.2 Illustrative wave plan for the five applications above

| Wave | Scope | Why here | Dependencies and constraints |
|---|---|---|---|
| 0 | Backups made immutable, interface queue monitoring, restore test of A | Foundations reduce the risk of every later change | Backup and monitoring tools |
| 1 | Isolate B; retire C after records decision; request vendor certification for A | Lowest effort, highest risk reduction | Clinical engineering, records management |
| 2 | Replatform A (database and OS upgrade) | Highest priority; needs vendor certification and seven interfaces retested | EHR (D) interface testing, laboratory validation, overnight window |
| 3 | Replatform E before January 2027 | Platform end of support | Dietary and EHR interface tests |
| 4 | Replace B | Budget cycle | Manufacturer, capital approval |

### 7.3 Change windows in 24x7 operations

Agree windows with nursing, pharmacy, laboratory and imaging leaders. Prefer low-census hours and avoid shift changes and medication pass times. Confirm the downtime plan is staffed for the window. Announce the window several days ahead, again the day before and at start and end. The runbook template defines the communication steps.

## 8. Engineering and release essentials

- **Change control for everything** (AM-13). Vendor-performed remote upgrades go through the same approval, communication and verification steps.
- **Clinical validation** (AM-14). Clinical informatics owns scripted workflow tests, for example:
  - order to result;
  - medication order to dispense to administration;
  - registration to charge;
  - image order to report.
  Keep the scripts and rerun them on every upgrade. Use synthetic or de-identified test data.
- **Interface regression.** Send test messages for each message type through each changed interface. Confirm receipt, mapping and acknowledgments. Check queues before and after.
- **Secure development** (AM-15). Most small hospitals own more code than they think: interface transformations, report queries, scripts. From NIST SP 800-218, the minimum is:
  - protected version control (PS.1);
  - review (PW.7);
  - dependency checks (PW.4);
  - testing (PW.8);
  - ongoing vulnerability identification (RV.1).
  Remove credentials from scripts and use a managed vault.
- **Vendor evidence.** Ask vendors for secure development evidence. The CISA secure software self-attestation form is an example of what producers give federal agencies and can be requested or matched by equivalent evidence.
- **AI-assisted engineering** (AM-16). Use approved tools only, keep PHI and secrets out of prompts, logs and test data, and have a person review every generated change.

## 9. Recovery tiers

Set recovery objectives per criticality with clinical and business owners. The values below are an illustrative structure, not benchmarks. The organization sets its own, matched to how long downtime procedures can safely carry operations.

| Tier | Examples | Illustrative RTO / RPO the organization might set | Test approach |
|---|---|---|---|
| 0 (dependencies) | Identity, DNS and network services, interface engine, backup system | Restored before Tier 1 | Included in every Tier 1 exercise |
| 1 (patient care) | EHR access, laboratory, pharmacy, imaging, blood bank | Hours / minutes to an hour | Annual full restore with interfaces, plus downtime exercise |
| 2 (revenue and operations) | Revenue cycle, scheduling, supply chain | One to a few days / hours | Annual restore |
| 3 (business) | Intranet, reporting, training | Days to weeks / a day | Restore on sample basis |

For vendor-hosted systems, compare the vendor's contractual recovery commitments with your tier. Also define how clinicians see data during the vendor's outage: downtime reports or a read-only copy.

## 10. Cutover and rollback checklist

Use with `templates/modernization-runbook.md`.

**Before (T–14 to T–1 days)**
- [ ] Owner-approved disposition and change record approved (AM-09, AM-13).
- [ ] Vendor certification of target versions in writing.
- [ ] Dependency map and interface list for the application confirmed (AM-02).
- [ ] Clinical validation scripts and interface tests passed in test; sign-off recorded.
- [ ] Business associate agreement in place for any new provider handling PHI (AM-22).
- [ ] Backup taken and a restore verified; rollback method tested (AM-17).
- [ ] Downtime plan staffed; downtime reports or read-only copy refreshed (AM-19).
- [ ] Communication sent to affected units, help desk and on-call.
- [ ] Go/no-go meeting held with application owner, clinical informatics, IT and vendor.

**During**
- [ ] Interfaces paused or queued at a recorded point; queue depth noted.
- [ ] Execution steps followed in order with timestamps.
- [ ] Rollback decision point time stated at start and watched.
- [ ] Smoke tests, interface tests and clinical validation run before release to users.

**Rollback triggers (examples to adapt)**
- Clinical validation fails on any patient-safety workflow.
- An interface cannot send or receive correctly and cannot be fixed before the decision point.
- Data integrity check fails.
- The change will exceed the approved window or the downtime tolerance.

**After**
- [ ] Queued messages replayed and reconciled.
- [ ] Back-entry of downtime documentation complete.
- [ ] Monitoring and alerts confirmed (AM-20).
- [ ] Inventory, dependency map and configuration baseline updated (AM-04).
- [ ] Hypercare staffed for the agreed period; issues logged.
- [ ] Lessons learned recorded.

## 11. Quick wins for small hospitals

1. Fill the triage sheet from accounts payable and discovery in one week.
2. Run discovery for Windows 10, Windows Server 2012/2012 R2/2016 and SQL Server 2016 or earlier, and put the results in the triage sheet.
3. Confirm ESU enrollment on every Windows 10 device you kept.
4. Block user-workstation access to device-attached systems.
5. Monitor interface engine queue depth and message age, with after-hours alerts.
6. Test one full restore of the most critical self-hosted application, including interfaces.
7. Refresh downtime reports and check the downtime workstations.
8. Move interface and report scripts into version control and remove embedded credentials.
9. Reconcile the business associate agreement register with PHI-flagged inventory rows.
10. Retire one lookup-only legacy system to an approved read-only archive.

## 12. Common mistakes

- Scoring from the inventory you wish you had. Unknown is an answer; blank is not.
- Treating the workbook's suggested disposition as the decision.
- Rehosting unsupported platforms to cloud infrastructure and calling it modernization.
- Planning waves by application instead of by dependency.
- Upgrading a database before the clinical vendor certifies it.
- Letting vendors change production outside change control.
- Testing technical function without clinical validation.
- Treating ESU as the plan rather than a bridge.
- Decommissioning before the records retention decision.
- Planning downtime for hours when ransomware outages last weeks.

## 13. Glossary

- **ADT, ORM, ORU**: HL7 v2 message types for admission, discharge and transfer, orders, and observation results.
- **Disposition**: the decision for an application (Retire, Retain, Rehost, Replatform, Refactor, Replace, Isolate).
- **ESU**: Extended Security Updates, a paid program that provides security updates for some Microsoft products after end of support for a limited period.
- **FHIR**: HL7 Fast Healthcare Interoperability Resources, a standard for exchanging health data through APIs.
- **Hypercare**: a period of heightened support after go-live.
- **Interface engine**: middleware that routes and transforms messages between clinical systems.
- **MDS2**: Manufacturer Disclosure Statement for Medical Device Security, a standard form describing a device's security features.
- **RTO / RPO**: recovery time objective (how fast) and recovery point objective (how much data loss is acceptable).
- **SBOM**: software bill of materials.
- **SSDF**: NIST Secure Software Development Framework, SP 800-218.

## 14. References

Opened on 2026-10-29.

- Microsoft lifecycle, Windows 10 Enterprise and Education: https://learn.microsoft.com/en-us/lifecycle/products/windows-10-enterprise-and-education
- Microsoft, Windows 10 Extended Security Updates: https://learn.microsoft.com/en-us/windows/whats-new/extended-security-updates
- Microsoft lifecycle FAQ, Extended Security Updates: https://learn.microsoft.com/en-us/lifecycle/faq/extended-security-updates
- Microsoft lifecycle, Windows Server 2012 R2: https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2012-r2
- Microsoft lifecycle, Windows Server 2016: https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016
- Microsoft lifecycle, SQL Server 2014: https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2014
- Microsoft lifecycle, SQL Server 2016: https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2016
- NIST SP 800-218, Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST Cybersecurity Framework 2.0: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- NIST SP 800-34 Rev. 1, Contingency Planning Guide: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
- FDA, Cybersecurity in medical devices: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity
- FDA, Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-system-considerations-and-content-premarket-submissions
- FDA, Cybersecurity in Medical Devices FAQs: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity-medical-devices-frequently-asked-questions-faqs
- HL7 FHIR: https://hl7.org/fhir/
- Health Industry Cybersecurity Practices (HICP), developed under the HHS 405(d) program: https://healthsectorcouncil.org/hicp/
- HHS Healthcare and Public Health Cybersecurity Performance Goals: https://hhscyber.hhs.gov/cybersecurity-performance-goals.html
- HIPAA Security Rule, 45 CFR Part 164 Subpart C: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C
- ONC SAFER Guides: https://www.healthit.gov/topic/safety/safer-guides
- CISA Secure Software Development Attestation Form: https://www.cisa.gov/secure-software-attestation-form
- Microsoft Azure Well-Architected Framework, disaster recovery: https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery
- Microsoft Cloud Adoption Framework, landing zones: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
