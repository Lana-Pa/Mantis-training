from model.project import Project
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        element = WebDriverWait(wd, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.menu")))
        self.project_cache = None

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']//td/a")[index].click()


    def delete_project(self, index):
        wd = self.app.wd
        self.open_projects()
        self.select_project_by_index(index)
        wd.find_element_by_xpath("//div[@class='border center']//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//div[@align='center']//input[@value='Delete Project']").click()
        element = WebDriverWait(wd, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.menu")))
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects()
            self.project_cache = []

            rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']")
            for element in rows:
                name = element.find_element_by_xpath(".//td[1]/a").text
                description = element.find_element_by_xpath(".//td[5]").text
                self.project_cache.append(Project(name=name, description=description))
            return list(self.project_cache)


    def count(self):
        wd = self.app.wd
        self.open_projects()
        return len(wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']//td/a"))

