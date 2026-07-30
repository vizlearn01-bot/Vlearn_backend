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
        self.curriculum = Curriculum.objects.create(name="844", code="844")
        self.grade_form4 = Grade.objects.create(name="Form 4", code="F4", curriculum=self.curriculum)
        self.subject_chem = Subject.objects.create(name="Chemistry", code="CHEM", grade=self.grade_form4)

        # Products & Variants
        self.student_prod = Product.objects.create(name="Student Form", slug="student-form", audience="STUDENT")
        self.variant_form4 = ProductVariant.objects.create(
            product=self.student_prod, name="Form 4 Annual", slug="f4-annual",
            duration_type="ANNUAL", duration_days=365, price=2500.00
        )
        self.scope_form4 = AccessScope.objects.create(
            product_variant=self.variant_form4, scope_type="GRADE", grade=self.grade_form4
        )

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
        invoice = Invoice.objects.create(invoice_number="INV12345")
        from billing_payment.models import InvoiceItem
        InvoiceItem.objects.create(invoice=invoice, name="Test Item", unit_price=1000.00, quantity=1)

        tx = InvoicePaymentTransaction.objects.create(
            transaction_id="TX12345",
            invoice=invoice,
            amount=1000.00,
            status="PENDING",
            transaction_details={"checkout_request_id": "REQ12345"}
        )

        # 1. Simulate partial payment callback (e.g. 500 KES instead of 1000 KES)
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
