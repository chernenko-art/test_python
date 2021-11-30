# -*- coding: utf-8 -*-


def test_delete_user(app):
    app.user.delete()
