from fastapi import APIRouter
from app.contacts.endpoints.routes.contacts_routes import contacts_router


root_router = APIRouter()

root_router.include_router(contacts_router)
