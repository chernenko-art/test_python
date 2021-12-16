# -*- coding: utf-8 -*-
from model.group import Group
import random
from random import randrange


def test_modify_group_name(app, db, json_groups, check_ui):
    # check what groups is not empty
    if len(db.get_group_list()) == 0:
        group = json_groups
        app.group.create(group)
    old_groups = db.get_group_list()
    # choice random group for modify
    group_random = random.choice(old_groups)
    group = Group(name="New Name")
    group.id = group_random.id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(group_random)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
