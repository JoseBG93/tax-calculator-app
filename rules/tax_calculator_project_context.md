# TAX CALCULATOR PRO - PROJECT CONTEXT RULE

## PROJECT OVERVIEW

**Project Name:** Tax Calculator Pro  
**Type:** Full-stack web application for municipal tax calculations  
**Technology Stack:** Python Flask + HTML/CSS/JS + SQLite  
**Target:** Learning project + Portfolio showcase  
**User:** José (Auxiliar Administrativo - Inspección Tributaria, Ayuntamiento de Alfafar)

## USER CONTEXT

### Professional Background
- **Current Role:** Funcionario Interino - Auxiliar Administrativo en Inspección Tributaria
- **Specialization:** IIVTNU (Impuesto sobre el Incremento del Valor de los Terrenos de Naturaleza Urbana)
- **Experience:** Software GTT y Gestiona, revisión de escrituras (compraventas, donaciones, herencias)
- **Location:** Ayuntamiento de Alfafar, Valencia, España

### Learning Goals
- **Primary:** Desarrollar habilidades técnicas para portfolio y mercado laboral
- **Approach:** Metodología estructurada tipo "FP" - entender QUÉ, POR QUÉ, CÓMO antes de implementar
- **Pace:** Progresivo, sin abrumarse, asentar fundamentos sólidos

### Technical Background
- **Formation:** Master IA finalizado + Full Stack Programming en progreso (ConquerBlocks)
- **Platforms:** EDTeam, Coursera, YouTube, Master IA (BigSchool)
- **Current Skills:** Python básico, Linux/Bash, Docker conceptos básicos
- **Future Goals:** React Native, aplicaciones móviles, FastAPI

## PROJECT ARCHITECTURE

### Directory Structure
```
tax-calculator-pro/
├── app/                    # Core Flask application
│   ├── __init__.py        # Flask app initialization
│   ├── models.py          # SQLAlchemy database models
│   ├── routes.py          # HTTP endpoints (API)
│   ├── services.py        # Business logic (tax calculations)
│   └── utils.py           # Helper functions
├── static/                # Frontend assets
│   ├── css/              # Stylesheets (main.css, calculator.css, responsive.css)
│   ├── js/               # JavaScript files
│   └── images/           # Images and icons
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── calculator.html   # Tax calculator interface
│   └── history.html      # Calculation history
├── data/                 # Synthetic datasets
│   ├── compraventa_*.json    # 10 synthetic property sales
│   ├── donacion_*.json       # 10 synthetic donations + 1 exempt
│   ├── herencia_*.json       # 10 synthetic inheritances + 1 multiple
│   └── synthetic_mcps_collection.json  # Complete dataset
├── database/             # SQLite database files
├── tests/                # Unit and integration tests
├── requirements.txt      # Python dependencies
├── explained_dependencies.txt  # Detailed dependency explanations
├── config.py            # Application configuration
└── run.py               # Application entry point
```

### Technology Stack

#### Backend (Flask)
- **Framework:** Flask 2.3.3 (microframework for learning)
- **Database:** SQLAlchemy 3.0.5 + SQLite (development)
- **ORM:** Flask-SQLAlchemy for database operations
- **Migrations:** Flask-Migrate for database versioning
- **CORS:** Flask-CORS for frontend-backend communication
- **Validation:** Marshmallow for data validation

#### Data Processing
- **Core:** Pandas 2.1.4 for data manipulation
- **Calculations:** NumPy 1.25.2 for numerical operations
- **Synthetic Data:** 33 JSON files with realistic tax documents
- **Future:** Scikit-learn for ML models

#### Frontend
- **Structure:** HTML5 + CSS3 + Vanilla JavaScript
- **Styling:** Custom CSS (no frameworks initially)
- **Responsive:** Mobile-first design approach
- **Future:** Bootstrap or Tailwind CSS

#### Development Tools
- **Testing:** Pytest + pytest-flask
- **Code Quality:** Black (formatting), Flake8 (linting), MyPy (type checking)
- **Imports:** isort for import organization
- **Environment:** Python virtual environment (taxapp)

## BUSINESS DOMAIN

### Tax Types Covered
1. **IIVTNU** (José's specialty) - Property value increase tax
2. **ISD** (Impuesto de Sucesiones y Donaciones) - Inheritance and gift tax
3. **Future:** IBI, IAE, ICIO, IVTM (complete municipal tax system)

### Document Types Processed
- **Compraventas:** Property sales with IIVTNU calculations
- **Donaciones:** Family donations with ISD calculations
- **Herencias:** Inheritance documents with ISD calculations
- **Synthetic Data:** 33 realistic documents for testing and ML training

### Calculation Features
- **Base Imponible:** Taxable base calculations
- **Cuotas:** Tax amount calculations
- **Reducciones:** Applicable deductions and exemptions
- **Validaciones:** Data validation and error checking
- **Historial:** Calculation history and audit trail

## DEVELOPMENT PHASES

### Phase 1: Basic Flask Application (Current)
- ✅ Project structure created
- ✅ Dependencies installed
- ✅ Virtual environment configured
- 🔄 Basic Flask setup (config.py, run.py, app/__init__.py)
- 🔄 First endpoint and database models
- 🔄 Basic frontend (calculator interface)

### Phase 2: Core Functionality
- Tax calculation engine
- Data processing with Pandas
- Database integration
- Basic UI/UX
- Testing framework

### Phase 3: Advanced Features
- Machine learning integration (Scikit-learn)
- Data visualization (Matplotlib/Seaborn)
- AI explanations (OpenAI API)
- PDF report generation
- Advanced UI components

### Phase 4: Production Ready
- Authentication and security
- Performance optimization
- Deployment configuration
- Documentation
- Portfolio presentation

## LEARNING OBJECTIVES

### Technical Skills
- **Web Development:** Flask framework, HTTP, REST APIs
- **Database Design:** SQLAlchemy ORM, migrations, data modeling
- **Data Processing:** Pandas, NumPy, data analysis
- **Testing:** Unit tests, integration tests, TDD
- **Code Quality:** Linting, formatting, type checking
- **Version Control:** Git, GitHub, collaboration

### Domain Knowledge
- **Tax Legislation:** Spanish municipal tax system
- **Document Processing:** Legal document analysis
- **Data Validation:** Business rule implementation
- **Audit Trail:** Calculation history and verification

### Professional Development
- **Portfolio Building:** Showcase project for job applications
- **Problem Solving:** Real-world application development
- **Best Practices:** Professional coding standards
- **Documentation:** Technical writing and project documentation

## COMMUNICATION STYLE

### Teaching Approach
- **Progressive:** Start simple, build complexity gradually
- **Explanatory:** Always explain WHY, not just HOW
- **Practical:** Connect theory to real-world applications
- **Encouraging:** Support learning journey, celebrate progress
- **Patient:** Allow time for understanding before moving forward

### Code Development
- **Commented:** Every significant code block explained
- **Modular:** Clear separation of concerns
- **Testable:** Code written with testing in mind
- **Maintainable:** Clean, readable, professional code
- **Scalable:** Architecture that can grow with requirements

### Project Management
- **Structured:** Clear phases and milestones
- **Documented:** Comprehensive project documentation
- **Version Controlled:** Proper Git workflow
- **Quality Focused:** Testing and code quality from start

## SUCCESS METRICS

### Technical Success
- ✅ Functional tax calculator application
- ✅ Clean, maintainable codebase
- ✅ Comprehensive test coverage
- ✅ Professional documentation
- ✅ Deployable application

### Learning Success
- ✅ Understanding of web development concepts
- ✅ Proficiency with Python ecosystem
- ✅ Database design and management skills
- ✅ Testing and quality assurance practices
- ✅ Project management and documentation

### Professional Success
- ✅ Impressive portfolio project
- ✅ Demonstrable technical skills
- ✅ Real-world problem-solving experience
- ✅ Professional development practices
- ✅ Foundation for future learning

## IMPORTANT CONTEXT NOTES

### User Preferences
- **Learning Style:** Structured, step-by-step, understand before implement
- **Communication:** Conversational, encouraging, practical examples
- **Pace:** Progressive, no rushing, solid foundations first
- **Focus:** Real-world applicability, professional standards

### Technical Constraints
- **Time:** Limited development time (full-time job + studies)
- **Experience:** Beginner to intermediate Python skills
- **Resources:** Personal learning environment, no production infrastructure
- **Goals:** Learning + portfolio, not commercial product

### Project Scope
- **Start:** Simple tax calculator with IIVTNU
- **Expand:** Additional tax types and features
- **Future:** Machine learning, mobile app, advanced features
- **End Goal:** Professional-quality application for portfolio

This context should guide all AI interactions to ensure responses are appropriate, helpful, and aligned with José's learning goals and project requirements. 