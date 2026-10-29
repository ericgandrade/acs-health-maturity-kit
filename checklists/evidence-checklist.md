# Evidence Checklist

Evidence confirms an answer of 3 or 4 (see the thresholds in `docs/methodology.md`). Use this list to send evidence requests at intake and to check off what was seen during sessions. Per-question detail — exact artifacts, red flags and healthcare considerations — is in the Question Guide sheet and `docs/question-guide.md`.

## How to use evidence

- **Show, don't send.** Evidence is shown on screen. In Notes, record the artifact name, source system, date and what it demonstrated. Never copy PHI, credentials, network addresses or vulnerability details into the workbook.
- **Score 3** needs a current document **and** system output (or a test result, where the practice is a test) showing organization-wide coverage, with exceptions listed.
- **Score 4** also needs measurement over time (at least two review cycles or a trend) and automation or alerting where practical.
- **Freshness:** within the practice's own cycle and never older than 12 months.
- **Outsourced practices:** the provider's report plus evidence that the organization reviewed it and acted.
- **Configured is not enforced:** report-only or audit-mode policies support 2 at most.

Evidence type key: **D** document · **S** system output · **T** test or exercise result.

## License Optimization

### Governance & Ownership (LO-01 to LO-04)
- [ ] SAM owner named in a job description or RACI covering procurement, IT, finance and compliance (D) — LO-01
- [ ] Licensing policy and a sample of recent request and approval records (D, S) — LO-02
- [ ] Renewal calendar with all agreements and the record of the last renewal review, showing it started before the notice period (D) — LO-03
- [ ] Most recent licensing cost report presented to leadership, with cost per user (D) — LO-04

### Entitlements (LO-05 to LO-08)
- [ ] Entitlement register reconciled to the Microsoft licensing portal or partner statement (S) — LO-05
- [ ] Last reconciliation of entitlements against contracts and invoices, with differences resolved (D) — LO-06
- [ ] Register of clinical and business application licenses (EHR modules, imaging, laboratory, revenue cycle) with metrics and true-up terms (D) — LO-07
- [ ] List of third-party licenses embedded in vendor systems and medical devices, with the owner of each (D) — LO-08

### Deployment & Usage (LO-09 to LO-12)
- [ ] Automated software discovery report and its coverage of endpoints, servers and cloud (S) — LO-09
- [ ] Last quarterly license usage review with inactive assignments and actions taken (S, D) — LO-10
- [ ] HR separation list reconciled with directory account and license removal for the last period (S) — LO-11
- [ ] Licensing approach for shared clinical devices and frontline staff, with assignment report (D, S) — LO-12

### Security Value Realization (LO-13 to LO-16)
- [ ] Completed License-Security Map sheet, verified against current Microsoft documentation and the agreement (D) — LO-13
- [ ] MFA and conditional access coverage report showing policy state is On, not report-only (S) — LO-14
- [ ] Endpoint protection and device management coverage report across all endpoints, including shared clinical workstations (S) — LO-15
- [ ] Email protection and data protection (encryption, DLP) policy states and coverage (S) — LO-16

### Cloud Cost (LO-17 to LO-20)
- [ ] Tagging policy and cost allocation report by department or application (D, S) — LO-17
- [ ] Reservation, savings plan and hybrid-use benefit coverage report (S) — LO-18
- [ ] Last monthly rightsizing review with actions taken (S, D) — LO-19
- [ ] Budgets and spending alerts configured per subscription (S) — LO-20

### Programs & Negotiation (LO-21 to LO-24)
- [ ] Record of eligibility review for nonprofit, healthcare or rural programs and the outcome (D) — LO-21
- [ ] Last review of agreement type against size and needs (D) — LO-22
- [ ] Record of savings reinvested in named security or modernization projects (D) — LO-23
- [ ] Effective license position with the date and method used (D, S) — LO-24

## App Modernization

### Portfolio Visibility (AM-01 to AM-04)
- [ ] Application inventory with business owner, technical owner, vendor, hosting and data handled (S or D) — AM-01
- [ ] Interface catalog or dependency map, including HL7/FHIR feeds and the interface engine (D, S) — AM-02
- [ ] Criticality classification for patient care, revenue cycle and operations, approved by business owners (D) — AM-03
- [ ] Inventory change history showing the last annual review and updates after changes (S) — AM-04

### Lifecycle & Supportability (AM-05 to AM-08)
- [ ] List of applications on platforms past end of support, including Windows 10 and older server and database versions (S) — AM-05
- [ ] Approved and funded plan per unsupported platform: upgrade, isolate, retire or purchase extended updates (D) — AM-06
- [ ] Vendor support status, roadmap and contract terms for clinical applications (D) — AM-07
- [ ] Isolation design for systems that cannot be upgraded, including medical device software, with biomedical engineering sign-off; MDS2 forms where available (D) — AM-08

### Rationalization & Roadmap (AM-09 to AM-12)
- [ ] Disposition per application (Retire, Retain, Rehost, Replatform, Refactor, Replace, Isolate) approved by owners (D) — AM-09
- [ ] Sequenced modernization roadmap linked to business priorities (D) — AM-10
- [ ] Capability map showing overlapping applications and consolidation decisions (D) — AM-11
- [ ] Total cost of ownership for major applications (D) — AM-12

### Engineering & Release (AM-13 to AM-16)
- [ ] Change records for recent releases showing approval, testing and rollback plans, including vendor-applied changes (S) — AM-13
- [ ] Automated test results for critical applications or interfaces (S) — AM-14
- [ ] Code review, dependency scanning and secrets management settings in the pipeline (S) — AM-15
- [ ] AI-assisted engineering policy: approved tools, data restrictions (no PHI), human review (D) — AM-16

### Resilience & Recovery (AM-17 to AM-20)
- [ ] Backup configuration showing immutability or isolation and the last restoration test report (S, T) — AM-17
- [ ] Documented recovery time and recovery point objectives per critical application and the last DR test result against them (D, T) — AM-18
- [ ] Downtime procedures per clinical area and the record of the last downtime exercise (D, T) — AM-19
- [ ] Monitoring dashboard or alert history for outages and performance (S) — AM-20

### Cloud & Data Readiness (AM-21 to AM-24)
- [ ] Cloud foundation design: identity, network, security and cost governance (D, S) — AM-21
- [ ] Business associate agreements for every cloud and SaaS provider that handles PHI, matched to the application inventory (D) — AM-22
- [ ] Interface roadmap toward standards-based APIs where applicable (D) — AM-23
- [ ] Data classification, retention and migration rules for PHI (D) — AM-24

## Zero Trust

### Identity (ZT-01 to ZT-04)
- [ ] Access policy list showing state On for remote access, email, administrators and vendors; authentication methods report (S) — ZT-01
- [ ] Shared and generic account report, and the sign-in approach on shared clinical workstations (S, D) — ZT-02
- [ ] Privileged account inventory showing separate administrator accounts and how elevation is granted (S) — ZT-03
- [ ] Offboarding records for workforce and vendors with time from separation to account disablement (S) — ZT-04

### Devices (ZT-05 to ZT-08)
- [ ] Asset inventory coverage of endpoints, servers and connected medical devices, reconciled with network discovery and biomedical engineering records (S) — ZT-05
- [ ] Known exploited vulnerability remediation report against defined timeframes; compensating controls for devices that only the manufacturer can patch (S, D) — ZT-06
- [ ] Device compliance policy and its enforcement before PHI access (S) — ZT-07
- [ ] Configuration baselines and drift report (D, S) — ZT-08

### Networks (ZT-09 to ZT-11)
- [ ] Segmentation design showing separation of medical devices, clinical systems, guest and corporate traffic — described in zones, without addresses (D) — ZT-09
- [ ] Vendor and remote access method showing brokered, logged and time-limited sessions, with the session log for one recent vendor connection (S) — ZT-10
- [ ] Encryption in transit for internal and external PHI connections, including interface feeds (D, S) — ZT-11

### Applications & Workloads (ZT-12 to ZT-15)
- [ ] SPF, DKIM and DMARC records and enforcement policy; attachment and link scanning settings (S) — ZT-12
- [ ] Per-application access policies based on identity and context (S) — ZT-13
- [ ] Last vulnerability test or penetration test report summary for internet-facing systems and the remediation status (T) — ZT-14
- [ ] Contract clauses requiring vendors to disclose vulnerabilities and report incidents (D) — ZT-15

### Data (ZT-16 to ZT-19)
- [ ] Encryption-at-rest coverage for servers, endpoints, removable media and backups (S) — ZT-16
- [ ] Data map of PHI storage locations and classification labels (D, S) — ZT-17
- [ ] DLP policies and their state for email, cloud storage and endpoints (S) — ZT-18
- [ ] Backup isolation design and evidence that backups cannot be deleted or encrypted with production credentials (S, T) — ZT-19

### Visibility & Analytics (ZT-20 to ZT-22)
- [ ] Log source list for identity, endpoints, network and key applications, with retention (S) — ZT-20
- [ ] 24x7 detection and response arrangement (in-house or managed) and a recent escalation record (D, S) — ZT-21
- [ ] Record of the last PHI access review and follow-up (S, D) — ZT-22

### Governance & Readiness (ZT-23 to ZT-28)
- [ ] Security risk analysis completed in the last 12 months and the risk management plan it drives (D) — ZT-23
- [ ] Incident response plan covering ransomware and extended downtime, and the after-action report of the last exercise (D, T) — ZT-24
- [ ] Training completion and phishing exercise results for the whole workforce, including clinical staff (S) — ZT-25
- [ ] Vendor security requirements and pre-onboarding assessment records (D) — ZT-26
- [ ] Remediation tracker with owners and dates (S) — ZT-27
- [ ] Zero Trust strategy with target maturity per pillar and an executive sponsor (D) — ZT-28

## Evidence register (per open item)

| ID | Question | Artifact requested | Owner (role) | Due | Status (Requested / Seen / Not available) |
|---|---|---|---|---|---|
| EV-ZT-19 | ZT-19 | *Illustrative:* restore test report from the backup console | Systems administrator | 5 working days | Requested |
