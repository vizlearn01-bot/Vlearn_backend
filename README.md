# VizLearn Backend

> The enterprise Django REST API powering **VizLearn** — handling Competency-Based Curriculum (CBC) delivery, AI-assisted content ingestion, multi-tenant school administration, assessment and grading analytics, STEM simulations, subscriptions, and Safaricom M-Pesa billing.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Django Apps Architecture](#django-apps-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Virtual Environment](#installation--virtual-environment)
  - [Environment Variables Configuration](#environment-variables-configuration)
  - [Running Database Migrations](#running-database-migrations)
  - [Account Provisioning & Role Elevation](#account-provisioning--role-elevation)
  - [Data Seeding & Management Commands](#data-seeding--management-commands)
  - [Running the Server](#running-the-server)
  - [Running Background Workers (Celery)](#running-background-workers-celery)
- [API Endpoints Architecture](#api-endpoints-architecture)
- [Authentication & Roles](#authentication--roles)
- [Curriculum & AI Content Ingestion Engine](#curriculum--ai-content-ingestion-engine)
- [Payments & Billing (M-Pesa / Daraja)](#payments--billing-mpesa--daraja)
- [Media & Video Delivery](#media--video-delivery)
- [Testing & Quality Assurance](#testing--quality-assurance)
- [Common Troubleshooting](#common-troubleshooting)
- [Deployment & Operations](#deployment--operations)
- [Contributing](#contributing)

---

## Overview

The VizLearn backend is a **Django 5.1 REST API** serving the multi-portal [VizLearn Frontend](https://github.com/Griffin-Ndede/Vlearn_frontend).

The system is structured across 8 specialized domain applications responsible for:
- **Curriculum Delivery** — Hierarchical CBC and secondary syllabi (Grades 6–10, Forms 3–4) with 25+ pedagogical blueprint card types, concept-by-concept navigation, and KaTeX mathematical typesetting.
- **AI-Powered Ingestion** — Multi-provider LLM pipeline (Google GenAI Gemini, OpenAI, Anthropic) generating structured pedagogical lesson blocks, misconceptions, worked examples, and SVG diagrams from educational source materials.
- **Multi-Tenant School Management** — Institutional models for schools, academic years, classes, streams, teacher allocations, and student admissions.
- **Assessment & Examination Analytics** — CBC assessment recording, KCSE mark entry, stream aggregations, and performance dashboards.
- **Interactive Science Simulations** — Backend registry and asset management supporting over 140 STEM interactive simulations.
- **Subscriptions & Entitlements** — Dynamic product catalog, multi-tiered access scopes, and feature entitlements.
- **Billing & Telephony** — Safaricom Daraja M-Pesa STK push integration, callback handling, immutable financial ledger entries, and Africa's Talking SMS/OTP delivery.
- **SEO Knowledge Base** — Server-rendered public knowledge articles, dynamic sitemaps, and search crawler controls.

---

## Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| [Django](https://www.djangoproject.com/) | 5.1.4 | Core web application framework |
| [Django REST Framework](https://www.django-rest-framework.org/) | 3.15.2 | RESTful API toolkit and serialization |
| [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/) | 5.4.0 | JWT authentication with token rotation & blacklist |
| [PostgreSQL / psycopg2-binary](https://www.psycopg.org/) | 2.9.10 | Primary relational database engine |
| [dj-database-url](https://github.com/jazzband/dj-database-url) | 2.3.0 | 12-factor database URL configuration |
| [google-genai](https://pypi.org/project/google-genai/) | 2.12.1 | Official Google GenAI SDK for Gemini models |
| [openai](https://github.com/openai/openai-python) | >=1.30.0 | OpenAI API client for AI generation fallback |
| [anthropic](https://github.com/anthropics/anthropic-sdk-python) | >=0.28.0 | Anthropic Claude SDK for AI generation fallback |
| [Celery](https://docs.celeryq.dev/) | >=5.4.0 | Asynchronous background job queue |
| [Redis](https://redis.io/) | >=5.0.0 | Celery message broker and Django cache backend |
| [django-daraja](https://github.com/drewpayment/django-daraja) | 1.3.0 | Safaricom M-Pesa Daraja API integration |
| [africastalking](https://africastalking.com/) | >=1.2.5 | SMS delivery for passwordless OTP authentication |
| [Pydantic](https://docs.pydantic.dev/) | >=2.0.0 | Structured output schema validation for AI agents |
| [pypdf](https://pypdf.readthedocs.io/) | 4.2.0 | Textbook PDF extraction for AI ingestion |
| [Cloudinary](https://cloudinary.com/) | 1.41.0 | Cloud image storage (with local storage fallback) |
| [django-cloudinary-storage](https://github.com/klis87/django-cloudinary-storage) | 0.3.0 | Cloudinary media backend |
| [Whitenoise](https://whitenoise.readthedocs.io/) | 6.8.2 | Static file serving for production |
| [Gunicorn](https://gunicorn.org/) | 23.0.0 | Production WSGI HTTP server |
| [openpyxl](https://openpyxl.readthedocs.io/) | >=3.1.0 | Excel template generation for school mark imports |
| [bleach](https://github.com/mozilla/bleach) | >=6.0.0 | HTML sanitization for user and AI content |

---

## Project Structure

```
Vlearn_backend/
├── Nexus_backend/                  # Core Django project configuration
│   ├── settings.py                 # Multi-environment settings & fail-fast guards
│   ├── urls.py                     # Root URL router
│   ├── celery.py                   # Celery application setup
│   ├── asgi.py                     # ASGI entry point
│   └── wsgi.py                     # WSGI production entry point
│
├── curriculum/                     # Core CBC curriculum domain (16 migrations)
│   ├── models.py                   # Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, Simulation
│   ├── api/                        # REST API ViewSets, serializers, and permission classes
│   ├── ai_ingestion/               # TopicModuleGenerationAgent & VisualGeneratorAgent
│   ├── publisher/                  # Cross-database curriculum promotion pipeline
│   └── management/commands/        # publish_curriculum, populate_simulations, ingest_lesson_md
│
├── organizations/                  # Multi-tenant school domain (9 migrations)
│   ├── models.py                   # School, AcademicYear, SchoolClass, Stream, TeacherAssignments
│   ├── views.py                    # School admin & teacher portal endpoints
│   └── urls.py                     # Mounted at /api/organizations/
│
├── assessments/                    # Academic examinations & analytics (2 migrations)
│   ├── models.py                   # Examination, ExaminationSubject, StudentMark, KCSEResults
│   ├── grading.py                  # Grade boundaries and aggregation algorithms
│   └── urls.py                     # Mounted at /api/assessments/ & /api/performance/
│
├── knowledge/                      # Public SEO articles & sitemaps (2 migrations)
│   ├── models.py                   # ArticleCategory, ArticleTag, Article
│   └── management/commands/        # seed_starter_knowledge
│
├── subscriptions/                  # Dynamic products & access scopes (5 migrations)
│   ├── models.py                   # Product, ProductVariant, AccessScope, Subscription
│   ├── api/                        # Mounted at /api/subscriptions/ (checkout, products, entitlements)
│   └── management/commands/        # seed_m3_products, create_subscription_plans
│
├── billing_payment/                # Invoicing & M-Pesa Daraja payments (6 migrations)
│   ├── models.py                   # Invoice, InvoiceItem, InvoicePaymentTransaction, FinancialLedgerEntry
│   ├── mpesa/                      # Daraja STK push utilities, callback validation, token caching
│   └── api/                        # Mounted at /api/billing-and-payments/
│
├── Resources/                      # Core auth, custom user, and media files (45 migrations)
│   ├── models.py                   # User (AUTH_USER_MODEL), UserProfile, ExperimentVideo, UploadedFile
│   ├── auth_urls.py                # Mounted at /api/auth/ (phone OTP login & password reset)
│   ├── health_views.py             # Health check endpoints (/health/, /ready/)
│   └── otp/                        # Africa's Talking SMS client
│
├── Questions/                      # Standalone quiz assessments (4 migrations)
│   ├── models.py                   # Quiz, Question, Answer, QuestionAttempt, StudentAnswer
│   └── urls.py                     # Mounted at /questions/
│
├── ai_infrastructure/              # Unified LLM provider factory & retry backoff engine
├── requirements.txt                # Production Python dependencies
├── manage.py
└── .env.example                    # Verified environment template
```

---

## Django Apps Architecture

### 1. `curriculum`
The primary pedagogical engine of the platform.
- **Hierarchy:** `Curriculum` $\rightarrow$ `Grade` $\rightarrow$ `Subject` $\rightarrow$ `Topic` $\rightarrow$ `LearningUnit` $\rightarrow$ `Lesson` $\rightarrow$ `LessonBlock`.
- **Lesson V2 Block Architecture:** `LessonBlock` stores granular, structured educational content mapped to 25+ pedagogical card types (Worked Examples, KaTeX Formulas, Misconception Alerts, Step Processes, and KCSE Structured Exam Questions).
- **Persistent Media Assets:** `LessonAsset` models SVG diagrams, images, YouTube embeds, and simulations attached to specific blocks.
- **AI Generation & Publishing:** Includes `GenerationJob`, `KnowledgePack`, `TopicModuleGenerationAgent`, and `VisualGeneratorAgent` for automated curriculum drafting from source textbooks.

### 2. `organizations`
Provides institutional tenancy for schools and educational institutions.
- **Models:** `School`, `OrganizationMembership`, `AcademicYear`, `SchoolClass`, `Stream`, `TeacherSubjectAssignment`, `TeacherStreamAssignment`, `TeacherLessonLog`, `StudentEnrollment`, `SchoolSubscription`.
- **Access:** Enables teachers to manage their specific streams and school administrators to oversee institutional performance.

### 3. `assessments`
Manages formal school examinations, continuous assessment tests (CATs), and national examination analytics.
- **Models:** `Examination`, `ExaminationSubject`, `StudentMark`, `KCSESchoolResult`, `KCSESubjectResult`.
- **Analytics:** Calculates class mean scores, subject rankings, grade distributions, and student academic baselines.

### 4. `knowledge`
Public-facing educational knowledge base and SEO system.
- **Models:** `ArticleCategory`, `ArticleTag`, `Article`.
- **SEO Integration:** Generates dynamic XML sitemaps (`/sitemap.xml`) and dynamic `robots.txt` (`/robots.txt`).

### 5. `Resources`
Handles user authentication and account infrastructure.
- **Custom User Model:** `AUTH_USER_MODEL = "Resources.User"` supports four platform roles: `student`, `teacher`, `school_admin`, and `platform_admin`.
- **Auth Features:** Password login, phone OTP registration/login via Africa's Talking, password reset tokens, and profile management.
- **Legacy Video Catalog:** Hosts `ExperimentVideo` (direct streaming videos). *(Note: There is no `Course` model; modern courses are represented in the `curriculum` app).*

### 6. `Questions`
Provides standalone assessment quizzes and student answer tracking.
- **Models:** `Quiz`, `Question` (MCQ or text), `Answer`, `QuestionAttempt`, `StudentAnswer`.

### 7. `subscriptions`
Dynamic entitlement and subscription product management.
- **Models:** `Product`, `ProductVariant` (Daily, Monthly, Term, Annual), `AccessScope` (Platform-wide, Grade-level, Subject-level), `Subscription`, `Promotion`.
- **Entitlement Service:** Dynamically checks user subscription status against requested subjects and curriculum features.

### 8. `billing_payment`
Financial processing and telecom billing.
- **Models:** `Invoice`, `InvoiceItem`, `InvoicePaymentTransaction`, `FinancialLedgerEntry`, `MpesaPaymentAccount`.
- **Safaricom Daraja Integration:** Initiates STK push requests, verifies webhook callback signatures, updates invoice states, and activates subscriptions automatically.

---

## Getting Started

### Prerequisites

- **Python:** `3.11` or `3.12`
- **PostgreSQL:** `15+` (Mandatory; SQLite is retired)
- **Redis:** `7+` (Optional for local development; required if running Celery background AI tasks)
- **pip** and **virtualenv**

### Installation & Virtual Environment

```bash
# 1. Clone the repository
git clone https://github.com/Griffin-Ndede/Vlearn_backend.git
cd Vlearn_backend

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate         # Linux / macOS
# venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables Configuration

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Configure your local PostgreSQL connection and core settings:

```env
# Django Core
SECRET_KEY=your-local-dev-secret-key
DEBUG=True
PUBLIC_SITE_URL=http://localhost:5173

# Database (PostgreSQL is required)
DATABASE_URL=postgres://<username>:<password>@localhost:5432/<dbname>

# Storage (Defaults to local filesystem storage if False)
USE_CLOUDINARY=False

# Celery & Caching (Optional for local dev; tasks run synchronously if unset)
CELERY_TASK_ALWAYS_EAGER=True
```

> ⚠️ **Important:** `DATABASE_URL` is **mandatory**. `Nexus_backend/settings.py` enforces a fail-fast check that crashes Django immediately if `DATABASE_URL` is missing.

### Running Database Migrations

The project contains **89 migrations** across all 8 apps. Execute migrations against your PostgreSQL database:

```bash
python manage.py migrate
```

### Account Provisioning & Role Elevation

Create a standard superuser:

```bash
python manage.py createsuperuser
```

> ⚠️ **Role Elevation Required:** By default, `createsuperuser` initializes users with `role='student'`. Because the frontend guards the Admin Portal (`/admin-dashboard/*`) with `allowedRoles={["platform_admin"]}`, elevate your superuser role using the Django shell:

```bash
python manage.py shell -c "from Resources.models import User; u = User.objects.get(username='<your-username>'); u.role='platform_admin'; u.save()"
```

### Data Seeding & Management Commands

Initialize starter data and catalog records:

```bash
# 1. Populate science simulation registry (140+ STEM sims)
python manage.py populate_simulations

# 2. Seed subscription products and pricing plans
python manage.py seed_m3_products

# 3. Seed M-Pesa payment accounts for Daraja integration
python manage.py seed_mpesa_accounts

# 4. Seed public SEO knowledge articles (optional)
python manage.py seed_starter_knowledge
```

### Running the Server

```bash
python manage.py runserver 127.0.0.1:8000
```

The API is served at [http://127.0.0.1:8000](http://127.0.0.1:8000).  
Access the Django Admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

### Running Background Workers (Celery)

For processing asynchronous AI curriculum ingestion, image generation, or PDF extractions:

```bash
# Ensure Redis is running locally on port 6379, then start the worker:
celery -A Nexus_backend worker -l info
```

*(If Redis is not running and `CELERY_TASK_ALWAYS_EAGER=True` is configured in `.env`, tasks execute synchronously in-process).*

---

## API Endpoints Architecture

Root routing is declared in `Nexus_backend/urls.py`:

| Prefix | Source App | Purpose |
|---|---|---|
| `/admin/` | `django.contrib.admin` | Django administration portal |
| `/health/`, `/api/health/` | `Resources.health_views` | System health check (HTTP 200) |
| `/ready/`, `/api/ready/` | `Resources.health_views` | Database and cache readiness probe |
| `/api/token/refresh/` | `rest_framework_simplejwt` | JWT access token refresh |
| `/api/auth/` | `Resources.auth_urls` | Phone OTP request, verification, password recovery |
| `/login/`, `/register/` | `Resources.urls` | Standard credentials authentication and profile |
| `/api/curriculum/` | `curriculum.api.urls` | Grades, subjects, topics, active lessons, lesson blocks, assets |
| `/api/organizations/` | `organizations.urls` | Schools, academic structures, teachers, students |
| `/api/assessments/` | `assessments.urls` | Examinations, KCSE marks, grading rubrics |
| `/api/performance/` | `assessments.urls` | Student, stream, and school academic analytics |
| `/api/subscriptions/` | `subscriptions.api.urls` | Product catalog, pricing variants, checkout, entitlements |
| `/api/billing-and-payments/`| `billing_payment.api.urls`| Invoices, payments, M-Pesa STK push & callbacks |
| `/questions/` | `Questions.urls` | Standalone quizzes, question attempts, submissions |
| `/api/knowledge/` | `knowledge.api.urls` | REST API for educational knowledge articles |
| `/knowledge/` | `knowledge.urls` | Server-rendered knowledge base views |
| `/sitemap.xml` | `knowledge.views` | Dynamic XML sitemap for SEO crawlers |
| `/robots.txt` | `knowledge.views` | Search engine indexing rules |

---

## Authentication & Roles

### JWT Configuration
Authentication uses `djangorestframework-simplejwt` configured in `Nexus_backend/settings.py`:

| Setting | Value |
|---|---|
| Access Token Lifetime | 1 day |
| Refresh Token Lifetime | 7 days |
| Token Rotation | Enabled (`ROTATE_REFRESH_TOKENS = True`) |
| Token Blacklist | Enabled (`BLACKLIST_AFTER_ROTATION = True`) |
| Header Type | `Bearer <access_token>` |

### User Roles
- `student` — Standard learner account.
- `teacher` — Educator with assigned school classes and streams.
- `school_admin` — Institutional administrator.
- `platform_admin` — Superuser with administrative and content-authoring privileges (`is_staff = True`).

Role information is serialized directly into the JWT token claims on login (`role`, `organization_id`, `user_id`) and hydrated through `GET /profile/`.

---

## Curriculum & AI Content Ingestion Engine

### Ingestion Pipeline
1. **Source Document Upload** — Textbook PDFs are ingested via `curriculum.KnowledgePack` and chunked using `pypdf`.
2. **Pedagogical Agent Processing** — `TopicModuleGenerationAgent` (`curriculum/ai_ingestion/agent.py`) parses text chunks using structured Pydantic schemas.
3. **Blueprint Block Construction** — Lessons are saved as `LessonBlock` records with validated pedagogical schemas (Worked Examples, KaTeX Formulas, Misconception Alerts).
4. **Visual Asset Generation** — `VisualGeneratorAgent` (`curriculum/ai_ingestion/visual_agent.py`) generates contextual SVG/Mermaid diagrams and links them as `LessonAsset`.
5. **Quality Gates** — Lessons remain in `draft` status until passing validation checks (learning goals, worked examples, quizzes) in `ContentStudio`.
6. **Cross-Database Publishing** — The management command `publish_curriculum` promotes approved curriculum data from staging to production databases via `PUBLISH_DATABASE_URL`.

---

## Payments & Billing (M-Pesa / Daraja)

The backend provides Safaricom Daraja STK Push integration via `billing_payment/mpesa/utils.py`:

1. **Checkout Initiation:** Frontend calls `POST /api/subscriptions/checkout/` to create a pending `Subscription` and `Invoice`.
2. **STK Push Dispatch:** Frontend calls `POST /api/billing-and-payments/invoices/<id>/payment-transactions/` with `{ amount, payment_method: "MPESA", payment_details: { mpesa_phone_number: "254..." } }`.
3. **Gateway Call:** Backend requests an OAuth bearer token from Safaricom Daraja and sends an STK push prompt to the customer's mobile device.
4. **Client Polling:** Frontend polls `GET /api/billing-and-payments/invoices/<number>/status/` every 2.5 seconds.
5. **Webhook Callback:** Upon PIN confirmation, Safaricom posts transaction results to `/api/billing-and-payments/mpesa/stk-push-callback/`.
6. **Reconciliation:** Backend marks the invoice as `PAID`, records a `FinancialLedgerEntry`, and activates the `Subscription`.

> 💡 **Local Development Webhooks:** To receive Daraja callbacks locally, expose port 8000 via a tunnel (e.g. ngrok: `ngrok http 8000`) and configure `MPESA_CALLBACK_URL` in `.env`. `Nexus_backend/settings.py` automatically appends the callback tunnel hostname to `ALLOWED_HOSTS`.

---

## Media & Video Delivery

### Cloudflare Stream (Video Delivery)
Course experiment videos are hosted on **Cloudflare Stream**:
- Direct iframe playback URL: `https://iframe.videodelivery.net/{cloudflare_video_id}`.
- HLS manifest: `https://videodelivery.net/{cloudflare_video_id}/manifest/video.m3u8`.
- Video uploads to Cloudflare Stream are mediated server-to-server through Django (`Resources/views.py:ExperimentVideoView`).

### Cloudinary (Media Storage)
User avatars and category banners use Cloudinary when `USE_CLOUDINARY=True`. In local development (`USE_CLOUDINARY=False`), Django defaults to local `FileSystemStorage` (`MEDIA_ROOT = BASE_DIR / "media"`), avoiding external API delivery limits.

---

## Testing & Quality Assurance

### Running Tests
Automated tests are located in individual app test directories (`curriculum/tests/`, `organizations/tests.py`, `knowledge/tests.py`, etc.):

```bash
# Run the entire test suite (requires a running PostgreSQL database with CREATEDB privileges)
python manage.py test

# Run tests for a specific application
python manage.py test curriculum
python manage.py test organizations
python manage.py test knowledge
```

### Health Check Probes
- `curl -I http://127.0.0.1:8000/health/` — Validates HTTP service liveness.
- `curl -I http://127.0.0.1:8000/ready/` — Validates database and cache connectivity.

---

## Common Troubleshooting

### 1. `ImproperlyConfigured: DATABASE_URL environment variable is required`
- **Cause:** `DATABASE_URL` is missing from `.env`. SQLite is retired; both development and production require PostgreSQL.
- **Fix:** Set `DATABASE_URL=postgres://<user>:<password>@localhost:5432/<dbname>` in `.env`.

### 2. Admin Portal Lockout
- **Cause:** Superuser account created via `createsuperuser` has `role='student'`.
- **Fix:** Run `python manage.py shell -c "from Resources.models import User; u = User.objects.get(username='<admin>'); u.role='platform_admin'; u.save()"`.

### 3. Celery Tasks Hanging Locally
- **Cause:** Redis server is not running locally.
- **Fix:** Either start Redis (`redis-server`) or set `CELERY_TASK_ALWAYS_EAGER=True` in `.env` to execute background jobs synchronously.

### 4. Production Host Security Crash
- **Cause:** `DEBUG=False` and `PUBLIC_SITE_URL` contains `localhost` or `127.0.0.1`.
- **Fix:** Set `PUBLIC_SITE_URL=https://api.vizlearn.co` (or your actual production domain) when deploying.

---

## Deployment & Operations

### Production Configuration
- **WSGI Server:** Gunicorn (`gunicorn Nexus_backend.wsgi:application --bind 0.0.0.0:8000`).
- **Static Assets:** Whitenoise (`python manage.py collectstatic --noinput`).
- **Database Pooling:** `conn_max_age=600` with `conn_health_checks=True` for managed PostgreSQL providers.
- **SSL & Security:** Enforced when `DEBUG=False` (`SECURE_SSL_REDIRECT=True`, `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`).

### Pre-Deployment Checklist
```bash
# 1. Collect static assets
python manage.py collectstatic --noinput

# 2. Apply database migrations
python manage.py migrate

# 3. Verify system checks
python manage.py check --deploy
```

---

## Contributing

1. Fork the repository and create your feature branch: `git checkout -b feature/your-feature-name`
2. Ensure migrations are generated for any model modifications: `python manage.py makemigrations`
3. Run test suites: `python manage.py test`
4. Commit your changes: `git commit -m "feat: describe your change"`
5. Push to your branch and open a Pull Request against `vlearn-revamp-backend`.

---

*Part of the VizLearn platform — built for learners, teachers, and institutions across Kenya.*