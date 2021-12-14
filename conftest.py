from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle


fixture = None
target = None


# fixture for initializing
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    # validation target file
    if target is None:
        # absolut path to file target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    # validation fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


# fixture for finalizing
@pytest.fixture(scope="session", autouse=True)  # autouse - automatic start fixture
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# hook for get params from cmd
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


# function for parametrise all test functions
def pytest_generate_tests(metafunc):  # metafunc - get info about test functions
    for fixture in metafunc.fixturenames:  # get info about test functions fixture
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])  # load data from file(name)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])  # where, from, presentation
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# import testdata from module
def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.json")) as f:  # path to json file
        return jsonpickle.decode(f.read())
