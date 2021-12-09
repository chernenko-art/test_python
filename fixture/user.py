from selenium.webdriver.common.by import By
from model.user import User
import re


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
        self.app.navigation.go_to_home_page()
        self.user_cache = None


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
        # delete first user
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.select_user_by_index(index)
        # delete user
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm changes
        self.app.driver.switch_to.alert.accept()
        self.app.navigation.go_to_home_page()
        self.user_cache = None

    def select_user_by_index(self, index):
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()

    def modify(self, user):
        # modify first user
        self.modify_by_index(0, user)

    def modify_by_index(self, index, user):
        self.open_form_to_modify(index)
        self.fill_user_form(user)
        # save changes
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.navigation.go_to_home_page()
        self.user_cache = None

    def open_form_to_modify(self, index):
        self.app.navigation.go_to_home_page()
        self.app.driver.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_form_by_view(self, index):
        self.app.navigation.go_to_home_page()
        self.app.driver.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def count(self):
        self.app.navigation.go_to_home_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    user_cache = None

    def get_contact_list(self):
        self.app.navigation.go_to_home_page()
        if self.user_cache is None:
            self.user_cache = []
            find_user_list = self.app.driver.find_element(By.ID, "maintable").find_elements(By.NAME, "entry")
            for user in find_user_list:
                user_params_list = user.find_elements(By.TAG_NAME, "td")
                first_name = user_params_list[2].text
                last_name = user_params_list[1].text
                user_id = user_params_list[0].find_element(By.NAME, "selected[]").get_attribute("value")
                # get all phones in str
                all_phones = user_params_list[5].text
                self.user_cache.append(User(firstname=first_name, lastname=last_name,
                                            id=user_id, all_phones_from_page=all_phones))
        # return copy user_cache
        return list(self.user_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_form_to_modify(index)
        firstname = self.app.driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = self.app.driver.find_element(By.NAME, "lastname").get_attribute("value")
        user_id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = self.app.driver.find_element(By.NAME, "home").get_attribute("value")
        workphone = self.app.driver.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = self.app.driver.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = self.app.driver.find_element(By.NAME, "phone2").get_attribute("value")
        return User(firstname=firstname, lastname=lastname, id=user_id, home=homephone, work=workphone,
                    mobile=mobilephone, phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        self.open_form_by_view(index)
        # get all text on page
        text = self.app.driver.find_element(By.ID, "content").text
        # get all phones on page with Fax number
        phones_with_fax = "".join(text.split('\n\n')[1])
        # delete Fax number
        phones_without_fax = re.sub("F.*", "", phones_with_fax)
        secondaryphone = text.split('\n\n')[5]
        all_phones = phones_without_fax + secondaryphone
        return User(all_phones_from_page=all_phones)
