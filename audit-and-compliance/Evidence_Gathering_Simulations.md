# SOC 2 Evidence Gathering Simulation & Audit Workpapers

**Lead Auditor:** Vrunda Dalsaniya  
**Engagement:** Internal Pre-Audit Assessment (SOC 2 Type II)  
**Target Systems:** AWS Cloud Infrastructure, Okta IdP, GitHub Enterprise, Jira Service Management  

---

## 1. Audit Evidence Collection Overview

In a SOC 2 Type II examination, auditors require concrete, time-stamped, tamper-evident artifacts demonstrating that security controls operated effectively throughout the entire audit window.

This document records the **Request for Information (RFI)**, the simulated evidence collected, the inspection methodology, and auditor observations.

---

## 2. Evidence Request & Workpapers

### Workpaper CC-6.1: Multi-Factor Authentication (MFA) Verification

* **Audit Request:** Provide proof that 100% of active users accessing corporate systems and production environments have MFA enforced.
* **Simulated Evidence Collected:**
  - Artifact: `IdP_MFA_Enrollment_Report_2026.csv`
  - Extraction Method: Okta System Log API / Reports Console
  - Extracted Query: `status eq "ACTIVE"`
* **Sample Data Extract:**
  ```csv
  User_ID,Email,Role,Status,MFA_Enrolled,MFA_Factor_Type,Last_Login_Timestamp
  USR-101,j.smith@company.com,DevOps Engineer,ACTIVE,TRUE,FIDO2 (WebAuthn),2026-09-28T09:14:22Z
  USR-102,a.davis@company.com,Software Engineer,ACTIVE,TRUE,TOTP Authenticator,2026-09-28T10:02:11Z
  USR-103,v.dalsaniya@company.com,GRC Analyst,ACTIVE,TRUE,FIDO2 (WebAuthn),2026-09-29T08:30:00Z
  USR-104,m.patel@company.com,Product Manager,ACTIVE,TRUE,TOTP Authenticator,2026-09-27T16:45:10Z
  ```
* **Auditor Verification Note:** Verified that no users were permitted bypass policies. SMS was deprecated in favor of TOTP and hardware security keys. **Control Effective.**

---

### Workpaper CC-6.4: Terminated User Deprovisioning SLA

* **Audit Request:** Provide a population of all employees separated between April 1 and September 30, 2026, alongside timestamped IdP suspension logs.
* **Simulated Evidence Collected:**
  - Artifact 1: BambooHR Terminations List (`HR_Terminations_Q2_Q3.csv`)
  - Artifact 2: Okta Deactivation Event Log (`Okta_Deactivation_Events.json`)
* **Comparative Reconciliation:**
  | Employee Name | Departure Date/Time (HR Record) | IdP Suspension Date/Time (Log) | Time Delta | SLA Status (Goal: < 4 hrs) |
  | :--- | :--- | :--- | :--- | :--- |
  | Employee A (ENG) | 2026-05-15 17:00 UTC | 2026-05-15 17:15 UTC | 15 mins | **Met** |
  | Employee B (MKT) | 2026-06-30 18:00 UTC | 2026-07-01 12:45 UTC | 18 hrs 45 mins | **Failed** (Logged as CAPA-2026-001) |
  | Employee C (FIN) | 2026-08-10 16:00 UTC | 2026-08-10 16:30 UTC | 30 mins | **Met** |
* **Auditor Verification Note:** Identified 1 instance of non-conformance where manual ticketing caused an SLA breach. Actioned in CAPA tracker with automated webhook remediation.

---

### Workpaper CC-7.2: Centralized Log Monitoring & Alert Verification

* **Audit Request:** Demonstrate that security events (specifically authentication failures / brute force attempts) trigger alerts to the on-call Security Operations team.
* **Simulated Evidence Collected:**
  - Artifact: Kibana Logstash parsing rule and alert webhook screenshot.
  - Test Case: Injected 10 consecutive failed SSH login attempts from IP `198.51.100.44`.
  - Alert Log:
    ```json
    {
      "timestamp": "2026-09-28T14:22:05Z",
      "alert_rule": "SOC-ALERT-AUTH-BRUTEFORCE",
      "severity": "HIGH",
      "source_ip": "198.51.100.44",
      "failed_attempts": 10,
      "time_window": "60s",
      "action_taken": "Automated IP block applied to AWS WAF / Security Group; Slack notification sent to #soc-alerts"
    }
    ```
* **Auditor Verification Note:** Verified that SIEM ingestion rules accurately captured, enriched, and triggered an incident alert within 45 seconds of generation. **Control Effective.**

---

### Workpaper A-1.2: Backup Restoration & Disaster Recovery Reperformance

* **Audit Request:** Provide objective evidence of the most recent database backup restoration test, including documented Recovery Time Objective (RTO) and Recovery Point Objective (RPO).
* **Simulated Evidence Collected:**
  - Artifact: AWS RDS Snapshot Restoration Execution Log (`dr-restore-prod-db-drill.log`)
  - Target RTO: < 4 Hours | **Actual Measured RTO:** 48 minutes
  - Target RPO: < 1 Hour | **Actual Measured RPO:** 12 minutes (Point-in-Time Recovery)
* **Auditor Verification Note:** Observed live restore of encrypted database snapshot to an isolated staging VPC. Verified data integrity and cryptographic checksums matches between source and restored database. **Control Effective.**
