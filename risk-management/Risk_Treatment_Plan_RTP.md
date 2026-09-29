# Information Security Risk Treatment Plan (RTP)

**Document Reference:** ISMS-RTP-2026-V1  
**Standard Compliance:** ISO/IEC 27001:2022 (Clause 6.1.3 & 8.3)  
**Author:** Vrunda Dalsaniya (Information Security & GRC)  
**Approved By:** Chief Information Security Officer (CISO)  
**Effective Date:** October 2026  
**Review Cycle:** Semi-Annual  

---

## 1. Executive Summary

This **Risk Treatment Plan (RTP)** documents the formal actions, responsibilities, resource allocations, and timelines established to treat identified information security risks exceeding the organization's risk tolerance threshold (Risk Score > 8). 

The treatment strategies align with the ISO/IEC 27001:2022 Annex A control set and the Organization's Risk Assessment Methodology.

---

## 2. Risk Treatment Decision Matrix

For every risk identified in the Risk Register, the ISMS Steering Committee evaluates treatment options using the **4 Ts Framework**:

1. **Treat:** Implement technical, administrative, or operational controls to lower likelihood or consequence.
2. **Transfer:** Shift financial liability via cyber liability insurance policies or contractual indemnities with suppliers.
3. **Tolerate:** Formally accept residual risk when remediation cost is disproportionate to potential loss and within risk appetite.
4. **Terminate:** Discontinue business processes or systems generating unacceptable risk exposure.

---

## 3. High-Priority Risk Treatment Action Plans

### Action Plan RTP-01: Endpoint Security & Anti-Ransomware Defense
* **Linked Risk:** `RSK-001` (Ransomware deployment encrypting corporate databases)
* **Initial Risk Score:** 20 (Critical) $\rightarrow$ **Target Residual Score:** 6 (Medium)
* **Treatment Strategy:** Treat (Technical Control Implementation)
* **Applicable ISO 27001 Controls:** 
  - `A.8.7` Protection against malware
  - `A.8.19` Installation of software on operational systems
  - `A.8.13` Information backup
* **Action Items:**
  1. Mandate rollout of Trend Micro / EDR agent to 100% of corporate endpoints and cloud workloads.
  2. Implement daily immutable AWS S3 Glacier / backup snapshots with air-gapped credentials.
  3. Enforce local administrator account disablement on all standard employee workstations.
* **Owner:** Security Operations Lead
* **Budget Allocated:** \$18,000 / year
* **Target Delivery Date:** November 15, 2026

---

### Action Plan RTP-02: Identity Governance & MFA Enforcement
* **Linked Risk:** `RSK-002` (Unauthorized access via credential stuffing / missing MFA)
* **Initial Risk Score:** 20 (Critical) $\rightarrow$ **Target Residual Score:** 6 (Medium)
* **Treatment Strategy:** Treat (Identity & Access Control)
* **Applicable ISO 27001 Controls:**
  - `A.5.15` Access control
  - `A.8.5` Secure authentication
* **Action Items:**
  1. Transition all SaaS enterprise applications to Okta / Entra ID Single Sign-On (SSO).
  2. Enforce phishing-resistant MFA (FIDO2 WebAuthn / TOTP authenticator) for all users; block SMS-based verification.
  3. Disable legacy basic authentication (IMAP, POP3, unauthenticated SMTP) at tenant level.
* **Owner:** IAM Specialist
* **Target Delivery Date:** Completed (October 2026)

---

### Action Plan RTP-03: Joiner-Mover-Leaver (JML) Deprovisioning Automation
* **Linked Risk:** `RSK-003` (Ex-employee retaining access; orphaned accounts)
* **Initial Risk Score:** 16 (High) $\rightarrow$ **Target Residual Score:** 4 (Low)
* **Treatment Strategy:** Treat (Process Automation & Operational Control)
* **Applicable ISO 27001 Controls:**
  - `A.6.5` Responsibilities after termination or change of employment
  - `A.5.18` Access rights
* **Action Items:**
  1. Deploy automated SCIM synchronization connecting BambooHR / Workday to Identity Provider.
  2. Implement strict SLA: Deactivate credentials within 4 hours of HR termination ticket; complete archive and license revocation within 24 hours.
  3. Formalize quarterly User Access Reviews (UAR) with automated anomaly detection scripts.
* **Owner:** IT Operations & HR Compliance
* **Target Delivery Date:** November 30, 2026

---

### Action Plan RTP-04: Third-Party & Supply Chain Risk Management (TPRM)
* **Linked Risk:** `RSK-005` (Data compromise at Tier-1 SaaS vendor)
* **Initial Risk Score:** 16 (High) $\rightarrow$ **Target Residual Score:** 6 (Medium)
* **Treatment Strategy:** Transfer & Treat
* **Applicable ISO 27001 Controls:**
  - `A.5.19` Information security in supplier relationships
  - `A.5.21` Managing ICT supply chain security
* **Action Items:**
  1. Require all Tier-1 vendors processing confidential customer data to submit annual SOC 2 Type II or ISO 27001 certificates.
  2. Execute Data Processing Addenda (DPAs) incorporating standard contractual clauses and mandatory breach notification SLAs (within 48 hours).
  3. Procure \$5M comprehensive cyber liability coverage covering supply-chain ransomware and third-party liabilities.
* **Owner:** GRC Analyst
* **Target Delivery Date:** December 15, 2026

---

### Action Plan RTP-05: AI Governance & Data Loss Prevention
* **Linked Risk:** `RSK-009` (Shadow AI leaking source code / confidential data to LLMs)
* **Initial Risk Score:** 16 (High) $\rightarrow$ **Target Residual Score:** 4 (Low)
* **Treatment Strategy:** Treat (Policy & Technical Controls)
* **Applicable Controls:** ISO/IEC 42001:2023 A.6.2, ISO/IEC 27001:2022 A.8.12
* **Action Items:**
  1. Enact corporate **AI Acceptable Use Policy** explicitly prohibiting the input of source code, customer records, and financial projections into public consumer AI models.
  2. Configure Secure Web Gateway (SWG) and DNS filtering to block unvetted AI generation platforms.
  3. Provision enterprise private AI instances with zero-data-retention agreements.
* **Owner:** AI Governance & Information Security Lead
* **Target Delivery Date:** October 31, 2026

---

## 4. Monitoring, Verification & Audit Sign-Off

The status of all treatments will be monitored by the GRC Analyst on a bi-weekly basis. Residual risk acceptance must be formally signed off by the ISMS Committee.

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **GRC Lead / Auditor** | Vrunda Dalsaniya | *Vrunda Dalsaniya* | 2026-10-01 |
| **Chief Information Security Officer** | Security Leadership | *CISO Approved* | 2026-10-02 |
