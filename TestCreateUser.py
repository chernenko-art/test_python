# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By
from user import User


class TestCreateUser():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_CreateUser(self):
        send_test_user_params = User(firstname="Eva", middlename="Semenova", lastname="Cocs", nickname="Coca", title="Nocomments",
                                     company="Google", address="Russia", home="Moscow", mobile="169421+", work="Google",
                                     fax="14481561", email="eva@mail.ru", email2="no", email3="no", homepage="no",
                                     phone2="+89945669", bday=12, bmounth="'October'", byear="1991", aday="'25'",
                                     amonth="'November'", ayear="2015", address2="Rome", notes="No")
        self.login(username="admin", password="secret")
        self.create_user(send_test_user_params)
        self.logout()
        self.close_home_page()

    def close_home_page(self):
        self.driver.close()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

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

    def open_users_page(self):
        self.driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.ID, "LoginForm").click()
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.ID, "LoginForm").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1012, 691)
