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

def setup_demo_accounts():
    print("Setting up marketing demo accounts...")

    curr_844 = Curriculum.objects.filter(name='844').first()
    grade_f3 = Grade.objects.filter(name='Form 3', curriculum=curr_844).first()
    subj_chem = Subject.objects.filter(id=27).first() or Subject.objects.filter(name__iexact='Chemistry', grade=grade_f3).first()

    curr_cbc = Curriculum.objects.filter(name='CBC').first()
    grade_g10 = Grade.objects.filter(name='Grade 10', curriculum=curr_cbc).first()
    subj_cs = Subject.objects.filter(id=38).first() or Subject.objects.filter(name__iexact='Computer Science', grade=grade_g10).first()

    demo_subjects = [s for s in [subj_chem, subj_cs] if s]

    # 1. Setup Demo School
    admin_user, _ = User.objects.get_or_create(username='demo_school_admin')
    admin_user.set_password('vizlearn123')
    admin_user.role = User.ROLE_SCHOOL_ADMIN
    admin_user.account_state = User.ACCOUNT_ACTIVE
    admin_user.is_staff = False
    admin_user.is_superuser = False
    admin_user.save()

    school, _ = School.objects.get_or_create(
        code='DEMO-001',
        defaults={
            'name': 'VizLearn Demo Academy',
            'contact_email': 'demo@vizlearn.co',
            'owner': admin_user,
            'school_type': 'NATIONAL',
            'curricula_offered': 'BOTH',
            'setup_status': 'FULLY_CONFIGURED',
            'setup_wizard_step': 8,
            'is_active': True,
        }
    )
    school.owner = admin_user
    school.curricula_offered = 'BOTH'
    school.is_active = True
    school.save()

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

    # Form 3 (8-4-4) Class & Stream
    f3_class, _ = SchoolClass.objects.get_or_create(
        school=school,
        name='Form 3',
        curriculum_grade=grade_f3
    )
    f3_stream, _ = Stream.objects.get_or_create(
        school_class=f3_class,
        name='Form 3 East'
    )

    # Grade 10 (CBC) Class & Stream
    g10_class, _ = SchoolClass.objects.get_or_create(
        school=school,
        name='Grade 10',
        curriculum_grade=grade_g10
    )
    g10_stream, _ = Stream.objects.get_or_create(
        school_class=g10_class,
        name='Grade 10 North'
    )

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

    # 2. Configure Student Demo Account (vizlearn-student-demo)
    student_names = ['vizlearn-student-demo', 'vizlearn_student_demo', 'vizlearn_test']
    for sname in student_names:
        su, _ = User.objects.get_or_create(username=sname)
        su.set_password('vizlearn123')
        su.email = f'{sname}@vizlearn.co'
        su.role = User.ROLE_STUDENT
        su.account_state = User.ACCOUNT_ACTIVE
        su.is_staff = False
        su.is_superuser = False
        su.first_name = 'Student'
        su.last_name = 'Demo'
        su.save()

        # Remove any school memberships to guarantee purely student view
        OrganizationMembership.objects.filter(user=su).delete()

        sp, _ = UserProfile.objects.get_or_create(user=su)
        sp.curriculum = curr_844
        sp.curriculum_grade = grade_f3
        sp.onboarding_complete = True
        sp.onboarding_status = 'FULLY_COMPLETE'
        sp.save()
        if demo_subjects:
            sp.selected_subjects.set(demo_subjects)
        print(f"Configured Student account '{sname}' (role: {su.role})")

    # 3. Configure Teacher Demo Account (vizlearn-teacher-demo)
    teacher_names = ['vizlearn-teacher-demo', 'vizlearn_teacher_demo']
    for tname in teacher_names:
        tu, _ = User.objects.get_or_create(username=tname)
        tu.set_password('vizlearn123')
        tu.email = f'{tname}@vizlearn.co'
        tu.role = User.ROLE_TEACHER
        tu.account_state = User.ACCOUNT_ACTIVE
        tu.is_staff = False
        tu.is_superuser = False
        tu.first_name = 'Teacher'
        tu.last_name = 'Demo'
        tu.save()

        tp, _ = UserProfile.objects.get_or_create(user=tu)
        tp.curriculum = curr_844
        tp.curriculum_grade = grade_f3
        tp.verified_school = school
        tp.onboarding_complete = True
        tp.onboarding_status = 'FULLY_COMPLETE'
        tp.save()
        if demo_subjects:
            tp.selected_subjects.set(demo_subjects)

        # Teacher Organization Membership
        tmem, _ = OrganizationMembership.objects.get_or_create(
            user=tu,
            school=school,
            defaults={'role': 'teacher', 'state': 'ACTIVE'}
        )
        tmem.role = 'teacher'
        tmem.state = 'ACTIVE'
        tmem.save()

        # Teacher Assignments - Form 3 Chemistry
        if subj_chem:
            TeacherSubjectAssignment.objects.get_or_create(
                teacher=tu,
                school=school,
                subject=subj_chem,
                academic_year=year
            )
            TeacherStreamAssignment.objects.get_or_create(
                teacher=tu,
                stream=f3_stream,
                subject=subj_chem,
                academic_year=year
            )

        # Teacher Assignments - Grade 10 Computer Science
        if subj_cs:
            TeacherSubjectAssignment.objects.get_or_create(
                teacher=tu,
                school=school,
                subject=subj_cs,
                academic_year=year
            )
            TeacherStreamAssignment.objects.get_or_create(
                teacher=tu,
                stream=g10_stream,
                subject=subj_cs,
                academic_year=year
            )

        print(f"Configured Teacher account '{tname}' (role: {tu.role})")

    print("\nSUCCESS: All Demo Accounts Configured with 8-4-4 Chemistry and CBC Grade 10 Computer Science!")

if __name__ == '__main__':
    setup_demo_accounts()

