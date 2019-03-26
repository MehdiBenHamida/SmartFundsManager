"""
 # Title: Smart Fund Manager
 # File: __init__.py
 # Description: Manage the routes of the application by registering the blueprints
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os

# make the base directory for the application
basedir = os.path.abspath(os.path.dirname(__file__))

# create the flask app here
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# initialize marshmallow
ma = Marshmallow(app)

# initialize sql_alchemy
db = SQLAlchemy(app)

# initialize cross origin policy
cors = CORS(app)

# import the blueprints
from SmartFundsManagerAPI.Controllers.IndexController import index

# register the blueprints here
app.register_blueprint(index)
