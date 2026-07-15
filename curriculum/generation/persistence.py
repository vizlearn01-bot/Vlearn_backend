from curriculum.models import Lesson, LessonBlock, GenerationJob, LearningUnit


class LessonPersistenceService:

    @staticmethod
    def get_or_create_draft_lesson(learning_unit_id: int) -> Lesson:
        lu = LearningUnit.objects.select_related(
            'topic', 'topic__subject'
        ).get(id=learning_unit_id)

        # Return existing draft if one exists for this learning unit
        lesson = Lesson.objects.filter(learning_unit=lu, status='draft').first()
        if not lesson:
            lesson = Lesson.objects.create(
                topic=lu.topic,
                learning_unit=lu,
                title=lu.name,
                status='draft',
                version=1,
            )
        return lesson

    @staticmethod
    def save_block(
        lesson: Lesson,
        block_type: str,
        title: str,
        content: str,
        order: int,
        block_id: str = None,
    ) -> LessonBlock:
        """
        Persist a generated block.

        - If `block_id` is provided (single-block regeneration), update that
          specific block by its database ID.
        - Otherwise, create a new block. Using update_or_create keyed on
          (lesson, block_type) would silently overwrite when a lesson contains
          multiple blocks of the same type, so we always insert a new record
          during full-lesson generation.
        """
        if block_id:
            block = LessonBlock.objects.filter(id=block_id, lesson=lesson).first()
            if block:
                block.content = content
                block.title = title
                block.save(update_fields=['content', 'title'])
                return block

        # Full generation: insert a new block at the specified order position
        block = LessonBlock.objects.create(
            lesson=lesson,
            block_type=block_type,
            title=title,
            content=content,
            order=order,
        )
        return block

    @staticmethod
    def update_job_status(job_id: int, status: str, error_message: str = None):
        from django.utils import timezone
        job = GenerationJob.objects.get(id=job_id)
        job.status = status
        if error_message:
            job.error_message = error_message
        if status in ('completed', 'failed'):
            job.completed_at = timezone.now()
        job.save()
