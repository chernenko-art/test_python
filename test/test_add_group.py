# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    group_params = Group(name="Lol", header="Happy", footer="Gays")
    old_groups = app.group.get_group_list()
    app.group.create(group_params)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    group_params = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group_params)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
