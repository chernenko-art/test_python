class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        self.app.driver.get("http://localhost/addressbook/")
        self.app.driver.set_window_size(1012, 691)

    def close_home_page(self):
        self.app.driver.close()