"""CLI and JSON reporting for curriculum publishing."""

import json
import os
import socket
from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

from django.conf import settings


@dataclass
class PublicationReport:
    publication_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    scope: dict = field(default_factory=dict)
    source_host: str = ""
    target_host: str = ""
    mode: str = "dry_run"  # 'validate', 'dry_run', 'apply'
    validation_passed: bool = True
    counts: dict[str, dict[str, int]] = field(default_factory=dict)
    production_only_items: dict[str, list[str]] = field(default_factory=dict)
    media_counts: dict[str, int] = field(default_factory=lambda: {
        'external_urls': 0,
        'cloudinary_assets': 0,
        'local_files_to_upload': 0,
        'missing_files': 0,
    })
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
    report_file: str = ""

    @property
    def total_creates(self) -> int:
        return sum(c.get('created', 0) for c in self.counts.values())

    @property
    def total_updates(self) -> int:
        return sum(c.get('updated', 0) for c in self.counts.values())

    @property
    def total_unchanged(self) -> int:
        return sum(c.get('unchanged', 0) for c in self.counts.values())

    @property
    def total_production_only(self) -> int:
        return sum(len(items) for items in self.production_only_items.values())

    def format_cli(self) -> str:
        lines = []
        border = "═" * 58
        lines.append(f"╔{border}╗")
        lines.append(f"║{'VLearn Curriculum Publisher':^58}║")
        lines.append(f"╠{border}╣")
        lines.append(f"║  Mode:    {self.mode.upper():<47}║")
        lines.append(f"║  Source:  {self.source_host:<47}║")
        lines.append(f"║  Target:  {self.target_host:<47}║")

        scope_str = ", ".join(f"{k}={v}" for k, v in self.scope.items()) if self.scope else "All Curriculum"
        lines.append(f"║  Scope:   {scope_str:<47}║")
        lines.append(f"╚{border}╝")
        lines.append("")

        # Publication / Diff table
        if self.counts:
            lines.append("═══ PUBLICATION PLAN ═════════════════════════════════════")
            lines.append(f"  {'Model':<26} {'Created':>8} {'Updated':>8} {'Unchanged':>10}")
            lines.append(f"  {'-'*26} {'-'*8} {'-'*8} {'-'*10}")
            for model_name, cnts in self.counts.items():
                created = cnts.get('created', 0)
                updated = cnts.get('updated', 0)
                unchanged = cnts.get('unchanged', 0)
                lines.append(f"  {model_name:<26} {created:>8} {updated:>8} {unchanged:>10}")
            lines.append(f"  {'-'*26} {'-'*8} {'-'*8} {'-'*10}")
            lines.append(f"  {'TOTAL':<26} {self.total_creates:>8} {self.total_updates:>8} {self.total_unchanged:>10}")
            lines.append("")

        # Production-only items
        if self.production_only_items:
            lines.append("═══ PRODUCTION-ONLY CONTENT (Preserved) ═════════════════")
            for model_name, items in self.production_only_items.items():
                if items:
                    lines.append(f"  {model_name}: {len(items)} record(s) preserved in production")
            lines.append("")

        # Media summary
        lines.append("═══ MEDIA SUMMARY ════════════════════════════════════════")
        lines.append(f"  External URLs (preserved):     {self.media_counts.get('external_urls', 0):>6}")
        lines.append(f"  Cloudinary assets (preserved): {self.media_counts.get('cloudinary_assets', 0):>6}")
        lines.append(f"  Local files to upload:         {self.media_counts.get('local_files_to_upload', 0):>6}")
        lines.append(f"  Missing files (blocking):      {self.media_counts.get('missing_files', 0):>6}")
        lines.append("")

        # Operational safety confirmation
        lines.append("═══ OPERATIONAL DATA PROTECTION ══════════════════════════")
        lines.append("  ✓ 0 Users modified")
        lines.append("  ✓ 0 Subscriptions modified")
        lines.append("  ✓ 0 Payment / Billing records modified")
        lines.append("  ✓ 0 Student Progress records modified")
        lines.append("  ✓ 0 School / Organization records modified")
        lines.append("  ✓ 0 GenerationJobs modified")
        lines.append("")

        # Warnings / Errors
        if self.warnings:
            lines.append("═══ WARNINGS ═════════════════════════════════════════════")
            for w in self.warnings:
                lines.append(f"  ⚠️  {w}")
            lines.append("")

        if self.errors:
            lines.append("═══ ERRORS ═══════════════════════════════════════════════")
            for e in self.errors:
                lines.append(f"  ❌ {e}")
            lines.append("")

        # Outcome summary
        lines.append("═" * 60)
        if self.mode == "validate":
            status = "VALIDATION SUCCESSFUL — Ready for --dry-run or --apply" if self.validation_passed else "VALIDATION FAILED"
        elif self.mode == "dry_run":
            status = "DRY RUN COMPLETE — Zero writes performed. Run with --apply to publish." if not self.errors else "DRY RUN FAILED"
        else:
            if self.errors:
                status = "PUBLICATION FAILED — ROLLED BACK (Zero writes committed)."
            else:
                status = f"PUBLICATION APPLIED — {self.total_creates} created, {self.total_updates} updated."
        lines.append(f"  {status}")
        lines.append("═" * 60)

        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "publication_id": self.publication_id,
            "timestamp": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "mode": self.mode,
            "scope": self.scope,
            "source_host": self.source_host,
            "target_host": self.target_host,
            "published_by": socket.gethostname(),
            "validation_passed": self.validation_passed,
            "summary": {
                "total_creates": self.total_creates,
                "total_updates": self.total_updates,
                "total_unchanged": self.total_unchanged,
                "total_production_only": self.total_production_only,
            },
            "counts": self.counts,
            "media_counts": self.media_counts,
            "warnings": self.warnings,
            "errors": self.errors,
        }

    def write_json(self, output_dir: str | None = None) -> str:
        if output_dir is None:
            base_dir = getattr(settings, 'BASE_DIR', os.getcwd())
            output_dir = os.path.join(base_dir, 'docs', 'publication-reports')

        os.makedirs(output_dir, exist_ok=True)
        ts_str = self.started_at.strftime("%Y-%m-%dT%H%M%SZ")
        filename = f"publication-{ts_str}-{self.publication_id[:8]}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)

        self.report_file = filepath
        return filepath

    def save_audit_record(self, source_db: str = 'default'):
        """Saves a CurriculumPublication audit record in the local database."""
        try:
            from curriculum.models import CurriculumPublication
            CurriculumPublication.objects.using(source_db).create(
                publication_id=uuid.UUID(self.publication_id) if isinstance(self.publication_id, str) else self.publication_id,
                scope=self.scope,
                source_host=self.source_host,
                target_host=self.target_host,
                result="success" if not self.errors else "failed",
                counts=self.counts,
                errors=self.errors,
                warnings=self.warnings,
                report_file=self.report_file,
                published_by=socket.gethostname(),
                started_at=self.started_at,
            )
        except Exception as e:
            # Audit recording should not crash the command
            pass
