from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avt = Column(String(300), nullable=False, default='https://res.cloudinary.com/dxowugugq/image/upload/v1768168766/aolangfco/avt/default_cnrzp5.jpg')
    participations = relationship('Participation', backref='user', lazy=True)

    def __str__(self):
        return self.name