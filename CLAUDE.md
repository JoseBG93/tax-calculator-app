# CLAUDE.md - AI Assistant Context File

## PROJECT OVERVIEW
**Tax Calculator Pro** - Flask web application for Spanish municipal tax calculations
- **Learning Project**: José's portfolio and skill development
- **Domain**: Spanish tax system (IIVTNU, ISD) for Ayuntamiento de Alfafar
- **Tech Stack**: Python Flask + SQLAlchemy + SQLite + HTML/CSS/JS

## USER PROFILE: JOSÉ
### Professional Context
- **Role**: Funcionario Interino - Auxiliar Administrativo, Inspección Tributaria
- **Specialization**: IIVTNU (Property Value Increase Tax)
- **Experience**: GTT/Gestiona software, legal document review (sales, donations, inheritances)
- **Location**: Ayuntamiento de Alfafar, Valencia, España

### Learning Style & Preferences
- **Methodology**: Structured "FP-style" - understand WHY before HOW
- **Pace**: Progressive, step-by-step, solid foundations first
- **Coding Style**: Hands-on typing, self-explanatory comments, learning by doing
- **Communication**: Patient explanations, practical examples, encouraging approach

### Technical Background
- **Current**: Python basics, Linux/Bash, Docker concepts, Master IA completed
- **Learning**: Full Stack Programming (ConquerBlocks), Flask, SQLAlchemy
- **Future Goals**: React Native, mobile apps, FastAPI

## CURRENT PROJECT STATUS

### Phase 1: Basic Flask Setup (IN PROGRESS)
- ✅ Project structure created
- ✅ Dependencies installed (`requirements.txt` with 46 packages)
- ✅ Virtual environment configured (`taxapp_env`)
- ✅ Configuration system implemented (`config.py`)
- 🔄 **CURRENT TASK**: Flask app initialization (`app/__init__.py`)
  - Currently implementing Application Factory Pattern
  - Step-by-step guided coding approach
  - José typing each snippet with detailed explanations

### Development Progress Tracking
**Todo List Status:**
1. 🔄 Implement Flask app initialization in app/__init__.py (IN PROGRESS)
2. ⏳ Create application entry point in run.py
3. ⏳ Set up basic database models in app/models.py  
4. ⏳ Create first route in app/routes.py
5. ⏳ Test the basic Flask application

### Key Files Status
- `config.py`: ✅ Complete (environment variables, database, CORS, file uploads)
- `app/__init__.py`: 🔄 In progress (imports added, working on create_app function)
- `run.py`: ❌ Empty (needs Flask app runner)
- `app/models.py`, `app/routes.py`, etc.: ❌ Not started

## TECHNICAL ARCHITECTURE

### Database Configuration
- **Type**: SQLite (development)
- **Location**: `sqlite:///database/app.db`
- **ORM**: SQLAlchemy 2.0.42
- **Migrations**: Flask-Migrate 4.0.5

### Key Dependencies (from requirements.txt)
```
Flask==2.3.3                 # Web framework
Flask-SQLAlchemy==3.0.5      # Database ORM
Flask-Migrate==4.0.5         # Database migrations
Flask-Cors==4.0.0            # Cross-origin requests
pandas==2.1.4                # Data processing
numpy==1.25.2                # Numerical operations
marshmallow==3.20.1          # Data validation
pytest==7.4.3                # Testing framework
black==23.11.0               # Code formatting
```

### Directory Structure
```
tax-calculator-pro/
├── app/                     # Core Flask application
│   ├── __init__.py         # 🔄 Flask app factory (in progress)
│   ├── models.py           # Database models (pending)
│   ├── routes.py           # HTTP endpoints (pending)
│   ├── services.py         # Tax calculation logic
│   └── utils.py            # Helper functions
├── config.py               # ✅ Environment configuration
├── run.py                  # ❌ App entry point (empty)
├── database/               # SQLite storage
├── static/                 # Frontend assets
├── templates/              # HTML templates
└── data/                   # 33 synthetic tax documents (JSON)
```

## DEVELOPMENT GUIDELINES

### Code Style Preferences
- **Comments**: Extensive, educational comments explaining WHY and HOW
- **Structure**: Clean, modular, following Flask best practices
- **Pattern**: Application Factory Pattern for Flask setup
- **Quality**: Professional standards suitable for portfolio

### Teaching Approach
- **Step-by-step**: Small code snippets with explanations
- **Interactive**: José types code himself, asks questions
- **Context**: Always explain business relevance to tax calculations
- **Patience**: Allow time for understanding concepts
- **Encouragement**: Celebrate progress and learning achievements

### Business Domain Context
- **Tax Types**: IIVTNU (José's specialty), ISD (inheritances/donations)
- **Documents**: Property sales, donations, inheritances
- **Calculations**: Base Imponible, tax amounts, reductions, exemptions
- **Data**: 33 synthetic documents for testing (compraventa_*.json, donacion_*.json, herencia_*.json)

## CURRENT SESSION CONTEXT

### Active Task: Flask App Initialization
- **File**: `app/__init__.py`
- **Progress**: Added imports (Flask, SQLAlchemy, Migrate, CORS), created extension objects
- **Next**: Implementing `create_app()` function with Application Factory Pattern
- **Learning Focus**: Understanding why we use factory pattern, what each import does

### Recent Accomplishments
- José correctly identified Flask as web framework for connecting apps to ports
- Successfully understood database configuration (SQLite at `database/app.db`)
- Added proper imports and extension objects to `__init__.py`

### Immediate Next Steps
1. Complete `create_app()` function in `__init__.py`
2. Add configuration loading and extension initialization
3. Create basic `run.py` to start the application
4. Test that Flask app runs successfully

## AI ASSISTANT BEHAVIOR RULES

### Communication Style
- Keep explanations clear and pedagogical
- Always explain WHY before showing HOW
- Use practical examples from tax domain when possible
- Be patient and encouraging
- Ask questions to check understanding

### Code Development
- Let José type code snippets himself
- Provide small, digestible code pieces
- Always include educational comments in code
- Follow Flask best practices and patterns
- Focus on clean, maintainable, professional code

### Project Management
- Use TodoWrite tool to track progress
- Mark tasks as completed when finished
- Break complex tasks into smaller steps
- Maintain focus on current phase objectives
- Document decisions and progress

This file should be updated as the project evolves to maintain accurate context for AI assistance.