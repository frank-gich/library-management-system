from enum import unique

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
#seting the secret key 
app.config['SECRET_KEY'] == 'af2bbabd5fe56ed015a8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookslibray.db'

db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category= 'infor'


from book_manage.forms import Upload, Borrow, LoginForm, RegistrationForm
from book_manage import routes
