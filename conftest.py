from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

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
    # get name browser(str) from cmd option (marker --browser)
    browser = request.config.getoption("--browser")
    # get data from json file (path to file getting from cmd option, marker --target)
    web_config = load_config(request.config.getoption("--target"))["web"]
    # validation fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


# fixture for data base
@pytest.fixture(scope="session")
def db(request):
    # get data from json file (path to file getting from cmd option, marker --target)
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                          password=db_config["password"])

    # finalizing db
    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


# fixture for data base ORM
@pytest.fixture(scope="session")
def ormdb(request):
    # get data from json file (path to file getting from cmd option, marker --target)
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = ORMFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])
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


# pytest hook - get params from cmd markers
def pytest_addoption(parser):
    # option for choice web browser
    parser.addoption("--browser", action="store", default="chrome")  # get value
    # option for get configuration from json file
    parser.addoption("--target", action="store", default="target.json")  # get path to json file
    # option for start ui tests
    parser.addoption("--check_ui", action="store_true")  # store_true: if option init - return True , another - False


# function for parametrise all test functions
def pytest_generate_tests(metafunc):  # metafunc - info about all fixtures
    for fixture in metafunc.fixturenames:  # find your fixture
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])  # load data from file(where name beginning after 5 symbols)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])  # where, from, presentation
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# import testdata from module
def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata  # path to module data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.json")) as f:  # path to json file
        return jsonpickle.decode(f.read())
