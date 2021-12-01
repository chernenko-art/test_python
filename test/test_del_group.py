# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    # check what groups is not empty
    if app.group.count() == 0:
        group_params = Group(name="Lol", header="Happy", footer="Gays")
        app.group.create(group_params)
    # start test
    app.group.delete_first_group()
