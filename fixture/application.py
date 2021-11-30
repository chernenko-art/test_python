from selenium import webdriver
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:
    """Test class for initializing and drop object"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def is_valid(self):
        try:
            assert self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
