# Import Flask functions for routing
from flask import (
  Flask,
  current_app,    # Gives access to the Flask application context (e.g., for config or logging)
  render_template, # Renders HTML templates with variables
  request,        # Handles incoming HTTP request data (form, args, etc.)
  redirect,       # Redirects the client to a different URL
  url_for,        # Generates URLs for routes/functions
  session,        # Stores user session data between requests
  flash,          # Sends one-time messages to the next request (useful for notifications)
  abort           # Aborts a request with an HTTP error code (e.g., 404, 403)
    )

app = Flask(__name__)


def index():
  return render_template('index.html')


@app.route('/login')
def login():
  """
  This function will handle the login process.
  It will render the login template and handle the login form submission.
  """
  if request.method == 'GET': # GET stands for get the form data. In other words, the user is requesting the login page.
    # You might want to render the login page here, or simply pass for now
    return render_template('login.html')

  elif request.method == 'POST':  # POST stands for post the form data. In other words, the user is submitting the login form.
    # Process login... extracting the form data
    username = request.form.get('username', '').strip() # When user submits a form with "name='username'", Flask stores it in request.form.
    # 'get()' is a method that retrieves the value of the 'username', and typing '' after allows to avoid app crashing if the user doesn't enter a username.
    password = request.form.get('password', '').strip()
    # Authenticate the user
    if username == 'jose' and password == 'alfafar2025':
      session['logged_in'] = True
      session['username'] = username
      return redirect(url_for('dashboard'))
    else:
      # Login failed
      return "Invalid credentials. Please try again."
    

@app.route('/dashboard')
def dashboard():
  """
  This function will handle the dashboard process.
  It will render the dashboard template and handle the dashboard form submission.
  """
  return render_template('dashboard.html')

def register():
  """
  This function will handle the registration process.
  It will render the registration template and handle the registration form submission.
  """
  return render_template('register.html')

def logout():
  """
  This function will handle the logout process.
  It will redirect the user to the login page.
  """
  session.clear() # Clears all session data
  return redirect(url_for('login'))

# This function will register app routes
def register_routes(app):
  """
  This function registers all app routes.
  """
  app.add_url_rule('/', 'root', index) # When the user visits the root URL through either port 5000 or 5001, the index function will be called, showing the message "Tax Calculator Pro is running!"
  app.add_url_rule('/index','index', index) # Also, user can type '/index' in the browser, and the same message will be shown.
  app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
  app.add_url_rule('/dashboard', 'dashboard', dashboard)
  app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
  app.add_url_rule('/logout', 'logout', logout, methods=['POST'])