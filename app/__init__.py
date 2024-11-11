from flask import Flask
from app.controller.UserController import user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app():
    #create app    
    app = Flask(__name__)

    #config migrate
    #localhost
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3307/simple'
    #docker
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db:3306/simple'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128), nullable=False)
        email = db.Column(db.String(128), unique=True, nullable=False)
        def __repr__(self):
            return f"<User {self.name}>"

    #config routes
    app.register_blueprint(user, url_prefix='/api')


    return app