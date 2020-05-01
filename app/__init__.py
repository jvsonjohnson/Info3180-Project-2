from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
ENV = 'dev'
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "secretkey"

if ENV == 'dev':
    app.debug = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:project1@localhost/project1"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
else:
    app.debug = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = ""
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import views  # nopep8
