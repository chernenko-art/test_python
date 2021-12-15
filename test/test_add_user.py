# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app, json_users):
    # get current user list
    user = json_users
    old_user_list = app.user.get_contact_list()
    app.user.create(user)
    assert len(old_user_list) + 1 == app.user.count()
    # get new user list
    new_user_list = app.user.get_contact_list()
    # add new user
    old_user_list.append(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
