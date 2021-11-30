# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    group_params = Group(name="Lol", header="Happy", footer="Gays")
    app.group.create(group_params)


def test_add_empty_group(app):
    group_params = Group(name="", header="", footer="")
    app.group.create(group_params)
