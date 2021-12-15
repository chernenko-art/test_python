# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_some_group(app, json_groups):
    group = json_groups
    # check what groups is not empty
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    # get index for delete random group
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # delete first element
    old_groups.pop(index)
    assert old_groups == new_groups
