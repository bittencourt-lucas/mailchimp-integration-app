from fastapi import APIRouter, HTTPException
from src.application.models.sync_contacts_response import SyncContactsResponse
from src.application.models.sync_output import SyncOutput
import logging
from src.application.services.integration.sync_mockapi_contacts_service \
    import SyncMockApiMailchimpService


root_router = APIRouter()


@root_router.get('/contacts/sync')
async def sync_contacts() -> SyncContactsResponse:
    """
    Synchronize contacts using SyncMockApiMailchimpService.

    Returns a dictionary with 'success' and 'data' keys if successful.
    Logs error and raises HTTPException(500) if an exception occurs.
    """
    try:
        result: SyncOutput = await \
            SyncMockApiMailchimpService().execute()
        return {'success': True, 'data': result}
    except Exception as e:
        logging.error(f'Error: {e}')
        raise HTTPException(status_code=500, detail='Error syncing contacts')
