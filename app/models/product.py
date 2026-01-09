from app import db
from sqlalchemy import Column, Integer, String, Float


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False, default=0)