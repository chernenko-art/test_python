# -*- coding: utf-8 -*-
from model.user import User
from random import randrange


def test_modify_user_name(app, json_users):
    # check what groups is not empty
    if app.user.count() == 0:
        user = json_users
        app.user.create(user)
    modify_user = User(firstname="Piter", lastname="Ivanov")
    # get current user list
    old_user_list = app.user.get_contact_list()
    # get index for modify random user
    index = randrange(len(old_user_list))
    # remember user id
    modify_user.id = old_user_list[index].id
    app.user.modify_by_index(index, modify_user)
    assert len(old_user_list) == app.user.count()
    # get new user list
    new_user_list = app.user.get_contact_list()
    # replace first user to modify user
    old_user_list[index] = modify_user
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
