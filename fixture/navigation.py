from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        if not self.check_home_page():
            self.app.driver.get("http://localhost/addressbook/")
            self.app.driver.set_window_size(1012, 691)

    def close_home_page(self):
        if self.check_home_page():
            self.app.driver.close()

    def check_groups_page(self):
        current_url = self.app.driver.current_url.endswith("/group.php")
        group_page_elements = self.app.driver.find_elements(By.NAME, "new")
        is_open = current_url and len(group_page_elements) > 0
        return is_open

    def open_groups_page(self):
        if not self.check_groups_page():
            self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def check_home_page(self):
        current_url = self.app.driver.current_url.endswith("")
        home_page_elements = self.app.driver.find_elements(By.NAME, "searchstring")
        is_open = current_url and len(home_page_elements) > 0
        return is_open

    def return_to_home_page(self):
        if not self.check_home_page():
            self.app.driver.find_element(By.LINK_TEXT, "home").click()
