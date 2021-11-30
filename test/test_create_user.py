# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app):
    test_user_params = User(
        firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments", company="Google",
        address="Russia", home="Moscow", mobile="169421+", work="Google", fax="14481561", email="eva@mail.ru",
        email2="no", email3="no", homepage="no", phone2="+89945669", bday=12, bmonth="'October'", byear="1991",
        aday="'25'", amonth="'November'", ayear="2015", address2="Rome", notes="No"
    )
    app.user.create(test_user_params)
