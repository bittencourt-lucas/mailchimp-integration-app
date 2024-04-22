from typing import List
from pydantic import BaseModel
from src.application.models.sync_contact import SyncContact


class SyncOutput(BaseModel):
    synced_contacts: int
    contacts: List[SyncContact]
