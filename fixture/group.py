from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.app.navigation.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit created group
        self.app.driver.find_element(By.NAME, "submit").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        self.app.driver.find_element(By.NAME, "delete").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        self.app.driver.find_element(By.NAME, "delete").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        self.app.driver.find_element(By.CSS_SELECTOR, f"input[value='{id}']").click()

    def count(self):
        self.app.navigation.open_groups_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.app.navigation.open_groups_page()
            self.group_cache = []
            find_group_list = self.app.driver.find_elements(By.CSS_SELECTOR, "span.group")
            for element in find_group_list:
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        # return copy group_cache
        return list(self.group_cache)
