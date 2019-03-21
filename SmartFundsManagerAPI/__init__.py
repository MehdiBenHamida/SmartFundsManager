from flask import Flask
from SmartFundsManagerAPI.Controllers.Index import index


app = Flask(__name__)
app.register_blueprint(index, url_prefix='/api')
