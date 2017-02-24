from random import randrange
from model.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    if app.project.count() == 0:
        app.project.create(Project(name="test", descriprion="test"))

    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project(index)

    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_project_list()

    old_projects[index:index + 1] = []
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)

