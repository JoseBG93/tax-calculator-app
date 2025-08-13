# Import Flask functions for routing
from flask import render_template, current_app  # current_app is a special Flask's object that represents the current application instance.
from app import db

# Basic route to test the application
# We use current_app inside the route function, not as a decorator.
def index():
  return "Tax Calculator Pro is running!"

# This function will register routes with the app
def register_routes(app):
  app.add_url_rule('/', 'index', index) # When the user visits the root URL, the index function will be called, showing the message "Tax Calculator Pro is running!"
  app.add_url_rule('/index','index_alt', index) # When the user visits the /index URL, the index_alt function will be called, showing the message "Tax Calculator Pro is running!"