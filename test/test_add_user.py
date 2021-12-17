# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app, db, json_users, check_ui):
    # get current user list from db
    user = json_users
    old_user_list = db.get_user_list()
    app.user.create(user)
    # get new user list from db
    new_user_list = db.get_user_list()
    # add new user
    old_user_list.append(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)
