from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_home_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "home").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit created group
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

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
        self.open_groups_page()
        self.select_first_group()
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_home_page()

    def modify_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()
