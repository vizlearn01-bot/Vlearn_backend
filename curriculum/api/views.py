from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, views, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
import threading

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    Lesson, LessonBlock, LessonAsset, LearningUnit,
    KnowledgePack, KnowledgeChunk,
    GenerationJob, PedagogyTemplate, GenerationRule,
)
from curriculum.api.serializers import (
    CurriculumSerializer, GradeSerializer, SubjectSerializer, TopicSerializer,
    LessonSerializer, LessonBlockSerializer, LearningUnitSerializer,
    KnowledgePackSerializer, KnowledgeChunkSerializer, GenerationJobSerializer,
    # V2 additions
    LessonAssetSerializer, LessonBlockV2Serializer, LessonV2Serializer,
)
from django.db import transaction
from curriculum.services import LessonGeneratorService
from curriculum.generation.orchestrator import GenerationOrchestrator
from curriculum.generation.blueprint_orchestrator import BlueprintOrchestrator
from curriculum.generation.persistence import LessonPersistenceService


# ---------------------------------------------------------------------------
# Public read-only curriculum navigation views
# ---------------------------------------------------------------------------

class BaseCurriculumViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for curriculum structure that allows public reads
    but requires admin privileges for any modifications.
    """
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

class CurriculumViewSet(BaseCurriculumViewSet):
    queryset = Curriculum.objects.all().order_by('-is_active', 'name')
    serializer_class = CurriculumSerializer

class GradeViewSet(BaseCurriculumViewSet):
    serializer_class = GradeSerializer

    def get_queryset(self):
        queryset = Grade.objects.select_related('curriculum').all().order_by('level')
        curriculum_id = self.request.query_params.get('curriculum')
        if curriculum_id:
            queryset = queryset.filter(curriculum_id=curriculum_id)
        return queryset

class SubjectViewSet(BaseCurriculumViewSet):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.select_related('grade', 'grade__curriculum').all().order_by('name')
        grade_id = self.request.query_params.get('grade')
        if grade_id:
            queryset = queryset.filter(grade_id=grade_id)
        return queryset

class TopicViewSet(BaseCurriculumViewSet):
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.select_related('subject', 'subject__grade').all().order_by('order')
        subject_id = self.request.query_params.get('subject')
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        return queryset


class ActiveLessonView(views.APIView):
    """
    Public endpoint: returns the latest published lesson for a given topic,
    including all its blocks.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)

        is_preview = request.query_params.get('preview') == 'true'
        if is_preview and request.user.is_staff:
            lesson = (
                Lesson.objects
                .filter(topic=topic)
                .prefetch_related('blocks')
                .order_by('-version')
                .first()
            )
        else:
            lesson = (
                Lesson.objects
                .filter(topic=topic, status='published')
                .prefetch_related('blocks')
                .order_by('-version')
                .first()
            )

        if not lesson:
            return Response(
                {"detail": "No published lesson found for this topic."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = LessonV2Serializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------------------------------------------------------------------------
# Lesson ViewSet
# ---------------------------------------------------------------------------

class LessonViewSet(viewsets.ModelViewSet):
    """
    V1 behaviour is the default and unchanged.
    Pass ?v=2 to receive V2 serialization (V2 fields + inline assets).
    """
    def get_serializer_class(self):
        if self.request.query_params.get('v') == '2':
            return LessonV2Serializer
        return LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.prefetch_related('blocks', 'assets').select_related(
            'topic', 'learning_unit', 'knowledge_pack'
        )
        topic_id = self.request.query_params.get('topic')
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        learning_unit_id = self.request.query_params.get('learning_unit')
        if learning_unit_id:
            queryset = queryset.filter(learning_unit_id=learning_unit_id)
        lesson_status = self.request.query_params.get('status')
        if lesson_status:
            queryset = queryset.filter(status=lesson_status)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def publish(self, request, pk=None):
        lesson = self.get_object()

        if lesson.status == 'published':
            return Response(
                {"errors": ["Lesson is already published."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not lesson.learning_unit:
            return Response(
                {"errors": ["Lesson must be associated with a learning unit."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subject = lesson.learning_unit.topic.subject
        template = PedagogyTemplate.objects.filter(subject=subject, is_active=True).first()

        if not template:
            return Response(
                {"errors": ["No active PedagogyTemplate found for this subject."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        rules = GenerationRule.objects.filter(template=template).order_by('order')
        mandatory_rules = rules.filter(is_mandatory=True)

        blocks = list(lesson.blocks.all())
        errors = []

        if not lesson.title:
            errors.append("Lesson title is missing.")

        # Check all mandatory blocks are present and have content
        for rule in mandatory_rules:
            matching_blocks = [b for b in blocks if b.block_type == rule.block_type]
            if not matching_blocks:
                errors.append(f"Missing mandatory block: {rule.block_type.replace('_', ' ')}")
            else:
                for b in matching_blocks:
                    if not b.content:
                        errors.append(f"Mandatory block '{b.title or b.block_type}' has no content.")
                    elif isinstance(b.content, dict) and not b.content.get('text') and not b.content.get('resource_id'):
                        errors.append(f"Mandatory block '{b.title or b.block_type}' has empty content.")

        # Check block ordering matches the template
        expected_order = [r.block_type for r in rules]
        actual_order = [b.block_type for b in blocks]
        filtered_actual = [t for t in actual_order if t in expected_order]
        try:
            indices = [expected_order.index(t) for t in filtered_actual]
            if indices != sorted(indices):
                errors.append("Block ordering does not match the pedagogy template.")
        except ValueError:
            pass

        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

        lesson.status = 'published'
        lesson.published_at = timezone.now()
        lesson.save()

        # Archive older published versions of this topic's lessons
        Lesson.objects.filter(
            topic=lesson.topic, status='published'
        ).exclude(id=lesson.id).update(status='archived')

        return Response(LessonSerializer(lesson).data)


# ---------------------------------------------------------------------------
# LessonBlock ViewSet
# ---------------------------------------------------------------------------

class LessonBlockViewSet(viewsets.ModelViewSet):
    serializer_class = LessonBlockSerializer

    def get_queryset(self):
        queryset = LessonBlock.objects.select_related('lesson')
        lesson_id = self.request.query_params.get('lesson')
        if lesson_id:
            queryset = queryset.filter(lesson_id=lesson_id)
        return queryset

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser])
    def reorder(self, request):
        """
        Expects a list of dicts: [{'id': 1, 'order': 0}, {'id': 2, 'order': 1}]
        """
        ordering = request.data.get('ordering', [])
        if not isinstance(ordering, list):
            return Response(
                {"detail": "ordering must be a list."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for item in ordering:
            LessonBlock.objects.filter(id=item['id']).update(order=item['order'])
        return Response({"detail": "Blocks reordered successfully."})

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def regenerate(self, request, pk=None):
        block = self.get_object()

        job = GenerationJob.objects.create(
            lesson=block.lesson,
            job_type='single_block',
            target_block_id=str(block.id),
        )

        thread = threading.Thread(
            target=GenerationOrchestrator.execute_job, args=(job.id,)
        )
        thread.daemon = True
        thread.start()

        return Response({"job_id": job.id, "detail": "Regeneration job started."})


# ---------------------------------------------------------------------------
# KnowledgePack ViewSet
# ---------------------------------------------------------------------------

class KnowledgePackViewSet(viewsets.ModelViewSet):
    serializer_class = KnowledgePackSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = KnowledgePack.objects.select_related('subject').all()
        subject_id = self.request.query_params.get('subject')
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        pack_status = self.request.query_params.get('status')
        if pack_status:
            queryset = queryset.filter(status=pack_status)
        return queryset

    @action(detail=False, methods=['post'])
    def upload(self, request):
        """
        Creates a KnowledgePack record in 'processing' status.
        Triggers background extraction.
        """
        subject_id = request.data.get('subject')
        file_obj = request.FILES.get('file')

        if not subject_id or not file_obj:
            return Response(
                {"detail": "subject and file are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        kp = KnowledgePack.objects.create(
            subject_id=subject_id,
            file=file_obj,
            status='processing',
        )

        from curriculum.extraction_pipeline import process_textbook_pipeline
        thread = threading.Thread(
            target=process_textbook_pipeline, args=(kp.id,)
        )
        thread.daemon = True
        thread.start()

        return Response(KnowledgePackSerializer(kp).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        kp = self.get_object()
        if kp.status == 'approved':
            return Response(
                {"detail": "Already approved."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        final_structure = request.data.get('structure', [])
        
        with transaction.atomic():
            # Populate Curriculum
            flat_units = []
            for i, topic_data in enumerate(final_structure):
                topic = Topic.objects.create(
                    subject=kp.subject,
                    name=topic_data.get('title', 'Untitled Topic'),
                    order=i
                )
                for j, unit_data in enumerate(topic_data.get('children', [])):
                    lu = LearningUnit.objects.create(
                        topic=topic,
                        name=unit_data.get('title', 'Untitled Unit'),
                        order=j
                    )
                    try:
                        start_page = int(unit_data.get('start_page') or topic_data.get('start_page') or 0)
                    except ValueError:
                        start_page = 0
                    flat_units.append({'lu': lu, 'start_page': start_page})

            # Phase 5: Intelligent Chunk Assignment
            valid_units = [u for u in flat_units if u['start_page'] > 0]
            valid_units.sort(key=lambda x: x['start_page'])
            
            for idx, u in enumerate(valid_units):
                start = u['start_page']
                if idx < len(valid_units) - 1:
                    end = valid_units[idx+1]['start_page'] - 1
                    if end < start:
                        end = start
                    kp.chunks.filter(start_page__gte=start, start_page__lte=end).update(
                        topic=u['lu'].topic,
                        learning_unit=u['lu']
                    )
                else:
                    kp.chunks.filter(start_page__gte=start).update(
                        topic=u['lu'].topic,
                        learning_unit=u['lu']
                    )

            kp.status = 'approved'
            kp.approved_at = timezone.now()
            kp.save()

            # Archive older approved versions for this subject
            KnowledgePack.objects.filter(
                subject=kp.subject, status='approved'
            ).exclude(id=kp.id).update(status='archived')

        return Response(KnowledgePackSerializer(kp).data)


# ---------------------------------------------------------------------------
# KnowledgeChunk ViewSet
# ---------------------------------------------------------------------------

class KnowledgeChunkViewSet(viewsets.ModelViewSet):
    serializer_class = KnowledgeChunkSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = KnowledgeChunk.objects.select_related(
            'knowledge_pack', 'topic', 'learning_unit'
        )
        pack_id = self.request.query_params.get('knowledge_pack')
        if pack_id:
            queryset = queryset.filter(knowledge_pack_id=pack_id)
        topic_id = self.request.query_params.get('topic')
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset


# ---------------------------------------------------------------------------
# LearningUnit ViewSet
# ---------------------------------------------------------------------------

class LearningUnitViewSet(viewsets.ModelViewSet):
    serializer_class = LearningUnitSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()] # Default for reading units

    def get_queryset(self):
        return LearningUnit.objects.select_related(
            'topic', 'topic__subject', 'topic__subject__grade',
            'topic__subject__grade__curriculum',
        ).all().order_by('order')

    @action(detail=True, methods=['get'])
    def repository_stats(self, request, pk=None):
        learning_unit = self.get_object()
        chunks = learning_unit.chunks.all()
        
        total_chunks = chunks.count()
        type_counts = {}
        for chunk in chunks:
            type_counts[chunk.chunk_type] = type_counts.get(chunk.chunk_type, 0) + 1
            
        # OCR confidence
        ocr_chunks = chunks.filter(ocr_confidence__isnull=False)
        if ocr_chunks.exists():
            avg_ocr = sum(c.ocr_confidence for c in ocr_chunks) / ocr_chunks.count()
        else:
            avg_ocr = None
            
        kp_version = "Unknown"
        first_chunk = chunks.first()
        if first_chunk and first_chunk.knowledge_pack:
            kp_version = f"v{first_chunk.knowledge_pack.version}"
            
        return Response({
            "total_chunks": total_chunks,
            "type_counts": type_counts,
            "avg_ocr_confidence": avg_ocr,
            "repository_version": kp_version,
            "has_warnings": total_chunks == 0
        })

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def generate_lesson(self, request, pk=None):
        learning_unit = self.get_object()
        lesson = LessonPersistenceService.get_or_create_draft_lesson(learning_unit.id)

        # ── Determine generation mode ──────────────────────────────────────────
        # Pass ?mode=blueprint (or {"mode": "blueprint"} in the body) to use the
        # new Instructional Blueprint engine.  Omitting the field keeps the
        # legacy V1 block-by-block engine so existing behaviour is unchanged.
        mode = request.data.get('mode') or request.query_params.get('mode') or 'legacy'
        if mode not in ('legacy', 'blueprint'):
            mode = 'legacy'

        job = GenerationJob.objects.create(
            lesson=lesson,
            job_type='full_lesson',
            generation_mode=mode,
        )

        if mode == 'blueprint':
            orchestrator_fn = BlueprintOrchestrator.execute_job
        else:
            orchestrator_fn = GenerationOrchestrator.execute_job

        thread = threading.Thread(target=orchestrator_fn, args=(job.id,))
        thread.daemon = True
        thread.start()

        return Response({
            "job_id": job.id,
            "generation_mode": mode,
            "detail": f"Generation job started (mode: {mode}).",
        })


# ---------------------------------------------------------------------------
# GenerationJob ViewSet (read-only for polling)
# ---------------------------------------------------------------------------

class GenerationJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GenerationJob.objects.select_related('lesson').all()
    serializer_class = GenerationJobSerializer


# ---------------------------------------------------------------------------
# LessonAsset ViewSet — V2 addition. Existing views above are unchanged.
# ---------------------------------------------------------------------------

class LessonAssetViewSet(viewsets.ModelViewSet):
    """
    CRUD for LessonAssets.

    Filter params:
      ?lesson=<id>   — all assets for a lesson
      ?block=<id>    — all assets attached to a specific block
      ?status=<val>  — filter by status (pending / attached / archived)
    """
    serializer_class = LessonAssetSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = LessonAsset.objects.select_related(
            'lesson', 'knowledge_chunk'
        ).prefetch_related('blocks')
        lesson_id = self.request.query_params.get('lesson')
        if lesson_id:
            qs = qs.filter(lesson_id=lesson_id)
        block_id = self.request.query_params.get('block')
        if block_id:
            qs = qs.filter(blocks__id=block_id)
        asset_status = self.request.query_params.get('status')
        if asset_status:
            qs = qs.filter(status=asset_status)
        return qs

    @action(detail=True, methods=['post'])
    def attach_to_block(self, request, pk=None):
        """
        Convenience action: add this asset to a LessonBlock's assets M2M.
        Body: { "block_id": <int> }
        """
        asset = self.get_object()
        block_id = request.data.get('block_id')
        if not block_id:
            return Response({'detail': 'block_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
        block = get_object_or_404(LessonBlock, id=block_id, lesson=asset.lesson)
        asset.blocks.add(block)
        return Response({'detail': f'Asset {asset.id} attached to block {block.id}.'})

    @action(detail=True, methods=['post'])
    def mark_attached(self, request, pk=None):
        """
        Marks the asset status as 'attached' once the admin has provided media.
        """
        asset = self.get_object()
        asset.status = 'attached'
        asset.save(update_fields=['status', 'updated_at'])
        return Response(LessonAssetSerializer(asset).data)
