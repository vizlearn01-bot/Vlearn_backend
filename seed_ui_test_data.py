import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from Resources.models import User
from subscriptions.models import SubscriptionPlan
from curriculum.models import Curriculum, Grade, Subject
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
)
from datetime import timedelta
from django.utils import timezone

def seed_test_accounts():
    print("Seeding UI Test Accounts & Environment...")

    # 1. Platform Admin
    admin_user, created = User.objects.get_or_create(
        username="platform_admin",
        defaults={"email": "admin@vizlearn.co", "role": "platform_admin", "is_staff": True, "is_superuser": True}
    )
    if created or not admin_user.check_password("password123"):
        admin_user.set_password("password123")
        admin_user.role = "platform_admin"
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
    print("[+] Platform Admin ready: username='platform_admin', password='password123'")

    # 2. School Admin 1 (School 1)
    sadmin1, created = User.objects.get_or_create(
        username="school_admin1",
        defaults={"email": "admin1@northschool.co", "role": "school_admin"}
    )
    if created or not sadmin1.check_password("password123"):
        sadmin1.set_password("password123")
        sadmin1.role = "school_admin"
        sadmin1.save()
    print("[+] School Admin 1 ready: username='school_admin1', password='password123'")

    # 3. School Admin 2 (School 2)
    sadmin2, created = User.objects.get_or_create(
        username="school_admin2",
        defaults={"email": "admin2@southschool.co", "role": "school_admin"}
    )
    if created or not sadmin2.check_password("password123"):
        sadmin2.set_password("password123")
        sadmin2.role = "school_admin"
        sadmin2.save()
    print("[+] School Admin 2 ready: username='school_admin2', password='password123'")

    # 4. Teacher 1
    teacher1, created = User.objects.get_or_create(
        username="teacher1",
        defaults={"email": "teacher1@northschool.co", "role": "teacher"}
    )
    if created or not teacher1.check_password("password123"):
        teacher1.set_password("password123")
        teacher1.role = "teacher"
        teacher1.save()
    print("[+] Teacher 1 ready: username='teacher1', password='password123'")

    # 5. Student 1
    student1, created = User.objects.get_or_create(
        username="student1",
        defaults={"email": "student1@northschool.co", "role": "student"}
    )
    if created or not student1.check_password("password123"):
        student1.set_password("password123")
        student1.role = "student"
        student1.save()
    print("[+] Student 1 ready: username='student1', password='password123'")

    # Ensure a SubscriptionPlan exists
    plan, _ = SubscriptionPlan.objects.get_or_create(
        plan_id="school_pro",
        defaults={
            "name": "School Pro Plan",
            "description": "Institutional Pro Subscription",
            "price": 500.00,
            "duration_days": 365,
        }
    )

    # Ensure Curriculum / Grade / Subject exist
    curr, _ = Curriculum.objects.get_or_create(name="CBC", defaults={"description": "Competency Based Curriculum"})
    grade10, _ = Grade.objects.get_or_create(curriculum=curr, name="Grade 10", defaults={"level": 10})
    chem, _ = Subject.objects.get_or_create(grade=grade10, name="Chemistry", defaults={"description": "Chemistry Grade 10"})

    # Setup School 1 (VizLearn Academy North)
    school1, _ = School.objects.get_or_create(
        code="VIZ-NORTH-001",
        defaults={
            "name": "VizLearn Academy North",
            "owner": sadmin1,
            "contact_email": "admin1@northschool.co",
            "phone_number": "+254700000001",
            "address": "Nairobi North Campus",
        }
    )
    OrganizationMembership.objects.get_or_create(
        user=sadmin1, school=school1,
        defaults={"role": "school_admin", "state": "ACTIVE"}
    )
    OrganizationMembership.objects.get_or_create(
        user=teacher1, school=school1,
        defaults={"role": "teacher", "state": "ACTIVE"}
    )
    OrganizationMembership.objects.get_or_create(
        user=student1, school=school1,
        defaults={"role": "student", "state": "ACTIVE"}
    )
    now = timezone.now()
    SchoolSubscription.objects.get_or_create(
        school=school1,
        defaults={
            "plan": plan,
            "max_teachers": 5,
            "max_students": 100,
            "start_date": now - timedelta(days=1),
            "end_date": now + timedelta(days=364),
            "is_active": True,
        }
    )
    ay1, _ = AcademicYear.objects.get_or_create(
        school=school1, name="2026 Academic Year",
        defaults={"start_date": now.date(), "end_date": (now + timedelta(days=300)).date(), "is_current": True}
    )
    sclass1, _ = SchoolClass.objects.get_or_create(
        school=school1, name="Form 4", curriculum_grade=grade10,
        defaults={"code": "F4"}
    )
    stream1, _ = Stream.objects.get_or_create(
        school_class=sclass1, name="North",
        defaults={"class_teacher": teacher1}
    )
    TeacherSubjectAssignment.objects.get_or_create(
        teacher=teacher1, school=school1, subject=chem, academic_year=ay1
    )
    TeacherStreamAssignment.objects.get_or_create(
        teacher=teacher1, stream=stream1, subject=chem, academic_year=ay1
    )
    StudentEnrollment.objects.get_or_create(
        student=student1, stream=stream1, academic_year=ay1,
        defaults={"status": "active"}
    )

    # Setup School 2 (VizLearn Academy South)
    school2, _ = School.objects.get_or_create(
        code="VIZ-SOUTH-002",
        defaults={
            "name": "VizLearn Academy South",
            "owner": sadmin2,
            "contact_email": "admin2@southschool.co",
            "phone_number": "+254700000002",
            "address": "Nairobi South Campus",
        }
    )
    OrganizationMembership.objects.get_or_create(
        user=sadmin2, school=school2,
        defaults={"role": "school_admin", "state": "ACTIVE"}
    )
    SchoolSubscription.objects.get_or_create(
        school=school2,
        defaults={
            "plan": plan,
            "max_teachers": 2,
            "max_students": 50,
            "start_date": now - timedelta(days=1),
            "end_date": now + timedelta(days=364),
            "is_active": True,
        }
    )

    print("Successfully seeded ready-to-test accounts and environment!")

if __name__ == "__main__":
    seed_test_accounts()
