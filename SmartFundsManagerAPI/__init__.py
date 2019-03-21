from flask import Flask


app = Flask(__name__)

from SmartFundsManagerAPI.Controllers.Index import index


app.register_blueprint(index)
