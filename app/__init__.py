from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config

def create_app():
    #initialice app
    app = Flask(__name__)
    # adding bootstrap
    bootstrap = Bootstrap(app)
    # app config (from config.py)
    app.config.from_object(Config)    

    return app

