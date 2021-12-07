# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    # check what groups is not empty
    if app.group.count() == 0:
        group = Group(name="Lol", header="Happy", footer="Gays")
        app.group.create(group)
    # start test
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # delete first element
    old_groups.pop(0)
    assert old_groups == new_groups
