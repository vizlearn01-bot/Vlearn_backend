#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from subscriptions.models import SubscriptionPlan

# Clear existing plans if needed
# SubscriptionPlan.objects.all().delete()

# INDIVIDUALS PLANS
SubscriptionPlan.objects.create(
    plan_id="individual_daily",
    name="Individual - Daily",
    description="24-hour access to courses and quizzes",
    price=100.00,
    duration_days=1,
    details={"features": ["Courses", "Quizzes", "24-hour access"], "tier": "individual"}
)

SubscriptionPlan.objects.create(
    plan_id="individual_monthly",
    name="Individual - Monthly",
    description="Monthly access with progress tracking",
    price=1000.00,
    duration_days=30,
    details={"features": ["Courses", "Quizzes", "Experiment Videos", "Progress Tracking", "Personalized Learning"], "tier": "individual"}
)

SubscriptionPlan.objects.create(
    plan_id="individual_term",
    name="Individual - Per Term",
    description="12-week term access for students",
    price=2500.00,
    duration_days=84,
    details={"features": ["Courses", "Quizzes", "Experiment Videos", "Progress Tracking", "Personalized Learning", "Term-long Support"], "tier": "individual"}
)

SubscriptionPlan.objects.create(
    plan_id="individual_form_8subjects",
    name="Individual - Per Form (8 Subjects)",
    description="Full form access with all 8 subjects",
    price=3500.00,
    duration_days=270,
    details={"features": ["All 8 Subjects", "Courses", "Quizzes", "Simulations", "Progress Tracking", "Personalized Learning Path"], "tier": "individual"}
)

# SCHOOLS PLANS
SubscriptionPlan.objects.create(
    plan_id="school_per_subject",
    name="School - Per Subject",
    description="Single subject access for entire school",
    price=1300.00,
    duration_days=30,
    details={"features": ["Single Subject", "Multiple Users", "Student Progress Tracking", "Teacher Dashboard"], "tier": "school"}
)

SubscriptionPlan.objects.create(
    plan_id="school_per_term",
    name="School - Per Term",
    description="Full curriculum for one term",
    price=4000.00,
    duration_days=84,
    details={"features": ["All Subjects", "Multiple Users", "Student Progress Tracking", "Teacher Dashboard", "Bulk Admin"], "tier": "school"}
)

SubscriptionPlan.objects.create(
    plan_id="school_per_stream",
    name="School - Per Stream",
    description="Full access for an entire stream",
    price=6500.00,
    duration_days=270,
    details={"features": ["All Subjects", "Unlimited Users", "Advanced Analytics", "Student Progress Tracking", "Teacher Dashboard"], "tier": "school"}
)

print("✓ All subscription plans created successfully!")
print("\nPlans created:")
for plan in SubscriptionPlan.objects.all():
    print(f"  - {plan.name}: ${plan.price} for {plan.duration_days} days")
