from fastapi import APIRouter
from src.application.services.integration.sync_mockapi_contacts_service \
    import SyncMockApiMailchimpService


root_router = APIRouter()


@root_router.get('/contacts/sync')
async def sync_contacts():
    return await SyncMockApiMailchimpService().execute()
