import os
import sys

import pytest

DEFAULT_ALLOWED_ORIGIN = "http://allowed.test"
os.environ.setdefault("CORS_ORIGINS", DEFAULT_ALLOWED_ORIGIN)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import create_app  # noqa: E402  pylint: disable=wrong-import-position


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def allowed_origin():
    return DEFAULT_ALLOWED_ORIGIN
