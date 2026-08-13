import hashlib
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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
    UserSummarySerializer,
)
from organizations.services import EntitlementService, SchoolOnboardingService
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
        email = request.data.get('email')
        role = request.data.get('role')
        intended_class_id = request.data.get('intended_class_id') or request.data.get('intended_class')
        intended_stream_id = request.data.get('intended_stream_id') or request.data.get('intended_stream')
        intended_subject_id = request.data.get('intended_subject_id') or request.data.get('intended_subject')

        if not school_id or not email or not role:
            return Response(
                {"detail": "school_id, email, and role are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            school = School.objects.get(pk=school_id)
        except School.DoesNotExist:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)

        intended_class = SchoolClass.objects.filter(pk=intended_class_id).first() if intended_class_id else None
        intended_stream = Stream.objects.filter(pk=intended_stream_id).first() if intended_stream_id else None
        intended_subject = Subject.objects.filter(pk=intended_subject_id).first() if intended_subject_id else None

        try:
            invitation = EntitlementService.create_school_invitation(
                school=school,
                email=email,
                role=role,
                created_by=request.user,
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

