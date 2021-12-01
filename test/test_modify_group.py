# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    # check what groups is not empty
    if app.group.count() == 0:
        group_params = Group(name="Lol", header="Happy", footer="Gays")
        app.group.create(group_params)
    # start test
    modify_group_params = Group(name="New Name")
    app.group.modify_first_group(modify_group_params)
