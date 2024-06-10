# wsgi.py
from app import app

# Vercel will look for the `app` callable.
application = app
