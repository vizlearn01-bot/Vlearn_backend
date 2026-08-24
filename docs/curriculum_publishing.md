# VLearn Curriculum Publishing Guide

## Overview

In the VLearn architecture:
- **Local PostgreSQL** is the curriculum authoring, review, and approval environment.
- **Supabase PostgreSQL** is the production runtime database serving live web users, payments, subscriptions, and school operations.
- **Publishing** is the controlled, one-way promotion of approved curriculum content from local development to production.

This is **not** a general database mirror or synchronization tool. The publishing engine is strictly additive and update-oriented, ensuring that operational data (users, payments, subscriptions, student progress, schools) is never modified or overwritten.

---

## Architecture Principles

1. **One-Way Promotion**: Content only flows from `local → production`.
2. **Operational Data Protection**: Over 40 operational models (`User`, `Subscription`, `Invoice`, `School`, `StudentEnrollment`, `LearningSession`, `RuntimeNodeProgress`, etc.) are permanently excluded.
3. **Additive by Default**: Production records are never deleted simply because they don't exist locally. Production-only records are reported as preserved.
4. **Stable Content Identity**: Models use permanent `content_uuid` (UUID4) and natural keys (`Curriculum.name`, `Grade(curriculum, name)`, `Subject(grade, name)`, `Simulation.key`). Integer database PKs are database-local implementation details.
5. **Content Hashing**: SHA-256 content hashes detect field-level changes accurately, ignoring timestamps and database IDs.
6. **Dependency Closure**: Specifying a scope (e.g. `--subject Mathematics`) automatically resolves and includes all related topics, learning units, concepts, objectives, lessons, lesson blocks, and assets.
7. **Three-Stage Workflow**: `--validate` → `--dry-run` → `--apply`.
8. **Idempotency**: Running `--apply` repeatedly with no source changes results in 0 creates and 0 updates.

---

## Prerequisites & Configuration

Add your production database URL to your local `.env` file:

```env
# ------------------------------------------------------------------------------
# Curriculum Publishing (local authoring → production promotion)
# ------------------------------------------------------------------------------
PUBLISH_DATABASE_URL=postgresql://postgres.xxx:password@aws-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=require
```

> [!WARNING]
> Never commit `PUBLISH_DATABASE_URL` with real credentials to version control. Keep it in your local `.env` only.

---

## Command Reference

### 1. Pre-Flight Validation (`--validate`)

Runs connectivity, schema compatibility, identity integrity, and media audits with **zero writes**.

```bash
python manage.py publish_curriculum --validate
```

Checks performed:
- Source and target database connectivity
- Verification that source and target databases are distinct
- Target database schema compatibility (verifying `content_uuid` and `content_hash` columns)
- Identity integrity (verifying no null `content_uuid` records)
- Operational model protection validation
- Media asset accessibility audit (flags missing local files)

---

### 2. Publication Dry Run (`--dry-run`)

Builds the complete publication plan and preview diff without touching production. This is the **default execution mode**.

```bash
# Preview all curriculum changes
python manage.py publish_curriculum

# Or explicitly:
python manage.py publish_curriculum --dry-run
```

**Scoped Dry Run:**

```bash
# Preview CBC curriculum only
python manage.py publish_curriculum --curriculum "CBC"

# Preview a specific grade and subject tree
python manage.py publish_curriculum \
    --curriculum "CBC" \
    --grade "Grade 4" \
    --subject "Mathematics"
```

**Example Output:**

```
╔══════════════════════════════════════════════════════════╗
║               VLearn Curriculum Publisher                ║
╠══════════════════════════════════════════════════════════╣
║  Mode:    DRY_RUN                                        ║
║  Source:  localhost:5433/vlearn_dev                      ║
║  Target:  aws-0-eu-central-1.pooler.supabase.com:postgres║
║  Scope:   curriculum=CBC, grade=Grade 4, subject=Math    ║
╚══════════════════════════════════════════════════════════╝

═══ PUBLICATION PLAN ═════════════════════════════════════
  Model                         Created  Updated  Unchanged
  --------------------------   -------- -------- ----------
  Curriculum                          0        0          1
  Grade                               0        0          1
  Subject                             0        0          1
  Topic                               2        0         10
  LearningUnit                        5        0         24
  Lesson                             12        3         45
  LessonBlock                       180       15        620
  LessonAsset                        24        0         80
  --------------------------   -------- -------- ----------
  TOTAL                             223       18        782

═══ MEDIA SUMMARY ════════════════════════════════════════
  External URLs (preserved):         84
  Cloudinary assets (preserved):     28
  Local files to upload:              2
  Missing files (blocking):           0

═══ OPERATIONAL DATA PROTECTION ══════════════════════════
  ✓ 0 Users modified
  ✓ 0 Subscriptions modified
  ✓ 0 Payment / Billing records modified
  ✓ 0 Student Progress records modified
  ✓ 0 School / Organization records modified
  ✓ 0 GenerationJobs modified

════════════════════════════════════════════════════════════
  DRY RUN COMPLETE — Zero writes performed. Run with --apply to publish.
════════════════════════════════════════════════════════════
```

---

### 3. Authorize and Publish (`--apply`)

Executes media uploads, acquires an advisory publication lock, and writes changes within an atomic database transaction on the production database.

```bash
# Publish with interactive confirmation
python manage.py publish_curriculum \
    --curriculum "CBC" \
    --grade "Grade 4" \
    --subject "Mathematics" \
    --apply
```

Before writing, you will be prompted:
```
--- PUBLICATION CONFIRMATION ---
Target Database: aws-0-eu-central-1.pooler.supabase.com:postgres
Scope:
  - curriculum: CBC
  - grade: Grade 4
  - subject: Mathematics

WARNING: This will overwrite data in the target database based on content_uuid.
To proceed, type 'PUBLISH' (case-sensitive) and press Enter.
> PUBLISH
```

**Non-Interactive / Automation:**

```bash
python manage.py publish_curriculum --apply --yes
```

> [!NOTE]
> `--yes` only bypasses the interactive terminal prompt. All safety checks (connection validation, schema inspection, media validation, source≠target verification) are **always executed**.

---

### 4. Database Alignment Check (`--align`)

Compares row counts and primary key overlaps across all models between local and production databases:

```bash
python manage.py publish_curriculum --align
```

---

## Media Handling

The visual enrichment system associates media assets with curriculum lessons. The publisher classifies and handles media systematically:

| Media Classification | Examples | Publisher Action |
|----------------------|----------|------------------|
| **External URL** | Wikimedia SVG, YouTube embed | Copied as-is (accessible via public CDN) |
| **Cloudinary Asset** | `https://res.cloudinary.com/...` | Preserved as-is (already accessible in production) |
| **Local Files** | Local diagrams, generated assets | Uploaded to production Cloudinary prior to DB transaction |
| **Missing Files** | Referenced file not found on disk | **Blocks publication** with validation error |

---

## Publication Reports & Audit Trail

Every publication execution automatically records:
1. **Machine-Readable JSON Report**: Stored in `docs/publication-reports/publication-YYYY-MM-DDTHHMMSS-XXXXXXXX.json` (credentials stripped).
2. **Local Database Audit Log**: Stored in `CurriculumPublication` table in local database.

---

## Troubleshooting

### `PublicationLockError`
If a previous publication crashed unexpectedly or is currently running, the advisory lock file (`/tmp/vlearn_publish.lock`) may remain. Ensure no other publishing process is running before removing the lock file.

### `Target database and source database are the same`
The command detected that `PUBLISH_DATABASE_URL` resolves to your local development database. Verify your connection string in `.env`.

### `Missing media: Local file not found on disk`
A lesson references a local asset path that does not exist. Ensure all media generation scripts have completed before publishing.
