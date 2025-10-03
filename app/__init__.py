# This file create the whole Flask application. It creates several Flask's apps. That is called Application Factory Pattern.

'''Flask is a Python web framework that creates web apps and handles HTTP requests and responses.
It manages both routes and templates, and serves your app on a port (like 5000).'''
from flask import Flask

'''SQLAlchemy is the Python's ORM (Object-Relational Mapping) that works like a database manager, allowing you to interact 
with databases using Python objects (OOP). Instead of writing raw SQL like 'SELECT * FROM users', you'll write Python code like
'User.query.all()'. It translates Python objects into database tables automatically.'''
from flask_sqlalchemy import SQLAlchemy

'''Migrate is a tool that helps you manage database changes over time. It allows you to track changes to your database
schema and apply them to your database. So, when you need to add, for example, a new column to a table, it creates 
"migration files" that safely update your database. Think of it as a version control for your database structure.'''
from flask_migrate import Migrate

'''CORS is a tool that allows you to manage Cross-Origin Resource Sharing (CORS) in your Flask application.
It allows you to configure which external domains are permitted to access resources from your application via CORS.
So, it allows your frontend (running on port 3000) to access resources from your backend (running on port 5000).
Without this, browsers would block requests from the frontend (requests) to the backend (responses), for security reasons.'''
from flask_cors import CORS

'''Flask-Login is a library that handles user authentication in Flask applications. It provides a simple way to manage user sessions and authentication.'''
from flask_login import LoginManager

'''Flask-WTF provides CSRF protection and form handling for Flask applications.'''
'''CSRF stands for Cross-Site Request Forgery. It is a security mechanism that protects against attacks where an attacker forces a user to execute unwanted actions 
on a web application in which they are currently authenticated.'''
from flask_wtf.csrf import CSRFProtect

'''Flask-Limiter provides rate limiting functionality to prevent abuse and DoS attacks.'''
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

'''Application Factory Pattern: The following function creates and configures a Flask application instance.
Why use this pattern? It allows you to create multiple app instances with different configurations
(testing, development, production) and makes your code more modular and testable.'''
def create_app():
    #Create a Flask application instance
    app = Flask(__name__)
    
    # 🔒 SECURITY: Enable auto-escaping for all templates to prevent XSS
    # This automatically escapes HTML characters in {{ variable }} expressions
    app.jinja_env.autoescape = True

    # Load configuration from config.py
    '''app.config.from_pyfile('config.py')''' # Doing this way, we load the whole content of the config.py file (imports, database URL, comments, etc). 
    # Since we want to load only the Config class, we need to do the following:
    app.config.from_object('config.Config') # This way, we load only the Config class from the config.py file.

    # This is the connection between the Flask app and the SQLAlchemy database, which is initialized.
    db.init_app(app)

    # This is the connection between the Flask app, the SQLAlchemy database and the Migrate database. It allows the app to manage database migrations.
    migrate.init_app(app, db) # Now, both SQLAlchemy and Migrate are connected to Flask app.

   
    # --- CORS Configuration Explanation ---
    # The following code sets up Cross-Origin Resource Sharing (CORS) for the Flask app.
    # It enables CORS using the allowed origins defined in config.py. This prevents unexpected
    # cross-origin requests from being accepted while still allowing the trusted frontends to
    # communicate with the backend.
    # 
    # 1. The list comprehension:
    #    allowed_origins = [
    #        origin.strip()
    #        for origin in app.config.get('CORS_ORIGINS', [])
    #        if origin and origin.strip()
    #    ]
    #    - This collects all origins (domains) allowed to access the backend, as defined in the app's config (CORS_ORIGINS).
    #    - 'for' iterates over each origin in the list.
    #    - 'if' filters out any empty or whitespace-only strings.
    #    - 'origin.strip()' removes leading/trailing whitespace from each origin string.
    #
    # 2. The CORS() call:
    #    CORS(
    #        app,
    #        resources={
    #            r"/*": {
    #                "origins": allowed_origins,
    #                "methods": ["GET", "POST", "OPTIONS"],
    #                "allow_headers": ["Content-Type", "Authorization"],
    #            }
    #        },
    #    )
    #    - 'resources' defines which routes CORS applies to. Here, r"/*" (a raw string) means "all routes".
    #    - 'origins' restricts which domains can make requests (using the cleaned list above).
    #    - 'methods' specifies which HTTP methods are allowed from cross-origin requests.
    #    - 'allow_headers' (should be 'allowed_headers', but Flask-CORS uses 'allow_headers') lists which headers can be sent by the client.
    #    - 'Headers' are the information that the client sends to the server.
    #    - This setup ensures only trusted frontends (like your React app on localhost:3000) can interact with the backend, and only with safe methods and headers.

    allowed_origins = [
        origin.strip()  # Clean up each origin string from the config
        for origin in app.config.get('CORS_ORIGINS', [])
        if origin and origin.strip()  # Skip empty or whitespace-only entries
    ]
    CORS(
        app,
        resources={
            r"/*": {  # Apply CORS to all routes (the 'r' means "raw string", so backslashes are not escaped)
                "origins": allowed_origins,
                "methods": ["GET", "POST", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],  # Only allow these headers from the client
            }
        },
    )

    # Initialize Flask-Login
    login_manager.init_app(app)

    # Set where to redirect the user if they are not logged in.
    login_manager.login_view = 'login'
    login_manager.login_message = 'Please login to access this page.'
    
    # Initialize CSRF protection
    csrf.init_app(app)
    
    # Initialize rate limiting
    limiter.init_app(app)
    
    # Add security headers
    @app.after_request # The method 'after_request' is a Flask decorator that runs after each request.
    def add_security_headers(response):
        """Add comprehensive security headers to all responses"""
        if app.config.get('SECURITY_HEADERS_ENABLED', True):

            # Prevent clickjacking by telling browsers not to allow this site to be displayed in a frame or iframe.
            # This helps protect your site from UI redress attacks (where a malicious site tries to trick users into clicking on something different from what they perceive).
            response.headers['X-Frame-Options'] = 'DENY'  # 'response' is a Flask Response object representing the HTTP response that will be sent to the client.
            # You can set headers on it to control browser behavior and enhance security.

            # Prevent MIME type sniffing by instructing browsers to strictly follow the declared Content-Type of files. MIME stands for Multipurpose Internet Mail Extensions.
            # This stops browsers from trying to guess (sniff) the file type, which can prevent certain types of attacks where a file is interpreted as something more dangerous than intended.
            response.headers['X-Content-Type-Options'] = 'nosniff'

            # Enable basic cross-site scripting (XSS) protection in browsers that support this header.
            # This tells the browser to block the page if it detects reflected XSS attacks.
            # Note: Modern browsers may ignore this header, but it can still provide some protection in older browsers.
            response.headers['X-XSS-Protection'] = '1; mode=block'
            
            # 🔒 CRITICAL: Content Security Policy - Blocks malicious scripts
            # This prevents execution of any inline scripts or external scripts from untrusted sources
            csp_policy = (
                "default-src 'self'; "                    # Only allow resources from same origin
                "script-src 'self' 'unsafe-inline'; "     # Allow scripts from same origin and inline (for onclick handlers)
                "style-src 'self' 'unsafe-inline'; "      # Allow styles from same origin and inline
                "img-src 'self' data:; "                   # Allow images from same origin and data URLs
                "font-src 'self'; "                       # Allow fonts from same origin
                "connect-src 'self'; "                     # Allow AJAX/fetch requests to same origin only
                "form-action 'self'; "                     # Allow form submissions to same origin only
                "base-uri 'self'; "                        # Prevent base tag injection
                "object-src 'none'; "                      # Block plugins like Flash
                "upgrade-insecure-requests; "              # Upgrade HTTP to HTTPS automatically
                "block-all-mixed-content"                  # Block mixed HTTP/HTTPS content
            )
            response.headers['Content-Security-Policy'] = csp_policy
            
            # Force HTTPS in production (when cookie secure is enabled)
            if app.config.get('SESSION_COOKIE_SECURE'):
                # This header enforces HTTP Strict Transport Security (HSTS), telling browsers to only use HTTPS for future requests to this domain.
                # 'max-age=31536000' means the browser should remember to enforce HTTPS for 1 year (in seconds).
                # 'includeSubDomains' applies this rule to all subdomains as well.
                response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
                
            # 🔒 Additional security headers
            response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'  # Control referrer information
            response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'  # Disable dangerous APIs
            
        return response

    # User loader function tells Flask-Login how to load a user by ID
    # Flask-Login stores only the user ID in the session
    # When it needs user info, it calls this function to get the full User object
    # Without this, Flask-Login can't work!
    @login_manager.user_loader # This decorator registers this function with Flask-Login.
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))
    
    from app import routes # Import the routes.py file from the app folder.
    routes.register_routes(app) # Register the routes with the Flask app.

    # Initialize Flask-Admin (admin panel)
    # This creates a visual web interface at /admin for database management
    # Only accessible by authenticated users with is_admin=True
    from app.admin import init_admin
    init_admin(app)

    # This returns the configured Flask application instance.
    return app 
    