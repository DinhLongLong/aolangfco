from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import admin, login


app = Flask(__name__)


app.secret_key = "alskwglkjasdglaskdgloaiweogjalksdglas"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/aolangfcodb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

login.init_app(app)
admin.init_app(app)
from app.admin import init_admin
init_admin()