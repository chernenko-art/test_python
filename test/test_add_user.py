# -*- coding: utf-8 -*-
import pytest
from model.user import User
import random
import string


def random_string(prefix, maxlen):
    # generate string on letters, numbers symbols and spaces
    symbol = string.ascii_letters + string.digits + " "*10
    # generate string on random symbols and length
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

test_data = [
                User(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email="",
                  email2="", email3="", phone2="")
            ] + [
    User(firstname=random_string("firstname", 10), middlename=random_string("lastname", 10),
         lastname=random_string("lastname", 10), address=random_string("address", 10), home=random_string("home", 10),
         mobile=random_string("mobile", 10), work=random_string("work", 10), email=random_string("email", 10),
         email2=random_string("email2", 10), email3=random_string("email3", 10), phone2=random_string("phone2", 10))
]


@pytest.mark.parametrize("user", test_data, ids=[repr(x) for x in test_data])
def test_create_user(app, user):
    # get current user list
    old_user_list = app.user.get_contact_list()
    app.user.create(user)
    assert len(old_user_list) + 1 == app.user.count()
    # get new user list
    new_user_list = app.user.get_contact_list()
    # add new user
    old_user_list.append(user)
    assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
