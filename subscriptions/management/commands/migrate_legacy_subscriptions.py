from django.core.management.base import BaseCommand
from django.db import transaction
from subscriptions.models import Subscription, ProductVariant, SubscriptionSubject
from Resources.models import StudentSubjectSelection

class Command(BaseCommand):
    help = "Migrates legacy Subscription records (product_variant=NULL) to canonical M3.1 ProductVariants while preserving entitlement continuity."

    def handle(self, *args, **options):
        legacy_subs = Subscription.objects.filter(product_variant__isnull=True)
        count = legacy_subs.count()
        self.stdout.write(f"Found {count} legacy subscriptions to migrate.")

        daily_variant = ProductVariant.objects.filter(slug='daily-access', is_active=True).first()
        monthly_variant = ProductVariant.objects.filter(slug='monthly-standard', is_active=True).first()
        school_variant = ProductVariant.objects.filter(slug='school-license-term', is_active=True).first()

        migrated = 0
        with transaction.atomic():
            for sub in legacy_subs:
                plan = sub.plan
                target_variant = None

                if plan:
                    plan_name = plan.name.lower()
                    if 'daily' in plan_name:
                        target_variant = daily_variant
                    elif 'school' in plan_name:
                        target_variant = school_variant
                    else:
                        target_variant = monthly_variant

                if not target_variant:
                    target_variant = monthly_variant or daily_variant

                sub.product_variant = target_variant
                sub.save(update_fields=['product_variant'])

                if not sub.entitled_subjects.exists():
                    selections = StudentSubjectSelection.objects.filter(user=sub.user)
                    for sel in selections:
                        SubscriptionSubject.objects.get_or_create(
                            subscription=sub,
                            subject=sel.subject
                        )

                migrated += 1

        remaining = Subscription.objects.filter(product_variant__isnull=True).count()
        self.stdout.write(self.style.SUCCESS(f"Successfully migrated {migrated} subscriptions. Remaining legacy subs with product_variant=NULL: {remaining}"))
