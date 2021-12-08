# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    # check what groups is not empty
    if app.group.count() == 0:
        group = Group(name="Lol", header="Happy", footer="Gays")
        app.group.create(group)
    old_groups = app.group.get_group_list()
    # get index for delete random group
    index = randrange(len(old_groups))
    group = Group(name="New Name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
