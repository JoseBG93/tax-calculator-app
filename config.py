# The 'os' module is imported to access environment variables and interact with the operating system,
# which is essential for retrieving configuration values (like secret keys, database URIs, etc.) from the environment.
import logging
import os

# The 'load_dotenv' function from the 'dotenv' package is imported to automatically load environment variables
# from a .env file into the process environment. This allows configuration to be managed outside the codebase,
# supporting best practices for security and flexibility across different environments (development, production, etc.).
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def _require_secret_key() -> str:
    """Return the SECRET_KEY environment variable or raise a helpful error."""

    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        message = (
            "SECRET_KEY environment variable is required. Generate a unique 32-byte "
            "value for each environment (e.g. with `python -c \"import secrets; "
            "print(secrets.token_hex(32))\"`) and set it before starting the app."
        )
        logger.critical(message)
        raise RuntimeError(message)
    return secret_key

# The 'load_dotenv' function is called to load environment variables from the .env file into the process environment.
# This ensures that all configuration values are properly set based on the environment variables defined in the .env file.
load_dotenv()

class Config:
    """Configuración base para la aplicación Flask"""

    # SECRET_KEY is used to sign cookies and sessions in Flask, ensuring the integrity and confidentiality of session data.
    # It is obtained from the 'SECRET_KEY' environment variable (recommended in production for greater security).
    # If the environment variable is missing, the application will raise a RuntimeError to avoid running with insecure defaults.
    # os.environ is a special Python dictionary that contains all the environment variables from the operating system.
    SECRET_KEY = _require_secret_key()

    # The value of DEBUG is obtained from the .env file as a string (for example, 'True' or 'False').
    # To ensure Flask interprets it correctly as a boolean, it is converted to lowercase and compared to 'true'.
    # This way, if you set DEBUG=True (or any case variation) in .env, debug mode will be enabled.
    # Example: DEBUG = 'True' → True; DEBUG = 'false' → False.
    # This conversion is important because environment variables are always received as text.
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

    # SQLALCHEMY_DATABASE_URI specifies the database connection string used by SQLAlchemy.
    # This URI tells the application where and how to connect to the database.
    # By default, it uses a local SQLite database file located at 'database/app.db'.
    # You can override this by setting the 'DATABASE_URL' environment variable to another database URI,
    # such PostgreSQL, MySQL, or another supported backend.
    # Example for PostgreSQL: 'postgresql://user:password@localhost/dbname'
    # This approach allows easy switching between development (local SQLite) and production (remote DB) environments.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # prevents unnecessary overhead by disabling modification tracking

    # File uploads
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'data/AI-generated')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 16777216))  # bytes
    # ALLOWED_EXTENSIONS defines what file types are permitted to be uploaded in the application.
    # It reads the 'ALLOWED_EXTENSIONS' environment variable, which should be a comma-separated string (e.g., 'pdf,jpg,jpeg,png').
    # If the variable is not set, it defaults to allowing 'pdf', 'jpg', 'jpeg', and 'png' files.
    # The string is split by commas to create a list, and then converted to a set for efficient membership checks.
    ALLOWED_EXTENSIONS = set(os.environ.get('ALLOWED_EXTENSIONS', 'pdf,jpg,jpeg,png').split(','))

    # NLP (Natural Language Processing) configuration
    # SPACY_MODEL specifies which spaCy language model app should use for NLP tasks.
    # It attempts to read the model name from the 'SPACY_MODEL' environment variable.
    # If 'SPACY_MODEL' is not set in the environment, it defaults to 'es_core_news_md' (a medium-sized Spanish model).
    # This approach allows easy switching between different spaCy models (e.g., for other languages or model sizes)
    # without changing the code—just by setting the environment variable.
    SPACY_MODEL = os.environ.get('SPACY_MODEL', 'es_core_news_md')

    # CORS_ORIGINS specifies which external domains are allowed to access app resources through Cross-Origin Resource Sharing (CORS).
    # This setting is important for web security, as it controls which frontends or external services can interact with the backend API from the browser.
    # By configuring CORS_ORIGINS, you can handle requests from specific origins, helping to prevent unauthorized cross-origin requests.
    # The value is read from the 'CORS_ORIGINS' environment variable as a comma-separated string (e.g., 'http://localhost:3000,https://myapp.com').
    # If not set, it assign 'http://localhost:3000' by default.
    # The string is split by commas to create a list of allowed origins.
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')

    # LEGAL AND REGULATORY FRAMEWORK CONFIGURATION
    # These settings define the legal and normative framework for IIVTNU tax calculations
    
    # Primary legislation references
    LGT_REFERENCE = "Ley 58/2003, de 17 de diciembre, General Tributaria (BOE-A-2003-23186)"
    LRHL_REFERENCE = "Real Decreto Legislativo 2/2004, de 5 de marzo, por el que se aprueba el texto refundido de la Ley reguladora de las Haciendas Locales (BOE-A-2004-4214)"
    
    # Current coefficient regulation (valid for 2025)
    CURRENT_COEFFICIENT_REGULATION = "Real Decreto-ley 8/2023, de 27 de diciembre"
    COEFFICIENT_BOE_REFERENCE = "BOE-A-2023-28318"
    
    # IIVTNU legal limits and defaults
    IIVTNU_MAX_TAX_RATE = float(os.environ.get('IIVTNU_MAX_TAX_RATE', '30.0'))  # Maximum 30% per LRHL Art. 108
    IIVTNU_MAX_FAMILY_BONUS = float(os.environ.get('IIVTNU_MAX_FAMILY_BONUS', '95.0'))  # Maximum 95% family bonus
    
    # Default municipal configuration (configurable for Alfafar-specific ordinances)
    MUNICIPALITY_NAME = os.environ.get('MUNICIPALITY_NAME', 'Alfafar')
    MUNICIPALITY_CODE = os.environ.get('MUNICIPALITY_CODE', '46910')  # INE code for Alfafar
    
    # Default IIVTNU tax rates (until Alfafar ordinances are accessible)
    IIVTNU_DEFAULT_TAX_RATE = float(os.environ.get('IIVTNU_DEFAULT_TAX_RATE', '30.0'))  # Using maximum as reference
    IIVTNU_DEFAULT_FAMILY_BONUS = float(os.environ.get('IIVTNU_DEFAULT_FAMILY_BONUS', '95.0'))  # Standard family bonus
    
    # Ordinance status tracking
    MUNICIPAL_ORDINANCE_STATUS = os.environ.get('MUNICIPAL_ORDINANCE_STATUS', 'PENDING_ACCESS')
    MUNICIPAL_ORDINANCE_YEAR = os.environ.get('MUNICIPAL_ORDINANCE_YEAR', '2024-2025')
    
    # Legal validation settings
    LEGAL_VALIDATION_ENABLED = os.environ.get('LEGAL_VALIDATION_ENABLED', 'True').lower() == 'true'
    STRICT_LEGAL_COMPLIANCE = os.environ.get('STRICT_LEGAL_COMPLIANCE', 'True').lower() == 'true'
    
    # SECURITY CONFIGURATION
    # Session security
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False').lower() == 'true'  # HTTPS only in production
    SESSION_COOKIE_HTTPONLY = True  # Prevent XSS attacks
    SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
    
    # CSRF protection
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = int(os.environ.get('WTF_CSRF_TIME_LIMIT', '3600'))  # 1 hour
    
    # Rate limiting
    RATELIMIT_STORAGE_URI = os.environ.get('RATELIMIT_STORAGE_URI', 'memory://')
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '100 per hour')
    
    # Security headers
    SECURITY_HEADERS_ENABLED = os.environ.get('SECURITY_HEADERS_ENABLED', 'True').lower() == 'true'