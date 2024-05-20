#Fabrica de App
from flask import Flask
from .config import configure
#from views import index

# Fazemos dentro da função
def create_app():
    app = Flask(__name__)
    configure(app)
    return app