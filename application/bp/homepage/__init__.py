"""
This module defines the homepage Blueprint.
It includes routes for the homepage and about page.
"""

from flask import Blueprint, render_template

# Declare Blueprint object
homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route('/')
def home():
    """Render the homepage."""
    return render_template('homepage.html')

@homepage.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')
