from flask import Flask
from . import routes
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['BUNDLE_ERRORS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@hostname/dbname"

jwt = JWTManager(app)

routes.create_route(app)
db = SQLAlchemy(app)
from application import models
db.create_all()

