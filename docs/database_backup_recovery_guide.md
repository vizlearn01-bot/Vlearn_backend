# VLearn PostgreSQL Database Backup & Disaster Recovery Guide

## Table of Contents
1. [Executive Summary & Scope](#1-executive-summary--scope)
2. [Recovery Objectives (RPO & RTO)](#2-recovery-objectives-rpo--rto)
3. [Backup Strategies & Formats](#3-backup-strategies--formats)
   - [3.1 Custom-Format Snapshots (`pg_dump -Fc`)](#31-custom-format-snapshots-pg_dump--fc)
   - [3.2 Compressed Plain-Text Dumps (`pg_dump | gzip`)](#32-compressed-plain-text-dumps-pg_dump--gzip)
   - [3.3 WAL Archiving & Point-In-Time Recovery (PITR)](#33-wal-archiving--point-in-time-recovery-pitr)
4. [Automated Backup Scheduling & Retention Policy](#4-automated-backup-scheduling--retention-policy)
   - [4.1 Backup Schedule Matrix](#41-backup-schedule-matrix)
   - [4.2 Retention Policy Enforcement](#42-retention-policy-enforcement)
5. [Restoration Procedures](#5-restoration-procedures)
   - [5.1 Restoring Custom-Format Snapshots (`pg_restore`)](#51-restoring-custom-format-snapshots-pg_restore)
   - [5.2 Restoring Compressed SQL Dumps (`psql`)](#52-restoring-compressed-sql-dumps-psql)
   - [5.3 Staging Restoration & Validation Workflow](#53-staging-restoration--validation-workflow)
6. [Backup Integrity Verification](#6-backup-integrity-verification)
   - [6.1 Table of Contents Inspection (`pg_restore --list`)](#61-table-of-contents-inspection-pg_restore---list)
   - [6.2 Automated Staging Restore Audits](#62-automated-staging-restore-audits)
7. [Comprehensive Verification & Command Reference](#7-comprehensive-verification--command-reference)

---

## 1. Executive Summary & Scope

This guide establishes the official, provider-agnostic Disaster Recovery (DR) and Database Backup strategy for PostgreSQL instances supporting the VLearn platform.

The procedures outlined herein apply across cloud providers (AWS RDS / EC2, GCP Cloud SQL / Compute Engine, Azure Flexible Server), containerized orchestrations (Docker / Kubernetes), and bare-metal infrastructure. The goal is to ensure high availability, data loss minimization, and rapid operational recovery in the event of hardware failures, data corruption, security breaches, or human error.

---

## 2. Recovery Objectives (RPO & RTO)

VLearn's business continuity metrics strictly define target boundaries for data loss and system downtime:

| Metric | Target Boundary | Description |
| :--- | :--- | :--- |
| **Recovery Point Objective (RPO)** | **< 1 Hour** | Maximum allowable window of data loss measured in time. Supported via continuous Write-Ahead Log (WAL) archiving combined with hourly incremental/WAL syncs and daily full snapshots. |
| **Recovery Time Objective (RTO)** | **< 2 Hours** | Maximum allowable duration from incident declaration to restored operational database readiness in production or failover environment. |

---

## 3. Backup Strategies & Formats

VLearn standardizes on two primary logical backup formats and continuous physical log archiving to balance speed, flexbility, and granularity.

### 3.1 Custom-Format Snapshots (`pg_dump -Fc`)
- **Format**: PostgreSQL custom archive format (`.dump` / `.dump.custom`).
- **Use Case**: Primary daily production snapshots.
- **Advantages**:
  - Compressed by default.
  - Supports parallel restoration (`pg_restore -j <N>`).
  - Enables selective table/schema restoration without manual SQL editing.
  - Embedded Table of Contents (TOC) enables instant archive validation without uncompressing.

### 3.2 Compressed Plain-Text Dumps (`pg_dump | gzip`)
- **Format**: Gzipped plain SQL script (`.sql.gz`).
- **Use Case**: Human-readable audits, migration across major PostgreSQL engine versions, emergency inspectable dumps.
- **Advantages**:
  - Standard SQL commands (`CREATE TABLE`, `INSERT`/`COPY`).
  - Portability across version boundaries and lightweight text inspection (`zcat`, `zgrep`).

### 3.3 WAL Archiving & Point-In-Time Recovery (PITR)
- **Mechanism**: Continuous archiving of 16MB WAL segment files using tools such as `pg_receivewal`, `pgBackRest`, `wal-g`, or cloud-native WAL archival.
- **Use Case**: Granular rollbacks to any specific second prior to a data corruption incident.

---

## 4. Automated Backup Scheduling & Retention Policy

### 4.1 Backup Schedule Matrix

| Task Type | Frequency | Execution Window | Storage Target |
| :--- | :--- | :--- | :--- |
| **WAL Archiving** | Continuous / Hourly Sync | Real-time / Hourly | Remote Immutable Storage (S3/GCS/MinIO) |
| **Full Snapshot (`-Fc`)** | Daily | 01:00 UTC | Primary Backup Bucket + Geo-Redundant Vault |
| **Plain SQL Dump (`gzip`)**| Weekly | Sunday 02:00 UTC | Cold Storage Vault |
| **Staging Restore Test** | Weekly | Monday 04:00 UTC | Isolated Staging / DR Cluster |

### 4.2 Retention Policy Enforcement
- **Retention Period**: **30 Days** standard retention for daily custom-format snapshots and WAL archives.
- **Policy Automation**: Automated lifecycle rules (e.g., S3 Lifecycle / GCS Object Lifecycle) or cron-based prune scripts clean up backups exceeding 30 days.

---

## 5. Restoration Procedures

### 5.1 Restoring Custom-Format Snapshots (`pg_restore`)
To restore a custom-format dump (`.dump`) into a targeted database:

```bash
# 1. Terminate active user connections (if restoring existing DB)
psql -h $DB_HOST -U $DB_USER -d postgres -c "
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE datname = '$DB_NAME' AND pid <> pg_backend_pid();"

# 2. Recreate target database
psql -h $DB_HOST -U $DB_USER -d postgres -c "DROP DATABASE IF EXISTS $DB_NAME;"
psql -h $DB_HOST -U $DB_USER -d postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"

# 3. Perform parallel restore via pg_restore
pg_restore -h $DB_HOST -U $DB_USER -d $DB_NAME --clean --if-exists --no-owner --role=$DB_USER -j 4 /backups/vlearn_prod_$(date +%Y%m%d).dump
```

### 5.2 Restoring Compressed SQL Dumps (`psql`)
To restore a `.sql.gz` plain-text backup:

```bash
gunzip -c /backups/vlearn_prod_$(date +%Y%m%d).sql.gz | psql -h $DB_HOST -U $DB_USER -d $DB_NAME
```

### 5.3 Staging Restoration & Validation Workflow
1. Provision isolated staging database container or instance.
2. Fetch the latest snapshot from backup storage.
3. Execute `pg_restore`.
4. Run standard application validation suites and check data row counts across key tables (`users`, `courses`, `enrollments`).

---

## 6. Backup Integrity Verification

Never rely on unverified backup files. Regular automated verification guarantees recoverability.

### 6.1 Table of Contents Inspection (`pg_restore --list`)
Before attempting a full restore, inspect the snapshot TOC to verify archive structure and detect corruption:

```bash
pg_restore --list /backups/vlearn_prod_latest.dump | head -n 30
```

### 6.2 Automated Staging Restore Audits
Every week, an automated workflow performs the following health checks:
1. Downloads the latest daily snapshot.
2. Restores into a disposable PostgreSQL container.
3. Verifies schema integrity and row non-zeroness:
   ```sql
   SELECT count(*) FROM users;
   SELECT count(*) FROM django_migrations;
   ```
4. Emits success telemetry or alerts on failure.

---

## 7. Comprehensive Verification & Command Reference

### Create Custom-Format Snapshot
```bash
pg_dump -h localhost -U vlearn_user -d vlearn_db -Fc -f /backups/vlearn_$(date +%Y%m%d_%H%M%S).dump
```

### Create Compressed Plain SQL Backup
```bash
pg_dump -h localhost -U vlearn_user -d vlearn_db | gzip -9 > /backups/vlearn_$(date +%Y%m%d_%H%M%S).sql.gz
```

### Inspect Snapshot Table of Contents (TOC)
```bash
pg_restore --list /backups/vlearn_latest.dump
```

### Restore Snapshot into Database (Parallel Threads)
```bash
pg_restore -h localhost -U vlearn_user -d vlearn_db -j 4 --clean --if-exists /backups/vlearn_latest.dump
```

### Verify Backup Integrity via SHA-256 Checksum
```bash
# Generate checksum at creation
sha256sum /backups/vlearn_latest.dump > /backups/vlearn_latest.dump.sha256

# Verify checksum before restore
sha256sum -c /backups/vlearn_latest.dump.sha256
```
