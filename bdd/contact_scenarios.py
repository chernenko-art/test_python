from pytest_bdd import scenario
from .contact_steps import *


@scenario("contact.feature", "Add new user")
def test_add_user():
    pass


@scenario("contact.feature", "Delete a user")
def test_delete_user():
    pass


@scenario("contact.feature", "Modify a user")
def test_modify_user():
    pass
