# Framework Mapping

Each question in the kit and the frameworks it references. The mapping is the author's interpretation for self-assessment; it is not an official crosswalk and does not establish compliance.

Abbreviations: **CPG-E** = HHS Cybersecurity Performance Goal (Essential); **CPG-X** = HHS Cybersecurity Performance Goal (Enhanced); **ZTMM** = CISA Zero Trust Maturity Model v2.0; **CSF** = NIST Cybersecurity Framework 2.0; **SSDF** = NIST SP 800-218.

This file is generated from `data/questionnaire.csv` by `tools/build_docs.py`. For scoring anchors, interview probes and evidence, see the [Question Guide](question-guide.md).

## License Optimization

| ID | Dimension | Question | HHS CPG | Other references | Weight |
|---|---|---|---|---|---|
| LO-01 | Governance & Ownership | Is a named person accountable for software licensing, renewals and license compliance? | — | ISO/IEC 19770-1; NIST CSF 2.0 GV.RR | 2 |
| LO-02 | Governance & Ownership | Are licensing decisions governed by a documented policy (requests, approvals, reharvesting, retirement)? | — | ISO/IEC 19770-1; NIST CSF 2.0 GV.PO | 2 |
| LO-03 | Governance & Ownership | Are renewals tracked in a calendar and reviewed well before expiry? | — | FinOps Framework (Operate) | 3 |
| LO-04 | Governance & Ownership | Is licensing cost reported to leadership with trends and per-user metrics? | — | FinOps Framework (Inform); NIST CSF 2.0 GV.OV | 1 |
| LO-05 | Entitlements | Is there a complete, current record of all Microsoft entitlements (agreements, products, quantities, terms)? | — | ISO/IEC 19770-1; NIST CSF 2.0 ID.AM | 3 |
| LO-06 | Entitlements | Are entitlements reconciled against contracts and invoices at least annually? | — | ISO/IEC 19770-1 | 2 |
| LO-07 | Entitlements | Are licenses for clinical and business applications (EHR modules, imaging, laboratory, revenue cycle) inventoried in the same repository? | — | NIST CSF 2.0 ID.AM | 2 |
| LO-08 | Entitlements | Are third-party license obligations embedded in vendor systems and medical devices (e.g., bundled Windows or SQL Server) identified? | CPG-E: Vendor/Supplier Cybersecurity Requirements | NIST CSF 2.0 GV.SC | 1 |
| LO-09 | Deployment & Usage | Is actual software deployment discovered automatically across endpoints, servers and cloud? | CPG-X: Asset Inventory | NIST CSF 2.0 ID.AM | 3 |
| LO-10 | Deployment & Usage | Is the use of assigned user licenses reviewed at least quarterly? | — | FinOps Framework (Inform, Optimize) | 3 |
| LO-11 | Deployment & Usage | Are the accounts and licenses of departing workforce members removed and reharvested promptly? | CPG-E: Revoke Credentials for Departing Workforce Members | HIPAA 45 CFR 164.308(a)(3)(ii)(C) | 3 |
| LO-12 | Deployment & Usage | Are licensing models for shared clinical devices and frontline staff applied correctly? | — | ISO/IEC 19770-1 | 1 |
| LO-13 | Security Value Realization | Does the organization know which security capabilities are already included in its current licenses? | CPG-E: Multifactor Authentication; CPG-E: Email Security; CPG-E: Strong Encryption | NIST CSF 2.0 ID.AM, PR.AA | 3 |
| LO-14 | Security Value Realization | Are licensed identity protections (multifactor authentication, conditional access) deployed to all users, including clinical and remote access? | CPG-E: Multifactor Authentication | HIPAA 45 CFR 164.312(d); NIST CSF 2.0 PR.AA | 3 |
| LO-15 | Security Value Realization | Are licensed endpoint protection and device management deployed to all endpoints, including shared clinical workstations? | CPG-E: Mitigate Known Vulnerabilities; CPG-X: Configuration Management | NIST CSF 2.0 PR.PS | 3 |
| LO-16 | Security Value Realization | Are licensed email protection and data protection features (encryption, data loss prevention, labeling) enabled for PHI? | CPG-E: Email Security; CPG-E: Strong Encryption | HIPAA 45 CFR 164.312(e)(1); NIST CSF 2.0 PR.DS | 2 |
| LO-17 | Cloud Cost | Are cloud subscriptions tagged and costs allocated to departments or applications? | — | FinOps Framework (Inform) | 2 |
| LO-18 | Cloud Cost | Are reservations, savings plans and hybrid-use benefits applied where eligible? | — | FinOps Framework (Optimize) | 2 |
| LO-19 | Cloud Cost | Are idle or oversized cloud resources identified and rightsized at least monthly? | — | FinOps Framework (Optimize) | 2 |
| LO-20 | Cloud Cost | Are budgets and spending alerts configured for cloud subscriptions? | — | FinOps Framework (Operate) | 1 |
| LO-21 | Programs & Negotiation | Has eligibility for nonprofit, healthcare or rural hospital licensing programs and discounts been verified? | — | Microsoft rural hospital cybersecurity program, announced June 10, 2024 (AHA program flyer, December 2024) | 2 |
| LO-22 | Programs & Negotiation | Is the agreement type (e.g., Enterprise Agreement, CSP, MCA) reviewed against current size and needs before renewal? | — | FinOps Framework (Optimize) | 2 |
| LO-23 | Programs & Negotiation | Are savings from license optimization reinvested in documented security or modernization priorities? | — | NIST CSF 2.0 GV.RM | 1 |
| LO-24 | Programs & Negotiation | Is license compliance risk assessed with a defensible effective license position? | — | ISO/IEC 19770-1 | 2 |

## App Modernization

| ID | Dimension | Question | HHS CPG | Other references | Weight |
|---|---|---|---|---|---|
| AM-01 | Portfolio Visibility | Is there a complete inventory of applications with business owner, technical owner, vendor and hosting model? | CPG-X: Asset Inventory | NIST CSF 2.0 ID.AM | 3 |
| AM-02 | Portfolio Visibility | Are dependencies between applications (interfaces, databases, HL7 or FHIR feeds, shared infrastructure) documented? | — | NIST CSF 2.0 ID.AM | 3 |
| AM-03 | Portfolio Visibility | Is each application classified by its criticality to patient care, revenue cycle and operations? | — | HIPAA 45 CFR 164.308(a)(7)(ii)(E); NIST CSF 2.0 ID.AM | 3 |
| AM-04 | Portfolio Visibility | Is the application inventory reviewed at least annually and updated with every change? | — | NIST CSF 2.0 ID.AM | 2 |
| AM-05 | Lifecycle & Supportability | Do you know which applications depend on platforms past end of support (e.g., Windows 10, older Windows Server or SQL Server)? | CPG-E: Mitigate Known Vulnerabilities | NIST CSF 2.0 ID.AM, ID.RA | 3 |
| AM-06 | Lifecycle & Supportability | Is there a funded plan for each unsupported platform (upgrade, isolate, retire or purchase extended updates)? | CPG-X: Cybersecurity Mitigation | NIST CSF 2.0 GV.RM, ID.RA | 3 |
| AM-07 | Lifecycle & Supportability | Are vendor support status, roadmap and contract terms tracked for clinical applications? | — | NIST CSF 2.0 GV.SC | 2 |
| AM-08 | Lifecycle & Supportability | Are legacy systems that cannot be upgraded (including medical device software) isolated with compensating controls? | CPG-X: Network Segmentation | NIST CSF 2.0 PR.IR; CISA ZTMM v2.0 Networks | 3 |
| AM-09 | Rationalization & Roadmap | Does each application have a documented disposition (retire, retain, rehost, replatform, refactor, replace or isolate)? | — | NIST CSF 2.0 ID.AM, GV.RM | 2 |
| AM-10 | Rationalization & Roadmap | Is there a sequenced modernization roadmap aligned with business priorities and regulatory deadlines? | — | NIST CSF 2.0 GV.RM, ID.IM | 2 |
| AM-11 | Rationalization & Roadmap | Are redundant applications with overlapping functions identified for consolidation? | — | NIST CSF 2.0 ID.AM | 1 |
| AM-12 | Rationalization & Roadmap | Is the total cost of ownership known for major applications? | — | FinOps Framework (Inform) | 1 |
| AM-13 | Engineering & Release | Are changes deployed through a controlled, repeatable release process with approval and rollback? | CPG-X: Configuration Management | NIST CSF 2.0 PR.PS | 3 |
| AM-14 | Engineering & Release | Is automated testing used for critical applications before release? | — | NIST SP 800-218 PW.8; NIST CSF 2.0 PR.PS | 2 |
| AM-15 | Engineering & Release | Are secure development practices (code review, dependency scanning, secrets management) applied to in-house and customized code? | — | NIST SP 800-218 PO.1, PS.1, PW.4, PW.7, RV.1 | 2 |
| AM-16 | Engineering & Release | If AI-assisted engineering is used, is it governed by policy (approved tools, data restrictions, human review)? | — | NIST CSF 2.0 GV.PO; NIST SP 800-218 PO.3; NIST SP 800-218A | 2 |
| AM-17 | Resilience & Recovery | Are backups of critical applications and data protected from tampering and is restoration tested? | — | HIPAA 45 CFR 164.308(a)(7)(ii)(A),(D); NIST CSF 2.0 PR.DS, RC.RP | 3 |
| AM-18 | Resilience & Recovery | Do critical applications have recovery time and recovery point objectives that are tested? | — | HIPAA 45 CFR 164.308(a)(7)(ii)(B); NIST CSF 2.0 RC.RP | 3 |
| AM-19 | Resilience & Recovery | Are downtime procedures for clinical workflows documented and exercised? | — | HIPAA 45 CFR 164.308(a)(7)(ii)(C); NIST CSF 2.0 RC.RP | 3 |
| AM-20 | Resilience & Recovery | Is monitoring in place to detect application outages and performance degradation? | — | NIST CSF 2.0 DE.CM | 2 |
| AM-21 | Cloud & Data Readiness | Is there a cloud foundation (identity, network, security, cost governance) in place before migrations? | — | Microsoft Cloud Adoption Framework (Ready); NIST CSF 2.0 PR.PS | 2 |
| AM-22 | Cloud & Data Readiness | Are business associate agreements in place with all cloud and SaaS providers that handle PHI? | CPG-E: Vendor/Supplier Cybersecurity Requirements | HIPAA 45 CFR 164.308(b); NIST CSF 2.0 GV.SC | 3 |
| AM-23 | Cloud & Data Readiness | Are interfaces moving toward standards-based APIs (e.g., HL7 FHIR) where applicable? | — | HL7 FHIR; NIST CSF 2.0 ID.AM | 1 |
| AM-24 | Cloud & Data Readiness | Are data classification, retention and migration rules for PHI defined before applications are moved? | — | HIPAA 45 CFR 164.310(d)(2)(iv); NIST CSF 2.0 PR.DS | 2 |

## Zero Trust

| ID | Dimension | Question | HHS CPG | Other references | Weight |
|---|---|---|---|---|---|
| ZT-01 | Identity | Is multifactor authentication enforced for remote access, email and privileged accounts? | CPG-E: Multifactor Authentication | HIPAA 45 CFR 164.312(d); CISA ZTMM v2.0 Identity; NIST CSF 2.0 PR.AA | 3 |
| ZT-02 | Identity | Does every workforce member use unique credentials, including on shared clinical workstations? | CPG-E: Unique Credentials | HIPAA 45 CFR 164.312(a)(2)(i); NIST CSF 2.0 PR.AA | 3 |
| ZT-03 | Identity | Are administrator accounts separate from daily user accounts and granted only when needed? | CPG-E: Separate User and Privileged Accounts | CISA ZTMM v2.0 Identity; NIST CSF 2.0 PR.AA | 3 |
| ZT-04 | Identity | Are the accounts of departing workforce members and vendors revoked promptly? | CPG-E: Revoke Credentials for Departing Workforce Members | HIPAA 45 CFR 164.308(a)(3)(ii)(C); NIST CSF 2.0 PR.AA | 3 |
| ZT-05 | Devices | Is there a complete inventory of endpoints, servers and connected medical devices? | CPG-X: Asset Inventory | CISA ZTMM v2.0 Devices; NIST CSF 2.0 ID.AM | 3 |
| ZT-06 | Devices | Are known exploited vulnerabilities remediated within defined, risk-based timeframes? | CPG-E: Mitigate Known Vulnerabilities | CISA ZTMM v2.0 Devices; NIST CSF 2.0 ID.RA, PR.PS | 3 |
| ZT-07 | Devices | Is device health and compliance checked before access to PHI is granted? | — | CISA ZTMM v2.0 Devices; NIST CSF 2.0 PR.AA | 2 |
| ZT-08 | Devices | Are secure configuration baselines applied and configuration drift monitored? | CPG-X: Configuration Management | CISA ZTMM v2.0 Devices; NIST CSF 2.0 PR.PS | 2 |
| ZT-09 | Networks | Is the network segmented so that medical devices, clinical systems, guest and corporate traffic are separated? | CPG-X: Network Segmentation | CISA ZTMM v2.0 Networks; NIST CSF 2.0 PR.IR | 3 |
| ZT-10 | Networks | Is remote and vendor access brokered through controlled, logged and time-limited connections? | CPG-E: Vendor/Supplier Cybersecurity Requirements | CISA ZTMM v2.0 Networks; NIST CSF 2.0 PR.AA | 3 |
| ZT-11 | Networks | Is PHI encrypted in transit on internal and external connections? | CPG-E: Strong Encryption | HIPAA 45 CFR 164.312(e)(2)(ii); NIST CSF 2.0 PR.DS | 2 |
| ZT-12 | Applications & Workloads | Are email protections (SPF, DKIM, DMARC, attachment and link scanning) enforced? | CPG-E: Email Security | CISA ZTMM v2.0 Applications and Workloads; NIST CSF 2.0 PR.PS | 3 |
| ZT-13 | Applications & Workloads | Is access to applications granted per application based on identity and context, rather than network location? | — | CISA ZTMM v2.0 Applications and Workloads; NIST CSF 2.0 PR.AA | 2 |
| ZT-14 | Applications & Workloads | Are internet-facing systems and critical applications tested for vulnerabilities at least annually? | CPG-X: Cybersecurity Testing | NIST CSF 2.0 ID.RA | 2 |
| ZT-15 | Applications & Workloads | Are vendors required to disclose vulnerabilities and report incidents that affect your systems or data? | CPG-X: Third Party Vulnerability Disclosure; CPG-X: Third Party Incident Reporting | HIPAA 45 CFR 164.308(b); HIPAA 45 CFR 164.314(a)(2)(i)(C); NIST CSF 2.0 GV.SC | 3 |
| ZT-16 | Data | Is PHI encrypted at rest on servers, endpoints, removable media and backups? | CPG-E: Strong Encryption | HIPAA 45 CFR 164.312(a)(2)(iv); NIST CSF 2.0 PR.DS | 3 |
| ZT-17 | Data | Is PHI classified and are its storage locations known? | — | CISA ZTMM v2.0 Data; NIST CSF 2.0 ID.AM | 2 |
| ZT-18 | Data | Are data loss prevention controls applied to email, cloud storage and endpoints? | — | CISA ZTMM v2.0 Data; NIST CSF 2.0 PR.DS | 2 |
| ZT-19 | Data | Are backups isolated from the production environment and protected against ransomware? | — | HIPAA 45 CFR 164.308(a)(7)(ii)(A); NIST CSF 2.0 PR.DS, RC.RP | 3 |
| ZT-20 | Visibility & Analytics | Are security logs from identity, endpoints, network and key applications collected centrally? | CPG-X: Centralized Log Collection | HIPAA 45 CFR 164.312(b); CISA ZTMM v2.0 Visibility and Analytics; NIST CSF 2.0 DE.CM | 3 |
| ZT-21 | Visibility & Analytics | Is there 24x7 capability, in-house or managed, to detect and respond to relevant threats? | CPG-X: Detect and Respond to Relevant Threats and TTPs | NIST CSF 2.0 DE.CM, DE.AE, RS.MA | 3 |
| ZT-22 | Visibility & Analytics | Are records of access to PHI reviewed regularly? | — | HIPAA 45 CFR 164.308(a)(1)(ii)(D) | 2 |
| ZT-23 | Governance & Readiness | Has a security risk analysis been completed in the last 12 months, driving a risk management plan? | — | HIPAA 45 CFR 164.308(a)(1)(ii)(A),(B); NIST CSF 2.0 GV.RM | 3 |
| ZT-24 | Governance & Readiness | Is there a tested incident response plan covering ransomware and extended downtime? | CPG-E: Basic Incident Planning and Preparedness; CPG-X: Centralized Incident Planning and Preparedness | HIPAA 45 CFR 164.308(a)(6), 164.308(a)(7); NIST CSF 2.0 RS.MA, RC.RP | 3 |
| ZT-25 | Governance & Readiness | Does the whole workforce complete cybersecurity awareness training, including phishing exercises? | CPG-E: Basic Cybersecurity Training | HIPAA 45 CFR 164.308(a)(5); NIST CSF 2.0 PR.AT | 2 |
| ZT-26 | Governance & Readiness | Are cybersecurity requirements included in vendor contracts and verified before onboarding? | CPG-E: Vendor/Supplier Cybersecurity Requirements | HIPAA 45 CFR 164.308(b); NIST CSF 2.0 GV.SC | 3 |
| ZT-27 | Governance & Readiness | Are identified vulnerabilities and gaps tracked to closure with owners and dates? | CPG-X: Cybersecurity Mitigation | NIST CSF 2.0 ID.RA-06; NIST CSF 2.0 ID.IM | 2 |
| ZT-28 | Governance & Readiness | Is there a Zero Trust strategy with a target maturity per pillar and an executive sponsor? | — | CISA ZTMM v2.0 (Governance); NIST CSF 2.0 GV.OC | 1 |
