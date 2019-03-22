"""
 # Title: Smart Fund Manager
 # File: Index.py
 # Description: The application default controller
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

from flask import Blueprint
from SmartFundsManagerAPI.Utilities.Logger import *

index = Blueprint('index', __name__)


@index.route('/')
def home():
    try:
        log_info("", "")
        return "Smart Fund Manager"
    except Exception as e:
        pass

