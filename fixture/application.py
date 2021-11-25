from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:
    """Test class for initializing and drop object"""

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def destroy(self):
        self.driver.quit()
