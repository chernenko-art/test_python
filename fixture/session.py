from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.navigation.open_home_page()
        self.app.driver.find_element(By.NAME, "user").click()
        self.app.driver.find_element(By.NAME, "user").send_keys(username)
        self.app.driver.find_element(By.ID, "LoginForm").click()
        self.app.driver.find_element(By.NAME, "pass").click()
        self.app.driver.find_element(By.NAME, "pass").send_keys(password)
        self.app.driver.find_element(By.ID, "LoginForm").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def ensure_login(self, username, password):
        if self.is_loggined() > 0:
            if self.check_loggined_name() != username:
                self.logout()
            else:
                return
        self.login(username, password)

    def check_loggined_name(self):
        return self.app.driver.find_element(By.XPATH, "//*[@id='top']/form/b").text[1:-1]

    def is_loggined(self):
        return len(self.app.driver.find_elements(By.LINK_TEXT, "Logout"))

    def logout(self):
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()
