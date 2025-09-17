"""Flask application entry point.

This module serves as the entry point for the Tax Calculator Pro application.
It creates and runs a Flask development server using the application factory
pattern.

Usage:
    python run.py

The application will start on http://127.0.0.1:5000 with debug mode enabled.
"""
import os
import glob

# Import the create_app function from module '__init__.py', within the app directory 
from app import create_app


def main():
    """Initialize and run the Flask application."""
    # Create Flask instance using the application factory pattern
    app = create_app()
    
    # Set development environment
    os.environ['FLASK_ENV'] = 'development'
    
    # Add template files to Flask's file watcher for auto-reload
    template_files = glob.glob('app/templates/*.html')
    
    # Run the Flask development server with proper configuration
    # Port can be set via environment variable or defaults to 5000
    port = int(os.environ.get('PORT', 5000))
    
    app.run(
        debug=True,
        use_reloader=True,
        extra_files=template_files,
        host='127.0.0.1',
        port=port
    )


if __name__ == '__main__':
    main()
