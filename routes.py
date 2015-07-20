"""
Routes and views for the bottle application.
"""

import os
import json

from bottle import route, view, static_file
from datetime import datetime


config = { "secret_key" : "my developer secret value" }
if os.getenv("MY_CONFIG"): # you can define the setting in your Azure Web App
                           # by setting "MY_CONFIG" in the Appsettings.
    config = json.loads(os.getenv("MY_CONFIG"))
        

@route('/static/<filepath:path>')
def server_static(filepath):
    """Handler for static files, used with the development server.
    When running under a production server such as IIS or Apache,
    the server should be configured to serve the static files."""
    return static_file(filepath, root="static/")

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        secret = config.get("secret_key")        
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
