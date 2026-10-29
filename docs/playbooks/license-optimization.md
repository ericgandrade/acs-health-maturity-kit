# Playbook: License Optimization

A practitioner guide for IT leaders and CFOs of small and mid-sized U.S. hospitals and clinics, and for the License Optimization Analyst agent. It covers questions LO-01 to LO-24 in `data/questionnaire.csv` and the License-Security Map in `data/license_security_map.csv`.

> **Advisory only.** This playbook is a self-assessment aid. It is not licensing, legal or compliance advice. Statements about what a Microsoft plan includes describe what is *typically* included according to Microsoft documentation reviewed on October 29, 2026. Always verify against current Microsoft documentation, the Product Terms and your own agreement. No prices are given.

## 1. Why this matters in healthcare

Hospitals spend on software in three places at once: productivity and security suites (usually Microsoft 365), clinical applications (EHR, imaging, laboratory, pharmacy, revenue cycle) and, increasingly, cloud infrastructure. In a small hospital these are often bought by different people. The CFO signs contracts, IT runs the tenant, departments buy modules from clinical vendors and a reseller handles renewals. Nobody sees the whole picture.

Three consequences follow:

1. **Shelfware.** Licenses are bought for peak headcount, kept for departed staff, or assigned at a higher tier than the role needs.
2. **Security left on the table.** Plans such as Microsoft 365 Business Premium, E3 and E5 typically include capabilities that map directly to HHS Cybersecurity Performance Goals: multifactor authentication, email security, encryption, endpoint detection and response, and audit logging. These capabilities are often licensed and not deployed. For a budget-constrained hospital, deploying what it already owns is usually the fastest and cheapest security improvement available.
3. **Compliance exposure.** On-premises Windows Server and SQL Server licensing, often on servers that run clinical systems, is the most common gap. It surfaces during an audit or a migration.

License optimization connects all three. Money recovered from shelfware can fund security gaps. Knowing what is licensed prevents duplicate purchases. A defensible license position removes surprise costs.

## 2. Method: entitlement, deployment and usage reconciliation

The method follows the logic of software asset management standards such as ISO/IEC 19770-1. It compares three views of the same product and acts on the differences.

| View | Question | Typical sources |
|---|---|---|
| **Entitlement** | What do we have the right to use? | Agreements, order forms, invoices, reseller statements, Microsoft 365 admin center (Billing > Your products), volume licensing summaries for perpetual licenses |
| **Deployment** | What is assigned or installed? | Microsoft 365 admin center (Billing > Licenses), Entra user and group assignments, endpoint management and EDR software inventory, server and hypervisor inventory |
| **Usage** | What is actually used, by whom, how much? | Microsoft 365 usage reports (Active users, Microsoft 365 Apps usage, Email activity), Entra `signInActivity`, application logs, department counts for clinical metrics |

### Step 1: Scope and owners (week 1)

- Name the SAM owner and a backup (LO-01).
- List every software vendor, agreement and billing account. Include accounts held by former resellers, affiliated clinics and departments (LO-05, LO-07).
- Agree the workforce categories with HR and the medical staff office: employed, PRN or per diem, agency or traveler, locum, resident, student, volunteer, vendor and affiliated physician. Each category behaves differently in usage data.

### Step 2: Build the entitlement register (weeks 1–3)

For each product, record:
- Agreement or channel (Enterprise Agreement, CSP, Microsoft Customer Agreement).
- Agreement number, product, quantity and term start and end.
- Billing frequency.
- Notice and auto-renewal terms.
- Software Assurance status.
- License metric (user, device, core, bed, provider, study).

Do not copy quantities from the admin center as if they were entitlements. The admin center shows what is provisioned, and purchase records show what was bought. Where they differ, investigate.

Include perpetual Windows Server and SQL Server licenses and Software Assurance. These determine Azure Hybrid Benefit eligibility (LO-18) and are central to any license position (LO-24).

### Step 3: Collect deployment and usage data (weeks 2–4)

**Microsoft 365**
- Purchased vs assigned per product: Microsoft 365 admin center, Billing > Licenses.
- Usage for 90 and 180 days: Reports > Usage. Usage reports conceal user, group and site names by default. A Global Administrator can turn this off in Org settings > Services > Reports if your privacy practices allow it, and the change is logged in the audit log. For a counts-only analysis, keep names concealed and work with totals.
- Last sign-in: Microsoft Entra admin center (Users, add the "Last interactive sign-in time" column) or Microsoft Graph `signInActivity`. Reading `lastSuccessfulSignInDateTime` through Graph requires Entra ID P1 or P2. Values may take up to 24 hours to update.

**Servers and applications**
- Servers: OS and SQL Server edition, cores, host and cluster, and whether disaster recovery or downtime copies exist.
- Clinical applications: the operational count for each license metric, provided by the department.

### Step 4: Reconcile and classify (weeks 3–5)

For each product, compute:

| Category | Definition | Action class |
|---|---|---|
| Unassigned | Purchased − assigned | Reduce at next allowed date, or reuse |
| Inactive | Assigned, no qualifying activity in the agreed window (for example 90 days), not on an exception list | Confirm with HR, then reharvest |
| Over-tier | Active, but uses only capabilities of a lower or frontline plan | Candidate downgrade, confirmed with department |
| Under-licensed | Deployed or used beyond entitlement | Risk to confirm with licensing partner |
| Security value gap | Capability licensed for users, not deployed or not covering them | Deploy (see section 7) |

**Choose the inactivity window deliberately.** Microsoft notes that many organizations use 90 to 180 days. In hospitals, keep an exception list for PRN and per-diem staff, staff on leave, seasonal and agency staff, and residents between rotations. Confirm every candidate with HR or the medical staff office before acting.

### Step 5: Decide and act (weeks 5–8)

- Reharvest inactive licenses and reuse them before buying new ones (LO-10, LO-11).
- Schedule reductions for the next allowed date. Under CSP new commerce, subscriptions can be canceled only in the first seven days of a term, so treat reductions on annual terms as end-of-term changes. Under an Enterprise Agreement, follow the anniversary and true-up process in the agreement.
- Send candidate plan changes to the department and the licensing partner (section 5).
- Deploy security value gaps (section 7).
- Record realized savings from invoices, not projections (LO-23).

### Step 6: Make it routine

- Run the reconciliation quarterly.
- Report to leadership at least semiannually (LO-04).
- Repeat it in full before every renewal (section 6).
- Automate the exports where practical, for example a scheduled Graph query for sign-in activity.

## 3. Worked shelfware calculation (Illustrative)

All quantities below are **fictional**, and prices are placeholders. Replace $P (price per user per month for the plan) and $Q (price per user per month for the candidate lower plan) with your own contract prices.

**Illustrative hospital:** 260 users on one plan with an annual term.

| Line | Symbol | Illustrative value |
|---|---|---|
| Licenses purchased | N_p | 260 |
| Licenses assigned | N_a | 238 |
| Assigned and active in last 90 days (after exception list) | N_act | 205 |
| Active users who use only web email, Teams and the EHR on shared workstations (candidate frontline or lower plan) | N_down | 30 |

**Formulas**

- Unassigned: U = N_p − N_a = 260 − 238 = **22**
- Inactive: I = N_a − N_act = 238 − 205 = **33**
- Annual unassigned waste: W_u = U × $P × 12 = 22 × $P × 12 = **264 × $P**
- Annual inactive waste: W_i = I × $P × 12 = 33 × $P × 12 = **396 × $P**
- Annual over-tier opportunity: W_d = N_down × ($P − $Q) × 12 = **360 × ($P − $Q)**
- Total annual opportunity: W = W_u + W_i + W_d = **660 × $P + 360 × ($P − $Q)**

**Timing matters.** The opportunity becomes savings only when quantities can change.

- **Annual CSP term:** reductions take effect at the term end. If the term ends in m months, first-year realized savings ≈ (U + I) × $P × (12 − m), assuming the lower quantity is renewed. Before then, the immediate value comes from reusing reharvested licenses instead of buying new ones.
- **Enterprise Agreement:** reductions depend on the enrollment type and anniversary terms. Model them only after confirming with your agreement.

**Reuse value.** If the hospital expects H new hires before the term ends, reusing reharvested licenses avoids buying min(H, U + I) new licenses.

**Sensitivity check.** Re-run I with a 180-day window. In the illustration, assume N_act rises to 219, so I = 19. Present both results. The difference is the population that needs HR confirmation.

**What the CFO sees (Illustrative):** "55 licenses are unassigned or inactive. Removing them at the term end avoids 660 × $P per year, and about 30 users may fit a lower plan. Realization depends on the renewal date and HR confirmation. Numbers to be confirmed with our licensing partner."

## 4. Workforce realities that change the numbers

- **PRN, per diem and agency staff** may work a few shifts a month. Use a longer activity window or an exception list, and give each agency account a sponsor and an end date.
- **Residents, students and rotating clinicians** follow academic calendars. Coordinate with the education coordinator and the medical staff office.
- **Shared clinical workstations.** Microsoft's shared computer activation documentation uses nurses sharing hospital computers as a supported example. Each user who signs in needs their own qualifying license, and generic shared accounts are not a licensing solution. They also break unique-credential requirements.
- **Kiosks, carts and dedicated devices** can use Intune device-only licenses. Device-only enrollment does not support Conditional Access or app protection policies, so it is unsuitable for devices that access PHI under user-based Conditional Access.
- **Departed staff mailboxes** may contain PHI and fall under retention requirements. Apply retention or conversion per policy before removing licenses.
- **Vendor and affiliated physician accounts** often need a different license and access model, such as guest access or a limited plan. Decide this explicitly.

## 5. Plan selection decision table

Use this to frame options for the licensing partner, not to decide alone. The "Typical inclusions" column comes from Microsoft documentation reviewed on October 29, 2026 (see section 11). Verify each item against your agreement.

| Situation | Option to model | Typical inclusions to verify | Watch-outs |
|---|---|---|---|
| Up to 300 users, mostly office and clinical staff, limited security tooling | **Microsoft 365 Business Premium** | Entra ID P1 (Conditional Access), Intune Plan 1, Defender for Business, Defender for Office 365 P1, Purview Message Encryption, manual labeling, DLP for Exchange/SharePoint/OneDrive, Audit (Standard); supports shared computer activation | Designed for up to 300 users; add-ons for Business Premium are capped at 300 seats; plan for growth and affiliations |
| Up to 300 users that need risk-based Conditional Access, PIM or identity threat detection | **Business Premium + Defender Suite for Business Premium** (and/or Purview Suite for Business Premium) | Adds Entra ID P2 and Defender capabilities; Purview Suite adds Audit (Premium) and advanced data protection | Same 300-seat cap; compare total cost with enterprise plans |
| Above 300 users, or expected to cross 300 | **Microsoft 365 E3** | Entra ID P1, Intune Plan 1, Defender for Endpoint P1, Purview core features (Message Encryption, manual labeling, DLP for Exchange/SharePoint/OneDrive), Audit (Standard), Microsoft 365 Apps for enterprise | Email protection beyond built-in protection may need an add-on; verify, because Microsoft pages differ on Defender for Office 365 P1 in E3 |
| E3 estate needing advanced security for all or some users | **E3 + Microsoft Defender Suite** (formerly Microsoft 365 E5 Security) | Entra ID P2, Defender for Endpoint P2, Defender for Office 365 P2, Defender for Identity, Defender for Cloud Apps | Some tenant-level services can't be limited to licensed users; license everyone who benefits |
| Need for advanced compliance (automatic labeling, Endpoint DLP, Audit Premium) plus advanced security | **Microsoft 365 E5**, or E3 + Defender and Purview Suites | E3 capabilities plus the security and compliance capabilities above | Compare full E5 with add-ons by role |
| Clinicians and staff who work mainly on shared devices, phones or tablets | **Frontline plans (F1, F3)** for those roles | Entra ID P1; F3 includes Purview Message Encryption and manual labeling; Audit (Standard) in F1 and F3 | Confirm desktop app needs, mailbox needs and device management before moving users; mixed estates need per-plan Conditional Access design |
| Kiosks, carts, dedicated devices without a named user | **Intune device-only licenses** | Device-targeted management | No Conditional Access or app protection; not for PHI access under user-based policies |

**Heuristics**

- Start with roles, not the whole estate. Administrators, executives, finance, and staff handling referrals or billing mailboxes are the usual candidates for advanced email and identity protection.
- Count every user who benefits from a tenant-level protection. For example, Defender for Office 365 licensing applies to users who access protected mailboxes, including shared mailboxes.
- Prefer deploying what you own before adding plans. A Business Premium or E3 tenant with Conditional Access unconfigured will gain more from configuration than from an upgrade.

## 6. Renewal readiness timeline (9–6–3)

Microsoft's Enterprise Agreement guidance describes a 120-day start for true-up discussions and requires the annual true-up order between 60 and 30 days before the anniversary. For a small hospital that also has to fit a budget cycle, start earlier.

| When | Activities | Output |
|---|---|---|
| **9 months before term end** | Confirm term end, notice and auto-renewal dates for each agreement; confirm SAM owner and backup; check budget calendar; recheck program eligibility (nonprofit, rural hospital programs) and end dates of promotional terms | Renewal plan with dates and owners |
| **6 months** | Run the full reconciliation (section 2) and the shelfware calculation (section 3); complete the License-Security Map; draft plan-mix options using the decision table; identify embedded and server licensing questions | Reconciled counts, options paper, open questions for the partner |
| **4–5 months** | Share options with finance and leadership; request quotes from more than one channel where appropriate; decide security priorities to fund from savings | Leadership decision on plan mix and reinvestment |
| **3 months** | Finalize quantities, term length and billing frequency; confirm reduction rights and cancellation windows in writing; for an Enterprise Agreement, prepare the true-up or update statement per the agreement timeline | Final order or true-up package |
| **Term end and +30 days** | Verify the invoice against the order; adjust assignments; record realized savings; schedule deployments funded by savings | Reconciled invoice, savings log, updated register |

**Agreement notes (verify against your agreement)**

- **Enterprise Agreement:** Microsoft describes it as designed for commercial organizations with at least 500 users or devices, with a three-year term. The annual true-up order is due between 60 and 30 days before the anniversary, and an update statement is submitted if nothing changed. Microsoft describes an Annual Order under the Subscription Enrollment through which counts can be increased or decreased. Don't assume reductions are available under other enrollment types.
- **CSP new commerce:** Monthly, annual and three-year terms are available for many subscriptions. Cancellation is allowed only in the first seven days of a term. Changes can be scheduled to take effect at the end of the term.
- **Microsoft Customer Agreement:** A billing account with billing profiles and invoice sections. Invoice sections can organize costs by department or project.

## 7. Security value already licensed: deployment checklist

Work through this list with the License-Security Map. For each item, record **licensed** (yes, no or verify), **deployed** (yes, partial or no) and **coverage** (users or devices covered ÷ total). Deploy in this order. The list follows the HHS Essential goals first.

**Identity (CPG-E Multifactor Authentication) — Entra ID P1, typically in E3, E5, F1, F3 and Business Premium**
- [ ] Conditional Access policy requiring MFA for all users is **On** (not Report-only).
- [ ] Administrators, vendors and remote access are included. Exclusions are documented, approved and dated.
- [ ] Legacy authentication is blocked.
- [ ] Break-glass accounts are excluded deliberately and monitored.
- [ ] Shared clinical workstations use session-based sign-in rather than unit-wide exclusions.

**Email (CPG-E Email Security) — Defender for Office 365 P1 typically in Business Premium; P2 typically in E5**
- [ ] Preset Standard or Strict protection, or equivalent anti-phishing, Safe Links and Safe Attachments policies, apply to all mailboxes, including shared referral, scheduling and billing mailboxes.
- [ ] SPF, DKIM and DMARC are configured for all domains, including unused ones.
- [ ] Attack simulation training is used where P2 is licensed.

**Endpoints (CPG-E Mitigate Known Vulnerabilities) — Defender for Endpoint P1 typically in E3, P2 typically in E5; Defender for Business typically in Business Premium**
- [ ] Every workstation is onboarded, including shared clinical workstations, and coverage is reconciled with the asset inventory.
- [ ] Servers are covered by separate server licensing. User plans typically don't cover servers.
- [ ] Devices that can't take agents are documented with compensating controls.

**Devices and configuration (CPG-X Configuration Management) — Intune Plan 1 typically in E3, E5 and Business Premium**
- [ ] Compliance policies exist for each platform.
- [ ] Device compliance is used in Conditional Access for PHI access.
- [ ] Security baselines are applied.

**Encryption and data protection (CPG-E Strong Encryption)**
- [ ] BitLocker is enabled on Windows Pro or Enterprise devices, with recovery keys escrowed in Entra ID or Active Directory.
- [ ] Purview Message Encryption is available to clinicians for external PHI. It's typically in E3, F3 and Business Premium.
- [ ] DLP policies for PHI are enforced (not simulation) on Exchange, SharePoint and OneDrive. This is typically in E3 and Business Premium.
- [ ] Where licensed (typically E5 or a Purview Suite), automatic labeling, Endpoint DLP and Teams DLP are planned.

**Logging (CPG-X Centralized Log Collection)**
- [ ] Purview Audit (Standard) is on and the retention period is known. Audit (Premium) is typically E5 or a Purview Suite add-on.
- [ ] If Microsoft Sentinel is used, the free data sources (Azure Activity, Office 365 audit logs, Defender security alerts) are connected first. Paid raw logs are added deliberately with a budget alert.

**Departing workforce (CPG-E Revoke Credentials) — no extra license needed**
- [ ] Disablement within one business day for all workforce types, with license removal per policy and a monthly HR reconciliation.

**Unsupported platforms**
- [ ] Every remaining Windows 10 device has a plan to upgrade, isolate, retire or enroll in Extended Security Updates. ESU is a paid program for version 22H2, for up to three years. It's typically included at no extra cost for Windows 10 VMs in Windows 365, Azure Virtual Desktop and Azure. Check current terms.

## 8. Cloud cost basics (FinOps)

The FinOps Framework organizes work into three phases: **Inform**, **Optimize** and **Operate**.

| Phase | What a small hospital does | Kit questions |
|---|---|---|
| Inform | Mandatory tags (owner, application, cost center, environment) enforced by Azure Policy; monthly cost by application; invoice sections or tags for affiliated entities | LO-17 |
| Optimize | Reservations for stable resources; savings plans for flexible compute; Azure Hybrid Benefit where Windows Server or SQL Server licenses with active Software Assurance or qualifying subscriptions exist; remove idle and rightsize oversized resources | LO-18, LO-19 |
| Operate | Budgets and alerts per subscription to owners and finance; monthly review; anomaly investigation; commitments aligned to the application roadmap | LO-20 |

**Commitment choices (verify current terms)**

| | Reservations | Savings plans |
|---|---|---|
| Commitment | Specific resource type, size and region (where applicable), 1 or 3 years | Fixed hourly spend, 1 or 3 years |
| Best for | Stable, predictable usage | Changing or dynamic workloads |
| Flexibility | Exchanges for the same type; limited self-service refunds | Cannot be canceled or refunded |
| Covers software? | No. VM reservations cover compute, not Windows or SQL licensing; use Azure Hybrid Benefit for licensing | Compute savings plan doesn't cover software, networking or storage |

**Healthcare cautions**
- Clinical systems may be sized to vendor specifications. Rightsize only with the vendor's agreement, and test during peak clinical hours.
- Disaster recovery and downtime environments look idle by design. Confirm their role before removing them.
- Don't commit for workloads the modernization roadmap plans to retire.

## 9. Quick wins for small hospitals

1. **Turn on what you own.** Move Conditional Access requiring MFA from Report-only to On. Apply preset email protection to every mailbox, including shared ones. Onboard all workstations to the licensed EDR. These steps typically need configuration time, not new licenses.
2. **Reharvest leavers.** Reconcile enabled, licensed accounts against the HR roster this week. Disable leavers and remove licenses per policy.
3. **Stop the next auto-renewal at the wrong quantity.** Put every term end and notice date in a calendar, and set a reminder at nine months.
4. **Check program eligibility.** In June 2024, Microsoft announced a cybersecurity program for rural hospitals. It described special pricing and time-limited security offers for eligible rural hospitals. Confirm with your licensing partner whether the program is still available, what it includes for your organization and when any promotional terms end.
5. **Clean up Azure leftovers.** Delete unattached disks and old snapshots, and set a budget alert on every subscription.
6. **Look before you buy.** Before purchasing any security tool, check the License-Security Map for an equivalent you already license.

## 10. Common mistakes

- **Using reseller counts as the entitlement record.** The reseller's report is one input, not your register.
- **Calculating "inactive" from one signal.** Mailbox activity alone misses clinicians who use only the EHR and Teams on shared devices. Combine sign-in data with app usage and HR status.
- **Reharvesting PRN and agency staff.** Removing access from a per-diem nurse who works next week creates a care-delivery problem and a help desk spike. Use the exception list.
- **Reporting projected savings.** Only invoice changes count. Savings on annual terms appear at renewal.
- **Downgrading by spreadsheet.** Moving clinicians to a frontline plan without checking desktop app, mailbox and device-management needs breaks workflows. Pilot with one unit.
- **Generic shared accounts to save licenses.** This violates unique-credential practices and undermines audit trails.
- **Licensing only some users of a tenant-wide protection.** Some services can't be limited to licensed users. Check the service description and license everyone who benefits.
- **Forgetting servers.** Windows Server and SQL Server under clinical systems, including disaster recovery copies, are where the compliance exposure is.
- **Buying commitments before deciding the application's future.** Savings plans can't be refunded.
- **Treating under-licensing findings as conclusions.** Confirm them with a licensing specialist before you act on them or disclose them.
- **Claiming compliance.** Deploying licensed controls supports HIPAA safeguards and HHS goals. It does not by itself establish HIPAA compliance.

## 11. Glossary

| Term | Meaning |
|---|---|
| Entitlement | The right to use software, established by an agreement, subscription or license |
| Effective license position (ELP) | Comparison of entitlements with deployment and usage, applying the vendor's licensing rules |
| Shelfware | Licenses paid for but unassigned or unused |
| Reharvesting | Removing a license from an inactive or departed user and reusing it |
| True-up | Under an Enterprise Agreement, the annual order reporting additional quantities deployed |
| Update statement | Under an Enterprise Agreement, the statement submitted when no true-up is needed |
| CSP | Cloud Solution Provider: buying through a Microsoft partner; new commerce terms apply |
| MCA | Microsoft Customer Agreement: billing account with billing profiles and invoice sections |
| Software Assurance (SA) | Benefits attached to some volume licenses; needed for some Azure Hybrid Benefit scenarios |
| Azure Hybrid Benefit | Applying eligible Windows Server or SQL Server licenses to reduce Azure costs |
| Reservation / savings plan | One- or three-year Azure commitment discounts (resource-specific vs hourly spend) |
| Shared computer activation | Microsoft 365 Apps activation mode for computers used by several licensed users |
| Device-only license | Intune license for devices without user affinity (kiosks, dedicated devices) |
| FinOps | Practice of managing cloud value through the Inform, Optimize and Operate phases |

## 12. References (official sources opened October 29, 2026)

**Identity and device management**
- Microsoft Entra licensing: https://learn.microsoft.com/en-us/entra/fundamentals/licensing
- Manage inactive user accounts: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-manage-inactive-user-accounts
- Intune licensing: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/licenses
- Intune in Business Premium: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-enrollment
- Microsoft 365 Business Premium (up to 300 users): https://learn.microsoft.com/en-us/microsoft-365/business-premium/

**Security and compliance service descriptions**
- Microsoft Defender service description: https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-defender-service-description
- Microsoft Purview service description: https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description
- Defender for Office 365 overview: https://learn.microsoft.com/en-us/defender-office-365/mdo-about
- Defender for Business overview: https://learn.microsoft.com/en-us/defender-business/mdb-overview
- Defender for Endpoint requirements: https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements
- BitLocker overview: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/
- Microsoft Sentinel billing: https://learn.microsoft.com/en-us/azure/sentinel/billing
- Windows 10 Extended Security Updates: https://learn.microsoft.com/en-us/windows/whats-new/extended-security-updates

**Microsoft 365 usage, frontline and shared devices**
- Microsoft 365 usage reports: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports
- Frontline worker licensing: https://learn.microsoft.com/en-us/microsoft-365/frontline/flw-licensing-options
- Shared computer activation: https://learn.microsoft.com/en-us/microsoft-365-apps/licensing-activation/overview-shared-computer-activation

**Agreements and purchasing**
- CSP new commerce: https://learn.microsoft.com/en-us/partner-center/customers/new-commerce-license-based
- Microsoft Customer Agreement billing account: https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/mca-overview
- Enterprise Agreement guidance: https://www.microsoft.com/licensing/guidance/Enterprise-Agreement

**Azure cost management**
- Azure Reservations: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations
- Azure savings plans: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview
- Azure Hybrid Benefit for Windows Server: https://learn.microsoft.com/en-us/azure/virtual-machines/windows/hybrid-use-benefit-licensing
- Azure resource tags: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources
- Cost Management budgets: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- Azure Advisor cost recommendations: https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations

**Frameworks and programs**
- FinOps Framework phases: https://www.finops.org/framework/phases/
- HHS Cybersecurity Performance Goals: https://hhscyber.hhs.gov/cybersecurity-performance-goals.html
- Microsoft Cybersecurity Program for Rural Hospitals (AHA-hosted flyer): https://www.aha.org/system/files/media/file/2024/12/microsoft-cybersecurity-program-for-rural-hospital-12-23-2024.pdf

ISO/IEC 19770-1 (IT asset management) is referenced by name; obtain it from ISO or your national standards body.
