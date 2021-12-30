from pytest_bdd import given, when, then
from model.user import User
import random


@given("a user list", target_fixture="user_list")
def user_list(db):
    return db.get_user_list()


@given("a user with <firstname>, <lastname> and <middlename>", target_fixture="new_user")
def new_user(db, firstname, lastname, middlename):
    return User(firstname=firstname, lastname=lastname, middlename=middlename)


@when("I add the user to the list", target_fixture="add_user")
def add_user(app, new_user):
    app.user.create(new_user)


@then("the new user list is equal to the old list with the added user")
def verify_user_added(db, app, new_user, user_list, check_ui):
    old_user_list = user_list
    new_user_list = db.get_user_list()
    old_user_list.append(new_user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)


@given("a non-empty user list", target_fixture="non_empty_user_list")
def non_empty_user_list(db, app):
    if len(db.get_user_list()) == 0:
        app.user.create(User(firstname="New name"))
    return db.get_user_list()


@given("a random user from the list", target_fixture="random_user")
def random_user(non_empty_user_list):
    return random.choice(non_empty_user_list)


@when("I delete the user from the list")
def delete_user(app, random_user):
    app.user.delete_by_id(random_user.id)


@then("the new user list is equal to the old list without the deleted user")
def verify_user_deleted(db, random_user, non_empty_user_list, app, check_ui):
    old_user_list = non_empty_user_list
    new_user_list = db.get_user_list()
    old_user_list.remove(random_user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)


@when("I modify the user from the list", target_fixture="modify_user")
def modify_user(app, random_user):
    user = User(firstname="Alarm!", lastname="Alarm!")
    app.user.modify_by_id(random_user.id, user)
    return user


@then("the new user list is equal to the old list with modified user")
def verify_user_modified(app, db, non_empty_user_list, random_user, modify_user, check_ui):
    old_user_list = non_empty_user_list
    new_user_list = db.get_user_list()
    modify_user.id = random_user.id
    old_user_list.remove(random_user)
    old_user_list.append(modify_user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
    if check_ui:
        assert sorted(new_user_list, key=User.id_or_max) == sorted(app.user.get_contact_list(), key=User.id_or_max)
