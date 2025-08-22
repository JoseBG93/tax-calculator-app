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


db = SQLAlchemy()
migrate = Migrate()

'''Application Factory Pattern: The following function creates and configures a Flask application instance.
Why use this pattern? It allows you to create multiple app instances with different configurations
(testing, development, production) and makes your code more modular and testable.'''
def create_app():
    #Create a Flask application instance
    app = Flask(__name__)

    # Load configuration from config.py
    '''app.config.from_pyfile('config.py')''' # Doing this way, we load the whole content of the config.py file (imports, database URL, comments, etc). 
    # Since we want to load only the Config class, we need to do the following:
    app.config.from_object('config.Config') # This way, we load only the Config class from the config.py file.

    # This is the connection between the Flask app and the SQLAlchemy database, which is initialized.
    db.init_app(app)

    # This is the connection between the Flask app, the SQLAlchemy database and the Migrate database. It allows the app to manage database migrations.
    migrate.init_app(app, db) # Now, both SQLAlchemy and Migrate are connected to Flask app.

    # Enable CORS for all routes and origins. It allows your frontend to communicate with your backend.
    CORS(app)


    from app import routes # Import the routes.py file from the app folder.
    routes.register_routes(app) # Register the routes with the Flask app.

    # This returns the configured Flask application instance.
    return app 
    