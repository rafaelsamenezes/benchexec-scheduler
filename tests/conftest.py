import sys, os
import tempfile

import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from scheduler import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def default_create_app():
    return create_app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

