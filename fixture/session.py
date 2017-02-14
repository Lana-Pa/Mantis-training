class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    # method for checking if user was logged in
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    #method for checking correct username
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    # smart logout
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    # smart login
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in(): # if user is logged in than check for username
            if self.is_logged_in_as(username):
                return # if username is OK than Return this value
            else:      # if username is wrong, than login again with valid username
                self.logout()
        self.login(username, password) # we can use this line in both cases



