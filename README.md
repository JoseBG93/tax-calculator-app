## Tax Calculator Pro 🧾💼

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-000?logo=flask)
![Status](https://img.shields.io/badge/Status-Pilot-brightgreen)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

**IIVTNU Tax Calculator** - Professional Flask application for Spanish municipal property value increase tax (Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana).

A specialized tax calculation system exclusively focused on IIVTNU for Ayuntamiento de Alfafar, handling property sales (compraventa), donations (donación), and inheritances (herencia).

### Table of Contents

- [About](#about)
- [Features ✨](#features-)
- [Technology Stack 🧰](#technology-stack-)
- [Project Structure 🗂️](#project-structure-)
- [Installation ⚙️](#installation-️)
  - [Prerequisites (for OCR/NLP)](#prerequisites-for-ocrnlp)
- [Usage ▶️](#usage-️)
- [Development 🧪](#development-)
- [License 📄](#license-)

### About

This project was born from real-world experience in Spanish municipal tax administration. As a civil servant with expertise at Alfafar town hall's Tax Inspection department, I work with property value increase tax calculations daily using GTT/Gestiona software.

**The Challenge**: The current workflow involves manual processing of property deeds for IIVTNU calculations - reading cadastral data, property values, transaction dates, involved parties, and applying municipal coefficients and bonifications. This manual process is time-consuming and error-prone, especially when dealing with complex cases like family bonifications (95%/50%) and varying annual coefficients based on ownership periods.

**The Solution**: This application automates IIVTNU calculations according to Alfafar's municipal ordinance (2022), implementing the current legal framework including the 29% tax rate, family bonifications, and updated state coefficients from RD-ley 8/2023. The system handles the complete legal validation process while maintaining compliance with LRHL articles 104-110.

**The Personal Journey**: This is a pilot project and a personal challenge. It represents my journey of learning new technologies and developing new skills while working full-time. As I don't have exclusive dedication to this project, it's not viable for immediate operational use by anyone. However, it serves as a learning platform and proof of concept.

**Collaboration Welcome**: If any programming professional in the sector is interested, they can collaborate, fork, or develop parallel projects. This repository is also open to curious minds who want to explore this initiative and understand how municipal processes can be modernized.

**The Vision**: This isn't just a calculator - it's a step toward modernizing municipal services. By digitizing tax calculations, we can reduce errors, improve efficiency, and provide better service to citizens. The goal is to demonstrate how technology can transform traditional administrative processes.

### Features ✨

**Current Implementation:**
- ✅ Flask app with Application Factory, CORS, CSRF, rate limiting and security headers
- ✅ User authentication with Flask-Login; admin routes protected with `@admin_required`
- ✅ Database models for tax domain (SQLAlchemy)
- ✅ Legal validation framework module scaffolded (`app/legal_validator.py`)
- ✅ Basic templates: `index`, `login`, `register`, `dashboard`, `calculator`, `history`, admin views
- ✅ Initial tests for CORS behavior (`tests/test_cors.py`)
- ✅ Enhanced synthetic data (33 IIVTNU test cases)

**Planned Features:**
- 🔄 Business logic in `services.py` for IIVTNU calculations
- 🔄 Document parsing and OCR integration
- 🔄 Automated legal validation workflows
- 🔄 Transaction history and reporting
- 🔄 Export capabilities for municipal systems

### Technology Stack 🧰

**Core Application:**
- **Backend**: Flask 2.3.3 (Application Factory Pattern)
- **Auth/Security**: Flask-Login 0.6.3, Flask-WTF 1.2.1 (CSRF), Flask-Limiter 3.8.0, security headers (CSP, X-Frame-Options, etc.)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLAlchemy 2.0.42 + Flask-Migrate 4.0.5
- **Data Processing**: pandas 2.1.4, numpy 1.25.2
- **Validation**: marshmallow 3.20.1
- **Configuration**: python-dotenv 1.0.0
- **CORS**: Flask-Cors 4.0.0

**Future Integrations (Available):**
- **Document OCR**: pdfplumber, ocrmypdf, pytesseract (Tesseract)
- **NLP (Spanish)**: spaCy (es_core_news_md), dateparser
- 
- **HTTP client**: requests

**Development Tools:**
- **Testing**: pytest 7.4.3
- **Code Quality**: black 23.11.0, flake8, mypy
- **Database**: SQLite (development)

### Project Structure 🗂️

```
tax-calculator-pro/
├── app/                       # Flask application core
│   ├── __init__.py            # ✅ Application Factory Pattern
│   ├── models.py              # ✅ SQLAlchemy database models
│   ├── routes.py              # ✅ HTTP endpoints and views (auth, admin, calculator)
│   ├── admin.py               # ✅ Flask-Admin panel configuration
│   ├── services.py            # 🔄 Tax calculation business logic (pending)
│   ├── security_validations.py # ✅ Input validation and sanitization
│   ├── legal_validator.py     # ✅ IIVTNU legal framework and compliance
│   └── utils.py               # 🔄 Helper functions and utilities (pending)
│
├── scripts/                   # 🆕 Management and utility scripts
│   ├── create_admin.py        # ✅ Superadmin account creation/management
│   ├── change_password.py     # ✅ Secure password change utility
│   ├── list_users.py          # ✅ User listing and status
│   ├── secrets_generator.py   # ✅ Generate secure SECRET_KEY
│   ├── bash_aliases.sh        # ✅ Development workflow aliases
│   └── ARCHITECTURE_DIAGRAM.py # ✅ Generate architecture diagrams
│
├── docs/                      # 📚 Comprehensive documentation
│   ├── README.md              # 🆕 Documentation index and guide
│   ├── LEGAL_FRAMEWORK.md     # ✅ LRHL articles 104-110
│   ├── NORMATIVE_GAPS.md      # ✅ Compliance gaps and validations
│   ├── ADMIN_PANEL_GUIDE.md   # ✅ Admin panel usage guide
│   ├── COMMIT_CONVENTIONS.md  # ✅ Git commit standards
│   ├── PROJECT_REVIEW.md      # ✅ Project status and decisions
│   ├── ALIASES_USAGE.md       # ✅ Development aliases reference
│   ├── COMANDOS_RAPIDOS_BD.md # ✅ Database commands quick reference
│   ├── normativa-municipal/   # ✅ Alfafar ordinance PDFs
│   └── flask_shell_guides/    # ✅ Flask shell interactive guides
│
├── learning/                  # 🆕 Personal learning materials
│   ├── README.md              # 🆕 Learning resources index
│   ├── python-decorators/     # Decorator patterns and examples
│   └── python-modules/        # Module usage guides and examples
│
├── data/                      # ✅ Test data and fixtures
│   └── synthetic_iivtnu_cases/ # 33 enhanced IIVTNU test cases
│
├── tests/                     # ✅ pytest test suite
│   ├── conftest.py            # Test configuration
│   └── test_cors.py           # CORS behavior tests
│
├── migrations/                # ✅ Database migrations (Flask-Migrate)
├── database/                  # SQLite database storage
├── dependencies/              # 📦 Requirements and package documentation
│   ├── requirements.txt       # ✅ Pinned Python packages
│   ├── Overview.md            # Package overview
│   └── Detailed_explanation.md # Detailed dependency documentation
│
├── .github/                   # CI/CD and automation
│   ├── workflows/             # GitHub Actions workflows
│   └── scripts/               # CI/CD utility scripts
│
├── run.py                     # ✅ Flask application entry point
├── config.py                  # ✅ Environment configuration
├── .env.example               # 🆕 Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # ✅ This file - Project documentation
```


### Installation ⚙️

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tax-calculator-pro
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv taxapp_env
   source taxapp_env/bin/activate  # Linux/Mac
   # taxapp_env\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r dependencies/requirements.txt
   ```

4. **Initialize database** (when ready)
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

### Environment Configuration 🔐

Every Flask environment (development, staging, production, CI, etc.) **must** provide a strong `SECRET_KEY` so cookies and
session data remain tamper-proof. Generate a unique 32-byte value per environment and store it through your preferred secrets
management solution (for local development this usually means a `.env` file; in production rely on your platform's secret
manager or environment variables).

Use one of the following commands to provision a key:

```bash
# Python standard library – outputs a 64 character hex string representing 32 random bytes
python -c "import secrets; print(secrets.token_hex(32))"

# Alternatively, with OpenSSL
openssl rand -hex 32
```

Once generated, export the value before starting the app:

```bash
export SECRET_KEY="<paste-your-unique-hex-string-here>"
```

> ℹ️ Reuse of the same key across environments is discouraged—rotating them independently limits the blast radius of leaked
> credentials and aligns with Flask's security recommendations.

Also consider configuring CORS origins for development:

```bash
export CORS_ORIGINS="http://localhost:3000"
```

#### Prerequisites (for OCR/NLP)

- System packages (Ubuntu/Debian):
  - `sudo apt update && sudo apt install -y tesseract-ocr ocrmypdf`
- spaCy Spanish model:
  - `python -m spacy download es_core_news_md`


### Usage ▶️

**Initial Setup:**
```bash
# 1. Generate secure SECRET_KEY
python scripts/secrets_generator.py

# 2. Export the generated key
export SECRET_KEY="<your-generated-key>"

# 3. Create superadmin account
python scripts/create_admin.py

# 4. (Optional) List all users
python scripts/list_users.py
```

**Run the Flask application:**
```bash
python run.py
```

The application will start on `http://localhost:5000` with routes like:
- `/` → redirects to `/index`
- `/index` → home page
- `/register` (GET/POST) → user registration (rate limited)
- `/login` (GET/POST) → login (rate limited)
- `/logout` (POST) → logout (requires login)
- `/dashboard` → protected page (requires login)
- `/calculator`, `/history` → shells for future IIVTNU features (require login)
- `/admin`, `/admin/users` → admin area (requires admin role)

**Management Scripts:**
All utility scripts are located in `scripts/` directory:
- `create_admin.py` - Create/update superadmin account
- `change_password.py` - Change user passwords securely
- `list_users.py` - List all registered users
- `secrets_generator.py` - Generate SECRET_KEY

See `scripts/README.md` for detailed usage instructions.

**Current Status:** Core Flask application is running with database models ready for IIVTNU calculations.


### Development 🧪

**Code Quality:**
```bash
black .                     # Code formatting
flake8                      # Linting
mypy                        # Type checking
pytest                      # Testing
```

**Development Workflow:**
1. Activate virtual environment: `source taxapp_env/bin/activate`
2. Run Flask application: `python run.py`
3. Access application: `http://localhost:5000`
4. Run tests: `pytest` (when test suite is implemented)

**Current Phase:** Auth + security hardening completed; database models and templates ready. Next: implement business logic in `services.py` and integrate legal validator into calculator flow, followed by test coverage.


### License 📄

**Educational Use Only** – This project is being developed solely for educational purposes and as a demonstration of municipal tax administration workflows. Although it is designed with scalability in mind for potential future enhancements, it is not an official or functional municipal system at this stage. I do not assume any responsibility for how others may use this code or its outputs.

**Legal Compliance:** All tax calculations follow current Spanish legislation (LRHL) and Alfafar municipal ordinance (2022). The application is built for educational demonstration of IIVTNU processes and is not intended for production use without proper legal validation and municipal approval.

---

**Project Status:** ✅ Phase 4 Complete - Database models and legal framework ready  
**Next Phase:** Web interface development for IIVTNU calculations