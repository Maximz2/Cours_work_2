import pytest
from flask import Flask

from application.app import creat_app


@pytest.fixture()
def app():
    app: Flask = creat_app()
    app.config["TESTING"] = True

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
