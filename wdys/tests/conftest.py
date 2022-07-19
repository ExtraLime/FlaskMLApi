import pytest
from wdys.app import create_app


@pytest.fixture(scope='session')
def app():

    params = {
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # Establish a context before running the tests

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
