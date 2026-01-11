from app import db
from sqlalchemy import Column, Integer, ForeignKey


class Participation(db.Model):
    __tablename__ = 'participation'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    league_id = Column(Integer, ForeignKey('league.id'), primary_key=True)
    rank = Column(Integer, nullable=False, default=0)