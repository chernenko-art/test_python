from model.user import User
import random


def test_add_contact_in_group(app, ormdb, json_groups, json_users):
    group = json_groups
    user = json_users
    if len(ormdb.get_group_list()) == 0:
        app.group.create(group)
    if len(ormdb.get_contact_list()) == 0:
        app.user.create(user)
    group = random.choice(ormdb.get_group_list())
    user = random.choice(ormdb.get_contact_list())
    if user in ormdb.get_contacts_in_group(group):
        app.user.del_user_from_group(user, group)
    old_contact_list_in_group = ormdb.get_contacts_in_group(group)
    app.user.add_user_in_group(user, group)
    new_contacts_list_in_group = ormdb.get_contacts_in_group(group)
    old_contact_list_in_group.append(user)
    assert sorted(old_contact_list_in_group, key=User.id_or_max) == sorted(new_contacts_list_in_group,
                                                                           key=User.id_or_max)
