'''
  This is the Flask's entry point.
  It imports the create_app function from the __init__ module within the app folder, and runs a Flask development server.
  When you run "python run.py" in the terminal, this file starts your web app on port 5000.
  '''
# We're gonna to import the create_app function from __init__.py file, within the app folder. 
from app import create_app

# Create a Flask instance using the factory pattern
app = create_app()

# The following condition ensures the app only runs if the script (run.py) is executed directly, not imported as a module by another file.
if __name__ == '__main__':
   # Run the Flask development server
   # debug=True enables auto-reload when you change Python code files
   # host='0.0.0.0' makes the app accessible from other devices on your network. Otherwise, host='127.0.0.1' means the app is only accessible from the local machine.
   import os
   import glob
   os.environ['FLASK_ENV'] = 'development'
   # Add template files to Flask's file watcher for auto-reload
   template_files = glob.glob('app/templates/*.html')
   app.run(debug=True, use_reloader=True, extra_files=template_files, host='127.0.0.1', port=5000)
