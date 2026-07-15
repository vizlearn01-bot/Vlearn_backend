from django.core.management.base import BaseCommand
from subscriptions.models import SubscriptionPlan


class Command(BaseCommand):
    help = "Create default subscription plans for Vlearn"

    def handle(self, *args, **options):
        plans_data = [
            # INDIVIDUALS PLANS
            {
                "plan_id": "individual_daily",
                "name": "Individual - Daily",
                "description": "24-hour access to courses and quizzes",
                "price": 100.00,
                "duration_days": 1,
                "details": {
                    "features": ["Courses", "Quizzes", "24-hour access"],
                    "tier": "individual",
                },
            },
            {
                "plan_id": "individual_monthly",
                "name": "Individual - Monthly",
                "description": "Monthly access with progress tracking",
                "price": 1000.00,
                "duration_days": 30,
                "details": {
                    "features": [
                        "Courses",
                        "Quizzes",
                        "Experiment Videos",
                        "Progress Tracking",
                        "Personalized Learning",
                    ],
                    "tier": "individual",
                },
            },
            {
                "plan_id": "individual_term",
                "name": "Individual - Per Term",
                "description": "12-week term access for students",
                "price": 2500.00,
                "duration_days": 84,
                "details": {
                    "features": [
                        "Courses",
                        "Quizzes",
                        "Experiment Videos",
                        "Progress Tracking",
                        "Personalized Learning",
                        "Term-long Support",
                    ],
                    "tier": "individual",
                },
            },
            {
                "plan_id": "individual_form_8subjects",
                "name": "Individual - Per Form (8 Subjects)",
                "description": "Full form access with all 8 subjects",
                "price": 3500.00,
                "duration_days": 270,
                "details": {
                    "features": [
                        "All 8 Subjects",
                        "Courses",
                        "Quizzes",
                        "Simulations",
                        "Progress Tracking",
                        "Personalized Learning Path",
                    ],
                    "tier": "individual",
                },
            },
            # SCHOOLS PLANS
            {
                "plan_id": "school_per_subject",
                "name": "School - Per Subject",
                "description": "Single subject access for entire school",
                "price": 1300.00,
                "duration_days": 30,
                "details": {
                    "features": [
                        "Single Subject",
                        "Multiple Users",
                        "Student Progress Tracking",
                        "Teacher Dashboard",
                    ],
                    "tier": "school",
                },
            },
            {
                "plan_id": "school_per_term",
                "name": "School - Per Term",
                "description": "Full curriculum for one term",
                "price": 4000.00,
                "duration_days": 84,
                "details": {
                    "features": [
                        "All Subjects",
                        "Multiple Users",
                        "Student Progress Tracking",
                        "Teacher Dashboard",
                        "Bulk Admin",
                    ],
                    "tier": "school",
                },
            },
            {
                "plan_id": "school_per_stream",
                "name": "School - Per Stream",
                "description": "Full access for an entire stream",
                "price": 6500.00,
                "duration_days": 270,
                "details": {
                    "features": [
                        "All Subjects",
                        "Unlimited Users",
                        "Advanced Analytics",
                        "Student Progress Tracking",
                        "Teacher Dashboard",
                    ],
                    "tier": "school",
                },
            },
        ]

        created_count = 0
        for plan_data in plans_data:
            plan, created = SubscriptionPlan.objects.get_or_create(
                plan_id=plan_data["plan_id"], defaults=plan_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✓ Created: {plan.name} - {plan.price} for {plan.duration_days} days"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⚠ Already exists: {plan.name}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Subscription plans setup complete! ({created_count} new plans created)"
            )
        )
