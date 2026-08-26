from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, views, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    Lesson, LessonBlock, LessonAsset, LearningUnit,
    KnowledgePack, KnowledgeChunk,
    GenerationJob, PedagogyTemplate, GenerationRule,
    Concept, ConceptRelationship, LearningObjective, Misconception,
    LearningExperienceGraph, LearningSession, RuntimeNodeProgress,
    Simulation,
)
from curriculum.api.serializers import (
    CurriculumSerializer, GradeSerializer, SubjectSerializer, TopicSerializer,
    LessonSerializer, LessonBlockSerializer, LearningUnitSerializer,
    KnowledgePackSerializer, KnowledgeChunkSerializer, GenerationJobSerializer,
    # V2 additions
    LessonAssetSerializer, LessonBlockV2Serializer, LessonV2Serializer,
    # V3/V4 additions
    ConceptSerializer, ConceptRelationshipSerializer, LearningObjectiveSerializer,
    MisconceptionSerializer, LearningExperienceGraphSerializer,
    LearningSessionSerializer, RuntimeNodeProgressSerializer,
    SimulationSerializer,
)
from django.db import transaction
from curriculum.services import LessonGeneratorService
from Resources.permissions import HasSimulationAccess, HasActiveSubscription
from Resources.policies import get_user_content_restrictions
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
        return [IsAuthenticated()]

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
        user = self.request.user
        restrictions = get_user_content_restrictions(user)

        if restrictions['is_restricted']:
            return queryset.filter(id__in=restrictions['allowed_subject_ids'])
        
        is_teacher_or_admin = (
            user.is_authenticated and (
                user.is_staff or 
                user.is_superuser or 
                getattr(user, 'role', None) in ['teacher', 'platform_admin', 'school_admin']
            )
        )

        if self.request.query_params.get('enrolled') == 'true' and user.is_authenticated:
            # Bypass enrolled filter for staff, teachers, and administrators
            if not is_teacher_or_admin:
                if hasattr(user, 'profile'):
                    queryset = queryset.filter(id__in=user.profile.selected_subjects.values('id'))
                
        grade_id = self.request.query_params.get('grade')
        if grade_id:
            queryset = queryset.filter(grade_id=grade_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        restrictions = get_user_content_restrictions(request.user)
        if restrictions['is_restricted']:
            instance = self.get_object()
            if instance.id not in restrictions['allowed_subject_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', 'This account has limited demo privileges.')},
                    status=status.HTTP_403_FORBIDDEN
                )
        return super().retrieve(request, *args, **kwargs)

class TopicViewSet(BaseCurriculumViewSet):
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.select_related('subject', 'subject__grade').all().order_by('order')
        user = self.request.user
        restrictions = get_user_content_restrictions(user)

        if restrictions['is_restricted']:
            return queryset.filter(id__in=restrictions['allowed_topic_ids'])

        subject_id = self.request.query_params.get('subject')
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        restrictions = get_user_content_restrictions(request.user)
        if restrictions['is_restricted']:
            instance = self.get_object()
            if instance.id not in restrictions['allowed_topic_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', 'This account has limited demo privileges.')},
                    status=status.HTTP_403_FORBIDDEN
                )
        return super().retrieve(request, *args, **kwargs)


class ActiveLessonView(views.APIView):
    """
    Public endpoint: returns the latest published (or active) lesson for a given topic,
    including all its blocks.
    """
    permission_classes = [HasActiveSubscription]

    def get(self, request, topic_id):
        # 1. Resolve topic by primary key ID or by order/subject fallback
        topic = None
        if str(topic_id).isdigit():
            topic = Topic.objects.filter(id=int(topic_id)).first()

        if not topic:
            subj_param = request.query_params.get('subject') or request.query_params.get('subject_id')
            if subj_param and str(topic_id).isdigit():
                if str(subj_param).isdigit():
                    topic = Topic.objects.filter(subject_id=int(subj_param), order=int(topic_id)).first()
                else:
                    topic = Topic.objects.filter(subject__name__iexact=subj_param, order=int(topic_id)).first()

        if not topic and str(topic_id).isdigit():
            topic = Topic.objects.filter(order=int(topic_id)).first()

        if not topic:
            return Response(
                {"detail": "No topic found for the provided identifier."},
                status=status.HTTP_404_NOT_FOUND,
            )

        user = request.user
        lesson_id_param = request.query_params.get('lessonId') or request.query_params.get('lesson_id')
        is_preview = request.query_params.get('preview') == 'true'
        is_teacher_or_admin = (
            user.is_staff or 
            user.is_superuser or 
            getattr(user, 'role', None) in ['teacher', 'platform_admin', 'school_admin']
        )

        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            if topic.id not in restrictions['allowed_topic_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', "This account has limited demo privileges and is restricted to the Graham's Law lesson.")},
                    status=status.HTTP_403_FORBIDDEN
                )
            if lesson_id_param and str(lesson_id_param).isdigit():
                if restrictions.get('allowed_lesson_ids') and int(lesson_id_param) not in restrictions['allowed_lesson_ids']:
                    return Response(
                        {"detail": restrictions.get('restriction_message', "This account has limited demo privileges and is restricted to the Graham's Law lesson.")},
                        status=status.HTTP_403_FORBIDDEN
                    )

        from organizations.services import EntitlementService
        has_access = EntitlementService.check_curriculum_access(user, topic.subject_id)



        # 2. Resolve target lesson
        if lesson_id_param and str(lesson_id_param).isdigit():
            lesson = (
                Lesson.objects
                .filter(id=int(lesson_id_param))
                .prefetch_related('blocks', 'blocks__assets', 'assets')
                .first()
            )
        else:
            lesson = None

        if not lesson:
            if restrictions['is_restricted'] and restrictions.get('allowed_lesson_ids'):
                lesson = (
                    Lesson.objects
                    .filter(topic=topic, id__in=restrictions['allowed_lesson_ids'])
                    .prefetch_related('blocks', 'blocks__assets', 'assets')
                    .first()
                )
            elif is_preview or is_teacher_or_admin:
                lesson = (
                    Lesson.objects
                    .filter(topic=topic)
                    .prefetch_related('blocks', 'blocks__assets', 'assets')
                    .order_by('learning_unit__order', '-version')
                    .first()
                )
            else:
                if not has_access:
                    return Response(
                        {"detail": "You do not have access to this topic."},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                lesson = (
                    Lesson.objects
                    .filter(topic=topic, status='published')
                    .prefetch_related('blocks', 'blocks__assets', 'assets')
                    .order_by('learning_unit__order', '-version')
                    .first()
                )
                if not lesson:
                    lesson = (
                        Lesson.objects
                        .filter(topic=topic)
                        .prefetch_related('blocks', 'blocks__assets', 'assets')
                        .order_by('learning_unit__order', '-version')
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

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class LessonViewSet(viewsets.ModelViewSet):
    """
    V1 behaviour is the default and unchanged.
    Pass ?v=2 to receive V2 serialization (V2 fields + inline assets).
    """
    pagination_class = StandardResultsSetPagination
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'publish']:
            return [IsPlatformAdmin()]
        return [HasActiveSubscription()]

    def get_serializer_class(self):
        if self.request.query_params.get('v') == '2':
            return LessonV2Serializer
        return LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.prefetch_related('blocks', 'blocks__assets', 'assets').select_related(
            'topic', 'learning_unit', 'knowledge_pack'
        ).order_by('learning_unit__order', 'id')
        topic_id = self.request.query_params.get('topic')
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        learning_unit_id = self.request.query_params.get('learning_unit')
        if learning_unit_id:
            queryset = queryset.filter(learning_unit_id=learning_unit_id)

        user = self.request.user
        if not user.is_authenticated:
            return queryset.none()

        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            queryset = queryset.filter(topic_id__in=restrictions['allowed_topic_ids'])
            if restrictions.get('allowed_lesson_ids'):
                queryset = queryset.filter(id__in=restrictions['allowed_lesson_ids'])
            lesson_status = self.request.query_params.get('status')
            if lesson_status:
                queryset = queryset.filter(status=lesson_status)
            else:
                queryset = queryset.filter(status='published')
            return queryset

        from organizations.services import EntitlementService
        has_full_access = EntitlementService.has_full_curriculum_access(user)
        is_teacher_or_admin = (
            user.is_staff or 
            user.is_superuser or 
            getattr(user, 'role', None) in ['teacher', 'platform_admin', 'school_admin']
        )

        lesson_status = self.request.query_params.get('status')

        if has_full_access or is_teacher_or_admin:
            if lesson_status:
                queryset = queryset.filter(status=lesson_status)
        else:
            allowed_subject_ids = EntitlementService.get_allowed_subject_ids(user)
            if allowed_subject_ids:
                queryset = queryset.filter(topic__subject_id__in=allowed_subject_ids)
            if lesson_status:
                queryset = queryset.filter(status=lesson_status)
            else:
                # Filter by published, or return available lessons if all in topic are draft
                published_qs = queryset.filter(status='published')
                if published_qs.exists():
                    queryset = published_qs

        return queryset

    def retrieve(self, request, *args, **kwargs):
        restrictions = get_user_content_restrictions(request.user)
        if restrictions['is_restricted']:
            instance = self.get_object()
            if restrictions.get('allowed_lesson_ids') and instance.id not in restrictions['allowed_lesson_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', "This account has limited demo privileges and is restricted to the Graham's Law lesson.")},
                    status=status.HTTP_403_FORBIDDEN
                )
            if instance.topic_id not in restrictions['allowed_topic_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', "This account has limited demo privileges and is restricted to the Graham's Law lesson.")},
                    status=status.HTTP_403_FORBIDDEN
                )
        return super().retrieve(request, *args, **kwargs)



    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def publish(self, request, pk=None):
        lesson = self.get_object()

        if not lesson.learning_unit:
            return Response(
                {"errors": ["Lesson must be associated with a learning unit."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not lesson.title and lesson.learning_unit:
            lesson.title = lesson.learning_unit.name

        lesson.status = 'published'
        lesson.published_at = timezone.now()
        lesson.save()

        # Archive older published versions of this learning unit's lessons
        Lesson.objects.filter(
            topic=lesson.topic, learning_unit=lesson.learning_unit, status='published'
        ).exclude(id=lesson.id).update(status='archived')

        return Response(LessonSerializer(lesson).data)


# ---------------------------------------------------------------------------
# LessonBlock ViewSet
# ---------------------------------------------------------------------------

class LessonBlockViewSet(viewsets.ModelViewSet):
    serializer_class = LessonBlockSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'reorder']:
            return [IsPlatformAdmin()]
        return [HasActiveSubscription()]

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

        from curriculum.tasks import regenerate_lesson_block_task
        transaction.on_commit(lambda: regenerate_lesson_block_task.delay(job.id))

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

        from curriculum.tasks import process_textbook_pipeline_task
        transaction.on_commit(lambda: process_textbook_pipeline_task.delay(kp.id))

        return Response(KnowledgePackSerializer(kp).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def reprocess(self, request, pk=None):
        """
        Re-triggers document ingestion & TOC extraction for an existing KnowledgePack.
        """
        kp = self.get_object()
        kp.status = 'processing'
        kp.save()

        from curriculum.tasks import process_textbook_pipeline_task
        transaction.on_commit(lambda: process_textbook_pipeline_task.delay(kp.id))

        return Response(KnowledgePackSerializer(kp).data)

    @action(detail=False, methods=['post'], url_path='test-extraction')
    def test_extraction(self, request):
        """
        Non-LLM Ingestion Sandbox Endpoint.
        Parses the entire document in real-time, performing automatic text extraction,
        OCR detection, image clipping, bounding box coordinates, and automatic TOC recovery.
        """
        import time, base64, uuid, fitz
        from curriculum.extraction_pipeline import TESSERACT_AVAILABLE, pytesseract, Image, DocumentIngestionService

        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"detail": "PDF file is required."}, status=status.HTTP_400_BAD_REQUEST)

        start_time = time.time()
        try:
            file_bytes = file_obj.read()
            doc = fitz.open(stream=file_bytes, filetype="pdf")
        except Exception as e:
            return Response({"detail": f"Failed to parse PDF file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            total_pages = len(doc)
            tested_pages = total_pages  # Parse entire document

            native_toc = doc.get_toc(simple=True)
            filtered_native_toc = [
                item for item in native_toc 
                if len(item) >= 2 and not any(dummy in item[1].lower() for dummy in ["table of contents", "contents", "overview", "preface", "foreword"])
            ]
            has_native_outline = len(filtered_native_toc) >= 2
            native_outline_length = len(filtered_native_toc)

            structure = []
            if has_native_outline:
                last_topic = None
                for item in filtered_native_toc:
                    if len(item) < 3: continue
                    level, title, page = item[0], item[1], item[2]
                    node = {
                        'id': str(uuid.uuid4()),
                        'title': title,
                        'start_page': page,
                        'type': 'topic' if level == 1 else 'unit',
                        'source_type': 'native',
                        'children': []
                    }
                    if level == 1:
                        structure.append(node)
                        last_topic = node
                    elif level >= 2 and last_topic:
                        node['type'] = 'unit'
                        last_topic['children'].append(node)

            if len(structure) < 2:
                toc_structure = DocumentIngestionService._heuristic_regex_recovery(doc, max_scan_pages=total_pages)
            else:
                toc_structure = structure

            pages_data = []
            ocr_pages_triggered = []
            total_ocr_confidence = 0.0
            ocr_confidence_count = 0
            chunk_type_counts = {'core_text': 0, 'definition': 0, 'worked_example': 0, 'exercise': 0, 'diagram': 0, 'practical': 0}
            total_chunks_found = 0

            for page_num in range(tested_pages):
                try:
                    page = doc[page_num]
                    text = page.get_text()
                    blocks = page.get_text("blocks")
                    
                    is_scanned = len(text.strip()) < 100 or len(blocks) == 0 or (len(blocks) == 1 and len(blocks[0]) >= 7 and blocks[0][6] == 1)

                    page_chunks = []
                    was_ocr_triggered = False
                    ocr_confidence = None

                    if is_scanned and TESSERACT_AVAILABLE:
                        was_ocr_triggered = True
                        ocr_pages_triggered.append(page_num + 1)
                        try:
                            pix = page.get_pixmap()
                            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                            ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
                            confidences = [int(c) for c in ocr_data['conf'] if c != '-1']
                            if confidences:
                                ocr_confidence = sum(confidences) / len(confidences)
                                total_ocr_confidence += ocr_confidence
                                ocr_confidence_count += 1
                            ocr_text = pytesseract.image_to_string(img)
                            if ocr_text.strip():
                                c_type = DocumentIngestionService._classify_text_block(ocr_text)
                                chunk_type_counts[c_type] = chunk_type_counts.get(c_type, 0) + 1
                                total_chunks_found += 1
                                page_chunks.append({
                                    'chunk_type': c_type,
                                    'content': ocr_text.strip(),
                                    'bbox': [0.0, 0.0, float(pix.width), float(pix.height)]
                                })
                        except Exception as ocr_err:
                            print(f"Sandbox OCR error on page {page_num + 1}: {ocr_err}")
                    else:
                        for b in blocks:
                            is_image_block = len(b) >= 7 and b[6] == 1
                            if is_image_block:
                                try:
                                    rect = fitz.Rect(b[:4])
                                    pix = page.get_pixmap(clip=rect)
                                    img_bytes = pix.tobytes("png")
                                    b64_str = f"data:image/png;base64,{base64.b64encode(img_bytes).decode('utf-8')}"
                                    chunk_type_counts['diagram'] += 1
                                    total_chunks_found += 1
                                    page_chunks.append({
                                        'chunk_type': 'diagram',
                                        'content': '[Visual Diagram Clip]',
                                        'image_b64': b64_str,
                                        'bbox': [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
                                    })
                                except Exception as img_err:
                                    print(f"Image clipping error on page {page_num + 1}: {img_err}")
                            else:
                                if len(b) >= 5 and isinstance(b[4], str) and b[4].strip():
                                    block_text = b[4].strip()
                                    c_type = DocumentIngestionService._classify_text_block(block_text)
                                    chunk_type_counts[c_type] = chunk_type_counts.get(c_type, 0) + 1
                                    total_chunks_found += 1
                                    page_chunks.append({
                                        'chunk_type': c_type,
                                        'content': block_text,
                                        'bbox': [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
                                    })

                    pages_data.append({
                        'page_number': page_num + 1,
                        'text_length': len(text.strip()),
                        'was_ocr_triggered': was_ocr_triggered,
                        'ocr_confidence': round(ocr_confidence, 2) if ocr_confidence is not None else None,
                        'chunks': page_chunks
                    })
                except Exception as page_err:
                    print(f"Error processing page {page_num + 1}: {page_err}")
                    continue

            processing_time_ms = int((time.time() - start_time) * 1000)
            avg_ocr_confidence = round(total_ocr_confidence / ocr_confidence_count, 2) if ocr_confidence_count > 0 else None

            return Response({
                'file_metadata': {
                    'filename': file_obj.name,
                    'total_pages': total_pages,
                    'tested_pages': tested_pages,
                    'has_native_outline': has_native_outline,
                    'native_outline_length': native_outline_length
                },
                'toc_structure': toc_structure,
                'extraction_metrics': {
                    'total_chunks_found': total_chunks_found,
                    'ocr_pages_triggered': ocr_pages_triggered,
                    'average_ocr_confidence': avg_ocr_confidence,
                    'processing_time_ms': processing_time_ms,
                    'chunk_type_counts': chunk_type_counts
                },
                'pages': pages_data
            })
        except Exception as outer_err:
            import traceback
            traceback.print_exc()
            return Response(
                {"detail": f"Document extraction failed: {str(outer_err)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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
            existing_topics = list(Topic.objects.filter(subject=kp.subject).order_by('order'))
            processed_topic_ids = set()
            flat_units = []

            for i, topic_data in enumerate(final_structure):
                title = topic_data.get('title', 'Untitled Topic')
                try:
                    topic_start = int(topic_data.get('start_page') or 0)
                except (ValueError, TypeError):
                    topic_start = 0

                # Match existing topic by title or order index
                target_topic = None
                for et in existing_topics:
                    if et.id not in processed_topic_ids:
                        if et.name.strip().lower() == title.strip().lower() or (
                            et.name.split(':')[0].strip().lower() == title.split(':')[0].strip().lower()
                        ):
                            target_topic = et
                            break

                if not target_topic and i < len(existing_topics):
                    candidate = existing_topics[i]
                    if candidate.id not in processed_topic_ids:
                        target_topic = candidate

                if target_topic:
                    target_topic.name = title
                    target_topic.order = i
                    target_topic.save()
                else:
                    target_topic = Topic.objects.create(
                        subject=kp.subject,
                        name=title,
                        order=i
                    )
                processed_topic_ids.add(target_topic.id)

                children = topic_data.get('children', [])
                existing_units = list(LearningUnit.objects.filter(topic=target_topic).order_by('order'))

                if children:
                    for j, unit_data in enumerate(children):
                        unit_title = unit_data.get('title', 'Untitled Unit')
                        try:
                            start_page = int(unit_data.get('start_page') or topic_start or 0)
                        except (ValueError, TypeError):
                            start_page = topic_start

                        lu = None
                        for eu in existing_units:
                            if eu.name.strip().lower() == unit_title.strip().lower():
                                lu = eu
                                break
                        if not lu and j < len(existing_units):
                            lu = existing_units[j]

                        if lu:
                            lu.name = unit_title
                            lu.order = j
                            lu.save()
                        else:
                            lu = LearningUnit.objects.create(
                                topic=target_topic,
                                name=unit_title,
                                order=j
                            )
                        flat_units.append({'lu': lu, 'start_page': start_page})
                else:
                    if existing_units:
                        for j, lu in enumerate(existing_units):
                            lu.topic = target_topic
                            lu.order = j
                            lu.save()
                            flat_units.append({'lu': lu, 'start_page': topic_start})
                    else:
                        lu = LearningUnit.objects.create(
                            topic=target_topic,
                            name=f"Overview: {target_topic.name}",
                            order=0
                        )
                        flat_units.append({'lu': lu, 'start_page': topic_start})

            # Shift orphan units from unused legacy topics to the first new topic
            unused_topics = Topic.objects.filter(subject=kp.subject).exclude(id__in=processed_topic_ids)
            for ut in unused_topics:
                orphan_units = list(LearningUnit.objects.filter(topic=ut))
                if orphan_units and processed_topic_ids:
                    fallback_topic = Topic.objects.get(id=list(processed_topic_ids)[0])
                    for ou in orphan_units:
                        ou.topic = fallback_topic
                        ou.save()
                        flat_units.append({'lu': ou, 'start_page': 0})
                ut.delete()

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

            # Trigger Phase 4/5 Semantic Graph Extraction asynchronously
            from curriculum.tasks import semantic_structure_extraction_task
            unit_ids = [u['lu'].id for u in valid_units if u.get('lu')]
            if unit_ids:
                transaction.on_commit(lambda: semantic_structure_extraction_task.delay(kp.id, unit_ids))

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
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()] # Default for reading units

    def get_queryset(self):
        queryset = LearningUnit.objects.select_related(
            'topic', 'topic__subject', 'topic__subject__grade',
            'topic__subject__grade__curriculum',
        ).all().order_by('order')
        topic_id = self.request.query_params.get('topic')
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        
        user = self.request.user
        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            if restrictions.get('allowed_learning_unit_ids'):
                queryset = queryset.filter(id__in=restrictions['allowed_learning_unit_ids'])
            elif restrictions.get('allowed_topic_ids'):
                queryset = queryset.filter(topic_id__in=restrictions['allowed_topic_ids'])
        return queryset

    def retrieve(self, request, *args, **kwargs):
        restrictions = get_user_content_restrictions(request.user)
        if restrictions['is_restricted']:
            instance = self.get_object()
            if restrictions.get('allowed_learning_unit_ids') and instance.id not in restrictions['allowed_learning_unit_ids']:
                return Response(
                    {"detail": restrictions.get('restriction_message', "This account has limited demo privileges and is restricted to the Graham's Law lesson.")},
                    status=status.HTTP_403_FORBIDDEN
                )
        return super().retrieve(request, *args, **kwargs)


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

    @action(detail=True, methods=['post'], url_path='reassign-topic')
    def reassign_topic(self, request, pk=None):
        """
        Safely shifts a LearningUnit (and its knowledge chunks) to a new Topic.
        Preserves all associated lessons, blocks, concepts, and graphs.
        """
        learning_unit = self.get_object()
        target_topic_id = request.data.get('target_topic_id')
        if not target_topic_id:
            return Response({"detail": "target_topic_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        target_topic = get_object_or_404(Topic, id=target_topic_id)
        learning_unit.topic = target_topic
        learning_unit.save()

        # Update associated knowledge chunks topic pointers
        learning_unit.chunks.all().update(topic=target_topic)

        return Response(LearningUnitSerializer(learning_unit).data)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def generate_lesson(self, request, pk=None):
        learning_unit = self.get_object()
        lesson = LessonPersistenceService.get_or_create_draft_lesson(learning_unit.id)

        # ── Determine generation mode ──────────────────────────────────────────
        # Pass ?mode=blueprint (or {"mode": "blueprint"} in the body) to use the
        # new Instructional Blueprint engine. Omitting the field defaults to the
        # learning_experience_planner (V3 Pedagogical Engine).
        mode = request.data.get('mode') or request.query_params.get('mode') or 'learning_experience_planner'
        if mode not in ('legacy', 'blueprint', 'learning_experience_planner'):
            mode = 'learning_experience_planner'

        job = GenerationJob.objects.create(
            lesson=lesson,
            job_type='full_lesson',
            generation_mode=mode,
        )

        from curriculum.tasks import execute_generation_job_task
        transaction.on_commit(lambda: execute_generation_job_task.delay(job.id))

        return Response({
            "job_id": job.id,
            "generation_mode": mode,
            "detail": f"Generation job started (mode: {mode}).",
        })

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser], url_path='create_manual_lesson')
    def create_manual_lesson(self, request, pk=None):
        learning_unit = self.get_object()
        lesson = LessonPersistenceService.get_or_create_draft_lesson(learning_unit.id)
        return Response(LessonV2Serializer(lesson).data, status=status.HTTP_200_OK)


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

# ---------------------------------------------------------------------------
# Semantic Graph ViewSets
# ---------------------------------------------------------------------------

class ConceptViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConceptSerializer
    def get_queryset(self):
        qs = Concept.objects.all()
        learning_unit = self.request.query_params.get('learning_unit')
        if learning_unit:
            qs = qs.filter(learning_unit_id=learning_unit)
        return qs

class ConceptRelationshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConceptRelationshipSerializer
    queryset = ConceptRelationship.objects.all()

class LearningObjectiveViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LearningObjectiveSerializer
    def get_queryset(self):
        qs = LearningObjective.objects.all()
        learning_unit = self.request.query_params.get('learning_unit')
        if learning_unit:
            qs = qs.filter(learning_unit_id=learning_unit)
        return qs

class MisconceptionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MisconceptionSerializer
    queryset = Misconception.objects.all()

class LearningExperienceGraphViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LearningExperienceGraphSerializer
    def get_queryset(self):
        qs = LearningExperienceGraph.objects.all()
        learning_unit = self.request.query_params.get('learning_unit')
        if learning_unit:
            qs = qs.filter(learning_unit_id=learning_unit)
        return qs


# ---------------------------------------------------------------------------
# Interactive Simulation Registry ViewSet
# ---------------------------------------------------------------------------

class SimulationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public Read-Only ViewSet for registered interactive simulations.
    Supports filtering by ?subject=CHEMISTRY and ?status=ACTIVE
    """
    serializer_class = SimulationSerializer
    permission_classes = [HasActiveSubscription]

    def get_queryset(self):
        user = self.request.user
        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted'] and not restrictions['allow_simulations']:
            return Simulation.objects.none()

        qs = Simulation.objects.all()
        subject = self.request.query_params.get('subject')
        if subject:
            subject_lower = subject.lower()
            if 'chem' in subject_lower:
                qs = qs.filter(subject__iexact='CHEMISTRY')
            elif 'phys' in subject_lower:
                qs = qs.filter(subject__iexact='PHYSICS')
            else:
                # Simulations currently only exist for Chemistry and Physics
                return Simulation.objects.none()

        topic = self.request.query_params.get('topic')
        if topic:
            topic_lower = topic.lower()
            if 'acid' in topic_lower or 'base' in topic_lower or 'salt' in topic_lower:
                qs = qs.filter(topic__icontains='Acids')
            elif 'energy' in topic_lower or 'heat' in topic_lower:
                qs = qs.filter(topic__icontains='Energy')
            elif 'rate' in topic_lower or 'reversible' in topic_lower or 'equilibrium' in topic_lower or 'haber' in topic_lower:
                qs = qs.filter(topic__icontains='Reaction Rates')
            elif 'electro' in topic_lower or 'cell' in topic_lower or 'battery' in topic_lower:
                qs = qs.filter(topic__icontains='Electrochemistry')
            elif 'metal' in topic_lower:
                qs = qs.filter(topic__icontains='Metals')
            elif 'gas' in topic_lower:
                qs = qs.filter(topic__icontains='Gas Laws')
            elif 'circuit' in topic_lower or 'electric' in topic_lower:
                qs = qs.filter(topic__icontains='Circuits')
            elif 'kinematic' in topic_lower or 'gravity' in topic_lower or 'motion' in topic_lower:
                qs = qs.filter(topic__icontains='Kinematics')
            elif 'optics' in topic_lower or 'lens' in topic_lower or 'ray' in topic_lower:
                qs = qs.filter(topic__icontains='Optics')
            else:
                qs = qs.filter(topic__icontains=topic)

        status_param = self.request.query_params.get('status')
        if status_param:
            qs = qs.filter(status__iexact=status_param)
        return qs

    def retrieve(self, request, *args, **kwargs):
        restrictions = get_user_content_restrictions(request.user)
        if restrictions['is_restricted'] and not restrictions['allow_simulations']:
            return Response(
                {"detail": "This account has limited demo privileges and cannot access simulations."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().retrieve(request, *args, **kwargs)



# ---------------------------------------------------------------------------
# High-Performance Media Proxy & Edge Cache
# ---------------------------------------------------------------------------

import hashlib
import requests
from django.http import HttpResponse
from django.views import View
from django.core.cache import cache

class MediaProxyView(View):
    """
    Proxies and caches external educational media assets (such as Wikimedia Commons)
    to bypass client-side CORS / IP rate limits and guarantee 100% reliable image delivery.
    """
    def get(self, request, *args, **kwargs):
        target_url = request.GET.get('url')
        if not target_url or not target_url.startswith(('http://', 'https://')):
            return HttpResponse('Missing or invalid url parameter', status=400)
            
        allowed_domains = ['wikimedia.org', 'wikipedia.org', 'cloudinary.com', 'phydemo.app']
        if not any(domain in target_url for domain in allowed_domains):
            return HttpResponse('Domain not permitted for proxying', status=403)
            
        cache_key = f"media_proxy_{hashlib.md5(target_url.encode('utf-8')).hexdigest()}"
        cached_data = cache.get(cache_key)
        if cached_data:
            response = HttpResponse(cached_data['content'], content_type=cached_data['content_type'])
            response['Cache-Control'] = 'public, max-age=2592000' # 30 days
            response['Access-Control-Allow-Origin'] = '*'
            return response
            
        headers = {
            'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'
        }
        try:
            r = requests.get(target_url, headers=headers, timeout=10)
            if r.status_code == 200:
                content_type = r.headers.get('content-type', 'image/jpeg')
                if len(r.content) <= 10 * 1024 * 1024:
                    cache.set(cache_key, {'content': r.content, 'content_type': content_type}, timeout=60 * 60 * 24 * 30)
                response = HttpResponse(r.content, content_type=content_type)
                response['Cache-Control'] = 'public, max-age=2592000'
                response['Access-Control-Allow-Origin'] = '*'
                return response

            # If direct fetch fails (e.g. 404/400/429) for Wikimedia/Wikipedia, resolve via MediaWiki API
            if any(dom in target_url for dom in ['wikimedia.org', 'wikipedia.org']):
                import urllib.parse
                raw_name = target_url.split('/')[-1].split('?')[0]
                if '-' in raw_name and raw_name.split('-')[0].replace('px', '').isdigit():
                    raw_name = raw_name.split('-', 1)[1]
                raw_name = urllib.parse.unquote(raw_name)
                if not raw_name.startswith('File:'):
                    raw_name = f"File:{raw_name}"

                api_url = 'https://commons.wikimedia.org/w/api.php'
                params = {
                    'action': 'query',
                    'format': 'json',
                    'titles': raw_name,
                    'prop': 'imageinfo',
                    'iiprop': 'url',
                }
                api_res = requests.get(api_url, params=params, headers=headers, timeout=10).json()
                pages = api_res.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    imageinfo = pdata.get('imageinfo', [])
                    if imageinfo:
                        live_url = imageinfo[0].get('url')
                        if live_url:
                            r_live = requests.get(live_url, headers=headers, timeout=10)
                            if r_live.status_code == 200:
                                content_type = r_live.headers.get('content-type', 'image/jpeg')
                                if len(r_live.content) <= 10 * 1024 * 1024:
                                    cache.set(cache_key, {'content': r_live.content, 'content_type': content_type}, timeout=60 * 60 * 24 * 30)
                                response = HttpResponse(r_live.content, content_type=content_type)
                                response['Cache-Control'] = 'public, max-age=2592000'
                                response['Access-Control-Allow-Origin'] = '*'
                                return response

                # If exact title lookup fails, try search query fallback
                search_query = raw_name.replace('File:', '').replace('.jpg', '').replace('.png', '').replace('.jpeg', '').replace('_', ' ')
                search_params = {
                    'action': 'query',
                    'format': 'json',
                    'generator': 'search',
                    'gsrsearch': f'filetype:bitmap|drawing {search_query}',
                    'gsrnamespace': 6,
                    'gsrlimit': 1,
                    'prop': 'imageinfo',
                    'iiprop': 'url',
                }
                search_res = requests.get(api_url, params=search_params, headers=headers, timeout=10).json()
                s_pages = search_res.get('query', {}).get('pages', {})
                for pid, pdata in s_pages.items():
                    imageinfo = pdata.get('imageinfo', [])
                    if imageinfo:
                        live_url = imageinfo[0].get('url')
                        if live_url:
                            r_live = requests.get(live_url, headers=headers, timeout=10)
                            if r_live.status_code == 200:
                                content_type = r_live.headers.get('content-type', 'image/jpeg')
                                if len(r_live.content) <= 10 * 1024 * 1024:
                                    cache.set(cache_key, {'content': r_live.content, 'content_type': content_type}, timeout=60 * 60 * 24 * 30)
                                response = HttpResponse(r_live.content, content_type=content_type)
                                response['Cache-Control'] = 'public, max-age=2592000'
                                response['Access-Control-Allow-Origin'] = '*'
                                return response

            return HttpResponse(f'Upstream error: {r.status_code}', status=r.status_code)
        except Exception as e:
            return HttpResponse(f'Proxy fetch error: {str(e)}', status=502)


