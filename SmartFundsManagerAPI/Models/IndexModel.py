from SmartFundsManagerAPI import db


class Index(db.model):
    """
    The main index model in the application
    Inherits from the db.model
    """
    # TODO: complete the class definition and complete the docstring

    pass


# TODO: do not commit this for the first project format

class Product(db.Model):
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

    
