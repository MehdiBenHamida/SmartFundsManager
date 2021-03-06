"""
 # Title: Smart Fund Manager
 # File: ProductModel.py
 # Description: Define product data structure and main CRUD methods
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

from SmartFundsManagerAPI import db, ma


# TODO: do not commit this for the first project format

class Product(db.Model):
    """
    Class product
    Attributes:
        id (int): The unique identifier of a product
        name (str): The name of the product
        description  (str): The complete description of a product
        price (float): The price of the product
        quantity (int): Integer representing the quantity of the product
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')


# initialize the schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)
