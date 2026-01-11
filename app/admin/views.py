from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_labels = {
        'id': 'Mã số',
        'name': 'Tên ingame',
        'username': 'Tên đăng nhập',
        'password': 'Mật khẩu',
    }
    column_exclude_list = ['username', 'password', 'avt']

    form_columns = ('name', 'username', 'password')


class LeagueView(ModelView):
    column_labels = {
        'id': 'Mã số',
        'name': 'Tên giải đấu',
        'format': 'Thể thức',
        'status': 'Trạng thái',
    }
    # column_exclude_list = ['username', 'password', 'avt']

    form_columns = ('name', 'format')


class FormatView(ModelView):
    column_labels = {
        'id': 'Mã số',
        'name': 'Tên thể thức',
        'teamsize': 'Số thành viên mỗi đội'
    }
    # column_exclude_list = ['username', 'password', 'avt']

    form_columns = ('name', 'teamsize')