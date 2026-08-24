"""Django management command to validate, preview, and publish curriculum content to production."""

import sys
from django.core.management.base import BaseCommand, CommandError
from curriculum.publisher.engine import CurriculumPublisher
from curriculum.publisher.verify_alignment import verify_alignment


class Command(BaseCommand):
    help = "Publishes approved curriculum from local authoring environment to production database."

    def add_arguments(self, parser):
        # Action modes
        mode_group = parser.add_argument_group("Execution Modes")
        mode_group.add_argument(
            "--validate",
            action="store_true",
            help="Run pre-flight validation checks only (connectivity, schema, identities, media, safety).",
        )
        mode_group.add_argument(
            "--dry-run",
            action="store_true",
            default=True,
            help="Build and preview publication diff without modifying target database (default mode).",
        )
        mode_group.add_argument(
            "--apply",
            action="store_true",
            help="Authorize and execute publication writes to target production database.",
        )
        mode_group.add_argument(
            "--align",
            action="store_true",
            help="Run one-time database alignment check (counts & PK comparison) between source and target.",
        )

        # Scope filters
        scope_group = parser.add_argument_group("Scope Filters")
        scope_group.add_argument(
            "--curriculum",
            type=str,
            help="Filter scope by curriculum name (e.g. 'CBC', '8-4-4').",
        )
        scope_group.add_argument(
            "--grade",
            type=str,
            help="Filter scope by grade name (e.g. 'Grade 4', 'Form 4').",
        )
        scope_group.add_argument(
            "--subject",
            type=str,
            help="Filter scope by subject name (e.g. 'Mathematics', 'Chemistry').",
        )

        # Safety & Automation
        parser.add_argument(
            "--yes",
            action="store_true",
            help="Skip interactive confirmation prompt when running with --apply.",
        )

    def handle(self, *args, **options):
        # 1. Alignment check utility
        if options.get("align"):
            self.stdout.write("Running database alignment verification...")
            verify_alignment()
            return

        # 2. Determine execution mode
        if options.get("validate"):
            mode = "validate"
        elif options.get("apply"):
            mode = "apply"
        else:
            mode = "dry_run"

        # 3. Build scope dictionary
        scope = {}
        if options.get("curriculum"):
            scope["curriculum"] = options["curriculum"]
        if options.get("grade"):
            scope["grade"] = options["grade"]
        if options.get("subject"):
            scope["subject"] = options["subject"]

        skip_confirmation = options.get("yes", False)
        verbosity = options.get("verbosity", 1)

        publisher = CurriculumPublisher(
            scope=scope,
            mode=mode,
            skip_confirmation=skip_confirmation,
            verbosity=verbosity,
        )

        try:
            success, report = publisher.run()
        except Exception as e:
            raise CommandError(f"Publishing failed with error: {e}")

        # Print formatted report
        self.stdout.write(report.format_cli())

        if report.report_file:
            self.stdout.write(f"\nReport written to: {report.report_file}")

        if not success:
            sys.exit(1)
