from app import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)