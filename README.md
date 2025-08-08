## Tax Calculator Pro 🧾💼

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-000?logo=flask)
![Status](https://img.shields.io/badge/Status-Pilot-brightgreen)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

Modern tax calculation for Spanish municipal deeds (compraventa, donación, herencia) with OCR + NLP assisted workflows.

A professional tax calculation application for Spanish property transactions, including sales (compraventa), donations (donación), and inheritances (herencia).

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

This project was born from real-world experience in Spanish municipal tax administration. As a tax interin civil servant who works with property transactions daily, I've witnessed the complexity and time-consuming nature of reading deeds and calculating taxes for property sales, donations, and inheritances.

**The Challenge, the Real Motivation**: The current workflow is, in truth, an exhausting ritual of manual steps. It begins with downloading deeds from the registry and storing them in computer folders. Then, using the GTT application (an extremely uncomfortable program to work with), data must be threaded through different screens and fields. Each deed must be read and understood in full: its cadastral data, values, dates, involved parties, ages, etc. From there, a cascade of tasks and actions must be initiated for each file, followed by the manual drafting in Word of the communications of initiation, hearing procedures, conformity acts, liquidation proposals, resolutions, and the same for sanctions when applicable, etc. These are tedious, boring, slow, and lengthy manual procedures. The true revolution is to compress this entire manual work ecosystem into an automated system with integrated AI and a business logic structure and technologies that optimize all this work to the maximum possible, leaving room for the civil servant to supervise that the calculations are correct.
So, this project springs from the frustration of performing manual bureaucratic tasks in 2025, when automation tools exist to make work more efficient and faster. These bureaucratic rituals drive me to keep moving forward, increasingly confident that things can change and improve, despite the resistance to change from many civil servant colleagues.

**The Personal Journey**: This is a pilot project and a personal challenge. It represents my journey of learning new technologies and developing new skills while working full-time. As I don't have exclusive dedication to this project, it's not viable for immediate operational use by anyone. However, it serves as a learning platform and proof of concept.

**Collaboration Welcome**: If any programming professional in the sector is interested, they can collaborate, fork, or develop parallel projects. This repository is also open to curious minds who want to explore this initiative and understand how municipal processes can be modernized.

**The Vision**: This isn't just a calculator - it's a step toward modernizing municipal services. By digitizing tax calculations, we can reduce errors, improve efficiency, and provide better service to citizens. The goal is to demonstrate how technology can transform traditional administrative processes.

### Features ✨

- Calculate taxes for different transaction types ➗
- Read deeds and extract data from them 🧠
- Support for Spanish tax regulations 🇪🇸
- Web-based interface with responsive design 🌐
- Transaction history tracking 📚
- Synthetic data for testing 🧪

### Technology Stack 🧰

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with Flask-Migrate
- **Frontend**: HTML, CSS, JavaScript
- **Document parsing & OCR**: pdfplumber, ocrmypdf, pytesseract (Tesseract)
- **NLP (Spanish)**: spaCy (es_core_news_md), dateparser
- **Data processing**: pandas, numpy
- **Validation/serialization**: marshmallow
- **HTTP client**: requests
- **Environment config**: python-dotenv
- **Testing**: pytest
- **Code Quality**: black, flake8, mypy

### Project Structure 🗂️

```
tax-calculator-pro/
├── app/                    # Application modules
├── data/                   # Sample transaction data
├── dependencies/           # Requirements and documentation
├── rules/                  # Business rules and context
├── static/                 # CSS, JS, and images
├── templates/              # HTML templates
├── database/               # Database files
├── run.py                  # Application entry point
└── config.py               # Configuration settings
```


### Installation ⚙️

1. Clone the repository
2. Create a virtual environment: `python -m venv taxapp_venv`
3. Activate the environment: `source taxapp_venv/bin/activate` (Linux/Mac) or `taxapp_venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r dependencies/requirements.txt`

#### Prerequisites (for OCR/NLP)

- System packages (Ubuntu/Debian):
  - `sudo apt update && sudo apt install -y tesseract-ocr ocrmypdf`
- spaCy Spanish model:
  - `python -m spacy download es_core_news_md`


### Usage ▶️

Run the application:
```bash
python run.py
```


### Development 🧪

- Code formatting: `black .`
- Linting: `flake8`
- Type checking: `mypy`
- Testing: `pytest`


### License 📄

This project is for educational and professional use in Spanish tax calculations.