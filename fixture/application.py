from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


# constructor
class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(3) # this option is needed to wait until elements will be loaded
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url


    # check if the browser is opened
    def is_valid(self):
        try:
            self.wd.current_url  # check for example what the url is now opened
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

