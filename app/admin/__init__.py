from app import db
from app.models import User, League, Format
from .views import UserView, LeagueView, FormatView
from app.extensions import admin


def init_admin():
    admin.add_view(UserView(User, db.session, name='Người chơi'))
    admin.add_view(LeagueView(League, db.session, name='Giải đấu'))
    admin.add_view(FormatView(Format, db.session, name='Thể thức'))