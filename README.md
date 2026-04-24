# Vlearn Backend

> The Django REST API powering **Vlearn (VizLearn)** — handling authentication, course resources, quizzes, science simulations, subscriptions, and M-Pesa / card billing for the Vlearn e-learning platform.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Django Apps](#django-apps)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Server](#running-the-server)
  - [Running Migrations](#running-migrations)
  - [Creating a Superuser](#creating-a-superuser)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Payments & Billing](#payments--billing)
  - [M-Pesa (Daraja)](#m-pesa-daraja)
  - [Billing Models](#billing-models)
- [Media & File Storage](#media--file-storage)
- [Video Hosting](#video-hosting)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## Overview

The Vlearn backend is a **Django 5.1 REST API** that serves the [Vlearn Frontend](https://github.com/Griffin-Ndede/Vlearn_frontend). It is structured as a multi-app Django project with the following core responsibilities:

- User registration, login, and JWT-based authentication
- Course content delivery — videos, uploaded files, and experiment resources
- Quiz and question management with student attempt tracking
- Subscription plan management and access gating
- Invoice generation and payment processing via **M-Pesa (Safaricom Daraja API)** and card
- Media file storage via **Cloudinary** and video hosting via **Cloudflare Stream**
- Deployed on **Render** and accessible at `api.vizlearn.co`

---

## Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| [Django](https://www.djangoproject.com/) | 5.1.4 | Web framework |
| [Django REST Framework](https://www.django-rest-framework.org/) | 3.15.2 | REST API toolkit |
| [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/) | 5.4.0 | JWT authentication |
| [django-cors-headers](https://github.com/adamchainz/django-cors-headers) | 4.6.0 | CORS policy management |
| [django-daraja](https://github.com/drewpayment/django-daraja) | 1.3.0 | Safaricom M-Pesa Daraja API integration |
| [django-rest-passwordreset](https://github.com/anexia-it/django-rest-passwordreset) | 1.5.0 | Password reset via email |
| [Cloudinary](https://cloudinary.com/) | 1.41.0 | Image and file media storage |
| [django-cloudinary-storage](https://github.com/klis87/django-cloudinary-storage) | 0.3.0 | Django storage backend for Cloudinary |
| [django-storages](https://django-storages.readthedocs.io/) | 1.14.6 | AWS S3 / cloud storage support |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | 1.38.8 | AWS SDK (S3 integration) |
| [psycopg2](https://www.psycopg.org/) | 2.9.10 | PostgreSQL database adapter |
| [dj-database-url](https://github.com/jazzband/dj-database-url) | 2.3.0 | Database URL parsing for deployment |
| [Gunicorn](https://gunicorn.org/) | 23.0.0 | WSGI HTTP server for production |
| [Whitenoise](https://whitenoise.readthedocs.io/) | 6.8.2 | Static file serving |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | 1.0.1 | `.env` file loading |
| [Pillow](https://pillow.readthedocs.io/) | 11.1.0 | Image processing |
| [PyJWT](https://pyjwt.readthedocs.io/) | 2.10.1 | JWT encoding/decoding |
| [cryptography](https://cryptography.io/) | 44.0.2 | Cryptographic operations |

---

## Project Structure

```
Vlearn_backend/
├── Nexus_backend/                  # Django project configuration
│   ├── settings.py                 # Main settings file
│   ├── urls.py                     # Root URL configuration
│   ├── asgi.py                     # ASGI entry point
│   └── wsgi.py                     # WSGI entry point
│
├── Resources/                      # Core app — users, courses, videos, files
│   ├── models.py                   # User, Course, ExperimentVideo, UploadedFile, etc.
│   ├── views.py                    # API views for resources
│   ├── urls.py                     # Resource URL routes
│   ├── signals.py                  # Post-save/delete signals
│   ├── admin.py
│   └── migrations/                 # 37+ migration files
│
├── Questions/                      # Quiz and question management app
│   ├── models.py                   # Quiz, Question, QuestionAttempt, StudentAnswer
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── subscriptions/                  # Subscription plan management app
│   ├── models.py                   # SubscriptionPlan, UserSubscription
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py                 # Mounted at /api/subscriptions/
│   └── migrations/
│
├── billing_payment/                # Billing, invoicing, and payments app
│   ├── models.py                   # Invoice, InvoiceItem, InvoicePaymentTransaction, MpesaPaymentAccount
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py                 # Mounted at /api/billing-and-payments/
│   ├── mpesa/
│   │   ├── serializers.py          # M-Pesa request/response serializers
│   │   └── utils.py                # M-Pesa helper functions (STK push, callback handling)
│   └── migrations/                 # 10 migration files
│
├── requirements.txt                # Python dependencies
├── manage.py
└── db.sqlite3                      # Local SQLite database (development only)
```

---

## Django Apps

### `Resources`
The core application. Contains the custom `User` model (set as `AUTH_USER_MODEL`), course content, experiment videos, uploaded resource files, video interactions, access tokens, and subscription linking. It has the most migration history (37+ migrations), indicating active development.

**Key models:** `User`, `Course`, `ExperimentVideo`, `UploadedFile`, `UserProfile`, `VideoInteraction`, `AccessToken`, `SubscriptionPlan`, `UserSubscription`

### `Questions`
Manages all quiz and assessment logic — quizzes, questions, answer groups, student attempts, and scoring.

**Key models:** `Quiz`, `Question`, `QuestionAttempt`, `StudentAnswer`

### `subscriptions`
Handles subscription plan definitions and user subscription assignments. Exposes its own REST API under `/api/subscriptions/`.

**Key models:** `SubscriptionPlan`, `UserSubscription`

### `billing_payment`
Handles invoicing, payment transaction records, and M-Pesa STK push integration. Contains a dedicated `mpesa/` sub-module for Daraja API utilities.

**Key models:** `Invoice`, `InvoiceItem`, `InvoicePaymentTransaction`, `MpesaPaymentAccount`

---

## Getting Started

### Prerequisites

- Python **3.11+**
- pip
- A virtual environment tool (e.g. `venv`)
- PostgreSQL (for production) or SQLite (for development — included by default)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Griffin-Ndede/Vlearn_backend.git
cd Vlearn_backend

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root. The application uses `python-dotenv` to load these automatically:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
LIVE_URL=api.vizlearn.co

# Database (leave blank to use SQLite locally)
DATABASE_URL=postgres://user:password@host:port/dbname

# Cloudinary (media storage)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Cloudflare Stream (video hosting)
CLOUDFLARE_STREAM_ACCOUNT_ID=your_account_id
CLOUDFLARE_STREAM_AUTH_TOKEN=your_auth_token

# M-Pesa / Safaricom Daraja
MPESA_ENVIRONMENT=sandbox          # or "production"
MPESA_CONSUMER_KEY=your_key
MPESA_CONSUMER_SECRET=your_secret
MPESA_SHORTCODE=your_shortcode
MPESA_EXPRESS_SHORTCODE=your_express_shortcode
MPESA_SHORTCODE_TYPE=paybill
MPESA_PASSKEY=your_passkey
MPESA_INITIATOR_USERNAME=your_username
MPESA_INITIATOR_SECURITY_CREDENTIAL=your_credential
```

> ⚠️ Never commit your `.env` file to version control. Add it to `.gitignore`.

### Running Migrations

```bash
python manage.py migrate
```

### Running the Server

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### Creating a Superuser

```bash
python manage.py createsuperuser
```

Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/).

---

## API Endpoints

All endpoints are defined across the four apps and wired together in `Nexus_backend/urls.py`:

| Prefix | App | Description |
|---|---|---|
| `/admin/` | Django Admin | Built-in Django admin panel |
| `/` | `Resources` | Users, courses, videos, files, auth |
| `/questions/` | `Questions` | Quizzes, questions, attempts, results |
| `/api/subscriptions/` | `subscriptions` | Subscription plans and user subscriptions |
| `/api/billing-and-payments/` | `billing_payment` | Invoices, payments, M-Pesa transactions |

> Refer to the individual `urls.py` files in each app for specific endpoint paths.

---

## Authentication

Vlearn uses **JSON Web Tokens (JWT)** via `djangorestframework-simplejwt`. The token configuration in `settings.py` is:

| Setting | Value |
|---|---|
| Access Token Lifetime | 1 day |
| Refresh Token Lifetime | 7 days |
| Rotate Refresh Tokens | Yes |
| Blacklist After Rotation | Yes |
| Auth Header Type | `Bearer` |

All protected API endpoints expect the header:

```
Authorization: Bearer <access_token>
```

Password reset is handled by `django-rest-passwordreset`, which sends a reset link via email.

---

## Payments & Billing

### M-Pesa (Daraja)

The backend integrates with **Safaricom's Daraja API** using `django-daraja` and a custom `billing_payment/mpesa/` module. The M-Pesa flow supports:

- **STK Push** — Prompts the user's phone for payment confirmation
- **Callback handling** — Receives and records payment confirmation from Safaricom
- **Sandbox & Production** — Controlled via the `MPESA_ENVIRONMENT` environment variable

The `mpesa/utils.py` file contains helper functions for initiating payments and processing callbacks. The `mpesa/serializers.py` handles validation of incoming Daraja callback payloads.

### Billing Models

| Model | Description |
|---|---|
| `Invoice` | Represents a billing invoice with due date, issued date, and paid status |
| `InvoiceItem` | Line items on an invoice with unit price and quantity |
| `InvoicePaymentTransaction` | Records each payment transaction tied to an invoice |
| `MpesaPaymentAccount` | Stores M-Pesa account/shortcode configuration |

---

## Media & File Storage

Uploaded files (course resources, images) are stored using **Cloudinary** via `django-cloudinary-storage`. Configuration is read from the environment:

```python
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}
```

In local development, media files are served from `MEDIA_ROOT = BASE_DIR / "media"` under the `/media/` URL prefix.

---

## Video Hosting

Course videos are hosted on **Cloudflare Stream**. The backend generates direct upload URLs for the frontend using the Cloudflare Stream API:

```
CLOUDFLARE_STREAM_BASE_URL = https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/stream
CLOUDFLARE_STREAM_UPLOAD_URL = {BASE_URL}/direct_upload
```

This allows the frontend (using `tus-js-client`) to upload video files directly to Cloudflare Stream without proxying through the Django server, keeping upload performance high.

---

## Deployment

The backend is deployed on **[Render](https://render.com/)** and served at:

```
https://api.vizlearn.co
```

Key deployment considerations:

- **Gunicorn** is used as the WSGI server (`gunicorn Nexus_backend.wsgi`)
- **Whitenoise** serves static files without a separate web server
- **`dj-database-url`** parses the `DATABASE_URL` environment variable to connect to a production PostgreSQL database
- `ALLOWED_HOSTS` includes `vlearn-backend-qw31.onrender.com` and `api.vizlearn.co`
- CORS is configured to allow requests only from `http://localhost:5173` (development) and `https://vizlearn.co` (production)
- Set `DEBUG=False` in production and provide a strong `SECRET_KEY` via the environment

### Deployment Checklist

```bash
# Collect static files before deploying
python manage.py collectstatic --noinput

# Run migrations on the production database
python manage.py migrate

# Start the server with Gunicorn
gunicorn Nexus_backend.wsgi:application --bind 0.0.0.0:8000
```

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "feat: describe your change"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request against the `main` branch

Please ensure all migrations are included for any model changes (`python manage.py makemigrations`) and that the app runs without errors before submitting.

---

*Part of the Vlearn / VizLearn platform — built for learners across Kenya and beyond.*