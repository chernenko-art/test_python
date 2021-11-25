# -*- coding: utf-8 -*-
from model.user import User


def test_CreateUser(app):
    send_test_user_params = User(
        firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments", company="Google",
        address="Russia", home="Moscow", mobile="169421+", work="Google", fax="14481561", email="eva@mail.ru",
        email2="no", email3="no", homepage="no", phone2="+89945669", bday=12, bmounth="'October'", byear="1991",
        aday="'25'", amonth="'November'", ayear="2015", address2="Rome", notes="No"
    )
    app.session.login(username="admin", password="secret")
    app.user.create(send_test_user_params)
    app.session.logout()










