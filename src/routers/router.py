from fastapi import APIRouter, HTTPException
import logging
from src.application.services.integration.sync_mockapi_contacts_service \
    import SyncMockApiMailchimpService


root_router = APIRouter()


@root_router.get('/contacts/sync')
async def sync_contacts():
    try:
        result = await SyncMockApiMailchimpService().execute()
        return {'success': True, 'data': result}
    except Exception as e:
        logging.error(f'Error: {e}')
        raise HTTPException(status_code=500, detail='Error syncing contacts')
