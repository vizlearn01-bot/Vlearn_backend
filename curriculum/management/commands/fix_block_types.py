"""
Management command: fix_block_types

Retroactively corrects the block_type field on every LessonBlock that was
assembled by an older version of ExperienceAssemblyService, which mapped all
node_types to the 'concept_explanation' fallback.

The actual node_type is stored in block.metadata['node_type'].  We re-run the
same mapping logic now present in the assembler to produce the correct type.

Usage:
    python manage.py fix_block_types           # dry-run (prints changes)
    python manage.py fix_block_types --apply   # writes to DB
"""

from django.core.management.base import BaseCommand
from curriculum.models import LessonBlock


def _map(node_type: str) -> str:
    nt = (node_type or '').lower().strip()

    # Introduction / Hook
    if any(k in nt for k in ['hook', 'engage', 'motivat', 'wonder', 'scenario']):
        return 'hook'
    if any(k in nt for k in ['story', 'narrative', 'context_setting']):
        return 'story'
    if any(k in nt for k in ['goal', 'objective', 'intro', 'overview', 'orient']):
        return 'learning_goal'

    # Core Explanations
    if any(k in nt for k in ['explain', 'concept', 'core', 'teach', 'present']):
        return 'concept_explanation'
    if any(k in nt for k in ['definition', 'define', 'term', 'vocabulary']):
        return 'definitions'
    if any(k in nt for k in ['analog', 'metaphor', 'comparison']):
        return 'analogy'
    if any(k in nt for k in ['observe', 'watch', 'discover']):
        return 'concept_explanation'
    if any(k in nt for k in ['predict', 'hypothes', 'anticipat']):
        return 'concept_explanation'

    # Worked Examples / Application
    if any(k in nt for k in ['worked', 'example', 'demonstrat', 'show_how']):
        return 'worked_example'
    if any(k in nt for k in ['real_world', 'real world', 'application', 'context', 'case_study']):
        return 'real_world_example'
    if any(k in nt for k in ['practice', 'apply', 'scaffold', 'guided', 'drill', 'extend', 'extension']):
        return 'worked_example'
    if any(k in nt for k in ['experiment', 'activity', 'lab', 'explore', 'investigate']):
        return 'experiment'

    # Assessment / Check for Understanding
    if any(k in nt for k in ['assess', 'quiz', 'check', 'test', 'evaluat', 'review']):
        return 'knowledge_check'
    if any(k in nt for k in ['remediat', 'reteach', 'misconception', 'mistake', 'correct', 'clarify']):
        return 'common_misconception'
    if any(k in nt for k in ['reflect', 'journal', 'think', 'metacognit']):
        return 'reflection'

    # Summary / Coaching
    if any(k in nt for k in ['summary', 'summar', 'recap', 'consolidat', 'wrap']):
        return 'summary'
    if any(k in nt for k in ['key_takeaway', 'takeaway', 'tip', 'callout', 'highlight', 'memory']):
        return 'key_takeaway'

    # Media Suggestions
    if any(k in nt for k in ['diagram', 'visual', 'illustrat', 'chart', 'graph', 'figure']):
        return 'suggested_diagram'
    if any(k in nt for k in ['simulat', 'interact', 'phet']):
        return 'suggested_simulation'

    return 'concept_explanation'


class Command(BaseCommand):
    help = 'Retroactively fix block_type on all LessonBlocks using stored metadata.node_type'

    def add_arguments(self, parser):
        parser.add_argument(
            '--apply',
            action='store_true',
            default=False,
            help='Actually write the changes (default is a dry-run)',
        )

    def handle(self, *args, **options):
        apply = options['apply']
        mode = 'APPLY' if apply else 'DRY-RUN'
        self.stdout.write(self.style.WARNING(f'[{mode}] Scanning LessonBlocks...\n'))

        blocks = LessonBlock.objects.all()
        updated = 0
        skipped = 0

        for block in blocks:
            node_type = (block.metadata or {}).get('node_type', '')
            if not node_type:
                skipped += 1
                continue

            correct_type = _map(node_type)
            if block.block_type != correct_type:
                self.stdout.write(
                    f'  Block #{block.id} | node_type={node_type!r} '
                    f'| {block.block_type!r} → {correct_type!r}'
                )
                if apply:
                    block.block_type = correct_type
                    block.component_type = correct_type
                    block.save(update_fields=['block_type', 'component_type'])
                updated += 1

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'[{mode}] Done. {updated} blocks would be updated, {skipped} skipped (no node_type in metadata).'
        ))
        if not apply:
            self.stdout.write(self.style.NOTICE('Run with --apply to commit changes.'))
