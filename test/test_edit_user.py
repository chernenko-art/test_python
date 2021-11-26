# -*- coding: utf-8 -*-
from model.user import User


def test_edit_first_group(app):
    edit_test_user_params = User(
        firstname="EDIT_Eva", middlename="EDIT_Semenova", lastname="EDIT_Cocs", nickname="EDIT_Coca",
        title="EDIT_Nocomments", company="EDIT_Google", address="EDIT_Russia", home="EDIT_Moscow",
        mobile="169421+", work="Google", fax="14481561", email="eva@mail.ru", email2="no", email3="no",
        homepage="no", phone2="+89945669", bday=12, bmounth="'October'", byear="1991", aday="'25'",
        amonth="'November'", ayear="2015", address2="Rome", notes="No"
    )
    app.session.login(username="admin", password="secret")
    app.user.edit(edit_test_user_params)
    app.session.logout()
