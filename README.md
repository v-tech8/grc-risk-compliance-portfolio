# 🛡️ Governance, Risk & Compliance (GRC) & ISMS Implementation Portfolio

[![Framework: ISO/IEC 27001:2022](https://img.shields.io/badge/Framework-ISO%2FIEC%2027001%3A2022-blue.svg)](https://www.iso.org/standard/27001)
[![Standard: SOC 2 Type II](https://img.shields.io/badge/Standard-SOC%202%20(Security%20%26%20Availability)-orange.svg)](https://www.aicpa.org/)
[![AI Governance: ISO/IEC 42001](https://img.shields.io/badge/Standard-ISO%2FIEC%2042001%3A2023-purple.svg)](https://www.iso.org/standard/42001)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Author:** Vrunda Dalsaniya  
> **Role:** Information Security, GRC & IT Risk Analyst  
> **Certifications:** ISO/IEC 27001:2022 Lead Auditor | ISO/IEC 42001:2023 (AIMS) Lead Auditor  

---

## 📌 Executive Summary

This repository contains a comprehensive, enterprise-aligned **Governance, Risk, and Compliance (GRC) and Information Security Management System (ISMS)** implementation portfolio. Designed from the perspective of an internal auditor and GRC analyst, this project demonstrates end-to-end operationalization of security governance frameworks across the complete compliance lifecycle:

1. **Enterprise Risk Management:** Qualitative 5×5 risk assessment, inherent vs. residual scoring, ISO 27001:2022 Annex A control mapping, and formal Risk Treatment Planning (RTP).
2. **SOC 2 Compliance & Internal Audit:** Trust Services Criteria (TSC) audit checklist (Security & Availability), mock evidence collection, and Corrective/Preventive Action (CAPA) tracking.
3. **Identity & Access Management (IAM) Governance:** Joiner-Mover-Leaver (JML) workflow modeling, quarterly User Access Review (UAR) simulation, and Python-based anomaly detection for privilege creep.
4. **ISMS Policy Framework:** Core security policies including Information Security Policy, Access Control Policy, and cutting-edge **ISO/IEC 42001 AI Acceptable Use & Governance Policy**.

---

## 🗂️ Repository Structure

```
├── risk-management/
│   ├── ISO27001_Risk_Register.csv        # Detailed risk register with 5x5 matrix & Annex A mappings
│   ├── Risk_Assessment_Methodology.md    # Scoring criteria (Likelihood x Impact) and acceptance thresholds
│   └── Risk_Treatment_Plan_RTP.md        # Formal ISMS Risk Treatment Plan (Treat, Transfer, Tolerate, Terminate)
│
├── audit-and-compliance/
│   ├── SOC2_Internal_Audit_Checklist.md  # SOC 2 TSC (Common Criteria & Availability) audit testing program
│   ├── CAPA_Tracker.csv                  # Corrective and Preventive Action tracking register with root cause
│   └── Evidence_Gathering_Simulations.md # Simulated audit requests, evidence artifacts, and inspection logs
│
├── identity-and-access-management/
│   ├── JML_Workflow_Procedures.md        # Joiner-Mover-Leaver lifecycle SOPs & visual flowchart
│   ├── Quarterly_UAR_Simulation.csv      # User access review dataset with flagged dormant/excessive privileges
│   └── uar_anomaly_checker.py            # Python script detecting SOD conflicts and orphaned accounts
│
├── policies/
│   ├── Information_Security_Policy.md    # Foundational ISMS charter (ISO 27001 Clause 5.2 compliant)
│   ├── Access_Control_Policy.md          # Granular IAM policy (RBAC, MFA, password complexity, PAM)
│   └── AI_Acceptable_Use_Policy.md       # AI risk management & governance policy (ISO 42001 aligned)
│
└── README.md
```

---

## 🔍 Key Project Highlights & Methodologies

### 1. Risk Assessment & Treatment (ISO/IEC 27001:2022)
- Applied a standard **5×5 Likelihood vs. Impact** qualitative scoring methodology:
  $$\text{Risk Score} = \text{Likelihood} \times \text{Impact}$$
- Mapped identified threats to updated **ISO 27001:2022 Annex A control themes**:
  - *Organizational Controls (Clause 5)*
  - *People Controls (Clause 6)*
  - *Physical Controls (Clause 7)*
  - *Technological Controls (Clause 8)*
- Developed a concrete **Risk Treatment Plan (RTP)** evaluating Treatment Strategy (Mitigate / Accept / Avoid / Transfer), Residual Risk calculation, Resource Allocation, and Owner Accountability.

### 2. SOC 2 Type II Audit & CAPA Management
- Structured an internal audit testing checklist covering key **Trust Services Criteria (TSC)**:
  - **CC6.1 - CC6.8**: Logical and Physical Access Controls (MFA, RBAC, Deprovisioning)
  - **CC7.1 - CC7.4**: System Operations & Threat Monitoring (Vulnerability scanning, Incident Response)
  - **A1.1 - A1.3**: Availability (Disaster recovery, backup testing, capacity management)
- Engineered a **CAPA (Corrective and Preventive Action) Tracker** applying the "5 Whys" root-cause methodology to close audit findings before external certification assessments.

### 3. IAM & User Access Review (UAR) Automation
- Modelled a zero-trust **Joiner-Mover-Leaver (JML)** workflow ensuring:
  - Day 1 onboarding based on least privilege and Role-Based Access Control (RBAC).
  - Immediate role transitions with revocation of legacy permissions (preventing privilege creep).
  - SLA-bound offboarding: Automated account suspension within 4 hours, complete deprovisioning within 24 hours.
- Built a Python-based **UAR Anomaly Checker** (`uar_anomaly_checker.py`) that analyzes quarterly access logs to detect:
  - Terminated employees with active credentials (orphaned accounts).
  - Users with unapproved high-privilege administrative rights.
  - Inactive accounts (>90 days dormancy).

### 4. AI Governance Integration (ISO/IEC 42001:2023)
- Reflecting modern regulatory landscapes (EU AI Act, ISO 42001), established an **AI Acceptable Use Policy** governing:
  - Prohibitions on entering sensitive PII or proprietary source code into public LLMs.
  - Mandatory human-in-the-loop validation for algorithmic decision systems.
  - Model risk tiers and third-party AI vendor risk assessment.

---

## 🚀 How to Review & Utilize This Repository

1. **Audit Checklists & Risk Registers:**
   - Open `risk-management/ISO27001_Risk_Register.csv` and `audit-and-compliance/CAPA_Tracker.csv` in Excel, Google Sheets, or GitHub table viewer.
2. **Policy Review:**
   - Explore the `policies/` directory for ready-to-adopt ISMS documents drafted to pass Stage 1 and Stage 2 certification audits.
3. **Run the UAR Script:**
   ```bash
   cd identity-and-access-management
   python3 uar_anomaly_checker.py
   ```

---

## 🎯 Target Industry Roles
- **GRC Analyst / IT Compliance Analyst**
- **Information Security Auditor (ISO 27001 / SOC 2)**
- **Cybersecurity Governance & Risk Consultant**
- **IAM / Security Operations Support**
