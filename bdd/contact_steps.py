from pytest_bdd import given, when, then
from model.user import User
import random


@given("a user list", target_fixture="user_list")
def user_list(db):
    return db.get_user_list()


@given("a user with <firstname>, <lastname> and <middlename>", target_fixture="new_user")
def new_user(db, firstname, lastname, middlename):
    return User(firstname="firstname", lastname="lastname", middlename="middlename")


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
