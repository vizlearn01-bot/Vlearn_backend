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
    SchoolSubscription, StudentEnrollment
)
from assessments.models import Examination, StudentMark

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
    f3_stream = Stream.objects.filter(school_class=f3_class, name__in=['East', 'Form 3 East']).first()
    if not f3_stream:
        f3_stream = Stream.objects.create(school_class=f3_class, name='East')
    else:
        f3_stream.name = 'East'
        f3_stream.save()

    # Grade 10 (CBC) Class & Stream
    g10_class, _ = SchoolClass.objects.get_or_create(
        school=school,
        name='Grade 10',
        curriculum_grade=grade_g10
    )
    g10_stream = Stream.objects.filter(school_class=g10_class, name__in=['North', 'Grade 10 North']).first()
    if not g10_stream:
        g10_stream = Stream.objects.create(school_class=g10_class, name='North')
    else:
        g10_stream.name = 'North'
        g10_stream.save()

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

        # Enroll in Form 3 East
        en, _ = StudentEnrollment.objects.get_or_create(
            student=su,
            academic_year=year,
            defaults={'stream': f3_stream, 'status': 'active'}
        )
        if en.stream != f3_stream or en.status != 'active':
            en.stream = f3_stream
            en.status = 'active'
            en.save()

        print(f"Configured Student account '{sname}' (role: {su.role})")

    # Sample Class Students for Form 3 East
    sample_students_data = [
        ("Brian", "Otieno", 74),
        ("Faith", "Wanjiku", 88),
        ("Kevin", "Mwangi", 62),
        ("Mercy", "Chebet", 91),
        ("Dennis", "Kiprono", 48),  # Requires attention (<50)
        ("Esther", "Achieng", 82),
        ("Samuel", "Mutua", 55),
        ("Grace", "Njeri", 79),
        ("Victor", "Omondi", 44),  # Requires attention (<50)
        ("Joy", "Wambui", 86),
        ("Emmanuel", "Koech", 68),
        ("Sharon", "Anyango", 73),
        ("Collins", "Barasa", 59),
        ("Beatrice", "Moraa", 80),
        ("Daniel", "Njoroge", 65),
    ]

    # Ensure Examination exists
    exam, _ = Examination.objects.get_or_create(
        school=school,
        academic_year=year,
        name='Term 1 Mid-Term 2026',
        defaults={
            'term': 1,
            'sequence': 1,
            'max_score': 100,
            'date': timezone.now().date(),
            'status': 'open',
        }
    )

    for fn, ln, score in sample_students_data:
        uname = f"{fn.lower()}.{ln.lower()}"
        std, _ = User.objects.get_or_create(
            username=uname,
            defaults={
                'first_name': fn,
                'last_name': ln,
                'email': f"{uname}@student.vizlearn.co",
                'role': User.ROLE_STUDENT,
                'account_state': User.ACCOUNT_ACTIVE,
            }
        )
        en, _ = StudentEnrollment.objects.get_or_create(
            student=std,
            academic_year=year,
            defaults={'stream': f3_stream, 'status': 'active'}
        )
        if en.stream != f3_stream or en.status != 'active':
            en.stream = f3_stream
            en.status = 'active'
            en.save()

        # Seed mark in chemistry if subj_chem exists
        if subj_chem:
            StudentMark.objects.update_or_create(
                student=std,
                examination=exam,
                subject=subj_chem,
                defaults={
                    'stream': f3_stream,
                    'academic_year': year,
                    'score': score,
                    'max_score': 100,
                }
            )

    # 8 sample students in Grade 10 North
    sample_cbc_students = [
        ("Liam", "Kariuki"),
        ("Sophia", "Nduta"),
        ("Noah", "Cheruiyot"),
        ("Olivia", "Mumbua"),
        ("Ethan", "Kiptoo"),
        ("Ava", "Wairimu"),
        ("Lucas", "Wafula"),
        ("Mia", "Akinyi"),
    ]
    for fn, ln in sample_cbc_students:
        uname = f"{fn.lower()}.{ln.lower()}"
        std, _ = User.objects.get_or_create(
            username=uname,
            defaults={
                'first_name': fn,
                'last_name': ln,
                'email': f"{uname}@student.vizlearn.co",
                'role': User.ROLE_STUDENT,
                'account_state': User.ACCOUNT_ACTIVE,
            }
        )
        en, _ = StudentEnrollment.objects.get_or_create(
            student=std,
            academic_year=year,
            defaults={'stream': g10_stream, 'status': 'active'}
        )
        if en.stream != g10_stream or en.status != 'active':
            en.stream = g10_stream
            en.status = 'active'
            en.save()

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

        # Link as Class Teacher
        if tname == 'vizlearn-teacher-demo':
            f3_stream.class_teacher = tu
            f3_stream.save()
        else:
            g10_stream.class_teacher = tu
            g10_stream.save()

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

        print(f"Configured Teacher account '{tname}' (role: {tu.role}, Class Teacher: {f3_stream.name})")

    print("\nSUCCESS: All Demo Accounts Configured with 8-4-4 Chemistry and CBC Grade 10 Computer Science!")

if __name__ == '__main__':
    setup_demo_accounts()

