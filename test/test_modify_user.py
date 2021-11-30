# -*- coding: utf-8 -*-
from model.user import User


def test_modify_user_name(app):
    modify_user_params = User(firstname="Piter")
    app.session.login(username="admin", password="secret")
    app.user.modify(modify_user_params)
    app.session.logout()
