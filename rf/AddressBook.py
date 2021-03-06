from fixture.application import Application
import json
import os.path
from fixture.db import DbFixture
from model.group import Group
from model.user import User


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target["db"]
        self.dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                                   password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def modify_group(self, group):
        group_data = Group(name="modify_name")
        self.fixture.group.modify_group_by_id(group.id, group_data)

    def group_list_should_be_equal(self, old_groups, new_groups):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def new_user(self, firstname,  middlename,  lastname):
        return User(firstname=firstname,  middlename=middlename,  lastname=lastname)

    def get_user_list(self):
        return self.dbfixture.get_user_list()

    def create_user(self, user):
        self.fixture.user.create(user)

    def delete_user(self, user):
        self.fixture.user.delete_by_id(user.id)

    def modify_user(self, user):
        user_data = User(firstname="modify_firstname")
        self.fixture.user.modify_by_id(user.id, user_data)

    def user_list_should_be_equal(self, old_user_list, new_user_list):
        assert sorted(old_user_list, key=User.id_or_max) == sorted(new_user_list, key=User.id_or_max)
