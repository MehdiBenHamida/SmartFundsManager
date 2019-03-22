"""
 # Title: Smart Fund Manager
 # File: Index.py
 # Description: The application default controller
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

import datetime
from flask import Blueprint, jsonify, Response, request
from SmartFundsManagerAPI.Utilities.Logger import *

# create a new blueprint for the controller
index = Blueprint('index', __name__)


@index.route('/')
def home():
    """
    The main index controller in the application
    :return: flask response
    """
    try:
        log_info("", "")
        response_body = {
            'application': "Smart Funds Manager",
            'version': pkg_resources.require("SmartFundsManagerAPI")[0].version,
            'author': "Mèhdi Ben Hamida",
            'copyrights': "Copyright (c) " + str(datetime.now().year) + ". All rights are reserved."
        }
        resp = Response(jsonify(response_body), status=200, mimetype='application/json')
        return resp
    except Exception as e:
        log_error("", "")

