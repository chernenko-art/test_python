from selenium.webdriver.common.by import By


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
        self.app.navigation.open_groups_page()
        self.select_first_group()
        self.app.driver.find_element(By.NAME, "delete").click()
        self.app.navigation.open_home_page()

    def modify_first_group(self, new_group_data):
        self.app.navigation.open_groups_page()
        self.select_first_group()
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.navigation.open_home_page()

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def count(self):
        self.app.navigation.open_groups_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))
