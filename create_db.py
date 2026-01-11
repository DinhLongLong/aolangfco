from app import app, db


with app.app_context():
    from app.models import *
    db.create_all()