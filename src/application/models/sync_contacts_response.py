from pydantic import BaseModel
from src.application.models.sync_output import SyncOutput


class SyncContactsResponse(BaseModel):
    success: bool
    data: SyncOutput
