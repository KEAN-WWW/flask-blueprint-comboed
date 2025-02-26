"""
This is the main entry point of the Flask application.
It initializes the Flask app and registers blueprints.
"""

from flask import Flask
from application.bp.homepage import homepage  # Import the Blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(homepage)

if __name__ == '__main__':
    app.run(debug=True)