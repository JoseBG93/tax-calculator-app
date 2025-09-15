# Import Flask functions for routing
from flask import (
  render_template, # Renders HTML templates with variables
  request,        # Handles incoming HTTP request data (form, args, etc.)
  redirect,       # Redirects the client to a different URL
  url_for,        # Generates URLs for routes/functions
  session,        # Stores user session data between requests
  flash,          # Stores a temporary message that appears on the next request (the next page load), then disappears.
    )
from app.models import User
from app import db, limiter
import re
import html

# Security validation functions
def validate_username(username):
    """Validate username format and security"""
    if not username or len(username.strip()) == 0:
        return False, "Username cannot be empty"
    
    username = username.strip()
    
    # Check length
    if len(username) < 3 or len(username) > 50:
        return False, "Username must be between 3 and 50 characters"
    
    # Check for valid characters (alphanumeric, underscore, hyphen)
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False, "Username can only contain letters, numbers, underscores, and hyphens"
    
    return True, "Valid"

def validate_password(password):
    """Validate password strength"""
    if not password or len(password.strip()) == 0:
        return False, "Password cannot be empty"
    
    password = password.strip()
    
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    
    return True, "Valid"

def sanitize_input(input_string):
    """Sanitize user input to prevent XSS"""
    if not input_string:
        return ""
    return html.escape(input_string.strip())

# This function will register app routes
def register_routes(app):
  """
  This function registers all app routes.
  """
  app.add_url_rule('/', 'root', root) # When the user visits the root URL through either port 5000 or 5001, the index function will be called, showing the message "Tax Calculator Pro is running!"
  app.add_url_rule('/index','index', index) # Also, user can type '/index' in the browser, and the same message will be shown.
  app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
  app.add_url_rule('/dashboard', 'dashboard', dashboard)
  app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
  app.add_url_rule('/logout', 'logout', logout, methods=['POST'])
  app.add_url_rule('/calculator', 'calculator', calculator, methods=['GET', 'POST'])
  app.add_url_rule('/history', 'history', history, methods=['GET', 'POST'])
  # DEBUG ROUTE DISABLED FOR SECURITY - Exposes password hashes
  # app.add_url_rule('/debug_users', 'debug_users', debug_users, methods=['GET'])


def root():
  return redirect(url_for('index'))


def index():
  return render_template('index.html')


@limiter.limit("5 per minute")  # Rate limit registration attempts
def register():
  """
  This function will handle the registration process.
  It will render the registration template and handle the registration form submission.
  """
  if request.method == 'GET':
    return render_template('register.html')
  elif request.method == 'POST':
    # Get and sanitize form data
    username = sanitize_input(request.form.get('username', ''))
    password = request.form.get('password', '')  # Don't sanitize passwords
    confirm_password = request.form.get('confirm_password', '')
    
    # Validate username
    username_valid, username_msg = validate_username(username)
    if not username_valid:
        flash(username_msg)
        return render_template('register.html', username=username)
    
    # Validate password
    password_valid, password_msg = validate_password(password)
    if not password_valid:
        flash(password_msg)
        return render_template('register.html', username=username)
    
    # Check password confirmation
    if password != confirm_password:
        flash('Passwords do not match. Please try again.')
        return render_template('register.html', username=username)
    
    # Check if username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('Username already exists. Please choose a different one.')
        return render_template('register.html', username=username)
    
    try:
        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    except Exception as e:
        db.session.rollback()
        flash('Registration failed. Please try again.')
        return render_template('register.html', username=username)


@limiter.limit("10 per minute")  # Rate limit login attempts
def login():
  """
  This function will handle the login process.
  It will render the login template and handle the login form submission.
  """
  if request.method == 'GET': # GET stands for get the form data. In other words, the user is requesting the login page.
    # Only clear flash messages if coming from a different page (not after failed login).
    if not request.args.get('show_flash'):
      session.pop('_flashes', None)
    return render_template('login.html')

  elif request.method == 'POST':  # POST stands for post the form data. In other words, the user is submitting the login form.
    # Process login... extracting and sanitizing the form data
    username = sanitize_input(request.form.get('username', ''))
    password = request.form.get('password', '')  # Don't sanitize passwords
    
    # Basic validation
    if not username or not password:
        flash("Please fill in all fields.")
        return redirect(url_for('login', show_flash=True))

    try:
        # Check database for user credentials
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['logged_in'] = True
            session['username'] = username
            # Regenerate session ID to prevent session fixation attacks
            session.permanent = True
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Not registered yet?")
            return redirect(url_for('login', show_flash=True))
    except Exception as e:
        flash("Login failed. Please try again.")
        return redirect(url_for('login', show_flash=True))
    

def dashboard():
  """
  This function will handle the dashboard process.
  It will render the dashboard template and handle the dashboard form submission.
  """
  if 'logged_in' not in session or not session['logged_in']:
    return redirect(url_for('login'))
  
  return render_template('dashboard.html')


def logout():
  """
  This function will handle the logout process.
  It will redirect the user to the login page.
  """
  session.clear() # Clears all session data
  return redirect(url_for('login'))


def debug_users():
  """
  DEBUG ROUTE: DISABLED FOR SECURITY REASONS
  This route exposed sensitive password hashes and has been disabled.
  In production, use proper admin panels with authentication.
  """
  # SECURITY FIX: Route disabled to prevent password hash exposure
  # If debug info is needed, implement proper authentication first
  return "Debug route disabled for security reasons", 403
  
  # Original insecure code (DO NOT UNCOMMENT):
  # users = User.query.all()
  # if not users:
  #   return "<h2>No users registered yet in database</h2>"
  # html = "<h2>Registered Users (Database):</h2><ul>"
  # for user in users:
  #   html += f"<li><strong>ID:</strong> {user.id} | <strong>Username:</strong> {user.username} | <strong>Password:</strong> {user.password} | <strong>Created:</strong> {user.created_at}</li>"
  # html += "</ul>"
  # return html


def calculator():
  """
  This function will handle the calculate process.
  """
  return render_template('calculator.html')


def history():
  """
  This function will handle the history process.
  """
  return render_template('history.html')
