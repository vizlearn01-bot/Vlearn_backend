from django.core.management.base import BaseCommand
from django.utils import timezone
from subscriptions.models import Product, ProductVariant, AccessScope, Promotion
from curriculum.models import Grade, Subject


class Command(BaseCommand):
    help = "Seed M3.1 Commercial Products, Variants, Promotions, and Access Scopes"

    def handle(self, *args, **options):
        # Deactivate legacy demonstration variants safely (preserve financial records)
        legacy_slugs = ["form-4-monthly", "form-4-term", "form-4-annual", "chemistry-form-4-annual", "teacher-chemistry-annual"]
        ProductVariant.objects.filter(slug__in=legacy_slugs).update(is_active=False)

        # 1. Student Daily Access
        student_daily_prod, _ = Product.objects.update_or_create(
            slug="student-daily-access",
            defaults={
                "name": "Student Daily Access",
                "audience": "STUDENT",
                "description": "Daily access to subjects selected in student profile",
                "is_active": True,
            }
        )
        v_daily, _ = ProductVariant.objects.update_or_create(
            slug="daily-access",
            defaults={
                "product": student_daily_prod,
                "name": "Student Daily Access",
                "duration_type": "MONTHLY",
                "duration_days": 1,
                "price": 100.00,
                "currency": "KES",
                "is_active": True,
            }
        )
        AccessScope.objects.filter(product_variant=v_daily, scope_type="PLATFORM").delete()

        # 2. Student Monthly Access
        student_monthly_prod, _ = Product.objects.update_or_create(
            slug="student-monthly-access",
            defaults={
                "name": "Student Monthly Access",
                "audience": "STUDENT",
                "description": "Monthly access to subjects selected in student profile",
                "is_active": True,
            }
        )
        v_monthly, _ = ProductVariant.objects.update_or_create(
            slug="monthly-standard",
            defaults={
                "product": student_monthly_prod,
                "name": "Student Monthly Access",
                "duration_type": "MONTHLY",
                "duration_days": 30,
                "price": 2500.00,
                "currency": "KES",
                "is_active": True,
            }
        )
        AccessScope.objects.filter(product_variant=v_monthly, scope_type="PLATFORM").delete()

        # 3. Student Signup Promotion (KES 1,500 for first-time monthly purchase)
        Promotion.objects.update_or_create(
            code="SIGNUP_PROMO_1500",
            defaults={
                "name": "Student Signup Promotion",
                "product_variant": v_monthly,
                "promotional_price": 1500.00,
                "rule_type": "FIRST_PURCHASE",
                "max_redemptions_per_user": 1,
                "is_active": True,
            }
        )

        # 4. Teacher Premium Product
        teacher_prem_prod, _ = Product.objects.update_or_create(
            slug="teacher-premium",
            defaults={
                "name": "Teacher Premium",
                "audience": "TEACHER",
                "description": "Full access to teaching workspace and lesson delivery tools",
                "is_active": True,
            }
        )
        v_teacher_prem, _ = ProductVariant.objects.update_or_create(
            slug="teacher-premium-annual",
            defaults={
                "product": teacher_prem_prod,
                "name": "Teacher Premium Annual",
                "duration_type": "ANNUAL",
                "duration_days": 365,
                "price": 2500.00,
                "currency": "KES",
                "is_active": True,
            }
        )
        AccessScope.objects.get_or_create(product_variant=v_teacher_prem, scope_type="PLATFORM")
        AccessScope.objects.get_or_create(product_variant=v_teacher_prem, scope_type="FEATURE", feature_key="teacher_workspace")
        AccessScope.objects.get_or_create(product_variant=v_teacher_prem, scope_type="FEATURE", feature_key="lesson_delivery")

        # 5. School Subject Stream License
        school_prod, _ = Product.objects.update_or_create(
            slug="school-stream-license",
            defaults={
                "name": "School Subject Stream License",
                "audience": "SCHOOL",
                "description": "Per-subject, per-term stream-based institutional access",
                "is_active": True,
            }
        )
        v_school_term, _ = ProductVariant.objects.update_or_create(
            slug="school-license-term",
            defaults={
                "product": school_prod,
                "name": "School License Term",
                "duration_type": "TERM",
                "duration_days": 90,
                "price": 1000.00,
                "currency": "KES",
                "is_active": True,
                "metadata": {
                    "base_price_1_stream": 1000.00,
                    "price_per_additional_stream": 300.00,
                }
            }
        )
        AccessScope.objects.get_or_create(product_variant=v_school_term, scope_type="PLATFORM")

        self.stdout.write(self.style.SUCCESS("✓ Successfully seeded M3.1 Products, Variants, Promotions, and Scopes (Idempotent)!"))
