import os
import django
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.utils import timezone
from Resources.models import User, UserProfile
from curriculum.models import Curriculum, Grade, Subject
from organizations.models import (
    School, OrganizationMembership, AcademicYear, Term,
    SchoolClass, Stream, TeacherSubjectAssignment, TeacherStreamAssignment,
    SchoolSubscription
)

def setup_demo_account():
    print("Setting up marketing demo account (vizlearn_test)...")

    # 1. User
    u, created = User.objects.get_or_create(username='vizlearn_test')
    u.set_password('vizlearn123')
    u.email = 'vizlearn_test@vizlearn.co'
    u.role = User.ROLE_SCHOOL_ADMIN
    u.account_state = User.ACCOUNT_ACTIVE
    u.is_staff = False
    u.is_superuser = False
    u.first_name = 'VizLearn'
    u.last_name = 'Demo'
    u.save()
    print(f"User vizlearn_test (ID: {u.id}) configured.")

    # 2. Profile
    p, _ = UserProfile.objects.get_or_create(user=u)
    curr_844 = Curriculum.objects.filter(name='844').first()
    grade_f3 = Grade.objects.filter(name='Form 3', curriculum=curr_844).first()
    subj_chem = Subject.objects.filter(id=27).first()

    p.curriculum = curr_844
    p.curriculum_grade = grade_f3
    p.onboarding_complete = True
    p.onboarding_status = 'FULLY_COMPLETE'
    p.save()
    if subj_chem:
        p.selected_subjects.set([subj_chem])
    print("User profile configured.")

    # 3. Demo School
    school, _ = School.objects.get_or_create(
        code='DEMO-001',
        defaults={
            'name': 'VizLearn Demo Academy',
            'contact_email': 'demo@vizlearn.co',
            'owner': u,
            'school_type': 'NATIONAL',
            'curricula_offered': '8-4-4',
            'setup_status': 'FULLY_CONFIGURED',
            'setup_wizard_step': 8,
            'is_active': True,
        }
    )
    school.owner = u
    school.is_active = True
    school.save()

    p.verified_school = school
    p.save()
    print(f"Demo school '{school.name}' (ID: {school.id}) configured.")

    # 4. Academic Year & Term
    year, _ = AcademicYear.objects.get_or_create(
        school=school,
        name='2026',
        defaults={
            'is_current': True,
            'start_date': timezone.now().date() - timedelta(days=30),
            'end_date': timezone.now().date() + timedelta(days=335),
        }
    )
    year.is_current = True
    year.save()

    term, _ = Term.objects.get_or_create(
        school=school,
        academic_year=year,
        number=1,
        defaults={
            'name': 'Term 1',
            'is_current': True,
            'start_date': timezone.now().date() - timedelta(days=30),
            'end_date': timezone.now().date() + timedelta(days=60),
        }
    )
    term.is_current = True
    term.save()

    # 5. School Classes & Streams
    f3_class, _ = SchoolClass.objects.get_or_create(
        school=school,
        name='Form 3',
        curriculum_grade=grade_f3
    )
    f3_stream, _ = Stream.objects.get_or_create(
        school_class=f3_class,
        name='Form 3 East'
    )

    # 6. Organization Membership
    mem, _ = OrganizationMembership.objects.get_or_create(
        user=u,
        school=school,
        defaults={'role': 'school_admin', 'state': 'ACTIVE'}
    )
    mem.role = 'school_admin'
    mem.state = 'ACTIVE'
    mem.save()

    # 7. Teacher Assignments
    if subj_chem:
        TeacherSubjectAssignment.objects.get_or_create(
            teacher=u,
            school=school,
            subject=subj_chem,
            academic_year=year
        )
        TeacherStreamAssignment.objects.get_or_create(
            teacher=u,
            stream=f3_stream,
            subject=subj_chem,
            academic_year=year
        )

    # 8. School Subscription
    sub, _ = SchoolSubscription.objects.get_or_create(
        school=school,
        defaults={
            'max_teachers': 50,
            'max_students': 2000,
            'is_active': True,
            'start_date': timezone.now() - timedelta(days=30),
            'end_date': timezone.now() + timedelta(days=335),
        }
    )
    sub.is_active = True
    sub.save()

    print("Marketing demo account setup COMPLETE!")

if __name__ == '__main__':
    setup_demo_account()
