from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='hithere'
app.config['SQLALCHEMY_DATABASE_URI']='SQLITE:///pitch.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)


from app import views
