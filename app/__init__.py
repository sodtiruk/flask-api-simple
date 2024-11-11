from flask import Flask

from .routes import main

from app.controller.UserController import user

def create_app():
    #create app    
    app = Flask(__name__)


    app.register_blueprint(main)

    app.register_blueprint(user, url_prefix='/api')


    return app