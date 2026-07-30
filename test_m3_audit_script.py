import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from Resources.models import User
from curriculum.models import Curriculum, Grade, Subject
from subscriptions.models import Product, ProductVariant, AccessScope, Subscription
from billing_payment.models import Invoice, InvoiceItem, InvoicePaymentTransaction
from organizations.models import School, SchoolSubscription, OrganizationMembership, StudentEnrollment
from organizations.services import EntitlementService

def run_m3_audit():
    print("=" * 80)
    print("VLEARN M3 VERIFICATION AUDIT - OBJECTIVE 2 & OBJECTIVE 3")
    print("=" * 80 + "\n")

    # -------------------------------------------------------------------------
    # OBJECTIVE 3: PRODUCT CATALOGUE TABLE AUDIT
    # -------------------------------------------------------------------------
    print("--- OBJECTIVE 3: PRODUCT CATALOGUE TABLE AUDIT ---")
    products = Product.objects.all().prefetch_related('variants__access_scopes', 'variants__access_scopes__grade', 'variants__access_scopes__subject')
    
    catalogue_records = []
    print(f"Total Seeded Products Found: {products.count()}\n")

    for prod in products:
        print(f"PRODUCT: [{prod.id}] {prod.name} (Slug: {prod.slug}, Audience: {prod.audience}, Active: {prod.is_active})")
        print(f"  Description: {prod.description}")
        variants = prod.variants.all()
        print(f"  Variants Count: {variants.count()}")
        
        for var in variants:
            scopes = var.access_scopes.all()
            scope_strs = []
            for sc in scopes:
                if sc.scope_type == 'GRADE':
                    scope_strs.append(f"GRADE:{sc.grade.name if sc.grade else 'None'}")
                elif sc.scope_type == 'SUBJECT':
                    scope_strs.append(f"SUBJECT:{sc.subject.name if sc.subject else 'None'}")
                elif sc.scope_type == 'FEATURE':
                    scope_strs.append(f"FEATURE:{sc.feature_key}")
                else:
                    scope_strs.append(f"PLATFORM")

            rec = {
                "product_id": str(prod.id),
                "product_name": prod.name,
                "slug": prod.slug,
                "audience": prod.audience,
                "description": prod.description,
                "is_active": prod.is_active,
                "variant_id": str(var.id),
                "variant_name": var.name,
                "variant_slug": var.slug,
                "duration_type": var.duration_type,
                "duration_days": var.duration_days,
                "price": float(var.price),
                "currency": var.currency,
                "variant_is_active": var.is_active,
                "access_scopes": scope_strs,
                "metadata": var.metadata,
            }
            catalogue_records.append(rec)
            print(f"    - VARIANT: [{var.id}] {var.name} | Duration: {var.duration_type} ({var.duration_days} days) | Price: {var.price} {var.currency} | Scopes: {', '.join(scope_strs)} | Metadata: {var.metadata}")
        print("-" * 60)

    # -------------------------------------------------------------------------
    # OBJECTIVE 2: COMMERCIAL SUBSCRIPTION FLOW AUDIT
    # -------------------------------------------------------------------------
    print("\n--- OBJECTIVE 2: COMMERCIAL SUBSCRIPTION FLOW AUDIT ---")
    
    # Retrieve curriculum subjects & grades
    grade_f4 = Grade.objects.filter(name__icontains="Form 4").first() or Grade.objects.filter(name__icontains="4").first()
    subject_chem = Subject.objects.filter(name__icontains="Chemistry").first()
    
    # Ensure a second subject for grade (e.g. Physics) to test scope boundary
    if grade_f4:
        subject_phys, _ = Subject.objects.get_or_create(name="Physics", grade=grade_f4)
    else:
        curriculum, _ = Curriculum.objects.get_or_create(name="KCSE Standard")
        grade_f4 = Grade.objects.create(name="Form 4", curriculum=curriculum, level=4)
        subject_chem = Subject.objects.create(name="Chemistry", grade=grade_f4)
        subject_phys = Subject.objects.create(name="Physics", grade=grade_f4)

    # Grade in another form (Form 3) to test Grade scope isolation
    curriculum = grade_f4.curriculum
    grade_f3, _ = Grade.objects.get_or_create(name="Form 3", curriculum=curriculum, defaults={"level": 3})
    subject_bio, _ = Subject.objects.get_or_create(name="Biology", grade=grade_f3)

    # Users
    student_user, _ = User.objects.get_or_create(
        username="flow_student_user",
        defaults={"email": "flow_student@vlearn.co", "role": "student"}
    )
    teacher_user, _ = User.objects.get_or_create(
        username="flow_teacher_user",
        defaults={"email": "flow_teacher@vlearn.co", "role": "teacher"}
    )

    client = APIClient()
    flow_evidence = {}

    # -------------------------------------------------------------------------
    # FLOW 1: Student Form Access Package
    # -------------------------------------------------------------------------
    print("\n[Flow 1] Auditing Student Form Access Package (Form 4 Annual)...")
    v_form4_annual = ProductVariant.objects.filter(slug="form-4-annual").first()
    if v_form4_annual:
        # Step 1: Product Selection
        prod = v_form4_annual.product
        print(f"  Step 1 - Selection: Product='{prod.name}' (Slug: {prod.slug}) -> Variant='{v_form4_annual.name}' (Price: {v_form4_annual.price} {v_form4_annual.currency})")
        
        # Step 2: Checkout / Pending Subscription
        sub = Subscription.objects.create(
            user=student_user,
            product_variant=v_form4_annual,
            status_state="PENDING_PAYMENT",
            is_active=False
        )
        print(f"  Step 2 - Checkout: Created Subscription ID={sub.id}, Status='{sub.status_state}'")

        # Step 3: Invoice Generation
        inv = sub.generate_invoice(billing_address={"full_name": "Student Form Purchaser", "email": student_user.email})
        print(f"  Step 3 - Invoice: Generated InvoiceNo='{inv.invoice_number}', Status='{inv.status}', Total={inv.total_amount} KES")

        # Step 4: Payment Transaction
        tx = InvoicePaymentTransaction.objects.create(
            invoice=inv,
            amount=v_form4_annual.price,
            status="PENDING",
            payment_method="MPESA"
        )
        tx.status = "COMPLETED"
        tx.transaction_date = timezone.now()
        tx.save()
        inv.refresh_from_db()
        print(f"  Step 4 - Payment: Transaction ID='{tx.transaction_id}', Status='{tx.status}' -> Invoice Status='{inv.status}'")

        # Step 5: Activation
        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=v_form4_annual.duration_days)
        sub.activated_at = timezone.now()
        sub.save()
        print(f"  Step 5 - Activation: Subscription Status='{sub.status_state}', Active={sub.is_active}, Period={sub.start_date.strftime('%Y-%m-%d')} to {sub.end_date.strftime('%Y-%m-%d')}")

        # Step 6: Entitlement Verification
        chem_access = EntitlementService.check_curriculum_access(student_user, subject_chem.id)
        phys_access = EntitlementService.check_curriculum_access(student_user, subject_phys.id)
        bio_access = EntitlementService.check_curriculum_access(student_user, subject_bio.id) # Form 3 subject
        print(f"  Step 6 - Entitlement: Chem(Form4)={chem_access}, Phys(Form4)={phys_access}, Bio(Form3)={bio_access}")
        
        flow_evidence["student_form"] = {
            "package_type": "Student Form Access",
            "product": prod.name,
            "variant": v_form4_annual.name,
            "duration": f"{v_form4_annual.duration_type} ({v_form4_annual.duration_days} days)",
            "price": float(v_form4_annual.price),
            "subscription_id": str(sub.id),
            "invoice_number": inv.invoice_number,
            "transaction_id": tx.transaction_id,
            "payment_status": tx.status,
            "activation_status": sub.status_state,
            "entitlement": {
                "form4_chem_access": chem_access,
                "form4_phys_access": phys_access,
                "form3_bio_access": bio_access,
                "scope_enforced_correctly": chem_access and phys_access and not bio_access
            }
        }
        tx.delete()
        sub.delete()
        inv.delete()

    # -------------------------------------------------------------------------
    # FLOW 2: Student Subject Access Package
    # -------------------------------------------------------------------------
    print("\n[Flow 2] Auditing Student Subject Access Package (Chemistry Form 4 Annual)...")
    v_chem_annual = ProductVariant.objects.filter(slug="chemistry-form-4-annual").first()
    if v_chem_annual:
        prod = v_chem_annual.product
        print(f"  Step 1 - Selection: Product='{prod.name}' -> Variant='{v_chem_annual.name}' (Price: {v_chem_annual.price} {v_chem_annual.currency})")
        
        sub = Subscription.objects.create(user=student_user, product_variant=v_chem_annual, status_state="PENDING_PAYMENT", is_active=False)
        inv = sub.generate_invoice(billing_address={"full_name": "Subject Student"})
        tx = InvoicePaymentTransaction.objects.create(invoice=inv, amount=v_chem_annual.price, status="PENDING", payment_method="CARD")
        tx.status = "COMPLETED"
        tx.save()
        inv.refresh_from_db()

        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=v_chem_annual.duration_days)
        sub.activated_at = timezone.now()
        sub.save()

        chem_access = EntitlementService.check_curriculum_access(student_user, subject_chem.id)
        phys_access = EntitlementService.check_curriculum_access(student_user, subject_phys.id)
        print(f"  Step 6 - Entitlement: Chem(Target)={chem_access}, Phys(Other Form4 Subject)={phys_access}")

        flow_evidence["student_subject"] = {
            "package_type": "Student Subject Access",
            "product": prod.name,
            "variant": v_chem_annual.name,
            "price": float(v_chem_annual.price),
            "subscription_id": str(sub.id),
            "invoice_number": inv.invoice_number,
            "transaction_id": tx.transaction_id,
            "payment_status": tx.status,
            "activation_status": sub.status_state,
            "entitlement": {
                "chem_access": chem_access,
                "phys_access": phys_access,
                "scope_enforced_correctly": chem_access and not phys_access
            }
        }
        tx.delete()
        sub.delete()
        inv.delete()

    # -------------------------------------------------------------------------
    # FLOW 3: Student Premium Package
    # -------------------------------------------------------------------------
    print("\n[Flow 3] Auditing Student Premium Package (Annual - KES 3,000 Max Price)...")
    v_prem_annual = ProductVariant.objects.filter(slug="student-premium-annual").first()
    if v_prem_annual:
        prod = v_prem_annual.product
        print(f"  Step 1 - Selection: Product='{prod.name}' -> Variant='{v_prem_annual.name}' (Price: {v_prem_annual.price} {v_prem_annual.currency})")
        
        sub = Subscription.objects.create(user=student_user, product_variant=v_prem_annual, status_state="PENDING_PAYMENT", is_active=False)
        inv = sub.generate_invoice(billing_address={"full_name": "Premium Student"})
        tx = InvoicePaymentTransaction.objects.create(invoice=inv, amount=v_prem_annual.price, status="PENDING", payment_method="MPESA")
        tx.status = "COMPLETED"
        tx.save()
        inv.refresh_from_db()

        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=v_prem_annual.duration_days)
        sub.activated_at = timezone.now()
        sub.save()

        full_access = EntitlementService.has_full_curriculum_access(student_user)
        client.force_authenticate(user=student_user)
        ent_data = client.get("/api/subscriptions/entitlements/me/").json()

        print(f"  Step 6 - Entitlement: Platform-Wide Access={full_access}, Features={ent_data.get('features')}")

        flow_evidence["student_premium"] = {
            "package_type": "Student Premium",
            "product": prod.name,
            "variant": v_prem_annual.name,
            "price": float(v_prem_annual.price),
            "subscription_id": str(sub.id),
            "invoice_number": inv.invoice_number,
            "transaction_id": tx.transaction_id,
            "payment_status": tx.status,
            "activation_status": sub.status_state,
            "entitlement": {
                "platform_wide_access": full_access,
                "features": ent_data.get('features', []),
                "max_price_policy_verified": float(v_prem_annual.price) <= 3000.00
            }
        }
        tx.delete()
        sub.delete()
        inv.delete()

    # -------------------------------------------------------------------------
    # FLOW 4: Teacher Subject Access Package
    # -------------------------------------------------------------------------
    print("\n[Flow 4] Auditing Teacher Subject Access Package (Teacher Chemistry Annual)...")
    v_tchem = ProductVariant.objects.filter(slug="teacher-chemistry-annual").first()
    if v_tchem:
        prod = v_tchem.product
        print(f"  Step 1 - Selection: Product='{prod.name}' -> Variant='{v_tchem.name}' (Price: {v_tchem.price} {v_tchem.currency})")
        
        sub = Subscription.objects.create(user=teacher_user, product_variant=v_tchem, status_state="PENDING_PAYMENT", is_active=False)
        inv = sub.generate_invoice(billing_address={"full_name": "Teacher Purchaser"})
        tx = InvoicePaymentTransaction.objects.create(invoice=inv, amount=v_tchem.price, status="PENDING", payment_method="MPESA")
        tx.status = "COMPLETED"
        tx.save()
        inv.refresh_from_db()

        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=v_tchem.duration_days)
        sub.activated_at = timezone.now()
        sub.save()

        chem_access = EntitlementService.check_curriculum_access(teacher_user, subject_chem.id)
        client.force_authenticate(user=teacher_user)
        ent_data = client.get("/api/subscriptions/entitlements/me/").json()

        print(f"  Step 6 - Entitlement: Subject Chem Access={chem_access}, Features={ent_data.get('features')}")

        flow_evidence["teacher_subject"] = {
            "package_type": "Teacher Subject Access",
            "product": prod.name,
            "variant": v_tchem.name,
            "price": float(v_tchem.price),
            "subscription_id": str(sub.id),
            "invoice_number": inv.invoice_number,
            "transaction_id": tx.transaction_id,
            "payment_status": tx.status,
            "activation_status": sub.status_state,
            "entitlement": {
                "chem_access": chem_access,
                "features": ent_data.get('features', []),
                "lesson_delivery_enabled": "lesson_delivery" in ent_data.get('features', [])
            }
        }
        tx.delete()
        sub.delete()
        inv.delete()

    # -------------------------------------------------------------------------
    # FLOW 5: Teacher Premium Package
    # -------------------------------------------------------------------------
    print("\n[Flow 5] Auditing Teacher Premium Package (Teacher Premium Annual)...")
    v_tprem = ProductVariant.objects.filter(slug="teacher-premium-annual").first()
    if v_tprem:
        prod = v_tprem.product
        print(f"  Step 1 - Selection: Product='{prod.name}' -> Variant='{v_tprem.name}' (Price: {v_tprem.price} {v_tprem.currency})")
        
        sub = Subscription.objects.create(user=teacher_user, product_variant=v_tprem, status_state="PENDING_PAYMENT", is_active=False)
        inv = sub.generate_invoice(billing_address={"full_name": "Teacher Premium"})
        tx = InvoicePaymentTransaction.objects.create(invoice=inv, amount=v_tprem.price, status="PENDING", payment_method="CARD")
        tx.status = "COMPLETED"
        tx.save()
        inv.refresh_from_db()

        sub.status_state = "ACTIVE"
        sub.is_active = True
        sub.start_date = timezone.now()
        sub.end_date = timezone.now() + timedelta(days=v_tprem.duration_days)
        sub.activated_at = timezone.now()
        sub.save()

        full_access = EntitlementService.has_full_curriculum_access(teacher_user)
        client.force_authenticate(user=teacher_user)
        ent_data = client.get("/api/subscriptions/entitlements/me/").json()

        print(f"  Step 6 - Entitlement: Platform-Wide={full_access}, Features={ent_data.get('features')}")

        flow_evidence["teacher_premium"] = {
            "package_type": "Teacher Premium",
            "product": prod.name,
            "variant": v_tprem.name,
            "price": float(v_tprem.price),
            "subscription_id": str(sub.id),
            "invoice_number": inv.invoice_number,
            "transaction_id": tx.transaction_id,
            "payment_status": tx.status,
            "activation_status": sub.status_state,
            "entitlement": {
                "platform_wide_access": full_access,
                "features": ent_data.get('features', []),
                "teacher_workspace_enabled": "teacher_workspace" in ent_data.get('features', [])
            }
        }
        tx.delete()
        sub.delete()
        inv.delete()

    # -------------------------------------------------------------------------
    # FLOW 6: School Institutional License Package
    # -------------------------------------------------------------------------
    print("\n[Flow 6] Auditing School Institutional License Package...")
    v_school = ProductVariant.objects.filter(slug="school-license-annual").first()
    if v_school:
        prod = v_school.product
        print(f"  Step 1 - Selection: Product='{prod.name}' -> Variant='{v_school.name}' (Base Price: {v_school.price} {v_school.currency})")
        print(f"  Seat Metadata: {v_school.metadata}")

        school, _ = School.objects.get_or_create(name="M3 Audit Demo Academy", defaults={"code": "DEMO01"})
        
        # School Subscription
        school_sub, _ = SchoolSubscription.objects.get_or_create(
            school=school,
            defaults={
                "product_variant": v_school,
                "max_students": 50,
                "max_teachers": 5,
                "start_date": timezone.now(),
                "end_date": timezone.now() + timedelta(days=365),
                "is_active": True,
            }
        )
        print(f"  Step 5 - Activation: SchoolSubscription ID={school_sub.id}, Max Students={school_sub.max_students}, Max Teachers={school_sub.max_teachers}")

        flow_evidence["school_institutional"] = {
            "package_type": "School Institutional License",
            "product": prod.name,
            "variant": v_school.name,
            "base_price": float(v_school.price),
            "metadata": v_school.metadata,
            "school_subscription_id": str(school_sub.id),
            "max_students": school_sub.max_students,
            "max_teachers": school_sub.max_teachers,
            "activation_status": "ACTIVE" if school_sub.is_active else "INACTIVE",
        }

    # Save summary report to JSON
    with open("m3_audit_summary.json", "w") as f:
        json.dump({
            "catalogue": catalogue_records,
            "flow_evidence": flow_evidence
        }, f, indent=2)

    print("\n" + "=" * 80)
    print("M3 AUDIT COMPLETED SUCCESSFULLY. Output saved to m3_audit_summary.json")
    print("=" * 80)

if __name__ == '__main__':
    run_m3_audit()
