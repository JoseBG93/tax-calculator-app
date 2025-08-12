# The 'os' module is imported to access environment variables and interact with the operating system, 
# which is essential for retrieving configuration values (like secret keys, database URIs, etc.) from the environment.
import os

# The 'load_dotenv' function from the 'dotenv' package is imported to automatically load environment variables 
# from a .env file into the process environment. This allows configuration to be managed outside the codebase, 
# supporting best practices for security and flexibility across different environments (development, production, etc.).
from dotenv import load_dotenv

# The 'load_dotenv' function is called to load environment variables from the .env file into the process environment.
# This ensures that all configuration values are properly set based on the environment variables defined in the .env file.
load_dotenv()

class Config:
    """Configuración base para la aplicación Flask"""

    # SECRET_KEY is used to sign cookies and sessions in Flask, ensuring the integrity and confidentiality of session data.
    # It is obtained from the 'SECRET_KEY' environment variable (recommended in production for greater security).
    # If not defined, it uses the default value 'dev-key-fallback' (only appropriate for development).
    # os.environ is a special Python dictionary that contains all the environment variables from the operating system.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-fallback')

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
    # such as for PostgreSQL, MySQL, or another supported backend.
    # Example for PostgreSQL: 'postgresql://user:password@localhost/dbname'
    # This approach allows easy switching between development (local SQLite) and production (remote DB) environments.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # prevents unnecessary overhead by disabling modification tracking

    # File uploads
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'data/uploads')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 16777216))  # bytes
    # ALLOWED_EXTENSIONS defines which file types are permitted for upload in the application.
    # It reads the 'ALLOWED_EXTENSIONS' environment variable, which should be a comma-separated string (e.g., 'pdf,jpg,jpeg,png').
    # If the variable is not set, it defaults to allowing 'pdf', 'jpg', 'jpeg', and 'png' files.
    # The string is split by commas to create a list, and then converted to a set for efficient membership checks.
    ALLOWED_EXTENSIONS = set(os.environ.get('ALLOWED_EXTENSIONS', 'pdf,jpg,jpeg,png').split(','))

    # NLP (Natural Language Processing) configuration
    # SPACY_MODEL specifies which spaCy language model the application should use for NLP tasks.
    # It attempts to read the model name from the 'SPACY_MODEL' environment variable.
    # If 'SPACY_MODEL' is not set in the environment, it defaults to 'es_core_news_md' (a medium-sized Spanish model).
    # This approach allows easy switching between different spaCy models (e.g., for other languages or model sizes)
    # without changing the code—just by setting the environment variable.
    SPACY_MODEL = os.environ.get('SPACY_MODEL', 'es_core_news_md')

    # CORS_ORIGINS specifies which external domains are permitted to access resources from this application via Cross-Origin Resource Sharing (CORS).
    # This setting is important for web security, as it controls which frontends or external services can interact with the backend API from the browser.
    # By configuring CORS_ORIGINS, you can restrict or allow requests from specific origins, helping to prevent unauthorized cross-origin requests.
    # The value is read from the 'CORS_ORIGINS' environment variable as a comma-separated string (e.g., 'http://localhost:3000,https://myapp.com').
    # If not set, it defaults to allowing only 'http://localhost:3000', which is typical for local development.
    # The string is split by commas to create a list of allowed origins.
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')