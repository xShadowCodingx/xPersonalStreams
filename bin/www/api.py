# This is the main API entry point

# Module Imports
from flask import Flask

# App Initialization
app = Flask(__name__, static_folder="public")

# Blueprint Imports
from .route_blueprints import index

# Blueprint Registration
app.register_blueprint(index)