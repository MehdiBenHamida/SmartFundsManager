"""
 # Title: Smart Fund Manager
 # File: IndexController.py
 # Description: The application default controller
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

import json
import datetime
from flask import Blueprint, Response, request
from SmartFundsManagerAPI.Utilities.Logger import *

# create a new blueprint for the controller
index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
def home():
    """
    The main index controller in the application
    :return: flask response
    """
    try:
        log_info("answer for root uri",  request.remote_addr)
        response_body = {
            'application': "Smart Funds Manager",
            'version': "0.0.0",  # TODO: pkg_resources.require("SmartFundsManagerAPI")[0].version,
            'author': "Mèhdi Ben Hamida",
            'copyrights': "Copyright (c) 2019-" + str(datetime.now().year) + ". All rights are reserved.",
            'error': False,
        }
        resp = Response(json.dumps(response_body), status=200, mimetype='application/json')
        return resp
    except Exception as e:
        log_error("Internal server error --> " + str(e), request.remote_addr)
        response_body = {
            'message': "Internal server error --> " + str(e),
            'error': True,
        }
        resp = Response(json.dumps(response_body), status=500, mimetype='application/json')
        return resp


# TODO: an empty template for a typical controller
@index.route('/template')
def template():
        try:
            # log the operation as an info with the remote user address
            log_info("answer for template uri", request.remote_addr)
            # call a method and makxe results
            # make the response body object
            response_body = {
                'message': "this is the template message",
                'error': False,
            }
            # make a flask response
            resp = Response(json.dumps(response_body), status=200, mimetype='application/json')
            return resp
        except Exception as e:
            # in case of exception is generated
            # log an error message with the remote user address
            response_body = {
                'message': "Internal server error --> " + str(e),
                'error': True,
            }
            # make a flask response
            resp = Response(json.dumps(response_body), status=500, mimetype='application/json')
            return resp
