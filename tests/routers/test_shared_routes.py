from src.routers.router import root_router
from fastapi import APIRouter


def test_root_router_exists():
    assert root_router.__class__ is APIRouter
