# Import Flask functions for routing
from flask import (
  render_template, # Renders HTML templates with variables
  request,        # Handles incoming HTTP request data (form, args, etc.)
  redirect,       # Redirects the client to a different URL
  url_for,        # Generates URLs for routes/functions
  session,        # Stores user session data between requests
  flash,          # Stores a temporary message that appears on the next request (the next page load), then disappears.
    )
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db, limiter
from app.security_validations import validate_username, validate_password, sanitize_input, admin_required, validate_and_sanitize_username
from functools import wraps
from datetime import datetime
import re
import html


# This function will register app routes
def register_routes(app):
  """
  This function registers all app routes.
  """
  app.add_url_rule('/', 'root', root) # When the user visits the root URL through either port 5000 or 5001, the index function will be called, showing the message "Tax Calculator Pro is running!"
  app.add_url_rule('/index','index', index) # Also, user can type '/index' in the browser, and the same message will be shown.
  app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
  app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
  app.add_url_rule('/logout', 'logout', logout, methods=['POST'])
  app.add_url_rule('/dashboard', 'dashboard', dashboard)
  app.add_url_rule('/calculator', 'calculator', calculator, methods=['GET', 'POST'])
  app.add_url_rule('/history', 'history', history, methods=['GET', 'POST'])
  
  # Admin routes for user management
  app.add_url_rule('/admin', 'admin_dashboard', admin_dashboard, methods=['GET'])
  app.add_url_rule('/admin/users', 'admin_users', admin_users, methods=['GET'])
  app.add_url_rule('/admin/users/<int:user_id>/toggle', 'admin_toggle_user', admin_toggle_user, methods=['POST'])
  app.add_url_rule('/admin/users/<int:user_id>/promote', 'admin_promote_user', admin_promote_user, methods=['POST'])
  
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
    # Get form data
    raw_username = request.form.get('username', '')
    password = request.form.get('password', '')  # Don't sanitize passwords
    confirm_password = request.form.get('confirm_password', '')
    
    # 🔒 SECURITY: Enhanced username validation and sanitization
    username_valid, username, username_msg = validate_and_sanitize_username(raw_username)
    if not username_valid:
        flash(f"Username validation failed: {username_msg}")
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
            # Check if account is active
            if not user.is_active:
                flash("Your account has been disabled. Contact administrator.")
                return redirect(url_for('login', show_flash=True))
            
            # Update login statistics
            user.last_login = datetime.utcnow()
            user.login_count += 1
            db.session.commit()
            
            # Flask-Login handles session management automatically
            login_user(user, remember=True)  # remember=True creates persistent session
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Not registered yet?")
            return redirect(url_for('login', show_flash=True))
    except Exception as e:
        flash("Login failed. Please try again.")
        return redirect(url_for('login', show_flash=True))
    

@login_required  # Flask-Login automatically redirects to login if not authenticated
def dashboard():
  """
  This function will handle the dashboard process.
  It will render the dashboard template and handle the dashboard form submission.
  """
  # No need to check session manually - @login_required handles it
  return render_template('dashboard.html')


@login_required  # Only logged-in users can logout
def logout():
  """
  This function will handle the logout process.
  It will redirect the user to the login page.
  """
  logout_user()  # Flask-Login handles clearing the session
  flash('You have been logged out successfully.')
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


@login_required # Only logged-in users can access this function.
def calculator():
  """
  This function will handle the calculate process.
  """
  return render_template('calculator.html')


@login_required # Only logged-in users can access this function.
def history():
  """
  This function will handle the history process.
  """
  return render_template('history.html')


# Admin routes
@admin_required
def admin_dashboard():
    """Admin dashboard showing system statistics"""
    total_users = User.query.count()
    active_users = User.query.filter_by(is_active=True).count()
    admin_users = User.query.filter_by(is_admin=True).count()
    
    # Get recent registrations (last 5)
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         active_users=active_users,
                         admin_users=admin_users,
                         recent_users=recent_users)


@admin_required
def admin_users():
    """List all users with management options"""
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)


@admin_required
def admin_toggle_user(user_id):
    """Toggle user active status"""
    if user_id == current_user.id:
        flash("Cannot disable your own account.")
        return redirect(url_for('admin_users'))
    
    user = User.query.get_or_404(user_id)
    user.is_active = not user.is_active
    db.session.commit()
    
    status = "enabled" if user.is_active else "disabled"
    flash(f"User {user.username} has been {status}.")
    return redirect(url_for('admin_users'))


@admin_required
def admin_promote_user(user_id):
    """Toggle admin status for a user"""
    if user_id == current_user.id:
        flash("Cannot modify your own admin status.")
        return redirect(url_for('admin_users'))
    
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    
    status = "promoted to admin" if user.is_admin else "removed from admin"
    flash(f"User {user.username} has been {status}.")
    return redirect(url_for('admin_users'))
