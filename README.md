# SmartCVSystem

Welcome to SmartCV System Repo

# 📘 SmartCVSystem

A Django-powered candidate–job matching platform using MySQL. It parses digital CVs, matches skills & experience to roles, and provides basic fit-reports.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django 4.x  
- **Database:** MySQL 8.x  
- **Authentication:** Django’s built-in auth system  
- **Environment:** `.env` (via `django-environ` or similar)  
- **Frontend (optional):** Bootstrap / TailwindCSS  

---

## 🚀 Features

1. **Resume Parsing**  
   Automatically extracts skills, experience, and education from uploaded CVs.  
2. **Candidate–Role Matching**  
   Algorithmic matching based on keyword analysis and weightings.  
3. **Secure Data Storage**  
   All applicant and match data encrypted at rest in MySQL.  
4. **Fit Reports**  
   Simple downloadable summaries of match scores.  

---

## 📥 Prerequisites

- Python 3.8+  
- MySQL server (local or remote)  
- `virtualenv` or `venv`  

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/SmartCVSystem.git
   cd SmartCVSystem


## 📂 Suggested Django Project Layout
_Each top-level package maps directly to the functional modules in your design._

```text
SmartCVSystem/
├── manage.py
├── requirements.txt
├── .env.example
├── config/                  # Django project settings & root URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── authx/               # Authentication & Authorization
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── profiles/            # User & Profile Management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── resumes/             # CV Upload, Storage & Parsing
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── services/
│   │   │   └── parser.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── repository/          # Search & Filtering
│   │   ├── migrations/
│   │   ├── search.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── jobposts/            # Job Postings Management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── matching/            # Candidate Scoring
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── rules.py
│   │   └── views.py
│   ├── shortlist/           # Shortlisting Panel
│   │   ├── migrations/
│   │   ├── models.py
│   │   └── views.py
│   └── common/              # Reusable utilities
│       ├── mixins.py
│       └── validators.py
├── templates/               # Global base templates (per-app templates live inside each app)
│   └── base.html
└── static/                  # Global static assets



