# Documentation Index 📚

Comprehensive documentation for Tax Calculator Pro - Spanish Municipal IIVTNU Tax System.

## Table of Contents

### 🏛️ Legal & Regulatory Framework
- **[LEGAL_FRAMEWORK.md](LEGAL_FRAMEWORK.md)** - Complete LRHL articles 104-110 for IIVTNU
- **[NORMATIVE_GAPS.md](NORMATIVE_GAPS.md)** - Known compliance gaps and pending validations
- **[normativa-municipal/](normativa-municipal/)** - Alfafar municipal ordinance PDFs (BOP documents)

### ⚙️ Technical Guides
- **[ADMIN_PANEL_GUIDE.md](ADMIN_PANEL_GUIDE.md)** - Flask-Admin panel usage and configuration
- **[COMMIT_CONVENTIONS.md](COMMIT_CONVENTIONS.md)** - Git commit message standards
- **[ALIASES_USAGE.md](ALIASES_USAGE.md)** - Development workflow aliases and shortcuts
- **[COMANDOS_RAPIDOS_BD.md](COMANDOS_RAPIDOS_BD.md)** - Quick database commands reference

### 🐚 Flask Shell Guides
- **[flask_shell_guides/](flask_shell_guides/)** - Interactive Flask shell usage
  - `FLASK_SHELL_README.md` - Complete guide to Flask shell
  - `FLASK_SHELL_QUICK_GUIDE.md` - Quick reference
  - `shell_helper.py` - Helper functions
  - `ejemplo_consultas.py` - Query examples

### 📊 Project Management
- **[PROJECT_REVIEW.md](PROJECT_REVIEW.md)** - Project status, milestones, and technical decisions

---

## Document Organization

### Legal Compliance (🏛️ Critical for Production)

These documents define the legal framework and ensure tax calculations comply with Spanish legislation:

1. **LEGAL_FRAMEWORK.md**: Foundation document with complete LRHL articles
2. **NORMATIVE_GAPS.md**: Tracks pending validations and compliance status
3. **normativa-municipal/**: Official Alfafar ordinances (primary legal source)

> ⚠️ **Important**: Before any production deployment, all items in NORMATIVE_GAPS.md must be resolved and validated by municipal legal department.

### Technical Documentation (⚙️ Development)

Guides for developers and system administrators:

- **Admin Panel**: User management, database administration via Flask-Admin
- **Database Commands**: Quick reference for SQLAlchemy operations
- **Commit Conventions**: Maintain consistent Git history
- **Aliases**: Speed up common development tasks

### Flask Shell (🐚 Interactive Development)

The Flask shell provides direct access to application context for:
- Database queries and testing
- User management
- Tax calculation experiments
- Debugging and inspection

See `flask_shell_guides/` for comprehensive examples.

---

## Contributing to Documentation

When adding new documentation:

1. **Place in appropriate category**:
   - Legal/regulatory → root of `docs/`
   - Technical guides → root of `docs/`
   - Flask-specific → `flask_shell_guides/`
   - API docs → `api/` (future)

2. **Update this index**:
   - Add entry with clear description
   - Link to the new document
   - Explain its purpose and audience

3. **Follow naming conventions**:
   - Use UPPERCASE for major documents: `LEGAL_FRAMEWORK.md`
   - Use lowercase for guides: `database_guide.md`
   - Use descriptive names: `admin_panel_guide.md` not `guide1.md`

4. **Include metadata**:
   - Date created/updated
   - Author/maintainer
   - Version if applicable
   - Related documents

---

## Documentation Standards

### Structure
- Start with clear title and purpose
- Include table of contents for long documents
- Use headers hierarchically (H1 → H2 → H3)
- Add code examples with syntax highlighting

### Content
- Write for the target audience (legal, technical, or general)
- Include practical examples
- Link to related documents
- Keep language clear and concise

### Maintenance
- Review quarterly for accuracy
- Update when code changes affect documentation
- Mark outdated sections clearly
- Archive superseded documents

---

## Quick Reference

| Need to... | See Document |
|-----------|--------------|
| Understand IIVTNU legal basis | LEGAL_FRAMEWORK.md |
| Check compliance status | NORMATIVE_GAPS.md |
| Use admin panel | ADMIN_PANEL_GUIDE.md |
| Work with Flask shell | flask_shell_guides/ |
| Run database commands | COMANDOS_RAPIDOS_BD.md |
| Follow Git conventions | COMMIT_CONVENTIONS.md |
| Review project status | PROJECT_REVIEW.md |

---

## External Resources

### Spanish Tax Legislation
- **LRHL**: [Real Decreto Legislativo 2/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214)
- **RD-ley 8/2023**: IIVTNU coefficients for 2025
- **LGT**: Ley 58/2003 General Tributaria

### Alfafar Municipal
- **Official Website**: https://alfafar.es
- **BOP Valencia**: Ordinances published in Provincial Bulletin
- **Municipal Transparency Portal**: Regulatory framework

### Flask & Python
- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Flask-Admin**: https://flask-admin.readthedocs.io/

---

**Last Updated**: October 2025  
**Maintained By**: Tax Calculator Pro Development Team  
**Contact**: José - Municipal Tax Administration Expert

