from selenium import webdriver
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:
    """Test class for initializing and drop object"""

    def __init__(self, browser, base_url):
        # choice browser driver
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.vars = {}
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            assert self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
