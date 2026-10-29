# Zero Trust Playbook for Small Hospitals

A practitioner guide for the Zero Trust part of the ACS Health Maturity Kit (questions ZT-01 to ZT-28). It is written for the IT leader of a rural, community or independent hospital or clinic, and for the agent that runs the assessment. It explains what to look for, how to decide, what to do first and what usually goes wrong.

This playbook is a self-assessment aid. It is not legal or compliance advice, and following it does not establish HIPAA compliance.

## 1. Why this matters in healthcare

In most industries a cyberattack is a business outage. In a hospital it is also a clinical event: the EHR goes dark, lab and imaging results stop flowing, pharmacy verification slows, ambulances may be diverted and staff fall back to paper for days or weeks. The HHS publication *Health Industry Cybersecurity Practices* (HICP, 2023 edition) frames this as "cyber safety is patient safety" and names five threats that dominate the sector: social engineering, ransomware, loss or theft of equipment or data, insider data loss, and attacks against network-connected medical devices.

Small hospitals face these threats with one to five IT staff, limited budgets, many vendor-managed systems and medical devices they do not control. Zero Trust is useful here not as a product category but as a discipline: verify every user and device explicitly, grant the least access needed, and assume an attacker may already be inside, so that one stolen password or one compromised vendor does not become a hospital-wide outage.

The kit uses three reference points:

| Framework | Role in this playbook |
|---|---|
| HHS HPH Cybersecurity Performance Goals (10 Essential, 10 Enhanced) | The sector baseline; each ZT question maps to a goal where one applies |
| CISA Zero Trust Maturity Model v2.0 | Pillars (Identity, Devices, Networks, Applications and Workloads, Data) and cross-cutting capabilities (Visibility and Analytics, Automation and Orchestration, Governance); stages Traditional, Initial, Advanced, Optimal |
| HIPAA Security Rule (45 CFR Part 164, Subpart C) and NIST CSF 2.0 | Specific safeguards and outcome categories cited in each question |

The HHS CPGs are voluntary. They were built from the CISA cross-sector CPGs and link each goal to HICP sub-practices, so working through the Essential Goals is also a practical way to apply HICP. Public Law 116-321 includes approaches developed under section 405(d) of the Cybersecurity Act of 2015 among the types of recognized security practices that HHS considers. That is a reason to document what you do, not a safe harbor.

A note on regulation: HHS published a proposed update to the HIPAA Security Rule on January 6, 2025. It is a proposal, not a final rule. Track its status, but assess against the current rule.

## 2. Method, step by step

### Step 1: Prepare (one week before)

Send the evidence request from the agent's `*evidence-list` command. Minimum set: identity provider policy list and MFA report, any asset inventory, the clinical engineering equipment list, the last risk analysis, the incident response plan and last tabletop report, backup architecture and the last restore record, the list of vendors with remote access, and the MDR or on-call arrangement. Invite clinical engineering and a nursing or emergency management representative; without them, device and downtime answers are guesses.

### Step 2: Essentials first (45 to 60 minutes)

Run `*essentials`: ZT-01, ZT-02, ZT-03, ZT-04, ZT-06, ZT-10, ZT-11, ZT-12, ZT-16, ZT-24, ZT-25 and ZT-26. These map to the ten HHS Essential Goals. If the session is cut short, you still have the sector baseline.

### Step 3: Remaining questions by pillar (45 minutes)

Use `*assess` for the rest. For each question, read the level anchors, ask the opening question, probe for scope, and look at evidence before agreeing a score.

### Step 4: Ransomware readiness and vendor access

Run `*ransomware-readiness` using the checklist in section 5, and `*vendor-access` using the pattern in section 6. These two views are what executives remember.

### Step 5: Score, crosswalk and findings

Run the scoring tool, review the CPG Crosswalk sheet, then `*findings`. Rank by gap points, but apply judgment: a weight-3 gap that opens a direct ransomware path (backups, MFA, vendor access) comes before a weight-3 gap that is mainly documentation.

### Step 6: Agree and hand off

Confirm findings with participants, assign suggested owners, list open evidence, and hand off to the Maturity Lead.

## 3. Decision criteria

### 3.1 Scoring evidence thresholds

Evidence thresholds: as defined in `docs/methodology.md` (Evidence thresholds). In short: statement for 0–2; document and system output (or a test result) covering the whole scope for 3; plus measurement and review over time for 4.

Two rules settle most disputes. First, configured is not enforced: report-only, audit or test mode caps the score at 2. Second, scope exclusions cap the score at 2 when they exclude a population the question names (vendors, contractors, medical devices, backups).

### 3.2 Mapping kit levels to CISA ZTMM stages

The kit scores 0–4 per question; CISA describes four stages per pillar. A rough correspondence for discussion:

| Kit pillar score | Approximate ZTMM stage | What it usually means at a small hospital |
|---|---|---|
| Below 1.5 | Traditional | Manual, static, perimeter-based; flat network; shared logins |
| 1.5 to 2.5 | Initial | Some automation and MFA; partial inventories; vendor access listed |
| 2.5 to 3.5 | Advanced | Enforced policies across the scope; segmentation; tested restores; 24x7 coverage |
| Above 3.5 | Optimal | Continuous, automated, measured; rare in small hospitals and not required everywhere |

This correspondence is the kit's interpretation, not a CISA scale. A realistic two-year target for a small hospital is Advanced in Identity and in the backup part of Data, and Initial to Advanced elsewhere.

### 3.3 Prioritizing vulnerabilities

Order remediation by exploitation and exposure, not by severity score alone:

| Priority | Condition | Target |
|---|---|---|
| 1 | Listed in the CISA KEV catalog and internet-facing (VPN, firewall, remote access gateway, file transfer, web portal) | Days, per your written standard |
| 2 | KEV-listed and internal, or critical severity and internet-facing | Weeks |
| 3 | Critical or high severity, internal | Within the monthly cycle |
| 4 | Others | Normal maintenance |

CISA's KEV catalog lists vulnerabilities known to be exploited. It is binding on federal civilian agencies, and CISA recommends that every organization prioritize it. For devices that cannot be patched, record the manufacturer's position and compensate (segmentation, access restriction, monitoring) with an expiry date on the exception.

### 3.4 Backup design decision

| Question | Acceptable answer | Not acceptable |
|---|---|---|
| Can domain admin delete backups? | No: separate credentials, MFA, immutable or offline copy | Yes, or "we would notice" |
| Is one copy immutable or offline? | Yes, with a retention lock normal admins cannot shorten | Offsite copy that syncs deletions |
| When was the EHR last fully restored? | Within 12 months, with time recorded | Never, or files only |
| Hosted EHR? | Vendor evidence of immutability and restore testing on file; contract states restore commitments | "The vendor handles it" |

## 4. Healthcare-specific realities

**Medical devices (IoMT).** Infusion pumps, monitors, imaging modalities, lab analyzers and their workstations often run older operating systems, cannot take endpoint agents and can only be changed per manufacturer guidance. Clinical engineering usually owns them. The tools you have are visibility (inventory and passive discovery), information from the manufacturer (the MDS2 form, the SBOM, security advisories and patch guidance), and network control (segmentation). Section 524B of the Federal Food, Drug, and Cosmetic Act requires manufacturers of "cyber devices" to include in premarket submissions a plan to monitor and address postmarket vulnerabilities, processes to provide updates and patches, and an SBOM. These are obligations on manufacturers; for a hospital they are a basis for procurement questions, not something you can enforce on installed devices.

**Vendor-hosted and vendor-managed systems.** Many small hospitals use a hosted EHR, a cloud PACS and outsourced revenue cycle. Responsibility moves to the vendor, but accountability does not. Keep their evidence on file and put notification and restore terms in the contract.

**Shared clinical workstations.** Nursing stations, carts and procedure rooms are used by many people per shift. If sign-in takes too long, staff share sessions. Badge-tap or proximity sign-in with fast user switching, MFA at the start of a shift session, and appropriate screen locks keep unique credentials practical.

**Interfaces.** HL7 feeds through an interface engine connect the EHR to lab, imaging, pharmacy and billing. They are often unencrypted on the internal network, and changes need vendor coordination and downtime windows.

**24x7 operations.** There is no quiet period. Patching, segmentation changes and restore tests need agreed windows with nursing and the EHR team. Containment actions by a managed provider need pre-agreed rules for device workstations.

**Small teams.** Two or three people may hold all administrator rights and cover each other on call. Design break-glass accounts and after-hours approval so security does not depend on one person being reachable.

**Non-employee workforce.** Agency nurses, locums, students, volunteers and affiliated physicians are workforce members for training and access purposes but are not on HR payroll. Offboarding and training figures that exclude them overstate maturity.

## 5. Ransomware readiness checklist

Use with `*ransomware-readiness`. Each line maps to a question; a "No" is a finding.

**Initial access**

- [ ] MFA is enforced (not report-only) on every remote entry point, email and vendor account (ZT-01).
- [ ] Internet-facing systems are scanned and KEV-listed findings are remediated first (ZT-06, ZT-14).
- [ ] Vendor remote access goes through a broker; no always-on vendor VPN accounts; no unapproved remote control tools (ZT-10).
- [ ] DMARC is at enforcement; attachment and link scanning covers all mailboxes; users can report phishing easily (ZT-12, ZT-25).

**Privilege escalation and lateral movement**

- [ ] Administrators use separate accounts that do not read email or browse (ZT-03).
- [ ] Local administrator passwords are unique per device.
- [ ] Vendor and service accounts are not domain administrators.
- [ ] Medical devices, servers, users and guests are in separate segments with reviewed rules (ZT-09).

**Backup destruction and data theft**

- [ ] At least one backup copy is immutable or offline (ZT-19).
- [ ] Backup administration uses separate credentials with MFA, not domain admin.
- [ ] Alerts fire on backup deletion or retention changes.
- [ ] DLP and egress monitoring would show large outbound transfers (ZT-18, ZT-20).

**Detection and containment**

- [ ] A 24x7 service sees endpoint and identity alerts and can isolate devices and disable accounts (ZT-21).
- [ ] Logs from identity, endpoints, VPN, firewall, email and the EHR are centralized with defined retention (ZT-20).
- [ ] The after-hours escalation list was tested in the last six months.

**Response and recovery**

- [ ] The incident response plan has a ransomware playbook with out-of-band communication (ZT-24).
- [ ] A tabletop with clinical and executive participants was held in the last 12 months.
- [ ] A full restore of the EHR (or the vendor's evidence of one) exists, with time recorded.
- [ ] The restore order is documented: identity, network services, database, application, interfaces, printing, device integrations.
- [ ] Downtime procedures assume weeks, not hours: paper forms, downtime reports, result delivery, pharmacy, registration, staffing.
- [ ] Contacts for law enforcement, the cyber insurer, legal counsel and critical vendors are held offline.

Readiness statement: "Ready" if every line in Initial access, Backup destruction and Response is checked; "Partially ready" if most are; "Not ready" if backups can be deleted by domain admin or remote access lacks MFA, regardless of other answers.

## 6. Vendor remote access pattern

**Target pattern**

1. **One inventory.** Every vendor that can connect: system supported, connection method, account names, MFA status, internal owner, contract reference. Clinical engineering contributes medical device vendors.
2. **One path in.** Vendors connect through a remote access broker or gateway, not through the general VPN, not through remote desktop exposed to the internet, and not through tools they install themselves.
3. **Named accounts with MFA.** One account per vendor engineer, never a shared vendor login. The vendor tells you when an engineer leaves; the contract says so.
4. **Least access.** The session reaches only the system the vendor supports.
5. **Time-limited.** Access is enabled on request or on a schedule and expires. Define who approves after hours; hospitals need 2 a.m. support.
6. **Logged and reviewed.** Session logs or recordings retained; review a sample monthly.
7. **Contracted.** MFA, named accounts, notification of incidents and staff changes, and compliance with the access method are in the contract (ZT-15, ZT-26).

**Transition approach**

| Phase | Action | Effort |
|---|---|---|
| 1 | Build the inventory; find remote tools on servers and device workstations with EDR or software inventory | 2–3 weeks |
| 2 | Require named accounts with MFA on existing paths; disable shared vendor accounts | 2–4 weeks |
| 3 | Stand up the broker; migrate highest-risk vendors first (domain-level access, EHR, backup) | 1–3 months |
| 4 | Switch to request-based enablement; remove the old paths | 1–2 months |

Where a medical device manufacturer requires its own remote connectivity, record it with clinical engineering, restrict it to the device segment, and ask the manufacturer what controls it supports.

The 2024 Change Healthcare attack is the reference case for the sector: in congressional testimony, UnitedHealth Group's CEO acknowledged that the server attackers entered through did not have MFA. CISA's guide to securing remote access software covers how attackers misuse legitimate remote tools.

## 7. Medical device segmentation approach

**Principle:** segment by what devices need to talk to, not by department.

**Step 1: Know the devices.** Merge the clinical engineering list with network discovery. For each device type record manufacturer, model, operating system and support status, owner, location, MDS2 on file, SBOM on file, and the flows it needs (for example to the interface engine, PACS, a central monitoring station, the manufacturer's service).

**Step 2: Group by risk and function.**

| Group | Examples | Typical flows needed |
|---|---|---|
| Imaging | CT, MR, X-ray, ultrasound | PACS, modality worklist |
| Laboratory | Analyzers, middleware | Lab information system or middleware |
| Patient monitoring | Monitors, central stations | Central station, EHR integration |
| Infusion | Pumps, pump server | Pump server, drug library updates |
| Unsupported or high risk | Devices on end-of-support operating systems | Minimum required only |
| Building and facilities | HVAC, access control, cameras | Their own management systems |

**Step 3: Separate first, then restrict.** Moving devices out of user networks into their own segments gives most of the risk reduction; tightening rules to specific flows comes later. Do not start with the most fragile group; start with a group that has good manufacturer documentation and a cooperative vendor.

**Step 4: Change safely.** Agree a window with the clinical department, have clinical engineering and the vendor present, test the clinical workflow end to end (an order goes out, a result or image comes back), and have a rollback plan.

**Step 5: Monitor.** Alert on traffic from device segments to unexpected destinations; review rules annually and when devices are added.

**Procurement.** Require the MDS2 form, an SBOM, the patch and end-of-support commitment, and the remote access method before purchase (ZT-26).

## 8. Worked example (Illustrative)

*Fictional 25-bed critical access hospital with two clinics, three IT staff, a hosted EHR and about 400 networked medical devices.*

Essentials results (Illustrative):

| ID | Score | Weight | Gap points (4 − score) × weight |
|---|---|---|---|
| ZT-01 MFA | 2 | 3 | 6 |
| ZT-02 Unique credentials | 1 | 3 | 9 |
| ZT-03 Separate admin | 2 | 3 | 6 |
| ZT-04 Revocation | 2 | 3 | 6 |
| ZT-06 KEV remediation | 1 | 3 | 9 |
| ZT-10 Vendor access | 1 | 3 | 9 |
| ZT-11 Encryption in transit | 2 | 2 | 4 |
| ZT-12 Email security | 2 | 3 | 6 |
| ZT-16 Encryption at rest | 3 | 3 | 3 |
| ZT-24 Incident response | 1 | 3 | 9 |
| ZT-25 Training | 3 | 2 | 2 |
| ZT-26 Vendor requirements | 1 | 3 | 9 |

Reading the result (Illustrative): the CPG Crosswalk reports each Essential goal separately, using the unweighted average of its mapped questions (3 or more = Meets, 2 to 2.99 = Partially meets, below 2 = Gap). Read the status goal by goal; the kit does not combine the Essentials into a single figure.

Ranking: five items tie at 9 gap points. Judgment breaks the tie toward the ransomware path: ZT-10 (always-on vendor VPN accounts) and ZT-06 (an internet-facing VPN appliance with a KEV-listed issue) first, then ZT-24, ZT-02 and ZT-26. ZT-19 backups, outside the Essentials, scored 1 (domain-joined repository) and is added to the first wave because it decides whether recovery is possible at all.

## 9. Quick wins for small hospitals

| Quick win | Question | Why it is cheap |
|---|---|---|
| Turn report-only MFA policies on; remove stale exclusions | ZT-01 | Often already licensed (verify against your agreement); configuration work |
| Patch KEV-listed items on edge devices | ZT-06 | Small number of devices, high impact |
| Enroll in CISA's free external vulnerability scanning | ZT-06, ZT-14 | No cost for eligible organizations |
| Disable shared vendor accounts; require named accounts | ZT-10 | Configuration and a vendor letter |
| Move DMARC from none to quarantine after aligning senders | ZT-12 | DNS changes |
| Separate backup credentials and enable immutability if the backup product supports it | ZT-19 | Often an existing feature |
| Unique local administrator passwords | ZT-03 | Free tooling exists in common platforms |
| Run a two-hour ransomware tabletop with nursing and executives | ZT-24 | CISA and HHS publish free exercise materials |
| Use HHS 405(d) awareness materials | ZT-25 | Free |
| Add MDS2 and SBOM requests to purchasing | ZT-26 | A procurement checklist change |

## 10. A 90-day plan for a small hospital

Assumptions: two to four IT staff, an MDR service or budget for one, executive sponsor named at kickoff. Owners are suggestions.

**Days 0–30: close the doors**

| Action | Questions | Suggested owner |
|---|---|---|
| Inventory every remote entry point and vendor connection | ZT-01, ZT-10 | IT manager |
| Enforce MFA on all remote access, email and vendor accounts; turn report-only policies on | ZT-01 | Identity administrator |
| Patch KEV-listed findings on internet-facing systems; enroll in CISA scanning | ZT-06 | Infrastructure lead |
| Separate backup credentials, add MFA, enable immutability or an offline copy | ZT-19 | Infrastructure lead |
| Create separate admin accounts; remove admin rights from daily accounts | ZT-03 | IT manager |
| Confirm 24x7 alert coverage and after-hours escalation list | ZT-21 | IT manager |

**Days 31–60: limit the blast radius**

| Action | Questions | Suggested owner |
|---|---|---|
| Disable shared vendor accounts; begin broker rollout for highest-risk vendors | ZT-10 | IT manager |
| Merge IT and clinical engineering inventories; flag unsupported devices | ZT-05 | Clinical engineering lead |
| Move the first medical device group and building systems into their own segments | ZT-09 | Network lead |
| Inventory shared and generic accounts; plan fast user switching | ZT-02 | Identity administrator |
| Align third-party senders and move DMARC to quarantine | ZT-12 | IT manager |
| Agree MDR containment authority, including device workstation rules | ZT-21 | IT leader and CNO |

**Days 61–90: prove recovery**

| Action | Questions | Suggested owner |
|---|---|---|
| Full restore test of the EHR or obtain the vendor's evidence; record time | ZT-19 | Infrastructure lead, EHR vendor |
| Ransomware tabletop with clinical and executive leaders; update downtime procedures for multi-week outage | ZT-24 | Security lead, emergency management |
| Update the risk analysis with this assessment; build one remediation tracker | ZT-23, ZT-27 | Compliance officer |
| Add security clauses and MDS2/SBOM requests to purchasing and renewals | ZT-15, ZT-26 | Contracts, clinical engineering |
| Present pillar targets and a funded roadmap to the executive sponsor | ZT-28 | IT leader |

Expected result after 90 days (Illustrative): the Essentials average moves from Initial toward Developing/Defined in Identity, Data (backups) and Governance; segmentation and vendor broker work continue into the next quarter.

## 11. Common mistakes

- Buying a tool before enforcing what is already licensed.
- Counting policies in report-only mode as done.
- Excluding vendors, physicians or a whole unit from MFA "temporarily" and never revisiting.
- Treating the hosted EHR as out of scope.
- Running segmentation projects without clinical engineering and then rolling back after a broken workflow.
- Restoring files and calling it a restore test.
- Sizing downtime procedures for a planned four-hour outage.
- Signing an MDR contract that allows notification only.
- Setting Optimal targets in every pillar with no budget.
- Scanning fragile medical devices actively during clinical hours.

## 12. Glossary

| Term | Meaning |
|---|---|
| CPG | HHS Healthcare and Public Health Cybersecurity Performance Goal; Essential or Enhanced |
| EDR | Endpoint detection and response software |
| HICP | Health Industry Cybersecurity Practices, the HHS 405(d) publication |
| Immutable backup | A backup copy that cannot be changed or deleted until its retention period ends |
| IoMT | Internet of Medical Things: network-connected medical devices |
| KEV | CISA Known Exploited Vulnerabilities catalog |
| MDR / MSSP | Managed detection and response / managed security service provider |
| MDS2 | Manufacturer Disclosure Statement for Medical Device Security, a standard form describing a device's security capabilities |
| Phishing-resistant MFA | Methods such as FIDO2 security keys or certificate-based authentication that cannot be relayed by a fake sign-in page |
| PIM / PAM | Privileged identity management / privileged access management |
| SBOM | Software bill of materials: the list of software components in a product |
| Section 524B | FD&C Act section setting cybersecurity requirements for manufacturers of cyber devices in premarket submissions |
| ZTMM | CISA Zero Trust Maturity Model |

## 13. References

All links were checked (HTTP 200) on 2026-10-29.

- HHS HPH Cybersecurity Performance Goals: https://hhscyber.hhs.gov/cybersecurity-performance-goals.html
- HHS Health Industry Cybersecurity Practices (HICP), 2023 edition: https://hhscyber.hhs.gov/Documents/HICP/HICP-Main-508.pdf
- CISA Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
- CISA Zero Trust Maturity Model v2.0 (PDF): https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf
- CISA Known Exploited Vulnerabilities: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA Vulnerability Scanning service: https://www.cisa.gov/resources-tools/services/cisa-vulnerability-scanning
- CISA #StopRansomware Guide: https://www.cisa.gov/stopransomware/ransomware-guide
- CISA Guide to Securing Remote Access Software: https://www.cisa.gov/resources-tools/resources/guide-securing-remote-access-software
- CISA Implementing Phishing-Resistant MFA (fact sheet): https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf
- CISA Healthcare and Public Health resources: https://www.cisa.gov/topics/cybersecurity-best-practices/healthcare
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- HIPAA Security Rule, 45 CFR Part 164 Subpart C: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C
- Proposed HIPAA Security Rule update (NPRM, January 6, 2025): https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information
- FDA Cybersecurity in Medical Devices: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity
- FDA Cybersecurity in Medical Devices FAQs (section 524B): https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity-medical-devices-frequently-asked-questions-faqs
- FDA premarket cybersecurity guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-system-considerations-and-content-premarket-submissions
- House Energy and Commerce Committee, What we learned from the Change Healthcare cyber attack: https://energycommerce.house.gov/posts/what-we-learned-change-healthcare-cyber-attack
