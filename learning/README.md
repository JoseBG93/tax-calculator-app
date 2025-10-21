# Personal Learning Materials 📚

This directory contains personal study notes, examples, and learning resources that support continuous professional development.

> **Note**: These materials are **not part of the main Tax Calculator Pro application**. They represent the developer's learning journey and serve as reference documentation for Python concepts and patterns.

## Contents

### 📖 Python Decorators (`python-decorators/`)

Comprehensive examples and notes on Python decorator patterns:
- `1_dataclass_basico.py` - Basic dataclass usage and concepts
- `2_property_decorador.py` - Property decorators for getters/setters
- `3_staticmethod_classmethod.py` - Static and class method decorators
- `4_decoradores_personalizados.py` - Creating custom decorators
- `5_decoradores_flask.py` - Flask-specific decorators (@app.route, @login_required, etc.)
- `6_dataclass_avanzado.py` - Advanced dataclass features
- `7_resumen_y_consejos.py` - Summary and best practices

**Purpose**: Understanding decorator patterns used extensively in the Flask application (routes, authentication, validation).

### 📦 Python Modules (`python-modules/`)

Documentation and examples for Python standard library and external packages:

#### Native Modules
- Debugging & Logging (logging, traceback)
- Data Formats (json)
- Runtime & System (os, sys)

#### External Modules
- **Backend Core**: Flask, SQLAlchemy, pytest, requests
- **Data Tooling**: pandas, numpy, matplotlib, scikit-learn
- **Scraping & Images**: BeautifulSoup, Pillow

**Purpose**: Quick reference for modules used in Tax Calculator Pro and general Python development.

## Why Separate from Main Project?

1. **Clarity**: Keeps the main application structure clean and professional
2. **Organization**: Educational materials distinct from production code
3. **Reusability**: These notes can benefit other projects and learning contexts
4. **Collaboration**: Other developers can focus on application code without navigating learning materials

## Learning Philosophy

This project embodies the principle of **learning by building**. As a civil servant working full-time while developing this application, these materials represent:

- 🎯 **Targeted Learning**: Focus on technologies directly applicable to the project
- 🔄 **Iterative Understanding**: Build concepts progressively as needed
- 📝 **Documentation Practice**: Learn by teaching (writing explanations)
- 🚀 **Real-World Application**: Immediately apply concepts to production code

## Integration with Main Project

While these materials are separate, they directly support the Tax Calculator Pro development:

| Learning Material | Application in Project |
|-------------------|------------------------|
| Flask decorators | Route definitions, auth protection (`app/routes.py`) |
| Dataclasses | Legal validation models (`app/legal_validator.py`) |
| SQLAlchemy | Database models (`app/models.py`) |
| pytest | Test suite (`tests/`) |
| pandas/numpy | Data processing for tax calculations |

## Contributing Your Learning

If you're exploring this project and want to contribute learning materials:
1. Add new examples with clear docstrings
2. Include practical use cases from the project
3. Update this README with new content
4. Share insights that helped you understand concepts

---

**Philosophy**: "The best way to learn is to build something real."

**Status**: Ongoing - Updated as new concepts are explored  
**Maintainer**: José - Continuous Learning Journey

