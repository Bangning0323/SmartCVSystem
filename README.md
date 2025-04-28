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
(Aligned 1-to-1 with your eight functional modules)

SmartCVSystem/
├── config/                          # Django project settings & URL routing
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── authx/                       # 🔐 Authentication & Authorization
│   │   ├── models.py   # User, Role, Permission objects
│   │   ├── views.py    # Login / register / password flows
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── profiles/                    # 👤 User & Profile Management
│   │   ├── models.py   # UserProfile, ResumeFile FK to user
│   │   ├── views.py    # Profile edit / resume upload forms
│   │   └── …
│   │
│   ├── resumes/                     # 📄 CV Upload & Storage + Parsing
│   │   ├── models.py   # FileMeta + ParsedData
│   │   ├── services/   # parser.py (spaCy, PyPDF, docx2txt…)
│   │   ├── views.py    # Upload, preview parsed data
│   │   └── …
│   │
│   ├── repository/                  # 🔎 Search & Filtering  (CV Repository)
│   │   ├── models.py   # IndexedTerm, Skill, etc.
│   │   ├── search.py   # Elastic / PG-full-text logic
│   │   └── …
│   │
│   ├── jobposts/                    # 📋 Job Postings Management
│   │   ├── models.py   # JobPost, Requirement
│   │   ├── views.py    # CRUD for job listings
│   │   └── …
│   │
│   ├── matching/                    # 🧮 Candidate Scoring
│   │   ├── models.py   # MatchScore table
│   │   ├── rules.py    # scoring weight & algorithm
│   │   └── …
│   │
│   ├── shortlist/                   # ⭐ Shortlisting Panel
│   │   ├── models.py   # Shortlist model (FK job ↔ CV)
│   │   ├── views.py    # HR dashboard, add/remove candidates
│   │   └── …
│   │
│   └── common/                      # Reusable utilities (mixins, helpers)
│       ├── mixins.py
│       └── validators.py
│
├── templates/                       # Global base templates (per-app templates live inside each app)
│   └── base.html
│
├── static/                          # Global static assets (logo, CSS vars, JS libs)
│
├── requirements.txt
├── .env.example
└── manage.py



