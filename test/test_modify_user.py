# -*- coding: utf-8 -*-
import random
from model.user import User


def test_modify_user_name(app, db, json_users, check_ui):
    # check what groups is not empty
    if len(db.get_user_list()) == 0:
        user = json_users
        app.user.create(user)
    user = User(firstname="Piter", lastname="Ivanov", middlename="Sergeevich")
    # get current user list from db
    old_user_list = db.get_user_list()
    # get id for modify random user
    user_random = random.choice(old_user_list)
    user.id = user_random.id
    app.user.modify_by_id(user.id, user)
    # get new user list
    new_user_list = db.get_user_list()
    # replace first user to modify user
    old_user_list.remove(user_random)
    old_user_list.append(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)
