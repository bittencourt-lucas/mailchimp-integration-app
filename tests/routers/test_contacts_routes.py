from routers.contacts_routes import contacts_router
from fastapi import APIRouter


def test_contacts_router_exists():
    assert contacts_router.__class__ is APIRouter
