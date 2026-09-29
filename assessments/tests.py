from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from Resources.models import User
from curriculum.models import Curriculum, Grade, Subject
from organizations.models import School, AcademicYear, SchoolClass, Stream, OrganizationMembership
from assessments.models import Examination, StudentMark
from assessments.services import MarkEntryService
from assessments.aggregation import PerformanceAggregator
from assessments.permissions import CanEnterMarks
from rest_framework.test import APIRequestFactory


class MarkEntryServiceTests(TestCase):
    def setUp(self):
        self.super_user = User.objects.create_superuser(username="admin_mark", email="admin_mark@test.com", password="password")
        self.school = School.objects.create(name="Test School", code="SCH001", owner=self.super_user)
        self.academic_year = AcademicYear.objects.create(school=self.school, name="2026", start_date="2026-01-01", end_date="2026-12-31")
        self.curriculum = Curriculum.objects.create(name="844-Assess")
        self.grade = Grade.objects.create(name="Form 3", curriculum=self.curriculum)
        self.subject = Subject.objects.create(name="Physics", grade=self.grade)
        self.school_class = SchoolClass.objects.create(school=self.school, curriculum_grade=self.grade, name="Form 3")
        self.stream = Stream.objects.create(school_class=self.school_class, name="Stream A")
        self.teacher = User.objects.create_user(username="teacher_mark", email="t@test.com", password="password", role="teacher")
        self.student1 = User.objects.create_user(username="student_mark1", email="s1@test.com", password="password", role="student")
        self.student2 = User.objects.create_user(username="student_mark2", email="s2@test.com", password="password", role="student")

        self.examination = Examination.objects.create(
            school=self.school,
            academic_year=self.academic_year,
            term=1,
            name="Opener Exam",
            sequence=1,
            max_score=100
        )

    def test_validate_marks_valid(self):
        marks_data = [
            {'student_id': self.student1.id, 'score': 85.0},
            {'student_id': self.student2.id, 'score': 72.5},
        ]
        self.assertTrue(MarkEntryService.validate_marks(marks_data, self.examination, self.subject, self.stream))

    def test_validate_marks_out_of_bounds_negative(self):
        marks_data = [{'student_id': self.student1.id, 'score': -5.0}]
        with self.assertRaises(ValidationError) as ctx:
            MarkEntryService.validate_marks(marks_data, self.examination, self.subject, self.stream)
        self.assertIn("out of bounds", str(ctx.exception))

    def test_validate_marks_out_of_bounds_exceeds_max(self):
        marks_data = [{'student_id': self.student1.id, 'score': 105.0}]
        with self.assertRaises(ValidationError) as ctx:
            MarkEntryService.validate_marks(marks_data, self.examination, self.subject, self.stream)
        self.assertIn("out of bounds", str(ctx.exception))

    def test_validate_marks_with_null_max_score_defaults_safely(self):
        exam_null_max = Examination.objects.create(
            school=self.school,
            academic_year=self.academic_year,
            term=2,
            name="Midterm Exam",
            sequence=2,
            max_score=None
        )
        marks_data = [{'student_id': self.student1.id, 'score': 95.0}]
        self.assertTrue(MarkEntryService.validate_marks(marks_data, exam_null_max, self.subject, self.stream))

        # Should still reject > 100
        marks_data_over = [{'student_id': self.student1.id, 'score': 110.0}]
        with self.assertRaises(ValidationError):
            MarkEntryService.validate_marks(marks_data_over, exam_null_max, self.subject, self.stream)

    def test_validate_marks_invalid_string_score(self):
        marks_data = [{'student_id': self.student1.id, 'score': 'not_a_number'}]
        with self.assertRaises(ValidationError) as ctx:
            MarkEntryService.validate_marks(marks_data, self.examination, self.subject, self.stream)
        self.assertIn("Invalid score value", str(ctx.exception))

    def test_validate_marks_duplicate_student_entries(self):
        marks_data = [
            {'student_id': self.student1.id, 'score': 80.0},
            {'student_id': self.student1.id, 'score': 90.0},
        ]
        with self.assertRaises(ValidationError) as ctx:
            MarkEntryService.validate_marks(marks_data, self.examination, self.subject, self.stream)
        self.assertIn("Duplicate student entries", str(ctx.exception))

    def test_save_marks_persists_records(self):
        marks_data = [
            {'student_id': self.student1.id, 'score': 88.0},
            {'student_id': self.student2.id, 'score': 64.0},
        ]
        MarkEntryService.save_marks(marks_data, self.examination, self.subject, self.stream, self.teacher)

        mark1 = StudentMark.objects.get(student=self.student1, examination=self.examination, subject=self.subject)
        self.assertEqual(float(mark1.score), 88.0)
        self.assertEqual(mark1.entered_by, self.teacher)

        # Update mark
        marks_data_updated = [
            {'student_id': self.student1.id, 'score': 92.0},
        ]
        MarkEntryService.save_marks(marks_data_updated, self.examination, self.subject, self.stream, self.teacher)
        mark1.refresh_from_db()
        self.assertEqual(float(mark1.score), 92.0)


class PerformanceAggregatorTests(TestCase):
    def setUp(self):
        self.super_user = User.objects.create_superuser(username="admin_agg", email="agg_admin@test.com", password="password")
        self.school = School.objects.create(name="Agg School", code="SCH002", owner=self.super_user)
        self.academic_year = AcademicYear.objects.create(school=self.school, name="2026", start_date="2026-01-01", end_date="2026-12-31")
        self.curriculum = Curriculum.objects.create(name="844-Agg")
        self.grade = Grade.objects.create(name="Form 2", curriculum=self.curriculum)
        self.subject = Subject.objects.create(name="Math", grade=self.grade)
        self.school_class = SchoolClass.objects.create(school=self.school, curriculum_grade=self.grade, name="Form 2")
        self.stream = Stream.objects.create(school_class=self.school_class, name="Stream Alpha")
        self.student = User.objects.create_user(username="student_agg", email="agg_s@test.com", password="password", role="student")

        self.exam = Examination.objects.create(
            school=self.school,
            academic_year=self.academic_year,
            term=1,
            name="Term 1 Exam",
            sequence=1,
            max_score=100
        )

        StudentMark.objects.create(
            student=self.student,
            examination=self.exam,
            subject=self.subject,
            stream=self.stream,
            academic_year=self.academic_year,
            score=76.0,
            max_score=100
        )

    def test_student_performance(self):
        perf = PerformanceAggregator.student_performance(self.student.id, self.academic_year.id)
        self.assertEqual(perf['average'], 76.0)
        self.assertIn('grade', perf)

    def test_stream_subject_average(self):
        avg_res = PerformanceAggregator.stream_subject_average(self.stream.id, self.subject.id)
        self.assertEqual(avg_res['average'], 76.0)

    def test_student_longitudinal_record_without_field_error(self):
        record = PerformanceAggregator.student_longitudinal_record(self.student.id)
        self.assertEqual(len(record), 1)
        self.assertEqual(record[0]['academic_year__name'], "2026")
        self.assertEqual(float(record[0]['score']), 76.0)


class AssessmentPermissionsTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.perm = CanEnterMarks()
        self.super_user = User.objects.create_superuser(username="admin_perm", email="ap@test.com", password="password")
        self.teacher = User.objects.create_user(username="teacher_perm", email="tp@test.com", password="password", role="teacher")
        self.student = User.objects.create_user(username="student_perm", email="sp@test.com", password="password", role="student")

    def test_unauthenticated_user_denied(self):
        request = self.factory.get("/")
        request.user = None
        self.assertFalse(self.perm.has_permission(request, None))

    def test_student_denied(self):
        request = self.factory.get("/")
        request.user = self.student
        self.assertFalse(self.perm.has_permission(request, None))

    def test_teacher_allowed(self):
        request = self.factory.get("/")
        request.user = self.teacher
        self.assertTrue(self.perm.has_permission(request, None))

    def test_platform_admin_allowed(self):
        request = self.factory.get("/")
        request.user = self.super_user
        self.assertTrue(self.perm.has_permission(request, None))
