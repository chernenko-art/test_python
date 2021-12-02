# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    # check what groups is not empty
    if app.group.count() == 0:
        group_params = Group(name="Lol", header="Happy", footer="Gays")
        app.group.create(group_params)
    # start test
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
