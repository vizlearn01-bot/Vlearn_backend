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

from Resources.models import User, UserProfile, VideoInteraction, UploadedFile, ExperimentVideo
from Questions.models import Quiz, Question, Answer
from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, KnowledgePack
from organizations.models import School, OrganizationMembership, AcademicYear, SchoolClass, Stream, StudentEnrollment
from subscriptions.models import SubscriptionPlan, Subscription
from billing_payment.models import Invoice, InvoiceItem, InvoicePaymentTransaction

from Questions.serializers import QuizSerializer
from curriculum.api.serializers import LessonSerializer
from organizations.serializers import SchoolClassSerializer, OrganizationMembershipSerializer, StudentEnrollmentSerializer
from subscriptions.api.serializers import SubscriptionSerializer
from billing_payment.api.serializers import InvoiceSerializer

def get_db_queries():
    return list(connection.queries)

def clear_db_queries():
    reset_queries()

print("================================================================================")
print("EMPIRICAL PROOF: UNOPTIMIZED VS OPTIMIZED QUERYSETS (10 ITEMS EACH)")
print("================================================================================")

def compare_optimization(app_name, name, unopt_qs, opt_qs, serializer_cls):
    # Unoptimized test
    clear_db_queries()
    items_unopt = list(unopt_qs[:10])
    data_unopt = serializer_cls(items_unopt, many=True).data
    queries_unopt = get_db_queries()
    q_count_unopt = len(queries_unopt)
    time_unopt = sum(float(q.get('time', 0)) * 1000 for q in queries_unopt)

    # Optimized test
    clear_db_queries()
    items_opt = list(opt_qs[:10])
    data_opt = serializer_cls(items_opt, many=True).data
    queries_opt = get_db_queries()
    q_count_opt = len(queries_opt)
    time_opt = sum(float(q.get('time', 0)) * 1000 for q in queries_opt)

    query_reduction = q_count_unopt - q_count_opt
    pct_reduction = round((query_reduction / q_count_unopt) * 100, 1) if q_count_unopt > 0 else 0.0

    res = {
        "app": app_name,
        "serializer": name,
        "unoptimized_queries": q_count_unopt,
        "unoptimized_time_ms": round(time_unopt, 3),
        "optimized_queries": q_count_opt,
        "optimized_time_ms": round(time_opt, 3),
        "query_reduction": query_reduction,
        "pct_reduction": pct_reduction
    }
    print(f"[{app_name}] {name}:")
    print(f"   Unoptimized: {q_count_unopt} queries ({time_unopt:.2f}ms)")
    print(f"   Optimized:   {q_count_opt} queries ({time_opt:.2f}ms)")
    print(f"   Reduction:   -{query_reduction} queries ({pct_reduction}% reduction!)\n")
    return res

results = []

# 1. StudentEnrollment
results.append(compare_optimization(
    "organizations", "StudentEnrollmentSerializer",
    StudentEnrollment.objects.all(),
    StudentEnrollment.objects.select_related('student', 'stream__school_class__school', 'academic_year'),
    StudentEnrollmentSerializer
))

# 2. OrganizationMembership
results.append(compare_optimization(
    "organizations", "OrganizationMembershipSerializer",
    OrganizationMembership.objects.all(),
    OrganizationMembership.objects.select_related('user', 'school', 'assigned_by'),
    OrganizationMembershipSerializer
))

# 3. SchoolClass
results.append(compare_optimization(
    "organizations", "SchoolClassSerializer",
    SchoolClass.objects.all(),
    SchoolClass.objects.select_related('curriculum_grade', 'school'),
    SchoolClassSerializer
))

# 4. Invoice
results.append(compare_optimization(
    "billing_payment", "InvoiceSerializer",
    Invoice.objects.all(),
    Invoice.objects.select_related('user_to', 'user_from').prefetch_related('invoice_items', 'payment_transactions'),
    InvoiceSerializer
))

# 5. Subscription
results.append(compare_optimization(
    "subscriptions", "SubscriptionSerializer",
    Subscription.objects.all(),
    Subscription.objects.select_related('user', 'plan', 'invoice'),
    SubscriptionSerializer
))

# 6. Lesson
results.append(compare_optimization(
    "curriculum", "LessonSerializer",
    Lesson.objects.all(),
    Lesson.objects.select_related('topic', 'knowledge_pack').prefetch_related('blocks'),
    LessonSerializer
))

# 7. Quiz
results.append(compare_optimization(
    "Questions", "QuizSerializer",
    Quiz.objects.all(),
    Quiz.objects.select_related('video').prefetch_related('questions__answers'),
    QuizSerializer
))

with open("optimization_benchmark_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Optimization benchmark complete. Output saved to optimization_benchmark_results.json.")
