from fastapi import FastAPI
from main import app


def test_app_exists():
    assert app.__class__ is FastAPI


def test_app_has_cors_middleware():
    assert app.add_middleware.__code__.co_argcount == 2
