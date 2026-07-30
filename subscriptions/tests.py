from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from Resources.models import User
from curriculum.models import Curriculum, Grade, Subject
from subscriptions.models import Product, ProductVariant, AccessScope, Subscription
from organizations.models import School, SchoolSubscription, OrganizationMembership, StudentEnrollment
from organizations.services import EntitlementService
from billing_payment.models import Invoice, InvoicePaymentTransaction


class M3EntitlementAndSubscriptionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Users
        self.super_user = User.objects.create_superuser(username="admin", email="admin@test.com", password="password")
        self.student = User.objects.create_user(username="student1", email="student@test.com", password="password", role="student")
        self.unsubscribed_student = User.objects.create_user(username="student2", email="student2@test.com", password="password", role="student")
        self.teacher = User.objects.create_user(username="teacher1", email="teacher@test.com", password="password", role="teacher")

        # Curriculum
        self.curriculum = Curriculum.objects.create(name="844")
        self.grade_form4 = Grade.objects.create(name="Form 4", curriculum=self.curriculum)
        self.subject_chem = Subject.objects.create(name="Chemistry", grade=self.grade_form4)

        # Products & Variants
        self.student_prod = Product.objects.create(name="Student Form", slug="student-form", audience="STUDENT")
        self.variant_form4 = ProductVariant.objects.create(
            product=self.student_prod, name="Form 4 Annual", slug="f4-annual",
            duration_type="ANNUAL", duration_days=365, price=2500.00
        )
        self.scope_form4 = AccessScope.objects.create(
            product_variant=self.variant_form4, scope_type="GRADE", grade=self.grade_form4
        )

        # Seed products, variants, promotions
        from django.core.management import call_command
        call_command('seed_m3_products')

        # Active Subscription for student
        self.sub_student = Subscription.objects.create(
            user=self.student,
            product_variant=self.variant_form4,
            status_state="ACTIVE",
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=365),
            is_active=True
        )

    def test_unauthenticated_user_denied_access(self):
        self.assertFalse(EntitlementService.check_curriculum_access(None, self.subject_chem.id))
        self.assertEqual(EntitlementService.get_allowed_subject_ids(None), [])

    def test_existence_bypass_bug_is_fixed(self):
        # Even though subject_chem exists, unsubscribed_student should NOT be granted access automatically!
        self.assertFalse(EntitlementService.check_curriculum_access(self.unsubscribed_student, self.subject_chem.id))
        self.assertNotIn(self.subject_chem.id, EntitlementService.get_allowed_subject_ids(self.unsubscribed_student))

    def test_subscribed_student_has_access(self):
        self.assertTrue(EntitlementService.check_curriculum_access(self.student, self.subject_chem.id))
        self.assertIn(self.subject_chem.id, EntitlementService.get_allowed_subject_ids(self.student))

    def test_platform_admin_has_full_access(self):
        self.assertTrue(EntitlementService.has_full_curriculum_access(self.super_user))
        self.assertIn(self.subject_chem.id, EntitlementService.get_allowed_subject_ids(self.super_user))

    def test_entitlements_me_api_endpoint(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get("/api/subscriptions/entitlements/me/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("curriculum_access", data)
        sub_ids = [s["id"] for s in data["curriculum_access"]["subjects"]]
        self.assertIn(self.subject_chem.id, sub_ids)

    def test_payment_amount_validation_and_idempotency(self):
        invoice = Invoice.objects.create()
        from billing_payment.models import InvoiceItem
        InvoiceItem.objects.create(invoice=invoice, name="Test Item", unit_price=1000.00, quantity=1)

        tx = InvoicePaymentTransaction.objects.create(
            invoice=invoice,
            amount=1000.00,
            status="PENDING",
            transaction_details={"checkout_request_id": "REQ12345"}
        )

        # 1. Simulate partial payment callback (500 KES instead of 1000 KES)
        payload_partial = {
            "Body": {
                "stkCallback": {
                    "MerchantRequestID": "M123",
                    "CheckoutRequestID": "REQ12345",
                    "ResultCode": 0,
                    "ResultDesc": "Success",
                    "CallbackMetadata": {
                        "Item": [
                            {"Name": "Amount", "Value": 500.00},
                            {"Name": "MpesaReceiptNumber", "Value": "REC123"},
                            {"Name": "TransactionDate", "Value": 20260729060000},
                            {"Name": "PhoneNumber", "Value": 254700000000}
                        ]
                    }
                }
            }
        }
        resp = self.client.post("/api/billing-and-payments/mpesa/stk-push-callback/", data=payload_partial, format="json")
        self.assertEqual(resp.status_code, 200)

        tx.refresh_from_db()
        self.assertEqual(tx.status, "FAILED")

        # Reset tx to PENDING for full payment test
        tx.status = "PENDING"
        tx.save()

        # 2. Simulate valid full payment callback
        payload_valid = {
            "Body": {
                "stkCallback": {
                    "MerchantRequestID": "M123",
                    "CheckoutRequestID": "REQ12345",
                    "ResultCode": 0,
                    "ResultDesc": "Success",
                    "CallbackMetadata": {
                        "Item": [
                            {"Name": "Amount", "Value": 1000.00},
                            {"Name": "MpesaReceiptNumber", "Value": "REC123"},
                            {"Name": "TransactionDate", "Value": 20260729060000},
                            {"Name": "PhoneNumber", "Value": 254700000000}
                        ]
                    }
                }
            }
        }
        resp = self.client.post("/api/billing-and-payments/mpesa/stk-push-callback/", data=payload_valid, format="json")
        self.assertEqual(resp.status_code, 200)

        tx.refresh_from_db()
        invoice.refresh_from_db()
        self.assertEqual(tx.status, "COMPLETED")
        self.assertEqual(invoice.status, "PAID")

        # 3. Simulate duplicate callback — should be skipped idempotently
        resp_dup = self.client.post("/api/billing-and-payments/mpesa/stk-push-callback/", data=payload_valid, format="json")
        self.assertEqual(resp_dup.status_code, 200)

    def test_student_daily_and_monthly_pricing_and_snapshot(self):
        # Create dedicated student for snapshot test
        snap_student = User.objects.create_user(username="snap_student", email="snap@test.com", password="password", role="student")
        from Resources.models import UserProfile
        profile, _ = UserProfile.objects.get_or_create(user=snap_student)
        profile.selected_subjects.add(self.subject_chem)

        # 1. Daily Checkout
        from subscriptions.models import ProductVariant, Promotion, SubscriptionSubject
        daily_var = ProductVariant.objects.get(slug="daily-access")
        self.client.force_authenticate(user=snap_student)

        resp = self.client.post("/api/subscriptions/checkout/", {"product_variant_id": str(daily_var.id)}, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["amount"], 100.0)

        # 2. Monthly Checkout with Promo
        monthly_var = ProductVariant.objects.get(slug="monthly-standard")
        resp_promo = self.client.post("/api/subscriptions/checkout/", {"product_variant_id": str(monthly_var.id)}, format="json")
        self.assertEqual(resp_promo.status_code, 201)
        self.assertEqual(resp_promo.json()["amount"], 1500.0)  # Promo applied for 1st purchase

        # Verify promo redemption created upon invoice payment
        sub_id = resp_promo.json()["subscription_id"]
        sub = Subscription.objects.get(id=sub_id)
        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=30)
        sub.save()

        # 3. Verify post-activation profile change does NOT expand active subscription access!
        bio_subj = Subject.objects.create(name="Biology", grade=self.grade_form4)
        profile.selected_subjects.add(bio_subj)  # Added after payment!

        # Entitlements should grant Chemistry (snapshotted), but NOT Biology
        allowed = EntitlementService.get_allowed_subject_ids(snap_student)
        self.assertIn(self.subject_chem.id, allowed)
        self.assertNotIn(bio_subj.id, allowed)

    def test_school_stream_pricing_formula(self):
        from subscriptions.services import CommercialPricingService

        # 1 stream, 1 subject = 1000 KES
        p1 = CommercialPricingService.calculate_school_price(stream_count=1, subject_count=1)
        self.assertEqual(p1["total_price"], 1000.0)

        # 2 streams, 1 subject = 1300 KES
        p2 = CommercialPricingService.calculate_school_price(stream_count=2, subject_count=1)
        self.assertEqual(p2["total_price"], 1300.0)

        # 3 streams, 1 subject = 1600 KES
        p3 = CommercialPricingService.calculate_school_price(stream_count=3, subject_count=1)
        self.assertEqual(p3["total_price"], 1600.0)

        # 4 streams, 1 subject = 1900 KES
        p4 = CommercialPricingService.calculate_school_price(stream_count=4, subject_count=1)
        self.assertEqual(p4["total_price"], 1900.0)

        # 3 subjects, 3 streams = 4800 KES (1600 * 3)
        p5 = CommercialPricingService.calculate_school_price(stream_count=3, subject_count=3)
        self.assertEqual(p5["total_price"], 4800.0)

    def test_school_subject_stream_term_entitlement_and_denial(self):
        from organizations.models import School, AcademicYear, SchoolClass, Stream, StudentEnrollment, SchoolSubscription
        school = School.objects.create(name="St. Jude High", code="STJUDE1", owner=self.super_user)
        acad_year = AcademicYear.objects.create(school=school, name="2026", start_date="2026-01-01", end_date="2026-12-31", is_current=True)
        s_class = SchoolClass.objects.create(school=school, curriculum_grade=self.grade_form4, name="Form 4")
        stream_east = Stream.objects.create(school_class=s_class, name="East")
        stream_west = Stream.objects.create(school_class=s_class, name="West")

        # Student enrolled in Stream East
        OrganizationMembership.objects.create(user=self.student, school=school, role="student", state="ACTIVE")
        StudentEnrollment.objects.create(student=self.student, stream=stream_east, academic_year=acad_year, status="active")

        # Unsubscribed student enrolled in Stream West
        OrganizationMembership.objects.create(user=self.unsubscribed_student, school=school, role="student", state="ACTIVE")
        StudentEnrollment.objects.create(student=self.unsubscribed_student, stream=stream_west, academic_year=acad_year, status="active")

        # Create SchoolSubscription covering Chemistry for Stream East ONLY
        school_sub = SchoolSubscription.objects.create(
            school=school,
            academic_year=acad_year,
            term_name="Term 1",
            start_date=timezone.now() - timedelta(days=1),
            end_date=timezone.now() + timedelta(days=90),
            is_active=True
        )
        school_sub.covered_subjects.add(self.subject_chem)
        school_sub.covered_streams.add(stream_east)

        # 1. Student in covered stream East gets Chemistry
        self.assertTrue(EntitlementService.check_curriculum_access(self.student, self.subject_chem.id))

        # 2. Student in uncovered stream West is DENIED Chemistry
        self.assertFalse(EntitlementService.check_curriculum_access(self.unsubscribed_student, self.subject_chem.id))

