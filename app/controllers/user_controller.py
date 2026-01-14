from app import app
from flask import render_template
from app.extensions import login
from app.services import get_user


@app.route('/user-login')
def user_login():
    return render_template('/pages/login.html')


@login.user_loader
def load_user(user_id):
    return get_user(user_id=user_id)