from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:
    """Test class for initializing and drop object"""

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def destroy(self):
        self.driver.quit()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1012, 691)

    def close_home_page(self):
        self.driver.close()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def open_users_page(self):
        self.driver.find_element(By.LINK_TEXT, "add new").click()

    def return_to_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").clear()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").clear()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").clear()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit created group
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def create_user(self, user):
        self.open_users_page()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(user.firstname)
        self.driver.find_element(By.NAME, "middlename").click()
        self.driver.find_element(By.NAME, "middlename").send_keys(user.middlename)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(user.lastname)
        self.driver.find_element(By.NAME, "nickname").click()
        self.driver.find_element(By.NAME, "nickname").send_keys(user.nickname)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys(user.title)
        self.driver.find_element(By.NAME, "company").click()
        self.driver.find_element(By.NAME, "company").send_keys(user.company)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(user.address)
        self.driver.find_element(By.NAME, "home").click()
        self.driver.find_element(By.NAME, "home").send_keys(user.home)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(user.mobile)
        self.driver.find_element(By.NAME, "work").click()
        self.driver.find_element(By.NAME, "work").send_keys(user.work)
        self.driver.find_element(By.NAME, "fax").click()
        self.driver.find_element(By.NAME, "fax").send_keys(user.fax)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(user.email)
        self.driver.find_element(By.NAME, "email2").click()
        self.driver.find_element(By.NAME, "email2").send_keys(user.email2)
        self.driver.find_element(By.NAME, "email3").click()
        self.driver.find_element(By.NAME, "email3").click()
        self.driver.find_element(By.NAME, "email3").send_keys(user.email3)
        self.driver.find_element(By.NAME, "homepage").click()
        self.driver.find_element(By.NAME, "homepage").click()
        self.driver.find_element(By.NAME, "homepage").send_keys(user.homepage)
        self.driver.find_element(By.NAME, "bday").click()
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = {user.bday}]").click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(14)").click()
        self.driver.find_element(By.NAME, "bmonth").click()
        dropdown = self.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = %s]" % user.bmounth).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(11)").click()
        self.driver.find_element(By.NAME, "byear").click()
        self.driver.find_element(By.NAME, "byear").send_keys(user.byear)
        self.driver.find_element(By.NAME, "aday").click()
        dropdown = self.driver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = %s]" % user.aday).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(27)").click()
        self.driver.find_element(By.NAME, "amonth").click()
        dropdown = self.driver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = %s]" % user.amonth).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(12)").click()
        self.driver.find_element(By.NAME, "ayear").click()
        self.driver.find_element(By.NAME, "ayear").send_keys(user.ayear)
        self.driver.find_element(By.NAME, "address2").click()
        self.driver.find_element(By.NAME, "address2").send_keys(user.address2)
        self.driver.find_element(By.NAME, "phone2").click()
        self.driver.find_element(By.NAME, "phone2").send_keys(user.phone2)
        self.driver.find_element(By.NAME, "notes").click()
        self.driver.find_element(By.NAME, "notes").send_keys(user.notes)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
