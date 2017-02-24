from model.project import Project
from data.project_data import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(project)

    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == app.project.count()
    old_projects.append(project)

    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)

