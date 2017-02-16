from model.project import Project
from data.project_data import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.create(project)

    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(new_projects, key=Project.max) == sorted(app.project.get_project_list(), key=Project.max)

