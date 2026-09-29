# SOC 2 Type II Internal Audit Checklist (Security & Availability)

**Standard:** AICPA Trust Services Criteria (TSC) — Security (Common Criteria) & Availability  
**Audit Scope:** Production Cloud Environment, Identity Provider, Core SaaS Platform  
**Lead Auditor:** Vrunda Dalsaniya (Internal Audit / GRC)  
**Period Under Review:** April 1, 2026 – September 30, 2026 (6-Month Observation Window)  

---

## 1. Audit Testing Program Overview

This audit checklist simulates the testing procedures executed by an internal security compliance auditor preparing an organization for an external SOC 2 Type II examination.

Testing methods utilized:
- **Inquiry:** Interviewing control owners.
- **Inspection:** Examining policies, logs, tickets, and configurations.
- **Observation:** Watching live operational procedures in real time.
- **Reperformance:** Independently executing control verification procedures.

---

## 2. Common Criteria (CC Series) — Security

### CC6: Logical and Physical Access Controls

| Control ID | Trust Criteria | Control Objective | Testing Procedure | Evidence Required | Audit Result | Deficiencies / CAPA Ref |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **CC6.1.1** | CC6.1 | Logical access to production systems requires unique user credentials and MFA. | Sample 25 production users across Engineering, DevOps, and Support; verify MFA enforcement on IdP. | IdP export showing user status and MFA enrollment date. | **Pass** | None. 100% MFA compliance verified. |
| **CC6.2.1** | CC6.2 | Role-Based Access Control (RBAC) enforces principle of least privilege. | Review IAM policies for AWS and GitHub. Inspect whether wildcards (`*:*`) or unapproved admin roles exist. | AWS IAM policy JSON dump; GitHub organization membership list. | **Pass** | Least privilege enforced via AWS IAM Identity Center. |
| **CC6.3.1** | CC6.3 | New hires are provisioned access based on management-approved role profiles. | Sample 10 joiners from HRIS; trace access request tickets to manager approval and role assignments. | Jira Access Request tickets with manager approval timestamps. | **Pass** | All sampled joiners had documented manager approval. |
| **CC6.4.1** | CC6.4 | Terminated employees' access is revoked within defined SLAs (4 hours). | Sample 8 offboarded employees from HR report; compare termination timestamp with IdP deactivation timestamp. | HR termination report vs. Okta/Google Workspace log timestamps. | **Exception** | **CAPA-2026-001**: 2 of 8 accounts took >18 hours to deprovision due to manual handoff. |
| **CC6.6.1** | CC6.6 | Privileged user access is reviewed on a quarterly basis (UAR). | Inspect Q2 2026 User Access Review sign-off and ticket records across GitHub, AWS, and DB instances. | Completed UAR spreadsheet, signed review ticket from VP of Engineering. | **Pass** | Q2 UAR completed with all revocations actioned within 5 business days. |
| **CC6.7.1** | CC6.7 | Data transmission over public networks is encrypted using TLS 1.2 or higher. | Run automated SSL/TLS scan against all external API endpoints and web portals. | SSL Labs A+ report; Cloudflare TLS minimum version configuration. | **Pass** | All public endpoints enforce TLS 1.3 with TLS 1.2 fallback. TLS 1.0/1.1 disabled. |

---

### CC7: System Operations & Incident Management

| Control ID | Trust Criteria | Control Objective | Testing Procedure | Evidence Required | Audit Result | Deficiencies / CAPA Ref |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **CC7.1.1** | CC7.1 | Vulnerability scanning is performed monthly; critical flaws remediated per SLA. | Inspect Tenable/Qualys scan reports for May, June, July, August 2026; verify remediation tickets. | Monthly vulnerability scan exports; Jira security tickets. | **Exception** | **CAPA-2026-002**: 1 High CVE on internal bastion host exceeded 30-day remediation SLA. |
| **CC7.2.1** | CC7.2 | Security events and authentication anomalies are logged and alerted centrally. | Review SIEM (ELK Stack / Splunk) configuration; test automated alert generation on multiple failed logins. | Logstash grok rules; Kibana alert trigger log; incident notification Slack channel. | **Pass** | Brute force alert triggered within 45 seconds of simulation. |
| **CC7.3.1** | CC7.3 | Security incidents are managed following a documented Incident Response Plan (IRP). | Review post-mortem report and timeline for any severity-1 or severity-2 security incidents during the period. | Incident Post-Mortem Doc (INC-2026-04); Root Cause Analysis (RCA). | **Pass** | IRP followed, containment within 35 minutes, documented post-mortem executed. |

---

## 3. Availability Criteria (A Series)

### A1: Availability & Business Continuity

| Control ID | Trust Criteria | Control Objective | Testing Procedure | Evidence Required | Audit Result | Deficiencies / CAPA Ref |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **A1.1.1** | A1.1 | Data backups are performed daily, encrypted, and replicated offsite. | Inspect AWS backup schedules and CloudWatch logs for RDS databases and persistent storage for 30 consecutive days. | AWS Backup console snapshot logs; encryption key verification (KMS). | **Pass** | Automated daily snapshots confirmed; encrypted with customer-managed KMS key. |
| **A1.2.1** | A1.2 | Backup restoration and Disaster Recovery (DR) testing is executed at least annually. | Review annual DR table-top and live failover restoration test results; calculate achieved RTO and RPO. | DR Test Report 2026; database restoration log with measured RTO of 45 mins (SLA: 4 hrs). | **Pass** | DR restoration successfully verified in isolated staging VPC. |
| **A1.3.1** | A1.3 | System availability and performance are monitored with automated alerts for degradation. | Inspect Datadog/Grafana synthetic uptime checks and threshold alerts for production microservices. | Status page history; Uptime monitoring report showing 99.98% uptime. | **Pass** | Meets customer SLA commitment of 99.9% uptime. |

---

## 4. Internal Audit Conclusion & Next Steps

- **Total Controls Tested:** 10 Controls
- **Passed Controls:** 8 (80%)
- **Exceptions Identified:** 2 (20%)
  - *Exception 1 (CC6.4.1):* Offboarding deprovisioning latency.
  - *Exception 2 (CC7.1.1):* Vulnerability remediation SLA breach.
- **Action Plan:** Logged directly into the **CAPA Tracker (`CAPA_Tracker.csv`)** with assigned owners and mandatory remediation verification before the formal external SOC 2 Type II audit.
