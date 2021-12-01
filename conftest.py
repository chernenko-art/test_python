from fixture.application import Application
import pytest


fixture = None


def initializing_fixture():
    global fixture
    fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        initializing_fixture()
    else:
        if not fixture.is_valid():
            initializing_fixture()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
