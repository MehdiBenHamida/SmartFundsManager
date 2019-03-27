"""
 # Title: Smart Fund Manager
 # File: ProductController.py
 # Description: Product CRUD routes definitions
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

import json
from flask import Blueprint, Response, request
from SmartFundsManagerAPI.Utilities.Logger import *

# create a new blueprint for the controller
product = Blueprint('product', __name__)


@product.route('/product', methods=['POST'])
def add_product():
    pass

