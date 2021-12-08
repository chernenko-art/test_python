# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app):
    user = User(
        firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments", company="Google",
        address="Russia", home="+798774", mobile="+7 166 94 21", work="8-(913)-794-61 58", fax="14481561", email="eva@mail.ru",
        email2="no", email3="no", homepage="no", phone2="+89945669", bday=12, bmonth="'October'", byear="1991",
        aday="'25'", amonth="'November'", ayear="2015", address2="Rome", notes="No"
    )
    # get current user list
    old_user_list = app.user.get_contact_list()
    app.user.create(user)
    assert len(old_user_list) + 1 == app.user.count()
    # get new user list
    new_user_list = app.user.get_contact_list()
    # add new user
    old_user_list.append(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
