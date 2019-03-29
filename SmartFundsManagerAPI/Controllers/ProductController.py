"""
 # Title: Smart Fund Manager
 # File: ProductController.py
 # Description: Product CRUD routes definitions
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

import json
from flask import Blueprint, Response, request
from SmartFundsManagerAPI.Models.ProductModel import *
from  SmartFundsManagerAPI.Models.ErrorModel import *
from SmartFundsManagerAPI.Utilities.Logger import *

# create a new blueprint for the controller
product = Blueprint('product', __name__)

# TODO: does not work properly, please fix it!
@product.route('/product', methods=['POST'])
def add_product():
    try:
        log_info("Add a new product", request.remote_addr)
        data = json.loads(request.data)
        name = data['name']
        description = data['description']
        price = data['price']
        qty = data['qty']
        new_product = Product(name, description, price, qty)
        db.session.add(new_product)
        db.session.commit()
        resp = Response(product_schema.jsonify(new_product), status=500, mimetype='application/json')
        return resp
    except Exception as e:
        log_error("Internal server error --> " + str(e), request.remote_addr)
        response_body = {
            'message': "Internal server error --> " + str(e),
            'code': 500,
            'error': True,
        }
        resp = Response(json.dumps(response_body), status=500, mimetype='application/json')
        return resp

