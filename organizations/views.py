import hashlib
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from organizations.permissions import IsSchoolAdmin

from organizations.models import (
    School,
    OrganizationMembership,
    AcademicYear,
    SchoolClass,
    Stream,
    TeacherSubjectAssignment,
    TeacherStreamAssignment,
    StudentEnrollment,
    SchoolSubscription,
    SchoolInvitation,
    TeacherSpecialty,
    Term,
    ExamConfiguration,
)
from organizations.serializers import (
    SchoolSerializer,
    OrganizationMembershipSerializer,
    AcademicYearSerializer,
    SchoolClassSerializer,
    StreamSerializer,
    TeacherSubjectAssignmentSerializer,
    TeacherStreamAssignmentSerializer,
    StudentEnrollmentSerializer,
    SchoolSubscriptionSerializer,
    SchoolInvitationSerializer,
    TeacherSpecialtySerializer,
    TermSerializer,
    ExamConfigurationSerializer,
    SetupWizardStateSerializer,
    BulkTeacherUploadSerializer,
    BulkStudentUploadSerializer,
    UserSummarySerializer,
)
from organizations.services import EntitlementService, SchoolOnboardingService, BulkUploadService
from curriculum.models import Subject

User = get_user_model()


class SchoolViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, and update School instances.
    """
    queryset = School.objects.all().order_by('-created_at')
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser:
            return School.objects.all().order_by('-created_at')
        
        # Filter schools where user is a member or owner
        return School.objects.filter(
            memberships__user=user,
            memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).distinct().order_by('-created_at')

    def perform_create(self, serializer):
        owner = serializer.validated_data.get('owner', self.request.user)
        school = serializer.save(owner=owner)
        
        # Ensure owner is registered as active school_admin membership
        OrganizationMembership.objects.get_or_create(
            user=owner,
            school=school,
            defaults={
                'role': 'school_admin',
                'state': 'ACTIVE',
                'assigned_by': self.request.user
            }
        )


class AcademicYearViewSet(viewsets.ModelViewSet):
    """
    Manage Academic Years for a school.
    """
    queryset = AcademicYear.objects.all().order_by('-start_date')
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class SchoolClassViewSet(viewsets.ModelViewSet):
    """
    Manage School Classes (e.g. Form 4, Grade 10).
    """
    queryset = SchoolClass.objects.all().order_by('name')
    serializer_class = SchoolClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs

    def create(self, request, *args, **kwargs):
        school_id = request.data.get('school')
        name = request.data.get('name')
        if school_id and name:
            existing = SchoolClass.objects.filter(school_id=school_id, name__iexact=name).first()
            if existing:
                serializer = self.get_serializer(existing)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)


class StreamViewSet(viewsets.ModelViewSet):
    """
    Manage Streams for classes (e.g. North, South).
    """
    queryset = Stream.objects.all().order_by('name')
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_class_id = self.request.query_params.get('school_class') or self.request.query_params.get('school_class_id')
        if school_class_id:
            qs = qs.filter(school_class_id=school_class_id)
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_class__school_id=school_id)
        return qs

    def create(self, request, *args, **kwargs):
        school_class_id = request.data.get('school_class')
        name = request.data.get('name')
        if school_class_id and name:
            existing = Stream.objects.filter(school_class_id=school_class_id, name__iexact=name).first()
            if existing:
                serializer = self.get_serializer(existing)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)


class OrganizationMembershipViewSet(viewsets.ModelViewSet):
    """
    Manage user memberships within a school and transition membership states.
    """
    queryset = OrganizationMembership.objects.all().order_by('-joined_at')
    serializer_class = OrganizationMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        
        user_param = self.request.query_params.get('user')
        if user_param == 'me':
            qs = qs.filter(user=self.request.user)
            
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        role = self.request.query_params.get('role')
        if role:
            qs = qs.filter(role=role)
        state = self.request.query_params.get('state')
        if state:
            qs = qs.filter(state=state)
        return qs

    @action(detail=True, methods=['post'], url_path='transition-state')
    def transition_state(self, request, pk=None):
        membership = self.get_object()
        new_state = request.data.get('state') or request.data.get('new_state')
        if not new_state:
            return Response(
                {"detail": "Parameter 'state' or 'new_state' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            updated_membership = EntitlementService.transition_membership_state(
                membership=membership,
                new_state=new_state,
                actor=request.user
            )
            serializer = self.get_serializer(updated_membership)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='add-teacher')
    def add_teacher(self, request):
        """
        Add a teacher to the school's authoritative staff roster.
        Establishes user record, membership, and specialties without forcing immediate invitation.
        """
        from Resources.models import User, UserProfile
        from organizations.models import TeacherSpecialty, SchoolInvitation
        from curriculum.models import Subject
        from django.db import transaction

        school_id = request.data.get('school_id') or request.data.get('school')
        name = request.data.get('name') or request.data.get('teacher_name')
        phone = request.data.get('phone') or request.data.get('phone_number')
        email = request.data.get('email')
        tsc = request.data.get('tsc_number') or request.data.get('tsc')
        specialties_str = request.data.get('specialties') or request.data.get('subject_specialties') or ''
        send_invite = request.data.get('send_invite', False)

        if not school_id:
            return Response({"detail": "school_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not name or not str(name).strip():
            return Response({"detail": "Teacher name is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not phone or not str(phone).strip():
            return Response({"detail": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        school = School.objects.filter(pk=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            EntitlementService.enforce_teacher_capacity(school)
        except ValidationError as e:
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)

        clean_phone = str(phone).strip().replace(' ', '').replace('-', '')
        if clean_phone.startswith('0'):
            clean_phone = '+254' + clean_phone[1:]
        elif clean_phone.startswith('254'):
            clean_phone = '+' + clean_phone

        with transaction.atomic():
            user = User.objects.filter(phone_number=clean_phone).first()
            if not user:
                names = str(name).strip().split(' ', 1)
                first_name = names[0]
                last_name = names[1] if len(names) > 1 else ''
                username = f"teacher_{clean_phone.replace('+', '')}"
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=clean_phone,
                    email=email or None,
                    role='teacher',
                    tsc_number=tsc or None,
                )
                user.set_unusable_password()
                user.save()
                UserProfile.objects.get_or_create(user=user)
            else:
                if name:
                    names = str(name).strip().split(' ', 1)
                    user.first_name = names[0]
                    if len(names) > 1:
                        user.last_name = names[1]
                if email and not user.email:
                    user.email = email
                if tsc:
                    user.tsc_number = tsc
                user.save()

            membership, _ = OrganizationMembership.objects.get_or_create(
                user=user,
                school=school,
                defaults={
                    'role': 'teacher',
                    'state': 'ACTIVE',
                    'assigned_by': request.user
                }
            )

            if specialties_str:
                specs = [s.strip() for s in specialties_str.split(',') if s.strip()]
                for spec_name in specs:
                    subject = Subject.objects.filter(name__iexact=spec_name).first()
                    if subject:
                        TeacherSpecialty.objects.get_or_create(
                            teacher=user,
                            subject=subject,
                            defaults={'school': school}
                        )

            if send_invite:
                try:
                    EntitlementService.create_school_invitation(
                        school=school,
                        role='teacher',
                        created_by=request.user,
                        phone_number=clean_phone,
                        email=email or ''
                    )
                except Exception as ex:
                    logger.warning(f"Could not dispatch invitation: {ex}")

        serializer = self.get_serializer(membership)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='send-invite')
    def send_invite(self, request, pk=None):
        membership = self.get_object()
        user = membership.user
        if not user or not user.phone_number:
            return Response({"detail": "Teacher has no phone number on file."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            invitation = EntitlementService.create_school_invitation(
                school=membership.school,
                role='teacher',
                created_by=request.user,
                phone_number=user.phone_number,
                email=user.email or ''
            )
            return Response({
                "detail": f"Invitation dispatched to {user.phone_number}",
                "raw_token": getattr(invitation, 'raw_token', None),
                "state": invitation.state
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)


class TeacherAssignmentViewSet(viewsets.ModelViewSet):
    """
    Manage Teacher Stream & Subject Assignments.
    """
    queryset = TeacherStreamAssignment.objects.all().order_by('-id')
    serializer_class = TeacherStreamAssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(stream__school_class__school_id=school_id)
        teacher_id = self.request.query_params.get('teacher') or self.request.query_params.get('teacher_id')
        if teacher_id:
            qs = qs.filter(teacher_id=teacher_id)
        stream_id = self.request.query_params.get('stream') or self.request.query_params.get('stream_id')
        if stream_id:
            qs = qs.filter(stream_id=stream_id)
        subject_id = self.request.query_params.get('subject') or self.request.query_params.get('subject_id')
        if subject_id:
            qs = qs.filter(subject_id=subject_id)
        return qs

    @action(detail=False, methods=['post'], url_path='assign-subject')
    def assign_subject(self, request):
        teacher_id = request.data.get('teacher_id') or request.data.get('teacher')
        school_id = request.data.get('school_id') or request.data.get('school')
        subject_id = request.data.get('subject_id') or request.data.get('subject')
        academic_year_id = request.data.get('academic_year_id') or request.data.get('academic_year')

        if not all([teacher_id, school_id, subject_id, academic_year_id]):
            return Response(
                {"detail": "teacher_id, school_id, subject_id, and academic_year_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not OrganizationMembership.objects.filter(
            user_id=teacher_id,
            school_id=school_id,
            state__in=['ACCEPTED', 'ACTIVE'],
            role='teacher'
        ).exists():
            return Response(
                {"detail": "Teacher must have an active teacher membership in the school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        assignment, _ = TeacherSubjectAssignment.objects.get_or_create(
            teacher_id=teacher_id,
            school_id=school_id,
            subject_id=subject_id,
            academic_year_id=academic_year_id
        )
        serializer = TeacherSubjectAssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='unassign-subject')
    def unassign_subject(self, request):
        assignment_id = request.data.get('assignment_id')
        if assignment_id:
            TeacherSubjectAssignment.objects.filter(id=assignment_id).delete()
            return Response({"detail": "Teacher subject assignment removed."}, status=status.HTTP_200_OK)

        teacher_id = request.data.get('teacher_id') or request.data.get('teacher')
        subject_id = request.data.get('subject_id') or request.data.get('subject')
        academic_year_id = request.data.get('academic_year_id') or request.data.get('academic_year')

        if teacher_id and subject_id and academic_year_id:
            TeacherSubjectAssignment.objects.filter(
                teacher_id=teacher_id,
                subject_id=subject_id,
                academic_year_id=academic_year_id
            ).delete()
            return Response({"detail": "Teacher subject assignment removed."}, status=status.HTTP_200_OK)

        return Response({"detail": "Valid assignment_id or parameters required."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='assign-stream')
    def assign_stream(self, request):
        teacher_id = request.data.get('teacher_id') or request.data.get('teacher')
        stream_id = request.data.get('stream_id') or request.data.get('stream')
        subject_id = request.data.get('subject_id') or request.data.get('subject')
        academic_year_id = request.data.get('academic_year_id') or request.data.get('academic_year')

        if not all([teacher_id, stream_id, subject_id, academic_year_id]):
            return Response(
                {"detail": "teacher_id, stream_id, subject_id, and academic_year_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            stream = Stream.objects.get(pk=stream_id)
            school_id = stream.school_class.school_id
        except Stream.DoesNotExist:
            return Response({"detail": "Stream not found."}, status=status.HTTP_404_NOT_FOUND)

        if not OrganizationMembership.objects.filter(
            user_id=teacher_id,
            school_id=school_id,
            state__in=['ACCEPTED', 'ACTIVE'],
            role='teacher'
        ).exists():
            return Response(
                {"detail": "Teacher must have an active teacher membership in the school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        assignment, _ = TeacherStreamAssignment.objects.get_or_create(
            teacher_id=teacher_id,
            stream_id=stream_id,
            subject_id=subject_id,
            academic_year_id=academic_year_id
        )
        serializer = TeacherStreamAssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='unassign-stream')
    def unassign_stream(self, request):
        assignment_id = request.data.get('assignment_id')
        if assignment_id:
            TeacherStreamAssignment.objects.filter(id=assignment_id).delete()
            return Response({"detail": "Teacher stream assignment removed."}, status=status.HTTP_200_OK)

        teacher_id = request.data.get('teacher_id') or request.data.get('teacher')
        stream_id = request.data.get('stream_id') or request.data.get('stream')
        subject_id = request.data.get('subject_id') or request.data.get('subject')
        academic_year_id = request.data.get('academic_year_id') or request.data.get('academic_year')

        if teacher_id and stream_id and subject_id and academic_year_id:
            TeacherStreamAssignment.objects.filter(
                teacher_id=teacher_id,
                stream_id=stream_id,
                subject_id=subject_id,
                academic_year_id=academic_year_id
            ).delete()
            return Response({"detail": "Teacher stream assignment removed."}, status=status.HTTP_200_OK)

        return Response({"detail": "Valid assignment_id or parameters required."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='subject-assignments')
    def list_subject_assignments(self, request):
        qs = TeacherSubjectAssignment.objects.all().order_by('-id')
        school_id = request.query_params.get('school') or request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        teacher_id = request.query_params.get('teacher') or request.query_params.get('teacher_id')
        if teacher_id:
            qs = qs.filter(teacher_id=teacher_id)
        serializer = TeacherSubjectAssignmentSerializer(qs, many=True)
        return Response(serializer.data)


class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    """
    Manage Student Enrollments into Streams with Entitlement Capacity checks.
    """
    queryset = StudentEnrollment.objects.all().order_by('-enrolled_at')
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(stream__school_class__school_id=school_id)
        stream_id = self.request.query_params.get('stream') or self.request.query_params.get('stream_id')
        if stream_id:
            qs = qs.filter(stream_id=stream_id)
        student_id = self.request.query_params.get('student') or self.request.query_params.get('student_id')
        if student_id:
            qs = qs.filter(student_id=student_id)
        status_param = self.request.query_params.get('status')
        if status_param:
            qs = qs.filter(status=status_param)
        return qs

    def perform_create(self, serializer):
        stream = serializer.validated_data.get('stream')
        school = stream.school_class.school
        EntitlementService.enforce_student_capacity(school)

        student = serializer.validated_data.get('student')
        # Ensure student has an active organization membership
        OrganizationMembership.objects.get_or_create(
            user=student,
            school=school,
            defaults={
                'role': 'student',
                'state': 'ACTIVE',
                'assigned_by': self.request.user
            }
        )

        serializer.save()

    @action(detail=False, methods=['post'], url_path='batch-enroll')
    def batch_enroll(self, request):
        stream_id = request.data.get('stream_id') or request.data.get('stream')
        academic_year_id = request.data.get('academic_year_id') or request.data.get('academic_year')
        student_ids = request.data.get('student_ids', [])
        if hasattr(request.data, 'getlist'):
            getlist_ids = request.data.getlist('student_ids')
            if getlist_ids:
                student_ids = getlist_ids
        if isinstance(student_ids, (int, str)):
            student_ids = [student_ids]
        student_emails = request.data.get('student_emails', [])
        if isinstance(student_emails, str):
            student_emails = [student_emails]

        if not stream_id or not academic_year_id:
            return Response(
                {"detail": "stream_id and academic_year_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            stream = Stream.objects.get(pk=stream_id)
        except Stream.DoesNotExist:
            return Response({"detail": "Stream not found."}, status=status.HTTP_404_NOT_FOUND)

        school = stream.school_class.school

        # Collect target student objects
        target_students = list(User.objects.filter(pk__in=student_ids))
        if student_emails:
            email_students = list(User.objects.filter(email__in=student_emails))
            target_students = list({s.id: s for s in target_students + email_students}.values())

        if not target_students:
            return Response({"detail": "No valid students provided for enrollment."}, status=status.HTTP_400_BAD_REQUEST)

        # Enforce student capacity
        try:
            EntitlementService.enforce_student_capacity(school)
        except ValidationError as e:
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)

        created_enrollments = []
        for student in target_students:
            # Ensure membership exists
            OrganizationMembership.objects.get_or_create(
                user=student,
                school=school,
                defaults={
                    'role': 'student',
                    'state': 'ACTIVE',
                    'assigned_by': request.user
                }
            )

            enrollment, created = StudentEnrollment.objects.get_or_create(
                student=student,
                academic_year_id=academic_year_id,
                defaults={
                    'stream': stream,
                    'status': 'active'
                }
            )
            if not created and enrollment.stream != stream:
                enrollment.stream = stream
                enrollment.status = 'active'
                enrollment.save()

            created_enrollments.append(enrollment)

        serializer = StudentEnrollmentSerializer(created_enrollments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SchoolSubscriptionViewSet(viewsets.ModelViewSet):
    """
    Manage Institutional Subscriptions.
    """
    queryset = SchoolSubscription.objects.all().order_by('-start_date')
    serializer_class = SchoolSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class SchoolInvitationViewSet(viewsets.ModelViewSet):
    """
    Create and list invitations to join a school as Teacher, Student, or Admin.
    Enforces seat capacity limits via EntitlementService.
    """
    queryset = SchoolInvitation.objects.all().order_by('-created_at')
    serializer_class = SchoolInvitationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        state = self.request.query_params.get('state')
        if state:
            qs = qs.filter(state=state)
        return qs

    def create(self, request, *args, **kwargs):
        school_id = request.data.get('school_id') or request.data.get('school')
        phone_number = request.data.get('phone_number') or request.data.get('phone')
        email = request.data.get('email') or ''
        role = request.data.get('role', 'teacher')
        intended_class_id = request.data.get('intended_class_id') or request.data.get('intended_class')
        intended_stream_id = request.data.get('intended_stream_id') or request.data.get('intended_stream')
        intended_subject_id = request.data.get('intended_subject_id') or request.data.get('intended_subject')

        if not school_id or (not phone_number and not email) or not role:
            return Response(
                {"detail": "school_id, role, and at least phone_number or email are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            school = School.objects.get(pk=school_id)
        except School.DoesNotExist:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)

        clean_phone = None
        if phone_number:
            clean_phone = str(phone_number).strip().replace(' ', '').replace('-', '')
            if clean_phone.startswith('0'):
                clean_phone = '+254' + clean_phone[1:]
            elif clean_phone.startswith('254'):
                clean_phone = '+' + clean_phone

        intended_class = SchoolClass.objects.filter(pk=intended_class_id).first() if intended_class_id else None
        intended_stream = Stream.objects.filter(pk=intended_stream_id).first() if intended_stream_id else None
        intended_subject = Subject.objects.filter(pk=intended_subject_id).first() if intended_subject_id else None

        try:
            invitation = EntitlementService.create_school_invitation(
                school=school,
                role=role,
                created_by=request.user,
                phone_number=clean_phone,
                email=email,
                intended_class=intended_class,
                intended_stream=intended_stream,
                intended_subject=intended_subject
            )
            serializer = self.get_serializer(invitation)
            data = serializer.data
            data['raw_token'] = getattr(invitation, 'raw_token', None)
            return Response(data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='revoke')
    def revoke(self, request, pk=None):
        invitation = self.get_object()
        invitation.state = 'REVOKED'
        invitation.save()
        serializer = self.get_serializer(invitation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherMyStreamsView(APIView):
    """
    GET /api/organizations/teacher/my-streams/
    Returns assigned streams, subjects, and student roster for the logged-in teacher.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teacher = request.user
        assignments = TeacherStreamAssignment.objects.filter(
            teacher=teacher
        ).select_related(
            'stream',
            'stream__school_class',
            'stream__school_class__school',
            'subject',
            'academic_year'
        )

        stream_map = {}
        for assign in assignments:
            stream = assign.stream
            s_id = stream.id
            if s_id not in stream_map:
                # Fetch enrolled students for this stream
                enrollments = StudentEnrollment.objects.filter(
                    stream=stream,
                    status='active'
                ).select_related('student')

                students_data = UserSummarySerializer(
                    [e.student for e in enrollments], many=True
                ).data

                stream_map[s_id] = {
                    "stream_id": stream.id,
                    "stream_name": stream.name,
                    "school_class_id": stream.school_class.id,
                    "school_class_name": stream.school_class.name,
                    "school_id": stream.school_class.school.id,
                    "school_name": stream.school_class.school.name,
                    "academic_year_id": assign.academic_year.id if assign.academic_year else None,
                    "academic_year_name": assign.academic_year.name if assign.academic_year else None,
                    "subjects": [],
                    "students": students_data
                }

            subject_info = {"id": assign.subject.id, "name": assign.subject.name}
            if subject_info not in stream_map[s_id]["subjects"]:
                stream_map[s_id]["subjects"].append(subject_info)

        if not stream_map and (getattr(teacher, 'role', None) in ['school_admin', 'platform_admin'] or teacher.is_superuser):
            # Admin workspace preview: return school's streams
            membership = OrganizationMembership.objects.filter(user=teacher).first()
            school = membership.school if membership else School.objects.first()
            if school:
                streams = Stream.objects.filter(school_class__school=school).select_related('school_class', 'school_class__school')
                for stream in streams:
                    enrollments = StudentEnrollment.objects.filter(stream=stream, status='active').select_related('student')
                    students_data = UserSummarySerializer([e.student for e in enrollments], many=True).data
                    stream_map[stream.id] = {
                        "stream_id": stream.id,
                        "stream_name": stream.name,
                        "school_class_id": stream.school_class.id,
                        "school_class_name": stream.school_class.name,
                        "school_id": stream.school_class.school.id,
                        "school_name": stream.school_class.school.name,
                        "academic_year_id": None,
                        "academic_year_name": None,
                        "subjects": [],
                        "students": students_data
                    }

        return Response(list(stream_map.values()), status=status.HTTP_200_OK)


class StudentMySchoolView(APIView):
    """
    GET /api/organizations/student/my-school/
    Returns school enrollment details for the logged-in student.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = request.user
        enrollments = StudentEnrollment.objects.filter(
            student=student,
            status='active'
        ).select_related(
            'stream',
            'stream__school_class',
            'stream__school_class__school',
            'academic_year'
        )

        result = []
        now = timezone.now()
        for e in enrollments:
            school = e.stream.school_class.school
            subscription = school.active_subscription
            has_active_sub = True  # Bypass subscription gate for testing

            result.append({
                "enrollment_id": e.id,
                "school_id": school.id,
                "school_name": school.name,
                "school_code": school.code,
                "class_id": e.stream.school_class.id,
                "class_name": e.stream.school_class.name,
                "stream_id": e.stream.id,
                "stream_name": e.stream.name,
                "academic_year_id": e.academic_year.id if e.academic_year else None,
                "academic_year_name": e.academic_year.name if e.academic_year else None,
                "has_active_subscription": has_active_sub,
                "enrolled_at": e.enrolled_at,
            })

        return Response(result, status=status.HTTP_200_OK)


class InvitationAcceptAPIView(APIView):
    """
    GET /api/organizations/invitations/accept/?token=<token>
    Validates invitation token without accepting.

    POST /api/organizations/invitations/accept/
    Accepts school invitation token and transitions membership state.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.query_params.get('token') or request.query_params.get('token_hash')
        if not token:
            return Response(
                {"detail": "Invitation token or token_hash parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest() if len(token) != 64 else token
        invitation = SchoolInvitation.objects.filter(token_hash=token_hash).first()

        if not invitation:
            return Response(
                {"detail": "Invalid invitation token.", "error": "invalid"},
                status=status.HTTP_404_NOT_FOUND
            )

        if invitation.state != 'PENDING':
            return Response(
                {"detail": "Invitation has already been used or revoked.", "error": "already_accepted"},
                status=status.HTTP_409_CONFLICT
            )

        if invitation.expires_at < timezone.now():
            invitation.state = 'EXPIRED'
            invitation.save()
            return Response(
                {"detail": "Invitation has expired.", "error": "expired"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({
            "valid": True,
            "email": invitation.email,
            "role": invitation.role,
            "school_name": invitation.school.name,
            "school_id": invitation.school.id,
            "intended_class": invitation.intended_class.name if invitation.intended_class else None,
            "intended_stream": invitation.intended_stream.name if invitation.intended_stream else None,
            "expires_at": invitation.expires_at,
        }, status=status.HTTP_200_OK)

    def post(self, request):
        token = request.data.get('token')
        token_hash = request.data.get('token_hash')

        if token:
            token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()

        if not token_hash:
            return Response(
                {"detail": "Invitation token or token_hash is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        invitation = SchoolInvitation.objects.filter(
            token_hash=token_hash,
            state='PENDING'
        ).first()

        if not invitation:
            return Response(
                {"detail": "Invalid or expired invitation token."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if invitation.expires_at < timezone.now():
            invitation.state = 'EXPIRED'
            invitation.save()
            return Response(
                {"detail": "Invitation has expired."},
                status=status.HTTP_400_BAD_REQUEST
            )

        target_user = request.user
        membership, _ = OrganizationMembership.objects.get_or_create(
            user=target_user,
            school=invitation.school,
            defaults={
                'role': invitation.role,
                'state': 'PENDING',
                'assigned_by': invitation.created_by
            }
        )

        invitation.state = 'ACCEPTED'
        invitation.save()

        try:
            updated_membership = EntitlementService.transition_membership_state(
                membership=membership,
                new_state='ACCEPTED',
                actor=request.user
            )
        except ValidationError as e:
            invitation.state = 'PENDING'
            invitation.save()
            return Response({"detail": str(e.message if hasattr(e, 'message') else e)}, status=status.HTTP_400_BAD_REQUEST)

        # Handle intended stream auto-enrollment or assignment
        if invitation.intended_stream:
            current_year = AcademicYear.objects.filter(
                school=invitation.school,
                is_current=True
            ).first() or AcademicYear.objects.filter(school=invitation.school).first()

            if invitation.role == 'student' and current_year:
                StudentEnrollment.objects.get_or_create(
                    student=target_user,
                    academic_year=current_year,
                    defaults={
                        'stream': invitation.intended_stream,
                        'status': 'active'
                    }
                )
            elif invitation.role == 'teacher' and current_year and invitation.intended_subject:
                TeacherStreamAssignment.objects.get_or_create(
                    teacher=target_user,
                    stream=invitation.intended_stream,
                    subject=invitation.intended_subject,
                    academic_year=current_year
                )

        serializer = OrganizationMembershipSerializer(updated_membership)
        return Response({
            "message": "Invitation accepted successfully",
            "membership": serializer.data
        }, status=status.HTTP_200_OK)


class SchoolRegisterProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            school = SchoolOnboardingService.register_school_profile(request.user, request.data)
            return Response({
                "message": "School registered successfully.",
                "school": {
                    "id": school.id,
                    "name": school.name,
                    "code": school.code,
                    "setup_status": school.setup_status
                }
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": getattr(e, 'message_dict', str(e))}, status=status.HTTP_400_BAD_REQUEST)


class SchoolSetupStateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, school_id):
        school = School.objects.filter(id=school_id, is_active=True).first()
        if not school:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Verify admin access
        if not request.user.memberships.filter(school=school, role='school_admin', state__in=['ACCEPTED', 'ACTIVE']).exists() and not request.user.is_staff:
            return Response({"error": "Unauthorized access to school setup."}, status=status.HTTP_403_FORBIDDEN)

        state = SchoolOnboardingService.get_school_setup_state(school)
        return Response(state, status=status.HTTP_200_OK)


class SchoolSaveDraftView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, school_id):
        school = School.objects.filter(id=school_id, is_active=True).first()
        if not school:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.memberships.filter(school=school, role='school_admin', state__in=['ACCEPTED', 'ACTIVE']).exists() and not request.user.is_staff:
            return Response({"error": "Unauthorized access."}, status=status.HTTP_403_FORBIDDEN)

        draft_data = request.data.get("draft_data", {})
        school = SchoolOnboardingService.save_setup_draft(school, draft_data, request.user)
        return Response({"message": "Draft saved successfully.", "setup_status": school.setup_status}, status=status.HTTP_200_OK)


class SchoolUploadBaselineView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, school_id):
        from Resources.models import UploadedFile
        school = School.objects.filter(id=school_id, is_active=True).first()
        if not school:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.memberships.filter(school=school, role='school_admin', state__in=['ACCEPTED', 'ACTIVE']).exists() and not request.user.is_staff:
            return Response({"error": "Unauthorized access."}, status=status.HTTP_403_FORBIDDEN)

        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"error": "Result sheet file is required."}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = UploadedFile.objects.create(
            user=request.user,
            file=file_obj,
            name=file_obj.name,
            size=file_obj.size,
            file_type=file_obj.name.split('.')[-1].lower(),
            description="Academic Baseline Upload"
        )

        try:
            result_sheet = SchoolOnboardingService.upload_academic_baseline(school, request.data, uploaded_file, request.user)
            return Response({
                "message": "Academic baseline file uploaded successfully.",
                "id": result_sheet.id,
                "processing_status": result_sheet.processing_status
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UnverifiedSchoolMergeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, suggestion_id):
        if not request.user.is_staff and getattr(request.user, 'role', '') != 'platform_admin':
            return Response({"error": "Platform admin access required."}, status=status.HTTP_403_FORBIDDEN)

        target_school_id = request.data.get('target_school_id')
        if not target_school_id:
            return Response({"error": "target_school_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            suggestion = SchoolOnboardingService.merge_unverified_school(suggestion_id, target_school_id, request.user)
            return Response({
                "message": f"Suggestion '{suggestion.name}' merged successfully into verified school ID {target_school_id}.",
                "status": suggestion.status
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class TeacherSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = TeacherSpecialty.objects.all().order_by('-created_at')
    serializer_class = TeacherSpecialtySerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all().order_by('academic_year', 'number')
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class ExamConfigurationViewSet(viewsets.ModelViewSet):
    queryset = ExamConfiguration.objects.all().order_by('-created_at')
    serializer_class = ExamConfigurationSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class SetupWizardView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get(self, request):
        school_id = request.query_params.get('school_id')
        if not school_id:
            return Response({"detail": "school_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({
            "current_step": school.setup_wizard_step,
            "school_data": SchoolSerializer(school).data
        }, status=status.HTTP_200_OK)

    def patch(self, request):
        school_id = request.data.get('school_id')
        step = request.data.get('step')
        if not school_id or step is None:
            return Response({"detail": "school_id and step are required."}, status=status.HTTP_400_BAD_REQUEST)
            
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        school.setup_wizard_step = int(step)
        school.save(update_fields=['setup_wizard_step'])
        
        return Response({
            "current_step": school.setup_wizard_step,
            "detail": "Setup wizard step updated successfully."
        }, status=status.HTTP_200_OK)


class BulkTeacherUploadView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def post(self, request):
        serializer = BulkTeacherUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        school_id = serializer.validated_data['school']
        file_obj = serializer.validated_data['file']
        
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            rows = BulkUploadService.parse_file(file_obj)
            created, errors = BulkUploadService.import_teachers(school, rows)
            return Response({"created": created, "errors": errors}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BulkStudentUploadView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def post(self, request):
        serializer = BulkStudentUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        stream_id = serializer.validated_data['stream']
        file_obj = serializer.validated_data['file']
        
        stream = Stream.objects.filter(id=stream_id).select_related('school_class__school').first()
        if not stream:
            return Response({"detail": "Stream not found."}, status=status.HTTP_404_NOT_FOUND)
            
        school = stream.school_class.school
        
        # Get current academic year
        academic_year = AcademicYear.objects.filter(school=school, is_current=True).first()
        if not academic_year:
            academic_year = AcademicYear.objects.filter(school=school).first()
            if not academic_year:
                return Response({"detail": "No academic year found for this school."}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            rows = BulkUploadService.parse_file(file_obj)
            created, errors = BulkUploadService.import_students(school, stream, academic_year, rows)
            return Response({"created": created, "errors": errors}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DownloadTemplateView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def get(self, request):
        import openpyxl
        from django.http import HttpResponse
        
        template_type = request.query_params.get('type')
        if template_type not in ['teacher', 'student']:
            return Response({"detail": "Invalid type. Must be 'teacher' or 'student'."}, status=status.HTTP_400_BAD_REQUEST)
            
        wb = openpyxl.Workbook()
        ws = wb.active
        
        if template_type == 'teacher':
            ws.title = "Teacher Upload Template"
            headers = ['Teacher Name', 'Phone Number', 'Email', 'TSC Number', 'Subject Specialties']
            example = ['John Doe', '+254700000000', 'john@example.com', '123456', 'Mathematics, Physics']
        else:
            ws.title = "Student Upload Template"
            headers = ['Student Name', 'Admission Number']
            example = ['Jane Doe', 'ADM-001']
            
        ws.append(headers)
        ws.append(example)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={template_type}_upload_template.xlsx'
        wb.save(response)
        
        return response
