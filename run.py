'''
  This is the entry point of the Flask application.
  It imports the create_app function from the app package and runs the Flask development server.
  When you run "python run.py", this file will start your web application on port 5000.
  '''
# We're gonna to import the create_app function from the app package, it means, "get the create_app function from the app package" (app/ folder, which contains the __init__.py file).
from app import create_app

# Create the Flask application instance using the factory pattern
app = create_app()

# The following condition ensures the app only runs if the script (run.py) is executed directly (not imported as a module by another file).
if __name__ == '__main__':
   # Run the Flask development server
   # debug=True enables auto-reload when you change code files
   # host='0.0.0.0' makes the app accessible from other devices on your network. Otherwise, host='127.0.0.1' means the app is only accessible from the local machine.
  app.run(debug=True)
