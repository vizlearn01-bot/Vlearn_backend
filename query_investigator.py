import os
import sys
import time
import json

os.environ['DJANGO_SETTINGS_MODULE'] = 'Nexus_backend.settings'
os.environ['DATABASE_URL'] = 'postgres://postgres:vlearn_secret@localhost:5433/vlearn_validation_db'
os.environ['DEBUG'] = 'True'

import django
django.setup()

from django.conf import settings
settings.ALLOWED_HOSTS = ['*']

from django.db import connection, reset_queries
from django.test import RequestFactory
from rest_framework.test import APIClient

from Resources.models import User, UserProfile, VideoInteraction, UploadedFile, ExperimentVideo, Category, Invitation
from Questions.models import Quiz, Question, Answer, QuestionAttempt, StudentAnswer
from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, KnowledgePack, Simulation
from organizations.models import School, OrganizationMembership, AcademicYear, SchoolClass, Stream, TeacherSubjectAssignment, StudentEnrollment, SchoolSubscription
from subscriptions.models import SubscriptionPlan, Subscription
from billing_payment.models import Invoice, InvoiceItem, InvoicePaymentTransaction

def get_db_queries():
    return list(connection.queries)

def clear_db_queries():
    reset_queries()

print("================================================================================")
print("VLEARN PHASE 1.3 QUERY & INDEX INVESTIGATION ON POSTGRESQL 16")
print("================================================================================")

client = APIClient()

# Ensure we have a set of baseline populated objects for N+1 detection
admin_user = User.objects.filter(role="platform_admin").first()
if not admin_user:
    admin_user = User.objects.create_superuser(username="investigator_admin", email="admin@vlearn.co", password="Password123!")

client.force_authenticate(user=admin_user)

# Seed dataset if count is low for N+1 scaling tests
print("\n--- Seeding bulk test dataset for N+1 query scaling tests ---")

curr, _ = Curriculum.objects.get_or_create(name="CBC Test", defaults={"description": "CBC Test"})
grade, _ = Grade.objects.get_or_create(curriculum=curr, name="Grade 10 Test", defaults={"level": 10})
subject, _ = Subject.objects.get_or_create(grade=grade, name="Physics Test")
topic, _ = Topic.objects.get_or_create(subject=subject, name="Kinematics Test")
video, _ = ExperimentVideo.objects.get_or_create(title="Kinematics Video Test", defaults={"difficulty": "Beginner"})

for i in range(10):
    quiz, _ = Quiz.objects.get_or_create(title=f"Quiz N+1 Test {i}", video=video, defaults={"time_limit": 15})
    for q_idx in range(3):
        q, _ = Question.objects.get_or_create(quiz=quiz, text=f"Question {q_idx} for Quiz {i}", defaults={"points": 5})
        for a_idx in range(4):
            Answer.objects.get_or_create(question=q, text=f"Option {a_idx} for Q{q_idx} Qz{i}", defaults={"is_correct": (a_idx==0)})

users = []
for i in range(10):
    u, _ = User.objects.get_or_create(username=f"student_n1_{i}", defaults={"email": f"student_n1_{i}@vlearn.co", "role": "student"})
    users.append(u)
    p, _ = UserProfile.objects.get_or_create(user=u, defaults={"school": f"School {i}", "grade": "Grade 10"})
    VideoInteraction.objects.get_or_create(user=u, video_url=f"https://video.com/{i}", defaults={"watched_duration": 100})

for i in range(5):
    sch, _ = School.objects.get_or_create(name=f"School Bulk {i}", code=f"SCH{i:03d}")
    ac_year, _ = AcademicYear.objects.get_or_create(school=sch, name="2026", defaults={"start_date": "2026-01-01", "end_date": "2026-12-31", "is_current": True})
    cls, _ = SchoolClass.objects.get_or_create(school=sch, curriculum_grade=grade, name=f"Form {i}")
    st, _ = Stream.objects.get_or_create(school_class=cls, name=f"East {i}")
    
    u = users[i]
    OrganizationMembership.objects.get_or_create(user=u, school=sch, defaults={"role": "student"})
    StudentEnrollment.objects.get_or_create(student=u, stream=st, academic_year=ac_year, defaults={"status": "active"})

plan, _ = SubscriptionPlan.objects.get_or_create(plan_id="plan_n1_test", defaults={"name": "Plan N1", "price": 100.0, "duration_days": 30})
for i in range(5):
    Subscription.objects.get_or_create(user=users[i], plan=plan, defaults={"is_active": True})

for i in range(5):
    inv, _ = Invoice.objects.get_or_create(invoice_number=f"INV-N1-{i:04d}", defaults={"user_to": users[i], "status": "PENDING"})
    for j in range(3):
        InvoiceItem.objects.get_or_create(invoice=inv, description=f"Item {j} for Inv {i}", defaults={"name": f"Item {j}", "unit_price": 50.0, "quantity": 1})
    InvoicePaymentTransaction.objects.get_or_create(invoice=inv, transaction_id=f"TXN-N1-{i:04d}", defaults={"amount": 150.0, "status": "COMPLETED"})

print("Bulk test dataset successfully seeded.")

# ==============================================================================
# SECTION 1: CATALOG INDEX ANALYSIS (pg_indexes & PostgreSQL catalog)
# ==============================================================================
print("\n" + "="*80)
print("SECTION 1: POSTGRESQL CATALOG INDEX COVERAGE AUDIT")
print("="*80)

cursor = connection.cursor()

cursor.execute("""
SELECT tablename, indexname, indexdef 
FROM pg_indexes 
WHERE schemaname = 'public' 
ORDER BY tablename, indexname;
""")
all_indexes = cursor.fetchall()
print(f"Total indexes in public schema: {len(all_indexes)}")

cursor.execute("""
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name,
    tc.constraint_name,
    EXISTS (
        SELECT 1
        FROM pg_index i
        JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        JOIN pg_class c ON c.oid = i.indrelid
        JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE n.nspname = 'public'
          AND c.relname = tc.table_name
          AND a.attname = kcu.column_name
    ) AS is_indexed
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
      AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
      AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_schema='public'
ORDER BY tc.table_name, kcu.column_name;
""")
fk_coverage = cursor.fetchall()
unindexed_fks = [fk for fk in fk_coverage if not fk[5]]
print(f"FK constraints: Total = {len(fk_coverage)}, Unindexed = {len(unindexed_fks)}")

filter_columns_to_check = [
    ("Resources_user", ["username", "email", "role", "is_active"]),
    ("Resources_videointeraction", ["user_id", "is_completed", "video_url"]),
    ("Resources_uploadedfile", ["file_type", "created_at"]),
    ("Questions_quiz", ["video_id", "created_at"]),
    ("Questions_question", ["quiz_id", "question_type"]),
    ("Questions_questionattempt", ["user_id", "quiz_id", "is_completed"]),
    ("Questions_studentanswer", ["attempt_id", "question_id"]),
    ("curriculum_curriculum", ["name"]),
    ("curriculum_grade", ["curriculum_id", "level"]),
    ("curriculum_subject", ["grade_id"]),
    ("curriculum_topic", ["subject_id"]),
    ("curriculum_lesson", ["topic_id", "knowledge_pack_id", "status"]),
    ("curriculum_lessonblock", ["lesson_id", "order"]),
    ("curriculum_simulation", ["key", "status", "domain"]),
    ("organizations_school", ["code", "name"]),
    ("organizations_organizationmembership", ["user_id", "school_id", "role", "is_active"]),
    ("organizations_schoolclass", ["school_id", "academic_year_id", "grade_id"]),
    ("organizations_stream", ["school_class_id"]),
    ("organizations_studentenrollment", ["student_id", "school_class_id", "stream_id", "status"]),
    ("subscriptions_subscription", ["user_id", "plan_id", "status", "start_date", "end_date"]),
    ("billing_payment_invoice", ["invoice_number", "user_id", "status", "created_at"]),
    ("billing_payment_invoiceitem", ["invoice_id"]),
    ("billing_payment_invoicepaymenttransaction", ["invoice_id", "transaction_id", "status"]),
]

column_index_status = []
for table, cols in filter_columns_to_check:
    for col in cols:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM pg_index i
                JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
                JOIN pg_class c ON c.oid = i.indrelid
                JOIN pg_namespace n ON n.oid = c.relnamespace
                WHERE n.nspname = 'public'
                  AND c.relname = %s
                  AND a.attname = %s
            );
        """, [table, col])
        is_ind = cursor.fetchone()[0]
        column_index_status.append({"table": table, "column": col, "indexed": is_ind})

print(f"Filter/Lookup columns audited: {len(column_index_status)}")
unindexed_filter_cols = [c for c in column_index_status if not c["indexed"]]
print(f"Unindexed filter/lookup columns count: {len(unindexed_filter_cols)}")
for uc in unindexed_filter_cols:
    print(f"  Unindexed: {uc['table']}.{uc['column']}")

# ==============================================================================
# SECTION 2: ENDPOINT & VIEW WORKFLOW QUERY TRACING
# ==============================================================================
print("\n" + "="*80)
print("SECTION 2: FUNCTIONAL WORKFLOW QUERY TRACING ACROSS ALL 6 APPS")
print("="*80)

workflow_results = []

def test_endpoint(app_name, scenario_name, method, url, data=None):
    clear_db_queries()
    start_time = time.time()
    if method == "GET":
        resp = client.get(url)
    elif method == "POST":
        resp = client.post(url, data=data, format='json')
    elapsed_ms = (time.time() - start_time) * 1000
    
    queries = get_db_queries()
    query_count = len(queries)
    db_time_ms = sum(float(q.get('time', 0)) * 1000 for q in queries)
    sql_statements = [q['sql'] for q in queries]
    unique_sqls = set(sql_statements)
    duplicate_count = len(sql_statements) - len(unique_sqls)
    
    result = {
        "app": app_name,
        "scenario": scenario_name,
        "method": method,
        "url": url,
        "status_code": resp.status_code,
        "query_count": query_count,
        "db_time_ms": round(db_time_ms, 3),
        "total_time_ms": round(elapsed_ms, 3),
        "duplicate_queries": duplicate_count,
        "sql_statements": sql_statements
    }
    workflow_results.append(result)
    print(f"[{app_name}] {scenario_name} ({method} {url}): Status {resp.status_code} | Queries: {query_count} | DB Time: {db_time_ms:.2f}ms | Duplicates: {duplicate_count}")
    return result, resp

# --- APP 1: Resources ---
test_endpoint("Resources", "List Files", "GET", "/files/")
test_endpoint("Resources", "List Experiment Videos", "GET", "/experiment_videos/")
test_endpoint("Resources", "List Video Interactions", "GET", "/video_interactions/")
test_endpoint("Resources", "User Profile Detail", "GET", "/profile/")
test_endpoint("Resources", "List Categories", "GET", "/categories/")
test_endpoint("Resources", "List Invitations", "GET", "/invitations/")

# --- APP 2: Questions ---
test_endpoint("Questions", "List Quizzes", "GET", "/questions/quizzes/")
quiz_first = Quiz.objects.first()
if quiz_first:
    test_endpoint("Questions", "Quiz Detail", "GET", f"/questions/quizzes/{quiz_first.id}/")
test_endpoint("Questions", "List Question Attempts", "GET", "/questions/attempts/")

# --- APP 3: curriculum ---
test_endpoint("curriculum", "List Curricula", "GET", "/api/curriculum/curricula/")
test_endpoint("curriculum", "List Grades", "GET", "/api/curriculum/grades/")
test_endpoint("curriculum", "List Subjects", "GET", "/api/curriculum/subjects/")
test_endpoint("curriculum", "List Topics", "GET", "/api/curriculum/topics/")
test_endpoint("curriculum", "List Lessons", "GET", "/api/curriculum/lessons/")
test_endpoint("curriculum", "List Lesson Blocks", "GET", "/api/curriculum/lesson-blocks/")
test_endpoint("curriculum", "List Knowledge Packs", "GET", "/api/curriculum/knowledge-packs/")
test_endpoint("curriculum", "List Simulations", "GET", "/api/curriculum/simulations/")

# --- APP 4: organizations ---
test_endpoint("organizations", "List Schools", "GET", "/api/organizations/schools/")
test_endpoint("organizations", "List School Classes", "GET", "/api/organizations/classes/")
test_endpoint("organizations", "List Streams", "GET", "/api/organizations/streams/")
test_endpoint("organizations", "List Organization Memberships", "GET", "/api/organizations/memberships/")
test_endpoint("organizations", "List Student Enrollments", "GET", "/api/organizations/enrollments/")

# --- APP 5: subscriptions ---
test_endpoint("subscriptions", "List Subscription Plans", "GET", "/api/subscriptions/plans/")
test_endpoint("subscriptions", "List Account Subscriptions", "GET", f"/api/subscriptions/users/{admin_user.id}/subscriptions/")
test_endpoint("subscriptions", "Active Subscriptions", "GET", f"/api/subscriptions/users/{admin_user.id}/subscriptions/active/")
test_endpoint("subscriptions", "Subscribed Users Count", "GET", "/api/subscriptions/subscribed-users/count/")

# --- APP 6: billing_payment ---
test_endpoint("billing_payment", "List Invoices", "GET", "/api/billing-and-payments/invoices/")
inv_first = Invoice.objects.first()
if inv_first:
    test_endpoint("billing_payment", "Invoice Detail", "GET", f"/api/billing-and-payments/invoices/{inv_first.invoice_number}/")
    test_endpoint("billing_payment", "List Invoice Items", "GET", f"/api/billing-and-payments/invoices/{inv_first.invoice_number}/invoice-items/")
    test_endpoint("billing_payment", "List Payment Transactions", "GET", f"/api/billing-and-payments/invoices/{inv_first.invoice_number}/payment-transactions/")

# ==============================================================================
# SECTION 3: EMPIRICAL N+1 SCALING PROOF
# ==============================================================================
print("\n" + "="*80)
print("SECTION 3: EMPIRICAL N+1 SCALING ANALYSIS")
print("="*80)

from Questions.serializers import QuizSerializer
from Resources.serializers import VideoInteractionSerializer
from curriculum.api.serializers import LessonSerializer
from organizations.serializers import OrganizationMembershipSerializer, StudentEnrollmentSerializer
from subscriptions.api.serializers import SubscriptionSerializer
from billing_payment.api.serializers import InvoiceSerializer

n1_scaling_results = []

def measure_serializer_n1(model_cls, serializer_cls, queryset_filter, app_name, model_name):
    # 1 item
    clear_db_queries()
    items_1 = list(model_cls.objects.filter(**queryset_filter)[:1])
    data_1 = serializer_cls(items_1, many=True).data
    q_count_1 = len(get_db_queries())
    
    # 5 items
    clear_db_queries()
    items_5 = list(model_cls.objects.filter(**queryset_filter)[:5])
    data_5 = serializer_cls(items_5, many=True).data
    q_count_5 = len(get_db_queries())

    # 10 items
    clear_db_queries()
    items_10 = list(model_cls.objects.filter(**queryset_filter)[:10])
    data_10 = serializer_cls(items_10, many=True).data
    q_count_10 = len(get_db_queries())

    is_n1 = (q_count_10 > q_count_1)
    
    res = {
        "app": app_name,
        "model": model_name,
        "q_1_item": q_count_1,
        "q_5_items": q_count_5,
        "q_10_items": q_count_10,
        "is_n1_anomaly": is_n1,
        "scaling": f"O(N) [{q_count_1} -> {q_count_5} -> {q_count_10}]" if is_n1 else f"O(1) [{q_count_1} queries]"
    }
    n1_scaling_results.append(res)
    print(f"[{app_name}] {model_name} Serializer Query Scaling: 1 item -> {q_count_1} q | 5 items -> {q_count_5} q | 10 items -> {q_count_10} q | Pattern: {res['scaling']}")
    return res

measure_serializer_n1(Quiz, QuizSerializer, {}, "Questions", "Quiz (with questions & answers)")
measure_serializer_n1(VideoInteraction, VideoInteractionSerializer, {}, "Resources", "VideoInteraction (with user)")
measure_serializer_n1(Lesson, LessonSerializer, {}, "curriculum", "Lesson (with topic, pack, blocks)")
measure_serializer_n1(OrganizationMembership, OrganizationMembershipSerializer, {}, "organizations", "OrganizationMembership (with user, school)")
measure_serializer_n1(StudentEnrollment, StudentEnrollmentSerializer, {}, "organizations", "StudentEnrollment (with student, class, stream)")
measure_serializer_n1(Subscription, SubscriptionSerializer, {}, "subscriptions", "Subscription (with user, plan)")
measure_serializer_n1(Invoice, InvoiceSerializer, {}, "billing_payment", "Invoice (with user, items, transactions)")

output_summary = {
    "indexes_audited": len(all_indexes),
    "fk_coverage": len(fk_coverage),
    "unindexed_fks": len(unindexed_fks),
    "unindexed_filter_cols": unindexed_filter_cols,
    "workflow_results": workflow_results,
    "n1_scaling_results": n1_scaling_results
}

with open("query_investigation_data.json", "w") as f:
    json.dump(output_summary, f, indent=2, default=str)

print("\nQuery investigation completed successfully. Data exported to query_investigation_data.json.")
