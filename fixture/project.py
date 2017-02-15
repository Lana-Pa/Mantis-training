from model.project import Project
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects(self):
        wd = self.app.wd
        # if not (wd.current_url.endswith("/mantisbt-1.2.19/") and len(wd.find_elements_by_link_text("My View"))>0):
        #     wd.find_element_by_xpath("//a[@href=contains(text(),'My View')]").click()
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



    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//tr[@class='row-1']"):
                name = element.find_element_by_xpath(".//td[1]").text
                description = element.find_element_by_xpath(".//td[5]").text

                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)
