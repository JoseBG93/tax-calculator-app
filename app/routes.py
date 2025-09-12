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
from app import db

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
  app.add_url_rule('/debug_users', 'debug_users', debug_users, methods=['GET'])


def root():
  return redirect(url_for('index'))


def index():
  return render_template('index.html')


def register():
  """
  This function will handle the registration process.
  It will render the registration template and handle the registration form submission.
  """
  if request.method == 'GET':
    return render_template('register.html')
  elif request.method == 'POST':
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    confirm_password = request.form.get('confirm_password', '').strip()
    # Python does not have a native switch statement, but we can simulate it using match-case (Python 3.10+).
    # We'll use a tuple to match the different cases.
    match (password == confirm_password, bool(username and password)):
      case (False, _):
        flash('Passwords do not match. Please try again.')
        return render_template('register.html', username=username)
      case (True, False):
        flash('Please fill all fields.')
        return redirect(url_for('register'))
      case (True, True):
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))


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
    # Process login... extracting the form data
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    # Check database for user credentials
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid credentials. Not registered yet?")
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
  DEBUG ROUTE: Shows all registered users from database (REMOVE IN PRODUCTION)
  """
  users = User.query.all()
  if not users:
    return "<h2>No users registered yet in database</h2>"
  
  html = "<h2>Registered Users (Database):</h2><ul>"
  for user in users:
    html += f"<li><strong>ID:</strong> {user.id} | <strong>Username:</strong> {user.username} | <strong>Password:</strong> {user.password} | <strong>Created:</strong> {user.created_at}</li>"
  html += "</ul>"
  return html


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
