# -*- coding: utf-8 -*-
from model.user import User
from random import randrange

def test_delete_user(app):
    # check what groups is not empty
    if app.user.count() == 0:
        user = User(
            firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments",
            company="Google", address="Russia", home="Moscow", mobile="169421+", work="Google", fax="14481561",
            email="eva@mail.ru", email2="no", email3="no", homepage="no", phone2="+89945669", bday=12,
            bmonth="'October'", byear="1991", aday="'25'", amonth="'November'", ayear="2015", address2="Rome", notes="No"
        )
        app.user.create(user)
    # get current user list
    old_user_list = app.user.get_user_list()
    # get index for delete random user
    index = randrange(len(old_user_list))
    app.user.delete_by_index(index)
    assert len(old_user_list) - 1 == app.user.count()
    # get new user list
    new_user_list = app.user.get_user_list()
    # del first user
    old_user_list.pop(index)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
