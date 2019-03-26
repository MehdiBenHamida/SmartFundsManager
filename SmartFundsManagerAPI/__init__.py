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

# create the flask app here
app = Flask(__name__)

# apply marshmallow flask on the flask application
ma = Marshmallow(app)

# define and apply the rules of CORS
cors = CORS(app)

# import the blueprints
from SmartFundsManagerAPI.Controllers.Index import index

# register the blueprints here
app.register_blueprint(index)
