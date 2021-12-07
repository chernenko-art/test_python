from selenium.webdriver.common.by import By
from model.user import User

class UserHelper:

    def __init__(self, app):
        self.app = app

    def add_new_user(self):
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()

    def create(self, user):
        self.add_new_user()
        self.fill_user_form(user)
        # save changes
        self.app.driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.app.navigation.return_to_home_page()


    def change_field_value(self, field_name, text):
        if text is not None:
            # check text field
            if field_name not in ["bday", "bmonth", "aday", "amonth"]:
                self.app.driver.find_element(By.NAME, field_name).click()
                self.app.driver.find_element(By.NAME, field_name).clear()
                self.app.driver.find_element(By.NAME, field_name).send_keys(text)
            # check dropdown list
            else:
                self.app.driver.find_element(By.NAME, field_name).click()
                dropdown = self.app.driver.find_element(By.NAME, field_name)
                dropdown.find_element(By.XPATH, "//option[. = %s]" % text).click()

    def fill_user_form(self, user):
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("fax", user.fax)
        self.change_field_value("email", user.email)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)
        self.change_field_value("homepage", user.homepage)
        self.change_field_value("bday", user.bday)
        self.change_field_value("bmonth", user.bmonth)
        self.change_field_value("byear", user.byear)
        self.change_field_value("aday", user.aday)
        self.change_field_value("amonth", user.amonth)
        self.change_field_value("ayear", user.ayear)
        self.change_field_value("address2", user.address2)
        self.change_field_value("phone2", user.phone2)
        self.change_field_value("notes", user.notes)

    def delete(self):
        # select first user
        self.app.driver.find_element(By.NAME, "selected[]").click()
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm changes
        self.app.driver.switch_to.alert.accept()
        self.app.navigation.return_to_home_page()

    def modify(self, user):
        # open modify form for first user
        self.app.driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_user_form(user)
        # save changes
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.navigation.return_to_home_page()

    def count(self):
        self.app.navigation.return_to_home_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    def get_user_list(self):
        self.app.navigation.return_to_home_page()
        user_list = []
        find_user_list = self.app.driver.find_element(By.ID, "maintable").find_elements(By.NAME, "entry")
        for user in find_user_list:
            user_params_list = user.find_elements(By.TAG_NAME, "td")
            first_name = user_params_list[2].text
            last_name = user_params_list[1].text
            user_id = user_params_list[0].find_element(By.NAME, "selected[]").get_attribute("value")
            user_list.append(User(firstname=first_name, lastname=last_name, id=user_id))
        return user_list
