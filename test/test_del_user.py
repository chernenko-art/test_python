# -*- coding: utf-8 -*-
from model.user import User
import random
from random import randrange


def test_delete_user(app, db, json_users, check_ui):
    user = json_users
    # check what groups is not empty
    if len(db.get_user_list()) == 0:
        app.user.create(user)
    # get current user list from db
    old_user_list = db.get_user_list()
    # delete random user by id in web
    user = random.choice(old_user_list)
    app.user.delete_by_id(user.id)
    # get new user list from db
    new_user_list = db.get_user_list()
    # del first user in list
    old_user_list.remove(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)
