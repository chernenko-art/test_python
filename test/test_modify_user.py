# -*- coding: utf-8 -*-
from model.user import User


def test_modify_user_name(app):
    modify_user_params = User(firstname="Piter")
    app.user.modify(modify_user_params)
