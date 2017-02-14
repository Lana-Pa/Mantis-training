import pytest
import json
import os.path
from fixture.application import Application


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture  # create fixture for initialization with checking
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']  # use "web" block from target.json
    if fixture is None or not fixture.is_valid():  # check for fixture validness
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    return fixture

@pytest.fixture(scope="session", autouse=True) # create fixture for finalization
def stop(request):
    def fin():
        fixture.session.ensure_logout() #check for preconditions before logout
        fixture.destroy()
    request.addfinalizer(fin) # teardown function
    return fixture


# hook - add additional parameters to load tests from cmd
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")  # parameter, what to do, definition of the parameter
    parser.addoption("--target", action="store", default="target.json")
