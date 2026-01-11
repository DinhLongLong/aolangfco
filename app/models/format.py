from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Format(db.Model):
    __tablename__ = 'format'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    teamsize = Column(Integer, nullable=False)
    leagues = relationship('League', backref='format', lazy=True)

    def __str__(self):
        return self.name
