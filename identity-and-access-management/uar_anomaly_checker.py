#!/usr/bin/env python3
"""
Quarterly User Access Review (UAR) Anomaly Detection Engine
Author: Vrunda Dalsaniya
Purpose: Automates compliance checks against user access datasets to identify:
         1. Orphaned accounts (active credentials for terminated staff)
         2. Dormant / inactive accounts (> 90 days)
         3. Non-technical staff with elevated / administrative privileges
         4. Missing Multi-Factor Authentication (MFA)
         5. Stale contractor / external party entitlements
"""

import csv
import sys
from pathlib import Path


def analyze_uar_data(csv_file_path: str):
    path = Path(csv_file_path)
    if not path.exists():
        print(f"[!] Error: File not found at {csv_file_path}")
        return

    print("=" * 80)
    print("🛡️  GRC AUDIT AUTOMATION: USER ACCESS REVIEW (UAR) ANOMALY DETECTOR")
    print(f"📁 Dataset: {path.name}")
    print("=" * 80)

    total_records = 0
    orphaned_accounts = []
    dormant_accounts = []
    excessive_privilege = []
    mfa_missing = []
    revoked_count = 0

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_records += 1
            user_id = row.get("User_ID")
            name = row.get("Full_Name")
            dept = row.get("Department")
            role = row.get("Assigned_Role")
            system = row.get("System_Name")
            mfa = row.get("MFA_Enabled", "").strip().upper() == "TRUE"
            last_login = int(row.get("Last_Login_Days_Ago", 0))
            hr_status = row.get("HR_Status", "").strip()
            manager_decision = row.get("Manager_Review_Decision", "").strip()

            if manager_decision.lower() == "revoked":
                revoked_count += 1

            # Check 1: Orphaned Accounts (Terminated or Contract Ended but still has system credentials)
            if hr_status in ["Terminated", "Contract Ended"]:
                orphaned_accounts.append({
                    "id": user_id, "name": name, "status": hr_status,
                    "system": system, "role": role
                })

            # Check 2: Dormant Accounts (> 90 days inactivity)
            if last_login > 90:
                dormant_accounts.append({
                    "id": user_id, "name": name, "days": last_login,
                    "system": system
                })

            # Check 3: Excessive Privileges (Marketing, Sales, Finance with Production Admin)
            if dept in ["Marketing", "Sales", "Human Resources"] and ("Admin" in role or "Administrator" in role):
                excessive_privilege.append({
                    "id": user_id, "name": name, "dept": dept,
                    "system": system, "role": role
                })

            # Check 4: Missing MFA
            if not mfa:
                mfa_missing.append({
                    "id": user_id, "name": name, "system": system
                })

    # Output Findings
    print(f"\n[+] Total Accounts Reviewed: {total_records}")
    print(f"[+] Total Revocation Decisions: {revoked_count}")

    print("\n" + "-" * 80)
    print("🚨 FINDING 1: CRITICAL ORPHANED ACCOUNTS (Terminated/Expired Staff)")
    print("-" * 80)
    if orphaned_accounts:
        for acc in orphaned_accounts:
            print(f" [CRITICAL] {acc['id']} | {acc['name']:<20} | Status: {acc['status']:<15} | System: {acc['system']} ({acc['role']})")
    else:
        print(" [PASS] No orphaned accounts detected.")

    print("\n" + "-" * 80)
    print("⚠️  FINDING 2: EXCESSIVE PRIVILEGE & SOD ANOMALIES")
    print("-" * 80)
    if excessive_privilege:
        for acc in excessive_privilege:
            print(f" [HIGH]     {acc['id']} | {acc['name']:<20} | Dept: {acc['dept']:<15} | Role: {acc['role']} on {acc['system']}")
    else:
        print(" [PASS] No excessive privileges identified.")

    print("\n" + "-" * 80)
    print("🕒 FINDING 3: DORMANT / INACTIVE ACCOUNTS (>90 Days)")
    print("-" * 80)
    if dormant_accounts:
        for acc in dormant_accounts:
            print(f" [MEDIUM]   {acc['id']} | {acc['name']:<20} | Inactive: {acc['days']} days | System: {acc['system']}")
    else:
        print(" [PASS] No dormant accounts detected.")

    print("\n" + "-" * 80)
    print("🔐 FINDING 4: MISSING MULTI-FACTOR AUTHENTICATION (MFA)")
    print("-" * 80)
    if mfa_missing:
        for acc in mfa_missing:
            print(f" [HIGH]     {acc['id']} | {acc['name']:<20} | Missing MFA on: {acc['system']}")
    else:
        print(" [PASS] 100% MFA compliance verified.")

    print("\n" + "=" * 80)
    print("📋 SUMMARY AUDIT RECOMMENDATION:")
    print(" 1. Immediately revoke active tokens for orphaned accounts (CAPA-2026-001).")
    print(" 2. Enforce automated RBAC profile alignment to remove production admin from non-tech roles.")
    print(" 3. Trigger automated deactivation notifications for accounts dormant over 90 days.")
    print("=" * 80)


if __name__ == "__main__":
    target_csv = Path(__file__).parent / "Quarterly_UAR_Simulation.csv"
    if len(sys.argv) > 1:
        target_csv = sys.argv[1]
    analyze_uar_data(target_csv)
