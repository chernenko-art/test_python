from pytest_bdd import given, when, then
from model.group import Group
import random


@given("a group list", target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given("a group with <name>, <header> and <footer>", target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add the group to the list")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given("a non-empty group list", target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New name"))
    return db.get_group_list()


@given("a random group from the list", target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when("I delete the group from the list")
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then("the new group list is equal to the old list without the deleted group")
def verify_group_deleted(db, random_group, non_empty_group_list, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)