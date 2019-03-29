"""
 # Title: Smart Fund Manager
 # File: ErrorModel.py
 # Description: Error response structure
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

from SmartFundsManagerAPI import ma


class ErrorSchema(ma.Schema):
    class Meta:
        fields = ('message', 'code', 'error')


# initialize the schema
error_schema = ErrorSchema(strict=True)

