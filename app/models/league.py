import enum
from app import db
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship


class LeagueStatus(enum.Enum):
    UNDERWAY = "underway"
    FINISH = "finish"


class League(db.Model):
    __tablename__ = 'league'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    status = Column(Enum(LeagueStatus), default=LeagueStatus.UNDERWAY, nullable=False)
    format_id = Column(Integer, ForeignKey("format.id"), nullable=False)
    participations = relationship('Participation', backref='league', lazy=True)