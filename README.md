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

This project was born from real-world experience in Spanish municipal tax administration. As a civil servant (Funcionario Interino - Auxiliar Administrativo) specializing in IIVTNU at Ayuntamiento de Alfafar's Tax Inspection department, I work with property value increase tax calculations daily using GTT/Gestiona software.

**The Challenge**: The current workflow involves manual processing of property deeds for IIVTNU calculations - reading cadastral data, property values, transaction dates, involved parties, and applying municipal coefficients and bonifications. This manual process is time-consuming and error-prone, especially when dealing with complex cases like family bonifications (95%/50%) and varying annual coefficients based on ownership periods.

**The Solution**: This application automates IIVTNU calculations according to Alfafar's municipal ordinance (2022), implementing the current legal framework including the 29% tax rate, family bonifications, and updated state coefficients from RD-ley 8/2023. The system handles the complete legal validation process while maintaining compliance with LRHL articles 104-110.

**The Personal Journey**: This is a pilot project and a personal challenge. It represents my journey of learning new technologies and developing new skills while working full-time. As I don't have exclusive dedication to this project, it's not viable for immediate operational use by anyone. However, it serves as a learning platform and proof of concept.

**Collaboration Welcome**: If any programming professional in the sector is interested, they can collaborate, fork, or develop parallel projects. This repository is also open to curious minds who want to explore this initiative and understand how municipal processes can be modernized.

**The Vision**: This isn't just a calculator - it's a step toward modernizing municipal services. By digitizing tax calculations, we can reduce errors, improve efficiency, and provide better service to citizens. The goal is to demonstrate how technology can transform traditional administrative processes.

### Features ✨

**Current Implementation:**
- ✅ IIVTNU tax calculations for Alfafar municipality
- ✅ Legal framework compliance (LRHL articles 104-110)
- ✅ Municipal ordinance integration (2022 parameters)
- ✅ Family bonification system (95%/50% rates)
- ✅ Dual calculation system (Alfafar vs State parameters)
- ✅ Database models for tax domain (SQLAlchemy)
- ✅ Flask application with proper architecture
- ✅ Enhanced synthetic data (33 IIVTNU test cases)

**Planned Features:**
- 🔄 Web interface for tax calculations
- 🔄 Document parsing and OCR integration
- 🔄 Automated legal validation workflows
- 🔄 Transaction history and reporting
- 🔄 Export capabilities for municipal systems

### Technology Stack 🧰

**Core Application:**
- **Backend**: Flask 2.3.3 (Application Factory Pattern)
- **Database**: SQLAlchemy 3.0.5 + Flask-Migrate 4.0.5
- **Data Processing**: pandas 2.1.4, numpy 1.25.2
- **Validation**: marshmallow 3.20.1
- **Configuration**: python-dotenv 1.0.0
- **CORS**: Flask-Cors 4.0.0

**Future Integrations (Available):**
- **Document OCR**: pdfplumber, ocrmypdf, pytesseract (Tesseract)
- **NLP (Spanish)**: spaCy (es_core_news_md), dateparser
- **Frontend**: HTML, CSS, JavaScript
- **HTTP client**: requests

**Development Tools:**
- **Testing**: pytest 7.4.3
- **Code Quality**: black 23.11.0, flake8, mypy
- **Database**: SQLite (development)

### Project Structure 🗂️

```
tax-calculator-pro/
├── app/                    # Flask application core
│   ├── __init__.py         # ✅ Application Factory Pattern
│   ├── models.py           # ✅ SQLAlchemy database models
│   ├── routes.py           # ✅ HTTP endpoints and views
│   ├── services.py         # Tax calculation business logic
│   ├── utils.py            # Helper functions and utilities
│   └── legal_validator.py  # ✅ IIVTNU legal framework
├── data/                   # ✅ 33 enhanced IIVTNU test cases
├── docs/                   # ✅ Legal documentation
│   ├── LEGAL_FRAMEWORK.md  # ✅ LRHL articles 104-110
│   ├── NORMATIVE_GAPS.md   # Legal compliance notes
│   └── normativa-municipal/ # ✅ Alfafar ordinance PDFs
├── static/                 # Frontend assets (CSS, JS, images)
├── templates/              # HTML Jinja2 templates
├── database/               # SQLite database storage
├── dependencies/           # ✅ requirements.txt (46 packages)
├── run.py                  # ✅ Flask application entry point
└── config.py               # ✅ Environment configuration
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

#### Prerequisites (for OCR/NLP)

- System packages (Ubuntu/Debian):
  - `sudo apt update && sudo apt install -y tesseract-ocr ocrmypdf`
- spaCy Spanish model:
  - `python -m spacy download es_core_news_md`


### Usage ▶️

**Run the Flask application:**
```bash
python run.py
```

The application will start on `http://localhost:5000` with:
- Root endpoint: `/` 
- Index page: `/index`
- IIVTNU calculation endpoints (in development)

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

**Current Phase:** Database models and legal framework completed. Next: Web interface development.


### License 📄

**Educational Use Only** – This project is being developed solely for educational purposes and as a demonstration of municipal tax administration workflows. Although it is designed with scalability in mind for potential future enhancements, it is not an official or functional municipal system at this stage. I do not assume any responsibility for how others may use this code or its outputs.

**Legal Compliance:** All tax calculations follow current Spanish legislation (LRHL) and Alfafar municipal ordinance (2022). The application is built for educational demonstration of IIVTNU processes and is not intended for production use without proper legal validation and municipal approval.

---

**Project Status:** ✅ Phase 4 Complete - Database models and legal framework ready  
**Next Phase:** Web interface development for IIVTNU calculations