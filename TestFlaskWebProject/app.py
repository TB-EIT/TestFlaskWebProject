"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import datetime

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "<h1>Hello World!</h1><p>App Version 2.0.0</p>"

@app.route('/watch')
def watch():
    return f"Current Time: {datetime.datetime.now()}"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
