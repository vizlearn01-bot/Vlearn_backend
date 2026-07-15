from django.core.management.base import BaseCommand
from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Populates the database with the canonical Form 4 Chemistry lesson.'

    def handle(self, *args, **kwargs):
        # 1. Create Hierarchy
        curriculum, _ = Curriculum.objects.get_or_create(
            name="Kenyan Secondary (8-4-4)",
            defaults={"description": "8-4-4 Curriculum"}
        )
        
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Form 4",
            defaults={"level": 4}
        )
        
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Chemistry"
        )
        
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            name="Acids, Bases and Salts",
            defaults={"order": 1}
        )
        
        # 2. Create Lesson
        lesson, created = Lesson.objects.get_or_create(
            topic=topic,
            version=1,
            defaults={
                "title": "Acids, Bases and Salts Complete Lesson",
                "status": "published",
                "published_at": timezone.now(),
                "immutable_metadata": {
                    "generation_job_id": "job_88a91b",
                    "ai_model": "gemini-1.5-flash",
                    "prompt_version": "v1.2",
                    "knowledge_pack_version": "kp_chem_844_v2",
                    "generated_at": datetime.datetime(2026, 7, 9, 8, 30, 0).isoformat()
                }
            }
        )
        
        if not created:
            self.stdout.write(self.style.WARNING("Lesson already exists. Skipping population."))
            return

        # 3. Create Blocks
        blocks_data = [
            {
                "block_id": "blk_01",
                "block_type": "overview",
                "order": 1,
                "title": "Lesson Overview",
                "content": "In this lesson, we explore the fundamental properties of acids, bases, and salts..."
            },
            {
                "block_id": "blk_02",
                "block_type": "objectives",
                "order": 2,
                "title": "Learning Objectives",
                "content": "- Define an acid and a base.\n- Understand the pH scale.\n- Explain the process of neutralization."
            },
            {
                "block_id": "blk_03",
                "block_type": "definitions",
                "order": 3,
                "title": "Key Definitions",
                "content": "**Acid**: A substance that produces hydrogen ions in water...\n**Base**: A substance that neutralizes an acid..."
            },
            {
                "block_id": "blk_04",
                "block_type": "core_explanation",
                "order": 4,
                "title": "Understanding Acids and Bases",
                "content": "Acids are ubiquitous in nature. The sour taste of a lemon..."
            },
            {
                "block_id": "blk_05",
                "block_type": "image_placeholder",
                "order": 5,
                "title": "The pH Scale Illustration",
                "content": {
                    "description": "A horizontal color gradient representing the pH scale from 0 to 14, marking 7 as neutral.",
                    "suggested_illustration": "Include familiar items like lemon juice (acidic) and soap (basic) on the scale.",
                    "search_keywords": ["pH scale", "acid base gradient", "chemistry pH"],
                    "resolved_image_url": "https://media.vlearn.co.ke/images/ph_scale_v1.png" 
                }
            },
            {
                "block_id": "blk_06",
                "block_type": "experiment",
                "order": 6,
                "title": "Testing pH with Litmus Paper",
                "content": {
                    "purpose": "To determine whether common household liquids are acidic or basic.",
                    "procedure": "1. Dip blue litmus paper into the lemon juice...\n2. Observe the color change...",
                    "expected_observations": "Blue litmus paper turns red in acids and remains blue in bases."
                }
            },
            {
                "block_id": "blk_07",
                "block_type": "simulation_placeholder",
                "order": 7,
                "title": "Acid-Base Neutralization Simulation",
                "content": {
                    "simulation_objective": "Allow students to mix varying strengths of acids and bases to see the resulting pH.",
                    "search_keywords": ["neutralization", "pH titration simulation", "chemistry interactive"],
                    "resolved_simulation_id": "sim_chem_titration_04"
                }
            },
            {
                "block_id": "blk_08",
                "block_type": "video_ref",
                "order": 8,
                "title": "Titration Demonstration",
                "content": {
                    "learning_objective": "Visualize a neutralization reaction using a burette and indicator.",
                    "search_keywords": ["titration", "neutralization experiment", "chemistry lab"],
                    "resolved_video_id": "vid_chem_titration_001"
                }
            },
            {
                "block_id": "blk_09",
                "block_type": "summary",
                "order": 9,
                "title": "Summary",
                "content": "- Acids produce H+ ions, bases neutralize them.\n- The pH scale measures acidity/alkalinity."
            },
            {
                "block_id": "blk_10",
                "block_type": "revision_questions",
                "order": 10,
                "title": "Revision Questions",
                "content": "1. What is the pH of pure water?\n2. Describe the color change of methyl orange in an acid."
            }
        ]

        for b_data in blocks_data:
            LessonBlock.objects.create(
                lesson=lesson,
                block_id=b_data['block_id'],
                block_type=b_data['block_type'],
                order=b_data['order'],
                title=b_data['title'],
                content=b_data['content']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated canonical lesson data!'))
