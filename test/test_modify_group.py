# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    modify_group_params = Group(name="New Name")
    app.group.modify_first_group(modify_group_params)
