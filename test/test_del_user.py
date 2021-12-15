# -*- coding: utf-8 -*-
from model.user import User
from random import randrange


def test_delete_user(app, json_users):
    user = json_users
    # check what groups is not empty
    if app.user.count() == 0:
        app.user.create(user)
    # get current user list
    old_user_list = app.user.get_contact_list()
    # get index for delete random user
    index = randrange(len(old_user_list))
    app.user.delete_by_index(index)
    assert len(old_user_list) - 1 == app.user.count()
    # get new user list
    new_user_list = app.user.get_contact_list()
    # del first user
    old_user_list.pop(index)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
