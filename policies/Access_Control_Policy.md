# Enterprise Access Control Policy

**Policy Reference:** POL-ISMS-004  
**ISO/IEC 27001:2022 Control Reference:** A.5.15, A.5.16, A.5.17, A.5.18, A.8.5  
**SOC 2 Trust Services Criteria:** CC6.1, CC6.2, CC6.3  
**Effective Date:** October 2026  
**Version:** 1.0  
**Author:** Vrunda Dalsaniya (Information Security & GRC)  
**Classification:** Public / Enterprise Standard  

---

## 1. Purpose & Scope

The purpose of this Access Control Policy is to establish mandatory requirements for granting, modifying, reviewing, and revoking logical access to the organization's information assets, cloud environments, networks, operating systems, and applications. 

This policy applies to all full-time employees, contractors, third-party partners, and automated system service accounts accessing corporate information processing facilities.

---

## 2. Core Access Principles

1. **Least Privilege (PoLP):** Users are granted only the minimum level of access required to execute their specific organizational duties.
2. **Need-to-Know:** Access to sensitive data is restricted to individuals with an explicit business justification.
3. **Default Deny:** All access permissions not explicitly permitted by written policy or role profile are prohibited by default.
4. **Segregation of Duties (SoD):** High-risk workflows (e.g., initiating vs. approving financial transactions; writing code vs. deploying to production) must require independent actors.

---

## 3. Policy Statements

### 3.1 User Access Management & Provisioning
- Access requests must originate through an authorized ticketing system (Jira Service Management) accompanied by formal manager approval.
- Access rights must be provisioned via standardized Role-Based Access Control (RBAC) profiles. Custom one-off permissions require CISO or GRC justification.
- Access to production environments is strictly restricted to authorized DevOps / SRE personnel and must utilize temporary Just-in-Time (JIT) access tokens with automated expiration (<8 hours).

### 3.2 Authentication & Password Standards
- **Multi-Factor Authentication (MFA):** MFA is mandatory for all corporate accounts, VPNs, SaaS platforms, and cloud infrastructure. Acceptable factors include FIDO2 hardware keys (YubiKey) or time-based one-time password (TOTP) authenticator applications. SMS-based verification is disallowed.
- **Password Complexity:**
  - Minimum length: 14 characters.
  - Must include uppercase, lowercase, numbers, and special symbols.
  - Automatically checked against known compromised credential lists (HaveIBeenPwned API).
- **Session Timeouts:** Inactive workstation screens must lock automatically after 10 minutes of inactivity. Idle web portal sessions must terminate after 30 minutes.

### 3.3 Privileged Access Management (PAM)
- Direct root/admin login to servers and databases is prohibited; engineers must authenticate with named individual accounts and elevate privileges through auditable tooling (e.g., `sudo`, Teleport, AWS IAM Identity Center).
- Administrative activities must generate immutable, real-time audit logs forwarded to the centralized SIEM.
- Shared administrative credentials ("generic accounts") are strictly prohibited.

### 3.4 User Access Reviews (UAR)
- Formal User Access Reviews must be conducted **quarterly** by designated department leaders and the GRC team.
- Accounts inactive for >90 days will be automatically disabled pending re-verification.
- Any unauthorized access detected during UAR must be revoked within 24 hours and logged in the CAPA register.

### 3.5 Deprovisioning & Offboarding (Leavers)
- HR must notify IT Operations at least 24 hours prior to scheduled voluntary terminations, or immediately upon involuntary termination.
- Upon notification, all account credentials, OAuth tokens, and network access must be suspended within a maximum SLA of **4 hours** (instantaneous for involuntary departures).
- Company-issued hardware must be surrendered, remotely locked, and wiped in accordance with the Asset Disposal Policy.

---

## 4. Compliance & Enforcement

Violations of this policy may lead to disciplinary action up to and including termination of employment, revocation of access privileges, and potential civil or criminal legal proceedings.

---

## 5. Review & Revision History

| Version | Date | Author | Description of Change |
| :---: | :---: | :--- | :--- |
| **1.0** | 2026-10-01 | Vrunda Dalsaniya | Initial draft aligned with ISO 27001:2022 and SOC 2 Type II controls. |
