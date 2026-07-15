from curriculum.models import GenerationJob, LessonBlock
from .retrieval import RetrievalService
from .prompting import PromptBuilder
from .llm_client import LLMClient
from .validation import ValidationEngine
from .persistence import LessonPersistenceService

class GenerationOrchestrator:
    @staticmethod
    def execute_job(job_id: int):
        job = GenerationJob.objects.select_related('lesson', 'lesson__learning_unit', 'lesson__learning_unit__topic', 'lesson__learning_unit__topic__subject').get(id=job_id)
        try:
            LessonPersistenceService.update_job_status(job.id, 'generating')
            
            lesson = job.lesson
            learning_unit = lesson.learning_unit
            
            # 1. Retrieve Context
            context_package = RetrievalService.assemble_context(learning_unit.id)
            
            # Determine rules to run
            template = learning_unit.topic.subject.pedagogy_templates.filter(is_active=True).first()
            if not template:
                raise Exception("No active PedagogyTemplate found for this subject.")
                
            rules = template.rules.all().order_by('order')
            
            if job.job_type == 'single_block':
                # Filter to just the target rule based on block ID
                target_block = LessonBlock.objects.get(id=job.target_block_id)
                rules = [r for r in rules if r.block_type == target_block.block_type]
                if not rules:
                     raise Exception("No rule found for this block type.")
            
            for rule in rules:
                # 2. Get Previous Blocks for context
                previous_blocks = list(LessonBlock.objects.filter(lesson=lesson, order__lt=rule.order).order_by('order').values('block_type', 'content'))
                
                # 3. Build Prompt
                prompt = PromptBuilder.build_prompt(context_package, rule, previous_blocks)
                
                # 4. Generate
                content = LLMClient.generate(prompt)
                
                # 5. Validate
                is_valid = ValidationEngine.validate_block(content, rule.validation_schema)
                if not is_valid:
                    raise Exception(f"Validation failed for block {rule.block_type}")
                    
                # 6. Persist
                block_id = job.target_block_id if job.job_type == 'single_block' else None
                title = rule.block_type.replace('_', ' ').title()
                LessonPersistenceService.save_block(lesson, rule.block_type, title, content, rule.order, block_id)
                
            LessonPersistenceService.update_job_status(job.id, 'completed')
        except Exception as e:
            LessonPersistenceService.update_job_status(job.id, 'failed', str(e))
