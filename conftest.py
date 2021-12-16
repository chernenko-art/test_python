from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


fixture = None
target = None


# help functions for load config
def load_config(file):
    global target
    if target is None:
        # absolut path to file target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        # load data from json
        with open(config_file) as f:
            target = json.load(f)
    return target


# fixture for web
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    # validation target file for web configuration
    web_config = load_config(request.config.getoption("--target"))["web"]
    # validation fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


# fixture for data base
@pytest.fixture(scope="session")
def db(request):
    # validation target file for db configuration
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    # finalizing db
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


#  finalizing web fixture
@pytest.fixture(scope="session", autouse=True)  # autouse - automatic start fixture
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# hook for get params from cmd
def pytest_addoption(parser):
    # description options
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")  # store_true - return True if option init, another - False


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


