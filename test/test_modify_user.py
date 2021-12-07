# -*- coding: utf-8 -*-
from model.user import User


def test_modify_user_name(app):
    # check what groups is not empty
    if app.user.count() == 0:
        user = User(
            firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments",
            company="Google", address="Russia", home="Moscow", mobile="169421+", work="Google", fax="14481561",
            email="eva@mail.ru", email2="no", email3="no", homepage="no", phone2="+89945669", bday=12,
            bmonth="'October'", byear="1991", aday="'25'", amonth="'November'", ayear="2015", address2="Rome",
            notes="No"
        )
        app.user.create(user)
    # start test
    modify_user = User(firstname="Piter", lastname="Ivanov")
    old_user_list = app.user.get_user_list()
    modify_user.id = old_user_list[0].id
    app.user.modify(modify_user)
    new_user_list = app.user.get_user_list()
    assert len(old_user_list) == len(new_user_list)
    old_user_list[0] = modify_user
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
